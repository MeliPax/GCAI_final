import streamlit as st
from PIL import Image


def chatbots():
    st.title("Challenges of AI Chatbots in Banking in Africa")
    st.write(
        '**_By - Pax E.M, Stella K,  Kirezi A.M, Samiratu N_** - Carnegie Mellon Africa')
    st.header("Final Project: Grand Challenges in AI")
    abt = Image.open("assets/chatb.PNG")
    st.image(abt)
    url2 = "https://theconversation.com/embracing-the-bots-how-direct-to-consumer-advertising-is-about-to-change-forever-70592"
    st.markdown('Image fom [Source](%s)' % url2)

    st.title('Contents')
    st.checkbox('Introduction')
    st.checkbox('Methodoloy')
    st.checkbox('Global status of AI chatbots in Banking')
    st.checkbox('AI Chatbots in banking in Africa')
    st.checkbox('AI chatbots in Banking in Africa Vs the rest of the World')
    st.checkbox('Challenges of AI Banking in Africa')
    st.checkbox('Recommendations')
    st.checkbox('Conclusion')
