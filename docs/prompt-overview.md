### Prompt Engineering

<figure>
  <blockquote class="blockquote">
   The technique of prompt engineering, which entails the crafting of precise, 
   task-specific instructions in natural language, either manually or through 
   automated means, and the careful selection of representative examples for 
   inclusion in the prompt, has become a central area of investigation for LLMs.
  </blockquote>
  <figcaption class="blockquote-footer">
   Principled Instructions Are All You Need for Questioning LLaMA-1/2, GPT-3.5/4
   <sup id="fnref:PRINCIPLED"><a class="footnote-ref" href="#fn:PRINCIPLED">1</a></sup>
  </figcaption>
</figure>


To effectively use Large Language Models (LLMs) and generative AI, you will need to construct a short textual 
description, called a prompt, that the LLM will use to generate text, images, or 
other media. Usually, you will need to iterate and change your prompt to improve the LLMs
outputs a few times until you have a result that meets your needs. 

How you construct your prompt will also impact aspects of the model's output, like 
accuracy, verbosity, or style customization. The set of techniques and approaches for 
constructing prompts is collectively called prompt engineering. 

In Anthropic's Prompt Engineering Guide, they suggest that before you begin applying 
specific prompt engineering techniques, you have a clear definition of success criteria
for your use case, ways to empirically test those criteria, and a first draft of your 
prompt.[^ANTHROPIC]

[^ANTHROPIC]: [Antropic Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/)
