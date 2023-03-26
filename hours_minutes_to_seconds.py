def hours_minutes_to_seconds(hours, minutes):
    hrs_min_to_seconds = (hours * 3600) + (minutes * 60)
    return hrs_min_to_seconds


print(hours_minutes_to_seconds(1, 3))
print(hours_minutes_to_seconds(2, 0))
print(hours_minutes_to_seconds(0, 0))