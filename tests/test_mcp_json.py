"""
Test framework for validating the MCP tool implementation in mcp.json.
Ensures the JSON structure, function definition, and tool functionality 
meet the required specifications.
"""

import asyncio
import json
import re
from pathlib import Path
import test_mcp  # Import at the top level
from test_mcp import (
    WORKSPACE_DIR,
    TEST_DIR,
    TEST_FILE,
    TEST_FILE2,
    MOVED_FILE,
    test_list_servers,
    test_filesystem_operations,
    test_brave_search
)

def extract_function_from_json(json_path):
    """Extract and prepare the function code from mcp.json"""
    print(f"\nLoading MCP implementation from: {json_path}")
    with open(json_path) as f:
        tool_data = json.load(f)
    
    # Validate JSON structure
    required_fields = ["component_type", "name", "description", "content", "tool_type"]
    for field in required_fields:
        if field not in tool_data:
            raise ValueError(f"Missing required field: {field}")
    
    if tool_data["component_type"] != "tool":
        raise ValueError("Invalid component_type")
    
    if tool_data["tool_type"] != "PythonFunction":
        raise ValueError("Invalid tool_type")
    
    # Validate function structure
    func_def = tool_data["content"]
    if not re.search(r"async\s+def\s+mcp\s*\(", func_def):
        raise ValueError("Invalid function definition")
    
    print("\nValidating function parameters...")
    required_params = ["server", "tool", "query", "path", "count", "content", "edits", 
                      "paths", "source", "destination", "pattern", "excludePatterns", "dryRun"]
    func_params = re.findall(r"async\s+def\s+mcp\s*\((.*?)\)\s*->", func_def, re.DOTALL)
    if not func_params:
        raise ValueError("Couldn't extract function parameters")
    for param in required_params:
        if param not in func_params[0]:
            raise ValueError(f"Missing required parameter: {param}")
    print("✓ All required parameters present")
    
    # Create namespace and execute function
    print("\nLoading function implementation...")
    namespace = {}
    exec(func_def, namespace)
    return namespace['mcp']

async def run_tests():
    """Run all tests using the JSON implementation"""
    print("\n🔍 Validating MCP JSON Implementation")
    
    try:
        # Get JSON path
        current_dir = Path(__file__).parent
        json_path = current_dir.parent / "tools" / "mcp.json"
        
        # Extract and validate implementation
        test_mcp.mcp = extract_function_from_json(json_path)
        print("\n✓ JSON structure validated")
        print("✓ Function structure validated")
        
        # Ensure workspace exists
        WORKSPACE_DIR.mkdir(parents=True, exist_ok=True)
        
        tests = [
            ("Server Discovery", test_list_servers),
            ("Filesystem Operations", test_filesystem_operations),
            ("Brave Search", test_brave_search)
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
        
    except Exception as e:
        print(f"\n❌ Validation failed: {str(e)}")
        raise

if __name__ == "__main__":
    # Set environment variable for config path
    import os
    os.environ['MCP_CONFIG_PATH'] = str(Path(__file__).parent.parent / "mcp_config.json")
    asyncio.run(run_tests())