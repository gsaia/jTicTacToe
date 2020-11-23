from Game import Game, GameOver, InvalidMoveError
from randomPlayer import randomPlayer
from humanPlayer import humanPlayer

game = Game()
a = game.board

print (game)
print()

game.make_move(1,1)
print(game)
print()

game.make_move(0,1)
print(game)
print()

game.make_move(0,0)
print(game)
print()

game.make_move(0,2)
print(game)
print()

game.make_move(2,2)
print(game)
print()

print("Second Game")
print()

game2 = Game()

p0 = humanPlayer()
p1 = randomPlayer()
players = [p0,p1]
count = 0
print (game2)
while True:
    player = players[count%2]
    count +=1
    x,y = player.move(game2)
    print(x,y)
    is_over = game2.make_move(x,y)
    print(game2)
    print()
    if is_over: break


print("Third Game")
print()

game3 = Game()

p1 = humanPlayer()
p0 = randomPlayer()
players = [p0,p1]
count = 0
print (game3)
while True:
    player = players[count%2]
    count +=1
    x,y = player.move(game3)
    print(x,y)
    is_over = game3.make_move(x,y)
    print(game3)
    print()
    if is_over: break