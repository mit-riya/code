import requests
import json
            
url="https://codeforces.com/api/problemset.problems?tags=implementation"

response_API=requests.get(url)
data=response_API.json()
problems=data.get('result')['problems']

with open("./data/problems.jsonl", 'w') as file:
    for problem in problems:
        doc_object = {"doc": str(problem)}
        file.write(json.dumps(doc_object) + '\n')