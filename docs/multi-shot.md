### Including Examples or Multi-shot Prompting 
In this technique, you provide a few (1-5) examples of what you would like to see in the LLMs 
output as part of your prompt. Multi-shot prompting 
particularly helpful when you require the output to include structured data like FOLIO JSON 
documents. 

**Example**: You are an expert cataloger, please return any records as FOLIO JSON, here is an
example:

```
Q: Parable of the Sower by Octiva Butler, published in 1993 by Four Walls Eight Windows in New York 

A: {"title": "Parable of the Sower", "source": "ChatGPT", 
    "contributors": [{"name": "Octiva Butler", "contributorTypeText": "Author"}], 
    "publication": [{"publisher": "Four Walls Eight Windows", "dateOfPublication": "1993", "place": "New York"}] }}
```
