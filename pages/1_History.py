import streamlit as st

import queries
from db import connect

conn = connect()

st.title("History")
crop = st.selectbox("Pick a bed", queries.crops(conn))
st.dataframe(queries.history(conn, crop), hide_index=True)
