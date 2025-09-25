import google.generativeai as genai
import os
import re

# Configure Gemini using os.environ.get
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

def get_raw_test_cases():
    try:
        if not os.environ.get("GEMINI_API_KEY"):
            raise ValueError("No GEMINI_API_KEY set")

        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt_text = """
        Generate 20 test cases for a number/math puzzle game.
        Include target number and available numbers.
        Return them line by line.
        """
        response = model.generate_content(prompt_text)
        return response.text.split("\n")
    except Exception as e:
        print(f"Gemini API failed: {e}")
        # Fallback: hardcoded test cases
        return [
            "Target: 10 Numbers: 1,2,3,4",
            "Target: 15 Numbers: 3,5,7",
            "Target: 8 Numbers: 2,2,4"
        ]

def parse_gemini_output(raw_cases):
    """
    Convert raw Gemini strings into structured test case dictionaries.
    """
    parsed_cases = []

    for line in raw_cases:
        if not line.strip() or line.startswith("**"):
            continue

        target_match = re.search(r"Target[:\s]*([\d]+)", line)
        numbers_match = re.search(r"Numbers[:\s]*([\d,\s]+)", line)

        if target_match and numbers_match:
            target_number = int(target_match.group(1))
            available_numbers = [int(x.strip()) for x in numbers_match.group(1).split(",") if x.strip()]

            expected_operations = ["+", "-", "*", "/"]

            parsed_cases.append({
                "target_number": target_number,
                "available_numbers": available_numbers,
                "expected_operations": expected_operations,
                "steps": ["Go to URL"]  # 👈 Added so executor has steps
            })

    return {
        "total_tests": len(parsed_cases),
        "test_cases": parsed_cases
    }

def get_structured_test_cases():
    raw_cases = get_raw_test_cases()
    return parse_gemini_output(raw_cases)