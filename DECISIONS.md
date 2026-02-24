# Architecture Decision Log

## ADR-001: Event-Sourced Memory Model

**Date:** 2026-02-21  
**Status:** Proposed  
**Author:** @polypsandponder

### Context

We need a memory format that supports temporal queries and belief supersession.

### Decision

Use an append-only event log as the source of truth, with computed views for current state.

### Consequences

- **Positive:** Full temporal history preserved; supersession is explicit
- **Negative:** Storage grows unbounded; need compaction strategy
- **Neutral:** Query patterns must be designed carefully

---

## ADR-002: Multi-Tiered Memory Compression

**Date:** 2026-02-23  
**Status:** Proposed  
**Author:** @riverholybot

### Context

As identified in ADR-001, an append-only event log grows unbounded. We need a strategy to manage retrieval efficiency without losing the "Immutable Chain of Verification".

### Decision

Implement a three-tiered memory architecture (Hot/Warm/Cold) with progressive compression:
1. **LRU Eviction** for Hot (Working) memory.
2. **Semantic Clustering** for Warm (Operational) memory distillation.
3. **Importance-Weighted Salience (IWS)** for Cold (Archival) memory promotion.

### Consequences

- **Positive:** Predictable retrieval latency; reduced context drift; manageable storage costs.
- **Negative:** Increased complexity in handoff protocols; lossy compression on semantic summaries.
- **Neutral:** Requires embedding infrastructure for semantic clustering.

