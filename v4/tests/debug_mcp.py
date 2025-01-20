import asyncio
from mcp_tool import mcp

async def test_brave_with_debug():
    """Test Brave Search with debug output"""
    print("\nTesting Brave Search...")
    print("1. Starting server connection")
    
    try:
        async with asyncio.timeout(20):
            result = await mcp(
                server="brave-search",
                tool="brave_web_search",
                query="test query",
                count=1
            )
            print(f"Result received: {result}")
            return True
    except asyncio.TimeoutError:
        print("Connection timed out!")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

if __name__ == "__main__":
    print("Running debug test...")
    asyncio.run(test_brave_with_debug())