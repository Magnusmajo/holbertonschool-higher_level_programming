from io import open

answer = [1, 2, 3]
# answer = 'no'
# answer = 'True'
# answer = 'False'

with open('18-answer.txt', 'w') as f:
    f.write(answer)

def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)