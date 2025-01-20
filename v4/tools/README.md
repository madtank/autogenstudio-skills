# MCP Tool Implementation Guide

## Discovery-First Implementation
This implementation of the Model Context Protocol (MCP) emphasizes self-discovering, self-documenting tools. All functionality is discoverable through the protocol itself.

### Tool Discovery
```python
# 1. List available servers
servers = await mcp(tool='list_available_servers')

# 2. Get tool details
tools = await mcp(server='server_name', tool='tool_details')
```

IMPORTANT: AI agents must always:
1. Check tool availability first
2. Get tool details before use
3. Provide clear summaries of tool results

## Core Features

### 1. Brave Search
```python
# First: Get tool details
details = await mcp(server="brave-search", tool="tool_details")

# Then: Use the tool
result = await mcp(
    server="brave-search",
    tool="brave_web_search",
    query="search query",
    count=3  # Optional: limit results
)

# Always explain results to user
"""
I found 3 relevant results about [topic]:
1. [First result summary]
2. [Second result summary]
3. [Third result summary]
"""
```

### 2. Filesystem Operations

#### Available Tools
```python
# List Allowed Directories
result = await mcp(
    server="filesystem",
    tool="list_allowed_directories"
)

# List Directory Contents
result = await mcp(
    server="filesystem",
    tool="list_directory",
    path="/path/to/directory"
)

# Read File
result = await mcp(
    server="filesystem",
    tool="read_file",
    path="/path/to/file"
)

# Get File Info
result = await mcp(
    server="filesystem",
    tool="get_file_info",
    path="/path/to/file"
)
```

Always explain results:
```python
"""
The directory contains:
- 3 subdirectories: [names]
- 5 files: [names]
"""

"""
The file contains documentation about [topic], 
including sections on [key points]
"""
```

### Allowed Directories
- `/Users/jacob/claude_home`
- `/Users/jacob/Library/Application Support/Claude`

## Implementation Details

### Core Function
```python
async def mcp(
    server: str,    # Server name (e.g., "brave-search", "filesystem")
    tool: str,      # Tool name (e.g., "brave_web_search", "read_file")
    query: str = None,  # Search query or other text input
    path: str = None,   # File/directory path
    count: int = None   # Result count for search
) -> str:
    """Docstring is crucial - it teaches agents:
    1. How to discover tools
    2. How to use tool_details
    3. How to interpret results
    """
```

### Testing Strategy

1. **Core Testing** (`test_mcp.py`)
   - Tool discovery tests
   - Core functionality tests
   - Result handling tests

2. **Integration Testing** (`test_mcp_json.py`)
   - AutoGen Studio compatibility
   - Agent interaction patterns
   - End-to-end workflows

## Development Guidelines

### Adding New Tools
1. **Discovery Support**
   - Implement tool_details
   - Clear parameter descriptions
   - Usage examples

2. **Result Handling**
   - Clear result formats
   - Example summaries
   - Error handling

3. **Testing**
   - Discovery tests
   - Functionality tests
   - Result explanation tests

### Modifying Existing Tools
1. Update tool details first
2. Maintain backward compatibility
3. Update result handling
4. Update tests

## Best Practices

### Tool Documentation
- Clear parameter descriptions
- Usage examples
- Result format examples
- Error handling guidance

### Agent Interaction
- Always check tool details
- Validate parameters
- Explain results clearly
- Handle errors gracefully

### Testing
- Test discovery first
- Verify parameter handling
- Check result explanations
- Test error cases