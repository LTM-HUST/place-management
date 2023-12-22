import os

RESPONSE_CODE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "response_code.txt")

def code2message(response_code):
    with open(RESPONSE_CODE_PATH, "r") as f:
        lines = f.readlines()
        
    for line in lines:
        [code, message] = line.split(" ", 1)
        if str(code) == str(response_code):
            return message[:-1] if message.endswith("\n") else message