# coding=utf-8

class Promedios:
    def get_status(self, cal1, cal2, cal3):
        promedio = (cal1 + cal2 + cal3) / 3

        if promedio > 6:
            return "Aprobado"
        else:
            return "Reprobado"