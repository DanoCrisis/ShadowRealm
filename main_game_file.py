import time
import random
import math
import sys
from colorama import init, Fore, Back, Style

init()
FORE = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]    # Sets the Foreground Colours
BACK = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE ]    # Sets the Background Colours
BRIG = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]                                                            # Sets the brightness styles

def print_s(str):                                                                                           # Defines a slow print
    for char in str:
            time.sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
    print()

def print_c(s, color=Fore.WHITE, brightness=Style.NORMAL, **kwargs):                                        # Defines a colour print
    print(f"{brightness}{color}{s}{Style.RESET_ALL}", **kwargs)

def print_s_c(str, color=Fore.WHITE, brightness=Style.NORMAL, **kwargs):                                    # Defines a slow colour print
    for char in str:
            time.sleep(.03)
            sys.stdout.write(f"{brightness}{color}{char}{Style.RESET_ALL}", **kwargs)
            sys.stdout.flush()
    print()


# ---------------------------------- ASCII ART IMAGES --------------------------------------------------------------------------------------
# Images should all be 15 rows high and 28 characters long
# ---------------------------------- Character Images --------------------------------------------------------------------------------------

human_wizard_image = [
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("             ^              "),
("           _/_\_     *      "),
("          .-\-/.    /       "),
("         / |   |\_ /        "),
("     {*}/_/|   |\_(/        "),
("         / (---)            "),
("        / /  _  \           "),
("     _.' / /   ||           "),
("     `--- '==  '==          ")
]

elf_wizard_image = [
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("           |\               "),
("         __/_\__  (@)       "),
("          <['')    |        "),
("           ) -|.   |        "),
("         /'|'''|\_ |        "),
("     {0}/_/|   |\_(/        "),
("         / (---)   |        "),
("        / /  _  \  |        "),
("     _.' / /   ||  |        "),
("     `--- '==  '== '        ")
]

dwarf_wizard_image = [
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("            _/^\_           "),
("            /8 '7     $     "),
("           .\ 888 _  /      "),
("          /| '\ 8\_(/       "),
("         / (---'\_(/        "),
("        / /  __ | /         "),
("      _. / /   ||           "),
("      `-- '==  '==          ")
]

human_knight_image = [
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("      /|   ~~,_             "),
("      \|    ( =)>           "),
("       |  .-/-_\   _        "),
("       | / | v |\ /I\       "),
("      (\/_/|___|\|I I|      "),
("           |_#_)  \I/       "),
("           / _  \           "),
("          / /  | )          "),
("         '==   '==          ")    
]

elf_knight_image = [
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("      ^     .==7            "),
("      |    <| -\            "),
("      |   .-/-_|   _        "),
("      |  / | ^ |\ /I\       "),
("     _|_/ /| V |\|I I|      "),
("     (\/_/ |___| |I I|      "),
("           |_#_)  \I/       "),
("           / _  \           "),
("          / /  | )          "),
("         '==   '==          ")
]

dwarf_knight_image = [
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("     *.*      __            "),
("     *|*     / -|           "),
("      |   _./___\           "),
("      |  / |  V |\ /I\      "),
("      (\/_/|__ _|\|I I|     "),
("           |_ #_)  \I/      "),
("           / __ \           "),
("          / /  | )          "),
("         '==   '==          ")
]

human_warrior_image = [
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("          _ _         ^     "),
("         (_v_\      </|     "),
("        .-\-/.      /_/     "),
("        \\\   |\===(/        "),
("         \\\__|\   /         "),
("         (***)==(/          "),
("        /  _ \  /           "),
("       / /  || /            "),
("      / /   ||/             "),
("      '==   '==             ")
]

elf_warrior_image = [
("                            "),
("                            "),
("                            "),
("                            "),
("                       /    "),
("          .MM         /     "),         
("         <| -\       /      "),
("        .-/-_|      /       "),
("        \\\   |\===(%        "),
("         \\\__|\==(%         "),
("         (***)  //          "),
("        /  _ \              "),
("       / /  ||              "),
("      / /   ||              "),
("      '==    '==            ")
]

dwarf_warrior_image = [
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("                       .    "),
("            (V\       7     "),
("           /8 '7     /      "),
("          .\ 888 _  /       "),
("          | '\ 8\_(%        "),
("          (***'\_(%         "),
("          / __ \ /          "),
("         / /  | |           "),
("        '==    '==          "),
]

# ---------------------------------- Character Images --------------------------------------------------------------------------------------

bat_image = [
("                            "),
("                            "),
("                            "),
("         __     __          "),
("         ) \_V_/ (          "),
("          )_   _(           "),
('            " "             '),
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("                            ")
]

goblin_image = [
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("                   /        "),
("            _     /         "),
("         p /..)>_/_         "),
('         \_." =.{>          '),
("           \T/-'            "),
("           /_\              "),
("          // \\\_            "),
("         _I    /            "),
]

bandit_image = [
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("            (_Ä_)           "),
("            ¢°/|  œ|==>     "),
("        /|  88-|_//         "),
("        ¦|//| ¥ _/          "),
("        (B/ |___|           "),
("            / # |           "),
("           /-.^.-\          "),
("          ( /   \ \         "),
("          =='   =='         ")
]

wolf_image = [
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("       /\                   "),
("  .---°  '-~~~~~~~-__       "),
("    '^v^-)   ______   `\__  "),      
("        \\\(      \\\(-'~~`   "),
("        _//\)    _//\)      "),
]

vulture_image = [
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),   
("             __             "),                   
("      .-`) /=,`|  (`,       "),
("     /-'(____||___)'-\      "),
("     ;.-/'--;  ;--'\-.;     "),
("     |;| '._(__)_,' |;|     "),
("     \:| |  Y  Y  | |:/     "),
("     /_:-` m'  'm `-;_\     ")

]

orc_image = [
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("                            "),
("            __              "),
("           .°/|> œ|====>    "),
("       ^  ¿^--|_//          "),
("      /|_//| # _/           "),
("     (||/y |# #|            "),
("      \|   / # |            "),
("       v  /-.^.-\           "),
("         ( /   \ \          "),
("         =='   =='          "),
] 

# ----------------------------------------------- Character Information -------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------- Character Variables and Lists -----------------------------------------------------

# ---------------- Base player stats --------------

# ----num -----0----1-----2----3------4-------5-------6-------7--------8-----9-------10------11--------12------13-------14------15--------16-------17------18-------19-------20------21------22-----23------24------25-------26-----------------------27-----------28------------29-------------30
# ----------Name - Lvl - Exp - HP - STa - STa reg - Mana - Mana Reg - STr - Attack - Foc - Mag Att - Tough - Phy Def - Armo - Mag Def - Fi Res - Fr Res-  Co Res - Speed - Acc - Evade - Crit -   Trait  - Race  - Class   Image                    Status     Skill Slots   Energy Type-- Character Num
player = ["Player", 1 ,   0 ,  100 ,  0 ,    0 ,      0 ,      0 ,      0 ,    0   ,  0  ,    0     ,   5   ,    0   ,    0    ,  0    ,   0   ,    0  ,     0 ,     4.5  , 0.85 , 0.05 ,  0.05 ,  "None", "None", "None",   [],                   "Active" ,       2,           "",           0]

# ------ Increases per level-----------------------
per_level_stats = [10, 0.2, 0.1,      0.2,    0.1,     0.15,  0.15,   2]


# ---------------- Base race and class stats --------------
# ----num -------0---1------2----------3------4---------5-----6------7-------8-------9-----10-------11
# ------Name -   HP -STa - STa reg - Mana - Mana Reg - STr - Foc - Tough - Speed -- Acc -- Evade - Crit
knight_stats =  [20,  4,    1,        0,       0,      1.1,   0,     10,      0,    0.05,   0,    0.05 ]
warrior_stats = [10,  4,    1,        0,       0,      1.4,   0,      5,      1,    0.05,   0.05,  0.1 ]
wizard_stats =  [ 0,  0,    0,        4,       1,        0,  1.0,      5,      1,    0.05,   0.05, 0.05 ]

human_stats =   [10, 1.6,   0.5,     1.6,     0.3,     0.3,  0.3,     5,     0.5,     0,    0.05,    0 ]
dwarf_stats =   [20, 1.6,   0.3,       0,       0,     0.6,    0,    15,       0,     0,    0.05,    0 ]
elven_stats =   [ 0,   1,   0.1,       2,     0.5,     0.3,  0.6,    10,     0.5,   0.05,     0,  0.05 ]


# ------------------------------------------- Player Skills ------------------------------------------------------------------------
# Multipliers = Speed / Attack / Additional Critical Chance / Stamina or Mana Usage

ditch_attack = ["Ditch attack", 1, 0.6, 0, 0, "A weak attack that can be performed when low on stamina. "]  
last_reserve = ["Last reserve", 1, 0.6, 0, 0, "A weak spell that can be performed when low on mana. "]   
regroup = ["Regroup", 2, 0, 0, 0, "Step back from battle and try to evade attacks while you recover your full stamina. "]
focus = ["Focus", 2, 0, 0, 0, "Step back from battle and try to evade attacks while you recover your full mana. "]
precision_attack = ["Precision attack", 0.9, 0.6, 0, 2, "A weak and slow attack, but it never misses. "]
piercing_attack = ["Piercing attack", 1, 1, 0, 3, "A thrusting attack that negates enemy armour. "]
fireball = ["Fireball", 1, 1.2, 0, 3, "Sends out a ball of flame, to one enemy, that hits for good damage and a chance to burn."]

fury = ["Fury", 1, 1, 0, 3, "Harness the rage, and attack, while increasing your speed and power for two turns. "]
critical_targeting = ["Critical targeting", 1, 1, 0, 3, "Assess the enemy's weaknesses; allowing you to score critical hits for two turns. "]
heavy_blow = ["Heavy blow", 0.9, 1.2, 0.05, 3, "A heavy attack with a chance to knock your enemy down. "]


skills_able_to_learn = []                                                           # Skills your player can learn at current time
player_skills = []                                                                   # Skills your player has learned
stage = 1                                                                            # Keeps track of the stage the player is at



# A list of the items the player has equipped in different slots------------------------------------------------------------------------

# ---------------------Weapon-----Head --- Body --- Feet --- Ring -- Shield/Trinket/Catalyst   --------------
#                          0        1        2        3        4       5               
player_equiped_codes = [""        , ""     , "",     "",       "",     ""]
player_equipped = [
    [],     
    [], 
    [],
    [], 
    [], 
    []
    ]

# A list of equipable items that have been found by the player character, but not equipped or stored yet. (Empty to begin with) --- xqf called something different now?

found_item = {


}


# A list of equipable items that have been found by the player character and stored in the inventory

equipables_inventory = {


}







# ---------------- Character Sheet ---------------------------------------------------------------------------------------------------


def character_sheet():
    spacing = 28 - (len(player[0]) + len(player[24]) + len(player[25]))
    spacing2 = 16 - len(player[23])
    spacing3 = 16 - (len(str(player[1])) + len(str(player[2])))
    spacing4 = 3 - len(str(player[9]))
    spacing5 = 3 - len(str(player[11]))
    spacing6 = 2 - len(str(round(player[13] * 100)))
    spacing7 = 2 - len(str(round(player[15] * 100)))
    spacing8 = 2 - len(str(player_equipped[0][1]))
    spacing9 = 2 - len(str(player[14]))
    spacing10 = 2 - len(str(round(player[16]*0.375)))
    spacing11 = 2 - len(str(round(player[17]*0.375)))
    spacing12 = 2 - len(str(round(player[18]*0.375))) 
    spacing13 = 3 - len(str(round(player[21]*100)))
    spacing14 = 3 - len(str(round(player[22]*100)))
    print()
    print(" _____________________________________________________________________________________")
    print("|                                                                                     |")
    if player[24] == "Elf":
        print(f"| {player[0]} - An {player[24]} {player[25]}{spacing*' '}Trait: {player[23]}{spacing2*' '}                          |")
    else:
        print(f"| {player[0]} - A {player[24]} {player[25]} {spacing*' '}Trait: {player[23]}{spacing2*' '}                          |")
    print(f"|                                                             {player[26][0]} |")
    print(f"| Level: {player[1]}     EXP: {player[2]}{spacing3*' '}                           {player[26][1]} |")
    if player[9] != 0:
        print(f"|                                 Attack:               -  {round(player[9])}{spacing4*' '}{player[26][2]} |")
    if player[11] != 0:
        print(f"|                                 Magical Attack:       -  {round(player[11])}{spacing5*' '}{player[26][2]} |")
    if player[0] == "Immortal":
        print(f"| Max Health          - {player[3]}     - Weapon Power:     - {spacing8*' '}{round(player_equipped[0][1])}  {player[26][3]} |")    
    else:
        print(f"| Max Health          - {player[3]}         - Weapon Power:     - {spacing8*' '}{round(player_equipped[0][1])}  {player[26][3]} |")  
    if player[4] != 0:
        print(f"| Max Stamina         - {math.floor(player[4])}                                     {player[26][4]} |")
        print(f"| Stamina Regen Speed - {math.floor(player[5])}         Physical Defence:     - {spacing6*' '}{round(player[13] * 100) } %{player[26][5]} |")
    if player[6] != 0:
        print(f"| Max Mana            - {math.floor(player[6])}                                     {player[26][4]} |")
        print(f"| Mana Regen Speed    - {math.floor(player[7])}         Physical Defence:     - {spacing6*' '}{int(player[13] * 100)} %{player[26][5]} |")
    if player[8] != 0:
        print(f"| Strength            - {player[8]:.1f}         - Armour:           - {spacing9*' '}{round(player[14])}  {player[26][6]} |")
    if player[10] != 0:
        print(f"| Focus               - {player[10]:.1f}         - Armour:           - {spacing9*' '}{round(player[14])}  {player[26][6]} |")
    print(f"| Toughness           - {round(player[12])}                                    {player[26][7]} |")
    print(f"| Speed               - {player[19]:.1f}       Magical Defence:      - {spacing7*' '}{round(player[15] * 100)} %{player[26][8]} |")
    print(f"| Accuracy            - {round(player[20] * 100)} %       - Fire Resist:       - {spacing10*' '}{round(player[16]*0.375)} %{player[26][9]} |")
    print(f"| Evasion             - {round(player[21] * 100)} %  {spacing13*' '}    - Frost Resist:      - {spacing11*' '}{round(player[17]*0.375)} %{player[26][10]} |")
    print(f"| Critical Chance     - {round(player[22] * 100)} %  {spacing14*' '}    - Corruption Resist: - {spacing12*' '}{round(player[18]*0.375)} %                        |")
    print("|_____________________________________________________________________________________|")
    print("")
    print(player[0:26])        #  xqf remove after testing


# -------------------------------------------------- Makeshift Camp Area ---------------------------------------------------------------------------

def learn_skills(stage, reloaded):
    if (player[28]-len(player_skills)) < 1:
        print_s_c(f"Finello: “I'm sorry you have no ability to learn new skills now.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
        time.sleep(1)
        print()
    elif (player[28]-len(player_skills)) == 1:
        print_s_c(f"Finello: “Now lets see, you have the ability to learn another skill.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
        time.sleep(1)
        print()
    else:
        print_s_c(f"Finello: “Now lets see, you have the ability to learn {(player[28]-len(player_skills))} skills.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
        time.sleep(1)
        print()
    print_s_c("Finello: “Currently I can teach you one of the following skills:” ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    if stage == 1 and reloaded == False:
        skills_able_to_learn.append(precision_attack)                 
        if player[25] == "Wizard" and player[24] == "Dwarf":
            skills_able_to_learn.append(ditch_attack)
        elif  player[25] == "Wizard" and player[24] != "Dwarf":
            skills_able_to_learn.append(last_reserve)
            skills_able_to_learn.append(focus)
            skills_able_to_learn.append(fireball)
        elif player[25] == "Warrior" or player[25] == "Knight":
            skills_able_to_learn.append(ditch_attack)
            skills_able_to_learn.append(regroup)
            skills_able_to_learn.append(piercing_attack)
        if player[24] == "Dwarf":
            skills_able_to_learn.append(heavy_blow)
        elif player[24] == "Human":
            skills_able_to_learn.append(fury)
        elif player[24] == "Elf":
            skills_able_to_learn.append(critical_targeting)
    elif stage == 16 and reloaded == False:                             # Additional skills for later stages need adding --------------- xqf
        pass
    elif stage == 31 and reloaded == False:
        pass
    elif stage == 46 and reloaded == False:
        pass
    elif stage == 61 and reloaded == False:
        pass
    num = 1
    list = ""
    for skill in skills_able_to_learn:
        print_c(f"{str(num)}. {skill[0]} - Cost {str(skill[4])} {player[29]} - {skill[5]} ", color=Fore.WHITE, brightness=Style.BRIGHT)
        time.sleep(2)
        print()
        if num < len(skills_able_to_learn):
            list += str(num)
            list += ", "
        num += 1
    time.sleep(1)
    print()
    print_s_c("Finello: “Which skill would you like to learn?” ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    question = f"{list}or {len(skills_able_to_learn)}? "
    answer = input(question)
    print()
    if answer.isdigit() == True and 0 < int(answer) <= len(skills_able_to_learn):
        player_skills.append(skills_able_to_learn[int(answer)-1])
        print_c(f"{player[0]} learned the {skills_able_to_learn[int(answer)-1][0]} skill. ", color=Fore.YELLOW, brightness=Style.BRIGHT)   
        skills_able_to_learn.remove(skills_able_to_learn[int(answer)-1]) 
        print()
        time.sleep(1)
        
    else:
        print_s_c("Finello: “I didn't understand you there, let me repeat that.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
        time.sleep(1)
        print()
        learn_skills(stage, True)

    if len(player_skills) < player[28]:
        learn_skills(stage, True)

    else:
        print_s_c("Finello: “Okay that's all I can teach you for now.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
        time.sleep(1)
        print()


def makeshift_camp():
    time.sleep(2)
    print()
    print()
    print_c("  __  __       _             _     _  __ _      ____                      ", color=Fore.CYAN, brightness=Style.BRIGHT)
    print_c(" |  \/  | __ _| | _____  ___| |__ (_)/ _| |_   / ___|__ _ _ __ ___  _ __  ", color=Fore.CYAN, brightness=Style.BRIGHT)
    print_c(" | |\/| |/ _` | |/ / _ \/ __| '_ \| | |_| __| | |   / _` | '_ ` _ \| '_ \ ", color=Fore.CYAN, brightness=Style.BRIGHT)
    print_c(" | |  | | (_| |   <  __/\__ \ | | | |  _| |_  | |__| (_| | | | | | | |_) |", color=Fore.CYAN, brightness=Style.BRIGHT)
    print_c(" |_|  |_|\__,_|_|\_\___||___/_| |_|_|_|  \__|  \____\__,_|_| |_| |_| .__/ ", color=Fore.CYAN, brightness=Style.BRIGHT)
    print_c("                                                                   |_|    ", color=Fore.CYAN, brightness=Style.BRIGHT)
    time.sleep(2)
    print()
    print()
    time.sleep(2)
    print()
    print()
    print_s_c("The camp is little more than a couple of wooden shacks and several large tents. ", color=Fore.WHITE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("Most of these seem to be housing wounded soldiers and villagers. ", color=Fore.WHITE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("A lovely aroma seems to be coming from one tent, and you make a beeline for that. ", color=Fore.WHITE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("Upon entering; you see a friendly elf dishing out hot soup into wooden bowls. ", color=Fore.WHITE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("You take a bowl for yourself and wolf it down, not realising how hungry you were. ", color=Fore.WHITE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("After you're done, you thank the elf and ask if she knows a Carla. ", color=Fore.WHITE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("She points you in the direction of a stout dwarf sorting through items in the back of a cart. ", color=Fore.WHITE, brightness=Style.BRIGHT)
    time.sleep(2)
    print()
    print()
    print_s_c("You walk over and tap the distracted dwarf on the shoulder. ", color=Fore.WHITE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c(f"{player[0]}: “Excuse me are you Carla?” ", color=Fore.GREEN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("Carla: “Yeah that's me, whadya want? I'm busy here.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c(f"{player[0]}: “Sorry, Orlan said you might be able to help me out with a few items.” ", color=Fore.GREEN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("Carla: “Look. I don't know what Orlan said but I've been able to salvage very little.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("Carla: “And what I do have, I will need to sell to get back on my feet.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("Carla: “I suppose I can let you have these potions I found…” ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print()
    print_c(f"{player[0]} receives 3 * Small Health Potion", color=Fore.YELLOW, brightness=Style.BRIGHT)    # ----- Add this to potion inventory ------xqf
    print()
    time.sleep(1)
    print()
    print_s_c("Carla: “But you will have to check back later if you want anything more, and it'll cost ya.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("Carla: “Course if you find anything of use out in the wilds, I'd be happy to buy it from you.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c(f"{player[0]}: “Thank you; if I am back this way again I will trade with you.” ", color=Fore.GREEN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("Carla: “Well with any luck I will be able to get this cart back on the road soon.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("Carla: “Then I can bring my wares to you.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c(f"{player[0]}: “By the way, do you happen to know where I can find Finello?” ", color=Fore.GREEN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("Carla: “What that crazy old man, thinks he's some sort of sage?” ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("Carla: “Yeah he's by the stream collecting water.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("Carla: “Don't go believing his stories though; he would have to have lived twenty lifetimes for all he says to be true.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("And with that she turns back to sorting through her inventory. ", color=Fore.WHITE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("Leaving her to it; you head down towards the stream. ", color=Fore.WHITE, brightness=Style.BRIGHT)
    time.sleep(2)
    print()
    print()
    print_s_c("You see on old man with a walking stick, wearing a plain brown robe. ", color=Fore.WHITE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("He is knelt down by the river with his back towards you. ", color=Fore.WHITE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("As you approach; he suddenly leaps up and spins around, brandishing his stick like a spear. ", color=Fore.WHITE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    if player[1] == "Elf":
        print_s_c(f"Finello: “What is an {player[24]} like you doing sneaking up on an old man?” ", color=Fore.BLUE, brightness=Style.BRIGHT)
        time.sleep(1)          
        print()
    else:
        print_s_c(f"Finello: “What is a {player[24]} like you doing sneaking up on an old man?” ", color=Fore.BLUE, brightness=Style.BRIGHT)
        time.sleep(1)
        print()
    print_s_c(f"{player[0]}: “I'm sorry I didn't mean to startle you; Orlan said you wanted to speak with me?” ", color=Fore.GREEN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("He relaxes and rests on his walking stick.", color=Fore.WHITE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c(f"Finello: “Ah so you're the {player[25]} that got knocked out cold.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)                  
    print()
    if player[24] == "Dwarf" and player[25] == "Wizard":
        print_s_c("Finello: “But you're a Dwarf, you can't do magic!” ", color=Fore.BLUE, brightness=Style.BRIGHT)
        time.sleep(1)
        print()
        print_s_c("Finello: : “What are you going to do with that staff, whack people on the head with it?” ", color=Fore.BLUE, brightness=Style.BRIGHT)
        time.sleep(1)
        print()
        print_s_c("Finello: : “Oh never mind, I may still be able to teach you a skill or two if you like?” ", color=Fore.BLUE, brightness=Style.BRIGHT)
        time.sleep(1)
        print()
    else:
        print_s_c(f"Finello: “I used to be a {player[25]} myself back in the day.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
        time.sleep(1)               
        print()
        if player[25] == "Warrior":
            print_s_c("Finello: “I once sliced a troll's head clean off.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
            time.sleep(1)
            print()
        elif player[25] == "Knight":
            print_s_c("Finello: “I once held off a mountain lion with just my shield.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
            time.sleep(1)
            print()
        elif player[25] == "Wizard":
            print_s_c("Finello: “I once burned a whole horde of zombies to ash.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
            time.sleep(1)
            print()
        print_s_c("Finello: “I'm sure you're capable but I could teach you a skill or two if you like?” ", color=Fore.BLUE, brightness=Style.BRIGHT)
        time.sleep(1)
        print()

    print_s_c("Would you like to learn some skills? ", color=Fore.WHITE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    answer = input("Yes or No? ")
    if answer.lower() == "yes" or  answer.lower() == "y":
        print()
        learn_skills(stage, False)                                                      
    else:
        print()
        print_s("Are you sure? Learning skills will aid you in battle. ")
        print()
        print_s("Learn some skills? ")
        print()
        answer_1 = input("Yes or No? ")
        if answer_1.lower() == "yes" or  answer_1.lower() == "y":
            print()
            learn_skills(stage, False)
        else:
            print()
            print_s_c("Finello: “Well okay but don't come crying to me if things get tough.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
            time.sleep(1)
            print()

    print_s_c("Finello: “Good luck out there.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("You thank the old man and head back towards the main camp. ", color=Fore.WHITE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("From there you see the main road and begin to head towards it. ", color=Fore.WHITE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c(f"Orlan: “Hey {player[0]}! Where do you think your going?” ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c(f"{player[0]}: “Hey Orlan; this road leads to the main town, and then onto the volcano doesn't it?” ", color=Fore.GREEN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c(f"Orlan: “Yes but you can't just waltz up there plain as day.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c(f"Orlan: “The shadows up ahead become too dense, and anyone that walks through does not return.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c(f"Orlan: “The heroes that set off before you made their way up the forest path.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("He points off to a small path on the right that winds through the forest. ", color=Fore.WHITE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c(f"Orlan: “Now I'm not saying that way is safe, but you will have a better chance going that way.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c(f"Orlan: “Me and the others at the camp are going to gather as many people as we can and form a caravan.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c(f"Orlan: “We will push on down the main road as far as we can and hopefully meet you up ahead.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c(f"{player[0]}: “Okay Orlan; if you think that is best, I will follow your route.” ", color=Fore.GREEN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c(f"{player[0]}: “However don't push on down the road if the shadows become too much.” ", color=Fore.GREEN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c(f"{player[0]}: “Hopefully I will find a way to clear them, but if not don't lead your people into danger.” ", color=Fore.GREEN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c(f"Orlan: “We will do what we must, I see no other way of ever leaving the island.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c(f"{player[0]}: “Then just give me time enough to give you a fighting chance.” ", color=Fore.GREEN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c(f"Orlan: “That I can do, and I shall see you up ahead.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("He holds out his hand and you shake it firmly, before setting off towards the forest. ", color=Fore.WHITE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    time.sleep(2)
    print()
    print()
    time.sleep(2)
    print()
    print()
    print_c("  _____                   _     ", color=Fore.GREEN, brightness=Style.BRIGHT)
    print_c(" |  ___|__  _ __ ___  ___| |_   ", color=Fore.GREEN, brightness=Style.BRIGHT)
    print_c(" | |_ / _ \| '__/ _ \/ __| __|  ", color=Fore.GREEN, brightness=Style.BRIGHT)
    print_c(" |  _| (_) | | |  __/\__ \ |_   ", color=Fore.GREEN, brightness=Style.BRIGHT)
    print_c(" |_|  \___/|_|  \___||___/\__|  ", color=Fore.GREEN, brightness=Style.BRIGHT)
    time.sleep(2)
    print()
    print()
    time.sleep(2)
    print()
    print()



# -------------------------------------------------- Introduction ---------------------------------------------------------------------------

def intro_text():
    print()
    time.sleep(1)
    print_s_c("On the island state of Bracknell there was a great volcano, which had lain dormant for many centuries. ", color=Fore.CYAN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("That is until a month or so ago; when the volcano smouldered once more. ", color=Fore.CYAN, brightness=Style.BRIGHT)
    time.sleep(2)
    print()
    print()
    print_s_c("Many of the islanders, fearing a full eruption, began to evacuate. ", color=Fore.CYAN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("However orc raiders and bandits swarmed to the area, preying upon the islanders as they tried to flee with their belongings. ", color=Fore.CYAN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("Prince Torlan tried to bring calm to the area by ordering his soldiers to patrol the roads. ", color=Fore.CYAN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("Unfortunately for everyone this was no ordinary eruption… ", color=Fore.CYAN, brightness=Style.BRIGHT)
    time.sleep(2)
    print()
    print()
    print_s_c("As the ground shook, black smoke issued forth from the volcano's cauldron. ", color=Fore.CYAN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("Not high into the sky as you would expect, but pouring down the mountainside as if it was heavy as molten rock itself. ", color=Fore.CYAN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("The smoke enveloped the entire island, plunging the islanders into a shadow world of hazy darkness and fear. ", color=Fore.CYAN, brightness=Style.BRIGHT)
    time.sleep(2)
    print()
    print()
    print_s_c("Panic spread like wildfire, and the people began turning on each other. ", color=Fore.CYAN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("To make matters worse, stories began to emerge of giant golems wandering the mists, spreading the shadow wherever they went. ", color=Fore.CYAN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("As if seized by some corruption; the local wildlife began to attack anyone they came across. ", color=Fore.CYAN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("Even the orcs and bandits started to act crazy, being as likely to attack their own as an innocent traveller. ", color=Fore.CYAN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("As the population panicked and fled, Prince Torlan marched what remained of his army into the shadowlands... ", color=Fore.CYAN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("Right towards the heart of the volcano, hoping to restore order to the land. ", color=Fore.CYAN, brightness=Style.BRIGHT)
    time.sleep(3)
    print()
    print()
    print()
    print_s_c("That was a week ago, and nothing has been heard from him or his company since. ", color=Fore.CYAN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("The King, fearing for his son's life, sent out a call to any hero living in his domain; ", color=Fore.CYAN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("To come forth and travel to the island of Bracknell. ", color=Fore.CYAN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("Many, including you, answered the King's call, ", color=Fore.CYAN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("And you now find yourself travelling across the sea, on a ship with twenty or so compatriots. ", color=Fore.CYAN, brightness=Style.BRIGHT)
    time.sleep(2)
    print()
    print()
    print_s_c("As you begin to near the island however, you feel that something is wrong. ", color=Fore.CYAN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("You hear cries and yelling from the crew. ", color=Fore.CYAN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("You run up on deck to see what the commotion is about, and that is when you see it...", color=Fore.CYAN, brightness=Style.BRIGHT)
    time.sleep(2)
    print()
    print()
    print_s_c("The sea is jet black and appears to be boiling and bubbling. ", color=Fore.CYAN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("The ship can't seem to sail through it, and you can hear the strain in the wooden planks of the hull. ", color=Fore.CYAN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("All of a sudden there is a yell, and you look up to see a great wave of shadow and darkness rise up behind you. ", color=Fore.CYAN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("Acting on pure instinct; you dive from the ship into the murky waters below...", color=Fore.CYAN, brightness=Style.BRIGHT)
    time.sleep(2)
    print()
    print()
    print_s_c("There is a huge crash as the wave strikes the vessel, and the strained hull gives way. ", color=Fore.CYAN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("The ship splits in two, and begins to sink down into the water. ", color=Fore.CYAN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("Before you can think of what to do; a piece of driftwood slams into your temple and everything goes black. ", color=Fore.CYAN, brightness=Style.BRIGHT)
    time.sleep(2)
    print()
    print()
    time.sleep(2)
    print()
    print()
    time.sleep(2)
    print()
    print()
    print_c("   ▄████████    ▄█    █▄       ▄████████ ████████▄   ▄██████▄   ▄█     █▄          ▄████████    ▄████████    ▄████████  ▄█          ▄▄▄▄███▄▄▄▄   ", color=Fore.BLACK, brightness=Style.BRIGHT) 
    print_c("  ███    ███   ███    ███     ███    ███ ███   ▀███ ███    ███ ███     ███        ███    ███   ███    ███   ███    ███ ███        ▄██▀▀▀███▀▀▀██▄ ", color=Fore.BLACK, brightness=Style.BRIGHT) 
    print_c("  ███    █▀    ███    ███     ███    ███ ███    ███ ███    ███ ███     ███        ███    ███   ███    █▀    ███    ███ ███        ███   ███   ███ ", color=Fore.BLACK, brightness=Style.BRIGHT) 
    print_c("  ███         ▄███▄▄▄▄███▄▄   ███    ███ ███    ███ ███    ███ ███     ███       ▄███▄▄▄▄██▀  ▄███▄▄▄       ███    ███ ███        ███   ███   ███ ", color=Fore.BLACK, brightness=Style.BRIGHT) 
    print_c("▀███████████ ▀▀███▀▀▀▀███▀  ▀███████████ ███    ███ ███    ███ ███     ███      ▀▀███▀▀▀▀▀   ▀▀███▀▀▀     ▀███████████ ███        ███   ███   ███ ", color=Fore.BLACK, brightness=Style.BRIGHT) 
    print_c("         ███   ███    ███     ███    ███ ███    ███ ███    ███ ███     ███      ▀███████████   ███    █▄    ███    ███ ███        ███   ███   ███ ", color=Fore.RED, brightness=Style.BRIGHT) 
    print_c("   ▄█    ███   ███    ███     ███    ███ ███   ▄███ ███    ███ ███ ▄█▄ ███        ███    ███   ███    ███   ███    ███ ███▌    ▄  ███   ███   ███ ", color=Fore.RED, brightness=Style.BRIGHT) 
    print_c(" ▄████████▀    ███    █▀      ███    █▀  ████████▀   ▀██████▀   ▀███▀███▀         ███    ███   ██████████   ███    █▀  █████▄▄██   ▀█   ███   █▀  ", color=Fore.RED, brightness=Style.BRIGHT) 
    print_c("                                                                                  ███    ███                           ▀                          ", color=Fore.RED, brightness=Style.BRIGHT)
    time.sleep(2)
    print()
    print()
    time.sleep(2)
    print()
    print()
    time.sleep(2)
    print()
    print()
    print_s_c("You awaken to find yourself lying on a beach; a figure is stood over you. ", color=Fore.WHITE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("Orlan: “Ah so you're finally awake.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("He reaches out his hand, and when you grasp it, he pulls you to your feet. ", color=Fore.WHITE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c(f"{player[0]}: “What happened here?” ", color=Fore.GREEN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("Orlan: “Your ship tried to sail through that.” He points to the blackened sea. ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("Orlan: “Don't know what it is, but no ship can make it in or out anymore.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c(f"{player[0]}: “Did anyone else make it off the ship?” ", color=Fore.GREEN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("Orlan: “Ai a few made it to shore. They were in better shape than you, so they have already set off into the woods.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("Orlan: “Before you go gallivanting off, I suggest you head up to the campsite.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("Orlan: “It's not much, just a makeshift camp where most of the survivors are holed up.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("Orlan: “But you can get some food & drink, and Carla has been collecting supplies, she may have something for you.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("Orlan: “Also the old man Finello wishes to speak with you, something about making sure you're prepared.” ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c(f"{player[0]}: “Okay I'll do that, thanks… erm.” ", color=Fore.GREEN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("Orlan: “The name's Orlan; come and see me before you head off, and I'll give you the lay of the land” ", color=Fore.BLUE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c(f"{player[0]}: “Thanks Orlan, I will” ", color=Fore.GREEN, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    print_s_c("You turn and head towards the treeline, where the makeshift camp has been established. ", color=Fore.WHITE, brightness=Style.BRIGHT)
    time.sleep(1)
    print()
    makeshift_camp()
    

# ---------------- Character select functions ------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------

# ---------------- Happy with Character ------------------------------------------------------------------------------------------------------

def character_check():
    print()
    print_s("Here is your character sheet, look it over and press enter when ready. ")
    time.sleep(1)
    print()
    character_sheet()
    print()
    input()
    print_s("Are you happy with your character? If not select 'No' to restart. ")
    print()
    answer = input("Yes or No? ")
    if answer.lower() == "yes" or answer.lower() == "y":
        print()
        print()
        print()
        print()
        intro_text()
    elif answer.lower() == "no" or answer.lower() == "n":
        print()

        global player                    # ------------------------------- Better way than global for these variables? ----- xqf
        global per_level_stats
        global player_equiped_codes
        global player_equipped

        player = ["Player", 1 ,   0 ,  100 ,  0 ,    0 ,      0 ,      0 ,      0 ,    0   ,  0  ,    0     ,   5   ,    0   ,    0    ,  0    ,   0   ,    0  ,     0 ,     4.5  , 0.85 , 0.05 ,  0.05 ,  "None", "None", "None",   []]
        per_level_stats = [10, 0.2, 0.1, 0.2, 0.1, 0.15, 0.15, 2]
        player_equiped_codes = ["", "", "", "", "", ""] 
        player_equipped = [[], [], [], [], [], []]

        print(player)
        print(player_equiped_codes)
        intro_to_char()


    else:
        print()
        print_s("Sorry I didn't understand that")
        print()
        character_check()
    

# ----------------Basic Equipment Equip-----------------------------------------------------------------------------------------------------


def equip_basic_armour(code, slot_num):

    player_equiped_codes[slot_num] = code

    player[14] += player_equipped[slot_num][1]  #   these add on the new item's values onto the player values
    player[16] += player_equipped[slot_num][2]
    player[17] += player_equipped[slot_num][3]
    player[18] += player_equipped[slot_num][4]
    player[player_equipped[slot_num][6]] += player_equipped[slot_num][7]    # --------check [6] holds the variable not the string - been changed


    player[13] = round(((player[12] + (player[14]/2)) * 0.0025), 3)      #   these calculate the new Pys Def and Mag Def values based on the new Armour -
    player[15] = round(((player[12] + player[16] + player[17] + player[18]) * 0.00125), 3)

    player[9] = math.floor(player_equipped[0][1] * player[8])       #   these calculate the new attack/mag attack values based on the weapons Power stat
    player[11] = math.floor(player_equipped[0][1] * player[10])

def equip_basic_weapon(code):

    player_equiped_codes[0] = code

    player[9] = math.floor(player_equipped[0][1] * player[8])       #   these calculate the new attack/mag attack values based on the weapons Power stat
    player[11] = math.floor(player_equipped[0][1] * player[10])



# ----------------Which equipment equip check-----------------------------------------------------------------------------------------------------

def basic_equip_checker():

    if player[25] == "Wizard" and player[24] == "Dwarf":

        player_equipped[0] = ['Cracked Staff', 2] 
        equip_basic_weapon("W9001")
        player_equipped[1] = ['Battered Woven Sandals', 1, 1, 1, 1, 'None', 3, 0]
        equip_basic_armour("FW000", 1)
        player_equipped[2] = ['Battered Woven Robes', 3, 2, 2, 2, 'None', 3, 0]
        equip_basic_armour("BW000", 2)
        player_equipped[3] = ['Battered Woven Cowl', 2, 1, 1, 1, 'None', 3, 0]
        equip_basic_armour("HW000", 3)

    elif player[25] == "Wizard" and player[24] == "Human":
        
        player_equipped[0] = ['Cracked Wand', 3]
        equip_basic_weapon("W7001")
        player_equipped[1] = ['Battered Spellwoven Sandals', 1, 6, 6, 6, 'None', 3, 0]
        equip_basic_armour("FS000", 1)
        player_equipped[2] = ['Battered Spellwoven Robes', 3, 15, 15, 15, 'None', 3, 0]
        equip_basic_armour("BS000", 2)
        player_equipped[3] = ['Battered Spellwoven Cowl', 2, 9, 9, 9, 'None', 3, 0]
        equip_basic_armour("HS000", 3)
        player_equipped[5] = ['Catalyst', 0, 0, 0, 0, 'Focus', 10, 0.1]
        equip_basic_armour("C0021", 5)

    elif player[25] == "Wizard" and player[24] == "Elf":
        
        player_equipped[0] = ['Cracked Staff', 4]
        equip_basic_weapon("W8001")
        player_equipped[1] = ['Battered Spellwoven Sandals', 1, 6, 6, 6, 'None', 3, 0]
        equip_basic_armour("FS000", 1)
        player_equipped[2] = ['Battered Spellwoven Robes', 3, 15, 15, 15, 'None', 3, 0]
        equip_basic_armour("BS000", 2)
        player_equipped[3] = ['Battered Spellwoven Cowl', 2, 9, 9, 9, 'None', 3, 0]
        equip_basic_armour("HS000", 3)
        player_equipped[5] = ['Catalyst', 0, 0, 0, 0, 'Focus', 10, 0.1]
        equip_basic_armour("C0021", 5)

    elif player[25] == "Knight" and player[24] == "Dwarf":

        player_equipped[0] = ['Cracked Mace', 4]
        equip_basic_weapon("W6001")
        player_equipped[1] = ['Battered Iron-Plate Greaves', 6, 1, 1, 1, 'None', 3, 0]
        equip_basic_armour("FI000", 1)
        player_equipped[2] = ['Battered Iron-Plate Plackart', 15, 2, 2, 2, 'None', 3, 0]
        equip_basic_armour("BI000", 2)
        player_equipped[3] = ['Battered Iron-Plate Great-Helm', 9, 1, 1, 1, 'None', 3, 0]
        equip_basic_armour("HI000", 3)
        player_equipped[5] = ['Cracked Wooden Shield', 7, 1, 3, 4, 'None', 3, 0]
        equip_basic_armour("S0001", 5)

    elif player[25] == "Knight" and player[24] == "Human":

        player_equipped[0] = ['Cracked Axe', 3]
        equip_basic_weapon("W4001")
        player_equipped[1] = ['Battered Iron-Plate Greaves', 6, 1, 1, 1, 'None', 3, 0]
        equip_basic_armour("FI000", 1)
        player_equipped[2] = ['Battered Iron-Plate Plackart', 15, 2, 2, 2, 'None', 3, 0]
        equip_basic_armour("BI000", 2)
        player_equipped[3] = ['Battered Iron-Plate Great-Helm', 9, 1, 1, 1, 'None', 3, 0]
        equip_basic_armour("HI000", 3)
        player_equipped[5] = ['Cracked Wooden Shield', 7, 1, 3, 4, 'None', 3, 0]
        equip_basic_armour("S0001", 5)

    elif player[25] == "Knight" and player[24] == "Elf":

        player_equipped[0] = ['Cracked Sword', 3]
        equip_basic_weapon("W5001")
        player_equipped[1] = ['Battered Iron-Plate Greaves', 6, 1, 1, 1, 'None', 3, 0]
        equip_basic_armour("FI000", 1)
        player_equipped[2] = ['Battered Iron-Plate Plackart', 15, 2, 2, 2, 'None', 3, 0]
        equip_basic_armour("BI000", 2)
        player_equipped[3] = ['Battered Iron-Plate Great-Helm', 9, 1, 1, 1, 'None', 3, 0]
        equip_basic_armour("HI000", 3)
        player_equipped[5] = ['Cracked Wooden Shield', 7, 1, 3, 4, 'None', 3, 0]
        equip_basic_armour("S0001", 5)

    elif player[25] == "Warrior" and player[24] == "Dwarf":

        player_equipped[0] = ['Cracked Spear', 4]
        equip_basic_weapon("W3001")
        player_equipped[1] = ['Battered Leather Boots', 3, 2, 2, 2, 'None', 3, 0]
        equip_basic_armour("FL000", 1)
        player_equipped[2] = ['Battered Leather Curiass', 7, 5, 5, 5, 'None', 3, 0]
        equip_basic_armour("BL000", 2)
        player_equipped[3] = ['Battered Leather Helmet', 4, 3, 3, 3, 'None', 3, 0]
        equip_basic_armour("HL000", 3)
        player_equipped[5] = ['Trinket', 0, 0, 0, 0, 'Strength', 8, 0.1]
        equip_basic_armour("T0021", 5)

    elif player[25] == "Warrior" and player[24] == "Human":

        player_equipped[0] = ['Cracked Halberd', 5]
        equip_basic_weapon("W1001")
        player_equipped[1] = ['Battered Leather Boots', 3, 2, 2, 2, 'None', 3, 0]
        equip_basic_armour("FL000", 1)
        player_equipped[2] = ['Battered Leather Curiass', 7, 5, 5, 5, 'None', 3, 0]
        equip_basic_armour("BL000", 2)
        player_equipped[3] = ['Battered Leather Helmet', 4, 3, 3, 3, 'None', 3, 0]
        equip_basic_armour("HL000", 3)
        player_equipped[5] = ['Trinket', 0, 0, 0, 0, 'Strength', 8, 0.1]
        equip_basic_armour("T0021", 5)

    elif player[25] == "Warrior" and player[24] == "Elf":

        player_equipped[0] = ['Cracked Katana', 4]
        equip_basic_weapon("W2001")
        player_equipped[1] = ['Battered Leather Boots', 3, 2, 2, 2, 'None', 3, 0]
        equip_basic_armour("FL000", 1)
        player_equipped[2] = ['Battered Leather Curiass', 7, 5, 5, 5, 'None', 3, 0]
        equip_basic_armour("BL000", 2)
        player_equipped[3] = ['Battered Leather Helmet', 4, 3, 3, 3, 'None', 3, 0]
        equip_basic_armour("HL000", 3)
        player_equipped[5] = ['Trinket', 0, 0, 0, 0, 'Strength', 8, 0.1]
        equip_basic_armour("T0021", 5)



    character_check()



# ---------------- Trait Select -----------------------------------------------------------------------------------------------------------


def trait_select():
    print_s("Your hero can also have one of the following character traits:")
    print()
    print()
    time.sleep(2)
    print("A) None: There's really nothing special about you.")
    print()
    time.sleep(1.5)
    print("B) Slippery: No one can lay a finger on you.")
    print()
    time.sleep(1.5)
    print("C) Speedy Gonzales: You like to have the first say in each battle.")
    print()
    time.sleep(2)
    print("D) Tough as nails: Hammer away as they might, the enemy is unlikely to cause much damage.")
    print()
    time.sleep(2)
    if player[25] == "Wizard" and player[24] == "Dwarf":
        print("E) Brute: You are stronger than the average bear.")
        print()
        time.sleep(2)
        print("F) Rigorous Cardio: All that training has paid off, you barely get tired.")
        print()
        time.sleep(2)
        print_s("Press the following buttons to add the trait to your character")
        print()
        time.sleep(1.5)
        print("A) None,   B) Slippery,   C) Speedy Gonzales,   D) Tough as Nails,    E) Brute,   F) Rigorous Cardio")
        print()
        time.sleep(1.5)
        print("Or press G) to see the traits again")
        print()
        time.sleep(1.5)
        answer = input("Enter A, B, C, D, E, F, or G ")
        print()
        if answer.lower() == "a" or answer.lower() == "none":
            print("You have chosen no trait.")
            print()
            time.sleep(1.5)
            basic_equip_checker()
        elif answer.lower() == "b" or answer.lower() == "slippery":
            print('You have chosen the "Slippery" trait.')
            print()
            time.sleep(1.5)
            player[21] += 0.1
            player[23] = "Slippery"
            basic_equip_checker()
        elif answer.lower() == "c" or answer.lower() == "speedy gonzales" or answer.lower() == "speedy":
            print('You have chosen the "Speedy Gonzales" trait.')
            print()
            time.sleep(1.5)
            player[19] += 0.5
            player[23] = "Speedy Gonzales"
            basic_equip_checker()
        elif answer.lower() == "d" or answer.lower() == "tough as nails" or answer.lower() == "tough":
            print('You have chosen the "Tough as Nails" trait.')
            print()
            time.sleep(1.5)
            player[12] += 10
            player[23] = "Tough as Nails"
            basic_equip_checker()
        elif answer.lower() == "e" or answer.lower() == "brute":
            print('You have chosen the "Brute" trait.')
            print()
            time.sleep(1.5)
            player[8] += 0.3
            player[23] = "Brute"
            basic_equip_checker()
        elif answer.lower() == "f" or answer.lower() == "rigorous cardio" or answer.lower() == "cardio" or answer.lower() == "rigorous":
            print('You have chosen the "Rigorous Cardio" trait.')
            print()
            time.sleep(1.5)
            player[5] += 0.5
            player[23] = "Rigorous Cardio"
            basic_equip_checker()
        elif answer.lower() == "g" or answer.lower() == "traits":
            print()
            time.sleep(1.5)
            trait_select()
        else:
            print_s("I didn't recognise that, just enter the letter that corresponds to the trait you want.")
            print()
            time.sleep(1.5)
            trait_select()



    elif player[25] == "Wizard":
        print("E) Inate Magic: Your body is just in tune to the natural flow of mana.")
        print()
        time.sleep(2)
        print("F) Scholar: When it comes to magic, yours has that extra spark.")
        print()
        time.sleep(2)
        print_s("Press the following buttons to add the trait to your character")
        print()
        time.sleep(1.5)
        print("A) None,   B) Slippery,   C) Speedy Gonzales,   D) Tough as Nails,    E) Inate Magic,   F) Scholar ")
        print()
        time.sleep(1.5)
        print("Or press G) to see the traits again")
        print()
        time.sleep(1.5)
        answer = input("Enter A, B, C, D, E, F, or G ")
        print()
        if answer.lower() == "a" or answer.lower() == "none":
            print("You have chosen no trait.")
            print()
            time.sleep(1.5)
            basic_equip_checker()
        elif answer.lower() == "b" or answer.lower() == "slippery":
            print('You have chosen the "Slippery" trait.')
            print()
            time.sleep(1.5)
            player[21] += 0.1
            player[23] = "Slippery"
            basic_equip_checker()
        elif answer.lower() == "c" or answer.lower() == "speedy gonzales" or answer.lower() == "speedy":
            print('You have chosen the "Speedy Gonzales" trait.')
            print()
            time.sleep(1.5)
            player[19] += 0.5
            player[23] = "Speedy Gonzales"
            basic_equip_checker()
        elif answer.lower() == "d" or answer.lower() == "tough as nails" or answer.lower() == "tough":
            print('You have chosen the "Tough as Nails" trait.')
            print()
            time.sleep(1.5)
            player[12] += 10
            player[23] = "Tough as Nails"
            basic_equip_checker()
        elif answer.lower() == "e" or answer.lower() == "inate magic" or answer.lower() == "inate" or answer.lower() == "magic":
            print('You have chosen the "Inate Magic" trait.')
            print()
            time.sleep(1.5)
            player[7] += 0.5
            player[23] = "Inate Magic"
            basic_equip_checker()
        elif answer.lower() == "f" or answer.lower() == "scholar":
            print('You have chosen the "Scholar" trait.')
            print()
            time.sleep(1.5)
            player[10] += 0.3
            player[23] = "Scholar"
            basic_equip_checker()
        elif answer.lower() == "g" or answer.lower() == "traits":
            print()
            time.sleep(1.5)
            trait_select()
        else:
            print("I didn't recognise that, just enter the letter that corresponds to the trait you want.")
            print()
            time.sleep(1.5)
            trait_select()


    else:
        print("E) Brute: You are stronger than the average bear.")
        print()
        time.sleep(2)
        print("F) Rigorous Cardio: All that training has paid off, you barely get tired.")
        print()
        time.sleep(2)
        print_s("Press the following buttons to add the trait to your character")
        print()
        time.sleep(1.5)
        print("A) None,   B) Slippery,   C) Speedy Gonzales,   D) Tough as Nails,    E) Brute,   F) Rigorous Cardio")
        print()
        time.sleep(1.5)
        print("Or press G) to see the traits again")
        print()
        time.sleep(1.5)
        answer = input("Enter A, B, C, D, E, F, or G ")
        print()
        if answer.lower() == "a" or answer.lower() == "none":
            print("You have chosen no trait.")
            print()
            time.sleep(1.5)
            basic_equip_checker()
        elif answer.lower() == "b" or answer.lower() == "slippery":
            print('You have chosen the "Slippery" trait.')
            print()
            time.sleep(1.5)
            player[21] += 0.1
            player[23] = "Slippery"
            basic_equip_checker()
        elif answer.lower() == "c" or answer.lower() == "speedy gonazales" or answer.lower() == "speedy":
            print('You have chosen the "Speedy Gonzales" trait.')
            print()
            time.sleep(1.5)
            player[19] += 0.5
            player[23] = "Speedy Gonzales"
            basic_equip_checker()
        elif answer.lower() == "d" or answer.lower() == "tough as nails" or answer.lower() == "tough":
            print('You have chosen the "Tough as Nails" trait.')
            print()
            time.sleep(1.5)
            player[12] += 10
            player[23] = "Tough as Nails"
            basic_equip_checker()
        elif answer.lower() == "e" or answer.lower() == "brute":
            print('You have chosen the "Brute" trait.')
            print()
            time.sleep(1.5)
            player[8] += 0.3
            player[23] = "Brute"
            basic_equip_checker()
        elif answer.lower() == "f" or answer.lower() == "rigorous cardio" or answer.lower() == "cardio" or answer.lower() == "rigorous":
            print('You have chosen the "Rigorous Cardio" trait.')
            print()
            time.sleep(1.5)
            player[5] += 0.5
            player[23] = "Rigorous Cardio"
            basic_equip_checker()
        elif answer.lower() == "g" or answer.lower() == "traits":
            print()
            time.sleep(1.5)
            trait_select()
        else:
            print_s("I didn't recognise that, just enter the letter that corresponds to the trait you want.")
            print()
            time.sleep(1.5)
            trait_select()




# ---------------- Dwarf Check --------------------------------------------------------------------------------------------------------

def dwarf_check():
    print_s("A dwarf can't use magic, they will make a bad wizard")
    print()
    time.sleep(0.8)
    print_s("Are you sure you wouldn't rather be a different class?")
    print()
    time.sleep(0.8) 
    answer = input("Change your class? Y/N ")
    print()
    if answer.lower() == "y" or answer.lower() == "yes":
        print("A wise decision.")
        print()
        class_select()
    elif answer.lower() == "n" or answer.lower() == "no":
        times = 0
        while times < 3:
            print_s("No seriously, the game will be really difficult if you continue.")
            print()
            time.sleep(0.8) 
            answer = input("Change your class? Y/N ")
            print()
            if answer.lower() == "y" or answer.lower() == "yes":
                print_s("A wise decision.")
                print()
                class_select()
            elif answer.lower() == "n" or answer.lower() == "no":
                times += 1
            else:
                print_s("I'm going to assume your backing out of that bad decision.")
                print()
                class_select()


        print_s("Okay then, if you insist.")
        print()
        time.sleep(0.8)
        print_s(f"{player[0]} is a Crazy Dwarf Wizard.")
        print()
        time.sleep(0.8)
        player[4] = 3
        player[5] = 1
        player[6] = 0
        player[7] = 0
        player[8] = 0.8
        player[10] = 0
        player[12] = 20
        player[19] = 5
        player[20] = 0.9
        player[21] = 0.05
        player[22] = 0
        player[25] = "Wizard"
        player[26] =  dwarf_wizard_image[:]
        player[30] = 9
        player[29] = "Stamina"

        per_level_stats[3] = 0
        per_level_stats[4] = 0
        per_level_stats[6] = 0

        trait_select()

    else:
        print_s("I'm going to assume your backing out of that bad decision.")
        print()
        class_select()




# ---------------- Class Select --------------------------------------------------------------------------------------------------------

def class_select():
    print_s(f"So what class is {player[0]} going to be?")
    print()
    time.sleep(0.8) 
    # print("Warrior:")   ------------------------------------------xqf xqf uncomment this when doen testing
    # print()
    # print()
    # time.sleep(1)
    # print_s("Warriors are fast, agile and hit with high damage.")
    # print()
    # time.sleep(2.5)
    # print_s("They weild two handed weapons and wear a trinket around their necks.")
    # print()
    # time.sleep(2.5)
    # print_s("They wear light armour that offers a mix of protection and movement.")
    # print()
    # time.sleep(2.5)
    # print("Knight:")
    # print()
    # print()
    # time.sleep(1)
    # print_s("Knights are slow to move, hit for medium damage, but are extremely sturdy.")
    # print()
    # time.sleep(2.5)
    # print_s("They weild a one handed weapon with a shield.")
    # print()
    # time.sleep(2.5)
    # print_s("They wear heavy armour that is high in defence, but suffers in movement.")
    # print()
    # time.sleep(2.5)
    # print("Wizard:")
    # print()
    # print()
    # time.sleep(1)
    # print_s("Wizards are not the hardiest of folk, but they make up for it with powerful spells.")
    # print()
    # time.sleep(2.5)
    # print_s("They weild staffs or wands, along with a magical catalyst.")
    # print()
    # time.sleep(2.5)
    # print_s("They wear robes that offer scant physical, but great magical protection.")
    # print()
    # time.sleep(2.5)
    print()
    print_s("Which class would you like to play as?")
    print()
    time.sleep(0.8)
    player_class = input("A) Warrior, B) Knight or C) Wizard? ")
    print()

    if player_class.lower() == "a" or player_class.lower() == "warrior":
        print_s(f"Ah so {player[0]} is a Warrior.")
        print()
        time.sleep(0.8)
        player[3] += warrior_stats[0]
        player[4] += warrior_stats[1]
        player[5] += warrior_stats[2]
        player[6] = 0
        player[7] = 0
        player[8] += warrior_stats[5]
        player[10] = 0
        player[12] += warrior_stats[7]
        player[19] += warrior_stats[8]
        player[20] += warrior_stats[9]
        player[21] += warrior_stats[10]
        player[22] += warrior_stats[11]
        player[25] = "Warrior"
        if player[24] == "Human":
            player[26] =  human_warrior_image[:]
            player[30] = 1
        elif player[24] == "Elf":
            player[26] =  elf_warrior_image[:]
            player[30] = 2
        elif player[24] == "Dwarf":
            player[26] =  dwarf_warrior_image[:]
            player[30] = 3
        player[29] = "Stamina"

        per_level_stats[3] = 0
        per_level_stats[4] = 0
        per_level_stats[6] = 0

        trait_select()

    elif player_class.lower() == "b" or player_class.lower() == "knight" or player_class.lower() == "k":
        print_s(f"Ah so {player[0]} is a Knight.")
        print()
        time.sleep(0.8)
        player[3] += knight_stats[0]
        player[4] += knight_stats[1]
        player[5] += knight_stats[2]
        player[6] = 0
        player[7] = 0
        player[8] += knight_stats[5]
        player[10] = 0
        player[12] += knight_stats[7]
        player[19] += knight_stats[8]
        player[20] += knight_stats[9]
        player[21] += knight_stats[10]
        player[22] += knight_stats[11]
        player[25] = "Knight"
        if player[24] == "Human":
            player[26] =  human_knight_image[:]
            player[30] = 5
        elif player[24] == "Elf":
            player[26] =  elf_knight_image[:]
            player[30] = 6
        elif player[24] == "Dwarf":
            player[26] =  dwarf_knight_image[:]
            player[30] = 7
        player[29] = "Stamina"

        per_level_stats[3] = 0
        per_level_stats[4] = 0
        per_level_stats[6] = 0

        trait_select()

    elif player_class.lower() == "c" or player_class.lower() == "wizard":
        
        if player[24] == "Dwarf":
            dwarf_check()

        else:
            print_s(f"Ah so {player[0]} is a Wizard.")
            print()
            time.sleep(0.8)
            player[3] += wizard_stats[0]
            player[4] = 0
            player[5] = 0
            player[6] += wizard_stats[3]
            player[7] += wizard_stats[4]
            player[8] = 0
            player[10] += wizard_stats[6]
            player[12] += wizard_stats[7]
            player[19] += wizard_stats[8]
            player[20] += wizard_stats[9]
            player[21] += wizard_stats[10]
            player[22] += wizard_stats[11]
            player[25] = "Wizard"
            if player[24] == "Human":
                player[26] =  human_wizard_image[:]
                player[30] = 7
            elif player[24] == "Elf":
                player[26] =  elf_wizard_image[:]
                player[30] = 8
            player[29] = "Mana"
        

            per_level_stats[1] = 0
            per_level_stats[2] = 0
            per_level_stats[5] = 0

            trait_select()
        

    elif player_class.lower() == "w":
        print_s("I'm sorry I don't know whether you mean Warrior or Wizard, lets look at the classes again:")
        print()
        time.sleep(0.8)
        class_select()

    
    else:
        print_s("I'm sorry I didn't understand that, lets look at the classes again:")
        print()
        time.sleep(0.8)
        class_select()



# ---------------- Race Select --------------------------------------------------------------------------------------------------------

def race_select():
    print()
    print_s(f"{player[0]} can be one of three races:")
    print()
    time.sleep(0.8)
    # print("Human:")       xqf uncomment after tests
    # print()
    # print()
    # time.sleep(1)
    # print_s("Humans are quick and sturdy, they excel as warriors, but make decent wizards also.")
    # print()
    # time.sleep(2.5)
    # print("Dwarf:")
    # print()
    # print()
    # time.sleep(1)
    # print_s("Dwarves are strong and tough, they make brilliant knights, but cannot use magic.")
    # print()
    # time.sleep(2.5)
    # print("Elf:")
    # print()
    # print()
    # time.sleep(1)
    # print_s("Elves are natural magic users, but their speed and accuracy can also make them good warriors.")
    # print()
    # time.sleep(2.5)
    print()
    print_s("Which race would you like to play as?")
    print()
    time.sleep(0.8)
    player_race = input("A) Human, B) Dwarf or C) Elf? ")
    print()

    if player_race.lower() == "a" or player_race.lower() == "human" or player_race.lower() == "h":
        print_s(f"Ah so {player[0]} is a Human.")
        print()
        time.sleep(0.8)
        player[3] += human_stats[0]
        player[4] += human_stats[1]
        player[5] += human_stats[2]
        player[6] += human_stats[3]
        player[7] += human_stats[4]
        player[8] += human_stats[5]
        player[10] += human_stats[6]
        player[12] += human_stats[7]
        player[19] += human_stats[8]
        player[20] += human_stats[9]
        player[21] += human_stats[10]
        player[22] += human_stats[11]
        player[24] = "Human"
        class_select()

    elif player_race.lower() == "b" or player_race.lower() == "dwarf" or player_race.lower() == "d":
        print_s(f"Ah so {player[0]} is a Dwarf.")
        print()
        time.sleep(0.8)
        player[3] += dwarf_stats[0]
        player[4] += dwarf_stats[1]
        player[5] += dwarf_stats[2]
        player[6] += dwarf_stats[3]
        player[7] += dwarf_stats[4]
        player[8] += dwarf_stats[5]
        player[10] += dwarf_stats[6]
        player[12] += dwarf_stats[7]
        player[19] += dwarf_stats[8]
        player[20] += dwarf_stats[9]
        player[21] += dwarf_stats[10]
        player[22] += dwarf_stats[11]
        player[24] = "Dwarf"
        class_select()

    elif player_race.lower() == "c" or player_race.lower() == "elf" or player_race.lower() == "e":
        print_s(f"Ah so {player[0]} is an Elf.")
        print()
        time.sleep(0.8)
        player[3] += elven_stats[0]
        player[4] += elven_stats[1]
        player[5] += elven_stats[2]
        player[6] += elven_stats[3]
        player[7] += elven_stats[4]
        player[8] += elven_stats[5]
        player[10] += elven_stats[6]
        player[12] += elven_stats[7]
        player[19] += elven_stats[8]
        player[20] += elven_stats[9]
        player[21] += elven_stats[10]
        player[22] += elven_stats[11]
        player[24] = "Elf"
        class_select()

    
    else:
        print_s("I'm sorry I didn't understand that, lets look at the races again:")
        print()
        time.sleep(0.8)
        race_select()


# ---------------------- Intro ----------------------------------------------------------------------------------------------------------------

def intro_to_char():
    print()
    print_s("Welcome to Shadow Realm.")
    print()
    time.sleep(0.8)
    print_s("Before you enter its murky depths...")
    print()
    time.sleep(0.8)
    player[0] = input("What is your characters name? ")
    print()
    time.sleep(0.8)
    if len(player[0]) > 12:
        print("I'm sorry but your name cannot be more than 12 characters long")
        print()
        time.sleep(0.8) 
        intro_to_char()
    elif player[0] == "Immortal":
        print_s("Immortal huh?")
        print()
        time.sleep(0.8)
        print_s("If you say so...")
        print()
        time.sleep(0.8)
        player[3] = 1000000
        race_select()
    else:
        print_s(f"{player[0]}, is that right?")
        print()
        time.sleep(0.8)
        answer = input("Yes or No? ")
        print()
        time.sleep(0.8)
        if answer.lower() == "yes" or answer.lower() == "y":
            race_select()
        else:
            print_s("Oh then lets try this again.")
            print()
            intro_to_char()

intro_to_char()
