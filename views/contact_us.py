import streamlit as st
import re

def show():
    st.title("📞 Contact Us")
    st.markdown("### Get in Touch with El Rawaa3-Architectural")
    st.markdown("---")
    
    # Two-column layout
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        st.subheader("Send Us a Message")
        
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Your Name *", placeholder="Mohamed Ali")
            email = st.text_input("Your Email *", placeholder="mohamed.ali@example.com")
            phone = st.text_input("Phone Number", placeholder="+1 (555) 123-4567")
            
            project_type = st.selectbox(
                "Project Type *",
                ["Select...", "Residential Construction", "Commercial Construction", 
                 "Renovation & Remodeling", "Architectural Design", "Other"]
            )
            
            message = st.text_area(
                "Message *", 
                placeholder="Tell us about your project...",
                height=150
            )
            
            submitted = st.form_submit_button("📧 Send Message", use_container_width=True)
            
            if submitted:
                # Basic validation
                if not name or not email or not message or project_type == "Select...":
                    st.error("⚠️ Please fill in all required fields marked with *")
                elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    st.error("⚠️ Please enter a valid email address")
                else:
                    st.success("✅ Thank you for contacting us! We will get back to you within 24 hours.")
                    st.balloons()
    
    with col2:
        st.subheader("📍 Our Office")
        
        st.markdown("""
        **Address:**  
        American Plaza  
        Building Suite 13  
        City Cairo, Plz 12345
        
        **Phone:**  
        +20 (0) 1121252163
        
        **Email:**  
        info@elrawaa3-arch.com
        
        **Business Hours:**  
        Saturday - Thursday: 9:00 AM - 5:00 PM  
        Friday: Closed
        """)
        
        st.markdown("---")
        st.subheader("🌐 Follow Us")
        st.markdown("""
        [LinkedIn](#) | [Facebook](#) | [Instagram](#) | [Twitter](#)
        """)
    
    # FAQ section
    st.markdown("---")
    st.subheader("❓ Frequently Asked Questions")
    
    with st.expander("How long does a typical project take?"):
        st.write("Project timelines vary based on scope and complexity. Residential projects typically take 6-12 months, while commercial projects may take 12-24 months.")
    
    with st.expander("Do you provide free consultations?"):
        st.write("Yes! We offer free initial consultations to discuss your project requirements and provide preliminary assessments.")
    
    with st.expander("What areas do you serve?"):
        st.write("We primarily serve the metropolitan area and surrounding regions within a 100-mile radius of our office.")