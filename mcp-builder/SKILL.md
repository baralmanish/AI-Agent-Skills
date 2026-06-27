---
name: mcp-builder
description: Generate and deploy MCP (Model Context Protocol) servers with planning, implementation, validation, and deployment. Use this skill when the user asks to build, create, or generate an MCP server, extend an existing MCP server, or deploy an MCP server to production. Covers Python and Node.js SDKs, tool implementation, resource management, and best practices.
license: Apache 2.0
---

# MCP Builder

Build production-ready Model Context Protocol (MCP) servers with comprehensive planning, implementation, testing, and deployment guidance.

## Process

### 🚀 High-Level Workflow

1. **Phase 1: Deep Research and Planning** — Understand requirements, study MCP architecture, plan server structure
2. **Phase 2: Implementation** — Write core server code, implement tools/resources, add error handling
3. **Phase 3: Validation** — Test locally, verify tool outputs, debug issues
4. **Phase 4: Deployment** — Containerize (if needed), set environment variables, deploy to production

### Phase 1: Deep Research and Planning

#### 1.1 Clarify Requirements
- What tools/resources should the server expose?
- What is the primary use case?
- Are there authentication or permission requirements?
- What are the scale/performance expectations?

#### 1.2 Choose SDK and Framework
- **Python**: Use the official Python SDK for MCP
  - Reference: [Python SDK README](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md)
  - Best for: Data processing, AI integrations, scientific computing
  - Framework: FastMCP (simplified decorator-based approach) or standard SDK

- **Node.js/TypeScript**: Use the official Node.js SDK
  - Best for: Web APIs, real-time features, JavaScript ecosystem integration
  - Framework: Full SDK with fine-grained control

- **Other languages**: Check [MCP Implementations](https://github.com/modelcontextprotocol#implementations) for community SDKs

#### 1.3 Study Framework Documentation
- **Python SDK**: Understand `Server` class, `@tool` decorator, `@resource` decorator, error handling patterns
- **Node.js SDK**: Understand server initialization, `Tool` and `Resource` classes, request/response handling
- Review reference implementation guides: See `reference/python_mcp_server.md` or `reference/nodejs_mcp_server.md`

#### 1.4 Plan Server Structure
```
my-mcp-server/
├── server.py (or server.ts for Node.js)      # Main server entry point
├── tools/
│   ├── __init__.py
│   ├── tool_1.py                              # Each tool in its own module
│   ├── tool_2.py
│   └── shared_utils.py                        # Shared utility functions
├── resources/
│   ├── __init__.py
│   ├── resource_1.py                          # Each resource in its own module
│   └── templates.py                           # Template definitions
├── requirements.txt (Python) or package.json  # Dependencies
├── .env.example                               # Environment variable template
├── README.md                                  # Usage documentation
└── Dockerfile (optional)                      # For containerization
```

### Phase 2: Implementation

#### 2.1 Create Server Instance
Initialize the MCP server with proper configuration.

**Python (FastMCP - Recommended):**
```python
from mcp.server.fastmcp import FastMCP

server = FastMCP("server-name", instructions="Brief description of what this server does")
```

**Python (Standard SDK):**
```python
from mcp.server import Server
from mcp.types import Tool, Resource

server = Server("server-name")
```

**Node.js:**
```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server({
  name: "server-name",
  version: "1.0.0",
});
```

#### 2.2 Implement Tools

A tool is a callable function that Claude can invoke. Always include:
- Clear, descriptive name
- Detailed description of what it does
- Input schema with types and documentation
- Error handling
- Return value documentation

**Python:**
```python
@server.tool()
def tool_name(arg1: str, arg2: int) -> str:
    """
    Brief description of what this tool does.
    
    Args:
        arg1: Description of arg1
        arg2: Description of arg2
    
    Returns:
        Description of return value
    """
    try:
        # Tool logic here
        result = perform_operation(arg1, arg2)
        return result
    except Exception as e:
        return f"Error: {str(e)}"
```

**Node.js:**
```typescript
server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [
    {
      name: "tool_name",
      description: "Brief description of what this tool does.",
      inputSchema: {
        type: "object",
        properties: {
          arg1: { type: "string", description: "Description of arg1" },
          arg2: { type: "number", description: "Description of arg2" },
        },
        required: ["arg1", "arg2"],
      },
    },
  ],
}));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "tool_name") {
    try {
      const result = performOperation(request.params.arguments.arg1);
      return { content: [{ type: "text", text: result }] };
    } catch (error) {
      return { isError: true, content: [{ type: "text", text: `Error: ${error}` }] };
    }
  }
  throw new Error("Unknown tool");
});
```

#### 2.3 Implement Resources (Optional)

Resources are read-only data sources that Claude can access. Include:
- URI schema
- Description
- Content type
- Data payload

**Python:**
```python
@server.resource()
def resource_name(uri: str) -> str:
    """
    Description of the resource and what URIs are supported.
    
    Example URIs:
        resource:///item/123
        resource:///config/settings
    """
    # Resource retrieval logic
    return resource_content
```

#### 2.4 Add Error Handling and Logging

- Wrap tool execution in try-catch
- Log errors with sufficient context
- Return meaningful error messages to Claude
- Never expose internal implementation details in error messages

### Phase 3: Validation

#### 3.1 Local Testing
- Test each tool individually with various inputs
- Test error cases and edge cases
- Verify output format and content

#### 3.2 Integration Testing
- Test tool chaining (one tool output → another tool input)
- Test with Claude to ensure outputs are useful
- Verify performance for large datasets

#### 3.3 Security Review
- Check for injection vulnerabilities
- Verify authentication/authorization if applicable
- Ensure sensitive data is not exposed in logs

### Phase 4: Deployment

#### 4.1 Environment Setup
Create `.env` file with required variables:
```bash
MCP_SERVER_NAME=my-server
LOG_LEVEL=info
API_KEY=your-api-key-here
```

#### 4.2 Containerization (Optional)
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "server.py"]
```

#### 4.3 Deployment Options
- **Local**: Run directly with `python server.py`
- **Docker**: `docker build -t my-mcp-server . && docker run my-mcp-server`
- **Cloud**: Deploy to AWS Lambda, Google Cloud Run, or similar
- **Anthropic Claude**: Register with Anthropic to use in Claude

## Best Practices

### Code Quality
- Use type hints (Python: type annotations; TypeScript: proper types)
- Write clear docstrings/JSDoc comments
- Keep functions focused and single-purpose
- Use consistent naming conventions

### Performance
- Implement caching for frequently accessed data
- Batch operations when possible
- Use async/await for I/O operations
- Monitor tool execution time

### Reliability
- Implement proper error handling and recovery
- Add retry logic for transient failures
- Log detailed information for debugging
- Test with real-world data volumes

### Security
- Validate all input parameters
- Use environment variables for secrets
- Implement rate limiting if needed
- Sanitize outputs before returning to Claude

## Reference Files

- `reference/python_mcp_server.md` — Complete Python SDK reference with detailed examples
- `reference/nodejs_mcp_server.md` — Complete Node.js SDK reference with TypeScript patterns
- `reference/tool_design_patterns.md` — Common patterns for different tool types
- `reference/deployment_guide.md` — Production deployment checklist

## Common Issues and Solutions

| Issue | Solution |
|---|---|
| Tool not appearing in Claude | Check that tool is properly registered with server |
| Timeouts | Check tool implementation for blocking I/O; use async operations |
| Authentication failures | Verify API keys and credentials in environment variables |
| Large dataset errors | Implement pagination or streaming for large responses |

