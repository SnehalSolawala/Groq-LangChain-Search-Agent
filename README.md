# 🔎 LangChain Chat with Search (Streamlit + Groq + Tools)

This project is an **AI-powered chatbot** built with [Streamlit](https://streamlit.io/) and [LangChain](https://www.langchain.com/).  
It uses **Groq’s LLaMA 3.1 model** as the reasoning engine and integrates with external tools like **DuckDuckGo**, **Wikipedia**, and **arXiv** to provide up-to-date answers.  

💡 Instead of just relying on the LLM’s training data, the chatbot can **search the web, query Wikipedia, and fetch scientific papers** to enrich responses.

---

## 🚀 Features
- ✅ Interactive **chat interface** built with Streamlit.  
- ✅ Powered by **Groq LLaMA 3.1** model for fast reasoning.  
- ✅ Integrated **tools**:
  - 🌐 DuckDuckGo Search → fetch latest web results  
  - 📖 Wikipedia Query → get concise summaries  
  - 📑 Arxiv Query → retrieve research paper abstracts  
- ✅ **Session memory** – chatbot remembers conversation history.  
- ✅ **Streaming responses** – see the agent’s thought process live.  
- ✅ **Error handling** – detects invalid API keys gracefully.  

---

## 📦 Installation

Clone the repository and install dependencies:

```bash
https://github.com/SnehalSolawala/Groq-LangChain-Search-Agent.git
cd langchain-chat-search
pip install -r requirements.txt
```

🔑 API Key Setup

  This project requires a Groq API key.
  
  Get your API key from Groq
  .
  
  You can either:
  
  Enter it manually in the Streamlit sidebar when running the app, OR
  
  Store it in a .env file (recommended):
  
  GROQ_API_KEY=your_api_key_here


▶️ Usage

  Run the Streamlit app:
  
  streamlit run app.py
  
  
  Open the link in your browser (usually http://localhost:8501).
  
  Enter your Groq API key in the sidebar.
  
  Start chatting! 🎉

🛠️ Project Structure
├── app.py                # Main Streamlit app
├── requirements.txt       # Python dependencies
├── tools_agents.ipynb     # ipynb file for first testing the code working
├── .env.example           # Example environment variables
└── README.md              # Project documentation




⚙️ How It Works

User enters a query in the Streamlit chat UI.

The Groq-powered LLaMA model (LLM) reasons about the query.

If needed, the agent selects a tool (Search, Wikipedia, or Arxiv).

The tool fetches real-time or external knowledge.

LLM combines the tool output with its own reasoning.

Final answer is displayed in chat.

🔑 Agent type: ZERO_SHOT_REACT_DESCRIPTION (decides tool use based on descriptions).
