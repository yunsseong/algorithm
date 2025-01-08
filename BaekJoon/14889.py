def rec(idx, team1, team2, count1, count2):
    global answer

    if count1 == n / 2 and count2 == n / 2:
        answer = min(answer, abs(cal(team1) - cal(team2)))
        return

    if count1 > n / 2 or count2 > n / 2:
        return

    rec(idx + 1, team1 + " " + str(idx), team2, count1 + 1, count2)
    rec(idx + 1, team1, team2 + " " + str(idx), count1, count2 + 1)


def cal(team):
    tmp = 0
    team = team.strip().split(" ")
    for i in range(len(team)):
        for j in range(len(team)):
            if i == j:
                continue
            tmp += ability[int(team[i])][int(team[j])]

    return tmp


n = int(input())
ability = [list(map(int, input().split())) for _ in range(n)]

answer = 999999999999999
rec(0, "", "", 0, 0)
print(answer)
