# https://atcoder.jp/contests/past201912-2/tasks/past201912_f

S = input() + "0"
#print(S)
words = []

index = 0
pointer = 0
upper_count = 0
while(True):
    if S[index] == "0":
        break
    if S[index].isupper():
        upper_count += 1
    if upper_count == 2:
        words.append(eval("S[{0}:{1}]".format(pointer, index+1)).lower())
        upper_count = 0
        pointer = index + 1
    index += 1

words = sorted(words)
answer = ""
for i in range(len(words)):
    word = words[i][0].upper() + words[i][1:-1] + words[i][-1].upper()
    answer += word

print(answer)
