async def mcp(server: str, tool: str, query: str = None, path: str = None, input: str = None, memoryId: str = None) -> str:
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

        with open(config_path) as f:
            servers = json.load(f).get('mcpServers', {})

        if server not in servers:
            return f"Error: Server {server} not found"

        # Build server config
        config = servers[server]
        command = npx_path if config['command'] == 'npx' else config['command']
        env = os.environ.copy()
        env.update(config.get('env', {}))

        # Build arguments based on tool
        args = {}
        if tool == "brave_web_search" and query:
            args['query'] = query
        elif tool == "ask_agent":
            if input:
                args['input'] = input
            if memoryId:
                args['memoryId'] = memoryId

        # Execute tool
        async with stdio_client(StdioServerParameters(command=command, args=config.get('args', []), env=env)) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                result = await session.call_tool(tool, arguments=args)
                return str(result)

    except Exception as e:
        return f"Error: {str(e)}"