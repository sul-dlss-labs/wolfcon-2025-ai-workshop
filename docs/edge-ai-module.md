### Edge AI Module 

The FOLIO [Edge AI Module][EDGE_AI] uses the [Pydantic AI][PYDANTIC_AI]
Generative AI agent framework to provide a set of API endpoints for interacting with 
different AI agents for for different FOLIO modules.

This backend module supports the following Generative AI services:

- OpenAI's ChatGPT (requires an API token)
- Anthropic Claude (requires an API token)
- Google Gemini (requires an API token)
- Locally hosted Llama model (through a hosted [GPT4ALL](https://www.nomic.ai/gpt4all) or [LLaMA.cpp](https://github.com/ggerganov/llama.cpp) instance)

By leveraging [Pydantic AI][PYDANTIC_AI], [Edge AI][EDGE_AI] Agents can do the following:

- Let developers define [Instructions](https://ai.pydantic.dev/agents/#instructions), either static that
  are defined in code or dynamic instructions based on the agent's current context.
- Define [Function Tools](https://ai.pydantic.dev/tools/) to allow models to perform actions and 
  retrieve additional information to help the models generate a response.
- Generate different outputs like JSON using [Structured output types](https://ai.pydantic.dev/output/)
- Define [Dependencies](https://ai.pydantic.dev/dependencies/) that can be injected to Instructions, tools,
  and output validators for the agent.
- Use different Generative AI [Models](https://ai.pydantic.dev/api/models/base/) and use different
  [model settings](https://ai.pydantic.dev/agents/#additional-configuration) to fine-tune the model's 
  responses.

[EDGE_AI]: https://github.com/folio-labs/edge-ai
[PYDANTIC_AI]: https://ai.pydantic.dev/
