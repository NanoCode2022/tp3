from os import read

from clase import *




def cargar_envios():
    v_envios = []
    cont = 0
    m = open("envios.csv","rt")
    for elem in m:
        s = elem.split(",")
        envio = Envio(s[0],s[1],s[2],s[3],s[4],s[5],s[6])
        v_envios.append(envio)
        mon = s[0].split("|")
        if mon[0] != mon[1]:
            cont += 1

    contador = len(v_envios)
    print("cantidad de envios: ",contador)
    print(f"cantidad de envios donde la moneda de origen es distinta a la de pago: {cont}")

    return v_envios

def mostrar_resultado(v):
    cant = 0
    por_total = 0
    may = 0
    cod_may = ""
    mf_may = 0
    for i in v:
        mb, por = comision_alg(i)
        cant += 1
        por_total += por
        mf, imp = comision_imp(mb,i)
        if por + imp > may:
            cod_may = Envio.cod_pag(i)
            mf_may = mf

    # 2.1
    print(f"porcentaje promedio de comisiones: {por_total//cant}")
    # 2.2
    print(f"Codigo de pago del mayor descuento por impuestos y comision: {cod_may}")
    # 2.3
    print(f"Monto final del mayor descuento por impuesto y comisiones: {mf_may}")



def comision_alg(i):
    mon_env = Envio.mon_env(i)
    alg = int(i.algcomision)
    nom = int(i.monto)
    com = 0
    monto_fijo = 0
    monto_base = 0
    if alg == 1:
        if mon_env == "01":
            com = (nom * 9) // 100
            monto_base = nom - com
    elif alg == 2:
        if mon_env == "02":
            if nom < 50000:
                com = 0
            elif nom >= 50000 and nom <= 80000:
                com = (nom * 5) // 100
            elif nom >= 80000:
                com = (nom * 7.8) // 100
            monto_base = nom - com
    elif alg == 3:
        if mon_env == "03" or mon_env == "04":
            monto_fijo = 100
            if nom > 25000:

                com = (nom * 6) // 100
            monto_base = nom - (com + monto_fijo)
    elif alg == 4:
        if mon_env == "05":
            if nom <= 100000:
                com = 500
            elif nom > 100000:
                com = 1000
            monto_base = nom - com
    elif alg == 5:
        if mon_env == "01":
            if nom < 500000:
                com = 0
            elif nom >= 500000:
                com = (nom * 7) // 100
                if com >= 50000:
                    com = 50000
    por = ((com + monto_fijo) * 100) // nom
    return monto_base, por

def comision_imp(m, i):
    im = int(i.algimpositivo)
    mf = 0
    imp = 0
    if im == 1:
        if m <= 300000:
            imp = 0
        elif m > 300000:
            exc = m - 300000
            imp = (exc * 25) // 100
        mf = m - imp
    elif im == 2:
        if m < 50000:
            imp = 50
        elif m >= 50000:
            imp = 100
        mf = m - imp
    elif im == 3:
        imp = (m * 3) // 100
        mf = m - imp
    return mf, imp


def menu():
    print(" === MENÚ === ")
    print("1) cargar envios")
    print("2) mostrar Resultados")
    print("0)  salir")
    op = int(input("ingrese el numero: "))
    return op


def principal():
    v_envios = []
    op = -1
    while op != 0:
        op = menu()
        if op == 1:
            v_envios = cargar_envios()
        elif op == 2:
            if v_envios:
                mostrar_resultado(v_envios)
            else:
                print("flaco sos pelotudo carga primero")
    return

if __name__ == "__main__":
    principal()