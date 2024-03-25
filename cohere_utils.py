import cohere

co = cohere.Client('dx4dffEstJvLVfBIgiwXRwJGwBl3jJP36ZP7OYVE')

def query(prompt:str,debug:bool=False):
    response = co.chat(prompt,temperature = 0.5)
    text = response.text
    if debug:
        return response
    else:
        return text

def chatbot(history:list[dict],message:str,preamble=str,debug:bool=False,temp:float=0.4): # what ails you?
    """
        Generates a response from a chatbot given a history of previous messages, a new message, and optional parameters.

        Parameters:
        - history (list[dict]): A list of dictionaries representing the chat history. Each dictionary should have a "role" key with a value of "USER" or "CHATBOT", and a "message" key with the corresponding message.
        - message (str): The new message to be processed by the chatbot.
        - preamble (str, optional): An optional preamble to be used in the chatbot response. Defaults to an empty string.
        - debug (bool, optional): A flag indicating whether to return additional debugging information. Defaults to False.
        - temp (float, optional): The temperature parameter for controlling the randomness of the chatbot response. Defaults to 0.4.

        Returns:
        - If debug is True, returns a tuple containing the chatbot response object and the updated chat history.
        - If debug is False, returns a tuple containing the chatbot response text and the updated chat history.
    """
    if message.startswith('--'): # TODO: add more commands
        if message.startswith('--settemp'):
            
            temp = float(message.split(' ')[1])

    if len(preamble) != 0:
        response = co.chat(chat_history=history,
                        preamble_override=preamble,
                        message=message,
                        connectors=[{"id": "web-search"}],
                        temperature=temp)
    else:
        response = co.chat(chat_history=history,
                        message=message,
                        connectors=[{"id": "web-search"}],
                        temperature=temp)
    msg = [{"role":"USER","message":message},
           {"role":"CHATBOT","message":response.text}]
    history += msg
    if debug:
        return response, msg
    else:
        return response.text, history

