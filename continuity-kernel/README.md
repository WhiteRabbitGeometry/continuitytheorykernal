# Continuity Kernel

A lightweight, reusable module for applying the working theory of Integrity Persistence / Continuity Theory to arbitrary objects, stories, systems, institutions, risks, or ideas.

This is not a simulation game. It is a conceptual analysis kernel designed so humans, AI agents, scripts, and projects can plug in their own subject matter and receive continuity-oriented prompts, schemas, and diagnostic categories.

## Core lens

The kernel assumes:

- Existence permits continuity.
- Continuity persists through constitutive inheritance.
- Identity emerges from continuity.
- Integrity measures correspondence across continuity.
- Stewardship preserves transmission.
- Debt accumulates through divergence.
- Drift is neutral change through time.
- Failure is not primitive; many failures emerge from deeper continuity dynamics.
- A healthy continuity preserves corrective inheritance.
- All analysis is scale-dependent: failure of what continuity, at what scale?

## Install locally

```bash
pip install -e .
```

## Minimal use

```python
from continuity_kernel import ContinuityLens

lens = ContinuityLens()

report = lens.analyze({
    "subject": "Waiting for Godot",
    "type": "literary work",
    "notes": "Two tramps wait for Godot. Continuity is minimal, repetitive, and unstable."
})

print(report["analysis_prompt"])
print(report["diagnostic_questions"])
```

## Files

- `continuity_kernel/lens.py` — main Python API
- `continuity_kernel/model.py` — dataclasses and taxonomy
- `continuity_kernel/theory.json` — machine-readable theory kernel
- `continuity_kernel/prompt_pack.md` — AI prompt templates
- `examples/example_usage.py` — simple usage demo

## Suggested use cases

- Literary analysis
- Risk assessment
- Institutional diagnosis
- AI alignment analysis
- Narrative design
- Worldbuilding
- Philosophy tools
- Continuity-aware agent prompts
- Failure-mode classification

## License

MIT
