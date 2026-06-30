# MCP Builder — Quick Reference

## Triggers

- "Build an MCP server with [purpose]"
- "Create tools for [domain]"
- "Add these tools to an MCP: [list]"
- "Deploy an MCP server to [platform]"
- "Debug MCP server [symptom]"

## Language Quick Pick

| Language             | Best For                 | Time to Deploy | Example                                 |
| -------------------- | ------------------------ | -------------- | --------------------------------------- |
| **Python + FastMCP** | Data, AI, simple logic   | ~5 mins        | `pip install mcp`                       |
| **Node.js + SDK**    | APIs, web integrations   | ~10 mins       | `npm install @modelcontextprotocol/sdk` |
| **TypeScript + SDK** | Large, type-safe servers | ~15 mins       | Full type coverage                      |

## Tool Design Template

```
Name: [tool_name]
Purpose: [What it does]
Inputs: [param1: type, param2: type]
Output: [Return format]
Errors: [What can go wrong]
Example: [Usage example]
```

## Common Tool Patterns

| Pattern      | Complexity | Example                                   |
| ------------ | ---------- | ----------------------------------------- |
| Calculation  | 🟢 Low     | Math, string transform, format conversion |
| Data Query   | 🟡 Medium  | Database query, API call, list filtering  |
| File I/O     | 🟡 Medium  | Read/write file, process document         |
| External API | 🟡 Medium  | REST client, SDK wrapper                  |
| Workflow     | 🔴 High    | Multi-step process, state management      |

## Python MCP Quickstart

```python
from mcp.server.fastmcp import FastMCP

server = FastMCP("my-server")

@server.tool()
def my_tool(param: str) -> str:
    """Tool description."""
    return result

if __name__ == "__main__":
    server.run()
```

## Node.js MCP Quickstart

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server({ name: "my-server", version: "1.0.0" });

server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [
    {
      name: "my_tool",
      description: "Tool description",
      inputSchema: {
        type: "object",
        properties: { param: { type: "string" } },
        required: ["param"],
      },
    },
  ],
}));

const transport = new StdioServerTransport();
await server.connect(transport);
```

## Error Handling Pattern

```python
# Python
try:
    result = dangerous_operation(input)
    return {"success": True, "result": result}
except ValueError as e:
    return {"error": f"Invalid input: {e}"}
except Exception as e:
    logging.error(f"Unexpected error: {e}")
    return {"error": "An error occurred"}
```

```typescript
// Node.js
try {
  const result = await dangerousOperation(input);
  return { content: [{ type: "text", text: result }] };
} catch (error) {
  return {
    content: [
      {
        type: "text",
        text: `Error: ${error instanceof Error ? error.message : "Unknown"}`,
      },
    ],
    isError: true,
  };
}
```

## Input Validation Quick Checks

✅ **Type Check**: `isinstance(x, str)` (Python) / `typeof x === "string"` (JS)  
✅ **Range Check**: `1 <= limit <= 100`  
✅ **Format Check**: URL, email, regex patterns  
✅ **Length Check**: `len(query) > 0 and len(query) < 1000`  
✅ **Enum Check**: `status in ["active", "inactive", "pending"]`

## Deployment Checklist

- [ ] Environment variables configured
- [ ] Secrets in .env file (never committed)
- [ ] Error handling comprehensive
- [ ] Logging configured
- [ ] Input validation in place
- [ ] Rate limiting considered
- [ ] Security review done
- [ ] Tests written and passing
- [ ] Docker image builds
- [ ] Deployment platform setup

## Deployment Targets

| Target           | Command                           | Notes             |
| ---------------- | --------------------------------- | ----------------- |
| Local            | `python server.py` or `npm start` | Development       |
| Docker           | `docker build && docker run`      | Consistency       |
| AWS Lambda       | Use `aws lambda create-function`  | Serverless        |
| Google Cloud Run | `gcloud run deploy`               | Serverless        |
| Render/Railway   | Git push to deploy                | Simple PaaS       |
| Anthropic Claude | Register at Anthropic             | For use in Claude |

## Testing Quick Pattern

```python
# Python with pytest
@pytest.mark.asyncio
async def test_my_tool():
    result = await my_tool("test_input")
    assert "expected" in result
```

```typescript
// Node.js with Jest
describe("My Tool", () => {
  it("should return expected output", async () => {
    const result = await myTool("test_input");
    expect(result.content[0].text).toContain("expected");
  });
});
```

## Common Issues & Fixes

| Issue            | Cause               | Fix                                       |
| ---------------- | ------------------- | ----------------------------------------- |
| Tool not in list | Not registered      | Add to `@server.tool()` decorator         |
| Timeout errors   | Blocking I/O        | Use async/await, add timeouts             |
| Auth failures    | Missing credentials | Set environment variables                 |
| Memory issues    | Large datasets      | Implement pagination                      |
| Slow performance | No caching          | Add `@lru_cache` (Python) or cache object |

## Performance Tips

⚡ **Use Async**: All I/O should be async (API calls, DB queries)  
💾 **Cache Results**: Use caching for repeated queries  
📦 **Batch Operations**: Process multiple items together  
🔍 **Validate Input Early**: Fail fast on bad input  
📊 **Monitor Latency**: Log execution time  
🎯 **Limit Results**: Cap returned data (e.g., max 100 rows)

## File Structure

```
my-mcp-server/
├── server.py (or server.ts)
├── requirements.txt (or package.json)
├── .env.example
├── Dockerfile
└── tests/
    └── test_server.py
```

## Resource vs Tool

| Aspect       | Tool                  | Resource                       |
| ------------ | --------------------- | ------------------------------ |
| **Purpose**  | Action/computation    | Data access                    |
| **Input**    | Parameters            | URI                            |
| **Use Case** | "Calculate this"      | "Read this file"               |
| **Example**  | calculate_tax(income) | read_config("app:///settings") |
