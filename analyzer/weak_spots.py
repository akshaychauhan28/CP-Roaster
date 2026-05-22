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

