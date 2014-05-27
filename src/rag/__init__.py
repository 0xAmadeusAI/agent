"""
TODO: implement RAG
We gonna tokenize tweets and store them in PGVector
That way Agent is gonna be able to remember previous tweets. Even the super old ones (1 year +)


# RAG System Specification: Tweet Storage and Retrieval

### Core Technologies
- Python 3.10+
- PostgreSQL 15+ with pgvector extension
- SQLAlchemy 2.0+ for database ORM
- Sentence Transformers for embedding generation
- LangChain for RAG pipeline orchestration
- FastAPI for API endpoints (optional)

### Key Dependencies
```
langchain
psycopg2-binary
sqlalchemy
pgvector
sentence-transformers
python-dotenv
pydantic
```

## 3. Database Schema

### Tweets Table
```sql
CREATE TABLE tweets (
    id SERIAL PRIMARY KEY,
    tweet_id VARCHAR(100) UNIQUE NOT NULL,
    content TEXT NOT NULL,
    author VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE,
    embedding vector(384),  -- Dimension depends on chosen embedding model
    metadata JSONB,
    created_at_ts TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at_ts TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create index for vector similarity search
CREATE INDEX tweet_embedding_idx ON tweets
USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);
```

### Metadata Schema (JSONB)
```json
{
    "language": "string",
    "hashtags": ["string"],
    "mentions": ["string"],
    "retweet_count": int,
    "like_count": int,
    "reply_count": int,
    "is_retweet": boolean,
    "source": "string"
}
```

## 4. System Components

### 4.1 Embedding Generator
- Utilize `sentence-transformers` library
- Default model: 'all-MiniLM-L6-v2' (384 dimensions)
- Batch processing capability for efficient embedding generation
- Caching mechanism for frequently accessed embeddings

### 4.2 Database Manager
- SQLAlchemy models and async session management
- CRUD operations for tweets
- Vector similarity search implementations
- Connection pooling and retry mechanisms
- Batch insert/update operations

### 4.3 RAG Pipeline
- Document chunking strategy (single tweets as chunks)
- Retrieval methods:
  - Cosine similarity search
  - Hybrid search (combining semantic and keyword search)
  - Metadata filtering
- Result reranking based on relevance scores
- Context window management for LLM input

### 4.4 API Layer (Optional)
- FastAPI endpoints for:
  - Tweet ingestion
  - Similarity search
  - Query processing
  - Health checks
- Authentication and rate limiting
- Swagger documentation

## 5. Key Features

### 5.1 Data Ingestion
- Batch tweet processing
- Automatic embedding generation
- Duplicate detection and handling
- Error handling and retry mechanisms
- Validation of tweet content and metadata

### 5.2 Search and Retrieval
- Vector similarity search with configurable k-nearest neighbors
- Metadata-based filtering
- Hybrid search combining semantic and keyword matching
- Customizable relevance scoring
- Query preprocessing and optimization

### 5.3 Performance Optimization
- Connection pooling
- Batch processing
- Caching layer for embeddings
- Index optimization
- Query performance monitoring

## 6. Configuration

### Environment Variables
```
DATABASE_URL=postgresql+psycopg2://user:password@localhost:5432/dbname
EMBEDDING_MODEL=all-MiniLM-L6-v2
BATCH_SIZE=100
CACHE_SIZE=1000
MAX_CONNECTIONS=20
```

### Configuration Parameters
```python
config = {
    "embedding": {
        "model_name": "all-MiniLM-L6-v2",
        "dimension": 384,
        "batch_size": 100
    },
    "database": {
        "pool_size": 20,
        "max_overflow": 10,
        "pool_timeout": 30
    },
    "search": {
        "default_k": 10,
        "score_threshold": 0.7,
        "reranking_threshold": 0.8
    }
}
```
"""