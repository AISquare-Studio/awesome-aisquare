# awesome-aisquare

<div align="center">
  <!-- Replace the URL below with your own demo GIF or screenshot -->
  <img src="banner.png" width="100%" alt="AISquare in action"/>
</div>

<br/>

Audit, trust, and governance infrastructure for agentic AI systems.

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/AISquare-Studio/awesome-aisquare?style=flat-square)](https://github.com/AISquare-Studio/awesome-aisquare/stargazers)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue?style=flat-square)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-aisquare.studio-green?style=flat-square)](https://docs.aisquare.studio)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)

</div>

## What is AISquare

Your AI agents are making decisions. Hopefully good ones. But can you prove it?

AISquare is the governance layer for AI agents. It records *why* decisions are made, enforces policies on what agents can do, and gives humans structured workflows to review, approve, or intervene — without replacing your existing agent framework. Think of it as the system of record for AI decisions, the same way financial systems track transactions. Except the transactions are "the AI decided to email your CEO at 3 AM."

This repo is your starting point.

## Ecosystem map

Click on a card to explore the project. ⭐ Star your favorites to show support!

<div align="center">
  <a href="https://github.com/AISquare-Studio/awesome-aisquare">
    <img src="./profile/pin-awesome-aisquare.svg" alt="awesome-aisquare"/>
  </a>
</div>

<div align="center">
  <a href="https://github.com/AISquare-Studio/AISquare-Studio-QA">
    <img src="./profile/pin-aisquare-studio-qa.svg" alt="AISquare-Studio-QA"/>
  </a>
  &nbsp;&nbsp;
  <a href="https://github.com/AISquare-Studio/aisquare-cli">
    <img src="./profile/pin-aisquare-cli.svg" alt="aisquare-cli"/>
  </a>
</div>

<div align="center">
  <a href="https://github.com/AISquare-Studio/pipe">
    <img src="./profile/pin-pipe.svg" alt="pipe"/>
  </a>
</div>

### 📋 Case study

<div align="center">
  <a href="https://on-anmols-mind.aisquare.studio/s/?type=note&id=4425&rid=990&ruid=0daa89e6-a7fd-40fc-9341-9db1c671a96a">
    <img src="dramatyze.png" width="100%" alt="Dramatyze platform screenshot" style="border-radius: 12px;"/>
  </a>
  <br/><br/>
  <a href="https://on-anmols-mind.aisquare.studio/s/?type=note&id=4425&rid=990&ruid=0daa89e6-a7fd-40fc-9341-9db1c671a96a"><img src="https://img.shields.io/badge/Dramatyze-Case_study:_AI_governance_in_action-58a6ff?style=for-the-badge" alt="Dramatyze Case Study"/></a>
</div>

### 🔜 Coming soon

<div align="center">

| Project | Description |
|:--------|:------------|
| **aisquare-examples** | Runnable governance scenario examples |
| **aisquare-templates** | Starter scaffolds for governed AI apps |
| **aisquare-integrations** | Adapters for LangChain, CrewAI, AutoGen |
| **AISquare SDK** | Client libraries for direct API integration |

</div>

## Quick links

<div align="center">
  <a href="https://docs.aisquare.studio"><img src="https://img.shields.io/badge/📖_Documentation-docs.aisquare.studio-2563eb?style=for-the-badge" alt="Documentation"/></a>
  <a href="https://docs.aisquare.studio/docs/api-reference/overview"><img src="https://img.shields.io/badge/🔌_API_Reference-docs.aisquare.studio-7c3aed?style=for-the-badge" alt="API Reference"/></a>
  <a href="https://aisquare.studio"><img src="https://img.shields.io/badge/🌐_Website-aisquare.studio-0d9488?style=for-the-badge" alt="Website"/></a>
  <a href="https://feedback.aisquare.studio"><img src="https://img.shields.io/badge/💬_Feedback-feedback.aisquare.studio-ea580c?style=for-the-badge" alt="Feedback"/></a>
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/🤝_Contributing-guidelines-16a34a?style=for-the-badge" alt="Contributing"/></a>
</div>

## Get started in 5 minutes

### AutoQA — AI-powered test generation

Turn plain-English test descriptions in your PRs into Playwright tests. Yes, really.

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

Open the PR. AutoQA generates and commits Playwright tests automatically. Modes: `generate` (single test), `suite` (full suite), `all` (everything).

Full docs: [AISquare-Studio-QA](https://github.com/AISquare-Studio/AISquare-Studio-QA)

---

### aisquare-cli — one terminal over your coding agents

Task a manager agent in plain words and it plans, spawns coders, testers and reviewers, and loops until the goal is met. Underneath, agents get a memory that persists your preferences and each project's conventions across sessions, so every session starts oriented instead of cold.

```bash
UV_PYTHON_DOWNLOADS=automatic uv tool install --python 3.13 aisquare-cli
cd path/to/your/repo
aisquare init --local --agent claude-code
```

Full docs: [aisquare-cli](https://github.com/AISquare-Studio/aisquare-cli)

---

### pipe — anything-to-anything connectors

Instead of building N² bespoke integrations, each service implements a single Source and/or Sink against a universal `DataEnvelope` spec. The framework handles type matching, pipeline orchestration and plugin discovery.

```bash
pip install "aisquare-pipe[popular]"
```

Full docs: [pipe](https://github.com/AISquare-Studio/pipe)

## How the pieces fit together

```
┌─────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│   Your Agent    │────▶│  AISquare Gov't  │────▶│     AutoQA       │
│ (any framework) │     │ (audit + policy) │     │ (test generation)│
└─────────────────┘     └──────────────────┘     └──────────────────┘
```

Your agent framework handles reasoning. AISquare handles the "wait, should you actually do that?" part — recording decisions, enforcing policies, and routing to human review. AutoQA validates behavior through generated tests.

## LLM-friendly docs

This repo ships [`llms.txt`](llms.txt) and [`llms-full.txt`](llms-full.txt) — structured text files designed for AI-native developer tools. Paste the raw URL into Cursor's `@Docs`, feed it to Claude or ChatGPT for project context, or use it with any tool that consumes plain-text documentation. Let your AI learn about the AI governance tool. It's not as meta as it sounds.

## Contributing

We welcome contributions across the entire ecosystem. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Issues tagged **"good first issue"** across all repos in the [AISquare-Studio org](https://github.com/AISquare-Studio) are a great entry point. No contribution is too small — typo fixes have mass-merged their way into many a changelog.

## Community and support

- [Feedback board](https://feedback.aisquare.studio) — Feature requests, bug reports, and the occasional "have you considered..."
- [Documentation](https://docs.aisquare.studio) — Guides, API reference, and tutorials
- [Security](SECURITY.md) — Responsible disclosure policy
- Email: [bots@aisquare.com](mailto:bots@aisquare.com)

## License

[Apache-2.0](LICENSE) — use it, fork it, govern your agents with it.
