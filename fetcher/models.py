from dataclasses import dataclass, field
from typing import List

@dataclass
class Submission:
    problem_name: str
    tags: List[str]
    rating: int
    verdict: str        # "OK" means solved, anything else means failed
    timestamp: int = 0

@dataclass
class RatingChange:
    contest_name: str
    old_rating: int
    new_rating: int

@dataclass
class UserProfile:
    handle: str
    rating: int
    max_rating: int
    rank: str
    max_rank: str
    contest_count: int
    submissions: List[Submission] = field(default_factory=list)
    rating_history: List[RatingChange] = field(default_factory=list)