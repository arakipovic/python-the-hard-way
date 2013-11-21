i = 0
numbers = []

while i <= 10 :
	numbers.append(i)
	i += 1
	
for i in numbers :
	print i
	
	
players = { 'kiki' : "Ronaldo", 'bale' : "Gareth", 'lukica' : "modic" }
for nadimak, prezime in players.items() :
	print nadimak, prezime