import streamlit as st

def show():
    # Hero section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.title("🏗️ Welcome to El Rawaa3-Architectural")
        st.markdown("""
        ### Building Dreams, Creating Futures
        We are a leading construction company specializing in innovative and sustainable building solutions.
        """)
        st.markdown("---")
        
        # Key features
        st.subheader("Why Choose Us?")
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            st.markdown("**🎯 Experience**")
            st.write("Over 7 years in construction industry")
        
        with col_b:
            st.markdown("**✅ Quality**")
            st.write("Premium materials and craftsmanship")
        
        with col_c:
            st.markdown("**♻️ Sustainability**")
            st.write("Eco-friendly building practices")
    
    with col2:
        st.image("https://via.placeholder.com/400x300/4A90E2/FFFFFF?text=Construction+Excellence", 
                 caption="Building Excellence Since 2010",
                 use_container_width=True)
    
    # Statistics section
    st.markdown("---")
    st.subheader("📊 Our Track Record")
    metric1, metric2, metric3, metric4 = st.columns(4)
    
    with metric1:
        st.metric("Projects Completed", "50+", "+3")
    with metric2:
        st.metric("Happy Clients", "35+", "+12")
    with metric3:
        st.metric("Team Members", "15+", "+2")
    with metric4:
        st.metric("Years Experience", "8+", "+1")