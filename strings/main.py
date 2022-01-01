# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

player = 'Ruud Gullit'
player2 = 'Marco van Basten'


goal_0 = 32
goal_1 = 54

scorers = player + ' ' + str(goal_0) + ', ' + player2 + ' ' + str(goal_1)

print(scorers)

report = f"""{player} scored in the {goal_0}nd minute
{player2} scored in the {goal_1}th minute""" 

print(report)

first_name = player.find('Ruud')
first_name = player[0:4]
print(first_name)

last_name_len = player.find('Gullit')
last_name_len = player[5:11]
print(len(last_name_len))

name_short = 'R. Gullit'
chant = f'{first_name}! ' * len(first_name)
print(chant)

good_chant = chant[-1] != " "
print(good_chant)
















 
