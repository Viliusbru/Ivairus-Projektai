from random import randint

lives = 3

while lives > 0:
    listas = ['Zirkles', 'Lapas', 'Sulinys']
    
    pick = listas[randint(0,2)]
    spejimas = input('''
    Zirkles(ivesk Z)

    Lapas(ivesk L)
    
    Sulinys(ivesk S)
    ''').upper()
    if (spejimas != 'Z' and spejimas != 'L' and spejimas != 'S'):
        print('ivesta neteisinga raide')
    elif(spejimas == 'Z'):
        if(pick == 'Lapas'):
            print('U WIN EZ')
            break
        elif(pick == 'Zirkles'):
            print('TIE')
        else:
            print('U DIED -1 HP')
            lives -= 1
    elif(spejimas == 'L'):
        if(pick == 'Sulinys'):
            print('ez win')
            break
        elif(pick == 'Lapas'):
            print('TIE')
        else:
            print('U DIED -1 HP')
            lives -= 1
    elif(spejimas == 'S'):
        if(pick == 'Zirkles'):
            print('Ez WIN')
            break
        elif(pick == 'Sulinys'):
            print('TIE')
        else:
            print('prapisai rip')
            lives -= 1
