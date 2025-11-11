import boto3
import json

prompt_data = """
write a poem o machine learning
"""

bedrock = boto3.client(service_name = "bedrock-runtime", region_name = "us-west-2")

payload = {
    "prompt" : prompt_data,
    "maxTokens" : 100,
    "temperature": 0.8,
    "topP" : 0.8
}


body = json.dumps(payload)

model_id = "anthropic.claude-3-sonnet-20240229-v1:0"

response = bedrock.invoke_model(
            body = body,
            modelId= model_id,
            accept = "application/json",
            contentType = "application/json"

)

response_body = json.loads(response.get("body").read())
response_text = response_body.get("completions")[0].get("data").get("text")

print(response_text)