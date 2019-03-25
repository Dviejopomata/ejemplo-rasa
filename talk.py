import time

import IPython
from IPython.display import clear_output, HTML, display
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter

interpreter = RasaNLUInterpreter('models/current/nlu')
messages = ["Hi! you can chat in this window. Type 'stop' to end the conversation."]
agent = Agent.load('models/dialogue', interpreter=interpreter)


def chatlogs_html(messages):
    messages_html = ""
    for m in messages:
        if m.endswith('.jpg'):
            messages_html += "<img src={}, alt='Tiger pub'></img>".format(m)
        else:
            messages_html += "<p>{}</p>".format(m)
    chatbot_html = """<div class="chat-window" {}</div>""".format(messages_html)
    return chatbot_html


while True:
    clear_output()
    display(HTML(chatlogs_html(messages)).data)
    time.sleep(0.3)
    a = input()
    messages.append(a)
    if a == 'stop':
        break
    responses = agent.handle_message(a)
    for r in responses:
        key = 'image' if 'image' in r.keys() else 'text'
        messages.append(r.get(key))
