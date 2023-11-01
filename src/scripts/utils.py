import numpy as np
import streamlit as st


def local_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def external_css(file_url):
    st.markdown(
        f'<link href="{file_url}" rel="stylesheet">', unsafe_allow_html=True
    )


def wide_col():
    return st.columns((0.02, 1, 0.02))


def narrow_col():
    return st.columns((0.35, 1, 0.35))


def narrow_col_intro():
    return st.columns((0.1, 1, 0.1))


def two_cols():
    return st.columns((0.1, 1, 0.2, 1, 0.1))


### DEFINE UTILITY FUNCTIONS
def log_utility(c):
    return np.log(c)


def crra_utility(c, gamma=2):
    if gamma == 1:
        return np.log(c)
    else:
        return c ** (1 - gamma) / (1 - gamma)
