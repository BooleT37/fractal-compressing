import math


def fill_row_with_intervals(row_length, interval_max_length):
    if row_length == 0:
        return []
    intervals_fit = int(math.ceil(row_length / interval_max_length))
    interval_fract_length = row_length / intervals_fit

    cumulative_length = 0.
    cumulative_length_int = 0
    intervals = []
    for i in range(intervals_fit):
        cumulative_length += interval_fract_length
        interval_length = round(cumulative_length) - cumulative_length_int
        intervals.append(interval_length)
        cumulative_length_int += interval_length
    return intervals
