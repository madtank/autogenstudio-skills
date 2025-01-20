# AutoGen Studio Skills Repository

## Overview
This repository houses tools and integrations for AutoGen Studio, with a focus on Model Context Protocol (MCP) integration in V4. Our implementation emphasizes discoverable, self-describing tools that AI agents can understand and use effectively.

## Repository Structure

### V4 Directory (`/v4`)
Features MCP-integrated tools built on a "discovery-first" architecture:
- Tools describe their own capabilities and parameters
- AI agents learn tool usage through built-in discovery mechanisms
- Focused on core capabilities with room for expansion

Current focus:
- **Brave Search**: Web search capabilities
- **Filesystem Operations**: Secure file handling
- **Tool Discovery**: Self-describing tool interfaces

### V2 Directory (`/v2`)
Legacy tools for AutoGen Studio V2 (see v2/README.md for details)

## Development Philosophy

### Discovery-First Design
Our V4 tools are built around the principle that AI agents should:
1. Discover available tools
2. Learn tool capabilities and parameters
3. Use tools appropriately based on their documentation

This approach:
- Makes tools self-documenting
- Reduces errors through parameter validation
- Scales naturally as new tools are added

### Development Workflow
1. Update and test core functionality in `mcp_tool.py`
2. Verify with Python tests (`test_mcp.py`)
3. Update AutoGen Studio integration in `mcp.json`
4. Validate with integration tests (`test_tools.py`)

## Contributing

### Adding New Tools
1. Start with `mcp_tool.py` for core implementation
2. Ensure tool is self-describing through MCP
3. Add appropriate tests
4. Create AutoGen Studio integration
5. Update documentation

### Testing
Each version includes specific testing tools:
- V4: Comprehensive test suite in `test_mcp.py` and `test_tools.py`
- V2: Individual tool test suites

## Getting Started
See `/v4/README.md` for detailed setup and usage instructions.

## License
This project is licensed under the terms specified in the LICENSE file.