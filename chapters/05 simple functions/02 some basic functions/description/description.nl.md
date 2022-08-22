We bekijken een aantal basis functies.

### Type casting

Eerder heb ik al gesproken over type casting functies. We gaan hier meer
in detail op in.

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
    integer terug die de waarde van de float naar beneden heeft
    afgerond. Als de parameter een string bevat die je als integer zou
    kunnen interpreteren, dan krijg je die integer terug als waarde.
    Anders krijg je een runtime error.

-   `str()` heeft één parameter en geeft als return value een string
    representatie van de waarde van de parameter.

Wat doet de volgende code?

```python
print( 10 * int( "100,000,000" ) )
```

De code hierboven geeft een runtime error.
Welke twee tekens moet je verwijderen om dit probleem op te lossen ?
*(de twee komma's)*

### Berekeningen

Een paar basis Python functies helpen bij berekeningen.

-   `abs()` krijgt een numerieke parameter waarde en en geeft als
    return value de absolute waarde van de parameter (is de waarde
    positief wordt hij geretourneerd, is de waarde negatief
    wordt de waarde vermenigvuldigd met -1 geretourneerd).

-   `max()` krijgt twee of meer numerieke parameters en geeft als
    return value de grootste.

-   `min()` krijgt twee of meer numerieke parameters en geeft als
    return value de kleinste.

-   `pow()` krijgt twee numerieke parameters en geeft als return value
    de eerste verheven tot de macht weergeven door de tweede. Optioneel
    mag je een derde parameter meegeven die een integer moet zijn. Als je dat
    doet, krijg je de waarde modulo de derde parameter terug.

-   `round()` krijgt een numerieke parameter die wiskundig wordt
    afgerond. Optioneel mag je als tweede parameter een integer meegeven
    die aangeeft hoeveel cijfers achter de komma behouden moeten worden.
    Als de tweede parameter niet wordt meegegeven, wordt afgerond op
    gehele getallen.

Bekijk de code hieronder en bedenk wat er op het scherm getoond wordt.

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

`len()` is een basis functie die één parameter krijgt en de lengte
van die parameter teruggeeft. Op dit moment is het enig zinvolle data
type dat je mee kunt geven aan `len()` een string waarvan je de
lengte krijgt. 

Wat print de code hieronder?

```python
print( len( 'man' ) )
print( len( 'mango' ) )
print( len( "" ) )  # "" is een lege string
print( len( 'mango\'s' ) )
```

*Antwoorden: 3, 5, 0, 7. Waarom heeft de laatste string een lengte van 7 en niet van 8?*

### `input()`

Veel programma's wensen data te krijgen van de gebruiker om verder te verwerken.
Je kunt de gebruiker vragen om een string in te voeren met behulp
van de functie `input()`. De functie krijgt één parameter: een string.
Deze string is de zogeheten "prompt." Wanneer nu `input()` wordt
aangeroepen, verschijnt de prompt op het schermen. De gebruiker geeft eender
welke tekst in (mag ook niets zijn) en sluit de invoer af door op `Enter` te drukken.
De return value van de functie is de string die de gebruiker heeft
ingegeven, exclusief de `Enter`.

Afhankelijk van de omgeving waarin je werkt, kan de prompt er anders uit zien.
Soms is het een rechthoek op het scherm met de prompt ervoor waarin de gebruiker
mag typen, soms moet de gebruiker de ingave op een command-line doen, soms
verschijnt een popup-window waarin de gebruiker moet typen.

Hier is een voorbeeld:

```python
tekst = input( "Geef een tekst in: " )
print( "Je hebt het volgende ingetypt:", tekst )
```

Realiseer je dat `input()` altijd een string teruggeeft. Bekijk de
volgende code:

```python
nummer = input( "Geef een getal: " )
print( "Je getal in het kwadraat is", nummer * nummer )
```

Deze code geeft ALTIJD een runtime error. Vermits `input()` een string
teruggeeft (ook al voer je een getal in!), wordt op de tweede regel een
poging gedaan twee strings met elkaar te vermenigvuldigen wat niet kan.
Je kunt dit probleem oplossen door gebruik te maken van type casting:

```python
nummer = input( "Geef een getal: " )
nummer = float( nummer )
print( "Je getal in het kwadraat is", nummer * nummer )
```

Deze code werkt indien de gebruiker een getal ingeeft; als de gebruiker
iets ingeeft dat niet in een getal omgezet kan worden, krijg je toch weer
een runtime error.
Verderop in dit hoofdstuk geef ik een methode die je kunt gebruiken om
naar een getal te vragen en je programma niet te laten "crashen" wanneer
de gebruiker iets anders ingeeft.

### `print()`

De functie `print()` krijgt nul of meer parameters mee, toont ze op het
scherm (als het er meerdere zijn met spaties ertussen) en gaat daarna
naar de volgende regel. Dus als je twee `print` statements gebruikt,
komt de output van de tweede onder die van de eerste te staan.
Als `print()` wordt aangeroepen zonder parameters, gaat de functie
alleen naar de volgende regel. Zo kun je lege regels op het scherm
zetten.

`print()` kan twee speciale parameters meekrijgen, die `sep` en `end`
heten.

`sep` geeft aan wat er getoond moet worden tussen iedere twee
parameters; default is dit een spatie. Je kunt die spatie wijzigen in
iets anders via `sep`, inclusief in een lege string.

`end` geeft aan wat `print()` moet uitvoeren nadat alle parameters zijn
getoond; default gaat hij naar een "nieuwe regel." Door `end` te wijzigen
kun je ervoor zorgen dat `print()` iets anders doet.

Om `sep` en `end` te gebruiken, moet je de parameters `sep=<string>` en/of
`end=<string>` opnemen. *(opmerking: als in een beschrijving van code iets tussen `<` en `>` staat, moet je dit niet letterlijk typen maar vervangen door wat de term tussen de `<` en `>` aangeeft, dus `<string>` betekent dat je daar een string moet typen.)*
Een voorbeeld met gebruikt van `sep` en `end`:

```python
print( "X", "X", "X", sep="x" )
print( "X", end="" )
print( "Y", end="" )
print( "Z" )
```

Na uitvoer bevat de eerste regel "XxXxX": drie keer hoofdletter "X"
gescheiden door een kleine letter "x", waarna wordt overgegaan naar een
nieuwe regel.
De tweede regel bevat "XYZ": na aanroepen van de `print()` "X" en "Y",
wordt niet naar een volgende regel gegaan.

### `format()`

`format()` is een nogal complexe functie die op een speciale manier
gebruikt moet worden. De functie staat je toe een geformatteerde string
te bouwen, dus een string met opmaak. We illustreren dit met een voorbeeld.
Je wilt de uitkomst van de volgende berekening tonen (float):

```python
print( 7/11 )
```

Als je de uitkomst moet tonen met 3 decimalen kan dit door te werken
met de `round()` functie. Bijvoorbeeld:

```python
print( round( 7/11, 3 ) )
```

Mogelijk heb je nog meerdere eisen. Stel bijvoorbeeld dat je ook
10 posities ruimte moet reserveren voor deze uitkomst, en dat binnen
deze 10 posities de uitkomst links moet uitgelijnd zijn. Dit lijkt
moeilijk realiseerbaar maar de `format()` functie maakt het mogelijk om
verschillende manieren van opmaak van het resulaat te combineren.
We bespreken hieronder een aantal mogelijkheden voor het gebruik van
de `format()` functie.

De `format()` functie wordt niet alleen aangestuurd via parameters
(zoals bij de eerder besproken functies), maar werkt bovendien enkel 
met een bepaald data type nl. "string". Dit soort functies -"methodes" genoemd-
worden anders aangeroepen dan diegene die we eerder behandelden. Hierbij is het
belangrijkste dat je hoeft te weten dat je een variabele (of waarde)
van het juiste data type vóór de functienaam plaatst, met een punt tussen
de variabele en de naam van de functie. Die variabele (of waarde) zelf is
ook beschikbaar voor de methode, net als de parameters.

De `format()` methode (laten we de correcte benaming gebruiken, het is
geen functie maar een methode) wordt als volgt aangeroepen:
`<string>.format()`. Hij retourneert een nieuwe string, die een
geformatteerde versie is van de string waarvoor de methode is
aangeroepen. `format()` kan een willekeurig aantal parameters
meekrijgen, die in de geformatteerde string ingebracht kunnen worden op
specifieke plaatsen.

De plaatsen waar `format()` de parameter waardes in de string plaatst
worden in de string aangegeven middels accolades (`{` en `}`). Als je
alleen `{}` gebruikt om de parameters aan te duiden, worden ze van
links naar rechts afgehandeld. Bijvoorbeeld:

```python
    print( "De eerste drie getallen zijn {}, {} en {}.".format( 
        "een", "twee", "drie" ) )
```

Als je ze in een andere volgorde wilt afhandelen, kun je de volgorde
bepalen door een getal tussen de acolades te zetten. De eerste parameter
is nummer 0, de tweede nummer 1, de derde nummer 2, etcetera (als je het
vreemd vindt om nummering te beginnen bij nul, weet dan dat dat
gebruikelijk is in programmeertalen, en dat je het nog vaker zult
tegenkomen in dit boek). Bijvoorbeeld:

```python
print( "Achterwaarts zijn ze {2}, {1} en {0}.".format( 
    "een", "twee", "drie" ) )
```

`format()` kan variabelen van ieder type verwerken, zolang ze maar een
fatsoenlijke string representatie hebben. Bijvoorbeeld, `format()` kan
getallen verwerken, en zelfs verschillende soorten data types mixen:

```python
print( "De eerste drie getallen zijn {}, {} en {}.".format( 
    1, "twee", 3.0 ) )
```

Als je de parameters op een specifieke manier wil formatteren, zijn daar
mogelijkheden voor, als je een dubbele-punt (:) tussen de accolades zet,
na het volgorde-nummer als je dat gebruikt, met rechts van de
dubbele-punt formatteringsinstructies. Ik zal een aantal
formatteringsinstructies opnoemen.

Ik begin met instructies voor string parameters. Als je een bepaalde
hoeveelheid tekens wilt reserveren voor een string, dan kun je dat
aangeven met een integer rechts van de dubbele-punt. Dit wordt de
"precisie" genoemd. De volgende code gebruikt een precisie van 7.

```python
print( "De eerste drie getallen zijn {:7}, {:7} en {:7}.".format( 
    "een", "twee", "drie" ) )
```

Als de precisie te kort is voor de lengte van de string, neemt
`format()` gewoon meer ruimte voor de string. Je kunt de precisie dus
niet gebruiken om een string voortijdig af te breken.

```python
print( "De eerste drie getallen zijn {:3}, {:3} en {:3}.".format( 
    "een", "twee", "drie" ) )
```

Als je precisie gebruikt, kun je de parameter links aanlijnen,
centreren, of rechts aanlijnen in de ruimte die je hebt gereserveerd.
Dat doe je door een "alignment" teken te plaatsen tussen de dubbele punt
en de precisie. Deze "alignment" tekens zijn `<` voor links aanlijnen,
`^` voor centreren, en `>` voor rechts aanlijnen.

```python
print( "De eerste drie getallen zijn {:<7}, {:^7} en {:>7}.".
    format( "een", "twee", "drie" ) )
```

Ik ga nu over op formatteringsinstructies voor getallen. Als je een
getal wilt laten interpreteren als een integer, moet je de kleine letter
"d" plaatsen rechts van de dubbele punt ("d" staat hierbij voor
"decimaal"). Wil je dat het getal wordt geïnterpreteerd als een float,
dan moet je een "f" plaatsen rechts van de dubbele-punt. `format()`
maakt de juiste conversie voor je als dat kan. Je kunt echter niet van
een float een integer maken, want dat veroorzaakt een runtime error.

```python
print( "{} gedeeld door {} is {}".format( 1, 2, 1/2 ) )
print( "{:d} gedeeld door {:d} is {:f}".format( 1, 2, 1/2 ) )
print( "{:f} gedeeld door {:f} is {:f}".format( 1, 2, 1/2 ) )
```

Net als bij strings, kun je voor getallen precisie en aanlijning
gebruiken. Dit doe je op dezelfde manier. En net als bij strings geldt
dat als de precisie niet voldoende groot is, de functie gewoon de ruimte
neemt die nodig is. Let erop dat een eventueel min-teken en een
eventuele punt in een float ook plaats nodig hebben.

```python
print( "{:5d} gedeeld door {:5d} is {:5f}".format( 1, 2, 1/2 ) )
print( "{:<5f} gedeeld door {:^5f} is {:>5f}".format( 1,2,1/2 ))
```

Tenslotte, en misschien het meest nuttig, kun je aangeven met hoeveel
decimalen een float getoond moet worden, door een punt en een getal te
plaatsen links van de letter "f." De `format()` methode zal het getal
afronden tot het juiste aantal decimalen. Merk op dat je ook mag
aangeven dat je nul decimalen wilt zien door `.0` te gebruiken, wat
ervoor zal zorgen dat een float wordt getoond als een integer.

```python
print( "{:.2f} gedeeld door {:.2f} is {:.2f}".format( 1,2,1/2 ))
```

De volgende toepassing van
`format()` realiseert het afronden op drie decimalen:

```python
print( "{:.3f}".format( 7/11 ) )
```


De combinatie van precisie, aanlijning, en decimalen staat je toe om
redelijk uitziende tabellen te tonen.

```python
s = "{:>5d} keer {:>5.2f} is {:>5.2f}"
print( s.format( 1, 3.75, 1 * 3.75 ) )
print( s.format( 2, 3.75, 2 * 3.75 ) )
print( s.format( 3, 3.75, 3 * 3.75 ) )
print( s.format( 4, 3.75, 4 * 3.75 ) )
print( s.format( 5, 3.75, 5 * 3.75 ) )
```
