#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# write 'hello world' to the console
print('hello world')

import random

# Define las opciones del juego
opciones = ["rock", "paper", "scissors"]

# Inicializa la puntuación del jugador
puntuacion_jugador = 0

# Bucle principal del juego
while True:
    # Pide al jugador que elija una opción
    jugada_jugador = input("Elige una opción: rock, paper o scissors: ").lower()

    # Valida la entrada del jugador
    if jugada_jugador not in opciones:
        print("Opción no válida.")
        continue

    # Elige una opción aleatoria para el equipo
    jugada_equipo = random.choice(opciones)

    # Determina el ganador
    if jugada_jugador == "rock" and jugada_equipo == "scissors":
        print("Ganaste!")
        puntuacion_jugador += 1
    elif jugada_jugador == "scissors" and jugada_equipo == "paper":
        print("Ganaste!")
        puntuacion_jugador += 1
    elif jugada_jugador == "paper" and jugada_equipo == "rock":
        print("Ganaste!")
        puntuacion_jugador += 1
    else:
        print("Perdiste!")

    # Pregunta al jugador si quiere jugar de nuevo
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (y/n): ").lower()
    if jugar_de_nuevo != "y":
        break

# Imprime la puntuación final del jugador
print("Tu puntuación final es:", puntuacion_jugador)

