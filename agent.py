from dotenv import load_dotenv
import os
from groq import Groq
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from search import multi_search, format_results
from report import save_report

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_groq(prompt, system_prompt="You are a helpful research assistant."):
    """Send a message to Groq and get a response."""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def generate_queries(topic):
    """Ask Groq to generate multiple search queries for a topic."""
    prompt = f"""Generate 3 different search queries for researching: '{topic}'
    Return only the queries, one per line, nothing else."""
    response = ask_groq(prompt)
    queries = [q.strip() for q in response.strip().split('\n') if q.strip()]
    return queries[:3]

def analyze_results(topic, search_results):
    """Ask Groq to analyze and summarize the search results."""
    system = """You are an expert research assistant. Analyze the provided 
    search results and give a comprehensive, well-structured answer."""
    
    prompt = f"""Topic: {topic}

Search Results:
{search_results}

Please provide:
1. SUMMARY: A clear answer to the research topic
2. KEY FINDINGS: 3-5 bullet points of the most important facts
3. CONTRADICTIONS: Any conflicting information found between sources
4. CONFIDENCE SCORE: Rate 1-10 how confident you are based on source agreement
5. SOURCES USED: List the most relevant URLs"""

    return ask_groq(prompt, system)

def main():
    from rich.console import Console
    from rich.panel import Panel
    console = Console()

    console.print(Panel("🔍 AI Research Agent", style="bold cyan"))
    
    topic = input("\nWhat would you like to research? → ").strip()
    
    if not topic:
        print("Please enter a topic!")
        return

    console.print("\n[cyan]Generating search queries...[/cyan]")
    queries = generate_queries(topic)
    
    console.print("\n[cyan]Searching the web...[/cyan]")
    results = multi_search(queries)
    
    console.print(f"\n[green]Found {len(results)} sources! Analyzing...[/green]\n")
    formatted = format_results(results)
    
    analysis = analyze_results(topic, formatted)
    
    console.print(Panel(analysis, title="Research Results", style="green"))

    saved = save_report(topic, analysis, queries, len(results))
    console.print(f"\n[yellow]📄 Report saved to: {saved}[/yellow]")

if __name__ == "__main__":
    main()