### Privacy Concerns in Large Language Models
With the widespread release of Large Language Models (LLMs) by various  organizations,
significant privacy issues[^PRIVACY_LLM] have emerged, including:

- **Personal details in training data**: Names, addresses, and financial information may
  be included in the training data for these models. 
- **Logged prompts containing sensitive information**: User inputs, including private 
  details, can be logged by the companies managing these LLMs. 
- **Re-identification of individuals:** Even in anonymized training data, individuals can potentially be
  re-identified through the model outputs and usage patterns.


#### Training Data 
The privacy of individuals can be compromised if their personal 
information is included in the large datasets used to train LLMs. Since people have often not 
consented to this data usage, and even anonymization techniques are vulnerable to prompt 
engineering attacks, there is a significant risk that raw training data, containing sensitive 
details, can be exposed by models as OpenAI's ChatGPT[^SCALEABLE].  

#### Inference Data Privacy: Revealing Too Much in Prompts
As people engage with LLMs on personal topics such relationship counseling, medical advice, 
and psychological concerns, the privacy risks associated with disclosing sensitive information
increase.[^GEN_AI_PRIVACY].

These prompts are often collected and logged by organizations like OpenAI or Google, creating 
privacy concerns if the inclusion of sensitive details becomes part of the future training data for 
these models.

#### Re-identification
Even when personal information in LLMs is anonymized, it can be vulnerable to re-identification. By 
analyzing LLMs responses, individuals could potential be identified thereby comprising their privacy
when interacting with theses AI systems.

#### Privacy with AI Agents
AI Agents using generative AI pose additional privacy concerns, especially when used with other 
systems.[^PRIVACY_PARADOX] Techniques such as sensitive information filtering, homomorphic encryption of users 
private data, session isolation, and response filtering.[^PROTECT_DATA_PRIVACY]  

[^PRIVACY_LLM]: [Privacy in Large Language Models: Attacks, Defenses and Future Directions](https://arxiv.org/abs/2310.10383)
[^SCALEABLE]: [Scalable Extraction of Training Data from (Production) Language Models](https://arxiv.org/abs/2311.17035)
[^GEN_AI_PRIVACY]: [Generative AI's privacy problem](https://www.axios.com/2024/03/14/generative-ai-privacy-problem-chatgpt-openai)
[^PROTECT_DATA_PRIVACY]: [On protecting the data privacy of Large Language Models (LLMs) and LLM agents: A literature review](https://doi.org/10.1016/j.hcc.2025.100300)
[^PRIVACY_PARADOX]: [SoK: The Privacy Paradox of Large Language Models: Advancements, Privacy Risks, and Mitigation](https://dl.acm.org/doi/10.1145/3708821.3733888)
