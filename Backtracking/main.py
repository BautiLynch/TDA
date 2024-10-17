from Objetos.barco import Barco
from Objetos.tablero import Tablero


def test01():
    tablero: Tablero = Tablero(3, [1,1,1], [1,1,1])
    assert(tablero != None)
    print("TEST 01 PASO")

def test02():
    tablero: Tablero = Tablero(3, [1,1,1],[1,1,1])
    barco: Barco = Barco(2)
    tablero.insertar_barco_vertical(barco, (0,0))
    tablero_esperado = [
        [1,0,0],
        [1,0,0],
        [0,0,0]
    ]
    assert(tablero.comparar_tableros(tablero_esperado))
    print("TEST 02 PASO")

def test03():
    tablero: Tablero = Tablero(3, [1,1,1], [1,1,1])
    barco: Barco = Barco(2)
    tablero.insertar_barco_vertical(barco, (1,0))
    tablero_esperado = [
        [0,0,0],
        [1,0,0],
        [1,0,0]
    ]
    assert(tablero.comparar_tableros(tablero_esperado))
    print("TEST 03 PASO")

def test04():
    tablero: Tablero = Tablero(3, [1,1,1], [1,1,1])
    barco: Barco = Barco(2)
    assert(not tablero.insertar_barco_vertical(barco,(2,0)))
    print("TEST 04 PASO")

def test05():
    tablero: Tablero = Tablero(3,[1,1,1], [1,1,1])
    barco1: Barco = Barco(2)
    barco2: Barco = Barco(2)
    tablero.insertar_barco_vertical(barco1, (0,0))
    assert(not tablero.insertar_barco_vertical(barco2, (1,0)))
    tablero_esperado = [
        [1,0,0],
        [1,0,0],
        [0,0,0]
    ]
    assert(tablero.comparar_tableros(tablero_esperado))
    print("TEST 05 PASO")

def test06():
    tablero: Tablero = Tablero(4,[1,1,1,1], [1,1,1,1])
    barco1: Barco = Barco(3)
    barco2: Barco = Barco(3)
    tablero.insertar_barco_vertical(barco1, (0,0))
    assert(not tablero.insertar_barco_vertical(barco2, (0,1)))
    tablero_esperado = [
        [1,0,0,0],
        [1,0,0,0],
        [1,0,0,0],
        [0,0,0,0],
    ]
    assert(tablero.comparar_tableros(tablero_esperado))
    print("TEST 06 PASO")

def test07():
    tablero: Tablero = Tablero(4,[1,1,1,1], [1,1,1,1])
    barco1: Barco = Barco(3)
    barco2: Barco = Barco(3)
    tablero.insertar_barco_vertical(barco1, (0,2))
    assert(not tablero.insertar_barco_vertical(barco2, (0,3)))
    tablero_esperado = [
        [0,0,1,0],
        [0,0,1,0],
        [0,0,1,0],
        [0,0,0,0],
    ]
    assert(tablero.comparar_tableros(tablero_esperado))
    print("TEST 07 PASO")

def test08():
    tablero: Tablero = Tablero(5,[1,1,1,1,1], [1,1,1,1,1])
    barco1: Barco = Barco(2)
    barco2: Barco = Barco(2)
    tablero.insertar_barco_vertical(barco1, (2,1))
    assert(not tablero.insertar_barco_vertical(barco2, (0,1)))
    tablero_esperado = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,1,0,0,0],
        [0,1,0,0,0],
        [0,0,0,0,0],
    ]
    assert(tablero.comparar_tableros(tablero_esperado))
    print("TEST 08 PASO")

def test09():
    tablero: Tablero = Tablero(5,[1,1,1,1,1], [1,1,1,1,1])
    barco1: Barco = Barco(2)
    barco2: Barco = Barco(2)
    tablero.insertar_barco_vertical(barco1, (0,1))
    assert(not tablero.insertar_barco_vertical(barco2, (2,1)))
    tablero_esperado = [
        [0,1,0,0,0],
        [0,1,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
    ]
    assert(tablero.comparar_tableros(tablero_esperado))
    print("TEST 09 PASO")

def test10():
    tablero: Tablero = Tablero(5,[2,2,2,2,2], [2,2,2,2,2])
    barco1: Barco = Barco(3)
    barco2: Barco = Barco(4)
    tablero.insertar_barco_vertical(barco1, (0,1))
    tablero.insertar_barco_vertical(barco2, (1,3))
    tablero_esperado = [
        [0,1,0,0,0],
        [0,1,0,1,0],
        [0,1,0,1,0],
        [0,0,0,1,0],
        [0,0,0,1,0],
    ]
    assert(tablero.comparar_tableros(tablero_esperado))
    print("TEST 10 PASO")

def test11():
    tablero: Tablero = Tablero(6, [2,2,2,2,2,2], [2,2,2,2,2,2])
    barco1: Barco = Barco(2)
    barco2: Barco = Barco(2)
    tablero.insertar_barco_vertical(barco1,(2,3))
    assert(not tablero.insertar_barco_vertical(barco2,(0,2)))
    assert(not tablero.insertar_barco_vertical(barco2, (0,4)))
    assert(not tablero.insertar_barco_vertical(barco2, (4,2)))
    assert(not tablero.insertar_barco_vertical(barco2, (4,4)))
    tablero_esperado = [
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,1,0,0],
        [0,0,0,1,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
    ]
    assert(tablero.comparar_tableros(tablero_esperado))
    print("TEST 11 PASO")

def tests():
    test01()
    test02()
    test03()
    test04()
    test05()
    test06()
    test07()
    test08()
    test09()
    test10()
    test11()

def main():
    tests()
    return

main()