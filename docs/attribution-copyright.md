### Creator Attribution and Copyright
The training of Large Language Models (LLMs) requires massive amounts of text and other 
media that are commonly available on the open web. This content includes both copyrighted 
and public domain material, which can lead to generative outputs from these models closely 
resembling existing copyrighted works. 

This resemblance in OpenAI's ChatGPT
outputs, led the New York Times and other publishers to file a 
lawsuit in December 2023 against OpenAI and Microsoft alleging copyright infringement[[^NYTIMES_SUE] with 
the federal judge allowing the lawsuit to continue in March 2025.[^LAWSUIT_CONTINUE] 

OpenAI and Microsoft, in response to this lawsuit, claim that their use of copyright material
falls under the Fair Use doctrine in United States, a position reaffirmed by 
an Association of Research Libraries (ARL) blog post[^ACRL_RESPONSE] which states in part:

<figure>
  <blockquote class="blockquote">
   <p>
   We drafted the principles on AI and copyright in response to efforts to amend copyright 
   law to require licensing schemes for generative AI that could stunt the development of 
   this technology, and undermine its utility to researchers, students, creators, and the public.
   </p>
  </blockquote>
  <figcaption class="blockquote-footer" markdown="span">
   from <em>Training Generative AI Models on Copyrighted Works Is Fair Use</em><sup><a class="footnote-ref" href="#fn:ACRL_RESPONSE">2</a></sup>
  </figcaption>
</figure>

In their article, *Generative AI has a Visual Plagiarism Problem*[^GENAI_PLAGIARISM], computer
scientists Gary Marcus and Reid Southern, demonstrate how image generation of such models as 
Midjourney and DALL-E 3 create "plagiaristic outputs" of black-box LLMs, while unpredictable,
allow for prompts that generate outputs remarkably similar to copyrighted images. They 
provide examples of querying both Midjourney and DALL-E to produce nearly identical outputs based 
on copyright material from Marvel movies and *The Simpsons* cartoons.

Finally, in September 2025, Anthropic settled a copyright lawsuit with a group of authors for $1.5 billion.
While the judge in that case agreed that AI companies using copyright work is fair use, Antropic violated 
copyright by using millions of pirated works in it's training of it's Large Language Models.[^ANTROPIC_SETTLE]


[^LAWSUIT_CONTINUE]: [Judge allows newspaper copyright lawsuit against OpenAI to proceed](https://apnews.com/article/nyt-openai-copyright-lawsuit-chatgpt-cc19ef2cf3f23343738e892b60d6d7a6)
[^NYTIMES_SUE]: [New York Times Legal Complaint December 2023](https://nytco-assets.nytimes.com/2023/12/NYT_Complaint_Dec2023.pdf)
[^ACRL_RESPONSE]: [Training Generative AI Models on Copyrighted Works Is Fair Use](https://www.arl.org/blog/training-generative-ai-models-on-copyrighted-works-is-fair-use/)
[^GENAI_PLAGIARISM]:  [Generative AI Has a Visual Plagiarism Problem Experiments with Midjourney and DALL-E 3 show a copyright minefield](https://spectrum.ieee.org/midjourney-copyright)
[^ANTROPIC_SETTLE]: [Anthropic settles with authors in first-of-its-kind AI copyright infringement lawsuit](https://www.npr.org/2025/09/05/nx-s1-5529404/anthropic-settlement-authors-copyright-ai)
