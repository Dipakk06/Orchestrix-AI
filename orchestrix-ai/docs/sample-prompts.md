# Sample Prompts

1. "Plan a 2-week learning roadmap for Kubernetes and execute the first task."
2. "Remember that I prefer concise responses and summarize today's project updates."
3. "Run calculator tool: (425 * 1.08) - 20"
4. "Draft an email to my team with project status."

# API Examples

```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"user_id":"demo-user","message":"Hello Orchestrix"}'
```

```bash
curl -X POST http://localhost:8000/api/agent/run \
  -H "Content-Type: application/json" \
  -d '{"user_id":"demo-user","task":"Research latest GPU pricing trends"}'
```
