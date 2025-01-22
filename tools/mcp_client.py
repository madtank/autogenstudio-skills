"""
Dynamic MCP (Model Context Protocol) client that provides access to various server capabilities.

This tool follows a discovery-first approach. To use it effectively:

1. List available servers:
   await mcp(tool='list_available_servers')

2. Discover tools for a specific server:
   await mcp(server='server_name', tool='tool_details')

3. Execute a specific tool:
   await mcp(
       server='server_name',
       tool='tool_name',
       arguments={'param1': 'value1', 'param2': 'value2'}
   )

Common Examples:
- Web Search: 
  await mcp(server='brave-search', tool='brave_web_search', arguments={'query': 'search terms'})
- File Operations:
  await mcp(server='filesystem', tool='read_file', arguments={'path': '/path/to/file'})

Always check tool availability and details before use as capabilities may change.
"""

async def mcp(server: str = None, tool: str = None, arguments: dict = None):
    """
    Dynamic MCP client that adapts to available server capabilities.
    
    Args:
        server: Name of the MCP server to use
        tool: Name of the tool to execute or special commands:
              - 'list_available_servers': List available servers
              - 'tool_details': Get tool information for a server
        arguments: Dictionary of tool-specific arguments
    
    Returns:
        Tool execution results or discovery information
    """
    try:
        import json
        import asyncio
        import os
        import platform
        from pathlib import Path
        from mcp import ClientSession, StdioServerParameters
        from mcp.client.stdio import stdio_client

        # Check multiple config locations
        possible_paths = [
            Path('mcp_config.json'),  # Current directory
            Path.home() / '.config' / 'autogen' / 'mcp_config.json',  # User config dir
            Path(os.getenv('MCP_CONFIG_PATH', 'mcp_config.json')),  # Environment variable
        ]

        config_path = None
        for path in possible_paths:
            if path.exists():
                config_path = path
                break

        if not config_path:
            paths_checked = '\n'.join(str(p) for p in possible_paths)
            return f"Error: No configuration file found. Checked:\n{paths_checked}"

        # Get system-specific npx path
        system = platform.system()
        if system == "Darwin":  # macOS
            default_npx = Path("/opt/homebrew/bin/npx")
        elif system == "Windows":
            default_npx = Path(os.getenv("APPDATA")) / "npm/npx.cmd"
        else:  # Linux and others
            default_npx = Path("/usr/local/bin/npx")

        # Find npx in PATH if default doesn't exist
        npx_path = str(default_npx if default_npx.exists() else "npx")

        # Load config
        with open(config_path) as f:
            config_data = json.load(f)
            servers = config_data.get('mcpServers', {})

        # Handle list_available_servers
        if tool == 'list_available_servers':
            enabled_servers = [name for name, cfg in servers.items() if cfg.get('enabled', True)]
            return json.dumps(enabled_servers, indent=2)

        # Validate server
        if not server:
            return "Error: Server parameter required for tool operations"
        if server not in servers:
            return f"Error: Server {server} not found"
        if not servers[server].get('enabled', True):
            return f"Error: Server {server} is disabled in configuration"

        # Build server connection
        config = servers[server]
        command = npx_path if config['command'] == 'npx' else config['command']
        env = os.environ.copy()
        env.update(config.get('env', {}))

        arguments = arguments or {}

        # Connect to server and execute tool
        async with stdio_client(StdioServerParameters(
            command=command, 
            args=config.get('args', []), 
            env=env
        )) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()

                # Handle tool_details
                if tool == 'tool_details':
                    result = await session.list_tools()
                    return json.dumps([{
                        'name': t.name,
                        'description': t.description,
                        'input_schema': t.inputSchema
                    } for t in result.tools], indent=2)

                # Execute requested tool
                if not tool:
                    return "Error: Tool name required"

                result = await session.call_tool(tool, arguments=arguments)
                return str(result)

    except Exception as e:
        return f"Error: {str(e)}"