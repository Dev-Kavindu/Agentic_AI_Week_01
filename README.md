# Agentic AI - Week 01

A practical OpenAI Agents SDK workshop covering agent basics, tools, memory, tracing,
parallel orchestration, sales email workflows, structured outputs, guardrails, web
search, image generation, and a multi-agent creative agency workflow.

## Repository Contents

| File | Purpose |
| --- | --- |
| `task-01.ipynb` | Introduces agents, tools, memory, tracing, streaming, and custom function tools. |
| `task-02.ipynb` | Demonstrates automated sales outreach, email sending, parallel drafting, agent selection, and orchestration. |
| `task-03.ipynb` | Demonstrates Pydantic structured output, email review, output guardrails, and professional prompt constraints. |
| `creative_agency.ipynb` | Runs a complete multi-agent workflow that plans, searches, writes scripts, creates posters, and emails the result. |
| `web_search_tool.py` | Provides a reusable free DuckDuckGo web-search tool for Python and OpenAI Agents SDK workflows. |
| `main.py` | Simple entry-point script for the project. |
| `pyproject.toml` | Python project metadata and dependencies. |
| `.env.example` | Template for API keys and SMTP settings. |

## What the Notebooks Demonstrate

### Task 1: Agent Fundamentals

`task-01.ipynb` builds the foundation for agent-based applications:

- Creates and runs a basic OpenAI-compatible agent.
- Streams agent responses as they are generated.
- Converts Python functions into agent tools with `@function_tool`.
- Uses `SQLiteSession` to retain conversation memory.
- Enables tracing for inspecting agent, tool, and model activity.
- Explores sequential and loop-style interaction patterns.
- Demonstrates tool and JSON-based agent workflows.

### Task 2: Sales Outreach and Agent Orchestration

`task-02.ipynb` demonstrates a practical email automation workflow:

- Sends plain-text and HTML email through an SMTP server.
- Wraps email sending as an agent-callable function tool.
- Generates multiple cold-email variants with separate agent roles.
- Runs agents in parallel to create and compare responses.
- Uses a picker agent to select the strongest email.
- Uses a sender agent to deliver the selected email.
- Compares code-based and LLM-driven orchestration.
- Shows how specialized agents can be exposed as tools to a coordinator.

### Task 3: Structured Output and Guardrails

`task-03.ipynb` adds reliability and validation:

- Uses Pydantic models to define predictable structured responses.
- Validates email review results such as professionalism and personalization placeholders.
- Adds output guardrails to inspect agent responses.
- Supports controlled stopping or continuation when an output fails a rule.
- Demonstrates the difference between plain text and typed agent output.

### Creative Agency Project

`creative_agency.ipynb` implements a multi-agent marketing pipeline:

- A planning agent turns a campaign request into a focused plan.
- A web-search agent gathers current information and supporting references.
- A script-writing agent creates poster concepts and production instructions.
- An image-generation agent creates promotional poster images.
- An email agent prepares HTML and plain-text campaign summaries.
- The poster files are attached and sent through Gmail-compatible SMTP.
- The workflow uses code orchestration and agent-as-tool orchestration.
- Each run creates a timestamped folder under `creative_agency_posters/`.
- OpenAI tracing records the run and its agent/tool activity.

## Core Agent Workflow

```text
User Request
     |
     v
Planner Agent --> Creative Strategy and Poster Plan
     |
     v
Web Search Agent --> Current Campaign Facts and References
     |
     v
Script Writer Agent --> Poster Copy and Visual Prompts
     |
     v
Image Generation Agent --> Poster Images
     |
     v
Email Agent --> Campaign Summary and Attachments
```

## Setup

### 1. Create a virtual environment

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

This project requires Python 3.14 or later, as defined in `pyproject.toml`.

### 2. Install dependencies

Using `uv`:

```powershell
uv sync
```

Alternatively, use `pip`:

```powershell
pip install -r requirements.txt
```

### 3. Configure environment variables

Copy `.env.example` to `.env`, then add only your own values:

```powershell
Copy-Item .env.example .env
```

Configure the required providers and services:

- `GEMINI_API_KEY` or `GROQ_API_KEY` for supported OpenAI-compatible providers.
- `OPENAI_API_KEY` for OpenAI services.
- `EMAIL_ADDRESS` for the sender address.
- `EMAIL_SMTP_SERVER` for the SMTP server, typically `smtp.gmail.com`.
- `EMAIL_APP_PASSWORD` for a Gmail app password or the provider-specific credential.

Never commit `.env`, API keys, app passwords, session databases, or real account details.

## Run the Project

Launch Jupyter Notebook:

```powershell
jupyter notebook
```

Open the notebooks in this order:

1. `task-01.ipynb`
2. `task-02.ipynb`
3. `task-03.ipynb`
4. `creative_agency.ipynb`

Run notebook cells from top to bottom. API calls and email sending require valid
credentials and may incur provider charges.

## Environment and Generated Files

The `.gitignore` excludes local runtime and generated content, including:

- Virtual environments and Python caches.
- `.env` secrets and private credentials.
- Jupyter checkpoints.
- SQLite session databases.
- Generated poster and image folders.
- IDE configuration and operating-system metadata.
- Logs, coverage reports, and temporary files.

The source notebooks and reusable Python modules remain trackable.

## Notes

- The web-search helper uses DuckDuckGo and has no fixed search result count by default.
- Email behavior depends on the configured SMTP provider and account security settings.
- Generated poster dimensions and quality depend on the image model and prompt used.
- Trace and session data may contain user prompts or outputs; keep it local and review it before sharing.