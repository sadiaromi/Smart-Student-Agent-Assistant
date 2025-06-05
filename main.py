import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load  API key from .env file
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("Error: GOOGLE_API_KEY not found in .env file")
    exit(1)

# Configure Gemini API key
genai.configure(api_key=api_key)

# Setup the Gemini model
model = genai.GenerativeModel("models/gemini-2.0-flash-lite")

def ask_assistant(user_input):
    prompt = """
You are a Smart Student Assistant.
You help students by doing the following:
1. Answer academic questions
2. Give effective study tips
3. Summarize short text passages

Keep the answers clear and student-friendly.
"""
    full_input = prompt + "\nUser: " + user_input
    response = model.generate_content(full_input)
    return response.text.strip()

if __name__ == "__main__":
    while True:
        user_input = input("👩🎓 You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        reply = ask_assistant(user_input)
        print("🤖 Assistant:", reply)
