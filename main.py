import os
import sys
import time
from dotenv import load_dotenv
from google import genai 

if len(sys.argv) < 2:
  print("pwease provide a pwompt uwu")
  time.sleep(2)
  sys.exit(1)
 
prompt = sys.argv[1]

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model = 'gemini-2.0-flash-001',
    contents = prompt
)

print(response.text,"\n","Prompt tokens:",response.usage_metadata.prompt_token_count,"\n","Response tokens:",response.usage_metadata.candidates_token_count)

