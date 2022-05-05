import random
import sys
from Dungeon import Dungeon
from Fighter import Fighter

dungeon_maze_multi_dimensional_list = [[]]
player = None


def create_and_populate_maze():
    global dungeon_maze_multi_dimensional_list
    global player

    player = Fighter("HERO", "No Pressure", 100, 100, 50, 70)

    f1 = Fighter('Jon Jones', 'The Polish Hammer', 100, 100, 10, 50)
    f2 = Fighter('Tony Ferguson', 'Unpredictable', 75, 75, 25, 60)
    f3 = Fighter('Jorge Masvidal', 'The Striker', 80, 80, 15, 55)
    f4 = Fighter('Francis Ngannou', 'Heavy Hitter', 50, 50, 50, 90)
    f5 = Fighter('Dan Cormier', 'Strike Force', 100, 100, 40, 60)
    f6 = Fighter('Zack Bryant', 'Strong', 70, 70, 55, 60)
    f7 = Fighter('Robert Murray', 'Tank', 175, 175, 20, 25)
    f8 = Fighter('Gary Gordon', 'Injury Prone', 50, 50, 50, 80)
    f9 = Fighter('Aaron James', 'Baller', 75, 75, 25, 60)

    fighter_list = [f1, f2, f3, f4, f5, f6, f7, f8, f9]
    random.shuffle(fighter_list)
    stole_soul_winner = random.randint(0, 8)
    fighter_list[stole_soul_winner].stole_soul = True

    d1 = Dungeon('The Dungeon', 'The Worst Dungeon Ever', fighter_list[0])
    d2 = Dungeon('The Dungeon With Moldy Water', 'A Moldy Dungeon', fighter_list[1])
    d3 = Dungeon('The Father Dungeon', 'Darth Vader Claims You', fighter_list[2])
    d4 = Dungeon('The Harry Potter Dungeon', 'You Meet Voldemort', fighter_list[3])
    d5 = Dungeon('Unworked Stone Walls', 'Very Stony', fighter_list[4])
    d6 = Dungeon('Superior Masonry Walls', 'The Superior Masonry', fighter_list[5])
    d7 = Dungeon('Natural Cavern Complex', 'Very Deep Caves', fighter_list[6])
    d8 = Dungeon('Safe Storage', 'You Can Trust This To Keep Your Stuff Safe', fighter_list[7])
    d9 = Dungeon('Ruined Structure', 'Not Actually Ruined', fighter_list[8])

    dungeon_list = [d1, d2, d3, d4, d5, d6, d7, d8, d9]
    random.shuffle(dungeon_list)

    dungeon_maze_multi_dimensional_list = [
        [dungeon_list[0], dungeon_list[1], dungeon_list[2]],
        [dungeon_list[3], dungeon_list[4], dungeon_list[5]],
        [dungeon_list[6], dungeon_list[7], dungeon_list[8]],
    ]


def play_game():
    global dungeon_maze_multi_dimensional_list
    start_row = int(random.randint(0, 2))
    start_column = int(random.randint(0, 2))

    bad_guy_to_fight = dungeon_maze_multi_dimensional_list[start_row][start_column].fighter

    while True:
        if player.is_alive():
            playerChoice = int(input('Press 1 to attack, press 2 to heal\n'))
            if playerChoice == 1:
                attackStrength = player.attack()
                bad_guy_to_fight.current_hit_points -= attackStrength
                print('BOOM! You struck with a strength of {}'.format(attackStrength))
                print('Your opponent now has {} hit points remaining\n'.format(
                    bad_guy_to_fight.current_hit_points))
            else:
                healResult = player.heal()
                if healResult:
                    print('You now have {} hit points\n'.format(player.current_hit_points))
                else:
                    print('You do not have any potions left, You are forced to attack\n')
                    attackStrength = player.attack()
                    bad_guy_to_fight.current_hit_points -= attackStrength
                    print('BOOM! You struck with a strength of {}'.format(attackStrength))
                    print('Your opponent now has {} hit points remaining\n'.format(
                        bad_guy_to_fight.current_hit_points))
        else:
            print('Sorry you lost, please try again')
            sys.exit()

        if bad_guy_to_fight.is_alive():
            attackStrength = bad_guy_to_fight.attack()
            player.current_hit_points -= attackStrength
            print('BOOM! Your opponent struck with a strength of {}'.format(attackStrength))
            print('You now have {} hit points remaining\n'.format(player.current_hit_points))
        else:
            print('Congrats! You have defeated this opponent!')
            player.current_hit_points = player.max_hit_points
            player.num_of_potions = 1
            if bad_guy_to_fight.stole_soul:
                print('You found your soul! :)')
            else:
                print('Sorry, he did not have your soul :(')
            break


if __name__ == '__main__':
    create_and_populate_maze()
    play_game()
