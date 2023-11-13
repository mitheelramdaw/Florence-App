import streamlit as st

# Create sliders with emojis
feeling = st.slider("How are you feeling this morning?", 0, 100, 50)
st.write(f"😢 {feeling} 😄")

sleep = st.slider("How was your sleep?", 0, 100, 50)
st.write(f"😴 {sleep} 😃")

ready = st.slider("How ready are you for today?", 0, 100, 50)
st.write(f"😓 {ready} 😁")

# Text area for daily tasks
tasks = st.text_area("What do you need to do today?", "")

# Text area for side notes
side_notes = st.text_area("Side notes", "")

# Save state to URL
st.experimental_set_query_params(feeling=feeling, sleep=sleep, ready=ready, tasks=tasks, side_notes=side_notes)
