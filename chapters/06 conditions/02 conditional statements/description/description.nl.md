Zoals ik in het vorige onderdeel aangaf, bestaat een "conditionele statement"
(ook wel "condities" of "`if` statements" genoemd) uit
een test gevolgd door één of meerdere acties, waarbij de acties alleen
worden uitgevoerd als de test `True` oplevert.

Een voorbeeld:

```python
x = 5
if x == 5:
    print( "x is 5" ) # enkel indien de waarde van x gelijk is aan 5 wordt deze afgedrukt
```

De syntax van een `if` statement is als volgt:

```python
if <boolean expressie>:
    <acties>
```

**Let op** noteer steeds een **dubbele punt** (:) achter de boolean expressie, en laat
alle `<acties>` die volgen na de boolean expressie, **inspringen**.

### Blokken code

Het is noodzakelijk dat de `<acties>` "inspringen". Python beschouwt statements die elkaar
opvolgen en dezelfde insprong hebben als één blok code. Het code blok
dat onder het `if` statement staat, is de lijst van alle acties die worden
uitgevoerd indien de boolean expressie `True` is; deze worden overgeslagen indien de boolean expressie `False` is. Een voorbeeld:

```python
x = 7
if x < 10:
    print( "Deze regel wordt alleen uitgevoerd als x < 10." )
    print( "Idem voor deze regel." )
print( "Deze regel wordt altijd uitgevoerd." )
```

Bedenk hoe de uitvoer er uit ziet voor `x = 7` en voor `x = 11`.
De `print()` regel die volgt na de `if` en niet inspringt, wordt uitgevoerd ongeacht het resultaat van de evaluatie van de boolean expressie.

Je kunt meerdere `if` statements gebruiken.

```python
x = 5
if x == 5: 
    print( "x is 5" )
if x > 4: 
    print( "x is groter dan 4" )
if  x >= 5:
    print( "x is groter dan of gelijk aan 5" )
if x < 6: 
    print( "x is kleiner dan 6" ) 
if x <= 5:
    print( "x is kleiner dan of gelijk aan 5" )
if x != 6 :
    print( "x is niet 6" )
```

Bedenk hoe de uitvoer er uit ziet voor `x = 4` of `x = 7`.

### Inspringen

**In Python is het gebruik van correcte insprongen zeer belangrijk!** Zonder
correcte inspringing kan Python niet zien welke regels code een blok
vormen en kan de code bijgevolg niet uitgevoerd worden zoals je bedoelt.[^5]

Inspringen doe je door één tabulatie naar rechts toe te passen (de `Tab` toets) of 4 spaties te gebruiken.

De volgende code bevat inspring-fouten. Verbeter de code.

```python
# Deze code bevat tabulatie-fouten!
x = 3
y = 4
if x == 3 and y == 4:
    print( "x is 3" )
   print( "y is 4" )
if x > 2 and y < 5:
print( "x > 2" )
print( "y < 5" )
if x < 4 and y > 3:
    print( "x < 4" )
        print( "y > 3" )
```

### Twee-weg beslissingen: `if` - `else` constructie

Het komt regelmatig voor dat je onder bepaalde voorwaarden een actie wilt laten uitvoeren, wanneer niet voldaan wordt aan de gestelde voorwaarde er een andere actie wordt uitgevoerd.
Python maakt dit mogelijk door aan een `if` statement een `else` tak toe te voegen.

```python
x = 4
if x > 2:
    print( "x is groter dan 2" )
else:
    print( "x is kleiner dan of gelijk aan 2" ) 
```

De syntax is:

```python
if <boolean expressie>:
    <acties>
else:
    <acties>
```

**Let op** dat er een **dubbele punt** achter de `else` staat, net zoals achter
de `<boolean expressie>` bij de `if`. Het is ook van belang dat het woord 
`else` **uitgelijnd** is met het woord `if`waar het bij hoort. 

![conditie](media/Condition.png "conditie"){:width="25%"}

Wanneer je een `else` tak toevoegt aan een `if` statement, wordt altijd 
één van de twee blokken `<acties>` uitgevoerd:
-   Als de boolean expressie `True` is, wordt het blok code onder de `if` uitgevoerd
    en wordt het blok code onder de `else` overgeslagen.
-   Als de boolean expressie `False` is, wordt het blok code onder de `if` overgeslagen
    en wordt het blok code onder de `else` uitgevoerd.

Zo kun je bijvoorbeeld gebruik maken van een `if` - `else` constructie om te testen 
of een integer even of oneven is. De modulo operator kan hierbij helpen:
als `x % 2` nul is, dan is `x` even, en anders is `x` oneven.

### Meer-weg beslissingen: `if` - `elif` - `else` constructie

Bij een `if` - `else` constructie, wordt slechts één blok code uitgevoerd van twee gegeven blokken code. Soms wil je echter dat er één blok code uitgevoerd wordt, niet van twee maar van meerdere blokken code. Dit soort meer-weg beslissingen kun je implementeren met een extra toevoeging aan een `if` statement in de vorm van één of meer `elif` takken (`elif`
staat voor "else if").

```python
leeftijd = 21
if leeftijd < 12:
    print( "Je bent een kind!" )
elif leeftijd < 18:
    print( "Je bent een teenager!" )
elif leeftijd < 30:
    print( "Je bent nog jong!" )
elif leeftijd < 50:
    print( "Beginnen grijze haren te komen?" )
else:
    print( "Wegen de jaren zwaar?" )
```

Verander in de code hierboven de waarde van de variabele `leeftijd` en
één van de andere code blokken zal uitgevoerd worden.

De syntax is (gegeven voor één `elif` maar kan uitgebreid worden met 
meerdere):

```python
if <boolean expressie>:
    <acties>
elif <boolean expressie>:
    <acties>
else:
    <acties>
```

De verschillende tests in een `if`-`elif`-`else` constructie
worden in volgorde uitgevoerd. De eerste boolean expressie die
geëvalueerd wordt als `True` laat het bijhorende blok code uitvoeren.
Daarna slaat Python de rest van de code binnen de constructie over.
De volgende boolean expressies in de constructie worden dus niet meer getest
en bijgevolg worden er ook geen andere blokken code meer
uitgevoerd. Slechts als alle boolean expressies in de
constructie `False` blijken te zijn, wordt het blok code bij de `else`
uitgevoerd.

Het toevoegen van `else` is optioneel. De laatste tak binnen de constructie
mag dus ook een `elif` tak zijn.

### Geneste condities

Het is mogelijk om `if` statements op te nemen in de code
blokken van een andere `if` statement. Zo'n geneste `if` wordt
alleen uitgevoerd als de boolean expressie die hoort bij het code blok
waarin de geneste `if` staat `True` is.

```python
x = 41
if x%7 == 0:
    # --- Hier begint een genest blok code  ---
    if x%11 == 0:
        print( x, "is deelbaar door 7 en 11." )
    else:
        print( x, "is deelbaar door 7, maar niet door 11." )
    # --- Hier eindigt een genest blok code ---
elif x%11 == 0:
    print( x, "is deelbaar door 11, maar niet door 7." )
else:
    print( x, "is niet deelbaar door 7 of 11." )
```

Onderstaand voorbeeld is een voorbeeld waarbij eveneens gewerkt wordt met geneste `if`
statements.

```python
leeftijd = 21
if leeftijd < 12:
    print( "Je bent een kind!" )
else:
    if leeftijd < 18:
        print( "Je bent een teenager!" )
    else:
        if leeftijd < 30:
            print( "Je bent nog jong!" )
        else:
            if leeftijd < 50:
                print( "Beginnen grijze haren te komen?" )
            else:
                print( "Wegen de jaren zwaar?" )
```

Het nesten van `if` statements kan vaak vermeden worden
door `elif`s te gebruiken. De code in het bovenstaand voorbeeld doet
hetzelfde als de "leeftijd" code gegeven onder het deel over de meer-weg beslissingen.
Ik neem aan dat je het ermee eens bent dat de versie met `elif`'s
prettiger leest.


[^5]: In veel programmeertalen worden blokken code door de compiler
    herkend doordat ze beginnen en eindigen met een speciaal symbool of
    gereserveerd woord: in talen als Java en C++ worden
    blokken code omsloten door accolades, in talen als Pascal en
    Modula beginnen ze met het woord `begin` en eindigen met het woord
    `end`. Ook al is correct inspringen in deze talen niet noodzakelijk, toch
    doen programmeurs dit meestal, ongeacht de taal die ze gebruiken. Dit maakt de 
    code overzichtelijker en duidelijker: je ziet meteen welke delen van de code bij elkaar
    horen. Bij Python is het inspringen wel een verplichting.

### Stroomdiagrammen

Vroeger stelden programmeurs een "stroomdiagram" op om
algoritmes te beschrijven. Dit stroomdiagram gebruikten ze dan als leidraad bij het uitschrijven van de code.  

Een stroomdiagram is een visuele, schematische weergave van de werking van een code. 
Hierbij wordt gebruik gemaakt van blokken die met elkaar verbonden worden door pijlen.
De vorm van het blok bepaalt de functie ervan.
De drie belangrijkste soorten zijn:
-   een rechthoekig blok met afgeronde hoeken: bevat de tekst "Start" of "Stop" en geeft 
    ofwel de start ofwel het einde van het algoritme aan;
-   een rechthoekig blok: bevat statements die uitgevoerd worden;
-   een ruitvormig blok: bevat een conditie die geëvalueerd wordt als `True` of `False`.

Om een stroomdiagram te interpreteren, begin je bij het "Start" blok, en
volg je de pijlen, waarbij je ieder statement dat je tegenkomt uitvoert.
Bij een ruitvormig blok evalueer je de conditie die erin
staat en volg je ofwel de pijl die met `True` gemarkeerd is als de
conditie `True` is, ofwel de pijl die met `False` gemarkeerd is als de
conditie `False` is. Wanneer je het "Stop" blok tegenkomt, ben je klaar.

![meer-weg beslissing](media/Chart2nl.png "meer-weg beslissing"){:width="45%" data-caption="Stroomdiagram dat een meer-weg beslissing weergeeft."}

Bovenstaand stroomdiagram hoort bij de "leeftijd" code die eerder in dit hoofdstuk werd uitgewerkt.
