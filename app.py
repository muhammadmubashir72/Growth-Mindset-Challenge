import streamlit as st
import random

# Default Motivational Quotes List
default_quotes = [
    "🌟 Believe in yourself and all that you are.",
    "🔥 Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "⏳ Don’t watch the clock; do what it does. Keep going.",
    "💡 The only way to do great work is to love what you do.",
    "🚀 You are never too old to set another goal or to dream a new dream.",
]

# Initialize session state for storing quotes
if "quotes" not in st.session_state:
    st.session_state.quotes = default_quotes.copy()

# Function to get a random quote
def get_random_quote():
    return random.choice(st.session_state.quotes)

# Streamlit UI
st.set_page_config(page_title="Motivation & Quotes", page_icon="💬", layout="centered")
st.title("💬 Daily Motivation & Quotes App")
st.write("Start your day with some inspiration! 🚀")

# Show Random Quote
quote = get_random_quote()
st.markdown(f"""
    <div style="background:#f4f4f4; padding:20px; border-radius:10px; text-align:center; font-size:18px;">
        <b>{quote}</b>
    </div>
""", unsafe_allow_html=True)

# Button to Refresh Quote
st.markdown("### 🔄 Get a New Quote")
if st.button("🔄 Refresh"):
    quote = get_random_quote()
    st.markdown(f"""
        <div style="background:#f4f4f4; padding:20px; border-radius:10px; text-align:center; font-size:18px;">
            <b>{quote}</b>
        </div>
    """, unsafe_allow_html=True)

# User Input to Add New Quotes
st.markdown("### ✨ Add Your Favorite Quote")
new_quote = st.text_input("Enter a motivational quote:")
if st.button("➕ Add Quote"):
    if new_quote:
        st.session_state.quotes.append("💡 " + new_quote)
        st.success("✅ Your quote has been added!")
    else:
        st.warning("⚠️ Please enter a quote before adding.")

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
