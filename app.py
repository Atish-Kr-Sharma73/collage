import streamlit as st

st.title('CampusX')

col1, col2 = st.columns(2)

with col1:
    st.image('1687467329658.jpg')

with col2:
    st.write("""
    At its core, CampusX aims to change this education system of India. We believe that high-quality education is not just for the privileged few. It is the right of everyone who seeks it. Through our mentorship program, we aim to bring quality education to every single student. A mentored student is provided with guidance on how to ace a technology through 24x7 mentorship, live and recorded video lectures, daily skill-building activities, project assignments, and evaluation, hackathons, interactions with industry experts, soft skill training, personal counseling, and comprehensive reports. All we need from you is intent, a ray of passion to learn.
    """)

st.header('Course Offered')
st.subheader('Data science')
st.subheader('Data Analysis')
st.subheader('Data Engineering')