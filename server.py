from rasa_core.agent import Agent
from rasa_core.channels.socketio import SocketIOInput
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig

action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
interpreter = RasaNLUInterpreter('./models/current/nlu')
agent = Agent.load('./models/current/dialogue', interpreter=interpreter, action_endpoint=action_endpoint)

input_channel = SocketIOInput(
    # event name for messages sent from the user
    user_message_evt="user_uttered",
    # event name for messages sent from the bot
    bot_message_evt="bot_uttered",
    # socket.io namespace to use for the messages
    namespace=None
)

# set serve_forever=True if you want to keep the server running
s = agent.handle_channels([input_channel], 5004, serve_forever=True)
