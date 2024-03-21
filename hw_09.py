import time

# Функція жадібного алгоритму
def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            result[coin] = count
    return result

# Функція динамічного програмування
def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [0] + [float('inf')]*amount
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i-coin] + 1)
    
    result = {}
    while amount > 0:
        for coin in coins:
            if amount >= coin and dp[amount] == dp[amount-coin] + 1:
                amount -= coin
                if coin in result:
                    result[coin] += 1
                else:
                    result[coin] = 1
                break
    return result

# Порівняння часу виконання, наприклад, для суми 113
start_time_greedy = time.time()
greedy_result = find_coins_greedy(113)
end_time_greedy = time.time()

start_time_dp = time.time()
dp_result = find_min_coins(113)
end_time_dp = time.time()

# Результати
print(f"Жадібний алгоритм результат: {greedy_result}") 
print(f"Час виконання жадібного алгоритму: {(end_time_greedy - start_time_greedy)*100}") 
print(f"Алгоритм динамічного програмування результат: {dp_result}")
print(f"Час виконання алгоритму динамічного програмування: {(end_time_dp - start_time_dp)*100}") 
