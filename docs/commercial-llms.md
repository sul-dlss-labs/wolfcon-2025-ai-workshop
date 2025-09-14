### Commercial Large Language Models (LLMs)
#### OpenAI's ChatGPT
The release of ChatGPT 3 by [OpenAI][OPENAI] in the fall of 2022 sparked 
the current boom in generative AI and Large Language Models (LLM). In March of 2023, 
OpenAI released ChatGPT 4 followed by various smaller upgrades with the release of ChatGPT 4.o.
[Last month](https://openai.com/index/introducing-gpt-5/) OpenAI released ChatGPT 5 with 
an improved reasoning model and a router that decides on specific tools and models based 
on the chat with the end user. However, ChatGPT 5 still suffers from the 
[same issues](https://garymarcus.substack.com/p/gpt-5-overdue-overhyped-and-underwhelming) that
earlier models suffered from including hallucinations and reasoning errors.


#### Microsoft ChatGPT Variant 
Microsoft has invested in [OpenAI][OPENAI] and is using a version of ChatGPT 4 in their Bing
[Copilot][COPILOT] search service. Microsoft's Copilot is 
able to access recent material after ChatGPT model's training data cut-off through a 
combination of Retrieval Assisted Generation (RAG), fine-tuning the model, and other methods. 

Additionally, through Microsoft's [Copilot][COPILOT] service, you can use ChatGPT's image 
generation functionality without paying for a separate [OpenAI][OPENAI] account. You
still need a Microsoft account to log in and use these advanced features. 

#### Google Gemini
In December of 2023, [Google][GOOG] publicly released their own Large Language Model (LLM)
to compete with OpenAI's ChatGPT. Their service called Gemini, is available at 
[https://gemini.google.com/][GEMINI]. 

Google Gemini has the [following models](https://ai.google.dev/gemini-api/docs/models) available 
for use through the Gemini API:

- **Gemini 2.5 Pro**: Google's most powerful thinking and multimodal model with maximum response accuracy
  and best performance of their models. It has a input token limit 1,048,576 and an output token
  limit of 65,536.[^2.5PRO]
- **Gemini 2.5 Flash**: Best price-performance multimodal model, accepts audio, video, and text. The model
  has an input token limit of 1,048,576 and an output token limit of 65,536.[^2.5FLASH]
- **Gemini 2.5 Flash-Lite**: Model is optimized for cost efficiency and low latency.
  
#### Anthropic's Claude
[Anthropic][ANTH] is a public-benefit corporation in San Francisco that developed and 
released a Large Language Model (LLM) called [Claude](https://www.anthropic.com/claude),
with the current version, Claude 4, released in of 22 May 2024[^CLAUDE]. 

There are three [Claude 4 models](https://docs.anthropic.com/en/docs/about-claude/models/):

- **Claude 4.1 Opus**: the largest and most capable model, with a context window of 200k characters
  and text and image inputs with 32k output tokens. [^4.1OPUS]
- **Claude 4 Opus**: Anthropic's previous flagship model, that takes both text and image with a 
  200k characters input limit and 32k output tokens. 
- **Claude 4 Sonnet**: High-performance model optimized for reasoning capabilities with text and
  image inputs with a 1 million context window in beta. 


Claude 3 is a competitor with ChatGPT 4 and on some benchmarks, performs as well 
or better than ChatGPT. 


#### X's Grok
[Grok][GROK] is a LLM from X (formally Twitter) with a [public chat interface](https://grok.com/) 
as well as [API](https://console.x.ai/home) (requires an account) that can be used by applications. 
Grok is integrated with the X social network and provides realtime search based on trends and traffic
in the X ecosystem. 

[ANTH]: https://www.anthropic.com/
[CHATGPT]: https://chatgpt.com/
[COPILOT]: https://copilot.microsoft.com/
[DALLE3]: https://openai.com/index/dall-e-3/
[GEMINI]: https://gemini.google.com/
[GOOG]: https://www.google.com/
[GROK]: https://x.ai/grok
[OPENAI]: https://openai.com/

[^2.5PRO]: [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models#gemini-2.5-pro)
[^2.5FLASH]: [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models#gemini-2.5-flash)
[^2.5FLASHLITE]: [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models#gemini-2.5-flash-lite)
[^4.1OPUS]: [Claude Opus 4.1](https://www.anthropic.com/news/claude-opus-4-1)

[^CLAUDE]: [Introducing Claude 4](https://www.anthropic.com/news/claude-4)
