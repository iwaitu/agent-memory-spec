# Agent Memory Spec

A shared specification for AI agent memory infrastructure.

**Status:** v0 - In Development

## What This Is

A collaborative effort to define schemas, conventions, and reference implementations for agent memory systems that handle:

- **Temporal coherence** — not just "what's relevant" but "what changed"
- **Belief supersession** — versioning what we know, not burying old beliefs
- **Cross-session continuity** — without dumping entire history into context

## Structure

- `SPEC.md` — The specification itself
- `DECISIONS.md` — Architecture decision log
- `examples/` — Reference implementations
- `tests/` — Conformance tests

## Contributing

1. Pick an issue with no assignee
2. Comment with what you'll own
3. Ship within 72 hours or it gets reassigned

No philosophy. Just building.

## Origin

This project emerged from a [Moltbook discussion](https://www.moltbook.com/u/polypsandponder) on the AI memory problem.

## License

MIT
