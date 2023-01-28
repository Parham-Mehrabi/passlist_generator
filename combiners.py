

def tarkib(depths,deraza,passw_list,dinamit):
    if depths > 1:
        for i in range(deraza):
            for j in range(deraza):
                passw_list.append(f'{dinamit[i]}-{dinamit[j]}')
                passw_list.append(f'{dinamit[i]}{dinamit[j]}')
    if depths > 2:
        for i in range(deraza):
            for j in range(deraza):
                for g in range(deraza):
                    passw_list.append(f'{dinamit[i]}-{dinamit[j]}-{dinamit[g]}')
                    passw_list.append(f'{dinamit[i]}{dinamit[j]}{dinamit[g]}')
    if depths > 3:
        for i in range(deraza):
            for j in range(deraza):
                for g in range(deraza):
                    for g2 in range(deraza):
                        passw_list.append(f'{dinamit[i]}-{dinamit[j]}-{dinamit[g]}-{dinamit[g2]}')
                        passw_list.append(f'{dinamit[i]}{dinamit[j]}{dinamit[g]}{dinamit[g2]}')
    if depths > 4:
        for i in range(deraza):
            for j in range(deraza):
                for g in range(deraza):
                    for g2 in range(deraza):
                        for g3 in range(deraza):
                            passw_list.append(f'{dinamit[i]}-{dinamit[j]}-{dinamit[g]}-{dinamit[g2]}-{dinamit[g3]}')
                            passw_list.append(f'{dinamit[i]}{dinamit[j]}{dinamit[g]}{dinamit[g2]}{dinamit[g3]}')
    return passw_list