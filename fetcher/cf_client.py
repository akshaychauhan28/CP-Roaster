import requests
from fetcher.models import UserProfile, Submission, RatingChange

BASE_URL = "https://codeforces.com/api/"

def get_user_info(handle):
    url = f"{BASE_URL}/user.info?handles={handle}"
    response = requests.get(url)
    data = response.json()

    if data['status'] != 'OK':
        raise ValueError("User not Found")
    
    user = data["result"][0]
    return UserProfile(
        handle=user["handle"],
        rating=user.get("rating", 0),
        max_rating=user.get("maxRating", 0),
        rank=user.get("rank", "unrated"),
        max_rank=user.get("maxRank", "unrated"),
        contest_count=0
    )

def get_submissions(handle):
    url = f"{BASE_URL}/user.status?handle={handle}"
    response = requests.get(url)
    data = response.json()

    if data['status'] != 'OK':
        raise ValueError("User not Found")

    submissions = []
    for s in data["result"]:      # loop through each submission
        problem = s.get("problem", {})
        submissions.append(Submission(
            problem_name = problem.get("name", "Unknown"),  # grab name FROM problem
            tags         = problem.get("tags", []),          # grab tags FROM problem
            rating       = problem.get("rating", 0),         # grab rating FROM problem
            verdict      = s.get("verdict", "UNKNOWN"), 
            timestamp    = s.get("creationTimeSeconds",0),
        ))

    return submissions


     
def get_rating_history(handle):
    url = f"{BASE_URL}/user.rating?handle={handle}"
    response = requests.get(url)
    data = response.json()

    if data['status'] != 'OK':
        return[]
    
    rating_history = []
    for h in data["result"]:
        rating_history.append(RatingChange(
            contest_name= h.get("contestName", "Unknown"),
            old_rating= h.get("oldRating", 0),
            new_rating= h.get("newRating", 0)
        ))

    return rating_history

def fetch_profile(handle):
    profile=get_user_info(handle)
    profile.submissions = get_submissions(handle)
    profile.rating_history = get_rating_history(handle)
    profile.contest_count = len(profile.rating_history)
    return profile