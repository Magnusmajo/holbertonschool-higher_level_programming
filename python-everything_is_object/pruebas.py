from io import open

# answer = 'yes'
# answer = 'no'
# answer = 'True'
answer = 'False'

with open('11-answer.txt', 'w') as f:
    f.write(answer)

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 is l2)