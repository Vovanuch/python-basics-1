'''

Given a list of football teams with the result of the match. Output the summary table of the results of all matches.

The team gets 3 points for winning, 0 points for loosing, 1 point for draw.

Input format:

The first line specifies the integer n n n — the number of completed games.
After this follow the n n n lines, which contain the game results in the following format:

First_team;Goals_by_first_team;Second_team;Goals_by_second_team

Output of your program should look like the following:

Team:Total_games Wins Draws Defeats Total_points


You can output teams in an arbitrary order.

Sample Input:

3
Zenit;3;Spartak;1
Spartak;1;CSKA;1
CSKA;0;Zenit;2

Sample Output:

CSKA:2 0 1 1 1
Zenit:2 2 0 0 6
Spartak:2 0 1 1 1

'''
# count of matches
n = int(input().strip())

#match results. List of lists
list_games = []
for i in range(n):
    list_games.append(input().strip().split(';'))
    
# list with teams names (not uniq)
list_teams_play = []
for i in range(n):
    list_teams_play.append(list_games[i][0])
    list_teams_play.append(list_games[i][2])

# list with teams names (sorted and uniq)
list_teams = sorted(list(set(list_teams_play)))

# dictionary with full info about team. Filling int fields with zero
dict_teams = dict()
for t in list_teams:
    dict_teams[t] = {}
    dict_teams[t]['games'] = 0
    dict_teams[t]['wins'] = 0
    dict_teams[t]['looses'] = 0
    dict_teams[t]['draws'] = 0
    dict_teams[t]['total_points'] = 0

# analyze of every game. Count all params (wins, scores, etc). 
for g in list_games:
    # counting game for every team
    dict_teams[g[0]]['games'] += 1
    dict_teams[g[2]]['games'] += 1
    
    # 1st team wins 
    if g[1] > g[3]:
        dict_teams[g[0]]['wins'] += 1
        dict_teams[g[0]]['total_points'] += 3
        dict_teams[g[2]]['looses'] += 1
    # 2nd team wins
    elif g[1] < g[3]:
        dict_teams[g[2]]['wins'] += 1
        dict_teams[g[2]]['total_points'] += 3
        dict_teams[g[0]]['looses'] += 1
    # draw
    elif g[1] == g[3]:
        dict_teams[g[2]]['draws'] += 1
        dict_teams[g[0]]['draws'] += 1
        dict_teams[g[2]]['total_points'] += 1
        dict_teams[g[0]]['total_points'] += 1

# print in correct needed format
for k, v in dict_teams.items():
    print(f"{k}:{v['games']} {v['wins']} {v['draws']} {v['looses']} {v['total_points']}")