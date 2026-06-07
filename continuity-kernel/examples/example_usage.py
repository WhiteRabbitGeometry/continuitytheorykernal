from continuity_kernel import ContinuityLens

lens = ContinuityLens()

examples = [
{
"subject": "Public Library",
"type": "institution",
"notes": """
A public library preserves knowledge across generations.
Funding has declined.
Experienced staff are retiring.
Digitization efforts are underway.
"""
},

```
{
    "subject": "Temperate Forest",
    "type": "ecosystem",
    "notes": """
    A forest ecosystem containing diverse species,
    nutrient cycles, and long-term ecological relationships.
    Wildfires periodically occur.
    """
},

{
    "subject": "Commercial Nuclear Power Plant",
    "type": "infrastructure",
    "notes": """
    A nuclear facility producing electricity through
    long-term reactor operations. Safety depends on
    maintenance, operator training, monitoring systems,
    and regulatory oversight.
    """
}
```

]

for example in examples:

```
report = lens.analyze(example)

print("=" * 60)
print("SUBJECT:", example["subject"])
print("=" * 60)

print("\nSuggested Failure Modes:")
print(report["hinted_failure_modes"])

print("\nSample Diagnostic Questions:")

for question in report["diagnostic_questions"][:5]:
    print("-", question)

print("\n")
```
