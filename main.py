import streamlit as st

from bitcoin.dashboard import fig

# Display chart using Streamlit
st.plotly_chart(fig, use_container_width=True)
