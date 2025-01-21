# AutoGen Studio Tools

## What is MCP and Why We Use It

Model Context Protocol (MCP) is like a USB port for AI tools - it provides a standardized way for AI agents to discover and use different capabilities. We chose MCP for AutoGen Studio because it enables a "discovery-first" approach where agents can:

1. List available tools (like looking in a toolbox)
2. Learn about each tool's capabilities (reading the manual)
3. Use tools effectively based on their understanding

### Quick Start

Getting started is as simple as installing the tools you want to use:
```bash
# Install the Brave Search tool
npx @michaellatman/mcp-get@latest install @modelcontextprotocol/server-brave-search

# Install the filesystem tool
npx @michaellatman/mcp-get@latest install @modelcontextprotocol/server-filesystem
```

### Core Tools We've Integrated

1. **Brave Search**
   - Web and local search capabilities
   - Perfect for agents to gather information
   - Easy to use with sensible defaults
   - Built-in content filtering
   - Rate limiting and caching

2. **Filesystem**
   - Secure file operations
   - Directory management
   - File reading and metadata

### Web Context Support

The MCP tools include robust web context capabilities:

1. **Web Search Integration**
   - Seamless Brave Search integration
   - Real-time web content access
   - Context-aware search filtering

2. **Web Content Processing**
   - Automatic content extraction
   - Smart result summarization
   - Relevant information filtering

## How It Works: Discovery-First AI Tools

Our implementation lets agents learn about tools naturally:

```python
# First, agent can list available tools
servers = await mcp(
    server="list_available_servers"
)

# Then learn about specific tools
tool_info = await mcp(
    server="brave-search",
    tool="tool_details"
)
```

### Benefits
- Agents can explore available tools on their own
- No need to hardcode tool knowledge
- Tools are self-documenting
- New tools can be added without changing agent code

### Configuration

Tools can be configured through environment variables or config files:

```bash
# Brave Search configuration
export BRAVE_API_KEY=your_key_here

# Filesystem configuration
export FS_ROOT_DIR=/path/to/allowed/directory
```

### Troubleshooting

Common issues and solutions:

1. **Tool Discovery Failed**
   - Check if tool is installed
   - Verify server is running

2. **Permission Errors**
   - Review configuration
   - Check file permissions

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## License

MIT License - See [LICENSE](LICENSE) file for details.