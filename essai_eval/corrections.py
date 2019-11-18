
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

class Exercice:

    def __init__(this, fonc, args):
        this.exercice = ExerciseFunction(fonc, args, layout='pprint', layout_args=(40, 25, 25))

    def exemples(this):
        return this.exercice.example(20)

    def tests(this, fonc):
        return this.exercice.correction(fonc)
        
        
def exemples(this):
    this.example(10)

exercice_somme = Exercice(
    lambda liste: sum(liste),
    [
        Args([1, 2, 3]),
        Args([4, 0, 6, 10]),
        Args([]) 
    ])


exercice_moyenne = Exercice(
    lambda liste : sum(liste) / len(liste),
    [
        Args([8, 2, 0, 10]),
        Args([10, 12, 14]),
        Args([6, 6, 6, 6, 6, 6]),
    ])

exercice_minimum = Exercice(
    lambda liste : min(liste),
    [
        Args([7, 3, 5, 4]),
        Args([10]),
        Args([5, 8, 4]),
        Args([2, 15, 30, 10, 19]),
    ])

exercice_cubes = Exercice(
    lambda n : [i**3 for i in range(n + 1)],
    [
        Args(0),
        Args(2),
        Args(4),
    ])

def trouver_index(obj, listeObjets):
    try:
        return listeObjets.index(obj)
    except ValueError:
        return -1
    
exercice_index = Exercice(
    trouver_index,
    [
        Args("A", ["B", "A", "C"]),
        Args(8, [4, 5, 6, 12, 8]),
        Args(3.14, [3.14, 1.41, 2.78]),
        Args(6, [2, 3, 5, 7]),
    ])

def bulle(listeNombres):
    for i in range(len(listeNombres) - 1):
        if listeNombres[i] > listeNombres[i + 1]:
            temp = listeNombres[i]
            listeNombres[i] = listeNombres[i + 1]
            listeNombres[i + 1] = temp
    return listeNombres

exercice_bulle = Exercice(
    bulle,
    [
        Args([2, 6, 8, 7]),
        Args([3, 1, 4]),
        Args([5, 3, 1, 6, 2]),
        Args([]),
    ])

def insertion(n, listeNombres):
    i = 0
    while i < len(listeNombres) and n > listeNombres[i]:
        i = i + 1
    listeNombres.insert(i, n)
    return listeNombres

exercice_insertion = Exercice(
    insertion,
    [
        Args(5, []),
        Args(3, [4, 6]),
        Args(7, [1, 6, 8, 11]),
        Args(9, [1, 3, 7]),
    ])


