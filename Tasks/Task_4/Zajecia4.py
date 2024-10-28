#%%
# # Zajęcia 4. Elementy programowania funkcyjnego w Pythonie
# Programowanie funkcyjne to takie, w którym zamiast dawać przepisy jak kolejno zmieniać stan obiektów, aby dojść do stanu pożądanego (to jest esencja programowania imperatywnego), dajemy przepisy jak konstruować nowe wartości ze starych (zwykle używając funkcji), aby dojść do wartości pożądanej. Elementami tego paradygmatu w Pythonie są niezmienialne struktury danych, takie jak napisy, krotki, frozen_set-y itd, ale także dostępność niektórych idiomów programistycznych, charakterystycznych dla "prawdziwych" języków funkcyjnych, takich jak Haskell czy OCaml.
# 
# W tym scenariuszu (potem jeszcze jednym z następnych) poznamy niektóre z tych idiomów, część z nich jest podobna do tego, co jest dostępne w Javie.
 #%%
# ## Funkcja map
# 
# Mając daną listę czasem potrzebujemy przetworzyć jej elementy i wyniki tego przetworzenia zebrać do nowej listy. Załóżmy, że potrzebujemy każdemu napisowi na liście przypisać jego długość. Można to w Pythonie zrobić na (co najmniej :) trzy różne sposoby.
# ### Sposób 1 (tradycyjnie)
 #%%
lista_napisów = "Ala zaadaptowała bardzo zabawnego kota".split()
lista_napisów
 #%%
l = []
for s in lista_napisów:
    l.append(len(s))    # l += [len(s)]   # można też tak, ale to właśnie append służy do dodawania JEDNEGO elementu do listy
l
 #%%
# Ten sposób ma trzy linijki, z czego mniej więcej dwie to boilerplate code, czyli kod "nudny, niewiele wnoszący, powtarzalny, zaśmiecający i zaciemniający czytelność [...]. Mimo to nie można z niego zrezygnować, ponieważ jest zwyczajnie potrzebny, łącząc w spójną całość pozostałe fragmenty aplikacji." (żródło: [pierwszy link z google'a](https://stormit.pl/boilerplate-code/)).
# 
# Sposób ten jest bardzo imperatywny w swej naturze - każdy obrót pętli zmiania stan obiektu (listy) przypisanego do zmiennej `l`.
# 
# ### Sposób 2 (list comprehension)
 #%%
[len(s) for s in lista_napisów]
 #%%
# Tutaj już boilerplate ma tylko ⅓ linijki, więc jest całkowicie akceptowalny. Już na pierwszy rzut oka widać, co ten kod robi. Nie ma tu też żadnej "zmiany stanu", po prostu magicznie powstaje lista wynikowa o odpowiednio skonstruowanych elementach.
# ### Sposób 3 (funkcja map)
 #%%
list(map(len, lista_napisów))
 #%%
# Pierwszym argumentem `map` jest funkcja, która będzie zaaplikowana do każdego elementu drugiego argumentu (czyli listy napisów). Ale tak naprawdę drugi argument wcale nie musi być listą, byleby miał elementy, które można z niego kolejno "wyciągać" (tak jak np. `range(...)`, krotka, słownik, zbiór, itp.). Wynikiem wywołania funkcji `map` też nie jest lista, tylko iterator, podobny do np. `range(...)` (co ma swoje zalety i wady), z którego można zrobić listę, używając konwersji `list(...)`. W razie potrzeby można też zrobić (niezmienialną) krotkę używając `tuple(...)`.
# 
# Funkcja `map` jest jednym z najbardziej emblematycznych idiomów programowania funkcyjnego.
# 
# W naszym przykładzie funkcja, którą chcemy zaaplikować do każdego elementu listy, była już zdefiniowana wcześniej, ale często zdarza się, że to co chcemy zrobić tylko "prawie" odpowiada jednej z gotowych funkcji. Na przykład jeśli chcielibyśmy policzyć liczbę wystąpień literki `a` w poszczególnych napisach z listy, to mamy gotową funkcję `count`, ale musimy do niej dołożyć informację, że chodzi o literkę `a`. Tradycyjny sposób to oczywiście zdefiniowanie odpowiedniej funkcji:
 #%%
def licz_a(s):
    return s.count('a')
 #%%
# Ale można też użyć funkcji anonimowej, czyli tzw. *wyrażenia lambda*.
# ## Funkcje anonimowe
 #%%
list(map(lambda s: s.count('a'), lista_napisów))
 #%%
# Funkcje anonimowe zajmują chyba pierwsze miejsce jeśli chodzi o skojarzenia z programowaniem funkcyjnym.  
# Składnia wyrażeń lambda w Pythonie to `lambda <parametry>: <wyrażenie>`, gdzie `<parametry>` to lista nazw parametrów rozdzielonych przecinkami, które to nazwy mogą oczywiście występować w `<wyrażeniu>`. Zdefiniowana funkcja jest taka jak w definicji:
# ```python
# def anonimowa(<parametry>):
#     return <wyrażenie>
# ```
 #%%
# ### Ćwiczenie 0
# Za pomocą funkcji `map` oraz funkcji anonimowej oblicz reszty z dzielenia przez 3 następującego zestawu liczb:
# 123,543,234,97,65,23,65
 #%%
# ### Ćwiczenie 1
# Na potrzeby tego ćwiczenia zdefiniujemy "parzy-długość" napisu jako największą liczbę **parzystą** mniejszą lub równą długości napisu.
# Oblicz listę "parzy-długości" napisów na `liście_napisów` przy użyciu funkcji `map`, zapisując funkcję liczącą "parzy-długość" za pomocą wyrażenia lambda (można w nim użyć `%` lub `//`).
 #%%
# ----------
# Z punktu widzenia składni Pythona wyrażenia lambda są po prostu wyrażeniami, czyli mogą występować we wszystkich fragmentach programu, tam gdzie pozostałe wyrażenia np. `x+5`. Funkcje reprezentowane przez wyrażenia lambda (a także na wszystkie inne sposoby, choćby nazwy funkcji zdefiniowanych za pomocą `def`) są traktowane przez Python jak wszystkie inne obiekty: można je przypisywać na zmienne, przekazywać do innej funkcji, dawać jako wynik funkcji, trzymać na liście albo w innych strukturach danych, itd.
 #%%
import random

def przez2(x):
    return x//2

razy2 = lambda x: 2*x

operacje = [przez2, lambda x: x+1, lambda x: x-1, razy2]

def losuj_operację():
    los = random.randrange(5)
    print("Wylosowano:", los)
    if los < len(operacje):
        return operacje[los]
    else:
        return lambda x: 0
 #%%
# za każdym odpaleniem losujemy funkcję, ale tę samą dla wszystkich liczb z range
list(map(losuj_operację(), range(10)))
 #%%
# dla każdej liczby z range osobne losowanie operacji
list(map(lambda x: operacje[random.randrange(4)](x), range(10)))
 #%%
# *Dygresja*: `random.randint(x,y)` to "jedyna" funkcja w Pythonie, która traktuje przedział liczb całkowitych jako obustronnie domknięty. Dlatego tu użyliśmy funkcji `random.randrange`, która przyjmuje parametr(y) tak jak `range`.
 #%%
# ### Różne użyteczne rzeczy w lambdach i nie tylko
# #### Wyrażenie warunkowe
# Bardziej użyteczną rzeczą od losowania funkcji :) jest *wyrażenie warunkowe* (to nie jest to samo, co *instrukcja* warunkowa, którą poznaliśmy wcześniej). Wyrażenie warunkowe w Pythonie ma składnię:
# 
# ```python
# <wyrażenie1> if <warunek> else <wyrażenie2>
# ```
# 
# co na polski przetłumaczylibyśmy najzgrabniej jako `<wyrażenie1>` o ile `<warunek>` wpp `<wyrażenie2>`. 
# 
# W C/C++/Javie byłoby to oczywiście `(<warunek> ? <wyrażenie1> : <wyrażenie2>)`. W Pythonie kolejność elementów jest na pierwszy rzut oka trochę dziwna, ale ta konstrukcja przewidziana jest na sytuacje, gdy warunek raczej jest spełniony :) np:
 #%%
list(map(lambda x: 'a'*x if x else "zero!", range(5)))
 #%%
# Ta "dziwna" kolejność elementów wyrażenia warunkowego ma dwie zalety: po pierwsze jest symetryczna (estetyka ;) a po drugie dobrze się komponuje sama ze sobą w przypadku więcej niż jednego warunku:
 #%%
x = 42
print("ujemna" if x < 0 else "zero" if x == 0 else "dodatnia")
 #%%
# Oczywiście wyrażenie warunkowe wcale nie musi występować w lambdzie. Ale tu jest szczególnie użyteczne, bo w "ciele" lambdy nie może być instrukcji.
# 
# Oczywiście jak się bardzo chce, to każde ograniczenie można obejść, choćby poprzez wywołanie funkcji. 
 #%%
# #### Jak zrobić print w lambdzie?
# Prostym (i często przydatnym np. do debugowania) sposobem obchodzenia ograniczenia składniowego wyrażeń lambda jest tworzenie "tymczasowych" krotek, np:
 #%%
list(map(lambda x: (print("Tu lambda:", x), x+1)[1], range(5)))
 #%%
# W ciele powyższej lambdy tworzymy "na chwilę" krotkę, której elementem o indeksie 0 jest *wynik* funkcji `print` (czyli `None`), a elementem o indeksie 1 jest właściwa wartość, którą wybieramy z krotki jako wynik całej lambdy. Inną konstrukcją z podobnym efektem jest alternatywa. "Wyrażenie" `print(x) or x+1` również spełni nasze oczekiwania, ponieważ `None` zwrócony przez `print` jest traktowane jak fałsz, a w tym przypadku wartość alternatywy to wprost wartość drugiego członu (wcale niekoniecznie `True` lub `False`).
# 
# Należy jednak pamiętać, że elementy programowania funkcyjnego, w tym w szczególności lambdy, nie są stworzone dla efektów ubocznych, a dla obliczania (nowych) wartości na podstawie argumentów. A zatem używanie efektów ubocznych w tych elementach to raczej zły styl programowania.
 #%%
# ### Ćwiczenie 2
# Wyznacz "następny element [ciągu Collatza](https://pl.wikipedia.org/wiki/Problem_Collatza)" dla każdej z liczb z zakresu [1,20].
 #%%
list(map(lambda c: 
 #%%
# ---------------
# 
# ## Funkcja filter
# 
# Drugą najpopularniejszą funkcją wyższego rzędu (czyli funkcją, której parametrem jest funkcja) na listach jest `filter`. Służy ona do wybierania z listy elementów spełniających podany predykat, np.
 #%%
def czy_parz(n):
    """Sprawdza czy liczba n jest parzysta"""
    if n % 2 == 0:
        return True
    else:
        return False

lista_liczb = [1, 10, 11, 121, 1000]
 #%%
list(filter(czy_parz, lista_liczb))
 #%%
# Pierwszym argumentem `filter` jest funkcja (nazwana poprzednio predykatem), która aplikowana jest do kolejnych elementów drugiego argumentu - listy (czy czegoś podobnego) - i wynikiem są tylko te elementy, dla których użyta funkcja daje wynik, który Python traktuje jako "prawda" (zwykle po prostu `True`). 
 #%%
# Podobnie jak w przypadku `map`, wynikiem funkcji `filter` jest iterator (dlatego w przykładach używaliśmy `list(filter(...))`. I znów, podobnie jak w przypadku `map`, użycie funkcji `filter` również można zastąpić innymi technikami: 
 #%%
# tradycyjnie... prawie 3 linie boilerplate code
l = []
for n in lista_liczb:
    if czy_parz(n):
        l.append(n)
l
 #%%
# list comprehension, prawie tak samo zgrabnie jak filter
[n for n in lista_liczb if czy_parz(n)]
 #%%
# ### Ćwiczenie 3
# Używając `filter` i `map` wyznacz wszystkie liczby, które są kwadratami liczb naturalnych mniejszych niż 100 i mają w swojej reprezentacji dwie jedynki pod rząd.
#  
# Podpowiedź: użyj `str(...)` do zamiany liczby na tekst i [`in` do wyszukiwania](https://docs.python.org/3/reference/expressions.html#membership-test-operations).
 #%%
# ------------------
# 
# ## Po co map i filter?
# Oczywistym jest, że bez `map` i `filter` można żyć. W zasadzie list comprehension to takie połączenie `map` i `filter` i w dodatku dużo osób twierdzi, że list comprehension jest bardziej czytelne, a w większości przypadków również bardziej efektywne. Zaletą `map` i `filter` jest zwięzłość (zwłaszcza w przypadku gdy funkcje stosowane jako parametr już istnieją) oraz łatwość komponowania.
# 
# Poeksperymentujmy z następującym zadaniem: podnieśmy do kwadratu wszystkie liczby z jakiegoś dużego przedziału (np. od 0 do 5 milionów), jeśli fortuna nam będzie sprzyjała, podnieśmy je jeszcze raz do kwadratu, a następnie wybierzmy z tego te liczby, których zapis dziesiętny jest palindromem.
# 
# Kod ten, zapisany za pomocą `map` i `filter` będzie wyglądał następująco:
 #%%
def czy_pal(n):
    """Sprawdza czy reprezentacja tekstowa liczby n jest palindromem."""
    s = str(n)
    return s == s[::-1]  # nie do końca efektywne, ale krótkie :)
 #%%
l = range(5_000_000)
l = map(lambda x: x*x, l)
if random.choice([True, False]):
  l = map(lambda x: x*x, l)
l = filter(czy_pal, l)
list(l)
 #%%
# Zauważmy, że ten kod do przedostatniej linijki włącznie, wykonuje się natychmiastowo. Cała praca związana z przetwarzaniem długiej listy odbywa się w ostatniej linii. Ten sam kod z użyciem list comprehension tworzy jedną lub dwie pośrednie listy pomocnicze (można to zobaczyć podglądając intepreter Pythona za pomocą polecenia top w trakcie wykonywania następnego fragmentu). Można by uniknąć tworzenia tych list pomocniczych, używając wyrażeń-generatorów, które produkują obiekty analogiczne do tych produkowanych przez `map` i `filter` (więcej o generatorach za parę tygodni :) 
 #%%
l = range(5_000_000)
l = [x*x for x in l]   # l = (x*x for x in l)   # tak zaoszczędzilibyśmy pamięć 
if random.choice([True, False]):
  l = [x*x for x in l]   # l = (x*x for x in l)   # j.w. 
[x for x in l if czy_pal(x)]
 #%%
# W tym kodzie również cała praca zostanie wykonana w ostatniej linijce, trudno też mu cokolwiek zarzucić, jeśli chodzi o przejrzystość i łatwość komponowania. Pomijając losowanie, "tekstowe" złożenie kilku takich operacji przetwarzających listę chyba nieco lepiej wygląda przy użyciu list comprehension, ale to kwestia gustu:
 #%%
list(filter(czy_pal, map(lambda x: x**4, range(5_000_000))))
 #%%
[x**4 for x in range(5_000_000) if czy_pal(x**4)]
 #%%
# Trzeba przy tym zaznaczyć, że byliśmy zmuszeni do dwukrotnego zapisania (i czasem też obliczenia) wyrażenia `x**4` (choć prawdę mówiąc dałoby się tego uniknąć, ale z użyciem konstrukcji, które są całkowicie niezgodne z duchem programowania funkcyjnego, którego fragmenty właśnie poznajemy - dlatego to teraz pomijamy :).
 #%%
# <!--
# # To jest rozwiązanie, ale go nie pokazujemy :) Po pierwsze bo jest do bólu imperatywne, gdyż używa wyrażenia-przypisania (jak w C).
# # A po drugie bo jest fuj! Używamy y przed jego definicją - ble.
# [ y for x in range(5_000_000) if czy_pal(y:=x**4)]
# -->
 #%%
# Gdyby zależało nam na poznaniu nie tylko palindromu, ale też liczby, której czwarta potęga jest palindromem, modyfikacja w wersji list comprehension jest łatwiejsza, choć i w przypadku `map` i `filter` radzimy sobie bez problemu za pomocą par.
 #%%
list(filter(lambda p: czy_pal(p[1]), map(lambda x: (x, x**4), range(5_000_000))))
 #%%
[(x, x**4) for x in range(5_000_000) if czy_pal(x**4)]
 #%%
# Reasumując, nie widać specjalnie przewagi `map` i `filter` nad list comprehension, zwłaszcza jeśli pamiętamy, że w przypadku wielu kroków wcale nie musimy generować list pośrednich (możemy używać wyrażeń-generatorów). W dodatku funkcje te uznawane są przez niektórych za *niepytoniczne* (ang. unpythonic :)
# Zainteresowanych odsyłam do dość obszernego wątku na [stackoverflow](https://stackoverflow.com/questions/1247486/list-comprehension-vs-map).
# 
# Jeśli chodzi o efektywność, to to jak zwykle zależy. W skrócie, jeśli mamy do wykonania jedną operację i w wyniku potrzebujemy listy, to lepiej używać list comprehension, z wyjątkiem `map(gotowa_funkcja, lista)`. Z kolei wyrażenia-generatory (a konkretnie generowanie z nich końcowych list) jest wolniejsze niż `map` i `filter`. W skrócie: warto te funkcje znać, ale nie ma po co ich zbyt często używać.
 #%%
# ## Funkcje opcjonalnie wyższego rzędu
# 
# Niektóre funkcje działające na ciągach, np. `max`, `min`, `sorted`, mają opcjonalny parametr `key`, który jest funkcją "wyciągającą" rzecz do porównania z danego elementu. Tu też wyrażenie lambda może być pomocne. 
 #%%
lista_napisów = "Zuzanna zaadaptowała bardzo zabawnego kota".split()
print(lista_napisów)
print(min(lista_napisów, key=len))     # najkrótszy napis
print(sorted("Grzegorz Brzęczyszczykiewicz zamieszkały Chrząszczyżewoszyce powiat Łękołody".split(), 
             key=lambda s: sum(x.lower() in 'aąeęioóuy' for x in s)))    # kolejność wg liczby samogłosek
print(max([(1, 2.5), (5, 0.7), (8, 1.5)], key=lambda p: p[1]))     # para o największej drugiej :) współrzędnej

slownik = {"ala":50, "ela":18}
print(slownik["ala"], "to skrót od", slownik.get("ala"))
print(min(slownik, key=slownik.get))      # klucz z najmniejszą wartością w słowniku. Uwaga, nazwa key próbuje nas tu zmylić :)

 #%%
# ## Ciekawostki o map, filter i nie tylko
 #%%
# ### Iteratory to nie listy
# Funkcje `map` i `filter` nie produkują list, tylko iteratory. Trzeba z nimi ostrożnie, bo są trochę podobne do list, co może dawać fałszywe poczucie komfortu, a niektóre różnice mogą być zaskakujące:
 #%%
l = [x*x for x in range(7)]
print("Pierwszy raz (:", *l, ":)")      # *l to wklejenie "tu" elementów l - jako kolejnych argumentów print
print("Drugi raz    (:", *l, ":)")
 #%%
l = map(lambda x: x*x, range(7))
print("Pierwszy raz (:", *l, ":)")      # usunięcie gwiazdki nie pomoże :)
print("Drugi raz    (:", *l, ":)")
 #%%
# Okazuje się, że iterator stworzony przez `map` jest "jednorazowy" (jak Streamy w Javie). Można z niego przeczytać kolejne wartości w celu utworzenia listy, albo iterowania pętlą, ale po przeczytaniu wszystkich wartości "znikają" one z iteratora. Zauważmy, że to działa podobnie do wczytywania danych z plików wejściowych (w szczególności ze strumieni takich jak np. standardowe wejście).
# 
# Zaletą iteratorów jest to, że można tanio "utworzyć" bardzo długi ciąg, a potem skorzystać tylko z takiej części, jaka jest potrzebna. Niestety, dla iteratorów nie działa przyjemna składnia do wybierania fragmentów (slice'ów) - trzeba użyć odpowiedniej funkcji z biblioteki `itertools`.
 #%%
bardzo_długi_ciąg = map(lambda x: x*x, range(10**100))   # dziesięć do setnej, a co! Kto leniwemu zabroni?!

import itertools
list(itertools.islice(bardzo_długi_ciąg,2,30,3))   # to nie is-lice (pol. czy-wszy :) tylko i-slice (jak i(teratorowe)-plasterkowanie)    
 #%%
# ### Uproszczone odsiewanie fejkniusów
# Jeśli chcesz odsiać "nieprawdziwe" elementy z listy za pomocą `filter`, zamiast funkcji można podać `None`.
 #%%
dziwna_lista = "ala   ma    kota".split(" ")
print(dziwna_lista)
 #%%
list(filter(lambda x: x, dziwna_lista))
 #%%
list(filter(None, dziwna_lista))
 #%%
# ### Map z wieloma listami
# Funkcję `map` można używać również z kilkoma listami i wieloargumentową funkcją:
 #%%
list(map(lambda x,y: x+y, [1,2,3], [40,30,20,10]))
 #%%
# Ten sam efekt można uzyskać za pomocą następującego wyrażenia list comprehension:
 #%%
[x + y for (x,y) in zip([1,2,3], [40,30,20,10])]
 #%%
# Użyta powyżej operacja `zip` tworzy iterator par złożonych z elementów obu "list", dopóki jedna z list się nie skończy.
 #%%
list(zip(range(10), range(100,50,-10)))
 #%%
# ### Moduł `operator`
# Zamiast prostych wyrażeń lambda w stylu `lambda x,y: x+y` można użyć gotowych funkcji z modułu `operator`, np.: 
 #%%
import operator
list(map(operator.add, range(10), [-1,1]*10))
 #%%
# Pozostałe nazwy analogicznych funkcji można znaleźć w wygodnej [tabelce w dokumentacji do modułu operator](https://docs.python.org/3/library/operator.html#mapping-operators-to-functions).
# ### Bezparametrowa lambda
# Wyrażenie lambda może mieć zero argumentów. Do czego to może służyć? Nie do `map` albo `filter`, ale na przykład do podania akcji do wykonania w specyficznych okolicznościach.
 #%%
def rób_coś(x, w_razie_awarii):
    print("Próbujemy ... ", end="")
    if x:
        print(100//x, "jest OK.")
    else:
        w_razie_awarii()

rób_coś(5, w_razie_awarii = lambda : print("logger.info('AWARIA!!!')"))

rób_coś(0, w_razie_awarii = lambda : print("logger.info('AWARIA!!!')"))

 #%%
# ## Funkcja reduce
# 
# Kolejną ważną funkcją wyższego rzędu na listach jest `reduce`. Nie ma jej wśród funkcji dostępnych "od razu", jest w module `functools`.
 #%%
from functools import reduce
reduce(lambda x,y: x*y, [2,10,1,7])
 #%%
# Działanie tej funkcji najlepiej wyobrazić sobie w ten sposób, że "w liście" zamiast przecinków wstawiamy * (tym razem to po prostu mnożenie :) i usuwamy `[` klamerki `]`, a zatem otrzymujemy 2 * 10 * 2 * 7. Oczywiście takie tłumaczenie jest dobre tylko dla funkcji łącznej (czyli takiej, której jest wszystko jedno jak wstawimy nawiasy). Tak naprawdę nawiasy wstawione są "bardziej z lewej".
 #%%
reduce(lambda x,y: x-y, [567,100,30,1])
 #%%
# Wynik to 567-100-30-1, czyli ((567-100)-30)-1. Nazwa `reduce` wzięła się stąd, że dokonujemy "redukcji" dwóch wartości do jednej - np. poprzez ich pomnożenie lub odjęcie - i postępujemy tak aż do skutku, czyli aż z całego zestawu zostanie jedna wartość.
# 
# Ale funkcji `reduce` można dać jeszcze jeden parametr - wartość startową.
 #%%
reduce(lambda x,y: x-y, [567,100,30,1], 999)
 #%%
# Teraz wynik to (((999-567)-100)-30)-1. Przy okazji, jak podamy wartość startową, funkcja ma sensowną wartość (właśnie tą startową) dla pustej listy.
# 
# Nic nie stoi też na przeszkodzie, aby wartość początkowa była zupełnie innego typu niż elemety listy, oczywiście nasza funkcja musi to brać pod uwagę.
 #%%
reduce(lambda s,x: s | {x},  [20,8,1,20,8],  {1000,1001}) 
 #%%
# W powyższym przykładzie `|` oznacza operator sumy zbiorów, a wynik to efekt dodawania wszyskich elementów listy do początkowego zbioru. 
# 
# Oczywiście każde działanie robione za pomocą `reduce` można zaprogramować za pomocą pętli po liście i zmieniających się wartości zmiennych, ale - zwłaszcza jak funkcja jest krótka - rozwiązaniom z `reduce` nie można odmówić zwięzłości i elegancji :)
 #%%
# ### Ćwiczenie 4
# Napisz funkcję `silnia` za pomocą `reduce` i `range`.
 #%%
# ### Ćwiczenie 5
# Napisz za pomocą `reduce` funkcję `sumuj`, która dla danej listy liczb oblicza parę, której pierwsza współrzędna będzie sumą liczb parzystych z tej listy, a druga sumą liczb nieparzystych. Może przydać się tutaj wyrażenie warunkowe (patrz wyżej). Przykłady: `sumuj [1,2,3,4,5] = (6,9)`, `sumuj [1,3,5] = (0,9)`

