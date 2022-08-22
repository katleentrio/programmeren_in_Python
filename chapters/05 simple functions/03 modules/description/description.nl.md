Naast die basisfuncties waarvan we er een aantal besproken hebben in het
voorgaande deeltje, biedt Python ook een groot
aantal zogeheten "modules" aan waarin zich vele nuttige functies bevinden.
Een module is eigenlijk een verzameling van een aantal functies.
Je kunt de functies van een module gebruiken in jouw programma door eerst de module
te importeren. Dit doe je door boven in je programma `import <modulenaam>`
op te nemen. Je kunt dan alle functies die de module bevat
gebruiken door de functienaam vooraf te laten gaan door de naam van de module en een
punt. Om bijvoorbeeld de functie `sqrt()` (vierkantswortel) uit de `math` module te
gebruiken, roep je `math.sqrt()` aan nadat je eerder `math` geïmporteerd hebt.

Als alternatief kun je ook specifieke functies vanuit een module
importeren zonder de volledige module te importeren:  

```python
from <module> import <functie1>, <functie2>, <functie3>, …
```
  
Bij deze alternatieve manier om functies te importeren, moet je
de naam van de module niet meer plaatsen voor de functie-aanroep.
Zo is:

```python
import math

print( math.sqrt( 4 ) )
```

equivalent aan:

```python
from math import sqrt

print( sqrt( 4 ) )
```

Als je een functie onder een andere naam in je programma wilt gebruiken,
kun je dat doen door gebruik te maken van het gereserveerde woord `as`. Dit kan zinvol
zijn als je meerdere modules gebruikt waarin toevallig functies
voorkomen die dezelfde naam hebben.

```python
from math import sqrt as squareroot

print( squareroot( 4 ) )
```

Je kunt zelf een module coderen, maar dit zou ons te ver leiden.
Voor de meeste min-of-meer-algemene problemen die je wilt oplossen,
is er reeds een module ontwikkeld die je kunt gebruiken. We bespreken
nu een aantal functies uit twee veelgebruikte standaard modules.

### `math`

De `math` module bevat een aantal nuttige wiskundige functies. Deze
functies zijn zeer efficiënt en geven meestal een float als return value.
Ik bespreek hier de belangrijkste (de anderen kan je steeds opzoeken in de Python
referentie):

-   `sqrt()` krijgt één numerieke parameter en geeft als return value de
    vierkantswortel van die parameter.

-   *`exp()` krijgt één numerieke parameter en geeft als return value $$e$$ tot de macht van die parameter. (leerstof wiskunde 3de graad)*

-   *`log()` krijgt één numerieke parameter en geeft als return value het natuurlijk logaritme van die parameter. Het natuurlijk logaritme is de waarde die de parameter als uitkomst heeft als je $$e$$ verheft tot deze waarde. (leerstof wiskunde 3de graad)*

-   *`log10()` krijgt één numerieke parameter en geeft als return value het logaritme met 10 als basis van de parameter. (leerstof wiskunde 3de graad)*


Bijvoorbeeld:

```python
from math import sqrt

getal = float( input("Geef een getal."))
print( "De vierkantswortel van", getal, "is gelijk aan", sqrt(getal) )
```

### `random`

De `random` module bevat functies die "toevalsgetallen" genereren.

-   `random()` krijgt geen parameter en geeft als return value een toevalsgetal;
    een float binnen het interval $$[0,1[$$.

-   `randint()` krijgt twee parameters: twee integers waarbij de
    eerste kleiner dan of gelijk moet zijn aan de tweede. Het
    geeft als return value een toevalsgetal dat een integer is dat ligt binnen het
    gesloten interval met als grenzen deze twee parameters. Zo geeft `randint(2,5)`
    2, 3, 4, of 5 als return value; elk met een gelijke kans.

-   `seed()` initialiseert de toevalsgetal-generator van Python. Als je
    een lijst van toevalsgetallen wilt hebben die iedere keer hetzelfde
    is voor je programma, kun je dat voor elkaar krijgen door aan het
    begin van je programma `seed()` aan te roepen met een vast getal,
    bijvoorbeeld 0. Dit kan nuttig zijn bij het testen van je programma.
    Als je de generator weer echt toevallige getallen wilt laten
    genereren op een later punt in je programma, kun je `seed()`
    nogmaals aanroepen zonder parameter.

Voorbeeld:

```python
from random import random, randint, seed

seed()
print( "Een toevalsgetal tussen 1 en 10 is", randint( 1, 10 ) )
print( "Een ander is", randint( 1, 10 ) )
seed( 0 )
print( "3 toevalsgetallen zijn:", random(), random(), random() )
seed( 0 )
print( "Dezelfde 3 zijn:", random(), random(), random() )
"""Elke regel die voorafgegaan wordt door seed( 0 ) gebruikt dezelfde reeks getallen. Door het getal te veranderen tussen de haakjes, genereer je een nieuwe reeks getallen die je opnieuw kan oproepen. """ 
seed( 1 )
print( "3 nieuwe toevalsgetallen zijn:", random(), random(), random() )
seed( 1 )
print( "Dezelfde 3 nieuwe getallen zijn:", random(), random(), random() )
```
