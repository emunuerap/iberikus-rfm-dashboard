
# Iberikus RFM Dashboard

This project simulates the work of a professional **Data Scientist hired by Iberikus**, a gourmet food distributor, to analyze customer behavior through **RFM segmentation** (Recency, Frequency, Monetary Value). The goal is to provide **actionable business insights** that help drive strategic decisions.

## 🚀 Features

- 📊 **Interactive RFM Dashboard**: Analyze customer segments in real-time
- 📈 **Dynamic KPIs**: Instantly update based on filters (cluster, frequency range)
- 🗂️ **Filtered Data Table**: View and explore segmented customers
- 🌐 **Multi-page layout**: Built using Dash Pages for clean navigation
- 🎨 **Modern UI**: Styled with Dash Bootstrap Components

## 📁 Project Structure

```
iberikus-rfm-dashboard/
│
├── app.py                     # Main Dash app entrypoint
├── requirements.txt           # Python dependencies
├── render.yaml                # Render.com deployment config
├── rfm_clustered_customers.csv # Input dataset (RFM + cluster)
│
├── pages/
│   ├── home.py                # Homepage with KPIs and insights
│   └── rfm_dashboard.py       # Main interactive dashboard
│
└── assets/
    └── iberikus_logo.png      # Logo used in UI
```

## ⚙️ Getting Started Locally

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/iberikus-rfm-dashboard.git
cd iberikus-rfm-dashboard
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

Then open your browser at [http://localhost:8050](http://localhost:8050)

## 🌍 Live Demo

If you deployed this on [Render.com](https://render.com/) or another platform, you can add the link here:

👉 [Live App](https://your-app.render.com)

## 🧠 Author

**Eduardo Porlan** – [LinkedIn](https://www.linkedin.com/in/eduardoporlan) · [Portfolio](https://www.eporlan.com)

## 🧪 Technologies Used

- Python
- Dash (Plotly)
- Pandas
- Dash Bootstrap Components
- Plotly Express
- Render (for deployment)
