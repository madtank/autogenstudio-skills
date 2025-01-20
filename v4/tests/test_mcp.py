import asyncio
import json
from mcp_tool import mcp

async def test_brave_search():
    """Test Brave Search functionality"""
    print("\n=== Testing Brave Search ===")
    
    query = "What is Model Context Protocol?"
    print(f"Searching for: {query}")
    
    result = await mcp(
        server="brave-search",
        tool="brave_web_search",
        query=query
    )
    print(f"Search Result:\n{result}")
    
    # Check if we got valid results
    return '"Error"' not in result and "content=" in result

async def test_bedrock_agent():
    """Test Bedrock Agent functionality"""
    print("\n=== Testing Bedrock Agent ===")
    
    print("Sending query to agent...")
    result = await mcp(
        server="bedrock-agent",
        tool="ask_agent",
        input="What are your capabilities?",
        memoryId="test-session-1"
    )
    print(f"Agent Response:\n{result}")
    
    # Check if we got valid results
    return '"Error"' not in result and "content=" in result

async def main():
    """Run tests"""
    print("\n🚀 Starting MCP Tests")
    
    # Test Brave Search
    brave_success = await test_brave_search()
    print("\nBrave Search:", "✓ Success" if brave_success else "❌ Failed")
    
    print("\n" + "="*50)  # Separator
    
    # Test Bedrock Agent
    bedrock_success = await test_bedrock_agent()
    print("\nBedrock Agent:", "✓ Success" if bedrock_success else "❌ Failed")
    
    # Summary
    print("\n=== Test Summary ===")
    tests_passed = 0
    tests_total = 2
    
    if brave_success:
        tests_passed += 1
    if bedrock_success:
        tests_passed += 1
    
    print(f"Tests passed: {tests_passed}/{tests_total}")
    if tests_passed == tests_total:
        print("\n✨ All tests passed!")
    else:
        print(f"\n⚠️ {tests_total - tests_passed} test(s) failed!")

if __name__ == "__main__":
    asyncio.run(main())