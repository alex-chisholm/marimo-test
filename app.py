import subprocess
import streamlit as st

# Title for the Streamlit App
st.title("Marimo Launcher")

# Functionality to Start/Stop Marimo Process
if "marimo_process" not in st.session_state:
    st.session_state.marimo_process = None

# Run Marimo Button
if st.button("Run Marimo Notebook"):
    if st.session_state.marimo_process is None or st.session_state.marimo_process.poll() is not None:
        # Start the Marimo app
        st.session_state.marimo_process = subprocess.Popen(["marimo", "run", "intro.py"])
        st.success("Marimo app is running!")
    else:
        st.warning("Marimo is already running.")

# Stop Marimo Button
if st.button("Stop Marimo Notebook"):
    if st.session_state.marimo_process and st.session_state.marimo_process.poll() is None:
        st.session_state.marimo_process.terminate()
        st.session_state.marimo_process = None
        st.success("Marimo app has been stopped.")
    else:
        st.warning("Marimo is not running.")

# Embed the Marimo app using an iframe
st.markdown(
    '<iframe src="http://localhost:8000" width="100%" height="800"></iframe>',
    unsafe_allow_html=True,
)

# Note about setup
st.write("Ensure that `marimo` is installed, `intro.py` is in the working directory, and port 8000 is available.")
