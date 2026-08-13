def minion_game(string):
    word = string
    score1 = 0
    score2 = 0
    check = 0
    count = len(word)
    
    while check < count:
        if word[check] == "A" or word[check] == "E" or word[check] == "I" or word[check] == "O" or word [check] == "U":
            points = len(word[check:])
            score1 = score1 + points
        check = check + 1
    check = 0
    while check < count:
        if word[check] != "A" and word[check] != "E" and word[check] != "I" and word[check] != "O" and word[check] != "U":
            points = len(word[check:])
            score2 = score2 + points
        check = check + 1
    if score1 > score2:
        winner = "Kevin"
    elif score1 < score2:
        winner = "Stuart"
    else: winner = "Draw"
    
    if score1 > score2:
        score = score1
    elif score1 < score2:
        score = score2
    else: score = ""
    
    return print(winner, score)

if __name__ == '__main__':
    s = input()
    minion_game(s)