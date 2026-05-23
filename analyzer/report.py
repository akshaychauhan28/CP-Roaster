from analyzer.stats import solved_count, acceptance_rate, avg_difficulty, activity_streak
from analyzer.weak_spots import top_weak_areas

def build_report(profile):
    report = {
        "handle":profile.handle,
        "rating":profile.rating,
        "rank":profile.rank,
        "max_rating":profile.max_rating,
        "contest_count":profile.contest_count,
        "solved_count":solved_count(profile),
        "acceptance_rate":acceptance_rate(profile),
        "avg_difficulty":avg_difficulty(profile),
        "activity_streak":activity_streak(profile),
        "top_weak_areas":top_weak_areas(profile)
    }

    return report