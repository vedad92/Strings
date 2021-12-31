# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

player1 = 'koeman'
player2 = 'gullit'
player3 = 'rijkaard'

goal_0 = 22
goal_1 = 36
goal_2 = 50

scorers = player1 + ' ' + str(goal_0) 

scorers = f"""player {player1} scored in the {goal_0}nd minute
player {player2} scored in the {goal_1}th minute,
player {player3} scored in the {goal_2}th minute""" 

print(scorers)

player = 'Marco van Basten'

firstName = player.find('Marco')
firstName = player[0:5]
print(firstName)

lastNameLen = player.find('van Basten')
lastNameLen = player[6:16]
print(lastNameLen, len(lastNameLen))

nameShort = 'M. van Basten'
chant = f'{firstName}! ' * len(firstName)
print(chant)

goodChant = chant[-1] != " "
print(goodChant)
















 
