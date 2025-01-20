# AutoGen Studio V4 Tools

## Core Philosophy: Discovery-First AI Tools

Our V4 implementation centers on the principle that AI agents should discover and learn how to use tools through their own inquiry. This is achieved through the Model Context Protocol (MCP), which provides:

1. **Tool Discovery**: Agents can list available tools
2. **Self-Documentation**: Each tool describes its parameters and usage
3. **Runtime Learning**: Agents understand tools by examining their descriptions

### Why This Matters
- Agents adapt to new tools without code changes
- Tools are self-documenting and self-validating
- Development is more maintainable and scalable

## Current Implementation

### Core Features
1. **Tool Discovery**
   - List available servers
   - Get detailed tool descriptions
   - Understand parameter requirements

2. **Brave Search**
   - Web search capabilities
   - Parameter validation
   - Result summarization

3. **Filesystem Operations**
   - Secure file access
   - Directory management
   - File metadata

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