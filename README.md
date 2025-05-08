

# CrewAI Multi Agent Stock Analyzer 📊🤖
**An AI-powered stock analysis and investment recommendation app built using [CrewAI Agents](https://www.crewai.com), [Gemini LLM](https://ai.google.dev/), [DuckDuckGo Search](https://duckduckgo.com/) and real-time financial data via Yahoo Finance. The application uses multi-agent AI with Gemini models to collect stock data, news, research/web scraping and perform financial analysis & generates comprehensive reports, news summaries, and buy/hold/sell advice.**


---

## 🔍 Features

- 📈 Real-time stock data, financial ratios, and historical trends
- 📰 Latest company-specific news analysis
- 🧠 Multi-agent reasoning using CrewAI
- 💡 Buy/Hold/Sell recommendations based on financial insights
- 📨 Report generation + optional email delivery
- 🧾 Exports PDF report for LinkedIn, email, or investor presentation use

---

## 🛠️ Tech Stack

- **CrewAI** – Autonomous multi-agent orchestration
- **Google Gemini (via Langchain)** – LLM for reasoning and generation
- **Yahoo Finance API** – Real-time financial data
- **Streamlit** – Interactive web UI
- **pdfkit + markdown** – PDF report generation
- **smtplib** – Email dispatch functionality
The Stock Analysis Report Generator allows users to generate comprehensive stock analysis reports based on company names or stock tickers. The application uses multi-agent AI with Gemini models using the [CrewAI framework](https://github.com/crewAIInc/crewAI) to collect stock data, news, research/web scraping and perform financial analysis. The Crew operates as hierarchical process with a manager agent coordinating the tasks of the other agaents. The agentic wokrflow has been evaluated using the AgentOps platform to trace the LLM output.

## 🤖🤖 Agents:**
- Stock Data Collector
- News Reader
- Financial Analyst
- Financial Expert

## Workflow
- Input company name or stock ticker to generate reports.
- Fetches real-time stock data and historical prices.
- Extract financial data from income statements, balance sheets and cash flow.
- Summarizes recent news articles related to the stock.
- Conducts stock market research with web scraping. 
- Generates a detailed stock analysis report in both text/markdown and PDF formats.
- Displays the report and chain of thought reasoning in the user interface. 
- Sends the generated report via email.

**Run Application:**
```bash
streamlit run app.py
```
## 🚀 Demo Screenshot

![App Screenshot](screenshot.png)

## Screenshots
<img width="308" alt="img1" src="https://github.com/user-attachments/assets/f087f0ab-4a62-4de4-8235-79d588f9acc8">
<img width="388" alt="img2" src="https://github.com/user-attachments/assets/592d5a9b-7118-407e-bb55-39610414ffb6">
<img width="505" alt="img3" src="https://github.com/user-attachments/assets/fef3d724-0c81-49f9-a949-80ccd7e63938"><br></br>
<img width="411" alt="img4" src="https://github.com/user-attachments/assets/5892b045-ab56-4e52-a1eb-92cf7ad8fa15">

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/MukulGupta121190/CrewAi-Gemini-Stock-Analyser.git
cd CrewAi-Gemini-Stock-Analyser
```

### 2. Create a virtual environment and install dependencies
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt
```

### 3. Configure .env
```bash
LITELLM_PROVIDER=gemini
MODEL_NAME=gemini-2.0-flash-lite
GEMINI_API_KEY=your_google_gemini_api_key
GOOGLE_APPLICATION_CREDENTIALS=path_to_your_service_account.json
AGENTOPS_API_KEY=your_agentops_api_key
SENDER_EMAIL=your_email@gmail.com
EMAIL_PASSWORD=your_app_specific_password
```

## 🔐 Why GOOGLE_APPLICATION_CREDENTIALS Is Required?

Gemini’s web tools and some Langchain integrations require access to Google Cloud resources (e.g., embedding, vector search). This is authenticated via a service account JSON file, pointed to by GOOGLE_APPLICATION_CREDENTIALS.
You can generate this JSON from:

## 🛡️ CrewAI Gemini Compatibility Fix
By default, CrewAI expects an OpenAI API key even if you’re using Google Gemini. To avoid this, we apply the following temporary workaround in config.py or before initializing the Crew:
```bash
os.environ["OPENAI_API_KEY"] = "dummy-key"
os.environ["AGENTOPS_DISABLED"] = "true"
```
This bypasses internal validation and disables telemetry via AgentOps.
