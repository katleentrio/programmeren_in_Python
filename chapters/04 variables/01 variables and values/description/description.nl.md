**Een variabele is een plaats in het geheugen van de computer die een naam heeft gekregen en waarin je een waarde kunt opslaan.**

Om een variabele te creëren in Python moet je een naam voor de variabele kiezen
waaraan je een waarde "toekent" ("assignment") door gebruik te maken van het
**is-gelijk-teken (`=`)** ("assignment operator").
Aan de linkerkant van het is-gelijk-teken zet je de variabele naam;
aan de rechterkant de waarde die je wilt opslaan in de variabele.
Voorbeeld:

```python
x = 5
print( x )
```

In deze code gebeuren twee dingen. 
Ten eerste wordt er een variabele gecreëerd met de naam `x` 
waaraan de waarde 5 wordt toegekend.  Ten tweede wordt
de inhoud van de variabele `x` op het scherm getoond door middel van de `print()` functie.
Merk op dat `print( x )` niet de letter `x` toont, maar de waarde die in
de variabele `x` is opgeslagen.

![variabele](media/Box.png "variabele"){:data-caption="Een variabele kan je voorstellen als een doos waarop je met een dikke viltstift een naam hebt geschreven, zodat je hem later gemakkelijk kunt terugvinden. Je kunt iets in de doos stoppen, en je kunt in de doos kijken om te zien wat er in zit (er kan wel slechts één ding tegelijkertijd in de doos zitten). Je kunt aan de inhoud van de
doos refereren door de naam te gebruiken die je op de doos hebt geschreven." width="35%"}

Je kunt je de variabele `x` voorstellen als een doos waarop je een `x` hebt geschreven
zodat je hem later gemakkelijk terug kunt vinden. Je kunt iets in de doos stoppen
(slechts één ding tegelijkertijd) en je kunt de inhoud ervan bekijken.
Je kunt naar de inhoud van de doos refereren door de naam te gebruiken 
die je op de doos noteerde. De term "**variabele**" duidt op de variabele **naam**, dus de
letter `x` op de doos. De term "**waarde**" duidt op de waarde die is
opgeslagen in de variabele, dus de **inhoud** van de doos.

Aan de rechterkant van het is-gelijk-teken kun je alles plaatsen wat een
waarde oplevert. Dit hoeft dus niet een getal te zijn, maar mag ook een
berekening zijn, een string of een aanroep van een functie die een
waarde oplevert (bijvoorbeeld de `int()` functie).

Wanneer je de eerste keer in je programma een waarde toekent aan een
specifieke variabele naam, wordt de variabele gecreëerd.
Als je later een andere waarde aan dezelfde variabele toekent, wordt de
eerste waarde "overschreven." In de metafoor van de doos: je maakt de
doos leeg en stopt er iets nieuws in. Een variabele bevat altijd de
laatst verkregen waarde. 
Bekijk onderstaande voorbeelden, bedenk telkens wat er gebeurt en controleer in Spyder.

```python
x = 5
print( x )
x = 7 * 9 + 13   # overschrijft de vorige waarde van x
print( x )
x = "En nu iets heel anders..."
print( x )
x = int( 15 / 4 ) - 27
print( x )
```

Eens een variabele is aangemaakt (en dus een waarde heeft) kun je hem
overal in je code oproepen door de variabele naam te geven. Je kunt
de variabele bijvoorbeeld gebruiken in een berekening.

```python
x = 2
y = 3
print( "x =", x )
print( "y =", y )
print( "x * y =", x * y )
print( "x + y =", x + y )
```

Je kunt de inhoud van een variabele kopiëren in een andere variabele,
via de assignment operator. Doe de volgende test in Spyder.

```python
x = 2
y = 3
print( "x =", x, "en y =", y )

# Verwissel de waardes van x en y via z
z = x
x = y
y = z
print( "x =", x, "en y =", y )
```

Je kunt de variabele ook zelf gebruiken aan de rechterkant van het is-gelijk-teken.

```python
x = 2
print( x )
x = x + 3
print( x )
```

Het is uiteraard evident dat een variabele gecreëerd moet zijn voordat je hem kunt
gebruiken. De volgende code geeft een foutmelding omdat `dagen_per_jaar` nog
niet gecreëerd was voordat hij gebruikt wordt in de eerste regel:

```python
print( dagen_per_jaar )
dagen_per_jaar = 365
```

**Maak er een gewoonte van om alle variabelen binnen een programma te "initialiseren"/"declareren" aan het begin van de code.**