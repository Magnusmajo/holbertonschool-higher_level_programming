from io import open

answer = [1, 2, 3, 4]
# answer = 'no'
# answer = 'True'
# answer = 'False'

with open('17-answer.txt', 'w') as f:
    f.write(answer)

# def increment(n):
#     n.append(4)

# l = [1, 2, 3]
# increment(l)
# print(l)