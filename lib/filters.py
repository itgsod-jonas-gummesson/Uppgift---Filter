fan_va_listit = [5,2,3,4,5,2,3,4,5,7,1,1,3,4,5,2,7,2,3,3,8,2,3,4,2,4]

def filter (lista, desire):
    for zdgnf in lista:
        if zdgnf == desire:
            print desire

def exclude (lista, desire):
    tick = 0
    for zdgnf in lista:
        if zdgnf != desire:
            print lista[tick]
        tick += 1

def unique (lista): # Funkar inte
    tick = 0
    hurk = []
    for zdgnf in lista:
        for zdgnf in hurk:
            if zdgnf != hurk[tick]:
                hurk.append(zdgnf)
        tick += 1
    print hurk
unique(fan_va_listit)