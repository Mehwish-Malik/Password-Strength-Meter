import streamlit as st 
import re 

# Set up page configuration
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")

# App title and description
st.title("🔐  Password Strength Meter")
st.markdown("""
🔐 **Welcome to the Ultimate Strength Checker!**  
🛠️ Use this simple tool to test how strong your password is.  
💡 Get helpful tips to create a secure and powerful password.  
🧠 Stay smart. 🔒 Stay safe.
""")

# Password input
password = st.text_input("Enter Your Password", type="password")

# Initialize feedback and score
feedback = []
score = 0

if password:
    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper and lower case check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain both uppercase and lowercase characters.")

    # Digit check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one digit.")

    # Special character check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Final feedback
    if score == 4:
        feedback.append("✅ Your password is strong!")
    elif score == 3:
        feedback.append("⚠️ Moderate password – consider adding more security features.")
    else:
        feedback.append("❌ Weak password – please make it stronger using the suggestions above.")
    
    st.markdown("## Feedback")
    for tip in feedback:
        st.write(tip)
else:
    st.info("Please enter your password to get started.")

# Signature
st.markdown("---")
st.markdown(" 👩‍💻 Created with 💫by **Mehwish Malik**")
