# AutoGen Studio V4 Tools

## Overview
This directory contains tools compatible with AutoGen Studio V4, featuring a powerful new integration with the Model Context Protocol (MCP).

### What is MCP?
MCP (Model Context Protocol) acts as a "Universal Serial Bus (USB)" for AI tools - it's a standardized way for AI models to interact with external tools and data sources. Just like USB revolutionized how devices connect to computers, MCP standardizes how AI models connect to various tools and services.

Key benefits:
- **Universal Compatibility**: Tools built with MCP can work across different AI platforms
- **Standardized Interface**: Consistent way to expose functionality to AI models
- **Plugin Architecture**: Easy to add new capabilities without changing the core system
- **Security**: Built-in security model for safe AI-tool interactions

### Available MCP Servers
The MCP ecosystem includes several official servers that provide different capabilities. You can find the complete list and documentation at [MCP Servers Repository](https://github.com/modelcontextprotocol/servers).

Key servers include:

1. **Brave Search**
   - Web search capabilities
   - Local business search
   - News and article search

2. **Filesystem**
   - File and directory operations
   - Read/write capabilities
   - Directory listing and searching

3. **Playwright**
   - Browser automation
   - Screenshot capture
   - Web interaction

4. **YouTube Transcript**
   - Video transcript extraction
   - Multi-language support

Each server can be accessed using the MCP tool by specifying the server name and desired functionality. For the latest list of servers and their capabilities, visit the [official MCP servers documentation](https://github.com/modelcontextprotocol/servers).

## Tools Included

1. **Calculator**
   - Simple arithmetic operations
   - Clear error handling
   - String-based results

2. **Website Fetcher**
   - Async URL content fetching
   - Input validation
   - Timeout handling
   - Comprehensive error handling

3. **MCP Integration**
   - Connects to any MCP-compatible server
   - Supports multiple services (e.g., Brave Search)
   - Enhanced error handling
   - Async operation support

### MCP Tool Configuration
The MCP tool requires specific configuration for your operating system. The tool looks for the Claude Desktop configuration file in the following locations:

#### macOS
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

#### Windows
```
%APPDATA%/Claude/claude_desktop_config.json
```

#### Linux
```
~/.config/Claude/claude_desktop_config.json
```

You'll also need to set the correct path to the `npx` command:
- macOS with Homebrew: `/opt/homebrew/bin/npx`
- Other systems: Use `which npx` to find the correct path

To customize the paths for your system, modify the following variables in mcp.json:
```python
# Example of how to make paths platform-agnostic
config_path = str(Path.home() / "Library/Application Support/Claude/claude_desktop_config.json")
npx_path = "npx"  # Or full path to npx
```

## Directory Structure
```
v4/
├── tools/
│   ├── calculator.json       # Calculator tool definition
│   ├── fetch_website.json   # Website fetcher tool definition
│   └── mcp.json            # MCP tool definition
├── test_tools.py           # Tool testing script
└── README.md               # This file
```

## Requirements
- Python 3.8+
- MCP Python SDK (`pip install mcp`)
- Claude Desktop with MCP servers configured
- Node.js and npx for certain MCP servers

## Testing
Use the included test script to validate tool functionality:
```bash
python test_tools.py
```

## Troubleshooting

### Common Issues
1. **Config File Not Found**: Ensure Claude Desktop is installed and has been run at least once
2. **NPX Not Found**: Verify Node.js is installed and npx is in your PATH
3. **Permission Issues**: Check file permissions on the config file
4. **Path Issues**: Update the paths in mcp.json to match your system configuration

### Config File Locations
You can use this Python code to find your config file location:
```python
from pathlib import Path
import platform

def get_config_path():
    system = platform.system()
    home = Path.home()
    
    if system == "Darwin":  # macOS
        return home / "Library/Application Support/Claude/claude_desktop_config.json"
    elif system == "Windows":
        return Path(os.getenv("APPDATA")) / "Claude/claude_desktop_config.json"
    else:  # Linux and others
        return home / ".config/Claude/claude_desktop_config.json"
```