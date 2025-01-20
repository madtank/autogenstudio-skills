{
  "version": "1.0.0",
  "component_type": "team",
  "name": "new_team_1737352488588",
  "participants": [
    {
      "component_type": "agent",
      "name": "assistant_agent",
      "agent_type": "AssistantAgent",
      "system_message": "You are a helpful assistant. Solve tasks carefully. You have a tool called MCP, this is USB for llm context, it's a set of tools. You will be asked to do MCP tools tests and validate the different options you can use with them. When the task is done respond with TERMINATE.",
      "model_client": {
        "component_type": "model",
        "model": "gpt-4o-2024-08-06",
        "model_type": "OpenAIChatCompletionClient"
      },
      "tools": [
        {
            "component_type": "tool",
            "name": "mcp",
            "description": "Access MCP (Model Context Protocol) servers with focus on two key capabilities:\n\n1. Web Search (Brave Search)\n   - Search the web for information\n   Example: mcp(server='brave-search', tool='brave_web_search', query='What is MCP?', count=3)\n\n2. File Operations\n   - List allowed directories\n   - List directory contents\n   - Read files\n   - Get file info\n   Example: mcp(server='filesystem', tool='read_file', path='/path/to/file')\n\nAllowed Directories:\n- /Users/jacob/claude_home\n- /Users/jacob/Library/Application Support/Claude",
            "content": "async def mcp(server: str, tool: str, query: str = None, path: str = None, count: int = None) -> str:\n    try:\n        import json\n        import asyncio\n        import os\n        import platform\n        from pathlib import Path\n        from mcp import ClientSession, StdioServerParameters\n        from mcp.client.stdio import stdio_client\n\n        # Get system-specific config path\n        system = platform.system()\n        home = Path.home()\n        \n        if system == \"Darwin\":  # macOS\n            config_path = home / \"Library/Application Support/Claude/claude_desktop_config.json\"\n            default_npx = Path(\"/opt/homebrew/bin/npx\")\n        elif system == \"Windows\":\n            config_path = Path(os.getenv(\"APPDATA\")) / \"Claude/claude_desktop_config.json\"\n            default_npx = Path(os.getenv(\"APPDATA\")) / \"npm/npx.cmd\"\n        else:  # Linux and others\n            config_path = home / \".config/Claude/claude_desktop_config.json\"\n            default_npx = Path(\"/usr/local/bin/npx\")\n\n        # Find npx in PATH if default doesn't exist\n        npx_path = str(default_npx if default_npx.exists() else \"npx\")\n\n        with open(config_path) as f:\n            servers = json.load(f).get('mcpServers', {})\n\n        if server not in servers:\n            return f\"Error: Server {server} not found\"\n\n        # Build server config\n        config = servers[server]\n        command = npx_path if config['command'] == 'npx' else config['command']\n        env = os.environ.copy()\n        env.update(config.get('env', {}))\n\n        # Build arguments based on tool\n        args = {}\n        if path is not None:\n            args['path'] = path\n        if query is not None:\n            args['query'] = query\n        if count is not None:\n            args['count'] = count\n\n        # Execute tool\n        async with stdio_client(StdioServerParameters(command=command, args=config.get('args', []), env=env)) as (read, write):\n            async with ClientSession(read, write) as session:\n                await session.initialize()\n                result = await session.call_tool(tool, arguments=args)\n                return str(result)\n\n    except Exception as e:\n        return f\"Error: {str(e)}\"",
            "tool_type": "PythonFunction"
        }
      ]
    }
  ],
  "team_type": "RoundRobinGroupChat",
  "termination_condition": {
    "component_type": "termination",
    "termination_type": "TextMentionTermination",
    "text": "TERMINATE"
  }
}