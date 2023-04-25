import random
import math
from scipy.stats import poisson, binom

# Estas 2 funciones son para que les tire mejores errores cuando se mandan alguna
def validar_equipo(equipo):
    assert (type(equipo) == tuple or type(equipo) == list) and len(equipo)== 3, f"El equipo debe ser una lista o tupla de 3 elementos, no {equipo}"
    nombre,pA,pB  = equipo
    assert 0 < pA < 1, f"La probabilidad de ataque debe ser un número entre 0 y 1, sin incluirlos, no {pA}"
    assert 0 < pB < 1, f"La probabilidad de defensa debe ser un número entre 0 y 1, sin incluirlos, no {pB}"

def validar_equipos(equipos):
    for equipo in equipos:
        validar_equipo(equipo)

def plambda(ataque, defensa):
    if ataque > defensa:
        # 0.5 - 5
        return 0.5 + 4.5 * (ataque - defensa)
    else:
        # 0 - 0.5
        return 0.5 + (ataque - defensa)/2

def simular_partido(equipoA, equipoB):
    validar_equipos([equipoA, equipoB])
    _,ataqueA,defensaA = equipoA
    _,ataqueB,defensaB = equipoB
    lambdaA = plambda(ataqueA, defensaB)
    lambdaB = plambda(ataqueB, defensaA)
    golesA = poisson.rvs(lambdaA, size=1)[0]
    golesB = poisson.rvs(lambdaB, size=1)[0]
    return golesA, golesB

def penales(equipoA,equipoB, cantidad = 5):
    validar_equipos([equipoA, equipoB])
    golesA = 0
    golesB = 0
    _,ataqueA,defensaA = equipoA
    _,ataqueB,defensaB = equipoB
    golesA = binom.rvs(cantidad, 1 - defensaB/4 - (1 - ataqueA/1)/4 , size=1)[0]
    golesB = binom.rvs(cantidad, 1 - defensaA/4 - (1 - ataqueB/1)/4 , size=1)[0]
    return golesA, golesB

def orden_en_tabla(equipo):
    nombre,puntos,GF,GC = equipo
    return puntos, GF-GC, GF

def ordenar_tabla(tabla):
    return sorted(tabla, key=orden_en_tabla, reverse=True)

