

# CrewAI Multi Agent Stock Analyzer 📊🤖

<img align="right" alt="Agentic AI Stock Analyser APP" height="220" width="500" src="https://github.com/user-attachments/assets/b16234cb-3791-4af5-8ef3-b16cd7f2e3dd">

**An AI-powered stock analysis and investment recommendation app built using [CrewAI Agents](https://www.crewai.com), [Gemini LLM](https://ai.google.dev/), [DuckDuckGo Search](https://duckduckgo.com/) and real-time financial data via Yahoo Finance. The application uses multi-agent AI with Gemini models to collect stock data, news, research/web scraping and perform financial analysis & generates comprehensive reports, news summaries, and buy/hold/sell advice.**


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


## 🤖🤖 Agents:
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
## 🚀 Demo Screenshots
<img width="450" alt="Application Interface" src="https://github.com/user-attachments/assets/35592071-f31c-4dc9-b478-16dafcfe60c2"/>
<img width="400" alt="Reliance_Industries_Stock_Analysis_Report" src="https://github.com/user-attachments/assets/95113f64-643a-427e-98ab-a4401da441b5"/>

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
### 4. Download and install wkhtmltopdf package to convert html files to pdf reports

- Download wkhtmltopdf package from https://wkhtmltopdf.org/downloads.html
- Use the following command on Mac terminal to install the package on your machine
```bash
Sudo installer -pkg /path_to_package/wkhtmltox-0.12.6-2.macos-cocoa.pkg -target /usr/local/bin
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

## Contributions
Contributions to this project are welcome! If you have any ideas for improvements, bug fixes, or new features, feel free to submit a pull request.

## Contact
For any questions or issues, please contact **[mukulgupta121190@gmail.com]** or feel free to reach out to me on **[LinkedIn](https://www.linkedin.com/in/mukulgupta0991/)**.

<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://www.linkedin.com/in/mukulgupta0991" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="mukulgupta0991" height="30" width="40" /></a>
<a href="https://www.hackerrank.com/mukulgupta121190" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/hackerrank.svg" alt="mukulgupta121190" height="30" width="40" /></a>
<a href="https://medium.com/@mukulgupta121190" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/medium.svg" alt="@mukulgupta121190" height="30" width="40" /></a>
<a href="https://kaggle.com/mukulgupta121190" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/kaggle.svg" alt="mukulgupta121190" height="30" width="40" /></a>
</p>
