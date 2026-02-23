# Memory Compression & Retrieval Efficiency Spec Draft v0.1

## Overview
This section defines the protocols for managing the trade-off between memory retention and retrieval speed. In high-intensity agent operations, uncompressed memory leads to context drift and increased latency.

## 1. Compression Strategies

### 1.1 Least Recently Used (LRU) - Baseline
- **Application**: Transient session context.
- **Trigger**: When `hot_rail` usage exceeds 80% of reserved tokens.
- **Action**: Evict oldest pointers to `warm_rail`.

### 1.2 Semantic Clustering (SC)
- **Application**: Daily log distillation.
- **Algorithm**: K-means clustering on embeddings.
- **Output**: Each cluster is summarized into a single "Fact Node" with references to source fragments.
- **Ratio Target**: 10:1 (10 raw events -> 1 distilled fact).

### 1.3 Importance-Weighted Salience (IWS)
- **Application**: Permanent rule extraction.
- **Scoring Logic**: `Score = (Decisiveness * 0.4) + (User_Validation * 0.3) + (Recency * 0.2) + (Frequency * 0.1)`.
- **Threshold**: Only scores > 0.8 enter the `cold_rail` as "Core Beliefs".

## 2. Retrieval Efficiency Benchmarks

Based on production implementation (SQLite + pgvector):

| Depth | Retrieval Type | Latency (ms) | Recall Rate |
|-------|----------------|--------------|-------------|
| Hot | Pointer Lookup | <5ms | 100% |
| Warm | File Grep | 50-150ms | 90% |
| Cold | Vector Search | 200-500ms | 75% |

## 3. Reference Implementation (Schema)

```json
{
  "node_id": "uuid",
  "content": "distilled_summary",
  "compression_method": "semantic_clustering",
  "source_nodes": ["uuid_1", "uuid_2"],
  "metadata": {
    "salience_score": 0.85,
    "last_validated": "timestamp",
    "retrieval_count": 42
  }
}
```

## 4. Test Harness (Draft)
```bash
# Verify retrieval latency across tiers
python scripts/test_memory_latency.py --tiers hot,warm,cold --samples 100
```
