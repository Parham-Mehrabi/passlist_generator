import threading
from hamzanan.hamzan import *


def tarkib(depths,deraza,passw_list,dinamit):
    if depths == 2:
        passw_list = dotaii(deraza,passw_list,dinamit)
        return passw_list
    if depths == 3:
        a = threading.Thread(target=dotaii, args=(deraza,passw_list,dinamit))
        b = threading.Thread(target=setaii, args=(deraza,passw_list,dinamit))
        a.start()
        b.start()
        a.join()
        b.join()
        return passw_list
    if depths == 4:
        a = threading.Thread(target=dotaii, args=(deraza,passw_list,dinamit))
        b = threading.Thread(target=setaii, args=(deraza,passw_list,dinamit))
        c = threading.Thread(target=chahartaii, args=(deraza,passw_list,dinamit))
        a.start()
        b.start()
        c.start()
        a.join()
        b.join()
        c.join()

        return passw_list
    if depths == 5:
        a = threading.Thread(target=dotaii, args=(deraza,passw_list,dinamit))
        b = threading.Thread(target=setaii, args=(deraza,passw_list,dinamit))
        c = threading.Thread(target=chahartaii, args=(deraza,passw_list,dinamit))
        d = threading.Thread(target=panjtaii, args=(deraza,passw_list,dinamit))
        a.start()
        b.start()
        c.start()
        d.start()
        a.join()
        b.join()
        c.join()
        d.join()
        return passw_list

    return passw_list
