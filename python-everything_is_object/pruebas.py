from io import open

# answer = 'yes'
# answer = 'no'
# answer = 'True'
answer = 'False'

with open('13-answer.txt', 'w') as f:
    f.write(answer)

l1 = [1, 2, 3]
l2 = l1
print(l1 is l2)