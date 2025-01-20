import json
import asyncio
import os
from pathlib import Path
from typing import Any, Dict

class ToolTester:
    def __init__(self):
        self.tools_dir = Path(__file__).parent / 'tools'
        self.tools = {}
        self.load_tools()

    def load_tools(self):
        """Load all tool definitions from the tools directory"""
        for tool_file in self.tools_dir.glob('*.json'):
            with open(tool_file) as f:
                tool_def = json.load(f)
                
                # Create namespace and execute the tool code
                namespace = {}
                exec(tool_def['content'], namespace)
                
                # Store tool info
                self.tools[tool_def['name']] = {
                    'function': namespace[tool_def['name']],
                    'description': tool_def['description']
                }

    async def test_calculator(self):
        """Test the calculator tool"""
        print("\n=== Testing Calculator ===")
        calc = self.tools['calculator']['function']
        
        test_cases = [
            (5, 3, '+'),
            (10, 2, '*'),
            (15, 3, '/'),
            (7, 4, '-'),
            (10, 0, '/'),  # Test division by zero
            (5, 3, '%')    # Test invalid operator
        ]
        
        for a, b, op in test_cases:
            result = calc(a, b, op)
            print(f"{a} {op} {b} = {result}")

    async def test_fetch_website(self):
        """Test the website fetcher tool"""
        print("\n=== Testing Website Fetcher ===")
        fetcher = self.tools['fetch_website']['function']
        
        url = input("Enter URL to fetch (or press enter for default): ").strip()
        if not url:
            url = "http://example.com"
        
        result = await fetcher(url)
        print(f"\nFetch result ({len(result)} characters):")
        print(result[:500] + "..." if len(result) > 500 else result)

    async def test_mcp(self):
        """Test the MCP tool"""
        print("\n=== Testing MCP ===")
        mcp = self.tools['mcp']['function']
        
        # Test brave search
        query = input("Enter search query (or press enter for default): ").strip()
        if not query:
            query = "What is MCP protocol?"
        
        result = await mcp(
            server="brave-search",
            tool="brave_web_search",
            query=query
        )
        print(f"\nSearch Result:\n{result}")

    async def run_tests(self):
        """Run all tests"""
        while True:
            print("\nTool Tester Menu:")
            print("1. Test Calculator")
            print("2. Test Website Fetcher")
            print("3. Test MCP")
            print("4. List Available Tools")
            print("5. Exit")
            
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == "1":
                await self.test_calculator()
            elif choice == "2":
                await self.test_fetch_website()
            elif choice == "3":
                await self.test_mcp()
            elif choice == "4":
                print("\n=== Available Tools ===")
                for name, info in self.tools.items():
                    print(f"\n{name}:")
                    print(f"Description: {info['description']}")
            elif choice == "5":
                print("\nExiting tester...")
                break
            else:
                print("\nInvalid choice. Please try again.")
            
            input("\nPress Enter to continue...")

def main():
    tester = ToolTester()
    asyncio.run(tester.run_tests())

if __name__ == "__main__":
    main()