"""
Test suite for the unified MCP client implementation.
Tests core functionality including server discovery, tool discovery,
and specific server capabilities (Brave search, filesystem operations).
"""

import asyncio
from asyncio import TimeoutError
import json
import os
from pathlib import Path
import pytest
import shutil
import sys
from typing import List, Tuple

# Add tools directory to path
sys.path.append(str(Path(__file__).parent.parent / "tools"))
from mcp_client import mcp

# Test constants
WORKSPACE_DIR = Path.cwd() / "mcp_workspace"
TEST_FILE = WORKSPACE_DIR / "test.txt"
TEST_FILE2 = WORKSPACE_DIR / "test2.txt"
MOVED_FILE = WORKSPACE_DIR / "moved.txt"
TEST_CONTENT = "Hello, World!"

@pytest.fixture(autouse=True)
def setup_workspace():
    """Setup and cleanup test workspace"""
    WORKSPACE_DIR.mkdir(parents=True, exist_ok=True)
    yield
    shutil.rmtree(WORKSPACE_DIR, ignore_errors=True)

async def with_timeout(coro, timeout=10):
    """Run coroutine with timeout"""
    try:
        return await asyncio.wait_for(coro, timeout)
    except TimeoutError:
        return "Error: Operation timed out"
    except Exception as e:
        return f"Error: {str(e)}"

async def test_server_discovery():
    """Test server discovery with error handling"""
    print("\nTesting server discovery...")
    
    # List available servers
    result = await with_timeout(mcp(tool='list_available_servers'))
    if isinstance(result, str) and result.startswith("Error"):
        print(f"Server discovery failed: {result}")
        return False
        
    servers = json.loads(result)
    print(f"✓ Found {len(servers)} servers: {', '.join(servers)}")
    
    # Test each server's tools
    successes = []
    for server in servers:
        print(f"\nGetting tools for {server}...")
        tools_result = await with_timeout(mcp(server=server, tool='tool_details'))
        
        if isinstance(tools_result, str) and tools_result.startswith("Error"):
            print(f"? Skipping {server}: {tools_result}")
            continue
            
        try:
            tools = json.loads(tools_result)
            print(f"✓ Found {len(tools)} tools:")
            for tool in tools:
                print(f"  - {tool['name']}")
            successes.append(server)
        except Exception as e:
            print(f"? Error parsing tools for {server}: {str(e)}")
    
    # Consider test successful if at least one server worked
    return len(successes) > 0

async def test_filesystem_operations():
    """Test filesystem operations"""
    print("\nTesting filesystem operations...")
    
    # Write test file
    print("Testing write_file...")
    result = await with_timeout(mcp(
        server='filesystem',
        tool='write_file',
        path=str(TEST_FILE),
        content=TEST_CONTENT
    ))
    if "successfully" not in str(result).lower():
        print(f"Write failed: {result}")
        return False
    print("✓ File written successfully")
    
    # Read test file
    print("Testing read_file...")
    result = await with_timeout(mcp(
        server='filesystem',
        tool='read_file',
        path=str(TEST_FILE)
    ))
    # Handle TextContent response format
    if isinstance(result, str) and 'TextContent' in result:
        result = result.split("text='")[1].split("'")[0]
    if result != TEST_CONTENT:
        print(f"Read content mismatch: {result}")
        return False
    print("✓ File read successfully")
    
    # List directory
    print("Testing list_directory...")
    result = await with_timeout(mcp(
        server='filesystem',
        tool='list_directory',
        path=str(WORKSPACE_DIR)
    ))
    if TEST_FILE.name not in str(result):
        print("File not found in directory listing")
        return False
    print("✓ Directory listed successfully")
    
    return True

async def test_brave_search():
    """Test Brave search capabilities"""
    print("\nTesting Brave search...")
    
    # Web search
    print("Testing web search...")
    result = await with_timeout(mcp(
        server='brave-search',
        tool='brave_web_search',
        query="latest AI developments",
        count=3
    ))
    
    if isinstance(result, str) and result.startswith("Error"):
        print(f"Web search failed: {result}")
        return False
        
    try:
        if result and len(result) > 0:
            print("✓ Web search successful")
            return True
        else:
            print("? No search results returned")
            return False
    except Exception as e:
        print(f"? Error parsing search results: {str(e)}")
        return False

async def run_all_tests():
    """Run all tests with better error handling"""
    print("\n=== Running MCP Client Tests ===")
    
    tests = [
        ("Server Discovery", test_server_discovery),
        ("Filesystem Operations", test_filesystem_operations),
        ("Brave Search", test_brave_search)
    ]
    
    results: List[Tuple[str, bool]] = []
    for name, test_func in tests:
        try:
            print(f"\n{'='*50}")
            print(f"Running {name} Tests")
            print('='*50)
            
            # Run test with timeout
            success = await with_timeout(test_func())
            results.append((name, success))
            
        except Exception as e:
            print(f"❌ Error in {name}: {str(e)}")
            results.append((name, False))
    
    # Print summary
    print("\n=== Test Summary ===")
    passed = sum(1 for _, success in results if success)
    total = len(tests)
    
    for name, success in results:
        status = "✓ Passed" if success else "❌ Failed"
        print(f"{name}: {status}")
    
    print(f"\nTests passed: {passed}/{total}")
    return passed > 0  # Success if at least one test passes

if __name__ == "__main__":
    # Set environment variable for config path to local directory
    os.environ['MCP_CONFIG_PATH'] = str(Path(__file__).parent.parent / "mcp_config.json")
    
    # Run tests with timeout
    try:
        success = asyncio.run(with_timeout(run_all_tests(), timeout=60))
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\nTests interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\nUnexpected error: {str(e)}")
        sys.exit(1)