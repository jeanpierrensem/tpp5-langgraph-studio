from langchain.tools import tool
from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain.messages import HumanMessage
#TP MULTI-AGENT : resource -> fichier 8 TP Multi-Agents.docx
# le but de ce tp est de créer un système multi-agent où les agents sont organisés de manière hiérarchique. 
# agent_manager = il joue le role de manager et appelle les autrres agents à travvers des outils
# agent squre_root : calcule la racine carée d'un nombre
# agent square : calcule le carré d'un nombre 
# on besoin d'un fichier de configuration(pont entre le code python et l'outil langgraph studio) qui va faire le lien entre notre agent 
# manager et l'outils langgraph pour visualisation = langGraph studio.(pour la visualisation. du graphe)
# le fichier de configuration dit où se trouve ton agent, comment le charger, quel environnement utiliser, comment lancer le projet
# utilité de langgraph studio = visualiser le graphe de votre agent, deboggage

#création de l'outil square_root
@tool
def square_root(x: float) -> float:
    """Calculate the square root of a number"""
    return x ** 0.5

#création de l'outil square
@tool
def square(x: float) -> float:
    """Calculate the square of a number"""
    return x ** 2

# 1-création des sous-agents


# sous-agent square_root basé sur le tool square_root
subagent_1 = create_agent(
    model='gpt-5-nano',
    tools=[square_root]
)

# sous-agent square basé sur le tool square
subagent_2 = create_agent(
    model='gpt-5-nano',
    tools=[square]
)

#création d'un agent principal(agent manager)
@tool
def call_subagent_1(x: float) -> float:
    """Call subagent 1 in order to calculate the square root of a number"""
    response = subagent_1.invoke({"messages": [HumanMessage(content=f"Calculate the square root of {x}")]})
    return response["messages"][-1].content

@tool
def call_subagent_2(x: float) -> float:
    """Call subagent 2 in order to calculate the square of a number"""
    response = subagent_2.invoke({"messages": [HumanMessage(content=f"Calculate the square of {x}")]})
    return response["messages"][-1].content

#genet manager avec les outils
main_agent = create_agent(
    model='gpt-5-nano',
    tools=[call_subagent_1, call_subagent_2],
    system_prompt="You are a helpful assistant who can call subagents to calculate the square root or square of a number."
)

#test : va se faire sur une interface graphique

