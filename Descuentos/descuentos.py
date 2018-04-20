# coding=utf-8

class Descuentos:
    def get_descuento(self, monto):
        if monto > 5000:
            return monto * .3
        elif  monto > 3000:
            return monto * .2
        elif monto > 1000:
            return monto * .1
        else:
            return 0