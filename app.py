import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import  ArxivAPIWrapper,WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun,WikipediaQueryRun,DuckDuckGoSearchRun
from langchain.agents import initialize_agent,AgentType
from groq import GroqError
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
import os
from dotenv import load_dotenv


#Arxiv and wikipedia tools
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1,doc_content_chars_max=200)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

wiki_wrapper = WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=200)
wiki = WikipediaQueryRun(api_wrapper=wiki_wrapper)


search = DuckDuckGoSearchRun(name="search")

st.title("Langchain, chat with search")

"""
In this example, we're using `StreamlitCallbackHandler` to display the thoughts and actions of an agent in an interactive Streamlit app.
Try more LangChain 🤝 Streamlit Agent examples at [github.com/langchain-ai/streamlit-agent](https://github.com/langchain-ai/streamlit-agent).
"""


#side bar for settingssss
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter GROQ API KEY : ", type ="password")

# Stop execution if no key provided
if not api_key:
    st.warning("🔑 Please enter your GROQ API key in the sidebar to continue.")
    st.stop()

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role":"assistant","content":"Hi,I'm a chatbot who can search the web. How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt:=st.chat_input(placeholder="what is machine learning"):
    st.session_state.messages.append({"role":"user","content":prompt})
    st.chat_message("user").write(prompt)

    llm=ChatGroq(groq_api_key=api_key,model_name="llama-3.1-8b-instant",streaming=True)
    tools=[search,arxiv,wiki]

    search_agent=initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,handle_parsing_errors=True)


    #if wrong groq api then it shows error
    
    #with st.chat_message("assistant"):
        #st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
        #response=search_agent.run(st.session_state.messages,callbacks=[st_cb])
        #st.session_state.messages.append({'role':'assistant',"content":response})
        #st.write(response)
    

    #if wrong groq api then it shows enter valid groq api
    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)

        try:
            response = search_agent.run(
                st.session_state.messages,
                callbacks=[st_cb]
            )
            st.session_state.messages.append({'role': 'assistant', "content": response})
            st.write(response)

        except GroqError:
            st.error("❌ Invalid GROQ API Key. Please enter the correct key in the sidebar.")
            st.stop()
