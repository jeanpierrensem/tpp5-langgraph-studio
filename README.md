#  TP 5 - Langgraph Studio  : Prof SARA RETAL

## Prerequis communs


- asyncio : utilisation des E/S en mode asynchrone, non bloquant
- mcp.server.fastmcp :  FastMCP
- tavily :  TavilyClient
- typing : Dict, Any
- requests import get



## Génération Augmentée par Récupération

<img src="2.png">


## fonctionnalité implémentées
### PARTIE 1 : Intégration d’un serveur MCP local avec chargement dynamique de tools, resources et prompts
- MCP local server via stdio
- Récupération dynamique des tools
- Resources MCP
- Prompt dynamique côté serveur MCP
- Agent LLM modulaire avec serveur MCP local (tools, resources et prompts dynamiques)

<img src="captures/1.png">

<img src="captures/2.png">

<img src="captures/3.png">

### PARTIE 2 : Agent LLM avec outil MCP de temps (time server) pour interrogation de l’heure en zone spécifique
- Configuration et initialisation d’un client MCP pour un serveur de temps avec gestion de timezone
- Récupération dynamique des tools
- Création et exécution d’un agent LLM avec outils MCP pour la consultation du temps local

<img src="captures/4.png">

### PARTIE 3 : Agent pour se connecter à un serveur MCP distant via HTTP streaming

<img src="captures/5.png">