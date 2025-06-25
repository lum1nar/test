v=[0,10,6,13,7,8]
w=[0,6,3,9,4,2]

dp = [[0]*11 for _ in range(6)]
a = 5
for a in dp:
    print(a)

for i in range(0,6):
    for W in range(0,11):
        if w[i] > W:
            dp[i][W] = dp[i-1][W]
        else:
            dp[i][W] = max(dp[i-1][W-w[i]]+v[i], dp[i-1][W])
#TODO： Eat something
print()       
for a in dp:
    print(a)
