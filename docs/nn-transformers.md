### Basics of Neural Networks
An artificial neural network is a fundamental computing technique and structure 
in artificial intelligence and machine learning. Large Language Models (LLMs)
are a very successful type of neural network but neural networks as a general
tool are used in other domains and to solve different problems such as machine 
vision, natural language processing, self-driving automobiles and more.[^NN_BEG]

#### Structure of a Neural Network
![Basic Neural Network](imgs/neural_network.png)[^WIKIPEDIA]

The basic unit of a neural network is a neuron that takes numerical inputs, 
performs mathematical operations on those inputs, and produces a numerical output. 

Multiple neurons are combined and structured into layers:
 
- **Input layer** (red circles in the graphic above)
- **One or more hidden layers** (blue circles) that process information from the input layer
- **Output layer** (green circles). 

#### Loss Function
Before training a neural network, a **loss** function is used as a way to quantify 
how well the network is performing. This allows the network to learn and improve. The 
Mean Squared Error is a common loss function for regression problems and simple
networks. When training a network, we are trying to minimize the loss function thereby
improving the predictive power of the network.[^HOU]


#### Learning Approaches
Neural networks can be trained using supervised learning or unsupervised learning:

-  **Supervised learning**: The neural network  has access to both the inputs and expected outputs. 
   It generates a loss function based on this training data to improve its predications.
-  **Unsupervised learning**: The neural network does not have the expected outputs. Instead,
   it create patterns and relationships in the input data without having a reference to outputs
   for calculating a loss function.


### Transformers
Large Language Models (LLMs) are based on a type of neural network called a Transformer.
First specified in a 2017[^ATTENTION] paper by then Google engineers, Transformers are the core
technology behind modern Generative AI models including LLMs. A transformer
neural net architecture improves on a basic task of predicting the next-word in a sentence or 
passage of text by adding a core mechanism called *self-attention* that allows the transformers a
greater ability to place incoming characters within a larger context of the entire text.  

In a simplified transformer model, text is fed into a stack of encoders, where each encoder 
consists of two sub-layers with different weights that process the text as it passes through 
the stack. From there, the text is then sent to a decoder stack, which assembles the predicated 
output text.

#### Transformer Demonstration
An online explanation of the Transformer architecture is available at 
[https://poloclub.github.io/transformer-explainer/][EXPLANIER], which uses a live GPT-2 model 
to demonstrate how transformers work with an accompanying article[^EXPLAIN_PAPER].

#### Simplified Overview

##### Text Embedding
Incoming text to the Transformer is parsed into smaller tokens, which can be a word or portions of
words. A numerical representation of these tokens, called **embeddings**, are generated that provide
a semantic relationship with other document **embeddings**.  

#### Transformer Block

##### Attention 
A transformer with multiple, identical encoders with each is made up of the 
following layers:

- **Self-Attention Layer** - helps the encoder consider the context of each word within the
  input sentence. As the model processes each word self attention allows it to look at
  others positions in the input sequence for clues for improving the encoding of the word.
- **Feed Forward Neural Network** - outputs from the self-attention layer are fed to 
  and independently applied to this layer.

##### Multi-Layer Decoders
After the text prompt has been fed through the encoders, the outputs from each of the
encoders are feed to the decoders. A decoder is made of three layers:

- **Self-Attention Layer** - same as the encoder, allows the word in context with the other
  words in the input sentence. 
- **Encoder-Decoder Attention** - a separate layer that assists the decoder in focusing on 
  the relevant parts in the input sentence.
- **Feed Forward Neural Network** - refines token representation

#### Output Probabilities
Final layers take the processed embeddings and transform them into probabilities for the next
tokens.  


[^NN_BEG]: [What is a neural network?](https://www.geeksforgeeks.org/neural-networks-a-beginners-guide/)
[^WIKIPEDIA]: [Neural Network (machine learning)](https://en.wikipedia.org/wiki/Neural_network_(machine_learning))
[^HOU]: [Machine Learning for Beginners: An Introduction to Neural Networks](https://victorzhou.com/blog/intro-to-neural-networks/)
[EXPLANIER]: https://poloclub.github.io/transformer-explainer/
[^ATTENTION]: [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
[^EXPLAIN_PAPER]: [Transformer Explainer: Interactive Learning of Text-Generative Models](https://arxiv.org/abs/2408.04619)
