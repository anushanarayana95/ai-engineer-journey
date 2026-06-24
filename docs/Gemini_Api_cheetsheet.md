# Gemini API Cheat Sheet

## Installation

pip install google-genai

## Imports

from google import genai
from dotenv import load_dotenv
import os

## Load Environment Variables

load_dotenv()

## Create Client

client = genai.Client(
api_key=os.getenv("GEMINI_API_KEY")
)

## Generate Content

response = client.models.generate_content(
model="gemini-2.5-flash",
contents="Explain FastAPI"
)

print(response.text)

## Environment Variable

.env

GEMINI_API_KEY=your_api_key

## Common Errors

### No API key provided

Cause:

* .env missing
* Wrong variable name
* load_dotenv() missing

### 429 RESOURCE_EXHAUSTED

Cause:

* Daily quota exceeded

### 503 UNAVAILABLE

Cause:

* High model demand

Solution:

* Retry later
