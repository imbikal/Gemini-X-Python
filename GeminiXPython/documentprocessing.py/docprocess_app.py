import streamlit as st
import httpx
from google import genai
from google.genai import types

# --- App Setup ---
st.set_page_config(page_title="Gemini PDF Summarizer", page_icon="📄")
st.title("📄 AI Document Summarizer")

# Initialize Gemini Client (Ensure your API Key is set in your environment)
# Or use: client = genai.Client(api_key="YOUR_API_KEY")
client = genai.Client()

# --- Sidebar Configuration ---
with st.sidebar:
    # st.header("Settings")
    # model_choice = st.selectbox("Model", ["gemini-2.0-flash"])
    word_limit = st.slider("Word Limit", 50, 500, 300)

# --- UI Layout ---
tab1, tab2 = st.tabs(["Upload PDF", "PDF URL"])

doc_data = None

with tab1:
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file:
        doc_data = uploaded_file.read()

with tab2:
    url = st.text_input("Paste PDF URL")
    if url:
        try:
            with st.spinner("Downloading PDF..."):
                response = httpx.get(url)
                response.raise_for_status()
                doc_data = response.content
        except Exception as e:
            st.error(f"Failed to fetch PDF: {e}")

# --- Processing ---
if doc_data:
    if st.button("Summarize Document"):
        try:
            with st.spinner("Gemini is reading..."):
                # Prepare the PDF part
                pdf_part = types.Part.from_bytes(
                    data=doc_data,
                    mime_type="application/pdf"
                )

                # Generate Content
                response = client.models.generate_content(
                    # model=model_choice,
                    contents=[pdf_part, "Summarize the document"],
                    config=types.GenerateContentConfig(
                        system_instruction=f"Answer within {word_limit} words"
                    )
                )

                st.markdown("### Summary")
                st.write(response.text)
                
        except Exception as e:
            st.error(f"An error occurred: {e}")
else:
    st.info("Please upload a file or provide a URL to begin.")