import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

print("Gemini Key Loaded:", os.getenv("GEMINI_API_KEY") is not None)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

try:
    model = genai.GenerativeModel("gemini-1.5-flash")  #  less restricted

    response = model.generate_content("Summarize the importance of AI in healthcare.")
    print("\n Gemini Response:\n", response.text)
except Exception as e:
    print("\n Error:", e)
