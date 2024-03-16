## loading all the environment variables
from dotenv import load_dotenv
load_dotenv() 

# Import Important libraries
import streamlit as st
import google.generativeai as genai
import os

# Configure Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set up the Model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
},
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

# Load Gemini Pro model
model = genai.GenerativeModel(model_name="gemini-pro", generation_config=generation_config, safety_settings=safety_settings)


# Navbar
st.set_page_config(
    page_title="Blog Section",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# title of our app
st.title('✍️ Farhan BlogGPT')

# create a subheader
st.subheader("AI Blog Section Generator 🤖")

# sidebar for the user input

with st.sidebar:
    st.title("Input Settings")
    st.subheader("Enter Details for the Section")
    
    # Section Heading
    section_heading = st.text_input("Section Heading ")
    
    # Subpoints
    
    subpoints = st.text_area("Subpoints (comma-separated)")
    
    # Add the Voice Tones
    voice_tones = st.sidebar.selectbox("Choose Voice Tones:", ["Formal","Friendly", "Bold", "Adventurous", "Witty", "Professional", "Casual", "Informative", "Creative", "Trendy", "Caring", "Cheerful", "Futuristic"])
    
    # Add the Writing Styles
    writing_styles = st.sidebar.selectbox("Choose Writing Styles:", ["Academic", "Conversational", "Creative", "Critical", "Descriptive", "Instructive", "Technical", "Analytical"])
    
    num_words = st.number_input("Number of words", min_value=250, max_value=3000, step=50)

    # Primary Keyword
    #primary_keyword = st.text_input("Primary Keyword ")
    
    # Secondary Keyword
    #secondary_keyword = st.text_input("Secondary Keyword")
    
    # Reference Article Link
    # reference_article_link = st.text_input("Reference Article Link")

    # Prompt
    prompt_parts = [
            f"""
            Please ignore all previous instructions. I want you to respond only in English. I want you to act as a highly skilled marketer and top-tier copywriter who is fluent in English. I want you to pretend that you are an expert at writing all types of CTAs in English. Write an section for the blog post about {section_heading}. Subpoint or supporting detail: {subpoints}(optional).
            Follow these instructions:
            1. You have a {voice_tones} tone of voice. 
            2. You have a {writing_styles} writing style. I want you to write around {num_words} words. 
            3. Mentions the number of words in the end of response.
            3. Avoiding jargon and complex terms.
            4. Write like a human.
            5. Focus first on creating high quality, thorough content that provides value to readers. 
            6. Improve scannability with headings, bullet points, lists, images, stats, and other visual elements where applicable.
            7. Keep paragraphs 3 sentences or less. Turn long sentences into two shorter ones.
            8. Markdown formatting where applicable
            9. When preparing the article, prepare to write the necessary words in bold. 
            10. Write content so that it can outrank other websites. 
            11. Do not reply that there are many factors that influence good search rankings.
            12. I know that quality of content is just one of them, and it is your task to write the best possible quality content here, not to lecture me on general SEO rules.
            13. Make sure that you don't follow ai pattern but article should be really simple and it should make sense. 
            14. Make sure to add a bit of humor and add some funny lines. Also add bold and italic
            15. write the information in your own words rather than copying and pasting from other sources also double-check for plagiarism because I need pure unique content
            
            """
            ]

    # Submit Button
    submit_button = st.button("Generate")

    # Clear All Button
    clear_button = st.button("Clear All")

if submit_button:
    # Display the spinner
        # Generate the response
        response = model.generate_content(prompt_parts)

        # Display the blog output
        st.write(response.text)
        
        
        

