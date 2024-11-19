# Inspection Methods
RAG is a technique for augmenting LLM knowledge with additional data.
LLMs can reason about wide-ranging topics, but their knowledge is limited to the public data up to a specific point in time that they were trained on.
If you want to build AI applications that can reason about private data or data introduced after a model's cutoff date, you need to augment the knowledge of the model with the specific information it needs.
The process of bringing the appropriate information and inserting it into the model prompt is known as retrieval augmented generation (RAG).
This repo uses llama-index with NVIDIA NIM
