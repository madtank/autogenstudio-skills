# AutoGen Studio MCP Tools

## What is MCP?

Model Context Protocol (MCP) is like a USB for AI tools - it provides a standardized way for AI agents to discover and use different capabilities. Think of it as plugging in new abilities for your AI agents! With our flexible dictionary-based implementation, agents can easily discover and use tools without needing to know their implementation details.

### Available MCP Servers

The MCP ecosystem is growing rapidly with many powerful servers available:

- **Brave Search** - Web and local search capabilities
- **Filesystem** - Complete file and directory operations
- **Playwright** - Browser automation and web scraping
- **MongoDB** - Direct database interactions
- **Sequential Thinking** - Structured reasoning and planning
- **FLUX** - Image generation and manipulation
- **Selenium** - Web automation and testing
- **SQLite** - Local database operations
- **Vector Store** - Embedding and similarity search
- **And many more!**

Check out the [MCP Servers Repository](https://github.com/modelcontextprotocol/servers) for the latest list of available servers. The ecosystem is rapidly growing with new capabilities being added regularly!

## Quick Start

1. **Install Requirements**:
```bash
# Create and activate virtual environment
python -m venv .env
source .env/bin/activate  # On Windows: .env\Scripts\activate

# Install required packages
pip install mcp
```

2. **Configure MCP**:
```bash
# Copy the example config
cp mcp_config.example.json mcp_config.json

# Edit mcp_config.json with your settings
{
  "mcpServers": {
    "brave-search": {
      "enabled": true,
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
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

3. **Start AutoGen Studio**:
```bash
autogenstudio ui --port 8080
```

## Dynamic Tool Usage

Our implementation uses a flexible dictionary-based approach, making it easy to discover and use tools:

```python
# 1. List Available Servers
servers = await mcp(tool='list_available_servers')

# 2. Discover Server Tools
tools = await mcp(
    server='brave-search',
    tool='tool_details'
)

# 3. Use Tools with Dictionary Arguments
# Web Search Example
result = await mcp(
    server='brave-search',
    tool='brave_web_search',
    arguments={
        'query': 'Latest AI developments',
        'count': 5
    }
)

# File Operations Example
result = await mcp(
    server='filesystem',
    tool='read_file',
    arguments={
        'path': '/path/to/your/file'
    }
)
```

## Example Templates

We provide ready-to-use templates to help you get started:

1. **Gallery Examples** (`/gallerys`):
   - Pre-configured tool setups
   - Example implementations
   - Best practices demonstrations

2. **Team Templates** (`/teams`):
   - Complete agent workflows
   - Tool integration examples
   - Task-specific configurations

To use a template:
1. Copy the desired template from `/gallerys` or `/teams`
2. Customize the JSON configuration for your needs
3. Load it in AutoGen Studio

## Available Tools

### 1. Brave Search
- Web search capabilities
- Local business search
- Configurable result limits
- Fresh content filtering

### 2. File Operations
- Read/Write files
- Directory operations
- File searches
- Metadata operations

### 3. More Coming Soon
The MCP ecosystem is constantly growing. Add new servers to your config to expand capabilities!

## Configuration Locations

The MCP client checks these locations for config files:

1. Current directory: `./mcp_config.json`
2. User config: `~/.config/autogen/mcp_config.json`
3. Environment: `$MCP_CONFIG_PATH`

## Development

### Testing
Run the test suite:
```bash
pytest tests/test_mcp_client.py -v
pytest tests/test_mcp_json.py -v
```

### Workspace
The `/mcp_workspace` directory is provided for testing but ignored by git. Your tests will create this automatically.

## Requirements

- Python 3.12+
- Node.js and npx
- MCP Python SDK
- AutoGen Studio

## License

MIT License - See LICENSE file for details