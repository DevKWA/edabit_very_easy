def profitable_gamble(prob, prize, pay):
    if prob * prize > pay:
        return True
    return False


print(profitable_gamble(0.2, 50, 9))
print(profitable_gamble(0.9, 1, 2))
print(profitable_gamble(0.9, 3, 2))