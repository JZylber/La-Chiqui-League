import random
import math
from scipy.stats import poisson, binom

equipos = (
    ("River", 0.9, 0.8),
    ("Boca", 0.6, 0.7),
    ("Independiente", 0.7, 0.6),
    ("San Lorenzo", 0.9, 0.9),
    ("Racing", 0.4, 0.3),
    ("Manchester City", 0.7, 0.8),
    ("Manchester united", 0.7, 0.6),
    ("Liverpool", 0.5, 0.6),
    ("Arsenal", 0.4, 0.5),
    ("Chelsea", 0.7, 0.5),
    ("Real Madrid", 0.9, 0.7),
    ("Barcelona", 0.8, 0.7),
    ("Atletico Madrid", 0.5, 0.9),
    ("Bayrn Munich", 0.8, 0.7),
    ("Borussia Dortmund", 0.6, 0.7),
    ("Inter", 0.7, 0.7),
    ("Milan", 0.9, 0.7),
    ("Juventus", 0.7, 0.7),
    ("Ajax", 0.7, 0.8),
    ("Porto", 0.8, 0.8),
)
Tabla_pos = [{'equipo': equipo, 'ptos' : 0, 'gf': 0, 'gc': 0} for equipo, gf, gc in equipos]
llave = [{'equipo': equipo} for equipo in equipos]

def simular_liga(equipos):  
    n = 1
    i = 0
    while i < len(equipos):
        while n < len(equipos):
            golesA, golesB = simular_partido(equipos[i], equipos[n])
            if golesA > golesB:
                Tabla_pos[i]['ptos'] += 3
            
            if golesA < golesB:
                Tabla_pos[n]['ptos'] +=3
            else:
                Tabla_pos[i]['ptos'] +=1
                Tabla_pos[n]['ptos'] +=1
            
            Tabla_pos[i]['gf'] += golesA
            Tabla_pos[i]['gc'] += golesB
            
            Tabla_pos[n]['gf'] += golesA
            Tabla_pos[n]['gc'] += golesB
            n +=1
        i += 1
        n = 0 
    for equipo in Tabla_pos:
        print(f"Equipo: {equipo['equipo']}, Puntos:{equipo['ptos']} GF: {equipo['gf']}, GC: {equipo['gc']}")

def simular_llave(equipos):
    n = 1
    i = 0
    while i < len(equipos):
        while n < len(equipos):
            golesA, golesB = simular_partido(equipos[i], equipos[n])
            if golesA > golesB: 
                llave.remove(llave[i])
                for a in llave:
                    print(llave[a])
            elif golesA < golesB:
                llave.remove(llave[n])
                for a in llave:
                    print(llave[a])
            else: 
                while golesA == golesB:
                    golesA, golesB = penales(equipos[i], equipos[n])
                    if golesA > golesB: 
                        llave.remove(llave[i])
                        for a in llave:
                            print(llave[a])
                    elif golesA < golesB:
                        llave.remove(llave[n])
                        for a in llave:
                            print(llave[a])
            n += 1
        i = 0
        n = 0
    for equipo in Tabla_pos:
        print(f"Equipo: {equipo['equipo']}, Puntos: {equipo['ptos']}, GF: {equipo['gf']}, GC {equipo['gc']}")
    
                
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

def penales(equipoA, equipoB, cantidad = 5):
    validar_equipos([equipoA, equipoB])
    _,ataqueA,defensaA = equipoA
    _,ataqueB,defensaB = equipoB
    golesA = binom.rvs(cantidad, 1 - defensaB/4 - (1 - ataqueA/1)/4, size=1)[0]
    golesB = binom.rvs(cantidad, 1 - defensaA/4 - (1 - ataqueB/1)/4, size=1)[0]
    return golesA, golesB

def orden_en_tabla(equipo):
    _, puntos, GF, GC = equipo
    return puntos, GF - GC, GF

def ordenar_tabla(tabla):
    return sorted(tabla, key=orden_en_tabla, reverse=True)

simular_llave(equipos)