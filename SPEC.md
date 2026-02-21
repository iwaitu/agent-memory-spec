# Agent Memory Specification v0.1 (DRAFT)

## Status

This specification is in early development. Everything is subject to change.

## Overview

This spec defines a portable, interoperable memory format for AI agents. The goal is to enable:

1. Agents to persist and retrieve memories across sessions
2. Temporal coherence (knowing what changed since last interaction)
3. Belief supersession (versioning knowledge, not just appending)
4. Cross-platform compatibility

## Core Concepts

### Memory Event

A memory event is the atomic unit of memory. It represents something the agent learned, decided, or experienced.

```json
{
  "id": "uuid",
  "type": "belief | decision | observation | correction",
  "timestamp": "ISO-8601",
  "content": "string",
  "supersedes": "uuid | null",
  "confidence": 0.0-1.0,
  "tags": ["string"],
  "source": "string"
}
```

### Supersession

When an agent learns something that contradicts a previous belief, it creates a new event that explicitly supersedes the old one. The old belief is not deleted — it's marked as superseded.

```json
{
  "id": "event-456",
  "type": "correction",
  "content": "User prefers light mode, not dark mode",
  "supersedes": "event-123",
  "timestamp": "2026-02-21T06:00:00Z"
}
```

### Confidence Decay

Beliefs that haven't been reconfirmed decay in confidence over time. This models the natural uncertainty of stale information.

```
confidence_t = confidence_0 * decay_rate ^ (days_since_creation)
```

Default decay rate: 0.95 per day (50% confidence after ~14 days without reconfirmation)

## File Format

### Daily Logs

Raw temporal records in `memory/YYYY-MM-DD.md`:

```markdown
# 2026-02-21

## 09:15 - Observation
User mentioned they're starting a new project called "Atlas"

## 14:30 - Decision  
Agreed to check in weekly on Atlas progress

## 16:00 - Correction
User prefers weekly updates on Monday, not Friday
Supersedes: belief about Friday updates from 2026-02-14
```

### Curated Memory

Long-term memory in `MEMORY.md`:

```markdown
# Long-Term Memory

## User Preferences
- Prefers light mode (updated 2026-02-21, was: dark mode)
- Weekly check-ins on Monday

## Active Projects
- Atlas: Started 2026-02-21, weekly updates

## Lessons Learned
- Always verify day-of-week with calendar before stating it
```

## Retrieval

### Semantic Search

Implementations SHOULD support semantic search over memory content, returning results ranked by:

1. Semantic similarity to query
2. Recency (more recent = higher rank)
3. Confidence (higher confidence = higher rank)

### Temporal Queries

Implementations SHOULD support queries like:

- "What changed since [timestamp]?"
- "What was believed about [topic] as of [timestamp]?"
- "What superseded [event-id]?"

## Open Questions

- [ ] How to handle conflicting beliefs from multiple sources?
- [ ] Standard format for cross-agent memory sharing?
- [ ] Privacy controls for sensitive memories?
- [ ] Compression strategies for long-running agents?

## Contributors

- @polypsandponder (initiator)
- (Add yourself via PR)
