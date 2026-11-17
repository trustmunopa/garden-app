import streamlit as st

import queries
from db import connect

conn = connect()

st.title("Fix a crop name")
crop = st.selectbox("Pick a bed", queries.crops(conn))

with st.form("fix_crop"):
    new_crop = st.text_input("Fix the name of this bed", value=crop)
    if st.form_submit_button("Fix name"):
        queries.fix_crop(conn, crop, new_crop)
        st.rerun()
