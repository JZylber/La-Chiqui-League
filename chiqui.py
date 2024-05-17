import random
import math
from scipy.stats import poisson, binom

class Equipo:
    def __init__(self, nombre, ataque, defensa):
        self.nombre = nombre
        self.puntos = 0
        self.goles_favor = 0
        self.goles_contra = 0
        self.ataque = ataque
        self.defensa = defensa

def simular_liga(equipos):
    partidos = [(equipo1, equipo2) for equipo1 in equipos for equipo2 in equipos if equipo1 != equipo2]
    
    for equipo1, equipo2 in partidos:
        goles_equipo1, goles_equipo2 = simular_partido(equipo1, equipo2)
        
        equipo1.goles_favor += goles_equipo1
        equipo1.goles_contra += goles_equipo2
        equipo2.goles_favor += goles_equipo2
        equipo2.goles_contra += goles_equipo1
        
        if goles_equipo1 > goles_equipo2:
            equipo1.puntos += 3
        elif goles_equipo2 > goles_equipo1:
            equipo2.puntos += 3
        else:
            equipo1.puntos += 1
            equipo2.puntos += 1

    tabla = [(equipo.nombre, equipo.puntos, equipo.goles_favor, equipo.goles_contra) for equipo in equipos]
    tabla_ordenada = ordenar_tabla(tabla)
    return tabla_ordenada

if __name__ == "__main__":
    equipos = [
        Equipo("River", 0.9, 0.8),
        Equipo("Boca", 0.6, 0.7),
        Equipo("Independiente", 0.7, 0.6),
        Equipo("San Lorenzo", 0.9, 0.9),
        Equipo("Racing", 0.4, 0.3),
        Equipo("Manchester City", 0.7, 0.8),
        Equipo("Manchester united", 0.7, 0.6),
        Equipo("Liverpool", 0.5, 0.6),
        Equipo("Arsenal", 0.4, 0.5),
        Equipo("Chelsea", 0.7, 0.5),
        Equipo("Real Madrid", 0.9, 0.7),
        Equipo("Barcelona", 0.8, 0.7),
        Equipo("Atletico Madrid", 0.5, 0.9),
        Equipo("Bayrn Munich", 0.8, 0.7),
        Equipo("Borussia Dortmund", 0.6, 0.7),
        Equipo("Inter", 0.7, 0.7),
        Equipo("Milan", 0.9, 0.7),
        Equipo("Juventus", 0.7, 0.7),
        Equipo("Ajax", 0.7, 0.8),
        Equipo("Porto", 0.8, 0.8),
    ]

    tabla_posiciones = simular_liga(equipos)
    imprimir_tabla_posiciones=(tabla_posiciones)


def validar_equipo(equipo):
    assert (type(equipo) == tuple or type(equipo) == list) and len(equipo)== 3, f"El equipo debe ser una lista o tupla de 3 elementos, no {equipo}"
    _, pA, pB  = equipo
    assert 0 < pA < 1, f"La probabilidad de ataque debe ser un número entre 0 y 1, sin incluirlos, no {pA}"
    assert 0 < pB < 1, f"La probabilidad de defensa debe ser un número entre 0 y 1, sin incluirlos, no {pB}"

def validar_equipos(equipos):
    for equipo in equipos:
        validar_equipo(equipo)

def plambda(ataque, defensa):
    if ataque > defensa:
        return 0.5 + 4.5 * (ataque - defensa)
    else:
        return 0.5 + (ataque - defensa)/2
    
def simular_partido(equipoA, equipoB):
    validar_equipos([equipoA, equipoB])
    _, ataqueA, defensaA = equipoA
    _, ataqueB, defensaB = equipoB
    lambdaA = plambda(ataqueA, defensaB)
    lambdaB = plambda(ataqueB, defensaA)
    golesA = poisson.rvs(lambdaA, size=1)[0]
    golesB = poisson.rvs(lambdaB, size=1)[0]
    return golesA, golesB

def orden_en_tabla(equipo):
    _, puntos, GF, GC = equipo
    return puntos, GF - GC, GF

def ordenar_tabla(tabla):
    return sorted(tabla, key=orden_en_tabla, reverse=True)

def imprimir_tabla_posiciones(tabla):
    print("Tabla de Posiciones:")
    print("--------------------")
    print("{:<20} {:<8} {:<8} {:<8}".format("Equipo", "Puntos", "GF", "GC"))
    print("--------------------")
    for equipo in tabla:
        print("{:<20} {:<8} {:<8} {:<8}".format(equipo[0], equipo[1], equipo[2], equipo[3]))
    print("--------------------")