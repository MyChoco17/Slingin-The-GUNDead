from pygame import *
from TexturesAndSounds import *
from csv import *
from PlayerChar import *
from importlib import *
from GameLoop import Game_Loop

# This is my Main Menu, where it'll ask for user input on whether the player would like to go to the game or to go to the scoreboards 
# My game variables will go here
def Main_Menu():
    global Game_Run, Game_Over_Run, SB_Menu, Menu_Run
    Menu_Background_Music()
    while Menu_Run == True:
        FPS_Clock.tick(FPS)
        Display.blit(Menu_Background, (0,0))
        Display.blit(Menu_Logo, (129,15))
        Display.blit(Load_To_Game_Text, (129, 520))
        Display.blit(Load_To_Scoreboard_Text, (45, 630))
        for events in event.get():   
            if events.type == KEYUP:
                if  events.key == K_RETURN: # This breaks the main menu loop, and enters the game loop to start playing, have fun!
                    mixer_music.stop()
                    Game_Run = True
                    Game_Over_Run = True
                    Menu_Run = False
                    Game_Loop()
                elif events.key == K_SPACE: # This blits over the main menu, and displays the scoreboard, from the scoreboardmenu() function
                    SB_Menu = True
                    ScoreBoardMenu()
            elif events.type == QUIT: # Quits the game from x button
                Menu_Run = False
                exit()
        try:
            display.update()
        except:
            error
        pass

# This function allows me to read the scoreboards' CSV file
def ReadScoreboard():
    with open('Scoreboard.csv', 'r') as File:
        Read = DictReader(File)
        Score = list(Read)
        return Score
# This function allows me to write my score into the scoreboards' CSV file
def WriteScoreboard(Score):
    with open('Scoreboard.csv', 'w', newline='') as File:
        NameAndScore = ['Name', 'Score'] # This creates a list to my CSV file with the name and score
        Write = DictWriter(File, fieldnames= NameAndScore)
        Write.writeheader()
        Write.writerows(Score)
# This function refreshes the scoreboard each time its called, sorting it from the highest score to the smallest, and only keeping the 10 biggest scores
def Update_Scoreboard():
    global Scoreboard_Text
    Score = ReadScoreboard()
    Score.sort(key=lambda x: int(x['Score']), reverse=True) # This sorts the list from biggest to smallest
    for i, player in enumerate(Score[:10]): #This returns the first 10 highest scores from the CSV file and renders the font and displays it into the screen
        Scoreboard_Text = font_for_text.render(f"{i + 1}) {player['Name']}: {player['Score']}", True, (0,0,0))
        Display.blit(Scoreboard_Text, (300, 200 + (i * 30)))
    Score = Score[:10]

# This is my scoreboard menu, that appears if the player has clicked the Space bar in the main menu
def ScoreBoardMenu():
    # The function below opens the CSV file and returns the scores
    ReadScoreboard()
    global SB_Menu, Scoreboard_Text, Menu_Run, Game_Run, Game_Over_Run
    while SB_Menu:
        FPS_Clock.tick(FPS)
        Display.blit(ScoreBoard_Background, (0,0))
        Display.blit(Load_To_Menu_Text, (85,560))
        # The function below is mainly called to display the scores onto the screen by calling on Display.blit at the end of the function
        Update_Scoreboard()
        for SBEvents in event.get():
            if SBEvents.type == QUIT: # This quits the game
                Menu_Run = False
                Game_Run = False
                Game_Over_Run = False
                SB_Menu = False
                quit()
            if SBEvents.type == KEYUP: # This exits the Scoreboard menu, back to the main menu
                 if SBEvents.key == K_ESCAPE:
                    SB_Menu = False
        try:
            display.update()
        except:
            error


def Get_Name(): # This is just used to get the player's name and saves it to the scoreboard when the game over function begins
    player_name = input("Type your name: ")
    return player_name
x = 0
def Game_Over(): # This is my Game Over menu, where it will ask for user input on whether the player would like to return to the menu or quit
    global Game_Over_Run, Menu_Run, Game_Run, player, x
    mixer_music.stop()
    while Game_Over_Run == True:
        FPS_Clock.tick(FPS)
        Display.blit(Game_Over_Screen, (0,0))
        Display.blit(Game_Over_Text, (150,65))
        Display.blit(Thanks_For_Playing_Text, (114, 275))
        Display.blit(Exit_Game_Text, (134, 390))
        if x == 0: # I did x == 0 because if I didnt, it would constantly ask for the players name, rather than just asking once, due to it being in a while loop
            player_name = Get_Name()
            player_score = player.score
            ScoreAchieved = ReadScoreboard()
            ScoreAchieved.append({'Name': player_name, 'Score': player_score}) # This saves the player name and score 
            Update_Scoreboard()
            WriteScoreboard(ScoreAchieved) # This writes whatever was appended into 'scores' to the CSV file
            mixer.Sound.play(WompWomp) # Sad Trombone
        for GMEvents in event.get():
            if GMEvents.type == QUIT:
                Game_Over_Run = False
                quit()
            elif GMEvents.type == KEYUP:
                # Pressing the Enter key will end the game, Thank you for playing!
                if GMEvents.key == K_RETURN:
                    Game_Run = False
                    Menu_Run = False
                    Game_Over_Run = False
                    exit()
        x += 1 # This exists so that the function to ask for the player name does not infinitely loop
        if x > 1:
            x = 1
        try:
            display.update()
        except:
            error
        pass