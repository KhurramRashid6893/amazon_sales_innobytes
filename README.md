````markdown
# 📊 Amazon Sales Dashboard with AI Insights

An **interactive**, single-page Streamlit app to explore Amazon sales data with **AI-powered** recommendations.
Live here: https://amazonsalesinnobytes.streamlit.app/
---

## 🔗 Quick Links

- [Live Demo](#) • 
- [Getting Started](#getting-started) • 
- [Features](#features) • 
- [Usage](#usage) • 
- [Deployment](#deployment) • 
- [Contributing](#contributing) • 
- [License](#license)

---

## 🖼️ Features

- **KPI Metrics**: Total Sales, Total Orders, Avg. Order Value  
- **Sales Overview**: Interactive monthly trends chart  
- **Product Analysis**: Top categories & sizes by volume  
- **Fulfillment Analysis**: Pie & bar breakdown of methods & statuses  
- **Customer Segmentation**: B2C vs. B2B visualization  
- **Geographical Analysis**: Top-N states & cities filters  
- **AI Insights**: One-click Gemini-powered business recommendations  
- **Full Sidebar**: Date range, category/size filters, B2B toggle, Top-N sliders  
- **Extras**: CSV upload/download, Order ID search, real-time filtering  

---

## 📥 Getting Started

1. **Clone repository**  
   ```bash
   git clone https://github.com/your-username/amazon-dashboard.git
   cd amazon-dashboard
````

2. **Create & activate virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate       # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API key**

   * **Option A**: Set env var

     ```bash
     export GENAI_API_KEY="YOUR_GEMINI_KEY"   # macOS/Linux
     set GENAI_API_KEY="YOUR_GEMINI_KEY"      # Windows
     ```
   * **Option B**: Edit `dashboard.py` and replace the placeholder.

5. **Place your data**

   * Ensure `Amazon Sale Report.csv` is in the root folder (or upload via sidebar).

---

## ▶️ Usage

Run locally:

```bash
streamlit run dashboard.py
```

* Open [http://localhost:8501](http://localhost:8501)
* Use sidebar controls to filter data, upload new CSVs, and generate AI insights!

---

## ☁️ Deployment

1. Push to GitHub:

   ```bash
   git add .
   git commit -m "Add Streamlit dashboard"
   git push origin main
   ```
2. On **Streamlit Cloud**:

   * Go to [share.streamlit.io](https://share.streamlit.io/)
   * Connect your repo, point to `dashboard.py`
   * Set `GENAI_API_KEY` in Secrets
   * Click **Deploy**

---

```
```
