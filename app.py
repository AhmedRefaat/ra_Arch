# import streamlit as st
# from pages import homepage, our_services, contact_us

# st.set_page_config(page_title="RA-Architecture", layout="centered")

# st.sidebar.title("Navigation")
# page = st.sidebar.radio("Go to", ("Homepage", "Our Services", "Contact Us"))

# if page == "Homepage":
#     homepage.show()
# elif page == "Our Services":
#     our_services.show()
# elif page == "Contact Us":
#     contact_us.show()



import streamlit as st
from views import homepage, our_services, contact_us

# Page configuration
st.set_page_config(
    page_title="RA-Architecture",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stRadio > label {
        font-size: 1.1rem;
        font-weight: 500;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.image("https://via.placeholder.com/200x80/2E86AB/FFFFFF?text=RA-Architecture", use_container_width=True)
    st.markdown("---")
    st.title("🏗️ Navigation")
    page = st.radio("Go to:", ("Homepage", "Our Services", "Contact Us"))
    st.markdown("---")
    st.caption("© 2025 RA-Architecture")

# Page routing
if page == "Homepage":
    homepage.show()
elif page == "Our Services":
    our_services.show()
elif page == "Contact Us":
    contact_us.show()