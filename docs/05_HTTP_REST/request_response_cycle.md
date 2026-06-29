# HTTP Request Response Cycle

Client

↓

HTTP Request

↓

Uvicorn

↓

FastAPI

↓

Business Logic

↓

Database

↓

JSON Response

↓

Client

## What happens if Uvicorn is stopped?

Streamlit

↓

requests.get()

↓

HTTP Request

↓

127.0.0.1

↓

Port 8000

↓

No server is listening

↓

Operating System returns "Connection Refused"

↓

requests retries

↓

ConnectionError is raised