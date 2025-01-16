# Biography-Based Smart Assistant Project: Simple Overview

Imagine you have a book about someone's life (a biography), and you want to create a smart assistant that can answer questions about it - like having a knowledgeable friend who has perfectly memorized this book!

## What We're Building (In Simple Terms)

We're creating two friendly "digital librarians":
1. An English-speaking librarian who knows an English biography by heart
2. A Greek-speaking librarian who knows the same biography in Greek

## How It Works (Simplified)
Think of it like this:
- We're teaching our digital librarian to read and understand the biography
- We organize all the information like a super-smart index card system
- When you ask a question, the librarian quickly finds the right "card" and gives you the answer
- If you ask about something that's not in the biography, the librarian politely says "I'm sorry, I only know about what's in this specific book"

## What Makes This Special?
1. **Super Focused**: Unlike general AI chatbots that try to know everything, our assistant only talks about the biography - making it very accurate for this specific topic
2. **Bilingual Brain**: It can work in both English and Greek, making the same information accessible to different audiences
3. **Honest Helper**: It won't make up information - if something isn't in the biography, it will tell you so

## Real-World Example
Imagine you're reading a biography about Marie Curie:
- You: "What did Marie Curie discover?"
- Assistant: *Quickly finds and tells you about her radioactivity research from the biography*
- You: "What's her favorite movie?"
- Assistant: "I'm sorry, I can only answer questions that are covered in the biography I've been given"

## Benefits
- Get instant, accurate answers about the biography
- No need to flip through pages
- Always get factual information, no made-up details
- Access the same information in two languages

It's like having a very knowledgeable assistant who has perfectly memorized one book and can discuss it in detail - but knows its limitations and won't pretend to know things outside of that book!​​​​​​​​​​​​​​​​


# Biography-Based AI Chatbot Development Project

## Project Overview
Create two specialized chatbots that can answer questions based solely on a provided biography - one for English and one for Greek text. The chatbots will demonstrate controlled context awareness through vector database integration.

## Business Objectives
1. Demonstrate precise biographical information retrieval
2. Showcase multilingual AI capabilities
3. Establish strict context boundaries
4. Validate vector embedding effectiveness across languages

## Technical Requirements

### Phase 1: English Biography Chatbot
#### Components
* Input: English biography (.txt format)
* Vector Database: Chroma
* LLM: Llama-2 (via Ollama)
* Framework: LangChain

#### Key Development Areas
1. **Text Processing Pipeline**
   - Implement efficient text chunking strategy
   - Consider overlap between chunks
   - Focus on maintaining context coherence

2. **Vector Database Setup**
   - Design schema for biographical data
   - Implement efficient similarity search
   - Consider metadata structuring

3. **Response Generation**
   - Implement strict context boundary checking
   - Develop clear "out of context" responses
   - Ensure response accuracy against source material

### Phase 2: Greek Biography Chatbot
#### Components
* Input: Greek biography (same content, translated)
* Vector Database: Chroma
* LLM: Meltemi (via Ollama)
* Embedding Model: BERT (Greek-specific from HuggingFace)
* Framework: LangChain

#### Key Development Areas
1. **Greek Text Processing**
   - Implement Greek-specific tokenization
   - Handle Greek character encoding properly
   - Maintain semantic coherence in chunks

2. **Custom Embedding Pipeline**
   - Configure BERT model for Greek text
   - Optimize embedding dimensions
   - Validate embedding quality

## Development Guidelines

### Data Processing Tips
* Experiment with different chunk sizes (recommended range: 256-1024 tokens)
* Consider sentence/paragraph boundaries during chunking
* Test various overlap percentages between chunks

### Vector Database Optimization
* Implement efficient indexing strategies
* Consider dimensionality reduction techniques
* Test different similarity metrics

### Response Quality Control
* Implement similarity score thresholds
* Develop comprehensive test cases
* Create evaluation metrics for response accuracy

## Testing Strategy

### Functional Testing
1. **Context Boundary Testing**
   - Test with in-context questions
   - Test with out-of-context questions
   - Validate response consistency

2. **Language-Specific Testing**
   - Verify proper Greek character handling
   - Test response coherence in both languages
   - Validate translation consistency

### Performance Testing
* Measure response latency
* Evaluate embedding quality
* Test system under various load conditions

## Success Metrics
1. Response accuracy (>95% match with source material)
2. Context boundary adherence (100%)
3. Response time (<3 seconds)
4. Greek text handling accuracy (>98%)

## Project Phases

### Phase 1
1. English biography processing setup
2. Vector database implementation
3. Llama-2 integration
4. Testing and optimization

### Phase 2
1. Greek BERT model integration
2. Greek text processing pipeline
3. Meltemi LLM integration
4. Cross-language testing

## Technical Considerations

### Key Focus Areas
* Proper chunk size determination
* Embedding quality validation
* Context window optimization
* Efficient vector similarity search
* Response filtering and validation

## Dependencies
```markdown
- Python 3.8+
- LangChain
- Chroma
- Ollama (Llama-2 & Meltemi)
- HuggingFace Transformers
- PyTorch
```

## Deliverables
1. Working English biography chatbot
2. Working Greek biography chatbot
3. Testing documentation
4. Performance metrics report
5. System architecture documentation