import streamlit as st
from summarizer import summarize_text
import PyPDF2
import tempfile

st.set_page_config(page_title="Gemini PDF Summarizer", page_icon="📄")

st.title("📄 Gemini PDF + Text Summarizer")
st.markdown("Upload a PDF or enter text manually. Choose summary length, then download it!")

# --- Option: PDF Upload or Text Input ---
option = st.radio("Choose input method:", ["Upload PDF", "Enter Text"])

input_text = ""

if option == "Upload PDF":
    uploaded_file = st.file_uploader("Upload PDF file", type=["pdf"])
    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(uploaded_file.read())
            pdf_reader = PyPDF2.PdfReader(tmp_file.name)
            input_text = "\n".join([page.extract_text() for page in pdf_reader.pages])
        st.success("PDF text extracted!")
else:
    input_text = st.text_area("✏ Paste your text here:", height=250)

# --- Summary Length Option ---
length_choice = st.radio("Select summary length:", ["Short", "Medium", "Detailed"])

# --- Summarize Button ---
if st.button("Summarize"):
    if input_text.strip():
        st.info("⏳ Generating summary...")
        length_prompt = {
            "Short": "Summarize briefly.",
            "Medium": "Summarize clearly in a few lines.",
            "Detailed": "Summarize in detailed paragraphs."
        }

        full_prompt = f"{length_prompt[length_choice]}\n\nText:\n{input_text}"
        summary = summarize_text(full_prompt)

        st.subheader(" Summary:")
        st.success(summary)

        # --- Download Option ---
        st.download_button(
            label=" Download Summary as .txt",
            data=summary,
            file_name="summary.txt",
            mime="text/plain"
        )
    else:
        st.warning("Please upload a PDF or enter some text.")


