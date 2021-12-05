import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib as plt


def chatbots():
    st.title('Global status of AI chatbots in Banking')
    st.write("**Projected total Bank Chatbot Cost Savings by 2023**")
    img = Image.open("assets/stats.PNG")
    st.image(img, width=353)
    urlst = "https://www.juniperresearch.com/infographics/ai-in-fintech-statistics"
    st.write('From [Juniperresearch.com](%s)' % urlst)
    st.markdown("""
     Banks have been using AI-based Chatbots to serve their customers in a novel ways like:
    - Providing 24/7 customers Services
    - Banks have used it to make services such as setting up accounts
    - Checking account balances
    - Money transfers,
    - Scheduling bill payments
    - e.t.c
    """)
    st.write("This has proven to be both time and cost saving for banks")

    st.header("What are the Challenges?")
    st.write("**_A. People using different languages_**")
    url = "https://aclanthology.org/2020.findings-emnlp.195.pdf"
    url2 = "https://en.wikipedia.org/wiki/Languages_of_Africa"
    # dataf = pd.read_csv('datasets/num-speakers.csv')
    # st.table(dataf.head(10))
    # st.markdown("[Source](%s)" % url2)

    img1 = Image.open("assets/barhh.png")
    st.image(img1)

    st.write(
        "**_B. Lack of digital corpora of African languages that can be used for NLP training_**")
    imgb = Image.open("assets/final.png")
    st.image(imgb)
    st.write(
        'Subset of African Languages and number of speakers according to Joshi et al (2020)')
    df = pd.read_csv('datasets/englishvsothers.csv')
    st.table(df)
    st.markdown("[Source](%s)" % url)

    st.write("**_C. Non-responsiveness of Existing Chatbots_**")
    st.write(
        "**_D. Illiteracy and a lack of understanding and adopting new technology_**")
    st.write("**_E. Lack of access to good infrastructure_**")

    original_title = '<p style="font-family:Courier; color:Blue; font-size: 20px;">       </p>'
    st.markdown(original_title, unsafe_allow_html=True)

    st.header('**AI chatbots in Banking in Africa Vs the rest of the World**')
    df_compare = pd.read_csv('datasets/compare.csv')
    st.table(df_compare)
