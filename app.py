from datetime import datetime
import streamlit as st
import time
from images_functions import download_images, process_images
from streamlit_functions import create_custom_css, create_output_markdown


# WEB (STREAMLIT) VERSION OF THE CONCURRENCY DEMO APP

# THE ACTUAL PROCESS
def run_processing(nr_images: int, threading_enabled: bool, multi_processing_enabled: bool, skip_second_part: bool) \
        -> None:
    with output.container():

        create_output_markdown('Started <span style="font-weight: 800;">part 1</span> at '
                               f'{datetime.now():%d-%m-%Y %H:%M:%S}...</span>')
        t1 = time.perf_counter()

        download_images(nr_images, threading_enabled)

        t2 = time.perf_counter()

        create_output_markdown('Finished <span style="font-weight: 800;">part 1</span> at '
                               f'{datetime.now():%d-%m-%Y %H:%M:%S}.</span>')

        create_output_markdown('')

        if not skip_second_part:
            create_output_markdown('Started <span style="font-weight: 800;">part 2</span> at '
                                   f'{datetime.now():%d-%m-%Y %H:%M:%S}...</span>')
            t3 = time.perf_counter()

            process_images(nr_images, multi_processing_enabled)

            t4 = time.perf_counter()

            create_output_markdown('Finished <span style="font-weight: 800;">part 2</span> at '
                                   f'{datetime.now():%d-%m-%Y %H:%M:%S}.</span>')

    with summary.container():
        create_output_markdown(f'Number of images: <span style="font-weight: 800;">{nr_images}</span> | '
                               f'Threading: <span style="font-weight: 800;">{threading_enabled}</span> | '
                               f'Multi processing: <span style="font-weight: 800;">{multi_processing_enabled}</span> | '
                               f'Skip second part: <span style="font-weight: 800;">{skip_second_part}</span>')
        create_output_markdown('<span style="font-weight: 800;">Part 1</span> took <span '
                               f'style="font-weight: 800; font-style: italic;">{round(t2 - t1, 2)}</span> seconds')
        if not skip_second_part:
            create_output_markdown('<span style="font-weight: 800;">Part 2</span> took <span '
                                   f'style="font-weight: 800; font-style: italic;">{round(t4 - t3, 2)}</span> seconds')


# SETUP
st.set_page_config(page_title='Concurrency with Python', layout='wide')
create_custom_css()

# TITLE
st.subheader('Concurrency with Python: threading and multiprocessing')

# EXPLANATION
with st.container():
    st.markdown('<span style="font-size: 0.9rem;">This simple Python app is split in two parts '
                'to explain the options to improve execution performance by ***threading*** - for IO bound processes - '
                'on one hand and ***multiprocessing*** - for CPU bound processes - on the other hand. It will download '
                'a given number of random images from [Lorem Picsum](https://picsum.photos/). This is the first part; '
                'the IO bound part. Next it will iterate over all the retrieved image and resize them and apply a '
                'filter to them. This second part is the CPU bound part.</span>'
                '<div style="padding-bottom: 0.4em;"></div>', unsafe_allow_html=True)
    st.markdown('<span style="font-size: 0.9rem;">Both parts of the process can be run *with* or '
                '*without* the performance enhancements, by selecting the *threading* and *multiprocessing* checkboxes '
                'below, so the difference can be actively experienced by playing around with the settings.</span>'
                '<div style="padding-bottom: 0.4em;"></div>', unsafe_allow_html=True)
    st.markdown('<span style="font-size: 0.9rem;">The source code for this app can be found on '
                '[Github](https://github.com/mwiertz/python_concurrency).</span>'
                '<div style="padding-bottom: 1em;"></div>', unsafe_allow_html=True)

# ACTUAL APP PART OF THE UI
c11, c12 = st.columns([5, 1])
with c11:
    output = st.empty()

with c12:
    nr_images = st.number_input('Number of images', min_value=10, max_value=2500, step=10, value=500)
    threading_enabled = st.checkbox('Threading')
    multi_processing_enabled = st.checkbox('Multi processing')

c21, c22 = st.columns([5, 1])
with c21:
    summary = st.empty()

with c22:
    if st.button('Run part 1'):
        run_processing(nr_images, threading_enabled, multi_processing_enabled, skip_second_part=True)
    if st.button('Run part 1 & 2'):
        run_processing(nr_images, threading_enabled, multi_processing_enabled, skip_second_part=False)
