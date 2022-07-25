Vooraleer ik expressies ga bespreken, moet ik eerst de functie
uitleggen die het mogelijk maakt om het resultaat van een expressie te laten zien.
In programma's moet je immers telkens expliciet aangeven dat je resultaten wilt tonen, 
zelfs als het gaat om een commando dat op de laatste regel van het programma staat.
De functie die dat doet is `print`. 

Je gebruikt de `print` functie als volgt: je schrijft het woord `print`,
gevolgd door ronde haakjes. Tussen de haakjes geef je de inhoud die je wilt laten
zien. In het voorbeeld dat hieronder gegeven wordt, wil je de tekst "Hello world!" laten verschijnen.
Een tekst typ je altijd tussen aanhalingstekens, je mag naar keuze dubbele of enkele aanhalingstekens gebruiken:

```python
print( "Hello, world!" )
```

Als je deze code laat uitvoeren, zie je dat de tekst "Hello, world!" wordt getoond.

Ter info: wanneer auteurs van teksten i.v.m. programmeren een functie bij naam noemen, 
plaatsen ze er een openings- en sluithaakje achter om aan te geven dat het een functienaam
betreft. Ik doe dit ook in het verdere verloop van de cursus. Bovendien gebruiken auteurs soms
niet het woord "functie," maar "statement" of "commando." Deze
termen duiden echter meestal op alles wat Python kan uitvoeren en beperkt zich niet
alleen tot functies. Bijvoorbeeld, een expressie is ook een "commando."

Je kunt meerdere dingen tegelijkertijd laten zien met een `print()`
functie. Hiervoor plaats je alles wat je wilt laten zien tussen de haakjes,
gescheiden door komma's. De `print()` functie laat dan al die items zien met spaties ertussen. Bijvoorbeeld:

```python
print( "Ik", "heb", "twee", "appels", "en", "een", "banaan" )
```

De spaties na elke komma in dit commando zijn overbodig.

```python
print("Ik","heb","twee","appels","en","een","banaan")
```

is precies hetzelfde als het commando ervoor. Je mag de spaties
toevoegen om de leesbaarheid van het programma te vergroten. Je mag ook spaties zetten
tussen het woord `print` en het openingshaakje, maar dit is niet gebruikelijk. De gewoonte is om
bij functies altijd het openingshaakje aan de naam van de functie "vast
te plakken."

Merk op dat je met `print()` niet alleen teksten, maar ook getallen kunt
laten zien. Getallen hoef je niet tussen dubbele aanhalingstekens te plaatsen. 
Je mag teksten en getallen door elkaar gebruiken.

```python
print( "Ik", "heb", 2, "appels", "en", 1, "banaan" )
```
