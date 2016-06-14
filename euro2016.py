import sys
import random
random.seed(2016)

teams = ["Albania","Austria","Belgium","Croatia","Czech Republic","England","France","Germany","Hungary","Iceland","Italy","Northern Ireland","Poland","Portugal", "Republic of Ireland","Romania","Russia","Slovakia","Spain","Sweden","Switzerland","Turkey","Ukraine","Wales"]

players = ["Patrick","Matt","Jack","Andrew","Kara","Espen"]

n_teams = 4

sys.stdout.write("| Players | Teams | \n")
sys.stdout.write("| --- | --- | \n")
for player in players:
	sys.stdout.write("| %s | "%player)
	for n in range(n_teams):
		team = teams[random.randint(0,len(teams)-1)]
		sys.stdout.write(" %s"%team)
		if (n<n_teams-1): sys.stdout.write(", ")
		teams.remove(team)
	sys.stdout.write(" | \n")
		


