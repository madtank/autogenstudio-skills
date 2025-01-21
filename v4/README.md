# AutoGen Studio V4 Tools

## What is MCP and Why We Use It

Model Context Protocol (MCP) is like a USB port for AI tools - it provides a standardized way for AI agents to discover and use different capabilities. We chose MCP for AutoGen Studio because it enables a "discovery-first" approach where agents can:

1. List available tools (like looking in a toolbox)
2. Learn about each tool's capabilities (reading the manual)
3. Use tools effectively based on their understanding

### Installing MCP Tools

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

2. **Filesystem**
   - Secure file operations
   - Directory management
   - File reading and metadata

## How It Works: Discovery-First AI Tools

Our implementation lets agents learn about tools naturally:

```python
# First, agent can list available servers
servers = await mcp(
    server="list_available_servers"
)

# Then learn about specific tools
tool_info = await mcp(
    server="brave-search",
    tool="tool_details"
)
```

### Why Discovery-First Matters
- Agents can explore available tools on their own
- No need to hardcode tool knowledge
- Tools are self-documenting
- New tools can be added without changing agent code

## Development Workflow

### 1. Core Development (`mcp_tool.py`)
```python
# Development happens here first
async def mcp(server: str, tool: str, ...):
    """
    Docstring is crucial - it teaches agents:
    1. How to discover tools
    2. How to use tool_details
    3. How to interpret results
    """
```

### 2. Testing (`test_mcp.py`)
- Tests core functionality
- Verifies tool discovery
- Ensures proper result handling

### 3. AutoGen Integration (`mcp.json`)
- Adapts core functionality for AutoGen Studio
- Maintains discovery-first approach
- Ensures proper result explanation

### 4. Integration Testing (`test_tools.py`)
- Validates AutoGen Studio compatibility
- Tests real-world usage patterns
- Confirms proper agent interaction

## Adding New Tools

### 1. Implementation Steps
1. Add core functionality to `mcp_tool.py`
2. Ensure proper discovery implementation
3. Add comprehensive tests
4. Create AutoGen Studio integration
5. Update documentation

### 2. Key Requirements
- Tools must be self-describing
- Include parameter validation
- Provide clear result explanations
- Follow discovery-first pattern

### 3. Testing Requirements
- Test tool discovery
- Test parameter validation
- Test result handling
- Test error cases

## Directory Structure
```
v4/
├── tools/
│   ├── mcp.json            # AutoGen Studio integration
│   └── README.md           # Tool-specific documentation
├── tests/
│   ├── mcp_tool.py         # Core implementation
│   ├── test_mcp.py         # Python tests
│   └── test_tools.py       # Integration tests
└── README.md               # This file
```

## Configuration

### MCP Server Setup
- Requires Claude Desktop
- Configuration in standard locations:
  - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
  - Windows: `%APPDATA%/Claude/claude_desktop_config.json`
  - Linux: `~/.config/Claude/claude_desktop_config.json`

### Development Requirements
- Python 3.8+
- MCP Python SDK
- Node.js and npx
- Claude Desktop

## Common Development Tasks

### Adding a New Tool
1. Update `mcp_tool.py`:
   - Add tool functionality
   - Ensure discovery support
   - Add result explanation

2. Add Tests:
   - Tool discovery tests
   - Functionality tests
   - Result handling tests

3. Update Integration:
   - Add to `mcp.json`
   - Test with AutoGen Studio
   - Verify agent interaction

### Modifying Existing Tools
1. Update core functionality
2. Verify discovery still works
3. Update tests
4. Test agent interaction

## Best Practices

### Tool Development
- Always implement discovery first
- Include clear parameter descriptions
- Provide meaningful result explanations
- Test agent interaction thoroughly

### Documentation
- Keep docstrings comprehensive
- Document discovery mechanisms
- Include usage examples
- Explain result formats