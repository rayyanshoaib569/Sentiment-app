import streamlit as st

st.set_page_config(
    page_title="CryptoTrend AI",
    page_icon="📈",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

.main {
    background-color: #0f172a;
}

.metric-card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #334155;
}

.big-title {
    font-size: 42px;
    font-weight: bold;
    color: #38bdf8;
}

.signal-buy {
    color: #22c55e;
    font-size: 32px;
    font-weight: bold;
}

.signal-sell {
    color: #ef4444;
    font-size: 32px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<p class="big-title">📈 CryptoTrend AI</p>',
    unsafe_allow_html=True
)

st.caption("Professional Trend Analysis Dashboard")

st.divider()

asset = st.selectbox(
    "Select Asset",
    ["BTCUSDT", "ETHUSDT", "SOLUSDT", "TSLA", "NVDA"]
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Price",
        "$108,500",
        "+2.4%"
    )

with col2:
    st.metric(
        "RSI(14)",
        "62",
        "+3"
    )

with col3:
    st.metric(
        "ATR %",
        "3.4%",
        "-0.2%"
    )

with col4:
    st.metric(
        "Trend",
        "Bullish",
        "MA20 > MA50"
    )

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.subheader("Trend Analysis")

    st.info("""
    MA20 = 106,200

    MA50 = 103,800

    Signal: BULLISH
    """)

with col2:

    st.subheader("Momentum")

    st.success("""
    RSI = 62

    Strong Bullish Momentum
    """)

st.divider()

st.subheader("AI Trade Signal")

st.markdown(
    '<p class="signal-buy">🟢 STRONG BUY</p>',
    unsafe_allow_html=True
)

st.progress(84)

st.write("Confidence Score: 84%")

st.divider()

st.subheader("Price Chart")

st.line_chart({
    "Price":[100,102,101,104,106,105,108],
    "MA20":[99,100,100,101,102,103,104],
    "MA50":[95,96,97,98,99,100,101]
})
