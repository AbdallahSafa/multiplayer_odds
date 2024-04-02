from socket import socket, AF_INET, SOCK_STREAM
from _thread import *
from game import Game
import pickle
server = "10.124.47.186"
port = 5555
s = socket(AF_INET, SOCK_STREAM)

try:
    s.bind((server, port))
except error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")
games = dict()
connected = set()
idCount = 0


def threaded_client(conn, p, gameID):
    global idCount
    conn.send(str.encode(str(p)))
    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()
            if gameID in games:
                game = games[gameID]
                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data == "challenger0" or data == "challenger1":
                        game.whoisChallenger(data)
                    elif data[-1] == 'D':
                        game.setDare(data[:-1])
                    elif data[-1] == 'O':
                        game.setOdds(data[:-1])
                    elif data[-1] == 'G':
                        game.setGuess(data[0], data[1:-1])
                    elif data != "get":
                        game.play(p, data)
                    reply = game
                    conn.sendall(pickle.dumps(reply))
            else:
                break
        except:
            break
    print("Lost connection")
    try:
        del games[gameID]
        print("Closing Game", gameID)
    except:
        pass
    idCount -= 1
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    idCount += 1
    p = 0
    gameID = (idCount - 1)//2
    if idCount % 2 == 1:
        games[gameID] = Game(gameID)
        print("Creating a new game...")
    else:
        games[gameID].ready = True
        p = 1
    start_new_thread(threaded_client, (conn, p, gameID))
