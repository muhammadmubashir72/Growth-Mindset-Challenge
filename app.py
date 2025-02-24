import streamlit as st
import random

# Motivational Quotes List
quotes = [
    "Believe in yourself and all that you are.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Don’t watch the clock; do what it does. Keep going.",
    "The only way to do great work is to love what you do.",
    "You are never too old to set another goal or to dream a new dream.",
]

# Function to get a random quote
def get_random_quote():
    return random.choice(quotes)

# Streamlit UI
st.title("🌟 Daily Motivation & Quotes App")
st.write("Start your day with some inspiration! 🚀")

# Show Random Quote
quote = get_random_quote()
st.markdown(f"> **{quote}**")

# Button to Refresh Quote
if st.button("🔄 Get New Quote"):
    quote = get_random_quote()
    st.markdown(f"> **{quote}**")

# User Input to Add New Quotes
new_quote = st.text_input("✨ Add Your Favorite Quote:")
if st.button("Add Quote"):
    if new_quote:
        quotes.append(new_quote)
        st.success("Your quote has been added! ✅")
    else:
        st.warning("Please enter a quote before adding.")

# Footer
st.write("---")
st.write("Made with ❤️ using Streamlit")

