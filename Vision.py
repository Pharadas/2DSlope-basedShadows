import random as rndm
import msvcrt

while True:

    print("Hey! f11 si quieres verlo en pantalla completa, 'n' si quieres reiniciarlo.\nRecuerda WASD para moverte.\nEste programa simula sombras, se veran asi --> '▒', y las paredes se veran asi --> '█', tu te veras asi --> '▲', y  tu objetivo es encontrar esto --> 'ﷺ'")

    l = input("Continuar? (y/n) --> ")
    if l == "n":
        break

    n = int(input("longitud (yo recomiendo 33, este sera el eje X) --> "))
    m = int(input("altura (yo recomiendo 40, este sera el eje Y) --> "))

    Mundo = [[" " for x in range(n)] for y in range(m)]

    while True:
        jugadorX = rndm.randint(0,n - 1)
        jugadorY = rndm.randint(0,m - 1)
        if Mundo[jugadorY][jugadorX] == " ":
            break

    while True:
        surpriseX = rndm.randint(0, n - 1)
        surpriseY = rndm.randint(0, m - 1) 

        if Mundo[surpriseY][surpriseX] == " ":
            break

    Cp = int(input("Cuantas paredes? ==> "))

    paredesY = []
    paredesX = []

    Pendientes = [[] for i in range(Cp)]

    for i in range(Cp):
        paredesX.append(rndm.randint(0,n - 1))
        paredesY.append(rndm.randint(0,m - 1))

    o = 0
    while True:
        if o == 1:
            Mundo[jugadorY][jugadorX] = " "

            movement = msvcrt.getwch()

            if movement == "w" and jugadorY > 0:
                if Mundo[jugadorY - 1][jugadorX] != "█":
                    jugadorY = jugadorY - 1
            if movement == "a" and jugadorX > 0:
                if Mundo[jugadorY][jugadorX - 1] != "█":
                    jugadorX = jugadorX - 1
            if movement == "d" and jugadorX < n - 1:
                if Mundo[jugadorY][jugadorX + 1] != "█":
                    jugadorX = jugadorX + 1
            if movement == "s" and jugadorY < m - 1:
                if Mundo[jugadorY + 1][jugadorX] != "█":
                    jugadorY = jugadorY + 1
            elif movement == "n":
                break
        
    # WorldBuilding===================================================================================================================

        for i in range(Cp):
                cinX = paredesX[i] - jugadorX
                cinY = paredesY[i] - jugadorY
                if paredesY[i] == jugadorY:
                    Pendientes[i] = [1 / (cinX) - 0.1, -1 / (cinX) + 0.1]
                elif cinX == 0:
                    Pendientes[i] = [(cinY) / (cinX + 0.5),(cinY) / (cinX - 0.5)]
                else:
                    pendiente = (cinY) / (cinX)
                    Pendientes[i] = [pendiente + (pendiente * 0.35), pendiente - (pendiente * 0.35)]

        # Logica de sombras============================================================================================================

        Mundo = [[" " for x in range(n)] for y in range(m)]

        for p in range(Cp):
            for y in range(len(Mundo)):
                for x in range(len(Mundo[y])):
                    try:
                        pen = (y - jugadorY) / (x - jugadorX)
                        if pen == 0:
                            if jugadorY == paredesY[p]:  # Mismo eje Y (diferente X)
                                if jugadorX > paredesX[p] and x < paredesX[p] and y == jugadorY:
                                    Mundo[y][x] = "▒"
                                elif jugadorX < paredesX[p] and x > paredesX[p] and y == jugadorY:
                                    Mundo[y][x] = "▒"

                        if jugadorY == paredesY[p]:
                            if y != jugadorY and x != jugadorX and jugadorX < paredesX[p] and x > paredesX[p]:
                                if pen <= Pendientes[p][0] and pen >= Pendientes[p][-1]:
                                    Mundo[y][x] = "▒"
                            elif (y != jugadorY and x != jugadorX and jugadorX > paredesX[p] and x < paredesX[p]):
                                if pen >= Pendientes[p][0] + 0.15 and pen <= Pendientes[p][-1] - 0.15:
                                    Mundo[y][x] = "▒"
                                
                        elif jugadorX == paredesX[p]:
                            if x != jugadorX and y < paredesY[p] and jugadorY > paredesY[p]:
                                if (jugadorY - y) / (jugadorX - x) <= Pendientes[p][0] or (jugadorY - y) / (jugadorX - x) >= Pendientes[p][1]:
                                    Mundo[y][x] = "▒"
                            elif x != jugadorX and y > paredesY[p] and jugadorY < paredesY[p]:
                                if pen >= Pendientes[p][0] or pen <= Pendientes[p][1]:
                                    Mundo[y][x] = "▒"

                        elif y != jugadorY and x != jugadorX:
                            if paredesY[p] < jugadorY and paredesX[p] > jugadorX:  # Cuadrante 1
                                if pen >= Pendientes[p][0] and pen <= Pendientes[p][-1]:
                                    if y < paredesY[p] and x > paredesX[p]:
                                        Mundo[y][x] = "▒"

                            if paredesY[p] > jugadorY and paredesX[p] > jugadorX:  # Cuadrante 4
                                if pen <= Pendientes[p][0] and pen >= Pendientes[p][-1]:
                                    if y > paredesY[p] and x > paredesX[p]:
                                        Mundo[y][x] = "▒"
                                    
                            if paredesY[p] > jugadorY and paredesX[p] < jugadorX:  # Cuadrante 3
                                if pen >= Pendientes[p][0] and pen <= Pendientes[p][-1]:
                                    if y > paredesY[p] and x < paredesX[p]:
                                        Mundo[y][x] = "▒"

                            if paredesY[p] < jugadorY and paredesX[p] < jugadorX:  # Cuadrante 2
                                if pen <= Pendientes[p][0] and pen >= Pendientes[p][-1]:
                                    if y < paredesY[p] and x < paredesX[p]:
                                        Mundo[y][x] = "▒"

                    except:
                        if jugadorX == paredesX[p]:  # Mismo eje X (diferente Y)=
                            if jugadorY > paredesY[p] and y < paredesY[p] and x == jugadorX:
                                Mundo[y][x] = "▒"
                            elif jugadorY < paredesY[p] and y > paredesY[p] and x == jugadorX:
                                Mundo[y][x] = "▒"

        o = 1

        for p in range(Cp):
            if Mundo[paredesY[p]][paredesX[p]] != "▒":
                Mundo[paredesY[p]][paredesX[p]] = "█"
            
        if Mundo[surpriseY][surpriseX] != "▒":
            Mundo[surpriseY][surpriseX] = "ﷺ"
        
        if jugadorY == surpriseY and jugadorX == surpriseX:
            break

        Mundo[jugadorY][jugadorX] = "▲"

        [print(i) for i in Mundo]
        print(["█" for i in range(n)])
    [print(i) for i in Mundo]
    print("Mistery box!")