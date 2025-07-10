n = int(input())
scores = list(map(int, input().split()))
highest = max(scores)
while highest in scores:
    scores.remove(highest)
runner_up = max(scores)
print(runner_up)
