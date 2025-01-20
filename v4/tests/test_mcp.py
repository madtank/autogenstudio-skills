import asyncio
import json
from mcp_tool import mcp

# Discovery Tests
async def test_list_servers():
    """Test listing available servers"""
    print("\n=== Testing Server Discovery ===")
    
    result = await mcp(tool="list_available_servers")
    servers = json.loads(result)
    print(f"Available Servers:\n{result}")
    
    assert "filesystem" in servers
    assert "brave-search" in servers
    print("✓ Server discovery test passed")
    return True

async def test_brave_search_tools():
    """Test getting tool details for Brave Search"""
    print("\n=== Testing Brave Search Tool Details ===")
    
    result = await mcp(server="brave-search", tool="tool_details")
    tools = json.loads(result)
    print(f"Brave Search Tools:\n{result}")
    
    # Verify we have the web search tool
    tool_names = [t['name'] for t in tools]
    assert "brave_web_search" in tool_names
    print("✓ Brave Search tool details test passed")
    return True

async def test_filesystem_tools():
    """Test getting tool details for Filesystem"""
    print("\n=== Testing Filesystem Tool Details ===")
    
    result = await mcp(server="filesystem", tool="tool_details")
    tools = json.loads(result)
    print(f"Filesystem Tools:\n{result}")
    
    # Verify we have the expected filesystem tools
    tool_names = [t['name'] for t in tools]
    expected_tools = ["list_allowed_directories", "list_directory", "read_file", "get_file_info"]
    for tool in expected_tools:
        assert tool in tool_names
    print("✓ Filesystem tool details test passed")
    return True

# Brave Search Tests
async def test_web_search():
    """Test Brave web search"""
    print("\n=== Testing Brave Search ===")
    
    query = "What is Model Context Protocol?"
    print(f"Searching for: {query}")
    
    result = await mcp(
        server="brave-search",
        tool="brave_web_search",
        query=query,
        count=3
    )
    print(f"Search Result:\n{result}")
    assert '"Error"' not in result
    assert 'content=' in result
    print("✓ Web search test passed")
    return True

# Filesystem Tests
async def test_list_directories():
    """Test listing allowed directories"""
    print("\n=== Testing List Directories ===")
    
    result = await mcp(
        server="filesystem",
        tool="list_allowed_directories"
    )
    print(f"Allowed Directories:\n{result}")
    assert '"Error"' not in result
    assert '/Users/jacob/claude_home' in result
    print("✓ List directories test passed")
    return True

async def test_directory_contents():
    """Test listing directory contents"""
    print("\n=== Testing Directory Contents ===")
    
    result = await mcp(
        server="filesystem",
        tool="list_directory",
        path="/Users/jacob/claude_home"
    )
    print(f"Directory Contents:\n{result}")
    assert '"Error"' not in result
    print("✓ Directory contents test passed")
    return True

async def test_read_file():
    """Test reading a file"""
    print("\n=== Testing File Reading ===")
    
    result = await mcp(
        server="filesystem",
        tool="read_file",
        path="/Users/jacob/claude_home/autogenstudio-skills/v4/tools/README.md"
    )
    print(f"File Contents (truncated):\n{result[:200]}...")
    assert '"Error"' not in result
    assert len(result) > 0
    print("✓ File reading test passed")
    return True

async def test_file_info():
    """Test getting file info"""
    print("\n=== Testing File Info ===")
    
    result = await mcp(
        server="filesystem",
        tool="get_file_info",
        path="/Users/jacob/claude_home/autogenstudio-skills/v4/tools/README.md"
    )
    print(f"File Info:\n{result}")
    assert '"Error"' not in result
    print("✓ File info test passed")
    return True

async def main():
    """Run all tests"""
    print("\n🚀 Starting MCP Tests")
    
    tests = [
        ("Server Discovery", test_list_servers),
        ("Brave Search Tools", test_brave_search_tools),
        ("Filesystem Tools", test_filesystem_tools),
        ("Brave Search", test_web_search),
        ("List Directories", test_list_directories),
        ("Directory Contents", test_directory_contents),
        ("Read File", test_read_file),
        ("File Info", test_file_info)
    ]
    
    results = []
    for name, test_func in tests:
        try:
            success = await test_func()
            results.append((name, success))
        except Exception as e:
            print(f"Error in {name}: {str(e)}")
            results.append((name, False))
        print("\n" + "="*50)  # Separator
    
    # Print summary
    print("\n=== Test Summary ===")
    passed = 0
    total = len(tests)
    
    print("\nDiscovery Tests:")
    for name, success in results[:3]:  # First 3 tests are discovery
        status = "✓ Passed" if success else "❌ Failed"
        print(f"  {name}: {status}")
        if success:
            passed += 1
    
    print("\nBrave Search:")
    for name, success in results[3:4]:  # One Brave Search test
        status = "✓ Passed" if success else "❌ Failed"
        print(f"  {name}: {status}")
        if success:
            passed += 1
    
    print("\nFilesystem Operations:")
    for name, success in results[4:]:  # Rest are filesystem tests
        status = "✓ Passed" if success else "❌ Failed"
        print(f"  {name}: {status}")
        if success:
            passed += 1
    
    print(f"\nTests passed: {passed}/{total}")
    if passed == total:
        print("\n✨ All tests passed!")
    else:
        print(f"\n⚠️ {total - passed} test(s) failed!")

if __name__ == "__main__":
    asyncio.run(main())