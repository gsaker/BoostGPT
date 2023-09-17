from revChatGPT.V3 import Chatbot
import os
import json
from typing import List
chatbot :Chatbot = None 

def getConfigDir(progName: str) -> str:
    return os.path.join(os.path.expanduser("~"), ".config", progName)
def createConfigDir(configDir: str):
    if not os.path.isdir(configDir):
        os.makedirs(configDir)
def writeConfigFile(key,data):
    fullPath = os.path.join(configDir, configFileName)
    newData = {key: data}
    try:
        with open(fullPath, "r") as file:
            jsonData = json.load(file)  # read existing JSON data
    except FileNotFoundError:
        jsonData = {}  # create empty JSON object if file doesn't exist
    jsonData.update(newData)  # add new data to existing JSON object
    with open(fullPath, "w") as file:
        json.dump(jsonData, file)  # write updated JSON object to file
def readConfigFile(key):
    fullPath = os.path.join(configDir, configFileName)
    with open(fullPath, "r") as file:
        data = json.load(file)
        return data[key]
def loadPrompts():
    prompts = readConfigFile("prompts")
    promptArray = []
    for prompt in prompts.splitlines():
        promptArray.append(prompt.split(":"))
    return promptArray
def initialSetup():
    global apiKey
    global chatbot
    if not checkIfConfigFileExists():
        createConfigDir(getConfigDir(progName))
        writeConfigFile("apiKey", "")
        writeConfigFile("prompts", "")
        writeConfigFile("chatbot","gpt-3")
    apiKey = readConfigFile("apiKey")
    chatbot = Chatbot(readConfigFile("apiKey"))
def checkIfConfigFileExists():
    fullPath = os.path.join(configDir, configFileName)
    print(os.path.isfile(fullPath))
    return os.path.isfile(fullPath)
#Globals
progName = "BoostGPT"
configArray = []
configFileName = "config.json"
configDir = getConfigDir(progName)
apiKey:str = None