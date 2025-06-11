import streamlit as st
import pandas as pd
import plotly.express as px
from google import genai

# ─── Configure GenAI Client ────────────────────────────────────────────────
client = genai.Client(api_key="AIzaSyDS1336LlHoyxTfvkJCgRRl4cpO34jtfl4")

# ─── 1) Data Loading & Caching ──────────────────────────────────────────────
@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df = df.drop(columns=['New', 'PendingS'], errors='ignore')
    df = df.dropna(subset=['Amount', 'currency'])
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date'])
    return df

# ─── 2) AI Insights Helper ──────────────────────────────────────────────────
@st.cache_data
def get_ai_insights(prompt: str) -> str:
    resp = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return resp.text

# ─── 3) App Setup ───────────────────────────────────────────────────────────
st.set_page_config(page_title="Amazon Sales Dashboard", layout="wide")
st.title("📊 Amazon Sales Dashboard with AI Insights")

# ─── Sidebar: File Upload & Filters ─────────────────────────────────────────
st.sidebar.title("🔎 Customize Dashboard")

# 3.1 CSV Upload or Default
data_file = st.sidebar.file_uploader("Upload CSV (or use default)", type=["csv"])
if data_file:
    df = pd.read_csv(data_file)
else:
    df = load_data("Amazon Sale Report.csv")

# parse dates
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])

# 3.2 Date Range Filter
min_date = df['Date'].dt.date.min()
max_date = df['Date'].dt.date.max()
start_date, end_date = st.sidebar.date_input(
    "Select date range",
    [min_date, max_date],
    min_value=min_date, max_value=max_date
)
df = df[(df['Date'].dt.date >= start_date) & (df['Date'].dt.date <= end_date)]

# 3.3 Category & Size Filters
cats = st.sidebar.multiselect(
    "Filter Categories",
    options=df['Category'].unique(),
    default=df['Category'].unique()
)
sizes = st.sidebar.multiselect(
    "Filter Sizes",
    options=df['Size'].unique(),
    default=df['Size'].unique()
)
df = df[df['Category'].isin(cats) & df['Size'].isin(sizes)]

# 3.4 Fulfilment & B2B Toggle
fulfill_sel = st.sidebar.multiselect(
    "Fulfilment Method",
    options=df['Fulfilment'].unique(),
    default=df['Fulfilment'].unique()
)
b2b_only = st.sidebar.checkbox("Show only B2B orders", value=False)
df = df[df['Fulfilment'].isin(fulfill_sel)]
if b2b_only:
    df = df[df['B2B'] == True]

# 3.5 Top-N Controls
top_n_state = st.sidebar.slider("Top N States", 5, 20, 10)
top_n_city  = st.sidebar.slider("Top N Cities", 5, 20, 10)

st.sidebar.markdown("---")
st.sidebar.write(f"Showing **{len(df):,}** orders from **{start_date}** to **{end_date}**")

# 3.6 Download & Search
with st.sidebar.expander("🔽 More Tools"):
    csv_data = df.to_csv(index=False).encode()
    st.download_button("Download Filtered Data", csv_data, "filtered_orders.csv", mime="text/csv")
    oid = st.text_input("Search by Order ID")
    if oid:
        st.write(df[df['Order ID'].str.contains(oid, case=False, na=False)])

# ─── 4) KPI Summary ─────────────────────────────────────────────────────────
st.header("📈 Key Metrics")
total_sales  = df['Amount'].sum()
total_orders = len(df)
avg_order    = df['Amount'].mean()

c1, c2, c3 = st.columns(3)
c1.metric("Total Sales",      f"₹{total_sales:,.0f}")
c2.metric("Total Orders",     f"{total_orders:,}")
c3.metric("Avg. Order Value", f"₹{avg_order:,.2f}")

# ─── 5) AI Insights Panel ──────────────────────────────────────────────────
if st.button("🧠 Generate AI Insights"):
    top_cat   = df.groupby('Category')['Qty'].sum().idxmax()
    top_state = df.groupby('ship-state')['Amount'].sum().idxmax()
    prompt = (
        f"We have {total_orders} orders totaling ₹{total_sales:,.0f} "
        f"from {start_date} to {end_date}. "
        f"Best-selling category: {top_cat}. Top state by revenue: {top_state}. "
        "Provide 3 concise, actionable business insights."
    )
    with st.spinner("Generating AI insights…"):
        insights = get_ai_insights(prompt)
    st.subheader("🤖 AI-Powered Insights")
    st.write(insights)

# ─── 6) Sales Overview ─────────────────────────────────────────────────────
if st.sidebar.checkbox("Show Sales Overview", True):
    st.subheader("1. Sales Overview")
    df['Month'] = df['Date'].dt.to_period('M').astype(str)
    monthly = df.groupby('Month')['Amount'].sum().reset_index()
    fig1 = px.line(monthly, x='Month', y='Amount', title="Monthly Sales Trend", markers=True)
    st.plotly_chart(fig1, use_container_width=True)

# ─── 7) Product Analysis ───────────────────────────────────────────────────
if st.sidebar.checkbox("Show Product Analysis", True):
    st.subheader("2. Product Analysis")
    cat_df = df.groupby('Category')['Qty'].sum().nlargest(10).reset_index()
    fig2 = px.bar(cat_df, x='Category', y='Qty', title="Top 10 Categories by Quantity Sold")
    st.plotly_chart(fig2, use_container_width=True)

    size_df = df['Size'].value_counts().nlargest(10).rename_axis('Size').reset_index(name='Count')
    fig3 = px.bar(size_df, x='Size', y='Count', title="Top 10 Sizes by Order Count")
    st.plotly_chart(fig3, use_container_width=True)

# ─── 8) Fulfillment Analysis ────────────────────────────────────────────────
if st.sidebar.checkbox("Show Fulfillment Analysis", False):
    st.subheader("3. Fulfillment Analysis")
    ful_df = df['Fulfilment'].value_counts().reset_index()
    ful_df.columns = ['Method', 'Count']
    fig4 = px.pie(ful_df, names='Method', values='Count', title="Fulfillment Method Split")
    st.plotly_chart(fig4, use_container_width=True)

    status_ful = df.groupby(['Fulfilment', 'Status']).size().reset_index(name='Count')
    fig4b = px.bar(
        status_ful, x='Fulfilment', y='Count', color='Status',
        barmode='group', title="Order Status by Fulfillment"
    )
    st.plotly_chart(fig4b, use_container_width=True)

# ─── 9) Customer Segmentation ──────────────────────────────────────────────
if st.sidebar.checkbox("Show Customer Segmentation", False):
    st.subheader("4. Customer Segmentation")
    seg = df.groupby('B2B')['Amount'].sum().reset_index(name='TotalSales')
    seg['Type'] = seg['B2B'].map({True:'B2B', False:'B2C'})
    fig5 = px.bar(seg, x='Type', y='TotalSales', title="Total Sales: B2C vs B2B")
    st.plotly_chart(fig5, use_container_width=True)

# ─── 10) Geographical Analysis ─────────────────────────────────────────────
if st.sidebar.checkbox("Show Geographical Analysis", False):
    st.subheader("5. Geographical Analysis")
    state_df = df.groupby('ship-state')['Amount'].sum().nlargest(top_n_state).reset_index()
    fig6 = px.bar(state_df, x='ship-state', y='Amount', title=f"Top {top_n_state} States by Sales")
    st.plotly_chart(fig6, use_container_width=True)

    city_df = df['ship-city'].value_counts().nlargest(top_n_city).rename_axis('City').reset_index(name='Orders')
    fig7 = px.bar(city_df, x='City', y='Orders', title=f"Top {top_n_city} Cities by Orders")
    st.plotly_chart(fig7, use_container_width=True)
