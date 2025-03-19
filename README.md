# 📊 AI-Powered CSV Analysis Suite

**Interactive data analysis tool with natural language queries and automated visualization**

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)


## 🌟 Key Features

### 📈 Intelligent Analysis
- Natural language query processing using GPT-4 Turbo
- Automated statistical analysis and insights generation
- Context-aware data interpretation

### 🎨 Smart Visualization
- Auto-detection of best visualization type
- Support for multiple chart types:
  - Bar Charts (Vertical/Horizontal)
  - Line Graphs
  - Pie Charts
  - Scatter Plots
  - Histograms
- Interactive Plotly charts with zoom/pan capabilities

### ⚙️ Technical Highlights
- LangChain agent for pandas DataFrame operations
- Error-resistant query parsing
- Responsive Streamlit UI
- CSV schema understanding
- Caching for large datasets

## 🚀 Quick Start

### Prerequisites
- OpenAI API key (GPT-4 enabled account)
- Python 3.9+

```bash
# Clone repository
git clone https://github.com/humzawaqar66/Chatbot-CSV-Analysis-OpenAI-LangChain-Streamlit-Integration.git
cd ai-csv-analyst

# Install dependencies
pip install -r requirements.txt

# Set API key (Linux/MacOS)
export OPENAI_API_KEY="your-api-key-here"
```

```bash
streamlit run app.py
```

### 🖥️ User Guide
Upload CSV
Upload Demo
Supported files: Any comma-separated CSV file

## Ask Questions
###Examples of supported queries:
```markdown
"Compare sales between Q1 and Q2 using a bar chart"
"Show distribution of age groups as pie chart"
"Plot temperature trends over time with a line graph"
"What's the correlation between price and demand?"
```
## Interpret Results

Natural language analysis
Interactive visualizations
Data summary statistics

## 🛠️ Technical Stack

###Component	Technology

NLP Engine:    	OpenAI GPT-4 Turbo
Data Framework:	LangChain + pandas
Visualization:	Matplotlib + Plotly
UI Framework:  	Streamlit
Cache System:	  LRU caching for query results


## Retail Analytics
```markdown
"Show monthly sales trends for 2023"
"Compare product category performance"
"Identify top 10 customers by purchase value"
```
## Healthcare Data
```markdown
"Visualize patient age distribution"
"Plot BMI vs cholesterol levels correlation"
"Show percentage of patients by blood type"
```
## Financial Analysis
```markdown
"Chart stock price volatility over time"
"Compare sector performance in Q3"
"Identify outliers in transaction amounts"
```

# ⚠️ Limitations
Maximum CSV size: 100MB (contact for enterprise needs)
Requires GPT-4 API access
Timezone-naive datetime handling
Limited image export capabilities

# 📜 License
MIT License - See LICENSE for details

