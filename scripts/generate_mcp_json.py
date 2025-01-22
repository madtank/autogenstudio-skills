"""
Generate MCP JSON format from Python implementation.
Takes the mcp_client.py file and converts it to the format required by AutoGen Studio.
"""

import json
import inspect
from pathlib import Path
import textwrap

def generate_mcp_json():
    """Generate MCP JSON from Python implementation"""
    # Read the Python file
    client_path = Path(__file__).parent.parent / "tools" / "mcp_client.py"
    with open(client_path, 'r') as f:
        content = f.read()
    
    # Extract docstring (everything between first set of triple quotes)
    description = content.split('"""')[1].strip()
    
    # Extract function implementation (everything after docstring)
    implementation = content[content.find('async def'):]
    
    # Ensure proper spacing and indentation
    implementation = textwrap.dedent(implementation)
    if not implementation.startswith('async def '):
        implementation = implementation.replace('async def', 'async def ', 1)
    
    # Create MCP JSON structure
    mcp_json = {
        "component_type": "tool",
        "name": "mcp",
        "description": description,
        "content": implementation,
        "tool_type": "PythonFunction"
    }
    
    # Write to mcp.json
    output_path = Path(__file__).parent.parent / "tools" / "mcp.json"
    with open(output_path, 'w') as f:
        json.dump(mcp_json, f, indent=2, ensure_ascii=False)
    
    print(f"Generated MCP JSON at: {output_path}")

if __name__ == "__main__":
    generate_mcp_json()