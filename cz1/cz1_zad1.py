#Twoj przyjaciel inwestor, Bitek ma pewien problem. Zdolal juz przewidziec ceny akcji na gieldzie
#pewnej firmy, tylko nie wie kiedy kupic, a kiedy sprzedac akcje(chce kupic pewnego dnia a potem
#sprzedac jakiegos pozniejszego z jak najwiekszym zyskiem), wiec poprosi l Cie o pomoc.
#W skrocie masz podany ciag an i masz wybrac takie 1 ≤i≤j ≤n, tak ˙zeby aj − ai by lo jak
#najwieksze.

import copy

days_nmbr = int(input(""))
days_list = []
days_list = input("").split()
days_list = [int(i) for i in days_list]

days_list_sorted = copy.deepcopy(days_list)
days_list_sorted.sort()

highest_number=(days_list.index(days_list_sorted[-1]), days_list_sorted[-1])
lowest_number=(days_list.index(days_list_sorted[0]), days_list_sorted[0])

if highest_number[0] > lowest_number[0]:
    print(highest_number[1]-lowest_number[1])
else:
    tmp_list_lth = [i for i in days_list[lowest_number[0]+1:]]
    tmp_list_htl = [i for i in days_list[0:highest_number[0]]]
    tmp_list_lth.sort()
    tmp_list_htl.sort()
    s_highest = (days_list.index(tmp_list_lth[-1]), tmp_list_lth[-1])
    s_lowest = (days_list.index(tmp_list_htl[0]), tmp_list_htl[0])
    if highest_number[1] - s_lowest[1] > s_highest[1] - lowest_number[1]:
        print(highest_number[1] - s_lowest[1])
    else:
        print(s_highest[1] - lowest_number[1])


