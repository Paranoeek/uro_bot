import datetime
import calendar
from dataclasses import dataclass


today = datetime.date.today()
tyear = today.year
int_tyear = int(tyear)
uro = [
"12 stycznia 1998 - Vanddeloon",
"5 lutego 2003 - Dudek",
"9 lutego 2003 - schafter",
"14 lutego 1997 - Bombelos",
"17 lutego 2002 - VeltY.",
"1 marca 2003 - Freyu",
"29 kwietnia 1998 - Emer",
"13 maja 1989 - Czarny",
"9 czerwca 1990 - burza24",
"11 czerwca 2005 - Chudy",
"27 czerwca 2005 - CyganK",
"28 czerwca 1996 - Bandi",
"30 czerwca 1997 - Belmondoe",
"20 lipca 2002 - May",
"3 sierpnia 2000 - Zobercik",
"11 sierpnia 2000 - Pioterrr",
"21 sierpnia 2003 - KA3DY",
"8 września 2000 - Chemik",
"18 września 1996 - Guttural",
"11 października 2002 - Ziemniak",
"17 listopada 2001 - Michaler",
"30 listopada 1995 - Bolo95",
"11 grudnia 2003 - Janusch",
"11 grudnia 1997 - K4M1Lo5",
"12 grudnia 2000 - Marco",
"25 grudnia 2000 - Daszek",
"27 grudnia 2001 - Gumi",
"17 maja 1998 - test",
"17 maja 2003 - test1"
]

 


month_num = {
    "stycznia": "01",
    "lutego": "02",
    "marca": "03",
    "kwietnia": "04",
    "maja": "05",
    "czerwca": "06",
    "lipca": "07",
    "sierpnia": "08",
    "września": "09",
    "października": "10",
    "listopada": "11",
    "grudnia": "12",
}


def urodc():
    for n in uro: 
        namedata = n
        dzien, miesiac, rok, dash, nick = namedata.split()
        miesiac = month_num[miesiac]
        namedata = f"{dzien}/{miesiac}/{rok} {dash} {nick}"
        

def urodc():
    urodzenia = {}
    
    for n in uro:
       
        namedata = n
        dzien, miesiac, rok, dash, nick = namedata.split()
        int_rok = int(rok)
        miesiac = month_num[miesiac]
        wiek = int_tyear-int_rok
        data = f"{miesiac}-{dzien}"
        urodzenia[nick, wiek] = data
  
        
    return urodzenia

urodzenia_dict = urodc()
print(urodzenia_dict)




