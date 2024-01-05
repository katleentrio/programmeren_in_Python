Een "conditionele statement" (voorwaarde), vaak een "if"-statement genoemd, bestaat uit
een test, gevolgd door één of meerdere acties. De test is een zogeheten "boolean
expressie" en kan slechts twee uitkomsten hebben: "waar" of "onwaar".
De acties die beschreven worden in het if-statement, worden alleen uitgevoerd
als het resultaat van de test "waar" is.

We verduidelijken dit aan de hand van een voorbeeld. Een app op een smartphone 
geeft een waarschuwing als de batterij minder dan 5% vol is. Dat betekent
dat de app een test uitvoert op een variabele `batterij_energie` en controleert of de waarde
van deze variabele kleiner is dan $$5$$; m.a.w. heeft de vergelijking `batterij_energie < 5` als resultaat "waar" dan zal de waarschuwing verschijnen. Is de waarde van de variabele $$17$$ dan is het resultaat van de test
"onwaar" en hoeft er geen melding gegeven te worden.

We gaan eerst dieper in op de ""boolean expressie -de test die uitgevoerd moet worden- vooraleer we in volgend hoofdstukje uitleggen hoe een "conditionele statement" wordt opgebouwd.

### Boolean

Een "boolean" is -net als een integer, float of string- een data type. 
**Data van het type "boolean" kan slechts twee waarden aannemen: `0` of `1`, `False` of `True`, `off` of `on`.** 
In Python wordt "waar" weergegeven door de waarde `True`, en "onwaar"
door de waarde `False`. **Alles wat niet `False` is, is automatisch `True`.**

Het data type van het resultaat van een test is altijd een boolean.
In Python wordt dit data type weergegeven met `bool`.

Iedere waarde wordt beschouwd als `True`, met uitzondering van de volgende waarden die worden beschouwd als `False`:

-   De speciale waarden `False`, `None`

-   Iedere numerieke waarde die nul is, bijvoorbeeld 0 en 0.0

-   Iedere lege serie, bijvoorbeeld een lege string (`""`)

-   Iedere functie of methode die één van de bovenstaande waarden
    retourneert (inclusief functies die niets retourneren)

**Een expressie die evalueert als `True` of `False` noemen we een "boolean expressie".**

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

**Let er op dat je de vergelijkingsoperator "gelijk aan" correct noteert: deze bestaan uit twee gelijkheidstekens $$==$$!**
 *Het enkel gelijkheidsteken $$=$$ is de assignment operator (kent een waarde toe aan een variabele). Meestal geeft Python een syntax of runtime error als je $$=$$ probeert te gebruiken om twee waarden met elkaar te vergelijken.*

Je kunt vergelijksoperatoren zowel tussen getallen als tussen strings
gebruiken. Vergelijkingen tussen strings zijn alfabetische vergelijkingen
waarbij "a" kleiner beschouwd wordt dan "z", hoofdletters altijd kleiner
beschouwd worden dan kleine letters, en cijfers kleiner dan alle letters.

Hieronder worden een aantal voorbeelden gegeven van vergelijkingen. Elke
vergelijking resulteert in een `False` of `True`. Vind je zelf het juiste resultaat? Controleer in Spyder.

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

Begrijp je ook waarom `3 < 13` `True` oplevert, maar `"3" < "13"` `False`?

Je kunt de uitkomst van een boolean expressie aan een variabele
toekennen als je wilt:

```python
groter = 5 > 2
print( groter )   # True wordt geprint
groter = 5 < 2
print( groter )   # False wordt geprint
print( type( groter ) )   # 'Bool' wordt geprint
```

Vergelijkingen tussen data types die niet met elkaar vergeleken kunnen worden,
leiden meestal tot runtime errors.

```python
# Deze code geeft een runtime error.
print( 3 < "3" )
```

### Logische operatoren

Meerdere boolean expressies kunnen gecombineerd worden door gebruik te
maken van logische operatoren. De drie logische operatoren ken je reeds vanuit wiskunde:
`and`, `or`, en `not`.

`and` en `or` plaats je tussen twee boolean expressies.
-   Bij het gebruik van `and` is het resultaat `True` als beide expressies `True` zijn; 
    in alle andere gevallen is het resultaat `False`
-   Bij het gebruik van `or` is het resultaat `False` als beide expressies `False` zijn; 
    in alle andere gevallen is het resultaat `True`

`not` kun je voor een boolean expressie plaatsen om hem om te keren van
`True` naar `False` en vice versa.

Bedenk nu wat er telkens wordt afgeprint in volgende voorbeelden. Test uit in Spyder.

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

Je kunt een combinatie van `and`s en `or`s gebruiken. Zonder gebruik van haakjes in je notatie worden de boolean expressies van links naar rechts geëvalueerd. Heb je een andere volgorde nodig, gebruik dan haakjes: in plaats van `a and b or c` te schrijven, moet je
`(a and b) or c` of `a and (b or c)` schrijven afhankelijk van de
gewenste volgorde. Het gebruik van haakjes maakt de code bovendien
makkelijker leesbaar. 

Zoals eerder aangehaald, worden boolean expressies van links naar rechts
geëvalueerd. Python stopt de evaluatie op het moment dat de uitkomst van
de evaluatie bekend is. Neem bijvoorbeeld de volgende code:

```python
x = 1
y = 0
print( (x == 0) or (y == 0) or (x / y == 1) )
```

Python evalueert de boolean expressie van links naar rechts. De gegeven
expressie is een combinatie van `or`s. Het resultaat van deze expressie is `True` als
één van de componenten `True` is. `y == 0`
evalueert `True` dus is het niet nodig dat Python de laatste evaluatie
nog uitvoert en dus stopt Python na `y == 0`.
*Merk op dat Python in dit geval enkel evaluaties uitvoert op de boolean expressies en niet kijkt naar resultaten van de berekeningen. Een berekening resulteert in een runtime error bij een nuldeling zoals het geval is bij `x / y == 1` (`y` is nul). Vermits hier een boolean expressie wordt geevalueerd geeft de code echter geen foutmelding.*

### `in` operator

**Binnen de toepassingen waarvoor wij Python gebruiken, is de `in` operator minder belangrijk. Je mag de uitleg bij dit onderdeel dan ook overslaan en meteen overgaan naar de volgende activeit. Wil je je hier toch verder in verdiepen, kan dit uiteraard altijd door de rest van de tekst door te nemen.**

Python heeft een speciale operator die de "membership test operator"
heet. Meestal wordt deze verkort de "in operator" genoemd en wordt gecodeerd als `in`.
De `in` operator test of een waarde voorkomt in een verzameling. De waarde wordt aan de linkerzijde van de `in` genoteerd, de verzameling aan de rechterzijde.

Een string kan beschouwd worden als een verzameling van tekens. 
Met behulp van de `in` operator kun je dus testen of een specifiek teken
(of een groep tekens) deel uitmaakt van een string. De
tegenhanger van de `in` operator is de `not in` operator die `True`
oplevert als `in` `False` oplevert, en vice versa. 

Een voorbeeld:

```python
print( "y" in "Python" )
print( "x" in "Python" )
print( "p" in "Python" )
print( "th" in "Python" )
print( "to" in "Python" )
print( "y" not in "Python" )
```

De evaluaties geven volgende resultaten: True False False True False False.
**Merk op dat er een onderscheid wordt gemaakt tussen grote en kleine letters.**
