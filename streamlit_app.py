import streamlit as st
import base64

# Set page configuration
st.set_page_config(
    page_title="SAGE - Smart Assistant that Gets Everything done",
    page_icon="✨",
    layout="wide"
)

# Function to read the HTML file
def get_html_content():
    with open('landing_page.html', 'r') as f:
        return f.read()

# Display the HTML content
def main():
    html_content = get_html_content()
    
    # Use HTML component to render the page
    st.components.v1.html(html_content, height=8000, scrolling=False)

if __name__ == "__main__":
    main()