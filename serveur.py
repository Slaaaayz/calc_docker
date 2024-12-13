import socket
from os import environ

CALC_PORT = environ.get("CALC_PORT")
CALC_PORT = CALC_PORT if CALC_PORT is not None else 6767

print(CALC_PORT)

try:
    CALC_PORT = int(CALC_PORT)
except ValueError:
    print(f"Erreur : La valeur de CALC_PORT '{CALC_PORT}' n'est pas un entier valide.")
    exit(1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Liaison sur le port configuré
s.bind(('0.0.0.0', CALC_PORT))

s.listen(1)
conn, addr = s.accept()
print(f"Connexion acceptée depuis {addr}")

while True:
    try:
        # On reçoit la string "Hello" du client
        data = conn.recv(1024)
        if not data:
            break
        print(f"Données reçues du client : {data.decode()}")

        conn.send("Hello".encode())

        # On reçoit le calcul du client
        data = conn.recv(1024)
        data = data.decode().strip("\n")

        # Évaluation et envoi du résultat
        res = eval(data)
        conn.send(str(res).encode())

    except socket.error:
        print("Erreur de socket.")
        break

conn.close()
