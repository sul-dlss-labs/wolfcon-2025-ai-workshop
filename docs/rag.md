### Retrieval Augmented Generation (RAG)
Retrieval Augmented Generation (RAG) is a Natural Language Processing (NLP) 
technique to enhance and localize the use of generative based Large Language 
Models (LLMs) by including specific external content in the LLM's context window. 

RAG is often employed to improve the accuracy and reliability of LLMs by 
better contextualizing the generative abilities of these models.

#### Key features of RAG:
- First proposed in a 2020 paper[^RAG_NLP]
- Provides a means to ground LLM output
- Allows LLMs to act as a narrative interface for document corpora or data repositories
- Enables LLMs to cite specific documents or data, reducing the chance of incorrect answers

### Embeddings and Vector Databases
While the RAG technique doesn't require the use of embeddings or vector databases,
adding an information retrieval component to your RAG system can improve overall
performance of compound AI systems. To create a vector database, first the documents
or data is converted into a mathematical representation as a text embedding,
or set of numeric vectors, that are used for matching and creating relationships.

These text embeddings are then stored in a database or datastore and then can be queried
by first converting a query into a text embedding and then finding the stored embeddings
that most closely match the query. The resulting embeddings are then converted back to
textual documents and then sent as a part of the context window to the LLM.

### Application to FOLIO
Creating a vector database of FOLIO JSON documents offers a number of advantages to 
AI workflows; both in the generative aspects of creating new documents
like invoices or inventory records from text or automatic prompts, and
minimize errors in the LLMs output.

#### FOLIO Organization RAG
- See the [OrgsVectorDB.ipynb](http://localhost:8888/notebooks/OrgsVectorDB.ipynb) notebook

[^RAG_NLP]: [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) 
