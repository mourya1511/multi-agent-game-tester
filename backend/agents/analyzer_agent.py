def analyze_results(results):
    analyzed = []
    for res in results:
        if res is None:
            continue
        res["reproducible"] = True
        analyzed.append(res)
    return analyzed
