from fetcher.models import UserProfile
from datetime import datetime, date, timezone, timedelta


def solved_count(profile):
    total = 0
    for i in profile.submissions:
        if i.verdict == 'OK':
            total +=1

    return total

def acceptance_rate(profile):
    if len(profile.submissions) == 0:
        return 0
    
    total_succesful_submission = (solved_count(profile)/len(profile.submissions)) * 100

    return total_succesful_submission

def avg_difficulty(profile):
    total_rating = 0
    total = 0
    for i in profile.submissions:
        if i.verdict == 'OK' and i.rating != 0:
            total_rating += i.rating 
            total +=1

    if total == 0:
        return 0
    average = total_rating/total
    return average

def activity_streak(profile):
    unique_days = set()

    for i in profile.submissions:
        user_time = datetime.fromtimestamp(i.timestamp, tz=timezone.utc).date()
        unique_days.add(user_time)
    
    sorted_days = sorted(unique_days,reverse=True)
    today_date = date.today()
    streak = 0

    for day in sorted_days:
        if day == today_date:
            streak +=1
            today_date = today_date - timedelta(days=1)

        else:
            break


    return streak        