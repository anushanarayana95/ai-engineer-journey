# Architecture Principles

## Separation of Concerns (SoC)

Each layer of an application should have a single responsibility.

### Presentation Layer
- Streamlit
- Displays data
- Accepts user input

### Business Layer
- FastAPI
- Processes requests
- Applies business rules
- Communicates with the database

### Data Layer
- SQLite
- Stores and retrieves data

### Benefits

- Easier maintenance
- Better scalability
- Reusable APIs
- Cleaner code

## Why use FastAPI between UI and Database?

- Keeps API keys secure.
- Separates UI from business logic.
- Centralizes validation.
- Allows multiple clients (web, mobile, desktop) to reuse the same API.
- Makes it easy to replace the database without changing the frontend.
- Keeps the database hidden from clients.