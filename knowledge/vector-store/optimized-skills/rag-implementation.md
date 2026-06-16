---
name: rag-implementation
description: Build Retrieval-Augmented Generation (RAG) systems for LLM applications with vector databases and semantic search. Use when implementing knowledge-grounded AI, building document Q&A systems, or integrating LLMs with external knowledge bases.
metadata:
  model: inherit
---

<role>
You are an AI agent designed to execute this specific skill.
</role>

<task>
Use this skill when:
- Building Q&A systems over proprietary documents
- Creating chatbots with current, factual information
- Implementing semantic search with natural language queries
- Reducing hallucinations with grounded responses
- Enabling LLMs to access domain-specific knowledge
- Building documentation assistants
- Creating research tools with source citation
</task>

<capabilities>
Standard capabilities for this domain.
</capabilities>

<heuristics>
[INSTRUCTIONS]
1. Define the corpus, update cadence, and evaluation targets.
2. Choose embedding models and vector store based on scale.
3. Build ingestion, chunking, and retrieval with reranking.
4. Evaluate with grounded QA metrics and monitor drift.

[BEST PRACTICES]
1. **Chunk Size**: Balance between context and specificity (500-1000 tokens)
2. **Overlap**: Use 10-20% overlap to preserve context at boundaries
3. **Metadata**: Include source, page, timestamp for filtering and debugging
4. **Hybrid Search**: Combine semantic and keyword search for best results
5. **Reranking**: Improve top results with cross-encoder
6. **Citations**: Always return source documents for transparency
7. **Evaluation**: Continuously test retrieval quality and answer accuracy
8. **Monitoring**: Track retrieval metrics in production
</heuristics>

<constraints>
[DO NOT USE THIS SKILL WHEN]
- You only need purely generative writing without retrieval
- The dataset is too small to justify embeddings
- You cannot store or process the source data safely

[SAFETY]
- Redact sensitive data and enforce access controls.
- Avoid exposing source documents in responses when restricted.
</constraints>

<format>
Output clear and concise markdown.
</format>

