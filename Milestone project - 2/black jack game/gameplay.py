
from BJ import *

print("<<<Welcome to the BlackJack Game!>>>")
g = Game()
r = Round(g.dealer,g.player)

while r.round_play():
	if g.player.stack > 0:
		r = Round(g.dealer,g.player)
		continue
	else:
		print("Stack devastated!")
		break
print("Goodbye!")