import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/api/diagnose"

st.title("PySage AI")
st.subheader("Intelligent Python/ML Troubleshooting Assistant")

uploaded_file = st.file_uploader(
    "Upload Python error log",
    type=["txt", "log"]
)

if uploaded_file:
    files = {
        "file": (
            uploaded_file.name,
            uploaded_file.getvalue()
        )
    }

    with st.spinner("Analyzing traceback..."):
        response = requests.post(API_URL, files=files)

    if response.status_code == 200:
        result = response.json()

        st.success("Diagnosis complete")

        st.write("### Error Type")
        st.write(result["error_type"])

        st.write("### Root Cause")
        st.write(result["probable_root_cause"])

        st.write("### Suggested Fixes")
        for fix in result["suggested_fixes"]:
            st.write(f"- {fix}")

        st.write("### Confidence")
        st.write(result["confidence"])
    else:
        st.error("Analysis failed")