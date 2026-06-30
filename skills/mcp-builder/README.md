# MCP Builder Skill

Generate and deploy production-ready Model Context Protocol (MCP) servers.

## Overview

This skill provides comprehensive guidance for building, testing, and deploying MCP servers that extend Claude's capabilities with custom tools and resources.

Use this skill when you want to:

- Create a new MCP server with custom tools
- Add new tools to an existing MCP server
- Implement resources for data access
- Deploy an MCP server to production
- Debug or optimize an existing server

## Sample Prompts

### Create a Simple MCP Server

```text
Build an MCP server with these tools:
1. weather - Get current weather for a city
2. forecast - Get 7-day weather forecast
3. alerts - Get weather alerts for a region

Use Python with FastMCP for speed.
Include proper error handling and logging.
```

### Data Access Server

```text
Build an MCP server that provides database access.
Tools needed:
- query_database(sql: string) - Execute SQL queries
- get_tables() - List available tables
- describe_table(table: string) - Get table schema

Connect to PostgreSQL.
Include query validation and result limits for safety.
```

### API Integration Server

```text
Create an MCP server that integrates with the GitHub API.
Implement these tools:
- search_repos(query, language, sort) - Search GitHub repositories
- get_repo_details(owner, repo) - Get repo info
- list_issues(owner, repo, state) - List repository issues
- create_issue(owner, repo, title, body) - Create a new issue

Use Node.js with proper authentication.
Include rate limiting awareness.
```

### File Processing Server

```text
Build an MCP server for document processing.
Tools:
- extract_text(file_path) - Extract text from PDF/DOCX
- convert_format(input_path, output_format) - Convert between formats
- analyze_document(file_path) - Get document statistics

Use Python and support PDF, DOCX, TXT, Markdown.
Validate file paths for security.
```

### Code Analysis Server

```text
Create an MCP server for code analysis and metrics.
Implement:
- analyze_code(file_path) - Get code metrics (complexity, LOC, etc.)
- find_issues(directory) - Identify common code issues
- suggest_improvements(file_path) - Suggest code improvements
- lint_check(file_path, language) - Run linting rules

Support Python, JavaScript, TypeScript, Go.
```

### Custom Business Logic

```text
Build an MCP server for our business operations.
Tools needed:
- get_employee(id) - Retrieve employee info
- list_projects(status, team) - List projects
- create_task(title, description, assignee) - Create task
- update_status(task_id, status) - Update task status
- get_metrics(date_range) - Get business metrics

Connect to our internal database.
Include access control and audit logging.
```

## Process

### Quick Start (5 minutes)

1. Choose language (Python recommended for speed, Node.js for web integrations)
2. Define 3-5 core tools your server will expose
3. Generate skeleton code with proper structure
4. Test locally with sample inputs

### Full Implementation (30-60 minutes)

1. Plan server architecture and tool design
2. Study MCP documentation and patterns
3. Implement core tools with error handling
4. Add resources if needed
5. Write comprehensive tests
6. Deploy and validate

## Technology Choices

| Language       | Best For                           | Speed     | Complexity  |
| -------------- | ---------------------------------- | --------- | ----------- |
| **Python**     | Data processing, AI, scientific    | Fast      | Low-Medium  |
| **Node.js**    | Web APIs, real-time, JavaScript    | Medium    | Medium      |
| **TypeScript** | Type-safe Node.js, large projects  | Medium    | Medium-High |
| **Go**         | High-performance, concurrent tools | Very Fast | High        |

## Reference Files

| File                                | Purpose                                     |
| ----------------------------------- | ------------------------------------------- |
| `SKILL.md`                          | Complete MCP server implementation guide    |
| `reference/python_mcp_server.md`    | Python SDK reference with 20+ code examples |
| `reference/nodejs_mcp_server.md`    | Node.js/TypeScript reference with patterns  |
| `reference/tool_design_patterns.md` | Common tool patterns by use case            |
| `reference/deployment_guide.md`     | Production deployment checklist             |

## Common Tool Patterns

| Pattern              | Example                                | Complexity  |
| -------------------- | -------------------------------------- | ----------- |
| Simple Calculation   | Math operations, string transforms     | Low         |
| Data Retrieval       | Database queries, API calls            | Medium      |
| External Integration | Third-party API wrappers               | Medium      |
| File Operations      | Read/write/transform files             | Medium-High |
| Complex Workflows    | Multi-step processes, state management | High        |

## Deployment Options

- **Local Development**: Run directly on your machine
- **Docker**: Containerized deployment for consistency
- **Cloud Functions**: AWS Lambda, Google Cloud Functions
- **Cloud VMs**: EC2, GCE, DigitalOcean
- **Anthropic Claude**: Register with Anthropic for use in Claude

## Best Practices

### Code Quality

✅ Type hints (Python) / TypeScript types  
✅ Clear docstrings / JSDoc comments  
✅ Single-purpose functions  
✅ Comprehensive error handling

### Performance

✅ Async/await for I/O operations  
✅ Caching for frequently accessed data  
✅ Batch operations where possible  
✅ Monitor tool execution time

### Reliability

✅ Retry logic for transient failures  
✅ Structured logging  
✅ Input validation  
✅ Security review

### Security

✅ Validate all inputs  
✅ Use environment variables for secrets  
✅ Implement rate limiting  
✅ Sanitize outputs before returning

## Debugging Tips

| Issue                | Solution                                        |
| -------------------- | ----------------------------------------------- |
| Tool not appearing   | Check tool registration with server             |
| Timeouts             | Use async operations; check for blocking I/O    |
| Auth failures        | Verify environment variables; check credentials |
| Large dataset errors | Implement pagination or streaming               |
| Memory leaks         | Monitor tool execution; implement cleanup       |

## Getting Started

1. Read `SKILL.md` for overview
2. Choose Python or Node.js based on your needs
3. Read appropriate language guide (`python_mcp_server.md` or `nodejs_mcp_server.md`)
4. Implement your server following the patterns
5. Test locally with sample inputs
6. Deploy using provided deployment guide
