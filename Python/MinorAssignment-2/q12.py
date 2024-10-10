import statistics

data = [1, 2, 3, 2, 3, 4, 4, 4, 5, 4, 5, 6]

mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)

print(f"Mean: {mean}, Median: {median}, Mode: {mode}")
