"""
MCP (Model Context Protocol) Tool Implementation
Provides a unified interface for accessing various server-based tools including:
- Filesystem operations (read, write, edit, search files)
- Web search capabilities (via Brave Search)
- Server discovery and tool inspection

The MCP function acts as a bridge between the client application and various 
server implementations, handling configuration, command execution, and error handling.
"""

async def mcp(
    server: str = None,
    tool: str = None,
    query: str = None,
    path: str = None,
    count: int = None,
    content: str = None,
    edits: list = None,
    paths: list = None,
    source: str = None,
    destination: str = None,
    pattern: str = None,
    excludePatterns: list = None,
    dryRun: bool = None
) -> str:
    """MCP (Model Context Protocol) provides access to various tools and servers.
    Before using any tools, you should:

    1. List available servers:
        mcp(tool='list_available_servers')

    2. Get details about tools on a server:
        mcp(server='server_name', tool='tool_details')

    Main servers include:
    - filesystem: For file operations 
    - brave-search: For web search capabilities

    File Operations:
    - read_file(path: str)
    - read_multiple_files(paths: list)
    - write_file(path: str, content: str)
    - edit_file(path: str, edits: list, dryRun: bool = False)
    - create_directory(path: str)
    - list_directory(path: str)
    - directory_tree(path: str)
    - move_file(source: str, destination: str)
    - search_files(path: str, pattern: str, excludePatterns: list = [])
    - get_file_info(path: str)
    - list_allowed_directories()

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

        # Get config path relative to the project root
        current_dir = Path(__file__).parent
        project_root = current_dir.parent
        config_path = project_root / "mcp_config.json"

        if not config_path.exists():
            example_path = project_root / "mcp_config.example.json"
            if example_path.exists():
                return f"Error: No configuration file found. Please copy {example_path} to {config_path} and update with your settings."
            return f"Error: No configuration file found at {config_path}"

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

        # Handle special tool cases first
        if tool == 'list_available_servers':
            # Only return enabled servers
            enabled_servers = [name for name, cfg in servers.items() if cfg.get('enabled', True)]
            return json.dumps(enabled_servers, indent=2)

        # Require server parameter for all other operations
        if not server:
            return "Error: Server parameter required for tool operations"
        if server not in servers:
            return f"Error: Server {server} not found"
        if not servers[server].get('enabled', True):
            return f"Error: Server {server} is disabled in configuration"

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
        if content is not None:
            args['content'] = content
        if edits is not None:
            args['edits'] = edits
        if paths is not None:
            args['paths'] = paths
        if source is not None:
            args['source'] = source
        if destination is not None:
            args['destination'] = destination
        if pattern is not None:
            args['pattern'] = pattern
        if excludePatterns is not None:
            args['excludePatterns'] = excludePatterns
        if dryRun is not None:
            args['dryRun'] = dryRun

        # Execute tool
        async with stdio_client(StdioServerParameters(command=command, args=config.get('args', []), env=env)) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                result = await session.call_tool(tool, arguments=args)
                return str(result)

    except Exception as e:
        return f"Error: {str(e)}"