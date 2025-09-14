### What is Model Context Protocol? (MCP)
The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) was 
initially released by Antropic (the creators of Claude) in November 
of 2024 and is an open standard for integrating
Large Language Models (LLMs) with external data sources and systems.

MCP allows a wide range of systems to be connected with with Generative AI
and its popularity and utility has increased dramatically over the past 
year as AI Agents have been integrated with a wide range of applications 
in many different industries.

The following diagram from the MCP website illustrates how MCP connects 
different AI applications with different data sources and systems:
![MCP Diagram](imgs/mcp-simple-diagram.png)

MCP has an inner **Data layer** that defines the JSON-RPC protocol for
client-server communication and an outer **Tranport layer** that defines
the data exchange between the client and servers.
