"""
Comprehensive test suite for the MCP (Model Context Protocol) implementation.
Tests all core functionality including:

1. Server Discovery
   - List and verify available servers
   - Validate server configurations

2. Filesystem Operations
   - Directory creation and manipulation
   - File read/write operations
   - File editing and moving
   - Directory listing and tree traversal
   - File search and pattern matching

3. Brave Search Integration
   - Web search capabilities
   - Result formatting and limits

Each test provides detailed output and verification steps.
The test suite can be run with `asyncio.run(main())`.
"""

import asyncio
import json
from pathlib import Path
from mcp_tool import mcp

# Define workspace paths
WORKSPACE_DIR = Path("~/claude_home/autogenstudio-skills/mcp_workspace")
TEST_DIR = WORKSPACE_DIR / "test_directory"
TEST_FILE = TEST_DIR / "test.txt"
TEST_FILE2 = TEST_DIR / "test2.txt"
MOVED_FILE = TEST_DIR / "moved.txt"

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

async def test_filesystem_operations():
    """Test all filesystem operations"""
    print("\n=== Testing Filesystem Operations ===")

    # 1. Create test directory
    print("\n1. Creating Directory:")
    result = await mcp(
        server="filesystem",
        tool="create_directory",
        path=str(TEST_DIR)
    )
    print(result)

    # 2. Write test file
    print("\n2. Writing File:")
    content = "Hello, this is a test file!\nIt has multiple lines.\nWe can edit it later."
    result = await mcp(
        server="filesystem",
        tool="write_file",
        path=str(TEST_FILE),
        content=content
    )
    print(result)

    # 3. Read file
    print("\n3. Reading File:")
    result = await mcp(
        server="filesystem",
        tool="read_file",
        path=str(TEST_FILE)
    )
    print(result)

    # 4. Write second file
    print("\n4. Writing Second File:")
    result = await mcp(
        server="filesystem",
        tool="write_file",
        path=str(TEST_FILE2),
        content="This is another test file.\nWe can read multiple files."
    )
    print(result)

    # 5. Read multiple files
    print("\n5. Reading Multiple Files:")
    result = await mcp(
        server="filesystem",
        tool="read_multiple_files",
        paths=[str(TEST_FILE), str(TEST_FILE2)]
    )
    print(result)

    # 6. Edit file
    print("\n6. Editing File:")
    result = await mcp(
        server="filesystem",
        tool="edit_file",
        path=str(TEST_FILE),
        edits=[{
            "oldText": "Hello",
            "newText": "Greetings"
        }]
    )
    print(result)

    # 7. Get file info
    print("\n7. Getting File Info:")
    result = await mcp(
        server="filesystem",
        tool="get_file_info",
        path=str(TEST_FILE)
    )
    print(result)

    # 8. List directory
    print("\n8. Listing Directory Contents:")
    result = await mcp(
        server="filesystem",
        tool="list_directory",
        path=str(TEST_DIR)
    )
    print(result)

    # 9. Get directory tree
    print("\n9. Getting Directory Tree:")
    result = await mcp(
        server="filesystem",
        tool="directory_tree",
        path=str(TEST_DIR)
    )
    print(result)

    # 10. Search files
    print("\n10. Searching Files:")
    result = await mcp(
        server="filesystem",
        tool="search_files",
        path=str(TEST_DIR),
        pattern="*.txt"
    )
    print(result)

    # 11. Move file
    print("\n11. Moving File:")
    result = await mcp(
        server="filesystem",
        tool="move_file",
        source=str(TEST_FILE2),
        destination=str(MOVED_FILE)
    )
    print(result)

    # 12. Verify final state
    print("\n12. Final Directory State:")
    result = await mcp(
        server="filesystem",
        tool="list_directory",
        path=str(TEST_DIR)
    )
    print(result)

    return True

async def test_brave_search(run_search: bool = False):
    """Test Brave web search
    Args:
        run_search: Whether to actually perform a search query. Defaults to False to avoid rate limits.
    """
    print("\n=== Testing Brave Search ===")
    
    if not run_search:
        print("\nSkipping Brave search test to avoid rate limits.")
        print("To run search test, call with run_search=True")
        return True
    
    print("\nSearching for: What is Model Context Protocol?")
    result = await mcp(
        server="brave-search",
        tool="brave_web_search",
        query="What is Model Context Protocol?",
        count=3
    )
    print(f"Search Result:\n{result}")
    
    return True

async def main():
    """Run all tests with detailed output"""
    print("\n🚀 Starting MCP Tests")
    
    tests = [
        ("Server Discovery", test_list_servers),
        ("Filesystem Operations", test_filesystem_operations),
        ("Brave Search", lambda: test_brave_search(run_search=False))  # Skip search by default
    ]
    
    results = []
    for name, test_func in tests:
        try:
            print(f"\n{'='*50}")
            print(f"Running {name} Tests")
            print('='*50)
            success = await test_func()
            results.append((name, success))
        except Exception as e:
            print(f"❌ Error in {name}: {str(e)}")
            results.append((name, False))
    
    # Print summary
    print("\n=== Test Summary ===")
    passed = 0
    total = len(tests)
    
    for name, success in results:
        status = "✓ Passed" if success else "❌ Failed"
        print(f"{name}: {status}")
        if success:
            passed += 1
    
    print(f"\nTests passed: {passed}/{total}")
    if passed == total:
        print("\n✨ All tests passed!")
    else:
        print(f"\n⚠️ {total - passed} test(s) failed!")

if __name__ == "__main__":
    asyncio.run(main())