def study_schedule(permanence_period, target_time):
    if not permanence_period:
        return None

    if not target_time:
        return None

    counter = 0
    for period in permanence_period:
        if type(period[0]) != int:
            return None
        if type(period[1]) != int:
            return None
        if period[0] <= target_time <= period[1]:
            counter += 1

    return counter
