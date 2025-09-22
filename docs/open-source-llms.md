### Meta's Llama
In February 2023, [Meta AI][METAAI] (the AI research division of the Meta that also includes Facebook) released 
an open-source Large Language Model (LLM) called LLaMA with a follow-up release in 
April 2024. Unlike other commercial LLMs, Meta AI released the weights along with supporting
code to allow for training and other uses not possible with similar models released by OpenAI,
Anthropic, and Google.

#### Using Llama
The easiest way to use Llama is go to [https://www.meta.ai](https://www.meta.ai) and start entering chat prompts. This 
multi-modal web application allows users to generate images and text (although to use the image
generator function requires logging in with a Facebook account). 

#### Using Llama Locally
Because of its release as open-source, you are able to download the LLaMA model to run and 
train locally on your computer or on cloud providers. While there 
are a number of ways for running LLaMA locally, a convenient method for running this
and other open-source models is using a project called [gpt4all][GPT4ALL]. [gpt4all][GPT4ALL]
uses [LLaMA.cpp][LLAMA.CCP] to internally run the models.

While the computing
requirements can vary depending on your laptop's hardware and OS, there are desktop versions
for [Macintosh](https://gpt4all.io/installers/gpt4all-installer-darwin.dmg), 
[Windows](https://gpt4all.io/installers/gpt4all-installer-win64.exe), and 
[Ubuntu](https://gpt4all.io/installers/gpt4all-installer-linux.run).

### Deepseek 
In January 2025, a Chinese company [Deepseek][DEEPSEEK] released an open-source LLM that 
equaled or surpassed the state-of-art models by OpenAPI, Antrophic, and Google. 


### OpenAI Open Source Models
On August 5, 2025 OpenAI released two of their models, [gpt-oss-120b]() and [gpt-oss-20b]()

### Alibaba Qwen3
[Alibaba](https://www.alibaba.com/) has released a family of [Qwen3](https://github.com/QwenLM/Qwen3) 
open-source models.


### Using Llama.cpp
The [LLaMA.cpp][LLAMA.CCP] project allows you to run fine-tuned
LLaMA models on your local computer. [LLaMA.cpp][LLAMA.CCP] provides an
OpenAI API compatible server that also allows us to integrate with [DSPy](dspy-docs.vercel.app/)
and [edge-ai][EDGE_AI] module.

[LLaMA.cpp][LLAMA.CCP] can also be run with Docker[^DOCKER] on your computer if you 
don't want or can't compile the C++ source code to run on your computer.

### Downloading a LLaMA-based Model
[LLaMA.cpp][LLAMA.CCP] uses the [GGUF](https://github.com/ggerganov/ggml/blob/master/docs/gguf.md) 
format for model inference and training. Look for GGUF models on [HuggingFace][HUGFACE]. 

[^DOCKER]: [LLaMA.cpp Docker instructions](https://github.com/ggerganov/llama.cpp/blob/master/docs/docker.md)
[DEEPSEEK]: https://www.deepseek.com/en
[EDGE_AI]: https://github.com/folio-labs/edge-ai
[LLAMA.CCP]: https://github.com/ggerganov/llama.cpp
[HUGFACE]: https://huggingface.co/models
[GPT4ALL]: https://gpt4all.io/
[METAAI]: https://ai.meta.com/ 
