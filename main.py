import streamlit as st

# Setting page layout to wide
st.set_page_config(layout="wide", page_title="Papi Letter", page_icon="images/papi.png")

col3, col4 = st.columns([2,4])

with col3:
    st.image("images/papi.png", caption="Rafa y Cris")

with col4:
    with open("letter.txt", 'r', encoding="utf-8") as file:
        carta = file.read()
    st.info(carta)

    st.markdown(
        '[Father and son icons created by Freepik - Flaticon](https://www.flaticon.com/free-icons/father-and-son)',
        unsafe_allow_html=True
    )


