import streamlit as st

# Streamlit Web App Title
st.title("📈 Live Trend Catcher - Stock Screener")

# High-Tech Theme
st.markdown(
    """
    <style>
    body {
        background-color: #030307;
        color: white;
    }
    .stButton>button {
        background-color: #0047ab;
        color: white;
        font-size: 18px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display Welcome Message
st.write("Welcome to the Live Trend Catcher Stock Screener powerd by TRADING VIEW!")

# User Input: Ticker Symbol
ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA, MSFT):", "AAPL")

# User Input: Percentage Threshold
threshold = st.slider("Select Percentage Change Threshold (%)", 1, 10, 5)

# Button to Trigger Stock Monitoring
if st.button("🔍 Start Monitoring"):
    st.success(f"Monitoring {ticker} for {threshold}% change...")
    # Placeholder for actual stock monitoring logic
    # (This can be replaced with Alpaca API or Yahoo Finance)

# Display Footer
st.write("Developed with ❤️ using Streamlit.")
