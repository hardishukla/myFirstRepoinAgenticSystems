import json
api = """
{
  "id": "req_123",
  "status": "success",
  "result": {
    "text": "Hello world",
    "confidence": 0.98
  }
}
"""
data = json.loads(api)
request_id = data.get("id")
status = data.get("status")
result_data = data.get("result", {})

text_result = result_data.get("text")
score = result_data.get("confidence")

print("Request ID:", request_id)
print("Status:", status)
print("Text Result:", text_result)
print("Confidence Score:", score)

if score < 0.9:
    print("Confidence score is below 0.9")

follow_up_result = {
    "original_request_id": request_id,
    "processed_text": text_result.upper() if text_result else None,
    "status": "processed",
    "confidence_checked": score
}
follow_up_json = json.dumps(follow_up_result, indent=4)

with open("response.json", "w") as file:
    file.write(follow_up_json)
