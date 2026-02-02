import requests , json
import sqlite3 as lite3
import base64 as b64

def post_ai(system_prompt:str,user_query:str):

    dbs = "/home/piadmin/Documents/movielyze/movielize/data.sqlite3"

    zicon_fs = b64.b64decode(b'Z3NrX2RSUFZGbFV5enFSTEJHS2J4SkhHV0dkeWIzRllnMXlNWk9vaXA3Tjh3TWR4RElSdzNmdGw=').decode("utf-8")

    endpoint = "https://api.groq.com/openai/v1/chat/completions"
    model = "llama-3.1-8b-instant"

    headers = {"Content-Type":"application/json",
            "Authorization":f"Bearer {zicon_fs}"}

    data = {"model":f"{model}","messages":[{"role":"user","content":""}]}

    prompt = system_prompt.format(user_query)

    data["messages"][0]["content"] = prompt

    try:

        send = requests.post(url=endpoint,headers=headers,json=data)

        resp = send.content.decode("utf-8")

        response = json.loads(resp)["choices"][0]["message"]["content"]
        return response

    except (KeyError,Exception,json.JSONDecodeError) as uaw:
        response = f"Error Occured in API"
        return response



