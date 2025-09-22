### Inventory Agent
The most developed AI Agent in the [Edge-AI Module][EDGE_AI], the 
[Instance Agent](https://github.com/folio-labs/edge-ai/blob/main/src/edge_ai/inventory/agents/instance.py) 
uses multi-shot prompt techniques to create an Inventory Instance record from either a text prompt
by a user or an uploaded cover image. The AI Agent has tooling for retrieving reference data needed to  
generate a valid Instance record that is POSTed to an existing [Inventory API](https://s3.amazonaws.com/foliodocs/api/mod-inventory-storage/p/instance-storage.html#instance_storage_instances_post) 
endpoint.

#### Jupyter Notebook
- See the [InventoryInstanceAgent.ipynb](http://localhost:8888/notebooks/InventoryInstanceAgent.ipynb) notebook

[EDGE_AI]: https://github.com/folio-labs/edge-ai

