# Step 1. Importing libraries
import streamlit as st
import google.generativeai as genai

# Step 2. API Key
key = 'AIzaSyDR20P2yn2hZHk2O8N-pQgqlNe3DW6kPlM'
genai.configure(api_key=key)
model = genai.GenerativeModel('gemini-2.5-flash-lite')

# Step 3. Main App
st.title('AI Studying Assistant')
st.text('Ask this smart assistant anything!')
col1, col2 = st.columns(2)

with col1:
    subjets = ['Math', 'Science', 'English', 'Arabic', 'ICT']
    subjet = st.selectbox('Choose Subject:', subjets)

    # Option 2
    tones = ['Mother to child', 'Friend to friend', 'Friendly', 'Pro']
    tone = st.selectbox('Choose a tone:', tones)

with col2:
    # Option 1
    details = ['Breif', 'Medium', 'Detailed']
    level = st.selectbox('Choose details level:', details)

    # Option  2 
    stages = ['Primary', 'Preparotory', 'Secondry']
    stage = st.selectbox('Choose your stage:', stages)

question = st.text_area('Enter your question')
if st.button('Get Answer'):
    prompt = f"""
    Help a student in {stage} stage to answer their question
    with {tone} tone and {level} of details in subject.
    here is the question that you should answer:
    {question}
    Answer with 500 word max.
    """
    response = model.generate_content(prompt)
    st.write(response.text)