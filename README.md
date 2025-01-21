# AutoGen Studio MCP Tools

## What is MCP?

Model Context Protocol (MCP) is like a USB for AI tools - it provides a standardized way for AI agents to discover and use different capabilities. Think of it as plugging in new abilities for your AI agents! For more information about available MCP servers and capabilities, check out the [MCP Servers Repository](https://github.com/modelcontextprotocol/servers).

## Core Features

Currently focused on two powerful capabilities:

### 1. Brave Search
```python
# Get information from the web
result = await mcp(
    server="brave-search",
    tool="brave_web_search",
    query="Latest AI developments",
    count=5
)
```

### 2. File Operations
```python
# List allowed directories
dirs = await mcp(
    server="filesystem",
    tool="list_allowed_directories"
)

# Read file contents
content = await mcp(
    server="filesystem",
    tool="read_file",
    path="/path/to/file"
)
```

## Discovery-First Design

Our implementation emphasizes self-discovering tools. AI agents can:

1. List available servers:
```python
servers = await mcp(tool='list_available_servers')
```

2. Learn about tools:
```python
tools = await mcp(server='server_name', tool='tool_details')
```

## Configuration

Create a `mcp_config.json` file based on the provided example:
```json
{
  "mcpServers": {
    "brave-search": {
      "enabled": true,
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-brave-search"
      ],
      "env": {
        "BRAVE_API_KEY": "your-api-key-here"
      }
    },
    "filesystem": {
      "enabled": true,
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/path/to/your/working/directory"
      ]
    }
  }
}
```

## Gallery & Teams

The repository includes example configurations for AutoGen Studio:

- `gallerys/`: Example tool configurations and templates
- `teams/`: Pre-configured agent teams that work with MCP tools

## Development

### Testing
Run the test suite:
```bash
python tests/test_tools.py
```

### Adding New Tools
1. Update `mcp_tool.py` with new functionality
2. Add tests in `tests/test_mcp.py`
3. Update integration in `tools/mcp.json`
4. Add examples to gallery if appropriate

## Best Practices

- Always check tool availability before use
- Get tool details to understand capabilities
- Provide clear summaries of tool results to users
- Handle errors gracefully

## Requirements

- Python 3.12+
- Node.js and npx
- MCP Python SDK

## License

MIT License - See LICENSE file for details