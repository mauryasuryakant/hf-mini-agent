import requests
import json

MODEL = "smollm2:360m"

task = input("Task: ")

prompt = f"""
Convert the user's task into JSON.

Task: {task}

Return ONLY valid JSON:
{{"a": number, "b": number, "operation": "add|subtract|multiply|divide"}}
"""

response = requests.post(
    # "http://localhost:11434/api/generate",
    "https://sturdy-xylophone-pjqg46g6rx7xh94j7-11434.app.github.dev/api/generate",
    json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }
)

action = json.loads(response.json()["response"])

a = action["a"]
b = action["b"]
op = action["operation"]

if op == "add":
    result = a + b
elif op == "subtract":
    result = a - b
elif op == "multiply":
    result = a * b
elif op == "divide":
    result = a / b

print("Result:", result)