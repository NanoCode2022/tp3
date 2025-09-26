class Envio:
    def __init__(self, cod,des,nom,tasa,monto,algcomision,algimpositivo ):
        self.cod = cod
        self.des = des
        self.nom = nom
        self.tasa = tasa
        self.monto = monto
        self.algcomision = algcomision
        self.algimpositivo = algimpositivo

    def mon_env(self):
        return self.cod.strip().split("|")[0].zfill(2)

    def mon_pago(self):
        return self.cod.strip().split("|")[1].zfill(2)

    def cod_pag(self):
        return self.cod.split("|")[2]
