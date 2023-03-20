import streamlit as st

st.title("🖼️ yt-img-app")
st.header('Youtube Thumnail Image Extractor App')

with st.expander("About this app"):
    st.write('This app retrieves the thumbnail image from a Youtube video.')

# Image settings
st.sidebar.header('Settings')
img_dict = {'Max': 'maxresdefault','High':'hqdefault','Medium':'mqdefault','Low':'sddefault'}
selected_img_quality = st.sidebar.selectbox('Image Quality',list(img_dict.keys()))
img_quality = img_dict[selected_img_quality]

yt_url = st.text_input('Paste Youtube URL', 'https://youtu.be/JwSS7052dyM')

def get_ytid(input_url):
    if 'youtu.be' in input_url:
        ytid = input_url.split('/')[-1]
    if 'youtube.com' in input_url:
        ytid = input_url.split('=')[-1]
    return ytid

# Display Youtube thumbnail image
if yt_url != '':
    ytid = get_ytid(yt_url)

    yt_img = f'https://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
    st.image(yt_img)
    st.write('Youtube video thumbnail image URL: ', yt_img)
else:
    st.write('👆 Enter URL to continue ...')