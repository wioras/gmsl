#!/usr/bin/env python3
"""
Optional Python / Streamlit Host Wrapper for Valeo_GMSL2_Pulse_WebSerial.html.
Serves the Web Serial browser application so users connect directly to their own
local USB/COM ports (EVKIT & PL303QMD-P) through Chrome/Edge over HTTPS.
"""
import os
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Valeo – GMSL2 Pulse (Web Serial)", layout="wide")
st.markdown("<style>.block-container{padding:0 !important; max-width:100% !important;} header,footer{visibility:hidden;}</style>", unsafe_allow_html=True)

html_path = os.path.join(os.path.dirname(__file__), "Valeo_GMSL2_Pulse_WebSerial.html")
with open(html_path, "r", encoding="utf-8") as f:
    html_src = f.read()

components.html(html_src, height=960, scrolling=True)
