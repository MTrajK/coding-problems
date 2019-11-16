import math

def solve(sentence, words):
    n = len(sentence)
    w = len(words)
    dp = [math.inf for i in range(n)]
    dp[0] = 0
    dw = [-1 for i in range(n)]

def solve_2(sentence, words):
    n = len(sentence)
    w = len(words)
    dp = [math.inf for i in range(n + 1)]
    dp[0] = 0
    dw = [-1 for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(w):
            start = i - len(words[j])
            if (start >= 0) and (words[j] == sentence[start: i]) and (dp[start] + 1 < dp[i]):
                dp[i] = dp[start] + 1
                dw[i] = j
    
    if dp[n] == math.inf:
        return None

    result = ['' for i in range(dp[n])]
    i = n
    j = dp[n] - 1
    while i > 0:
        result[j] = words[dw[i]]
        i -= len(words[dw[i]])
        j -= 1

    return result


# Test 1
# Correct result => ['the', 'quick', 'brown', 'fox']
print(solve('thequickbrownfox', ['quick', 'brown', 'the', 'fox']))

# Test 2
# Correct result => ['bed', 'bath', 'and', 'beyond']
print(solve('bedbathandbeyond', ['bed', 'bath', 'bedbath', 'and', 'beyond']))

# Test 3
# Correct result => ['bed', 'bathand', 'beyond']
print(solve('bedbathandbeyond', ['bed', 'bath', 'bedbath', 'bathand', 'beyond']))

# Test 4
# Correct result => None ('beyo' doesn't exist)
print(solve('bedbathandbeyo', ['bed', 'bath', 'bedbath', 'bathand', 'beyond']))

# Test 5
# Correct result => ['314', '15926535897', '9323', '8462643383279']
print(solve('3141592653589793238462643383279', ['314', '49', '9001', '15926535897', '14', '9323', '8462643383279', '4', '793']))