# awesome-aisquare

Audit, trust, and governance infrastructure for agentic AI systems.

[![GitHub stars](https://img.shields.io/github/stars/AISquare-Studio/awesome-aisquare?style=flat-square)](https://github.com/AISquare-Studio/awesome-aisquare/stargazers)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue?style=flat-square)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-aisquare.studio-green?style=flat-square)](https://docs.aisquare.studio)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)

## What is AISquare

AISquare is the governance layer for AI agents. It records *why* decisions are made, enforces policies on what agents can do, and gives humans structured workflows to review, approve, or intervene — all without replacing your existing agent framework. Think of it as the system of record for AI decisions, the same way financial systems track transactions.

This repo is your starting point.

## Ecosystem map

| Repo | What it does | Status | Stars |
|------|-------------|--------|-------|
| **[awesome-aisquare](https://github.com/AISquare-Studio/awesome-aisquare)** | You are here. Ecosystem hub, quickstarts, and links. | Active | [![Stars](https://img.shields.io/github/stars/AISquare-Studio/awesome-aisquare?style=flat-square&label=)](https://github.com/AISquare-Studio/awesome-aisquare) |
| **[AISquare-Studio-QA](https://github.com/AISquare-Studio/AISquare-Studio-QA)** | AI-powered GitHub Action — write tests in plain English, get production-ready Playwright tests back. | Active | [![Stars](https://img.shields.io/github/stars/AISquare-Studio/AISquare-Studio-QA?style=flat-square&label=)](https://github.com/AISquare-Studio/AISquare-Studio-QA) |
| **[django-ais](https://github.com/AISquare-Studio/django-ais)** | Django-native orchestration for agentic workflows. DB-backed jobs, YAML pipelines, real-time event streaming. | Pre-release | [![Stars](https://img.shields.io/github/stars/AISquare-Studio/django-ais?style=flat-square&label=)](https://github.com/AISquare-Studio/django-ais) |
| `aisquare-examples` | Runnable use-case examples | Coming soon | — |
| `aisquare-templates` | Starter scaffolds for governed AI apps | Coming soon | — |
| `aisquare-integrations` | Adapters for LangChain, CrewAI, AutoGen, and more | Coming soon | — |

## Quick links

[Documentation](https://docs.aisquare.studio) · [API Reference](https://docs.aisquare.studio/api-reference) · [Website](https://aisquare.studio) · [Feedback](https://feedback.aisquare.studio) · [Contributing](CONTRIBUTING.md)

## Get started in 5 minutes

### AutoQA — AI-powered test generation

Turn plain-English test descriptions in your PRs into Playwright tests.

**1. Add the workflow** to `.github/workflows/autoqa.yml`:

```yaml
name: AutoQA
on:
  pull_request:
    types: [opened, edited, synchronize]

jobs:
  autoqa:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: AISquare-Studio/AISquare-Studio-QA@main
        with:
          openai_api_key: ${{ secrets.OPENAI_API_KEY }}
          staging_url: ${{ secrets.STAGING_URL }}
          mode: generate
```

**2. Configure secrets** — add `OPENAI_API_KEY` and `STAGING_URL` to your repo's GitHub Actions secrets.

**3. Write tests in your PR body** using an `autoqa` block:

````markdown
```autoqa
1. Navigate to the login page
2. Enter valid credentials
3. Verify the dashboard loads
```
````

Open the PR. AutoQA generates and commits Playwright tests automatically. Modes: `generate`, `suite`, `all`.

Full docs: [AISquare-Studio-QA](https://github.com/AISquare-Studio/AISquare-Studio-QA)

---

### django-ais — Django-native agent orchestration

Orchestrate agentic workflows inside your existing Django stack — Postgres, Celery, Channels, ORM. No new infrastructure.

> **Note:** django-ais is in pre-release. The API may change.

```bash
pip install django-ais
```

```python
# settings.py
INSTALLED_APPS = [
    ...
    "django_ais",
]

# workers.py
from django_ais import Worker

class SummaryWorker(Worker):
    name = "summarizer"

    def execute(self, job):
        # Your agent logic here
        return {"summary": summarize(job.payload["text"])}
```

Define workflows in YAML, stream events over SSE/WebSocket, and manage jobs through the Django ORM.

Full docs: [django-ais](https://github.com/AISquare-Studio/django-ais)

## How the pieces fit together

```
┌─────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│   Your Agent    │────▶│  AISquare Gov't  │────▶│     AutoQA       │
│ (any framework) │     │ (audit + policy) │     │ (test generation)│
└─────────────────┘     └──────────────────┘     └──────────────────┘
                                │
                                ▼
                        ┌──────────────────┐
                        │    django-ais    │
                        │ (orchestration)  │
                        └──────────────────┘
```

Your agent framework handles reasoning. AISquare handles governance — recording decisions, enforcing policies, and routing to human review. AutoQA validates behavior through generated tests. django-ais orchestrates multi-step workflows inside Django.

## Roadmap

- **aisquare-examples** — Runnable examples for common governance scenarios
- **aisquare-templates** — Starter scaffolds for governed AI applications
- **aisquare-integrations** — Adapters for LangChain, CrewAI, AutoGen, and other frameworks
- **AISquare SDK** — Client libraries for direct API integration

## LLM-friendly docs

This repo ships [`llms.txt`](llms.txt) and [`llms-full.txt`](llms-full.txt) — structured text files designed for AI-native developer tools. Paste the raw URL into Cursor's `@Docs`, feed it to Claude or ChatGPT for project context, or use it with any tool that consumes plain-text documentation.

## Contributing

We welcome contributions across the entire ecosystem. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Issues tagged **"good first issue"** across all repos in the [AISquare-Studio org](https://github.com/AISquare-Studio) are a great entry point.

## Community and support

- [Feedback board](https://feedback.aisquare.studio) — Feature requests and bug reports
- [Documentation](https://docs.aisquare.studio) — Guides, API reference, and tutorials
- [GitHub Discussions](https://github.com/orgs/AISquare-Studio/discussions) — Questions and community conversation
- Email: [bots@aisquare.com](mailto:bots@aisquare.com)

## License

This project is licensed under [Apache-2.0](LICENSE).
