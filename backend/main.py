import sys
import asyncio
import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# --- Windows async fix for Playwright subprocesses ---
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

# --- Import agents and utils ---
from backend.agents.planner_agent import get_structured_test_cases
from backend.agents.orchestrator_agent import orchestrate_tests
from backend.agents.analyzer_agent import analyze_results
from backend.utils.save_report import save_report

# --- Ensure reports directory exists ---
os.makedirs("reports", exist_ok=True)

# --- FastAPI app ---
app = FastAPI(title="Multi-Agent Game Tester")

# --- API Endpoints ---
@app.get("/plan")
async def plan():
    """Return structured test plan."""
    return get_structured_test_cases()

@app.get("/execute")
async def execute():
    """Run top test cases asynchronously and return report."""
    plan = get_structured_test_cases()
    test_cases = plan["test_cases"]

    # Execute tests asynchronously
    results = orchestrate_tests(test_cases)


    # Analyze results
    analyzed = analyze_results(results)

    # Save final report
    report_path = save_report(analyzed)

    return {"report": report_path, "results": analyzed}

# --- Serve frontend and reports ---
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
app.mount("/reports", StaticFiles(directory="reports"), name="reports")
