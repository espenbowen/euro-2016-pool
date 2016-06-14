import sys
import random
random.seed(2016)

teams = ["Albania","Austria","Belgium","Croatia","Czech Republic","England","France","Germany","Hungary","Iceland","Italy","Northern Ireland","Poland","Portugal", "Republic of Ireland","Romania","Russia","Slovakia","Spain","Sweden","Switzerland","Turkey","Ukraine","Wales"]

players = ["Patrick","Matt","Jack","Andrew","Kara","Espen"]

sys.stdout.write("| Players | Teams | \n")
sys.stdout.write("| --- | --- | \n")
for player in players:
	sys.stdout.write("| %s | "%player)
	for _ in range(4):
		team = teams[random.randint(0,len(teams)-1)]
		sys.stdout.write(" %s "%team)
		teams.remove(team)
	sys.stdout.write("| \n")
		


