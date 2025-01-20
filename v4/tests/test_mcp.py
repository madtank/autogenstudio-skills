import asyncio
import json
from mcp_tool import mcp

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
    
    print("\nBrave Search:")
    for name, success in results[:1]:  # First test is Brave Search
        status = "✓ Passed" if success else "❌ Failed"
        print(f"  {name}: {status}")
        if success:
            passed += 1
    
    print("\nFilesystem Operations:")
    for name, success in results[1:]:  # Rest are filesystem tests
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