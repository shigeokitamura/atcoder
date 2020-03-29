# https://atcoder.jp/contests/past201912-2/tasks/past201912_e

N, Q = map(int, input().split())
S = [list(map(int,list(input().split()))) for i in range(Q)]

f = [["N"] * (N+1) for i in range(N+1)]

for i in range(N+1):
    f[0][i] = "E"
    f[i][0] = "E"
#print(S)

def following(id):
    result = []
    for i in range(1, N+1):
        if f[id][i] == "Y":
            result.append(i)
    return result

def followers(id):
    result = []
    for i in range(1, N+1):
        if f[i][id] == "Y":
            result.append(i)
    return result

for i in range(Q):
    #print(S[i])
    if S[i][0] == 1:
        #print("hoge")
        follower = S[i][1]
        followed = S[i][2]
        f[follower][followed] = "Y"
    elif S[i][0] == 2:
        #print("fuga")
        user = S[i][1]
        #print(followers(S[i][1]))
        for i in followers(user):
            f[user][i] = "Y"
    elif S[i][0] == 3:
        #print("piyo")
        user = S[i][1]
        for i in following(user):
            for j in following(i):
                if user != j:
                    f[user][j] = "Y"

for i in range(1, N+1):
    print("".join(f[i][1:]))
