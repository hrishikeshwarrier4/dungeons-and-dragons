#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 02:00:37 2024

@author: hrishikeshwarrier
"""

import streamlit as st
import os
from openai import OpenAI

# Ideally, use environment variables for API keys to avoid exposing them in your code.
api_key = os.getenv('NEW_OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

def generate_text(prompt):
    try:
        response = client.completions.create(
            model="gpt-3.5-turbo-0125",  # Adjust as necessary, considering newer models
            prompt=prompt,
            temperature=0.7,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0,
            presence_penalty=0
        )
        # Accessing the response directly, as response objects are now Pydantic models
        return response.choices[0].text.strip()
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return "Error generating text."

st.title('AI Dungeon Master')

user_input = st.text_input("What's your next move?", '')

if user_input:
    ai_response = generate_text(user_input)
    st.text(ai_response)