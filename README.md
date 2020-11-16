# SNAKE-LADDER GAME
- [SNAKE-LADDER GAME](#snake-ladder-game)
    + [Introduction:](#introduction-)
    + [Requirements](#requirements)
    + [Installation](#installation)
    + [Configuration](#configuration)
    + [Run program](#run-program)
    + [Customization](#customization)


### Introduction:
> This is a Command Line version of traditional Snake Ladder Game.
### Requirements
- Python 3+
- Git 2+
### Installation
- Clone the repository to your local directory using "git clone" command using any command line terminal.
- Install pip manager if your system doesn't have it using following command.
````
 python get-pip.py
````
- Install pyinstaller package using pip if your system doesn't have it using following command.
````
pip install pyinstaller
````
- Then using following any one of these commands create executable files.
````
// To create single executable file
pyinstaller --onefile SnakeLadder.py
// OR
// To create directory with executable files and it's supporting files
pyinstaller SnakeLadder.py
```` 
### Configuration
- Copy **testcases** directory where your main executable (**/dist/SnakeLadder**) file relies
### Run program
- Run executable file which is in dist/SnakeLadder directory. It will start game.
### Customization
- If you want to customize Snake Ladder board's Snakes & Ladders positions and it's numbers change .txt files contents which is inside testcases folder/directory in following manner :
1. Number of snakes (s) followed by s lines each containing 2 numbers denoting the head and tail positions of the snake.
2. Number of ladders (l) followed by l lines each containing 2 numbers denoting the start and end positions of the ladder.
3. Number of players (p) followed by p lines each containing a name.
