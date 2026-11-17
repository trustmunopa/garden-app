import streamlit as st

# this imports the queries.py file in our project in its entirety, and just the connect and reset things in the "db.py"
# note how the .py is omitted from the imported module file name

import queries      
from db import connect, reset

conn = connect()

st.title("Garden Beds")
st.write("Pick a page in the sidebar.")
st.caption(f"Logs with no bed: {queries.orphan_count(conn)}")

# RESET: throw away garden.db so the app builds a fresh one
if st.button("Reset garden"):
    conn.close()
    reset()
    st.rerun()
