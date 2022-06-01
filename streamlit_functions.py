import streamlit as st


def create_custom_css() -> str:
    custom_css = '<style>' \
                 'div[data-testid="stVerticalBlock"] > div:nth-of-type(3) > div[data-testid="stVerticalBlock"] ' \
                 '  { background-color: #E9F2FC; padding: 0.4rem 0.8rem; inline-size: min-content; ' \
                 '    overflow-wrap: break-word; margin-bottom: 1.6rem }' \
                 'div[data-testid="stVerticalBlock"] > div:nth-of-type(4) > div:first-of-type[data-testid="column"] ' \
                 '  { background-color: #F0F2F6; padding: 0.4rem 0.8rem; inline-size: min-content; ' \
                 '    overflow-wrap: break-word; }' \
                 'div[data-testid="stVerticalBlock"] > div:nth-of-type(5) > div:first-of-type[data-testid="column"] ' \
                 '  { background-color: #D4EDDA; padding: 0.4rem 0.8rem; inline-size: min-content; ' \
                 '    overflow-wrap: break-word; }' \
                 'div[data-testid="stMarkdownContainer"] > p { margin-bottom: 0em; }' \
                 'div[data-testid="stVerticalBlock"] { padding-bottom: 0.6em; }'
    return st.markdown(custom_css, unsafe_allow_html=True)


def create_output_markdown(text: str) -> str:
    return st.markdown(f'<span style="font-family: monospace; font-size: 0.9em; font-weight: 400; '
                       f'padding-bottom: 0.8em;">{text}</span>', unsafe_allow_html=True)
