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

(Add new decisions below)
