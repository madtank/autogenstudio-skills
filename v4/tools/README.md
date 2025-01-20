# MCP Tool Implementation

## Overview
This implementation of the Model Context Protocol (MCP) tool focuses on providing reliable access to key MCP servers, with specific argument handling for each tool type.

## Supported Servers & Tools

### Brave Search
- **Server**: `brave-search`
- **Tools**:
  - `brave_web_search`
    - Arguments: `query` (required), `count` (optional)
    - Example: `mcp(server="brave-search", tool="brave_web_search", query="search term")`

### Bedrock Agent
- **Server**: `bedrock-agent`
- **Tools**:
  - `ask_agent`
    - Arguments: `input` (required), `memoryId` (optional)
    - Example: `mcp(server="bedrock-agent", tool="ask_agent", input="query", memoryId="session-1")`

## Implementation Notes

### Argument Handling
Each tool type has specific argument handling to ensure reliable operation:
```python
# Build arguments based on tool
args = {}
if tool == "brave_web_search" and query:
    args['query'] = query
elif tool == "ask_agent":
    if input:
        args['input'] = input
    if memoryId:
        args['memoryId'] = memoryId
```

### Testing
Two test approaches are available:
1. Direct Python testing (`test_mcp.py`)
2. JSON validation testing (`test_mcp_json.py`)

Both use the same test cases but different entry points.

## Development Guidelines

1. Keep tool implementations simple and focused
2. Add explicit argument handling for each tool type
3. Use proper async/await patterns
4. Always test both Python and JSON implementations

## Adding New Tools
When adding support for new tools:

1. Add tool-specific argument handling
2. Update tests for the new tool
3. Document the tool's arguments and usage
4. Verify both Python and JSON implementations