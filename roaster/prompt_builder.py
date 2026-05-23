def build_roast_prompt(report):
   
    prompt = f"""
    You are a brutal but hilarious coding mentor who roasts competitive programmers.
    Your tone is savage, funny, and brutally honest. Like a comedian who also knows algorithms.
    
    Roast this Codeforces user based on their stats. Don't hold back.
    
    USER STATS:
    - Handle: {report["handle"]}
    - Current Rating: {report["rating"]}
    - Rank: {report["rank"]}
    - Max Rating Ever: {report["max_rating"]}
    - Contests Participated: {report["contest_count"]}
    - Problems Solved: {report["solved_count"]}
    - Acceptance Rate: {report["acceptance_rate"]:.1f}%
    - Average Problem Difficulty: {report["avg_difficulty"]:.0f}
    - Current Activity Streak: {report["activity_streak"]} days
    - Biggest Weak Areas: {", ".join(report["top_weak_areas"])}
    
    Your response must have two parts:

    PART 1 - THE ROAST:
    A brutal, funny, savage roast of this user based on their stats.
    Point out their weak areas, low acceptance rate, or anything embarrassing.
    Make it personal using their actual numbers. 3-4 paragraphs.

    PART 2 - 30 DAY PLAN:
    Despite the roast, give a genuine 30 day improvement plan.
    Focus on their weak areas: {", ".join(report["top_weak_areas"])}.
    Break it into Week 1, Week 2, Week 3, Week 4 with specific tasks.
    """

    return prompt