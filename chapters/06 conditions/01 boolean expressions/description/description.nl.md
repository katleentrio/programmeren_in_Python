Een "conditionele statement", vaak een "if"-statement genoemd, bestaat uit
een test gevolgd door één of meerdere acties. De test is een zogeheten "boolean
expressie" en kan slechts twee uitkomsten hebben: "waar" of "onwaar".
De acties die beschreven worden in het if-statement, worden alleen uitgevoerd
als het resultaat van de test "waar" is.

We verduidelijken dit aan de hand van een voorbeeld. Een app op een smartphone 
geeft een waarschuwing als de batterij minder dan 5% vol is. Dat betekent
dat de app test of een zekere variabele `batterij_energie` kleiner is
dan $$5$$, dus of de vergelijking `batterij_energie < 5` als resultaat
"waar" heeft. Is de waarde van de variabele nu $$17$$ dan evalueert de test
"onwaar" en hoeft er geen melding gegeven te worden.

### Booleans

Een "boolean" is een data type dat slechts twee waarden kan aannemen:
`0` of `1`, `False` of `True`, `off` of `on`. Welke waarde er precies
kan gebruikt worden, is afhankelijk van de omgeving. In Python
wordt "waar" weergegeven door de waarde `True`, en "onwaar"
door de waarde `False`. Alles wat niet `False` is, is automatisch `True`.

Het data type van het resultaat van een test is altijd een boolean.
In Python wordt dit data type weergegeven met `bool`.

The volgende waarden worden beschouwd als zijnde `False`:

-   De speciale waarde `False`

-   De speciale waarde `None`

-   Iedere numerieke waarde die nul is, bijvoorbeeld 0 en 0.0

-   Iedere lege serie, bijvoorbeeld een lege string (`""`)

-   Iedere functie of methode die één van de bovenstaande waarden
    retourneert (inclusief functies die niets retourneren)

Iedere andere waarde wordt beschouwd als zijnde `True`.

Een expressie die evalueert als `True` of `False` noemen we een "boolean
expressie".

### Vergelijkingen

De meest gebruikte boolean expressies zijn vergelijkingen. Een
vergelijking bestaat uit twee waarden met een vergelijkingsoperator
ertussen. De vergelijkingsoperatoren zijn:

| operator | omschrijving |
|:--------:|-------------|
|        `==`  | gelijk aan |
|        `!=` |  niet gelijk aan |
|        `<`  |    kleiner dan |
|        `<=` |  kleiner dan of gelijk aan |
|        `>`  |  groter dan |
|        `>=` |  groter dan of gelijk aan |

{:class="table table-striped table-condensed" style="width:auto;margin-left:auto;margin-right:auto;"}

Let er op dat je de vergelijkingsoperator "gelijk aan" correct noteert: deze
bestaan uit twee gelijkheidstekens $$==$$! De enkele $$=$$ is de assignment operator.
Meestal geeft Python een syntax of runtime error als je $$=$$ probeert te
gebruiken om twee waarden te vergelijken.

Je kunt vergelijksoperatoren zowel tussen getallen als tussen strings
gebruiken. Vergelijkingen tussen strings zijn alfabetische vergelijkingen
waarbij "a" kleiner beschouwd wordt dan "z", hoofdletters altijd kleiner
beschouwd worden dan kleine letters, en cijfers kleiner dan alle letters.

Hieronder worden een aantal voorbeelden gegeven van vergelijkingen. Elke
vergelijking resulteert in een `False` of `True`. Vind je zelf het juiste resultaat?

```python
print( "1.", 2 < 5 )
print( "2.", 2 <= 5 )
print( "3.", 3 > 3 )
print( "4.", 3 >= 3 )
print( "5.", 3 == 3.0 )
print( "6.", 3 == "3" )
print( "7.", "syntax" == "syntax" )
print( "8.", "syntax" == "semantiek" )
print( "9.", "syntax" == " syntax" )
print( "10.", "Python" != "rotzooi" )
print( "11.", "Python" > "Perl" )
print( "12.", "banaan" < "mango" )
print( "13.", "banaan" < "Mango" )
```

1-True 2-True 3-False 4-True 5-True 6-False	7-True 8-False 9-False 10-True
11-True 12-True 13-False. Zorg dat je begrijpt waarom ze deze uitkomsten geven.
Begrijp je ook waarom `3 < 13` `True` oplevert, maar `"3" < "13"` `False`?

Je kunt de uitkomst van een boolean expressie aan een variabele
toekennen als je wilt:

```python
groter = 5 > 2
print( groter )
groter = 5 < 2
print( groter )
print( type( groter ) )
```

Vergelijkingen tussen data types die niet met elkaar vergeleken kunnen worden,
leiden meestal tot runtime errors.

```python
# Deze code geeft een runtime error.
print( 3 < "3" )
```

### `in` operator

Python heeft een speciale operator die de "membership test operator"
heet. Meestal wordt deze verkort de "in operator" genoemd aangezien
hij gecodeerd wordt als `in`. De `in` operator test of een waarde
voorkomt in een verzameling. De waarde wordt aan de linkerzijde van
de `in` genoteerd, de verzameling aan de rechterzijde.

Er zijn verschillende soorten verzamelingen in Python. Wij beperken ons
hier echter tot de string. Een string kan beschouwd worden als een verzameling
van tekens. Je kunt testen of een specifiek teken (of een groep tekens)
deel uitmaakt van een string met behulp van de `in` operator. De
tegenhanger van de `in` operator is de `not in` operator die `True`
oplevert als `in` `False` oplevert, en vice versa. Een voorbeeld:

```python
print( "y" in "Python" )
print( "x" in "Python" )
print( "p" in "Python" )
print( "th" in "Python" )
print( "to" in "Python" )
print( "y" not in "Python" )
```

De evaluaties geven volgende resultaten: True False False True False False.
Merk op dat er een onderscheid wordt gemaakt tussen grote en kleine letters.

### Logische operatoren

Meerdere boolean expressies kunnen gecombineerd worden door gebruik te
maken van logische operatoren. Er zijn drie logische operatoren:
`and`, `or`, en `not`.

`and` en `or` plaats je tussen twee boolean expressies.

Als `and` tussen twee boolean expressies staat, is het resultaat `True`
als beide expressies `True` zijn; anders is het resultaat `False`.

Als `or` tussen twee boolean expressies staat, is het resultaat `True`
als één of beide expressies `True` is; het resultaat is alleen `False`
als beide `False` zijn.

`not` kun je voor een boolean expressie plaatsen om hem om te keren van
`True` naar `False` en vice versa.

Bedenk nu wat er telkens wordt afgeprint in volgende voorbeelden?

```python
t = True
f = False
print( t and t )
print( t and f )
print( f and t )
print( f and f )
print( t or t )
print( t or f )
print( f or t )
print( f or f )
print( not t )
print( not f )
```

True, False, False, False, True, True, True, False, False, True

Je kunt een combinatie van `and`s en `or`s gebruiken. De boolean
expressies worden dan van links naar rechts geëvalueerd. Opgelet,
een combinatie van `and`s en `or`s kan leiden tot onverwachte
resultaten. Hou daarom de expressies zo eenvoudig mogelijk en
gebruik haakjes om te zorgen dat ze in de gewenste volgorde
geëvalueerd worden: in plaats van `a and b or c` te schrijven, moet je
`(a and b) or c` of `a and (b or c)` schrijven afhankelijk van de
gewenste volgorde. Het gebruik van haakjes maakt de code bovendien
makkelijker leesbaar. Zo is het voor iedereen duidelijk in welke volgorde
de evaluaties worden uitgevoerd. Haakjes hoef je uiteraard niet te
plaatsen wanneer je een logische expressie maakt met alleen `and`s,
of alleen `or`s, want dan is de evaluatie duidelijk.

Geef in de volgende code waarden aan `a`, `b`, en `c` die ertoe
leiden dat de twee expressies verschillende uitkomsten hebben.

```python
a = # True of False?
b = # True of False?
c = # True of False?

print( (a and b) or c )
print( a and (b or c) )
```

Zoals eerder aangehaald worden boolean expressies van links naar rechts
geëvalueerd. Python stopt de evaluatie op het moment dat de uitkomst van
de evaluatie bekend is. Neem bijvoorbeeld de volgende code:

```python
x = 1
y = 0
print( (x == 0) or (y == 0) or (x / y == 1) )
```

Python evalueert de boolean expressie van links naar rechts. De gegeven
expressie is een combinatie van `or`s. Deze expressie zal dus `True` als
resultaat hebben indien één van de componenten `True` is. `y == 0`
evalueert `True` dus is het niet nodig dat Python de laatste evaluatie
nog uitvoert en dus stopt Python na `y == 0`.
Merk op dat Python in dit geval enkel evaluaties uitvoert op de boolean expressies
en niet kijkt naar resultaten van de berekeningen. Een berekening resulteert in een
runtime error bij een nuldeling zoals het geval is bij `x / y == 1` (`y` is nul).
Vermits hier een boolean expressie wordt geevalueerd geeft de code echter geen
foutmelding. 
