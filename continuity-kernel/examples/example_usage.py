from continuity_kernel import ContinuityLens

lens = ContinuityLens()

subject = {
    "subject": "Severance",
    "type": "television show",
    "notes": "A corporation partitions memory and creates innies/outies with severed inheritance pathways.",
    "parent_continuities": ["corporate institution", "human identity"],
    "child_continuities": ["innie", "outie", "Lumon mythology"],
}

report = lens.analyze(subject)

print(report["analysis_prompt"])
print("\nSuggested failure modes:", report["hinted_failure_modes"])
