import asyncio
import json
import re
from test_mcp import test_web_search, test_list_directories, test_directory_contents, test_read_file, test_file_info

def extract_function_from_json(json_path):
    """Extract and prepare the function code from mcp.json"""
    with open(json_path) as f:
        tool_data = json.load(f)
    
    # Get the function content
    func_code = tool_data['content']
    
    # Create a module-level namespace
    namespace = {}
    
    # Execute the function definition in this namespace
    exec(func_code, namespace)
    
    # Return the function object
    return namespace['mcp']

async def validate_json_and_test():
    """Validate mcp.json and run tests using its implementation"""
    print("\n🔍 Validating MCP JSON Implementation")
    
    try:
        # Get correct path relative to this file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(current_dir, "..", "tools", "mcp.json")
        
        with open(json_path) as f:
            tool_data = json.load(f)
        
        required_fields = ["component_type", "name", "description", "content", "tool_type"]
        for field in required_fields:
            if field not in tool_data:
                raise ValueError(f"Missing required field: {field}")
        
        if tool_data["component_type"] != "tool":
            raise ValueError("Invalid component_type")
        
        if tool_data["tool_type"] != "PythonFunction":
            raise ValueError("Invalid tool_type")
        
        print("✓ JSON structure validated")
        
        # Extract and validate function structure
        func_def = tool_data["content"]
        if not re.search(r"async\s+def\s+mcp\s*\(", func_def):
            raise ValueError("Invalid function definition")
        
        print("✓ Function structure validated")
        
        # Extract function and run tests
        print("\n🚀 Running Tests with JSON Implementation")
        
        # Replace the mcp import in test_mcp with our extracted function
        import test_mcp
        test_mcp.mcp = extract_function_from_json(json_path)
        
        # Run tests
        brave_success = await test_web_search()
        print("\nBrave Search:", "✓ Success" if brave_success else "❌ Failed")
        
        print("\n" + "="*50)  # Separator
        
        # Run filesystem tests
        fs_tests = [
            ("List Directories", test_list_directories),
            ("Directory Contents", test_directory_contents),
            ("Read File", test_read_file),
            ("File Info", test_file_info)
        ]
        
        fs_results = []
        for name, test_func in fs_tests:
            success = await test_func()
            fs_results.append((name, success))
        
        # Summary
        print("\n=== Test Summary ===")
        
        print("\nBrave Search:")
        print(f"  Web Search: {'✓ Passed' if brave_success else '❌ Failed'}")
        
        print("\nFilesystem Operations:")
        tests_passed = 1 if brave_success else 0
        for name, success in fs_results:
            status = "✓ Passed" if success else "❌ Failed"
            print(f"  {name}: {status}")
            if success:
                tests_passed += 1
        
        total_tests = len(fs_tests) + 1
        print(f"\nTests passed: {tests_passed}/{total_tests}")
        
        if tests_passed == total_tests:
            print("\n✨ All tests passed!")
        else:
            print(f"\n⚠️ {total_tests - tests_passed} test(s) failed!")
        
    except Exception as e:
        print(f"\n❌ Validation failed: {str(e)}")
        raise  # Re-raise to show full traceback

if __name__ == "__main__":
    import os
    asyncio.run(validate_json_and_test())