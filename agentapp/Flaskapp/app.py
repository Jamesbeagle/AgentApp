from datetime import datetime, timedelta
from flask_cors import CORS, cross_origin 
from apiflask import APIFlask
from flask_cors import CORS, cross_origin
from flask import request, jsonify, make_response ,send_file
from ollama import chat
from ollama import ChatResponse

import threading
import random
import html

import time
import json
import re
import os

import logging
#import pandas as pd
import traceback
from threading import Thread


app = APIFlask(__name__)
# threading.Thread(target=checker_thread, daemon=True).start()
cors=CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
tools = {"search": "search", "weather": "get_weather", "stock": "get_stock_price"}

@app.route('/heartbeat', methods=['POST'])
def heartbeat():
    
    response: ChatResponse = chat(model='deepseek-r1:latest', messages=[
    {
        'role': 'system',
        'content': f"""you are an orchestrator that is responsible for deciding which tools and what content to use to answer a question.
                    here are the tools you can use {str(tools)}, if you do not have the tool to answer the question then respond with "NewTool_Required"
                     Your responses must be in JSON format:"""+ """
                     {"tool": "tool_name", "content": "content_to_use"} or {"tool": "NewTool_Required", "content": "content_to_use"}
                         """,
    },
    {
        'role': 'user',
        'content': 'what is the function of a Active Grill shutter',
    },
    ])
    print(response['message']['content'])
    return jsonify({"response": response['message']['content']})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)