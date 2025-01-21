import pytest
import json
import os
from pathlib import Path
import shutil
from tests.mcp_tool import mcp

@pytest.fixture
def config_dir(tmp_path):
    """Create a temporary directory for config files"""
    return tmp_path

@pytest.fixture
def test_config():
    """Sample test configuration"""
    return {
        "mcpServers": {
            "brave-search": {
                "enabled": True,
                "command": "npx",
                "args": [
                    "-y",
                    "@modelcontextprotocol/server-brave-search"
                ],
                "env": {
                    "BRAVE_API_KEY": "test-key"
                }
            },
            "disabled-server": {
                "enabled": False,
                "command": "npx",
                "args": ["test"]
            }
        }
    }

async def test_missing_config(monkeypatch, config_dir):
    """Test behavior when config file is missing"""
    monkeypatch.setattr('tests.mcp_tool.Path.parent', lambda x: config_dir)
    result = await mcp(server="brave-search", tool="test")
    assert "Error: No configuration file found" in result

async def test_invalid_config_json(monkeypatch, config_dir):
    """Test behavior with invalid JSON in config"""
    config_path = config_dir / "mcp_config.json"
    with open(config_path, 'w') as f:
        f.write("invalid json{")
    
    monkeypatch.setattr('tests.mcp_tool.Path.parent', lambda x: config_dir)
    result = await mcp(server="brave-search", tool="test")
    assert "Error: " in result

async def test_disabled_server(monkeypatch, config_dir, test_config):
    """Test accessing a disabled server"""
    config_path = config_dir / "mcp_config.json"
    with open(config_path, 'w') as f:
        json.dump(test_config, f)
    
    monkeypatch.setattr('tests.mcp_tool.Path.parent', lambda x: config_dir)
    result = await mcp(server="disabled-server", tool="test")
    assert "Error: Server disabled-server is disabled in configuration" in result

async def test_list_enabled_servers(monkeypatch, config_dir, test_config):
    """Test that only enabled servers are listed"""
    config_path = config_dir / "mcp_config.json"
    with open(config_path, 'w') as f:
        json.dump(test_config, f)
    
    monkeypatch.setattr('tests.mcp_tool.Path.parent', lambda x: config_dir)
    result = await mcp(tool="list_available_servers")
    servers = json.loads(result)
    assert "brave-search" in servers
    assert "disabled-server" not in servers

async def test_missing_required_fields(monkeypatch, config_dir):
    """Test handling of missing required fields in config"""
    config = {
        "mcpServers": {
            "test-server": {
                "enabled": True
                # Missing required 'command' field
            }
        }
    }
    config_path = config_dir / "mcp_config.json"
    with open(config_path, 'w') as f:
        json.dump(config, f)
    
    monkeypatch.setattr('tests.mcp_tool.Path.parent', lambda x: config_dir)
    result = await mcp(server="test-server", tool="test")
    assert "Error: " in result

async def test_invalid_tool_arguments(monkeypatch, config_dir, test_config):
    """Test handling of invalid tool arguments"""
    config_path = config_dir / "mcp_config.json"
    with open(config_path, 'w') as f:
        json.dump(test_config, f)
    
    monkeypatch.setattr('tests.mcp_tool.Path.parent', lambda x: config_dir)
    # Test with a negative count which should be invalid
    result = await mcp(server="brave-search", tool="brave_web_search", count=-1)
    assert "Error: " in result

async def test_server_not_found(monkeypatch, config_dir, test_config):
    """Test accessing a non-existent server"""
    config_path = config_dir / "mcp_config.json"
    with open(config_path, 'w') as f:
        json.dump(test_config, f)
    
    monkeypatch.setattr('tests.mcp_tool.Path.parent', lambda x: config_dir)
    result = await mcp(server="nonexistent-server", tool="test")
    assert "Error: Server nonexistent-server not found" in result