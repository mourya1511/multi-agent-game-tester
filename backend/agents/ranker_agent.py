def rank_test_cases(test_cases):
    # skip any string test cases
    dict_cases = [tc for tc in test_cases if isinstance(tc, dict)]
    ranked = sorted(dict_cases, key=lambda x: len(x.get("steps", [])), reverse=True)
    return ranked
