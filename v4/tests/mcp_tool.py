async def mcp(server: str = None, tool: str = None, query: str = None, path: str = None, count: int = None) -> str:
    """MCP (Model Context Protocol) provides access to various tools and servers.
Before using any tools, you should:

1. List available servers:
    mcp(tool='list_available_servers')

2. Get details about tools on a server:
    mcp(server='server_name', tool='tool_details')

Main servers include:
- filesystem: For file operations 
- brave-search: For web search capabilities

IMPORTANT:
1. Always check tool details before use to understand required parameters
   and proper usage. Do not make assumptions about how tools work - use tool_details
   to verify the correct parameters and format.

2. The user cannot see the raw tool results - you must always provide a clear summary
   of what the tool did and what was found. For example:
   - When reading a file: Explain what was in the file
   - When searching: Summarize the search results
   - When listing directories: Describe what was found

Never just execute a tool without explaining its results to the user. Always interpret
and explain the output in a way that's meaningful to the user.
"""
    try:
        import json
        import asyncio
        import os
        import platform
        from pathlib import Path
        from mcp import ClientSession, StdioServerParameters
        from mcp.client.stdio import stdio_client

        # Get system-specific config path
        system = platform.system()
        home = Path.home()
        
        if system == "Darwin":  # macOS
            config_path = home / "Library/Application Support/Claude/claude_desktop_config.json"
            default_npx = Path("/opt/homebrew/bin/npx")
        elif system == "Windows":
            config_path = Path(os.getenv("APPDATA")) / "Claude/claude_desktop_config.json"
            default_npx = Path(os.getenv("APPDATA")) / "npm/npx.cmd"
        else:  # Linux and others
            config_path = home / ".config/Claude/claude_desktop_config.json"
            default_npx = Path("/usr/local/bin/npx")

        # Find npx in PATH if default doesn't exist
        npx_path = str(default_npx if default_npx.exists() else "npx")

        # Load config
        with open(config_path) as f:
            servers = json.load(f).get('mcpServers', {})

        # Handle special tool cases first
        if tool == 'list_available_servers':
            return json.dumps(list(servers.keys()), indent=2)

        # Require server parameter for all other operations
        if not server:
            return "Error: Server parameter required for tool operations"
        if server not in servers:
            return f"Error: Server {server} not found"

        # Build server config
        config = servers[server]
        command = npx_path if config['command'] == 'npx' else config['command']
        env = os.environ.copy()
        env.update(config.get('env', {}))

        if tool == 'tool_details':
            async with stdio_client(StdioServerParameters(
                command=command,
                args=config.get('args', []),
                env=env
            )) as (read, write):
                async with ClientSession(read, write) as session:
                    await session.initialize()
                    result = await session.list_tools()
                    return json.dumps([{
                        'name': tool.name,
                        'description': tool.description,
                        'input_schema': tool.inputSchema
                    } for tool in result.tools], indent=2)

        # Build arguments based on tool
        args = {}
        if path is not None:
            args['path'] = path
        if query is not None:
            args['query'] = query
        if count is not None:
            args['count'] = count

        # Execute tool
        async with stdio_client(StdioServerParameters(command=command, args=config.get('args', []), env=env)) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                result = await session.call_tool(tool, arguments=args)
                return str(result)

    except Exception as e:
        return f"Error: {str(e)}"