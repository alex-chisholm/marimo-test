import streamlit as st
import requests

# Configuration for Marimo app
MARIMO_INTERNAL_URL = "http://127.0.0.1:8000"  # Marimo's local URL
MARIMO_IFRAME_URL = "http://01935556-5c7e-381a-2829-d30da942a8d0.share.connect.posit.cloud/marimo"  # External proxy URL (if configured)

# Function to check if Marimo is reachable
def is_marimo_running():
    try:
        response = requests.get(MARIMO_INTERNAL_URL, timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

# Streamlit app UI
st.title("Streamlit + Marimo Integration")
st.write("This Streamlit app embeds the Marimo notebook as an interactive iframe.")

# Check if Marimo is running
if is_marimo_running():
    st.markdown(
        f'<iframe src="{MARIMO_IFRAME_URL}" width="100%" height="800"></iframe>',
        unsafe_allow_html=True,
    )
else:
    st.error(
        "Marimo app is not accessible. Ensure it is running and properly configured. "
        "If you're hosting this on Posit Cloud, make sure Marimo is proxied to the correct URL."
    )
