from io import open

# answer = 'yes'
# answer = 'no'
answer = 'True'

with open('9-answer.txt', 'w') as f:
    f.write(answer)

s1 = "Best School"
s2 = "Best School"
print(s1 is s2)