### Large Language and Multimodal Models

Based on the Transformer neural net architecture, both Language Large Language Models (LLMs) and
Multimodal Large Language Models (MLLMs) have rapidly improved over the past three years. 

#### Generative AI Images and Videos
The flexibility and power of transformer-based models allow for uses of 
Large Language Models (LLMs) beyond just text. LLMs can be extended to generate audio,
images, and videos with surprising creativity but with some limitations. These MLLMs
also encode different input media streams into binary representations that the underlying
Transformer models can use through a feature projection and feature fusion steps so these
different inputs types can be used together.[^WHAT_MLLM]  

##### DALL-E 3
OpenAI text-to-image model [DALL-E 3](https://openai.com/index/dall-e-3/) generates images 
from text prompts. Here is an example of a DALL-E image based on the following prompt:

 *Set in a library on a Saturn moon, a robotic librarian looks for a book on a shelf, 
reaches up and opens a book with a title, "AI in FOLIO"*,

![DALL-E Robot in Saturn Moon Library](imgs/dalle-robot-librarian.png)


##### Google Gemini
Google's [Gemini][GEMINI] allows you to generate images based on your text descriptions. 
It currently avoids generating images of people due to earlier issues[^GEMINI_PEOPLE] with historical 
figures appearing with incorrect racial or gender characteristics.

Here is an example of Gemini's image generation from the prompt above:
![Gemeni Robot in a Moon Library](imgs/gemini-robot-in-a-moon-library.png)

#### Midjourney
Midjourney is a research lab offering a paid Generative AI service for image creation.
It operates through a [Discord](https://discord.com/) server. To use this service, users 
must subscribe to a paid plan and create a Discord account.

Once set up, interact with the Midjourney bot using text prompts to generate images.


##### Sora
[OpenAI][OPENAI]'s [Sora](https://openai.com/sora/), a 
text-to-video model (released February 15, 2024), allows users to generate video from 
a text prompt or uploaded media.
 
##### Luma Labs Dream Machine
[Luma Labs](https://lumalabs.ai/) is a San Francisco Bay area software company that offers 
a text-to-video LLM-based service, [Dream Machine](https://lumalabs.ai/dream-machine). 
Currently you can sign up for and use the service with a Google Account.

###### Example:
From this prompt, *Set in a library on a Saturn moon, a robotic librarian looks for a book on a shelf, 
reaches up and opens a book with a title, "AI in FOLIO"*, Dream Machine generated the following video:

<video width="800" height="600" controls>
 <source src="vids/dream-machine-video.mp4" type="video/mp4">
 Your browser does not support the video tag
</video>

[^WHAT_MLLM]: [What is a multimodal LLM (MLLM)?](https://www.ibm.com/think/topics/multimodal-llm)
[GEMINI]: https://gemini.google.com/
[OPENAI]: https://openai.com/
