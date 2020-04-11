S = input()

count = 0
for i in range(len(S)-1):
    if S[i] == S[i+1]:
        count += 1

if count > 0:
    print("Bad")
else:
    print("Good")