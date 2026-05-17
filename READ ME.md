# 🔍 AI Research Agent

An AI-powered research agent built with Python that searches 
multiple web sources, detects contradictions, and generates 
confidence-scored research reports automatically.

## Features
- 🌐 Real-time multi-source web search
- ⚡ Contradiction detection between sources
- 📊 Confidence scoring based on source agreement
- 📄 Auto-saves research reports as markdown files

## Tech Stack
- Python
- Groq API (LLaMA 3.3 70B)
- Tavily Search API
- Rich library

## How to Run
1. Clone the repo
2. Create a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Add your API keys to `.env`
5. Run: `python agent.py`