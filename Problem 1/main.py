import sys

if(len(sys.argv) != 2):
    print('python %s <num>' %sys.argv[0])
    sys.exit()

num = int(sys.argv[1])
if(num > 3):
    dp = [0] * (num+1)
    dp[0] = 1
    dp[1] = 2
    dp[2] = 4

    for i in range(3, num):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[num-1])
elif(num == 3):
    print(4)
elif(num == 2):
    print(2)
elif(num == 1):
    print(1)
else:
    print(0)