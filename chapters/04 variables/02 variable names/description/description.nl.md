Zoals eerder gemeld, krijgen variabelen een naam. Je bent vrij om de naam
te kiezen en hoeft je dus niet te beperken tot `x`, `y`, en `z` zoals in voorgaande
voorbeelden. Houd je in de naamkeuze wel aan een aantal **eenvoudige regels / afspraken**:

-   Een variabele naam mag enkel bestaan uit letters (zowel hoofd- als kleine letters), cijfers en "underscores" (`_`).
    Let op: Python is "case sensitive" dus gevoelig voor de verschillen tussen hoofd- en kleine letters. Zo is de variabele naam `wereld` voor Python niet hetzelfde als de variabele naam `Wereld`.

-   Een variabele naam begint steeds met een letter. 

-   Kies een betekenisvolle naam in het Nederlands. Voorbeeld: een
    variabele die het aantal seconden in een week bijhoudt, zou de naam
    `sec_per_week` kunnen hebben.
   
-   Als een variabele naam uit meerdere woorden bestaat,
    scheid de woorden dan met underscores vb. `secs_per_week`.
    Je kan er ook voor kiezen om elk woord te starten met een hoofdletter vb. `SecPerWeek`

-   Een variabele naam mag geen gereserveerd woord zijn binnen Python. 

"Gereserveerde woorden" (of "keywords") zijn:

    False      class      finally    is         return
    None       continue   for        lambda     try
    True       def        from       nonlocal   while
    and        del        global     not        with
    as         elif       if         or         yield
    assert     else       import     pass
    break      except     in         raise


-   Kies *nooit* een variabele naam die ook de naam is van een functie. Dit kan leiden tot fouten.

De conventie met betrekking tot het kiezen van **betekenisvolle variabele namen** is eigenlijk de belangrijkste omdat het de code leesbaar en
onderhoudbaar maakt. Bekijk de volgende code eens. Begrijp je wat deze code doet?

```python
a = 3.14159265
b = 7.5
c = 8.25
d = a * b * b * c / 3
print( d )
```

Je ziet waarschijnlijk wel dat er een
benadering van $$\pi$$ in voorkomt, maar wat stelt `d` voor?

Deze code berekent het volume van een kegel. Met het gebruik van de
variabele namen a, b, c en d had je dat waarschijnlijk
niet geraden. Bekijk nu de volgende, equivalente code waarin enkel de
variabele namen werden aangepast:

```python
pi = 3.14159265
straal = 7.5
hoogte = 8.25
volume_van_kegel = pi * straal * straal * hoogte / 3
print( volume_van_kegel )
```

Dit maakt het een stuk leesbaarder.

Bij code met betekenisvolle namen hoef je geen commentaarregels op te nemen om de gebruiker te
laten begrijpen wat de code precies doet. Toch kan als eerste regel een commentaarregel zoals hieronder weergegeven meer duidelijkheid bieden over het doel van het programma:  

```python
# berekening van volume van kegel met gegeven straal en hoogte
```
**Wij spreken af dat we elke code laten starten met een commentaarregel die het doel van het programma aangeeft.**

{:class="callout callout-info"}
> ### Oefening op het gebruik van correcte variabele namen
>  
> #### Opgave
> In de code hieronder wordt de waarde 1 toegekend aan een aantal mogelijke variabele namen. Sommige hiervan zijn correct, andere niet. Identificeer de foutieve namen en leg uit waarom.
> ```python
>  classificatie = 1   # 1
>  Classificatie = 1   # 2
>  cl@ssificatie = 1   # 3
>  class1f1cat1e = 1   # 4
>  1classificatie = 1  # 5
>  _classificatie = 1  # 6
>  class = 1           # 7
>  Class = 1           # 8
>  ```
>  
> #### Antwoord
> De derde, vijfde, en zevende zijn *foutieve* namen: in de derde gebruikt men een at-sign (`@`), de vijfde begint met een cijfer, en de zevende naam is een gereserveerd woord (dit valt op vanwege de syntax highlighting). 
> Alle andere namen zijn correct. Toch zouden *volgens de conventies* de tweede, de zesde en de achtste naam *vermeden* moeten worden: de zesde begint met een underscore, de tweede en achtste bevatten een hoofdletter en de achtste naam lijkt bovendien op een gereserveerd woord.

### Constanten

"Constanten" zijn **variabelen waaraan een vaste waarde is toegekend**. De inhoud van de variabele verandert dus niet bij het doorlopen van de code. 
Constanten krijgen, net als elke andere variabele een naam.  Kies een betekenisvolle naam zodat de code duidelijker wordt, makkelijker te begrijpen is. Zeker wanneer vaste waarden meerdere malen terugkeren in de code, is het raadzaam om eenmalig een constante te definiëren bovenin de code, waar ze gemakkelijk gevonden en gewijzigd kan worden.

Volgens afspraak worden alle letters in de namen van de constante als **hoofdletters** geschreven. 

Het volgende voorbeeld maakt het voordeel en het gebruik van constanten duidelijk. Het eindbedrag (inclusief BTW) wordt berekend voor een rekening van €24,95 exclusief BTW. Het resultaat wordt afgerond op een cent.

```python
totaal = 24.95
eind_totaal = int( 100 * totaal * 1.21 ) / 100
print( eind_totaal )
```

Hieronder wordt dezelfde code opnieuw geschreven, maar dit keer met gebruik van constanten.

```python
BTW_FACTOR = 1.21
CENTEN = 100

totaal = 24.95
eind_totaal = int( CENTEN * totaal * BTW_FACTOR ) / CENTEN
print( eind_totaal )
```
Merk op dat de code eenvoudiger te begrijpen is gezien er een betekenis wordt gegeven aan de constanten. Wanneer de BTW tarieven zouden wijzigen, volstaat het om bovenaan in de code de waarde van de variabele BTW_FACTOR aan te passen.

*Opmerking: in andere programmeertalen heeft een constante een eigen datatype.*
*In Python is een constante een gewone variabele die we volgens afspraak een naam geven die volledig bestaat uit hoofdletters.* 