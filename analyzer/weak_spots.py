from fetcher.models import UserProfile

def tag_rates_fail(profile):
    tag_stats = {}

    for each in profile.submissions:
        for each_tag in each.tags:
            if each_tag not in tag_stats:
                tag_stats[each_tag] = {"attempts": 0, "fails": 0}
            tag_stats[each_tag]["attempts"] += 1
            if each.verdict != "OK":
                tag_stats[each_tag]["fails"] += 1

    return tag_stats

def top_weak_areas(profile,n=3):
    tag_stats = tag_rates_fail(profile)
    sorted_tag_stats = []
    
    for user_tags, user_tags_info in tag_stats.items():
        if user_tags_info["attempts"] == 0:
            continue

        else:
            fail_rate = (user_tags_info["fails"]/user_tags_info['attempts'])*100
            sorted_tag_stats.append((user_tags,fail_rate))

    second_sorted_tag_stats = sorted(sorted_tag_stats,key = lambda sorted_tag_stats: sorted_tag_stats[1],reverse=True)
    final_sorted_tag_stats = []    
    for i in range(n):
        final_sorted_tag_stats.append(second_sorted_tag_stats[i][0])

    return final_sorted_tag_stats