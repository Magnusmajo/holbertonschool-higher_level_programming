from io import open

answer = '[1, 2, 3, 4]'
# answer = 'no'
# answer = 'True'
# answer = 'False'

with open('14-answer.txt', 'w') as f:
    f.write(answer)

l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)