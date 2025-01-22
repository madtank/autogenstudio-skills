"""
Test the generated MCP JSON file for AutoGen Studio compatibility.
"""

import json
import os
from pathlib import Path
import pytest

def test_mcp_json_structure():
    """Test that the generated JSON has the correct structure"""
    json_path = Path(__file__).parent.parent / "tools" / "mcp.json"
    assert json_path.exists(), "mcp.json not found"
    
    with open(json_path) as f:
        data = json.load(f)
    
    # Check required fields
    assert data["component_type"] == "tool", "Invalid component_type"
    assert data["name"] == "mcp", "Invalid name"
    assert data["tool_type"] == "PythonFunction", "Invalid tool_type"
    
    # Check description format
    assert "discovery-first approach" in data["description"], "Missing discovery approach in description"
    assert "List available servers" in data["description"], "Missing server listing in description"
    assert "Common Examples" in data["description"], "Missing examples in description"
    
    # Check function definition
    assert "async def mcp" in data["content"], "Invalid function definition"
    assert "server: str = None" in data["content"], "Missing server parameter"
    assert "tool: str = None" in data["content"], "Missing tool parameter"
    assert "arguments: dict = None" in data["content"], "Missing arguments parameter"
    
    print("✓ MCP JSON structure validated successfully")

if __name__ == "__main__":
    test_mcp_json_structure()