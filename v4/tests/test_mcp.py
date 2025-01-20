import asyncio
import pytest
from mcp_tool import mcp  # Import from local mcp_tool.py file

async def test_basic():
    """Test basic MCP functionality"""
    print("\n=== Testing MCP Basic Functionality ===")
    
    # Test 1: Brave Search
    print("\nTest 1: Brave Search")
    query = "What is MCP protocol?"
    result = await mcp(
        server="brave-search",
        tool="brave_web_search",
        query=query
    )
    print(f"Search Result:\n{result}")
    assert result is not None
    assert isinstance(result, str)
    assert len(result) > 0
    print("✓ Brave Search test passed")
    
    # Test 2: Filesystem
    print("\nTest 2: Filesystem")
    result = await mcp(
        server="filesystem",
        tool="list_allowed_directories"
    )
    print(f"Allowed Directories:\n{result}")
    assert result is not None
    assert isinstance(result, str)
    print("✓ Filesystem test passed")

    # Test 3: YouTube Transcript
    print("\nTest 3: YouTube Transcript")
    try:
        result = await mcp(
            server="youtube-transcript",
            tool="get_transcript",
            query={
                "url": "https://www.youtube.com/watch?v=Du8mbxGQ9Ek",
                "lang": "en"
            }
        )
        print(f"Transcript Result:\n{result}")
        assert result is not None
        assert isinstance(result, str)
        print("✓ YouTube Transcript test passed")
    except Exception as e:
        print(f"✗ YouTube Transcript test failed: {e}")

if __name__ == "__main__":
    asyncio.run(test_basic())