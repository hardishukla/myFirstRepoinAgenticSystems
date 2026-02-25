import json

# Step 1: Store JSON-formatted string (simulated API response)
api_response_json = """
{
  "id": "req_123",
  "status": "success",
  "result": {
    "text": "Hello world",
    "confidence": 0.98
  }
}
"""

# Step 2: Parse JSON string into Python dictionary
parsed_response = json.loads(api_response_json)

# Step 3: Extract required fields (without hardcoding values)
request_id = parsed_response.get("id")
status = parsed_response.get("status")
result_data = parsed_response.get("result", {})

text_result = result_data.get("text")
confidence_score = result_data.get("confidence")

# Step 4: Print extracted information
print("Request ID:", request_id)
print("Status:", status)
print("Text Result:", text_result)
print("Confidence Score:", confidence_score)

# Step 5: Check confidence threshold
if confidence_score is not None and confidence_score < 0.9:
    print("⚠️ Warning: Confidence score is below 0.9")

# Step 6: Create a new follow-up Python dictionary
follow_up_result = {
    "original_request_id": request_id,
    "processed_text": text_result.upper() if text_result else None,
    "status": "processed",
    "confidence_checked": confidence_score
}

# Step 7: Convert dictionary to JSON string
follow_up_json = json.dumps(follow_up_result, indent=4)