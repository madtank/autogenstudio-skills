import os
import json
import asyncio
from pathlib import Path
import sys

# Add the parent directory to the Python path
sys.path.append(str(Path(__file__).parent))
from mcp_tool import mcp

# Define workspace directory
WORKSPACE_DIR = Path(__file__).parent.parent / "mcp_workspace"

async def print_tool_details(tool_name: str, details: dict):
    """Helper to print full tool documentation"""
    print(f"\n=== {tool_name} ===")
    print(f"Description: {details['description']}")
    print("\nArguments:")
    for prop, info in details['input_schema']['properties'].items():
        print(f"  {prop}:")
        print(f"    Type: {info.get('type', 'Not specified')}")
        if 'description' in info:
            print(f"    Description: {info['description']}")
        if 'default' in info:
            print(f"    Default: {info['default']}")
    print(f"\nRequired fields: {details['input_schema'].get('required', [])}")

async def test_filesystem_tool_discovery():
    """Show all available filesystem tools and their complete documentation"""
    print("\n🔍 Discovering Filesystem Tools")
    
    result = await mcp(server="filesystem", tool="tool_details")
    tools = json.loads(result)
    
    print(f"\nFound {len(tools)} filesystem tools:")
    for tool in tools:
        await print_tool_details(tool['name'], tool)
    
    return tools

async def test_file_operations():
    """Test full range of file operations"""
    print("\n📂 Testing File Operations")
    
    try:
        # Setup test area
        test_dir = WORKSPACE_DIR / "test_files"
        result = await mcp(
            server="filesystem",
            tool="create_directory",
            path=str(test_dir)
        )
        print(f"\n1. Create Directory Result:")
        print(result)

        # 1. Write a file
        test_file = test_dir / "test.txt"
        content = "Hello from MCP!\nThis is a test file."
        result = await mcp(
            server="filesystem",
            tool="write_file",
            path=str(test_file),
            content=content
        )
        print(f"\n2. Write File Result:")
        print(result)

        # 2. Read the file
        result = await mcp(
            server="filesystem",
            tool="read_file",
            path=str(test_file)
        )
        print("\n3. Read File Result:")
        print(result)

        # 3. Get file info
        result = await mcp(
            server="filesystem",
            tool="get_file_info",
            path=str(test_file)
        )
        print("\n4. Get File Info Result:")
        print(result)

        # 4. List directory
        result = await mcp(
            server="filesystem",
            tool="list_directory",
            path=str(test_dir)
        )
        print("\n5. List Directory Result:")
        print(result)

        # 5. Directory tree
        result = await mcp(
            server="filesystem",
            tool="directory_tree",
            path=str(test_dir)
        )
        print("\n6. Directory Tree Result:")
        print(result)

        # 6. Edit file
        result = await mcp(
            server="filesystem",
            tool="edit_file",
            path=str(test_file),
            edits=[{
                "oldText": "Hello",
                "newText": "Greetings"
            }]
        )
        print("\n7. Edit File Result:")
        print(result)

        # 7. Search for files
        result = await mcp(
            server="filesystem",
            tool="search_files",
            path=str(test_dir),
            pattern="*.txt"
        )
        print("\n8. Search Files Result:")
        print(result)

        # 8. Read multiple files
        result = await mcp(
            server="filesystem",
            tool="read_multiple_files",
            paths=[str(test_file)]
        )
        print("\n9. Read Multiple Files Result:")
        print(result)

        # 9. Move file
        move_source = test_file
        move_dest = test_dir / "moved.txt"
        result = await mcp(
            server="filesystem",
            tool="move_file",
            source=str(move_source),
            destination=str(move_dest)
        )
        print("\n10. Move File Result:")
        print(result)

    except Exception as e:
        print(f"\n❌ Error during operation: {str(e)}")

async def test_allowed_directories():
    """Test allowed directory restrictions"""
    print("\n🔒 Testing Directory Access Controls")
    
    # List allowed directories
    result = await mcp(
        server="filesystem",
        tool="list_allowed_directories"
    )
    print("\nAllowed directories:", result)
    
    # Try to access a directory outside allowed paths
    result = await mcp(
        server="filesystem",
        tool="list_directory",
        path="/etc"  # This should fail
    )
    print("\nAttempting to access restricted directory:", result)

async def main():
    """Run all filesystem tests"""
    # Create workspace if it doesn't exist
    if not WORKSPACE_DIR.exists():
        WORKSPACE_DIR.mkdir(parents=True)
    
    print("\n🚀 Starting Filesystem Tests")
    
    # First discover all tools
    print("\n=== Tool Discovery ===")
    tools = await test_filesystem_tool_discovery()
    
    # Test file operations
    print("\n=== File Operations ===")
    await test_file_operations()
    
    # Test directory restrictions
    print("\n=== Directory Restrictions ===")
    await test_allowed_directories()

if __name__ == "__main__":
    asyncio.run(main())