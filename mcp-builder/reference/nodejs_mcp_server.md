# Node.js MCP Server Implementation Guide

## Quick Start

### Installation
```bash
npm install @modelcontextprotocol/sdk
npm install -D typescript ts-node @types/node
```

### Minimal Example
```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { 
  ListToolsRequestSchema, 
  CallToolRequestSchema,
  TextContent 
} from "@modelcontextprotocol/sdk/types.js";

const server = new Server({
  name: "my-server",
  version: "1.0.0",
});

server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [
    {
      name: "greet",
      description: "Greet someone by name",
      inputSchema: {
        type: "object",
        properties: {
          name: { type: "string", description: "Person's name" },
        },
        required: ["name"],
      },
    },
  ],
}));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "greet") {
    const name = request.params.arguments.name;
    return {
      content: [{ type: "text" as const, text: `Hello, ${name}!` }],
    };
  }
  throw new Error("Unknown tool");
});

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("Server running on stdio");
}

main().catch(console.error);
```

## Server Setup

### Initialize Server
```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";

const server = new Server({
  name: "my-server",
  version: "1.0.0",
  capabilities: {
    tools: {},
    resources: {},
  },
});
```

### Register Transport
```typescript
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}
```

## Tool Implementation

### Basic Tool
```typescript
server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [
    {
      name: "add_numbers",
      description: "Add two numbers together",
      inputSchema: {
        type: "object" as const,
        properties: {
          a: { type: "number", description: "First number" },
          b: { type: "number", description: "Second number" },
        },
        required: ["a", "b"],
      },
    },
  ],
}));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "add_numbers") {
    const { a, b } = request.params.arguments as { a: number; b: number };
    const result = a + b;
    return {
      content: [
        {
          type: "text" as const,
          text: `${a} + ${b} = ${result}`,
        },
      ],
    };
  }
  throw new Error("Unknown tool");
});
```

### Tool with Complex Input
```typescript
interface ProcessDataParams {
  data: string;
  format: "json" | "csv" | "xml";
  limit?: number;
}

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "process_data") {
    const { data, format, limit } = request.params.arguments as ProcessDataParams;
    
    if (!["json", "csv", "xml"].includes(format)) {
      return {
        content: [
          {
            type: "text" as const,
            text: `Error: Unsupported format '${format}'`,
          },
        ],
        isError: true,
      };
    }
    
    try {
      const result = processData(data, format, limit);
      return {
        content: [{ type: "text" as const, text: JSON.stringify(result) }],
      };
    } catch (error) {
      return {
        content: [
          {
            type: "text" as const,
            text: `Error: ${error instanceof Error ? error.message : "Unknown error"}`,
          },
        ],
        isError: true,
      };
    }
  }
  throw new Error("Unknown tool");
});
```

## Resource Implementation

### Simple Resource
```typescript
import {
  ListResourcesRequestSchema,
  ReadResourceRequestSchema,
  ResourceContents,
} from "@modelcontextprotocol/sdk/types.js";

server.setRequestHandler(ListResourcesRequestSchema, async () => ({
  resources: [
    {
      uri: "config:///database",
      name: "Database Config",
      description: "Database configuration",
      mimeType: "application/json",
    },
    {
      uri: "config:///api",
      name: "API Config",
      description: "API configuration",
      mimeType: "application/json",
    },
  ],
}));

server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
  const uri = request.params.uri;

  let content: string;
  if (uri === "config:///database") {
    content = JSON.stringify({ host: "localhost", port: 5432 });
  } else if (uri === "config:///api") {
    content = JSON.stringify({ timeout: 30, retries: 3 });
  } else {
    throw new Error(`Unknown resource: ${uri}`);
  }

  return {
    contents: [
      {
        uri,
        mimeType: "application/json",
        text: content,
      },
    ],
  } as ResourceContents;
});
```

## Error Handling

### Structured Error Response
```typescript
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  try {
    if (request.params.name === "risky_operation") {
      const result = await performRiskyOperation(request.params.arguments);
      return {
        content: [{ type: "text" as const, text: JSON.stringify(result) }],
      };
    }
  } catch (error) {
    const errorMessage = error instanceof Error ? error.message : "Unknown error";
    console.error(`Tool error: ${errorMessage}`);
    
    return {
      content: [
        {
          type: "text" as const,
          text: JSON.stringify({ error: errorMessage }),
        },
      ],
      isError: true,
    };
  }
  throw new Error("Unknown tool");
});
```

## Input Validation

### Validate Tool Arguments
```typescript
interface FetchParams {
  url: string;
  timeout?: number;
  retries?: number;
}

function validateFetchParams(params: unknown): params is FetchParams {
  const p = params as Record<string, unknown>;
  
  if (typeof p.url !== "string" || !p.url.startsWith("http")) {
    throw new Error("Invalid URL");
  }
  
  if (p.timeout !== undefined && (typeof p.timeout !== "number" || p.timeout < 1)) {
    throw new Error("Timeout must be a positive number");
  }
  
  if (p.retries !== undefined && (typeof p.retries !== "number" || p.retries < 0)) {
    throw new Error("Retries must be non-negative");
  }
  
  return true;
}

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "fetch_data") {
    try {
      validateFetchParams(request.params.arguments);
      const { url, timeout = 10, retries = 3 } = request.params.arguments as FetchParams;
      
      const result = await fetchWithRetry(url, timeout, retries);
      return {
        content: [{ type: "text" as const, text: result }],
      };
    } catch (error) {
      return {
        content: [
          {
            type: "text" as const,
            text: `Error: ${error instanceof Error ? error.message : "Unknown error"}`,
          },
        ],
        isError: true,
      };
    }
  }
  throw new Error("Unknown tool");
});
```

## Async Operations

### Fetch from External API
```typescript
async function fetchFromAPI(url: string, timeout: number = 10000): Promise<string> {
  const controller = new AbortController();
  const id = setTimeout(() => controller.abort(), timeout);

  try {
    const response = await fetch(url, {
      signal: controller.signal,
      headers: {
        "User-Agent": "MCP-Server/1.0",
      },
    });

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    return await response.text();
  } finally {
    clearTimeout(id);
  }
}

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "fetch_url") {
    try {
      const { url } = request.params.arguments as { url: string };
      const data = await fetchFromAPI(url);
      
      return {
        content: [{ type: "text" as const, text: data }],
      };
    } catch (error) {
      return {
        content: [
          {
            type: "text" as const,
            text: `Error: ${error instanceof Error ? error.message : "Unknown error"}`,
          },
        ],
        isError: true,
      };
    }
  }
  throw new Error("Unknown tool");
});
```

## Logging and Debugging

### Configure Logging
```typescript
interface LogEntry {
  timestamp: Date;
  level: "debug" | "info" | "warn" | "error";
  message: string;
  data?: unknown;
}

const logs: LogEntry[] = [];

function log(
  level: "debug" | "info" | "warn" | "error",
  message: string,
  data?: unknown
) {
  const entry: LogEntry = { timestamp: new Date(), level, message, data };
  logs.push(entry);
  console.error(`[${level.toUpperCase()}] ${message}`, data || "");
}

// Use in tools:
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  log("info", `Tool called: ${request.params.name}`);
  
  if (request.params.name === "debug_tool") {
    log("debug", "Debug tool executed", request.params.arguments);
    return {
      content: [{ type: "text" as const, text: "OK" }],
    };
  }
  
  throw new Error("Unknown tool");
});
```

## Performance Optimization

### Caching Results
```typescript
interface CacheEntry<T> {
  value: T;
  timestamp: number;
  ttl: number;
}

class Cache<T> {
  private store = new Map<string, CacheEntry<T>>();

  set(key: string, value: T, ttlMs: number = 5 * 60 * 1000) {
    this.store.set(key, {
      value,
      timestamp: Date.now(),
      ttl: ttlMs,
    });
  }

  get(key: string): T | null {
    const entry = this.store.get(key);
    if (!entry) return null;

    if (Date.now() - entry.timestamp > entry.ttl) {
      this.store.delete(key);
      return null;
    }

    return entry.value;
  }
}

const cache = new Cache<string>();

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "get_cached_data") {
    const { key } = request.params.arguments as { key: string };
    
    // Check cache first
    const cached = cache.get(key);
    if (cached) {
      return {
        content: [{ type: "text" as const, text: cached }],
      };
    }

    // Fetch if not cached
    const data = await fetchData(key);
    cache.set(key, data);

    return {
      content: [{ type: "text" as const, text: data }],
    };
  }
  throw new Error("Unknown tool");
});
```

## Testing Tools Locally

### Unit Test Example (using Jest)
```typescript
describe("MCP Tools", () => {
  it("should greet with correct name", async () => {
    // Mock the server request
    const result = {
      content: [{ type: "text" as const, text: "Hello, Alice!" }],
    };
    
    expect(result.content[0].text).toBe("Hello, Alice!");
  });

  it("should handle errors gracefully", async () => {
    const result = {
      content: [
        {
          type: "text" as const,
          text: JSON.stringify({ error: "Invalid input" }),
        },
      ],
      isError: true,
    };
    
    expect(result.isError).toBe(true);
  });
});
```

## Deployment

### Package.json
```json
{
  "name": "my-mcp-server",
  "version": "1.0.0",
  "type": "module",
  "main": "build/server.js",
  "scripts": {
    "build": "tsc",
    "start": "node build/server.js",
    "dev": "ts-node src/server.ts"
  },
  "dependencies": {
    "@modelcontextprotocol/sdk": "^0.5.0"
  },
  "devDependencies": {
    "@types/node": "^20.0.0",
    "typescript": "^5.0.0",
    "ts-node": "^10.0.0"
  }
}
```

### Docker Deployment
```dockerfile
FROM node:20-slim

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY src ./src
COPY tsconfig.json .

RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
```

