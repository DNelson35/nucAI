import os
import sys
import time
import argparse
from dotenv import load_dotenv
from google import genai 
from google.genai import types

if len(sys.argv) < 2:
  print("pwease provide a pwompt uwu")
  time.sleep(2)
  sys.exit(1)
 
parser = argparse.ArgumentParser(
  prog="nucAI",
  description="Buddy Nuc the AI helper"
)

parser.add_argument(
  "prompt", 
  type=str, 
  help="the message to send nucAI wrapped in quotes"
)

parser.add_argument(
  "-v", "--verbose",
  action="store_true",
  help="enables verbose mode"
)

args = parser.parse_args()

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

messages = [
  types.Content(role="user", parts=[types.Part(text=args.prompt)])
]
response = client.models.generate_content(
    model = 'gemini-2.0-flash-001',
    contents = messages
)

if args.verbose:
  print(f"User prompt: {args.prompt}")
  print(f"{parser.prog}: {response.text}")
  print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
  print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
else:
  print(response.text)

