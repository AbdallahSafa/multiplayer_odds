# Odds Game
- STILL WIP

<img width="699" alt="image" src="https://github.com/AbdallahSafa/multiplayer_odds/assets/95765787/83224d85-27be-4589-88dc-d3811a45e41a">
<img width="400" alt="image" src="https://github.com/AbdallahSafa/multiplayer_odds/assets/95765787/9a94f9f8-dae3-4410-8cb8-2bcaf3818c80">
<img width="400" alt="image" src="https://github.com/AbdallahSafa/multiplayer_odds/assets/95765787/205521ca-ca6f-472d-bed6-b0e810f23298">

## Description
This is a Python-based implementation of the game "Odds". In this game, two players challenge each other to perform a dare, with the odds of having to do the dare themselves being agreed upon. The players then type a number within the agreed range. If they typed the same number, the player who was issued the challenge has to do the dare.

## Technologies Used
- Python: The game logic and networking is implemented in Python.
- Pygame: Pygame is used for the graphical user interface of the game.
- Socket: Python's built-in socket library is used for networking to allow the game to be played over a network.
- Pickle: Python's built-in pickle module is used for serializing and deserializing Python object structures. It's used in this project to send game data over the network between the server and the client.

## How to Play
1. Run the server script on a machine. Ensure the server variable is set to a local ip address.
2. Run the client script on two different machines (or different instances on the same machine). These will be the players.
3. On the client, click on the "DARE" button to issue a challenge.
4. The game will then proceed as per the rules of "Odds".

## Project Structure
- `server.py`: This script sets up the server and handles incoming connections from clients.
- `client.py`: This script sets up the client-side application and handles the game's GUI.
- `game.py`: This script contains the `Game` class, which encapsulates the game logic.
- `network.py`: This script contains the `Network` class, which handles the network communication between the server and the client.

## Future Improvements
- Implement a better system for handling multiple games simultaneously.
- Improve the graphical user interface for a better user experience.
- Add more error handling for network errors and disconnections.

## License
This project is licensed under the terms of the MIT license.
