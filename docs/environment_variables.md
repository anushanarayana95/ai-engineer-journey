# Environment Variables Cheat Sheet

## Install

pip install python-dotenv

## Import

from dotenv import load_dotenv
import os

## Load Variables

load_dotenv()

## Read Variable

api_key = os.getenv("GEMINI_API_KEY")

## Example .env

GEMINI_API_KEY=your_key_here

## Never Commit

.env

Add to .gitignore

.env
