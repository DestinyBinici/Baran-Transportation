import streamlit as st
from PIL import Image

def main():
    st.set_page_config(page_title="Baran Transportation", page_icon=":truck:", layout="wide")

    st.title("Baran Transportation")

    st.header("About Us")
    st.write("Baran Transportation is a trusted truck business operating in the United States. We provide reliable and efficient transportation services to meet all your logistics needs.")

    st.header("Our Services")
    services = [
        "Long-haul transportation",
        "Local deliveries",
        "Specialized freight",
        "Logistics solutions"
    ]
    for service in services:
        st.write(f"- {service}")

    st.header("Contact Information")
    st.write("Phone: (904) 566-9082")
    st.write("Owners: Cihan Binici and Kader Binici")

    st.header("Location")
    st.write("We are proudly serving across the United States.")

    st.header("Our Fleet")
    col1, col2 = st.columns(2)

    # Placeholder images
    with col1:
        st.image("/api/placeholder/400/300", caption="Truck 1")
    with col2:
        st.image("/api/placeholder/400/300", caption="Truck 2")

if __name__ == "__main__":
    main()
