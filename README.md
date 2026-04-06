# Market Research Crew

A multi-agent AI system powered by [CrewAI](https://crewai.com) that conducts comprehensive market research and generates a business analysis report.

## Agents

| Agent | Role |
|-------|------|
| Market Research Specialist | Market sizing, growth trends, industry analysis |
| Competitive Intelligence Analyst | Competitor analysis, strengths/weaknesses, market gaps |
| Customer Insights Researcher | Customer segments, pain points, willingness to pay |
| Product Strategy Advisor | MVP features, differentiation, development roadmap |
| Business Analyst | Pricing strategy, revenue model, risk analysis, go/no-go recommendation |

**Process:** Sequential (each agent builds on previous agents' findings)

**Tools:** SerperDevTool (web search), ScrapeWebsiteTool (web scraping)

## Prerequisites

- Python >= 3.10, < 3.14
- [uv](https://docs.astral.sh/uv/) package manager
- OpenAI API key
- Serper API key (for web search)

## Setup

### 1. Install uv

```bash
pip install uv
```

### 2. Clone the repo

```bash
git clone https://github.com/omkarkhoche3448/market-research-crew.git
cd market-research-crew
```

### 3. Install dependencies

```bash
crewai install
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL_NAME=gpt-4o-mini
SERPER_API_KEY=your_serper_api_key_here
```

Get your API keys from:
- OpenAI: [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
- Serper: [serper.dev](https://serper.dev) (2,500 free searches)

## Running the Crew

```bash
crewai run
```

**Note (Windows):** If you see emoji encoding errors, run with:

```bash
PYTHONIOENCODING=utf-8 PYTHONUTF8=1 crewai run
```

The crew will generate a report at `reports/report.md`.

## Customizing the Product Idea

Edit `src/market_research_crew/main.py` and change the `product_idea` value:

```python
inputs = {
    "product_idea": "Your product idea here"
}
```

## Customizing Agents & Tasks

- `src/market_research_crew/config/agents.yaml` — Agent roles, goals, backstories
- `src/market_research_crew/config/tasks.yaml` — Task descriptions and expected outputs
- `src/market_research_crew/crew.py` — Agent/task logic and tools

## Deploy to CrewAI Platform

```bash
crewai login
crewai deploy create
crewai deploy push
crewai deploy status
```

## Project Structure

```
market_research_crew/
├── .env                          # API keys (not committed)
├── pyproject.toml                # Project config
├── reports/                      # Generated report output
│   └── report.md
└── src/market_research_crew/
    ├── config/
    │   ├── agents.yaml           # Agent definitions
    │   └── tasks.yaml            # Task definitions
    ├── crew.py                   # Crew orchestration
    ├── main.py                   # Entry point
    └── tools/
        └── custom_tool.py        # Custom tools
```
