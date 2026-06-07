"""
Continuity Kernel model.

This module contains the current working taxonomy of Continuity Theory.

It is intentionally plain Python so other projects and AI agents can import it,
serialize it, extend it, or use it to generate prompts.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any


CONTINUITY_DYNAMICS = {
    "inheritance": "Transmission of organizational structure across transformation.",
    "transformation": "Change through which a continuity either adapts, drifts, fragments, or terminates.",
    "stewardship": "Maintenance of inheritance pathways.",
    "debt": "Accumulated divergence between representation, reality, function, lineage, or stewardship.",
    "drift": "Neutral gradual change through time; not necessarily failure unless traceability or correspondence degrades.",
    "selection": "Differential survival or propagation of continuities.",
    "adaptation": "Capacity to transform while preserving sufficient inheritance.",
    "recursion": "A continuity containing, modeling, or modifying itself through feedback.",
    "ecological_interaction": "Interaction between nested or neighboring continuities.",
    "corrective_inheritance": "The ability of reality, observation, or critique to modify the continuity's future states.",
}

CONTINUITY_CONDITIONS = {
    "integrity": "Degree of correspondence across continuity.",
    "traceability": "Degree to which lineage can be recovered, verified, or reconstructed.",
    "correspondence": "Alignment between representation and reality, function, principle, or lineage.",
    "stewardship_quality": "How well transmission preserves meaningful inheritance rather than mere artifacts.",
    "resilience": "Capacity to preserve viability under perturbation.",
    "corrective_capacity": "Capacity to notice, accept, and inherit correction.",
    "propagation": "Capacity to reproduce or transmit into future states.",
    "context_integrity": "Degree to which local context remains connected to the larger continuity.",
}

CONTINUITY_OUTCOMES = {
    "persistence": "The continuity remains viable through transformation.",
    "restoration": "Correspondence is repaired after divergence.",
    "fragmentation": "Inheritance weakens or branches into multiple successor continuities.",
    "speciation": "Fragmentation produces viable descendant continuities.",
    "collapse": "Viability fails after accumulated debt or shock.",
    "termination": "Constitutive inheritance ceases.",
    "absorption": "A continuity loses independence but survives as part of another continuity.",
    "simulacrum": "Representation persists while constitutive inheritance weakens or terminates.",
    "overload": "Inherited structure accumulates faster than adaptive capacity can process.",
}

FAILURE_MODES = {
    "correspondence_failure": "Representations diverge from reality.",
    "traceability_failure": "Lineage becomes difficult or impossible to reconstruct.",
    "context_failure": "Local context disconnects from the larger continuity.",
    "neglect": "Necessary stewardship or maintenance ceases.",
    "capture": "Stewardship becomes subordinate to another continuity.",
    "dependency_failure": "Continuity depends too heavily on a single steward or bottleneck.",
    "transmission_failure": "Knowledge, structure, or practice cannot be transferred.",
    "propagation_failure": "The continuity cannot reproduce into future states.",
    "selection_failure": "Poor inheritances are preferentially transmitted.",
    "simulacral_drift": "Representation replaces inheritance; the continuity becomes a copy of itself.",
    "fragmentation": "Sub-continuities diverge beyond stable identity.",
    "identity_lock": "A continuity refuses adaptation in order to preserve represented identity.",
    "continuity_overload": "Too much inherited structure burdens adaptation.",
    "continuity_drift": "Gradual change moves the continuity away from prior identity; not inherently pathological.",
    "false_restoration": "A continuity attempts to restore an imagined past rather than its actual lineage.",
    "predation": "A continuity survives by extracting inheritance capacity from another continuity.",
    "continuity_cancer": "A continuity thrives locally while damaging the larger continuity that sustains it.",
    "feedback_amplification": "Errors reproduce and amplify through recursive loops.",
    "recursive_delusion": "The model replaces reality and corrections become threats.",
    "recursive_closure": "A framework or system becomes immune to corrective inheritance.",
    "deferred_stewardship": "Action is postponed while debt accumulates.",
    "habitat_loss": "Supporting ecological continuities disappear.",
    "ecological_cascade": "Dependent continuities fail together.",
    "severance": "Lineage is broken or rendered unrecoverable.",
}

SCALE_QUESTIONS = [
    "What is the subject continuity?",
    "What parent continuities contain it?",
    "What child continuities compose it?",
    "Which neighboring continuities cooperate, compete, parasitize, or steward it?",
    "Is this event a failure locally but adaptive globally?",
    "Is success at one scale producing debt at another scale?",
]

CORE_DIAGNOSTIC_QUESTIONS = [
    "What continuity is being examined?",
    "What persists through transformation?",
    "What is inherited?",
    "What is represented as inherited?",
    "What is actually inherited?",
    "Where is lineage traceable?",
    "Where is traceability missing?",
    "What correspondence is strong?",
    "What correspondence is weak?",
    "What stewardship mechanisms preserve transmission?",
    "Where is debt accumulating?",
    "Where can corrective inheritance enter?",
    "Where has corrective inheritance been blocked?",
    "Is apparent success backed by integrity or momentum?",
    "Is the system adapting, drifting, fragmenting, restoring, or becoming a simulacrum?",
    "Failure of what continuity, at what scale?",
]


@dataclass
class SubjectProfile:
    subject: str
    type: Optional[str] = None
    notes: Optional[str] = None
    parent_continuities: List[str] = field(default_factory=list)
    child_continuities: List[str] = field(default_factory=list)
    neighboring_continuities: List[str] = field(default_factory=list)
    observed_failures: List[str] = field(default_factory=list)
    observed_strengths: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
