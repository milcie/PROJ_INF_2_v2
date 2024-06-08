# PROJ_INF_2_v2

Program umożliwia działanie wtyczki w programie QGIS i przeprowadzania działań, takich jak obliczenie równicy wysokości między dwoma punktami oraz obliczenie pola powierzchni.:

WYMAGANIA:

    Python 3.9
    Biblioteki: math, PyQt5
    QGIS 3.36.0
    system Windows

INSTRUKCJA OBSŁUGI:
Program umożliwia przeprowadzenie wyżej wymienionych operacji w określonej wersji programu QGIS. Po pobraniu plików należy przeładować wtyczkę PROJ_INF_2_v2 w programie.

W przypadku obliczenia przewyższeń:
1. Najpierw zaznaczyć dwa punkty, których wysokość jest określona w metrach.
2. Wejść we Wtyczki -> PROJ_INF_2_v2. Uruchomi się interfejs wtyczki.
3. Działamy jedynie w pierwszej części, która liczy przewyższenia. Wybrać warstwę, na krórej znajdują się zaznaczone dwa punkty.
4. Kliknąć przycisk oblicz.
5. Przewyższenie wyświetli się w zaokrągleniu do stu tysięcznych metra.


W przypadku obliczenia pól powierzchni:
1. Najpierw zaznaczyć conajmniej trzy punkty, których współrzędne są określone w metrach.
2. Wejść we Wtyczki -> PROJ_INF_2_v2. Uruchomi się interfejs wtyczki.
3. Działamy jedynie w drugiej części, która liczy pola powierchni. Wybrać warstwę, na krórej znajdują się zaznaczone dwa punkty.
4. Kliknąć przycisk oblicz.
5. Pole wyświetli się w zaokrągleniu do stu tysięcznych metrów kwadratowch.

   
