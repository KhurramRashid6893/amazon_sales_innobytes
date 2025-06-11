```markdown
# Amazon Sales Dashboard with AI Insights

An interactive Streamlit dashboard for visualizing and analyzing Amazon sales data, enriched with AI-generated business insights via Google GenAI (Gemini).

## 🚀 Features

- **Sales Overview**: Monthly sales trends line chart  
- **Product Analysis**: Top categories and sizes by quantity/orders  
- **Fulfillment Analysis**: Pie chart & status breakdown for fulfillment methods  
- **Customer Segmentation**: B2C vs. B2B sales comparison  
- **Geographical Analysis**: Top-N states and cities by revenue/orders  
- **KPI Metrics**: Total sales, total orders, average order value  
- **AI Insights**: One-click Gemini-powered, contextual insights based on your filters  
- **Full Sidebar Customization**: Date range, categories, sizes, fulfillment methods, B2B toggle, Top-N sliders  
- **Data Export & Search**: Download filtered data; search orders by ID  
- **File Upload**: Drop-in CSV upload to override default dataset  

## 📁 Repository Structure

```

amazon-dashboard/
├── dashboard.py          # Main Streamlit application
├── Amazon Sale Report.csv# Sample dataset (rename if needed)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

````

## 🛠️ Prerequisites

- Python 3.8+  
- Google GenAI API key (Gemini)  

## ⚙️ Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/amazon-dashboard.git
   cd amazon-dashboard
````

2. **Create & activate a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate       # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Key**

   * Set environment variable:

     ```bash
     export GENAI_API_KEY="YOUR_GEMINI_API_KEY"   # macOS/Linux
     set GENAI_API_KEY="YOUR_GEMINI_API_KEY"      # Windows
     ```
   * Or replace the placeholder in `dashboard.py`:

     ```python
     genai.configure(api_key="YOUR_GEMINI_API_KEY")
     ```

## ▶️ Usage

Run the Streamlit app locally:

```bash
streamlit run dashboard.py
```

* Open [http://localhost:8501](http://localhost:8501) in your browser.
* Use the sidebar to filter data, upload your own CSV, and generate AI insights.

## ☁️ Deployment

1. **Push to GitHub**

   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**

   * Go to [share.streamlit.io](https://share.streamlit.io/)
   * Connect your GitHub repo and select `dashboard.py`
   * Set the `GENAI_API_KEY` in the Secrets section
   * Click **Deploy**

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m "Add YourFeature"`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

* [Streamlit](https://streamlit.io/) for the rapid dashboard framework
* [Plotly Express](https://plotly.com/python/plotly-express/) for interactive charts
* [Google GenAI (Gemini)](https://developers.generativeai.google/) for AI-powered insights

```
```
