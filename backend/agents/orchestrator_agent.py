# backend/agents/orchestrator_agent.py
from concurrent.futures import ThreadPoolExecutor, as_completed
from .executor_agent import execute_test_case_sync  # Use the sync executor
from backend.agents.ranker_agent import rank_test_cases

# Create a thread pool for parallel test execution
executor = ThreadPoolExecutor(max_workers=5)  # Adjust number of threads as needed

def run_test_sync(test_case, test_id):
    """
    Wrapper to run a single test case synchronously.
    """
    try:
        result = execute_test_case_sync(test_case, test_id)
    except Exception as e:
        result = {
            "test_id": test_id,
            "verdict": "Failed",
            "error": str(e),
            "artifacts": [],
        }
    return result

def orchestrate_tests(test_cases):
    """
    Execute all test cases using ThreadPoolExecutor synchronously.
    Returns a list of results.
    """
    results = []
    futures = {executor.submit(run_test_sync, test, idx + 1): idx for idx, test in enumerate(test_cases)}

    for future in as_completed(futures):
        result = future.result()
        results.append(result)

    # Optionally rank results or re-order based on test_id
    results.sort(key=lambda x: x["test_id"])
    return results
