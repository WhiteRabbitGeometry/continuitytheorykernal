"""
ContinuityLens

A small utility for generating continuity-theory prompts and structured
diagnostic checklists for arbitrary subjects.

Designed for use in AI agents, notebooks, apps, or GitHub projects.
"""

from __future__ import annotations

from dataclasses import asdict
from importlib.resources import files
import json
from typing import Dict, Any, List, Union

from .model import (
    SubjectProfile,
    CONTINUITY_DYNAMICS,
    CONTINUITY_CONDITIONS,
    CONTINUITY_OUTCOMES,
    FAILURE_MODES,
    CORE_DIAGNOSTIC_QUESTIONS,
    SCALE_QUESTIONS,
)


class ContinuityLens:
    """Reusable interface for applying continuity theory."""

    def __init__(self) -> None:
        self.theory = self.load_theory()

    def load_theory(self) -> Dict[str, Any]:
        path = files("continuity_kernel").joinpath("theory.json")
        return json.loads(path.read_text(encoding="utf-8"))

    def normalize_subject(self, subject: Union[str, Dict[str, Any], SubjectProfile]) -> SubjectProfile:
        if isinstance(subject, SubjectProfile):
            return subject
        if isinstance(subject, str):
            return SubjectProfile(subject=subject)
        if isinstance(subject, dict):
            return SubjectProfile(**subject)
        raise TypeError("subject must be a string, dict, or SubjectProfile")

    def diagnostic_questions(self, subject: Union[str, Dict[str, Any], SubjectProfile]) -> List[str]:
        profile = self.normalize_subject(subject)
        questions = list(CORE_DIAGNOSTIC_QUESTIONS)

        if profile.parent_continuities or profile.child_continuities or profile.neighboring_continuities:
            questions.extend(SCALE_QUESTIONS)

        return questions

    def classify_failure_terms(self, notes: str) -> List[str]:
        """
        Extremely simple keyword-based failure-mode hinting.

        This is intentionally transparent and easy to replace with better NLP.
        """
        notes_lower = notes.lower()
        hints = []

        keyword_map = {
            "memory": "traceability_failure",
            "forgot": "traceability_failure",
            "archive": "traceability_failure",
            "lie": "correspondence_failure",
            "fraud": "correspondence_failure",
            "corrupt": "correspondence_failure",
            "neglect": "neglect",
            "maintenance": "neglect",
            "drift": "continuity_drift",
            "overload": "continuity_overload",
            "bureaucracy": "continuity_overload",
            "restore": "false_restoration",
            "nostalgia": "false_restoration",
            "parasit": "predation",
            "extract": "predation",
            "monopoly": "continuity_cancer",
            "cancer": "continuity_cancer",
            "feedback": "feedback_amplification",
            "recursive": "recursive_closure",
            "dogma": "recursive_closure",
            "closed": "recursive_closure",
            "sever": "severance",
            "extinct": "termination",
            "collapse": "collapse",
            "fragment": "fragmentation",
        }

        for key, mode in keyword_map.items():
            if key in notes_lower and mode not in hints:
                hints.append(mode)

        return hints

    def build_prompt(self, subject: Union[str, Dict[str, Any], SubjectProfile]) -> str:
        profile = self.normalize_subject(subject)
        data = asdict(profile)

        prompt = f"""Apply the Continuity / Integrity Persistence lens to the following subject.

Subject:
{json.dumps(data, indent=2)}

Use these principles:
- Treat the subject as a continuity, not merely as an object.
- Identify what persists through transformation.
- Distinguish actual lineage, represented lineage, and traceable lineage.
- Analyze integrity as correspondence across continuity.
- Identify stewardship mechanisms that preserve transmission.
- Identify debt, drift, overload, fragmentation, restoration, predation, or closure.
- Ask where corrective inheritance can still enter the system.
- Specify scale: failure or success of what continuity, at what level?
- Avoid treating all change as failure.
- Avoid treating persistence as proof of integrity.

Produce:
1. Subject continuity.
2. Inherited structures.
3. Integrity strengths.
4. Continuity debts.
5. Failure modes or risk modes.
6. Corrective inheritance pathways.
7. Scale/ecology notes.
8. One compressed thesis sentence.
"""
        return prompt

    def analyze(self, subject: Union[str, Dict[str, Any], SubjectProfile]) -> Dict[str, Any]:
        profile = self.normalize_subject(subject)
        notes = profile.notes or ""
        hinted = self.classify_failure_terms(notes)

        return {
            "subject_profile": asdict(profile),
            "analysis_prompt": self.build_prompt(profile),
            "diagnostic_questions": self.diagnostic_questions(profile),
            "hinted_failure_modes": hinted,
            "taxonomy": {
                "dynamics": CONTINUITY_DYNAMICS,
                "conditions": CONTINUITY_CONDITIONS,
                "outcomes": CONTINUITY_OUTCOMES,
                "failure_modes": FAILURE_MODES,
            },
        }

    def export_theory_json(self) -> Dict[str, Any]:
        return self.theory
