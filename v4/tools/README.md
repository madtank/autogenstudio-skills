# MCP Tool Implementation

## Overview
This implementation of the Model Context Protocol (MCP) tool focuses on two core functionalities:
1. Web search capabilities via Brave Search
2. Secure filesystem operations

## Brave Search Operations

### Web Search
```python
# Basic web search
result = await mcp(
    server="brave-search",
    tool="brave_web_search",
    query="search query",
    count=3  # Optional: limit results
)
```

## Filesystem Operations

### Available Tools

1. **List Allowed Directories**
   ```python
   result = await mcp(
       server="filesystem",
       tool="list_allowed_directories"
   )
   ```

2. **List Directory Contents**
   ```python
   result = await mcp(
       server="filesystem",
       tool="list_directory",
       path="/path/to/directory"
   )
   ```

3. **Read File**
   ```python
   result = await mcp(
       server="filesystem",
       tool="read_file",
       path="/path/to/file"
   )
   ```

4. **Get File Info**
   ```python
   result = await mcp(
       server="filesystem",
       tool="get_file_info",
       path="/path/to/file"
   )
   ```

### Allowed Directories
- `/Users/jacob/claude_home`
- `/Users/jacob/Library/Application Support/Claude`

## Implementation Notes

### Core Function
```python
async def mcp(
    server: str,    # Server name (e.g., "brave-search", "filesystem")
    tool: str,      # Tool name (e.g., "brave_web_search", "read_file")
    query: str = None,  # Search query or other text input
    path: str = None,   # File/directory path
    count: int = None   # Result count for search
) -> str:
```

### Testing Strategy

1. **Direct Python Testing**
   ```bash
   python v4/tests/test_mcp.py
   ```
   Tests both Brave Search and filesystem operations.

2. **JSON Implementation Testing**
   ```bash
   python v4/tests/test_mcp_json.py
   ```
   Validates the JSON implementation matches Python functionality.

## Development Guidelines

1. **Tool-Specific Features**
   - Brave Search: Focus on query formatting and result parsing
   - Filesystem: Ensure safe file operations within allowed directories

2. **Testing**
   - Group tests by tool type
   - Include both success and error cases
   - Verify proper error handling
   - Test with realistic inputs

3. **Error Handling**
   - Return clear error messages
   - Handle network issues (Brave Search)
   - Check file permissions (Filesystem)
   - Validate all inputs

## Adding New Features

When adding new features:

1. Determine appropriate tool category
2. Add tool-specific argument handling
3. Update tests with new cases
4. Document usage and examples
5. Verify both Python and JSON implementations