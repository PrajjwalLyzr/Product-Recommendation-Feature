import streamlit as st
import os
from utils import utils
from PIL import Image
from productRecommendation import recommendation_analyzr


# page config
st.set_page_config(
        page_title="Lyzr - Product Recommendation",
        layout="centered",   
        initial_sidebar_state="auto",
        page_icon="./logo/lyzr-logo-cut.png"
    )

# style the app
st.markdown("""
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    [data-testid="stSidebar"][aria-expanded="true"]{
           min-width: 450px;
           max-width: 450px;
       }
    </style>
    """, unsafe_allow_html=True)


# Streamlit app interface
image = Image.open("./logo/lyzr-logo.png")
st.image(image, width=150)
st.title('Product Recommender')
st.markdown('An app leveraging Lyzr.ai to helps manufacturers discover suitable industrial machinery based on their specific needs and budget.')

# Setting up the sidebar for input
st.sidebar.title("Product Recommender")
api_key = st.sidebar.text_input("Enter your OpenAI API key", type='password')
# submit_api_key = st.sidebar.button("Submit API Key")


if api_key != '':
    # if submit_api_key:
        # utils.save_api_key(api_key)
        # st.sidebar.success('API Key Saved!!!')

        # with open('api_key.txt', 'r') as file:
        #     api_key = file.read()
        #     api_key = api_key.replace(" ","")

    os.environ['OPENAI_API_KEY'] = api_key

    col1, col2 = st.columns(2)
    with col1:
        material = st.selectbox(label='Type of material will the machine be working with', options=['None', 'Plastic Resin', 'Metal Filament', 'Sheet Metal', 'Steel', 'Aluminium', 'Brass', 'Plastic','Textiles', 'Leather', 'Thermoplastics', 'Various', 'Various Paints', 'Wood', 'Composites'])
        process = st.selectbox(label='Desired manufacturing process', options=['None', 'Additive Manufacturing', 'Automation', 'Finishing', 'Machining','Metal Fabrication', 'Plastic Manufacturing', 'Textile Manufacturing'])
        power = st.slider('Power in kW', min_value=0, max_value=20)

    with col2:
        budget = st.text_input('Budget for the new machine in dollars')
        automation_level = st.selectbox(label='Automation level of machine', options=['None','Automatic', 'Mannual', 'CNC'])
        weight = st.slider('Weight in tons', min_value=0.25, max_value=5.0)

    if (material and process and automation_level) != 'None':
        if st.button('Submit'):
            st.markdown('---')
            product = recommendation_analyzr(material=material, budget=budget, automation_level=automation_level, process=process, power=power, weight=weight)
            st.text_input('Recommended Product', value=product)
            

        

