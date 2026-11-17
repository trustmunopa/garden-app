import streamlit as st

import queries
from db import connect

conn = connect()

st.title("Remove a bed")
crop = st.selectbox("Pick a bed", queries.crops(conn))

with st.form("remove_bed"):
    st.write("Remove the bed we picked above")
    if st.form_submit_button("Remove bed"):
        if queries.remove_bed(conn, crop):
            st.rerun()
        else:
            st.error(f"Can't remove {crop}: it still has logs.")
