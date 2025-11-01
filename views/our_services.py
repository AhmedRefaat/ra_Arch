import streamlit as st

def show():
    st.title("🔧 Our Services")
    st.markdown("### Comprehensive Construction Solutions for Every Need")
    st.markdown("---")
    
    # Services in expandable sections
    services = [
        {
            "title": "🏠 Residential Construction",
            "description": "Custom home building, housing developments, and residential complexes designed to meet your lifestyle needs.",
            "features": ["Custom Home Design", "Multi-family Units", "Luxury Villas", "Eco-friendly Homes"]
        },
        {
            "title": "🏢 Commercial Construction",
            "description": "Office buildings, retail spaces, and commercial complexes built to industry standards and specifications.",
            "features": ["Office Buildings", "Retail Spaces", "Warehouses", "Mixed-Use Developments"]
        },
        {
            "title": "🔨 Renovation & Remodeling",
            "description": "Transform existing spaces with our expert renovation and remodeling services for both residential and commercial properties.",
            "features": ["Kitchen Remodeling", "Bathroom Upgrades", "Space Extensions", "Interior Redesign"]
        },
        {
            "title": "📐 Architectural Design",
            "description": "Innovative and functional architectural designs that blend aesthetics with practicality and sustainability.",
            "features": ["3D Modeling", "Blueprint Development", "Space Planning", "Sustainable Design"]
        },
        {
            "title": "📋 Project Management",
            "description": "End-to-end project management ensuring timely delivery, budget adherence, and quality assurance.",
            "features": ["Timeline Planning", "Budget Management", "Quality Control", "Resource Coordination"]
        }
    ]
    
    # Display services in cards
    for i, service in enumerate(services):
        with st.expander(service["title"], expanded=(i==0)):
            st.write(service["description"])
            st.markdown("**Key Features:**")
            cols = st.columns(2)
            for idx, feature in enumerate(service["features"]):
                with cols[idx % 2]:
                    st.markdown(f"✓ {feature}")
    
    # Call to action
    st.markdown("---")
    st.info("💡 **Need a custom solution?** Contact us to discuss your specific project requirements!")