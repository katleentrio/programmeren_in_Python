Zoals eerder gemeld, krijgen variabelen een naam. Je bent vrij om de naam
te kiezen en hoeft je dus niet te beperken tot `x`, `y`, en `z` zoals in voorgaande
voorbeelden. Houd je in de naamkeuze wel aan een aantal **eenvoudige regels**:

-   Een variabele naam mag enkel bestaan uit letters (zowel hoofd- als kleine letters), cijfers en "underscores" (`_`).
    Let op: Python is "case sensitive" dus gevoelig voor de verschillen tussen hoofd- en kleine letters. Zo is de variabele naam `wereld` voor Python niet hetzelfde als de variabele naam `Wereld`.

-   Een variabele naam moet beginnen met een letter of een underscore.

-   Een variabele naam mag geen gereserveerd woord zijn. "Gereserveerde woorden" (of "keywords") zijn:

    False      class      finally    is         return
    None       continue   for        lambda     try
    True       def        from       nonlocal   while
    and        del        global     not        with
    as         elif       if         or         yield
    assert     else       import     pass
    break      except     in         raise

|        	|          	|         	|          	|        	|
|--------	|----------	|---------	|----------	|--------	|
| False  	| class    	| finally 	| is       	| return 	|
| None   	| continue 	| for     	| lambda   	| try    	|
| True   	| def      	| from    	| nonlocal 	| while  	|
| and    	| del      	| global  	| not      	| with   	|
| as     	| elif     	| if      	| or       	| yield  	|
| assert 	| else     	| import  	| pass     	|        	|
| break  	| except   	| in      	| raise    	|        	|

### Afspraken 

Programmeurs houden zich aan een aantal conventies wanneer ze 
variabele namen kiezen. Tracht je hier ook aan te houden
wanneer je je eigen code schrijft. De belangrijkste conventies zijn de volgende:

-   Kies *nooit* een variabele naam die ook de naam is
    van een functie. Zo loop je immers
    de kans dat de functie niet langer door de code gebruikt kan worden,
    wat kan leiden tot fouten.

-   Kies een naam die betekenisvol is in de context van het programma. Voorbeeld: een
    variabele die het aantal seconden in een week bijhoudt, zou de naam
    `secs_per_week` kunnen hebben.
    Uitzondering hierop: voor "*wegwerp variabelen*" hoef je geen betekenisvolle 
    variabele naam te kiezen. Wegwerp variabelen zijn
    variabelen die slechts in een klein deel van de code gebruikt
    worden en naderhand niet meer. Ze hebben
    eigenlijk geen betekenis maar worden toegepast als tijdelijk hulpmiddel.
    Vaak worden hiervoor één-letter namen gebruikt, zoals `i` of `j`.

-   Om verwarring tussen hoofd- en kleine letters te vermijden,
    gebruik je best alleen kleine letters in variabele namen.

-   Als een variabele naam uit meerdere woorden bestaat,
    plaats dan underscores tussen die woorden.

-   Kies nooit variabele namen die beginnen met een
    underscore, ook al is dit toegelaten. (Dit wordt voorbehouden voor de
    auteurs van Python.)

De conventie met betrekking tot het kiezen van betekenisvolle
variabele namen is eigenlijk de belangrijkste omdat het de code leesbaar en
onderhoudbaar maakt. Bekijk de volgende code eens. Begrijp wat deze code doet?

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

Code met betekenisvolle namen wordt vaak "zelf-documenterend" genoemd;
je hoeft er geen commentaarregels in op te nemen om de gebruiker te
laten begrijpen wat de code precies. Dat neemt niet weg
dat in bovenstaande code als eerste regel een commentaarregel zoals hieronder
nog meer duidelijkheid kan bieden:  

```python
# berekening van volume van kegel met gegeven straal en hoogte
```

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
> Alle andere namen zijn correct. Toch zouden *volgens de conventies* de tweede, de zesde en de achtste naam *vermeden* moeten worden: de zesde begint met een underscore, de tweede en achtste bevatten een hoofdletter en de achtste maam lijkt bovendien op een gereserveerd woord.

### Constanten

"Constanten" zijn vaste waarden die aan een variabele zijn toegekend
en dus niet meer veranderen. Het is de afspraak dat alle letters in de
namen van deze variabelen hoofdletters zijn. Constanten worden gebruikt
om de code leesbaarder en onderhoudbaarder te maken. 

In het volgende voorbeeld wordt het eindbedrag berekend 
voor een rekening van €24,95 exclusief BTW:

```python
totaal = 24.95
eind_totaal = int( 100 * totaal * 1.21 ) / 100
print( eind_totaal )
```

In de volgende equivalente code worden constanten gebruikt. Dit
maakt de code leesbaarder:

```python
BTW_FACTOR = 1.21
CENTEN = 100

totaal = 24.95
eind_totaal = int( CENTEN * totaal * BTW_FACTOR ) / CENTEN
print( eind_totaal )
```

Een bijkomend voordeel bij het gebruik van constanten is dat het nu
ook gemakkelijker is om de code aan te passen als de BTW tarieven wijzigen.
*Zeker als vaste waarden meerdere malen terugkeren in de code, is het raadzaam om eenmalig een constante te definieren bovenin de code, waar ze gemakkelijk gevonden en gewijzigd kunnen worden.*

Hoewel constanten erg nuttig kunnen zijn, worden ze -in tegenstelling
tot veel andere programmeertalen- niet door Python
ondersteund en beschouwd als een gewone variabele.
Het is echter de gewoonte om de variabelen waarvan de naam volledig uit
hoofdletters bestaat, te beschouwen als constanten die niet
in de code gewijzigd mogen worden nadat ze hun initiële waarde hebben
gekregen. 
