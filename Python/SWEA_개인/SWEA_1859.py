T = int(input())
for i in range(1,T+1):
    N = int(input())
    prices = list(map(int,input().split()))
    max_prices_idx = prices.index(max(prices))
    price_sum = 0
    profit = 0
    cnt=0
    for j in range(len(prices)):
        price_sum+=prices[j]
        cnt+=1
        if j == max_prices_idx:
            profit+=(prices[j]*(cnt-1))-(price_sum-prices[j])
            cnt = 0
            price_sum =0
            max_prices_idx = prices[max_prices_idx+1:].index(max(prices[max_prices_idx+1:]))
    print(profit)


    