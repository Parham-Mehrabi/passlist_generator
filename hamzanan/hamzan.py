def dotaii(deraza, passw_list, dinamit):
    for i in range(deraza):
        for j in range(deraza):
            passw_list.append(f'{dinamit[i]}-{dinamit[j]}')
            passw_list.append(f'{dinamit[i]}{dinamit[j]}')
    return passw_list


def setaii(deraza, passw_list, dinamit):
    for i in range(deraza):
        for j in range(deraza):
            for g in range(deraza):
                passw_list.append(f'{dinamit[i]}-{dinamit[j]}-{dinamit[g]}')
                passw_list.append(f'{dinamit[i]}{dinamit[j]}{dinamit[g]}')
    return passw_list


def chahartaii(deraza, passw_list, dinamit):
    for i in range(deraza):
        for j in range(deraza):
            for g in range(deraza):
                for g2 in range(deraza):
                    passw_list.append(f'{dinamit[i]}-{dinamit[j]}-{dinamit[g]}-{dinamit[g2]}')
                    passw_list.append(f'{dinamit[i]}{dinamit[j]}{dinamit[g]}{dinamit[g2]}')
    return passw_list


def panjtaii(deraza, passw_list, dinamit):
    for i in range(deraza):
        for j in range(deraza):
            for g in range(deraza):
                for g2 in range(deraza):
                    for g3 in range(deraza):
                        passw_list.append(f'{dinamit[i]}-{dinamit[j]}-{dinamit[g]}-{dinamit[g2]}-{dinamit[g3]}')
                        passw_list.append(f'{dinamit[i]}{dinamit[j]}{dinamit[g]}{dinamit[g2]}{dinamit[g3]}')
    return passw_list


