import boto3
import json
import base64
import os

# --- Your prompt ---
prompt_data = "Provide me a 4K image of a beach"

prompt_template = [{"text": prompt_data, "weight": 1}]

# --- Initialize Bedrock runtime client ---
bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")

# --- Payload for the Stability AI model ---
payload = {
    "text_prompts": prompt_template,
    "cfg_scale": 10,
    "seed": 0,
    "steps": 50,
    "width": 512,
    "height": 512
}

body = json.dumps(payload)

# --- Model ID for Stable Diffusion ---
model_id = "stability.stable-diffusion-xl-v1"

# --- Invoke model ---
response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

# --- Parse and decode image ---
response_body = json.loads(response["body"].read())
artifact = response_body["artifacts"][0]
image_base64 = artifact["base64"]
image_bytes = base64.b64decode(image_base64)

# --- Save output ---
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)
file_path = os.path.join(output_dir, "generated_image.png")

with open(file_path, "wb") as f:
    f.write(image_bytes)

print(f"✅ Image generated and saved at: {file_path}")
