We bekijken een aantal basis functies.

### Type casting

Eerder werd al gesproken over type casting functies. We bekijken dit meer
in detail.

-   `float()` heeft één parameter en geeft als return value een floating-point
    representatie van de waarde van de parameter. Als de waarde een
    integer is, krijg je dezelfde waarde terug als float. Als de
    parameter een float is, krijg je dezelfde waarde terug. Als de
    parameter een string bevat die je als integer of float zou kunnen
    interpreteren, dan krijg je die float terug als waarde. Anders krijg
    je een runtime error.

-   `int()` heeft één parameter en geeft als return value een integer 
    representatie van de waarde van de parameter. Als de waarde een integer is,
    krijg je dezelfde waarde terug. Als de waarde een float is, krijg je een
    integer terug die de waarde van de float *naar beneden* heeft
    afgerond. Als de parameter een string bevat die je als integer zou
    kunnen interpreteren, dan krijg je die integer terug als waarde.
    Anders krijg je een runtime error.

-   `str()` heeft één parameter en geeft als return value een string
    representatie van de waarde van de parameter.

Wat doet de volgende code?

```python
print( 10 * int( "100,000,000" ) )
```

Pas de code aan zodat er runtime error meer verschijnt en het juiste resultaat wordt afgedrukt op het scherm.

### Berekeningen

Een paar basis Python functies helpen bij berekeningen.

-   `abs()` heeft een numerieke parameter en geeft als
    return value de absolute waarde van de parameter.

-   `max()` heeft twee of meer numerieke parameters (gescheiden door een komma) en geeft als
    return value de grootste.

-   `min()` heeft twee of meer numerieke parameters (gescheiden door een komma) en geeft als
    return value de kleinste.

-   `pow()` heeft twee numerieke parameters en geeft als return value
    de eerste parameter verheven tot de macht weergeven door de tweede.

-   `round()` heeft een numerieke parameter die wiskundig wordt
    afgerond. Optioneel mag je als tweede parameter een integer meegeven
    die aangeeft **hoeveel cijfers na de komma** gegeven moeten worden.
    Als de tweede parameter niet wordt meegegeven, wordt afgerond op
    gehele getallen.

Bekijk de code hieronder en bedenk wat er op het scherm getoond wordt. Test in Spyder.

```python
x = -2
y = 3
z = 1.27

print( abs( x ) )
print( max( x, y, z ) )
print( min( x, y, z ) )
print( pow( x, y ) )
print( round( z, 1 ) )
```

### `len()`

`len()` is een basis functie die één parameter heeft en de lengte
van die parameter teruggeeft. Deze functie wordt meestal toegepast op een string waarvan je de
lengte terugkrijgt. 

Wat print de code hieronder? Zoek eerst zelf het antwoord; doe dan de test in Spyder.

```python
print( len( 'man' ) )
print( len( 'mango' ) )
print( len( "" ) )  # "" is een lege string
print( len( 'mango\'s' ) )
```

### `input()`

Veel programma's willen gegevens krijgen van de gebruiker om verder te verwerken.
Deze gegevens kan je opvragen met behulp van de functie `input()`.

De functie heeft één **parameter: een string waarin gevraagd wordt naar de nodige data**.
Deze string is de **"prompt"**; de tekst die verschijnt aan de gebruiker.
Wanneer nu `input()` wordt aangeroepen, verschijnt de prompt op het scherm. De gebruiker geeft zijn
data in (mag ook niets zijn) en sluit de invoer af door op `Enter` te drukken.
De **return value** van de functie is de **data ingevoerd door de gebruiker, exclusief de `Enter`.** De return value  van de functie is **steeds een string.**

Afhankelijk van de omgeving waarin je werkt, kan de prompt er anders uit zien.
Dit kan een popup-window zijn waarin de gebruiker moet typen, het is ook mogelijk dat de gebruiker de ingave op een command-line moet typen. Dit laatste is het geval bij gebruik van Spyder.

Hier is een voorbeeld:

```python
tekst = input( "Geef een tekst in: " )
print( "Je hebt het volgende ingetypt:", tekst )
```

**Realiseer je dat `input()` altijd een string teruggeeft.** Bekijk de
volgende code:

```python
nummer = input( "Geef een getal: " )
print( "Je getal in het kwadraat is", nummer * nummer )
```

Deze code geeft ALTIJD een runtime error. Vermits `input()` een string
teruggeeft (ook al voer je een getal in!), wordt op de tweede regel een
poging gedaan twee strings met elkaar te vermenigvuldigen wat niet kan.
**Je kunt dit probleem oplossen door gebruik te maken van type casting**:

```python
nummer = input( "Geef een getal: " )
nummer = float( nummer )
print( "Je getal in het kwadraat is", nummer * nummer )
```

Deze code werkt indien de gebruiker een getal ingeeft; als de gebruiker
iets ingeeft dat niet in een getal omgezet kan worden, krijg je toch weer
een runtime error.

### `print()`

De functie `print()` heeft nul of meer parameters, toont ze op het
scherm (als het er meerdere zijn met spaties ertussen) en gaat daarna
naar de volgende regel. Dus als je twee `print` statements gebruikt,
komt de output van de tweede onder die van de eerste te staan.
Als `print()` wordt aangeroepen zonder parameters, gaat de functie
alleen naar de volgende regel. Zo kun je lege regels op het scherm
zetten.

`print()` kan twee speciale parameters meekrijgen, die `sep` en
`end` heten.

**`sep`** geeft aan wat er getoond moet worden tussen iedere twee
parameters; default is dit een spatie. Je kunt die spatie wijzigen in
iets anders via `sep`.

**`end`** geeft aan wat `print()` moet uitvoeren nadat alle parameters zijn
getoond; default gaat hij naar een "nieuwe regel." Door `end` te wijzigen
kun je ervoor zorgen dat `print()` iets anders doet.

Om `sep` en `end` te gebruiken, moet je de parameters `sep=<string>` en/of
`end=<string>` opnemen. *(opmerking: als in een beschrijvende tekst van code iets tussen `<>` staat, moet je de haakjes niet letterlijk over typen maar vervangen door wat de term tussen de `<>` aangeeft, dus `<string>` betekent dat je daar een string moet typen.)*
Een voorbeeld met gebruikt van `sep` en `end`:

```python
print( "X", "X", "X", sep="x" )
print( "X", end="" )
print( "Y", end="" )
print( "Z" )
```

Test dit uit. Je zal zien dat na uitvoer de eerste regel "XxXxX" bevat: drie keer hoofdletter "X"
gescheiden door een kleine letter "x", waarna wordt overgegaan naar een
nieuwe regel.
De tweede regel bevat "XYZ": na aanroepen van de `print()` "X" en "Y",
wordt niet naar een volgende regel gegaan; na "Z" wel.

### `format()`

De laatste functie die wer hier bespreken is de `format()` functie. Deze maakt het mogelijk een geformatteerde string
te bouwen, dus een string met opmaak. 

We illustreren het aanpassen van de opmaak met een eenvoudig voorbeeld waarbij
je de `format()` functie nog niet nodig hebt. 
Je wilt de uitkomst van de volgende berekening tonen (float):

```python
print( 7/11 )
```

Als je de uitkomst moet tonen met 3 decimalen kan dit door te werken
met de `round()` functie. Bijvoorbeeld:

```python
print( round( 7/11, 3 ) )
```

Met behulp van de `format()` functie kan je nog veel meer aanpassingen aanbrengen.
Het is wel een nogal complexe functie die op een speciale manier
gebruikt moet worden. In het vervolg van deze tekst wordt hier dieper op ingegaan.
**Voor ons gebruik van Python, is de opmaak echter niet prioritair. Je mag de uitleg bij deze functie dan ook overslaan en verder gaan met de volgende activiteit. Weet dat je hier altijd extra info kan terugvinden. Ben je nieuwsgierig en wil je hier toch meer over weten, mag je je uiteraard verder verdiepen in deze functie.**

Stel bijvoorbeeld dat je 10 posities ruimte moet reserveren voor deze uitkomst, 
en dat binnen deze 10 posities de uitkomst links moet uitgelijnd zijn. Dit lijkt
moeilijk realiseerbaar maar de `format()` functie maakt het mogelijk om
verschillende manieren van opmaak van het resulaat te combineren.
We bespreken hieronder een aantal mogelijkheden voor het gebruik van
de `format()` functie.

De `format()` functie wordt niet alleen aangestuurd via parameters
(zoals bij de eerder besproken functies), maar werkt bovendien enkel 
met een bepaald data type nl. "string". Dit soort functies -"methodes" genoemd-
worden anders aangeroepen dan diegene die we eerder behandelden. Hierbij is het
belangrijkste dat je weet dat je een variabele (of waarde)
van het juiste data type vóór de functienaam plaatst, met een punt tussen
de variabele en de naam van de functie. Die variabele (of waarde) zelf is
ook beschikbaar voor de methode, net als de parameters.

De `format()` methode wordt als volgt aangeroepen:
**`<string>.format()`**. De return value is een nieuwe string die een
geformatteerde versie is van de string waarvoor de methode is
aangeroepen.

`format()` kan een willekeurig aantal **parameters** meekrijgen (tussen
de haakjes), die in de geformatteerde string ingebracht kunnen worden
op specifieke **plaatsen**. De plaatsen waar `format()` de parameterwaarden
in de string plaatst, worden in de string aangegeven door middel van
accolades `{}`. Als je niets typt tussen de accolades in de string `{}`,
worden de parameters van links naar rechts verwerkt. Bijvoorbeeld:

```python
    print( "De eerste drie getallen zijn {}, {} en {}.".format( 
        "een", "twee", "drie" ) )
    """ let op de syntax: de methode wordt toegepast binnen een print() functie.
    Voor het punt staat de string die je wilt opmaken, na het punt volgt
    de benaming van de methode format() met tussen de haakjes de parameters."""
```

Als resultaat wordt op het scherm "De eerste drie getallen zijn een, twee en drie."
afgedrukt. Wens de volgorde waarin de parameters in de zin verschijnen aan te passen,
dan plaats je een getal tussen de accolades: het plaatsnummer van de parameter.
De plaats van de eerste parameter is 0, van de tweede 1, van de derde 2, enz.
Bijvoorbeeld:

```python
print( "Achterwaarts zijn ze {2}, {1} en {0}.".format( 
    "een", "twee", "drie" ) )
```

Het resultaat wordt nu "Achterwaarts zijn ze drie, twee en een."

`format()` kan variabelen van ieder type verwerken zolang ze maar een
string representatie hebben. Zo kan `format()` ook
getallen verwerken, maar ook verschillende soorten data types mixen:

```python
print( "De eerste drie getallen zijn {}, {} en {}.".format( 
    1, "twee", 3.0 ) )
```

Door gebruik te maken van de `format()` methode kunnen we een opmaak geven
aan de parameters door middel van formatteringsinstructies. Dit gebeurt
voor elke parameter afzonderlijk en wordt ingevoerd tussen de accolades.
Na het plaatsnummer (indien van toepassing) typ je een dubbele-punt (:),
gevolgd door de formatteringsinstructies. We bespreken er een paar.

De eerste instructies zijn **formateringsinstructies voor string parameters**.
Wanneer je een bepaalde vaste plaats (een vaste hoeveelheid tekens)
wilt reserveren voor een string, dan kun je dat aangeven door een integer
rechts van de dubbele-punt in te voeren. Dit wordt de **"precisie"**
genoemd. De volgende code gebruikt een precisie van 7.

```python
print( "De eerste drie getallen zijn {:7}, {:7} en {:7}.".format( 
    "een", "twee", "drie" ) )
""" de parameters worden van links naar rechts ingevoerd.
Voor elke parameter wordt dezelfde plaats gebruikt: de plaats van 7 tekens; al dan niet leeg"""
```

Wanneer nu de opgegeven precisie te kort is voor de lengte van de string,
past `format()` de ruimte aan zodat de string volledig wordt weergegeven.
Je kunt de precisie dus niet gebruiken om een string voortijdig af te breken.

Wanneer je precisie gebruikt, kun je de parameter **"uitlijnen"** in de
gereserveerde ruimte. Dit doe je door een "alignment" teken te plaatsen
tussen het dubbele-punt en de precisie. De "alignment" tekens zijn 
`<` voor links uitlijnen, `^` voor centreren en `>` voor rechts uitlijnen.

```python
print( "De eerste drie getallen zijn {:<7}, {:^7} en {:>7}.".
    format( "een", "twee", "drie" ) )
```

De volgende **formatteringsinstructies** gelden **voor getallen**. Je kunt een 
**data type** toekennen aan een getal: voor een integer plaats je de kleine letter
"d" rechts van het dubbele-punt ("d" staat voor "decimaal"), voor een float
plaats je een "f" rechts van het dubbele-punt. `format()`
maakt de juiste conversie als dit kan. Je kunt echter geen integer van 
een float maken; dit veroorzaakt een runtime error.

```python
print( "{} gedeeld door {} is {}".format( 1, 2, 1/2 ) )
print( "{:d} gedeeld door {:d} is {:f}".format( 1, 2, 1/2 ) )
print( "{:f} gedeeld door {:f} is {:f}".format( 1, 2, 1/2 ) )
```

De volgende resultaten verschijnen na uitvoer:
"1 gedeeld door 2 is 0.5", "1 gedeeld door 2 is 0.500000" en
"1.000000 gedeeld door 2.000000 is 0.500000".

Ook voor getallen kun je **precisie** en **uitlijning** gebruiken. Dit doe je op
dezelfde manier als bij strings. Let erop dat een eventueel min-teken
ook een plaats nodig heeft, net als een eventueel punt in een float.

```python
print( "{:5d} gedeeld door {:5d} is {:5f}".format( 1, 2, 1/2 ) )
print( "{:<5f} gedeeld door {:^5f} is {:>5f}".format( 1,2,1/2 ))
```

Tenslotte, kun je het **aantal decimalen** aangeven waarmee een float getoond moet worden.
Dit doe je door een punt en een getal te plaatsen links van de letter "f".
De `format()` methode zal het getal afronden tot het gevraagde aantal decimalen.
Wanneer je nul decimalen wilt zien door `.0` te gebruiken, wordt de float als een integer getoond.

```python
print( "{:.2f} gedeeld door {:.2f} is {:.2f}".format( 1,2,1/2 ))
```

"1.00 gedeeld door 2.00 is 0.50" wordt getoond op het scherm.
In volgende toepassing wordt afgerond op drie decimalen:

```python
print( "{:.3f}".format( 7/11 ) )
```

De combinatie van precisie, uitlijning, en decimalen staat je toe om
redelijk uitziende tabellen te tonen.

```python
s = "{:>5d} keer {:>5.2f} is {:>5.2f}"
print( s.format( 1, 3.75, 1 * 3.75 ) )
print( s.format( 2, 3.75, 2 * 3.75 ) )
print( s.format( 3, 3.75, 3 * 3.75 ) )
print( s.format( 4, 3.75, 4 * 3.75 ) )
print( s.format( 5, 3.75, 5 * 3.75 ) )
```
