# config.py
from crewai import LLM
import streamlit as st
from dotenv import load_dotenv
import os
import agentops


def initialize_app():
    load_dotenv()

    # Set Gemini configuration
    gemini_key = os.getenv("GEMINI_API_KEY")
    model_name = os.getenv("MODEL_NAME")
    credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    provider = os.getenv("LITELLM_PROVIDER")

    if not gemini_key:
        raise ValueError("Missing GEMINI_API_KEY in .env file")
    
    if not credentials_path:
        raise ValueError("Missing GOOGLE_APPLICATION_CREDENTIALS in .env file. Please set the path to your Google Cloud credentials JSON file.")

    # Set necessary environment variables
    os.environ["GEMINI_API_KEY"] = gemini_key
    os.environ["MODEL_NAME"] = model_name
    os.environ["LITELLM_PROVIDER"] = "gemini"
    os.environ["LITELLM_API_KEY"] = gemini_key

    os.environ["GOOGLE_API_KEY"] = gemini_key
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
    
    # Set Langchain specific environment variables
    os.environ["LANGCHAIN_API_KEY"] = gemini_key
    os.environ["LANGCHAIN_PROVIDER"] = "google"

    # Remove any conflicting environment variables
    os.environ.pop("OPENAI_API_KEY", None)
    os.environ.pop("LITELLM_OPENAI_API_KEY", None)
    os.environ.pop("LITELLM_API_KEY", None)
    os.environ.pop("LITELLM_PROVIDER", None)
    os.environ.pop("CREWAI_API_KEY", None)
    os.environ.pop("CREWAI_PROVIDER", None)

    print(f"✅ Using Gemini model: {model_name}")
#   print(f"✅ Using Google Cloud credentials from: {credentials_path}")
