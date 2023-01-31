#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st


# In[2]:


st.write("""
# Mini Chatbot 
 
** Ask me anything! ** """
)


# In[3]:


## READ KEYS 
import json 
import openai

f = open("open-ai.json") 
key = json.load(f)["key"];  


# In[4]:


def GPT_Completion(texts):
    ## Call the API key under your account (in a secure way)
    openai.api_key = key
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt =  texts,
    temperature = 0.6,
    top_p = 1,
    max_tokens = 64,
    frequency_penalty = 0,
    presence_penalty = 0
    )
    return st.text_area("Chatbot:", value=response.choices[0].text.lstrip(),height=200, max_chars=None, key=None)

## Provide 'training' to GPT-3 on how to be sarcastic
input = st.text_input('User:')

GPT_Completion(input)


# In[ ]:




