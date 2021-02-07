team = {}
teamStatus1 = []
teamStatus2 = []
for i in range(2):
    tteam = input('введите названию команды: ')
    a = input('сколько раз команда выиграла: ')
    teamStatus1.append(a)
    b = input('сколько раз команда проиграла: ')
    teamStatus1.append(b)
    teamStatus2.append(teamStatus1)
    team[tteam] = teamStatus2

print(team)