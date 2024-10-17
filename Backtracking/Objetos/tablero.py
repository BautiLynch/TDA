from Objetos.barco import Barco


class Tablero():

    def __init__(self, tamaño, valores_horizontales, valores_verticales):
        if len(valores_horizontales) != len(valores_verticales) != tamaño:
            raise Exception("Parametros invalidos")
        self.tablero = self._crear_tablero(tamaño)
        self.valores_horizontales = valores_horizontales
        self.valores_verticales = valores_verticales

    def _crear_tablero(self, tamaño):
        tablero = []
        for i in range(tamaño):
            linea = [0] * tamaño
            tablero.append(linea)
        return tablero
    
    def insertar_barco_vertical(self, barco: Barco, posicion) -> bool:
        (pos_v, pos_h) = (posicion[0], posicion[1])
        if self._el_barco_se_pasa_del_tablero(pos_v , barco):
            return False
        if self._hay_otro_barco_abajo(pos_v, pos_h, barco):
            return False
        if self._hay_otro_barco_arriba(pos_v, pos_h, barco):
            return False
        for i in range(pos_v, pos_v + barco.length()):
            if self._el_casillero_esta_vacio(i, pos_h):
                return False
            if self._casilla_a_la_izquierda_esta_ocupada(i, pos_h):
                return False
            if self._casilla_a_la_derecha_esta_ocupada(i, pos_h):
                return False
        
        for i in range(pos_v, pos_v + barco.length()):
            self.tablero[i][pos_h] = 1
        return True

    
    def _el_casillero_esta_vacio(self, pos_v: int, pos_h: int) -> bool:
        return self.tablero[pos_v][pos_h] != 0
    
    def _casilla_a_la_izquierda_esta_ocupada(self, pos_v: int, pos_h: int) -> bool:
        if pos_h <= 0:
            return False
        return self.tablero[pos_v][pos_h - 1] != 0

    def _casilla_a_la_derecha_esta_ocupada(self, pos_v: int, pos_h: int) -> bool:
        if pos_h >= len(self.tablero) - 1:
            return False
        return self.tablero[pos_v][pos_h + 1] != 0
    
    def _el_barco_se_pasa_del_tablero(self, pos_v: int, barco: Barco) -> bool:
        return pos_v + barco.length() > len(self.tablero)

    def _hay_otro_barco_abajo(self, pos_v: int, pos_h: int, barco: Barco):
        if pos_v + barco.length() >= len(self.tablero):
            return False
        if self.tablero[pos_v + barco.length()][pos_h] != 0:
            return True
        if pos_h + 1 < len(self.tablero) and self.tablero[pos_v + barco.length()][pos_h + 1] != 0:
            return True
        if pos_h - 1 > 0 and self.tablero[pos_v + barco.length()][pos_h - 1] != 0:
            return True
        return False
    
    def _hay_otro_barco_arriba(self, pos_v: int, pos_h: int, barco: Barco):
        if pos_v <= 0:
            return False
        if self.tablero[pos_v - 1][pos_h] != 0:
            return True
        if pos_h + 1  < len(self.tablero) and self.tablero[pos_v - 1][pos_h + 1] != 0:
            return True
        if pos_h - 1 > 0 and self.tablero[pos_v - 1][pos_h - 1] != 0:
            return True
        return False
    
    def comparar_tableros(self, tablero) -> bool:
        if len(tablero) != len(self.tablero):
            return False
        for i in range(len(tablero)):
            if len(tablero[i]) != len(self.tablero[i]):
                return False
            for j in range(len(tablero[i])):
                if tablero[i][j] != self.tablero[i][j]:
                    return False
        return True