from io import open

# answer = 'yes'
answer = 'no'

with open('5-answer.txt', 'w') as f:
    f.write(answer)

# a = 89
# b = a + 1

# print(f'ID of a = {id(a)} \n  Id of b={id(b)}')