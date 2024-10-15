class Tablero():

    def __init__(self, tamaño, valores_horizontales, valores_verticales):
        if len(valores_horizontales) != len(valores_verticales) != tamaño:
            raise Exception("Parametros invalidos")
        self.tablero = self._crear_tablero(tamaño)
        self.valores_horizontales = valores_horizontales
        self.valores_verticales = valores_verticales

    def _crear_tablero(tamaño):
        tablero = []
        for i in range(tamaño):
            linea = [0] * tamaño
            tablero.insert(linea)
        return tablero
    
    def insertar_barco_vertical(self, barco, posicion):
        (pos_h, pos_v) = (posicion[0], posicion[1])

        if no_entra_en_vertical(barco, posicion):
        # if pos_h != 0 and self.tablero[pos_v][pos_h - 1] != 0:
        #     return False
        # if pos_h != len(self.tablero) and self.tablero[pos_v][pos_h + barco.length] != 0:
        #     return False
        # # Checkeo de superposición
        # for i in range(barco.length):
        #     # Checkeo de superposición
        #     if self.tablero[pos_v][pos_h + i] != 0:
        #         return False
        #     # Checkeo de bounds
        #     if pos_v != 0 and self.tablero[pos_v - 1][pos_h + i] != 0:
        #         return False
        #     if pos_v != len(self.tablero) and self.tablero[pos_v + 1][pos_h + i] != 0:
        #         return False
    
    def _es_valido():