
# 📄 AI Utility Tool using Gemini LLM: Text /Article Summarizer​

A powerful and lightweight **text and PDF summarization tool** powered by **Gemini 1.5 Flash**. This Streamlit-based web app allows users to generate concise summaries from raw text or uploaded academic documents. It also includes controls for summary length and the ability to download the summary.

---

## 🎯 Project Objectives

- Summarize long-form content using Gemini LLM.
- Enable PDF upload and summarization.
- Provide length control for summaries (Short / Medium / Detailed).
- Easy deployment and usability through Streamlit.

---

## ⚙️ Methodology

This application uses **Google's Gemini 1.5 Flash model** via the `google-generativeai` Python client. The text input or uploaded PDF is processed and passed to the model through an engineered prompt. Output is then displayed in a clean UI with optional download functionality.

---

## 🚀 Key Features

- 🧠 **Powered by Gemini 1.5 Flash (Google AI)**
- 📄 **Supports PDF Uploads**
- 📏 **Control Summary Length**: Short / Medium / Detailed
- 💾 **Save Summary**: Download output as `.txt`
- 🖥️ **Streamlit-based UI** for intuitive interaction
- ✅ **API Key Management** using environment variables

---

## 📁 Directory Structure

```

gemini\_sum/
├── app.py                # Main Streamlit app
├── summarizer.py         # Gemini API logic
├── test\_gemini.py        # Standalone API test script
├── requirements.txt      # Dependencies
└── .gitignore

````

---

## 🧰 Dependencies

Install these using `pip install -r requirements.txt`:

- `streamlit`
- `google-generativeai`
- `PyPDF2`
- `python-dotenv` *(if used for local API key loading)*

---

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sreelekshmisaju/gemini-summarizer.git
cd gemini-summarizer
````

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/Scripts/activate
venv\Scripts\activate   # On Windows
# source venv/bin/activate  # On Linux/Mac
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Your Gemini API Key

#### Option 1: Direct in Python

```python
import google.generativeai as genai
genai.configure(api_key="YOUR_API_KEY")
```

#### Option 2: Using Environment Variable

```bash
# Set this in your terminal or OS
export GEMINI_API_KEY="your_key_here"   # Linux/macOS
set GEMINI_API_KEY=your_key_here        # Windows CMD
```

---

## ▶️ Running the App

```bash
python -m streamlit run app.py

streamlit run app.py
```

Then open the provided local URL in your browser (e.g. `http://localhost:8501`).

---

## 📦 Deployment (Streamlit Cloud)

1. Push your code to GitHub.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud).
3. Connect your GitHub repo and deploy.
4. Ensure your **`GEMINI_API_KEY` is set in the app’s secrets**.

Go to **Manage App → Settings → Secrets**:

```toml
GEMINI_API_KEY = "your_actual_key"
```

---

## 🧪 Example Usage

## 🎥 Demo Video

▶️ [Click here to watch the demo](https://drive.google.com/file/d/1pdgQ4s5OJTD908jzAaBAdskv_l1jT-c4/view?usp=sharing)


## 🧩 Troubleshooting

| Issue                         | Solution                                                                |
| ----------------------------- | ----------------------------------------------------------------------- |
| `ModuleNotFoundError: PyPDF2` | Ensure `PyPDF2` is added in `requirements.txt`.                         |
| `API key expired`             | Regenerate key at [Google AI Studio](https://makersuite.google.com/app) |
| `404 model not found`         | Ensure you're using `gemini-1.5-flash`                                  |
| `429 quota exceeded`          | You’ve hit your free tier quota — try again later or upgrade your plan. |

---




