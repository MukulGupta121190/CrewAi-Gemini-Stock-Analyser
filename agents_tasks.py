from crewai import Agent, Task, Crew, Process, LLM
from custom_tools import (
    fetch_stock_data, 
    fetch_stock_financials, 
    fetch_stock_news,
    search_tool,
    get_current_stock_price
)
import os
from datetime import datetime

# Current date for context
Today = datetime.now().strftime("%Y-%m-%d")

# Set dummy OpenAI API key to bypass validation
os.environ["OPENAI_API_KEY"] = "dummy-key"

# Create a single LLM instance to be used by all agents
def get_llm():
    gemini_key = os.getenv("GEMINI_API_KEY")
    model_name = os.getenv("MODEL_NAME") # Use the standard model name
    
    if not gemini_key:
        raise ValueError("Missing GEMINI_API_KEY in .env file")
    
    # Create CrewAI LLM instance with Gemini
    return LLM(
        provider="google",
        model=model_name,
        api_key=gemini_key,
        temperature=0,
        verbose=True
    )

# Create the LLM instance
llm_instance = get_llm()

# Create embeddings instance
""" embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={'device': 'cpu'}
) """

# Agent for gathering financial data
data_collector = Agent(
    role="Stock Data Collector",
    goal="Efficiently gather stock market data for financial analysis.",
    backstory=("A reliable financial data collector who has access to stock data APIs and tools."),
    llm=llm_instance,
    tools=[fetch_stock_data, fetch_stock_financials],
    verbose=True,
    max_iter=5,
    allow_delegation=False, 

)

data_collection_task = Task(
    description="Collect key stock data metrics for {company_stock} using its ticker format. Use only the data provided and do not request for more metrics.",
    expected_output="Data about most relevant financial metrics, income statement for stock analysis. Indicate also about current financial status and trend over the period",
    agent=data_collector,
    async_execution=False,
)

# News Researcher 
news_reader = Agent(
    role="News and Info Researcher",
    goal="Gather and provide the latest news and information about the company from the internet",
    llm=llm_instance,
    verbose=True,
    backstory=f"You are an expert researcher who can gather detailed information about a company. Consider you are on: {Today}",
    tools=[search_tool],
    cache=True,
    max_iter=5,
    allow_delegation=False, 
)

news_reader_task = Task(
    description="Find the latest financial news and business information about company: {company_stock} and summarize the key points from recent articles.",
    expected_output="A summary of the latest news and business information about {company_stock}.",
    agent=news_reader,
    llm=llm_instance,
)

# Financial Analyst  
financial_analyst = Agent(
    role="Financial Analyst",
    goal="Analyze financial stock data and use stock information to write a comprehensive stock analysis report.",
    backstory=(
        f"You are an expert in analyzing financial data, stock/company-related current information and "
        f"making a comprehensive stock analysis report. Use Indian units for numbers (lakh,crore). "
        f"Consider you are on: {Today}"
    ),
    tools=[fetch_stock_data, fetch_stock_financials, fetch_stock_news],
    verbose=True,
    max_iter=5,
    llm=llm_instance,
)

# Task to analyse financial data and news
financial_analysis_task = Task(
    description=(
        "Analyze the research on {company_stock} and write a comprehensive stock analysis report."
    ),
    expected_output=(
        "A detailed report that includes analysis of the stock data, financial insights, recent news and market information "
        "followed by the conclusion."
    ),
    agent=financial_analyst,
    output_file="stock_report.txt",
    async_execution=False,
    context=[data_collection_task, news_reader_task],
    llm=llm_instance,
)

financial_expert = Agent(
    role="Financial Expert",
    goal="Coordinate financial analysis of a stock, make investment recommendations",
    backstory=(
        f"You are an expert financial advisor who can provide investment recommendations. "
        f"Consider the financial analysis, current information about the company, current stock price, "
        f"and make recommendations about whether to buy/hold/sell a stock along with reasons. "
        f"When using tools, try with and without the suffix '.NS' to the stock symbol and see what works. "
        f"Consider you are on: {Today}"
    ),
    llm=llm_instance,
    verbose=True,
    tools=[get_current_stock_price, fetch_stock_data],
    max_iter=5,
)

# Task to make investment recommendations
advise = Task(
    description=(
        "Make a recommendation about investing in a stock, based on the financial analysis and current stock price. "
        "First, get the current stock price using the get_current_stock_price tool. "
        "Then, analyze the financial data and make a recommendation. "
        "Explain the reasons for your recommendation."
    ),
    expected_output=(
        "A recommendation about whether to buy/hold/sell a stock along with elaborated reasons, "
        "including current price analysis and financial metrics."
    ),
    agent=financial_expert,
    context=[financial_analysis_task],
    llm=llm_instance,
)

crew = Crew(
    agents=[data_collector, news_reader, financial_analyst, financial_expert],
    tasks=[data_collection_task, news_reader_task, financial_analysis_task, advise],
    verbose=True,
    process=Process.sequential,
    memory=False,  # Disable memory to prevent RAG storage errors
    llm=llm_instance
)
