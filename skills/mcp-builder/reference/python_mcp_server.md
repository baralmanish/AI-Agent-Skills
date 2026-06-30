# Python MCP Server Implementation Guide

## Quick Start

### Installation

```bash
pip install mcp
# or for faster development:
pip install "mcp[fastmcp]"
```

### Minimal Example with FastMCP

```python
from mcp.server.fastmcp import FastMCP

server = FastMCP("my-server")

@server.tool()
def greet(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    server.run()
```

## Standard SDK Pattern

### Create Server

```python
import asyncio
from mcp.server import Server
from mcp.types import Tool, TextContent

server = Server("my-server")

@server.list_tools()
async def list_tools() -> list[Tool]:
    """Return available tools."""
    return [
        Tool(
            name="greet",
            description="Greet someone by name",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Person's name"}
                },
                "required": ["name"],
            },
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Execute a tool."""
    if name == "greet":
        return [TextContent(type="text", text=f"Hello, {arguments['name']}!")]
    else:
        raise ValueError(f"Unknown tool: {name}")
```

### Run with Stdio Transport

```python
from mcp.server.stdio import stdio_server

async def main():
    async with stdio_server(server) as streams:
        await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
```

## Tool Implementation Patterns

### Simple Calculation Tool

```python
@server.tool()
def calculate(expression: str) -> str:
    """
    Evaluate a mathematical expression.

    Args:
        expression: Mathematical expression (e.g., "2 + 2")

    Returns:
        The result of the calculation
    """
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}"
```

### Data Retrieval Tool

```python
@server.tool()
def fetch_data(query: str, limit: int = 10) -> str:
    """
    Fetch data from a data source.

    Args:
        query: Search query
        limit: Maximum number of results

    Returns:
        JSON formatted data
    """
    try:
        data = database.search(query, limit=limit)
        return json.dumps(data, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"
```

### Tool with File Operations

```python
@server.tool()
def read_file(path: str) -> str:
    """
    Read and return file contents.

    Args:
        path: File path (relative to safe directory)

    Returns:
        File contents
    """
    safe_dir = "/data"
    full_path = os.path.abspath(os.path.join(safe_dir, path))

    # Security check: ensure path is within safe directory
    if not full_path.startswith(safe_dir):
        return "Error: Access denied"

    try:
        with open(full_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: File not found"
```

## Resource Implementation

### Simple Resource

```python
@server.resource()
def config_resource(uri: str) -> str:
    """
    Serve configuration files.

    Supported URIs:
        config:///database
        config:///api
    """
    if uri == "config:///database":
        return json.dumps({"host": "localhost", "port": 5432})
    elif uri == "config:///api":
        return json.dumps({"timeout": 30, "retries": 3})
    else:
        raise ValueError(f"Unknown resource: {uri}")
```

## Error Handling

### Structured Error Responses

```python
@server.tool()
def safe_operation(value: str) -> str:
    """Perform operation with error handling."""
    if not value:
        return '{"error": "Value cannot be empty"}'

    try:
        result = process(value)
        return json.dumps({"success": True, "result": result})
    except ValueError as e:
        return json.dumps({"error": f"Invalid value: {str(e)}"})
    except Exception as e:
        # Log the actual error for debugging
        logging.error(f"Unexpected error: {e}", exc_info=True)
        return json.dumps({"error": "An unexpected error occurred"})
```

## Async Operations

### Async Tool

```python
import asyncio

@server.tool()
async def fetch_from_api(url: str) -> str:
    """Fetch data from an API endpoint."""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as resp:
                return await resp.text()
    except asyncio.TimeoutError:
        return "Error: Request timed out"
    except Exception as e:
        return f"Error: {str(e)}"
```

## Input Validation

### Schema-Based Validation

```python
from typing import Optional

@server.tool()
def process_data(
    data: str,
    format: str = "json",
    limit: Optional[int] = None
) -> str:
    """
    Process input data.

    Args:
        data: Input data to process
        format: Data format (json, csv, xml)
        limit: Optional maximum items to process

    Returns:
        Processed data
    """
    if format not in ["json", "csv", "xml"]:
        return f"Error: Unsupported format '{format}'"

    if limit is not None and limit < 1:
        return "Error: Limit must be >= 1"

    try:
        return process(data, format=format, limit=limit)
    except Exception as e:
        return f"Error: {str(e)}"
```

## Logging and Debugging

### Configure Logging

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@server.tool()
def example_tool(param: str) -> str:
    """Example tool with logging."""
    logger.info(f"Tool called with param: {param}")
    try:
        result = do_something(param)
        logger.debug(f"Result: {result}")
        return result
    except Exception as e:
        logger.error(f"Error in example_tool: {e}", exc_info=True)
        return f"Error: {str(e)}"
```

## Testing Tools Locally

### Manual Testing

```bash
# Run the server in one terminal
python server.py

# In another terminal, test with curl (if using HTTP transport)
curl -X POST http://localhost:8000/tools/greet \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice"}'
```

### Unit Tests

```python
import pytest

@pytest.mark.asyncio
async def test_greet_tool():
    result = await call_tool("greet", {"name": "Alice"})
    assert "Hello, Alice" in result[0].text

@pytest.mark.asyncio
async def test_greet_empty_name():
    result = await call_tool("greet", {"name": ""})
    assert "error" in result[0].text.lower() or result[0].text == "Hello, !"
```

## Performance Optimization

### Caching Results

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_operation(key: str) -> str:
    """Perform expensive operation with caching."""
    return compute_result(key)

@server.tool()
def get_cached_result(key: str) -> str:
    """Get result with automatic caching."""
    return expensive_operation(key)
```

### Batch Operations

```python
@server.tool()
def batch_process(items: list[str]) -> str:
    """Process multiple items efficiently."""
    if len(items) > 100:
        return "Error: Maximum 100 items per request"

    results = []
    for item in items:
        try:
            results.append(process_item(item))
        except Exception as e:
            results.append(f"Error processing {item}: {e}")

    return json.dumps(results)
```

## Deployment

### Environment Variables

```python
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

if not API_KEY:
    raise ValueError("API_KEY environment variable not set")
```

### Docker Deployment

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

CMD ["python", "server.py"]
```
