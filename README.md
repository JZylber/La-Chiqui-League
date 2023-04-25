# La oficina del Chiqui

## Instalación

Para correr el tp, necesitamos una librería de estadística para simular los partidos. Se instala con:

```bash
pip install --user scipy
```

## Objetivo

El Chiqui nos pidio analizar distintos sistemas de competencia en el fútbol. En particular, nos interesa comparar un sistema de liga (todos contra todos) contra un sistema de llaves por eliminación. Para esto, vamos a armar funciones que simulen cada tipo de torneo, y vamos a armar experimentos que testeen hipótesis sobre cada tipo.

## Equipos

A los equipos los vamos a modelar con dos números entre 0 y 1, que van representar su ataque y defensa respectivamente. A mayor número, mejor el ataque o defensa. Los equipos entonces van a ser tuplas o listas con 3 elementos: el nombre, la probabilidad de ataque y la probabilidad de defensa. Por ejemplo
```python
("Deportivo Riestra",0.6,0.4)
```

## Partidos

Para simular los partidos, yo les voy a proveer dos funciones que son probabilísticas.
- `simular_partido`: Toma 2 equipos y devuelve el resultado en goles (basado en los ataques y defensas)
- `penales`: Toma 2 equipos y devuelve el resultado en goles (basado en los ataques y defensas) de patear 5 penales por equipo. Opcionalmente, se le puede pasar un tercer parámetro, `cantidad`, que es la cantidad de penales por equipo.

## Liga

En una liga, todos los equipos juegan con todos los otros 1 sola vez (sin vuelta). Los partidos se juegan con la función `simular_partido`. Suman 3 puntos si ganan, 1 si empatan y 0 si pierden. El campeón es quien al final de todos los partidos, tiene más puntos. Si hay dos con igual cantidad de puntos, gana el que mayor diferencia de goles (```golesMetidos - golesRecibidos```) y si perisiste el empate, quien tiene más. Hay una función auxiliar que les puede ayudar a determinar el campeón de un torneo. Las tablas de un torneo tienen la forma:

| Nombre | Puntos | Goles a Favor | Goles en Contra |
| --- | --- | --- | --- |
| River | 27 | 26 | 10 |
| Argentinos Jrs. | 26 | 25 | 14 |
| Barracas Central | 26 | 20 | 15 |
| ... | ... | ... | ... |

Que en python lo vamos a representar como lista de listas. Pueden usar otras estructuras, pero al momento de llamar la función `ordenar_tabla` debe ser una lista de listas.

## Llaves

Asumiendo que la cantidad de equipos es una potencia de 2 (4,8,16,32,etc), se realizan partidos de a pares de equipos, en donde se determina un ganador que pasa a la siguiente ronda. Esto se repite hasta llegar a un único equipo, que es el ganador. Como en cada partido no puede haber empate, se define de la siguiente manera:

1. Se simulan el partido con `simular_partido`.
2. Si no hay un ganador, se juegan una ronda de penales. Una ronda son 5 penales por equipo usando la función `penales`.
3. Si sigue sin haber un ganador, se va un penal por eliminación, es decir, 1 penal por equipo hasta que se defina un ganador. Se puede usar la función `penales` con `cantidad = 1`.

## Consigna

### Parte A: Por el 6

Realizar una función que, dado un conjunto de equipos, simule un campeonato de liga siguiendo las indicaciones descritas anteriormente, y devuelva la tabla de resultados **ordenada por puntaje**. Hay funciones para ordenar una tabla de posiciones. Probar que funcione.

### Parte B: Por el 8

Realizar una función que, dado un conjunto de equipos, simule un campeonato de llaves siguiendo las indicaciones descritas anteriormente, y devuelva **el equipo ganador**. Probar que funcione.

### Parte C: Por el 9

Ahora, hagamos la copa de liga argentina, que es una mezcla de los dos sistemas. Funciona de la siguiente forma:

1. Se hacen 2 grupos de 14 equipos, en donde juegan todos contra todos 1 partido (igual que la Parte A)
2. El top 4 de cada grupo juega luego un torneo de llaves por eliminación. Quien juega contra quien está determinado por el orden en que salieron en las mini ligas.

Obviamente pueden (y se espera) que reutilicen las funciones de la parte A y B. Probar que funcione. Para más información, **Googleen**.

### Parte D: Por el 10

Para llegar al 10, tiene que hacer una parte de experimentación, más *a lo chona*. Para esto, hay que dejar los `.py` y moverse a notebooks, osea, `.ipynb`.

Antes de arrancar, planteense algunas hipótesis. Algunas preguntas orientadoras: ¿Qué esperan que pase en cada sistema? ¿Quiénes son los que ganan más seguido? ¿Como afectan ataque y defensa en los partidos y torneos?

Corran los sistemas reiteradas veces (más de 100), y con equipos apropiados para la hipótesis planteada. Registren lo observado, y vean que ocurrió con sus hipótesis.

**Tienen que registrar la experimentación**. La experimentación se debe registrar como bloques markdown del notebook, y deben estar si o si:
- Hipótesis de que creen que va a pasar (no hace falta que sea súper formal, alcanza con que digan que creen que va a pasar).
- Observaciones contrastadas con lo esperado. 

Realizar **al menos** 3 experimentos distintos.

## Entrega
La entrega se hace pusheando al repositorio creado por github classroom, y enviando el hash del commit en una entrega del campus.

## Evaluación
Se va a evaluar por código funcional y legible para otras personas. **Hay reentrega**. En la reentrega pueden corregir y agregar partes. La nota depende de lo que hayan llegado a hacer:
- 6: Parte A
- 8: Partes A y B
- 9: Partes A, B y C
- 10: Partes A, B, C y D