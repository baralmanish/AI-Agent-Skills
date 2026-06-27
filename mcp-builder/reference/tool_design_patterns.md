# MCP Tool Design Patterns

## Overview

This guide shows common patterns for implementing tools in MCP servers, with production-ready code examples for Python and Node.js.

---

## 1. Simple Calculation Tool

### Use Case
Math operations, unit conversions, format transformations

### Pattern: Python
```python
@server.tool()
def calculate_discount(price: float, discount_percent: float) -> str:
    """
    Calculate discounted price.
    
    Args:
        price: Original price
        discount_percent: Discount percentage (0-100)
    
    Returns:
        Formatted result with original and discounted prices
    """
    if price < 0:
        return "Error: Price cannot be negative"
    if not 0 <= discount_percent <= 100:
        return "Error: Discount must be between 0-100"
    
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    
    return f"Original: ${price:.2f} | Discount: {discount_percent}% | Final: ${final_price:.2f}"
```

### Pattern: Node.js
```typescript
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "calculate_discount") {
    const { price, discount_percent } = request.params.arguments as {
      price: number;
      discount_percent: number;
    };

    if (price < 0) {
      return {
        content: [{ type: "text", text: "Error: Price cannot be negative" }],
        isError: true,
      };
    }
    if (discount_percent < 0 || discount_percent > 100) {
      return {
        content: [{ type: "text", text: "Error: Discount must be 0-100" }],
        isError: true,
      };
    }

    const discountAmount = price * (discount_percent / 100);
    const finalPrice = price - discountAmount;

    return {
      content: [
        {
          type: "text",
          text: `Original: $${price.toFixed(2)} | Discount: ${discount_percent}% | Final: $${finalPrice.toFixed(2)}`,
        },
      ],
    };
  }
});
```

---

## 2. Data Query Tool

### Use Case
Database queries, API calls, data filtering and retrieval

### Pattern: Python
```python
import sqlite3
import json

@server.tool()
def query_customers(status: str = "active", limit: int = 10) -> str:
    """
    Query customers by status.
    
    Args:
        status: Customer status (active, inactive, pending)
        limit: Maximum results (1-100)
    
    Returns:
        JSON array of matching customers
    """
    valid_statuses = ["active", "inactive", "pending"]
    if status not in valid_statuses:
        return f"Error: Status must be one of {valid_statuses}"
    
    if not 1 <= limit <= 100:
        return "Error: Limit must be between 1-100"
    
    try:
        conn = sqlite3.connect(":memory:")  # Use actual DB in production
        cursor = conn.cursor()
        
        query = "SELECT id, name, email, status FROM customers WHERE status = ? LIMIT ?"
        cursor.execute(query, (status, limit))
        
        columns = [desc[0] for desc in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        conn.close()
        return json.dumps({"count": len(results), "data": results})
    except Exception as e:
        return json.dumps({"error": str(e)})
```

### Pattern: Node.js
```typescript
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "query_customers") {
    const { status = "active", limit = 10 } = request.params.arguments as {
      status?: string;
      limit?: number;
    };

    const validStatuses = ["active", "inactive", "pending"];
    if (!validStatuses.includes(status)) {
      return {
        content: [
          {
            type: "text",
            text: `Error: Status must be one of ${validStatuses.join(", ")}`,
          },
        ],
        isError: true,
      };
    }

    if (limit < 1 || limit > 100) {
      return {
        content: [
          { type: "text", text: "Error: Limit must be between 1-100" },
        ],
        isError: true,
      };
    }

    try {
      // Replace with actual DB call
      const customers = await db.query(
        "SELECT id, name, email, status FROM customers WHERE status = ? LIMIT ?",
        [status, limit]
      );

      return {
        content: [
          {
            type: "text",
            text: JSON.stringify({ count: customers.length, data: customers }),
          },
        ],
      };
    } catch (error) {
      return {
        content: [
          {
            type: "text",
            text: JSON.stringify({ error: error instanceof Error ? error.message : "Unknown error" }),
          },
        ],
        isError: true,
      };
    }
  }
});
```

---

## 3. File Operation Tool

### Use Case
Read/write files, process documents, transform file formats

### Pattern: Python
```python
import os
from pathlib import Path

@server.tool()
def read_file_safe(filename: str) -> str:
    """
    Read file contents safely.
    
    Args:
        filename: File name (relative to safe directory)
    
    Returns:
        File contents or error message
    """
    safe_dir = Path("/app/data")
    requested_file = safe_dir / filename
    
    # Security: ensure file is within safe directory
    try:
        requested_file.resolve().relative_to(safe_dir.resolve())
    except ValueError:
        return "Error: Access denied - file outside safe directory"
    
    if not requested_file.exists():
        return f"Error: File not found: {filename}"
    
    if not requested_file.is_file():
        return "Error: Path is not a file"
    
    try:
        with open(requested_file, "r", encoding="utf-8") as f:
            contents = f.read()
        
        size_kb = len(contents) / 1024
        if size_kb > 10000:
            return f"Error: File too large ({size_kb:.1f} KB, max 10MB)"
        
        return contents
    except UnicodeDecodeError:
        return "Error: File is not UTF-8 text"
    except Exception as e:
        return f"Error: {str(e)}"
```

### Pattern: Node.js
```typescript
import fs from "fs/promises";
import path from "path";

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "read_file_safe") {
    const { filename } = request.params.arguments as { filename: string };
    const safeDir = "/app/data";
    const requestedFile = path.join(safeDir, filename);

    // Security: ensure file is within safe directory
    const resolved = path.resolve(requestedFile);
    if (!resolved.startsWith(safeDir)) {
      return {
        content: [
          {
            type: "text",
            text: "Error: Access denied - file outside safe directory",
          },
        ],
        isError: true,
      };
    }

    try {
      const stats = await fs.stat(resolved);

      if (!stats.isFile()) {
        return {
          content: [{ type: "text", text: "Error: Path is not a file" }],
          isError: true,
        };
      }

      if (stats.size > 10 * 1024 * 1024) {
        return {
          content: [
            {
              type: "text",
              text: `Error: File too large (${(stats.size / 1024 / 1024).toFixed(1)} MB, max 10MB)`,
            },
          ],
          isError: true,
        };
      }

      const contents = await fs.readFile(resolved, "utf-8");
      return { content: [{ type: "text", text: contents }] };
    } catch (error) {
      return {
        content: [
          {
            type: "text",
            text: `Error: ${error instanceof Error ? error.message : "Unknown error"}`,
          },
        ],
        isError: true,
      };
    }
  }
});
```

---

## 4. API Integration Tool

### Use Case
Call external APIs, fetch web data, integrate with third-party services

### Pattern: Python
```python
import aiohttp
import asyncio
from typing import Optional

@server.tool()
async def fetch_api_data(
    url: str,
    method: str = "GET",
    timeout: int = 10,
    headers: Optional[dict] = None
) -> str:
    """
    Fetch data from an external API.
    
    Args:
        url: API endpoint URL
        method: HTTP method (GET, POST)
        timeout: Request timeout in seconds
        headers: Optional custom headers
    
    Returns:
        JSON response or error
    """
    if not url.startswith(("http://", "https://")):
        return "Error: URL must start with http:// or https://"
    
    if method not in ["GET", "POST"]:
        return "Error: Method must be GET or POST"
    
    if timeout < 1 or timeout > 60:
        return "Error: Timeout must be between 1-60 seconds"
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.request(
                method,
                url,
                headers=headers or {},
                timeout=aiohttp.ClientTimeout(total=timeout)
            ) as response:
                if response.status >= 400:
                    return f"Error: HTTP {response.status}"
                
                data = await response.json()
                return json.dumps(data)
    except asyncio.TimeoutError:
        return "Error: Request timed out"
    except Exception as e:
        return f"Error: {str(e)}"
```

### Pattern: Node.js
```typescript
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "fetch_api_data") {
    const {
      url,
      method = "GET",
      timeout = 10,
      headers = {},
    } = request.params.arguments as {
      url: string;
      method?: string;
      timeout?: number;
      headers?: Record<string, string>;
    };

    if (!url.startsWith("http://") && !url.startsWith("https://")) {
      return {
        content: [
          {
            type: "text",
            text: "Error: URL must start with http:// or https://",
          },
        ],
        isError: true,
      };
    }

    if (!["GET", "POST"].includes(method)) {
      return {
        content: [{ type: "text", text: "Error: Method must be GET or POST" }],
        isError: true,
      };
    }

    if (timeout < 1 || timeout > 60) {
      return {
        content: [
          { type: "text", text: "Error: Timeout must be between 1-60 seconds" },
        ],
        isError: true,
      };
    }

    try {
      const controller = new AbortController();
      const id = setTimeout(() => controller.abort(), timeout * 1000);

      const response = await fetch(url, {
        method,
        headers,
        signal: controller.signal,
      });

      clearTimeout(id);

      if (!response.ok) {
        return {
          content: [{ type: "text", text: `Error: HTTP ${response.status}` }],
          isError: true,
        };
      }

      const data = await response.json();
      return {
        content: [{ type: "text", text: JSON.stringify(data) }],
      };
    } catch (error) {
      return {
        content: [
          {
            type: "text",
            text: `Error: ${error instanceof Error ? error.message : "Unknown error"}`,
          },
        ],
        isError: true,
      };
    }
  }
});
```

---

## 5. Multi-Step Workflow Tool

### Use Case
Complex processes, data transformation pipelines, multi-step operations

### Pattern: Python
```python
from enum import Enum

class WorkflowStep(Enum):
    VALIDATE = "validate"
    PROCESS = "process"
    STORE = "store"

@server.tool()
async def process_document(
    document_id: str,
    action: str = "full"
) -> str:
    """
    Process document through workflow.
    
    Args:
        document_id: ID of document to process
        action: "full" for all steps, or specific step
    
    Returns:
        Workflow result with status
    """
    valid_actions = ["validate", "process", "store", "full"]
    if action not in valid_actions:
        return f"Error: Action must be one of {valid_actions}"
    
    result = {"document_id": document_id, "steps": []}
    
    try:
        # Step 1: Validate
        if action in ["validate", "full"]:
            validation = validate_document(document_id)
            result["steps"].append({
                "step": "validate",
                "status": "success" if validation else "failed",
                "details": validation or "Document invalid"
            })
            if not validation and action == "full":
                return json.dumps(result)
        
        # Step 2: Process
        if action in ["process", "full"]:
            processed = await process_content(document_id)
            result["steps"].append({
                "step": "process",
                "status": "success",
                "record_count": len(processed)
            })
        
        # Step 3: Store
        if action in ["store", "full"]:
            stored = await store_result(document_id)
            result["steps"].append({
                "step": "store",
                "status": "success",
                "timestamp": stored
            })
        
        result["status"] = "completed"
        return json.dumps(result)
    except Exception as e:
        result["status"] = "error"
        result["error"] = str(e)
        return json.dumps(result)
```

---

## 6. Caching and Performance Pattern

### Use Case
Expensive operations that repeat, data that doesn't change often

### Pattern: Python
```python
from functools import lru_cache
import time

@lru_cache(maxsize=128)
def expensive_lookup(query: str) -> str:
    """Compute with automatic caching."""
    time.sleep(2)  # Simulates expensive operation
    return f"Result for {query}"

@server.tool()
def get_cached_lookup(query: str) -> str:
    """Get lookup result (cached if available)."""
    cache_info = expensive_lookup.cache_info()
    result = expensive_lookup(query)
    
    return json.dumps({
        "result": result,
        "cache_hits": cache_info.hits,
        "cache_misses": cache_info.misses
    })
```

### Pattern: Node.js
```typescript
class CacheStore<T> {
  private store = new Map<string, { value: T; timestamp: number; ttl: number }>();

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

  clear() {
    this.store.clear();
  }
}

const cache = new CacheStore<string>();
```

