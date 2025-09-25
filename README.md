Multi-Agent Game Tester POC

Overview:

This is a proof of concept for a multi-agent web game tester focused on number and math puzzle games. The target game is EzyGamers Puzzle.
The system uses multiple AI agents to create test plans, run key test cases, gather artifacts, check results, and produce a detailed report.

Features:

PlannerAgent:
Generates over 20 candidate test cases using LangChain.
Creates structured test plans for execution.

RankerAgent:
Ranks candidate test cases.
Chooses the top 10 tests for execution.
ExecutorAgents and OrchestratorAgent
Runs selected test cases at the same time.
Gathers artifacts: screenshots, DOM snapshots, console logs.

AnalyzerAgent:
Checks results with repeat and cross-agent verification.
Ensures test outcomes can be replicated.

Reporting:
Produces a JSON report that includes:
Test verdicts (Pass/Fail)
Gathered artifacts

Installation:

# Clone repository
git clone https://github.com/mourya1511/multi-agent-game-tester.git
cd multi-agent-game-tester

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
playwright install

Running the POC

Start FastAPI server
uvicorn backend.main:app --reload
Generate Test Plan
Open in browser: http://127.0.0.1:8000/plan

This shows a structured plan with over 20 candidate tests.

Execute Top Tests
Open in browser: http://127.0.0.1:8000/execute
This runs the top 10 tests at the same time.

It gathers artifacts (screenshots) and creates a report.

View Reports

Reports are saved in the reports/ directory.

Sample JSON report:

{
  "report": "reports/final_report.json",
  "results": [
    {
      "test_id": 1,
      "verdict": "Pass",
      "artifacts": ["reports/test_1.png"],
      "reproducible": true
    },
    {
      "test_id": 2,
      "verdict": "Pass",
      "artifacts": ["reports/test_2.png"],
      "reproducible": true
    }
  ]
}

Project Structure:

multi-agent-game-tester/
├── backend/            # Backend agents and FastAPI app
├── frontend/           # Minimal frontend UI
├── reports/            # Generated test reports and screenshots
├── venv/               # Virtual environment
├── requirements.txt
├── README.md

Demo Video:

Demonstrates plan generation, execution of the top 3 tests (to see all 10, run the full test), and opening a sample report with artifacts.
Save video in repo: demo/Multi-Agent_Game_Tester_Demo.mp4

Notes:

The FastAPI backend is fully asynchronous and works on Windows and Linux.
Playwright is used for browser automation and gathering artifacts.
Make sure to activate the virtual environment before running the server.
