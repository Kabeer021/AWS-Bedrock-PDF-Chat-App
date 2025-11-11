import boto3
import json

prompt_data = """
write a poem on Machine learning
"""

bedrock = boto3.client(service_name = "bedrock-runtime", region_name = "us-west-2")


payload = {
            "prompt" : prompt_data,
            "max_gen_len":100,
            "temperature":0.5, #Controls creativity / randomness in generation.

            "top_p": 0.9 #The model considers only the smallest set of words whose cumulative probability is ≥ p.
}

body = json.dumps(payload)

model_id = "meta.llama3-70b-instruct-v1:0"

response = bedrock.invoke_model(
            body = body,
            modelId= model_id,
            accept = "application/json",
            contentType = "application/json"

)
response_body = json.loads(response.get("body").read())

response_text = response_body["generation"]

print(response_text)