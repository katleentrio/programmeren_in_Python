Voor we van start kunnen gaan, moet eerst de functie `print()` worden besproken. We moeten 
immers kunnen zien wat het resultaat van een ingevoerde expressie/bewerking is.
In programma's moet je telkens expliciet aangeven dat je resultaten wilt tonen/afprinten. 

Je gebruikt de `print()` functie als volgt: je schrijft het woord `print`,
gevolgd door ronde haakjes. Tussen de haakjes geef je de inhoud die je wilt laten
zien. In het voorbeeld dat hieronder gegeven wordt, wil je de tekst "Hello world!" laten verschijnen.
Een **tekst** typ je altijd **tussen aanhalingstekens**, je mag naar keuze dubbele of enkele aanhalingstekens gebruiken:

```python
print( "Hello, world!" )
```

Als je deze code laat uitvoeren (doe de test in Spyder), zie je dat de tekst "Hello, world!" wordt getoond.

*Ter info: wanneer in een tekst een functie bij naam wordt genoemd, wordt de naam gevolgd door
een openings- en sluithaakje.* 

Je kunt meerdere dingen tegelijkertijd laten zien met een `print()`
functie. Hiervoor plaats je alles wat je wilt laten zien tussen de haakjes,
gescheiden door komma's. De `print()` functie laat dan al die items zien met spaties ertussen. Bijvoorbeeld:

```python
print( "Ik", "heb", "twee", "appels", "en", "een", "banaan" )
```

In bovenstaand voorbeeld worden spaties na elke komma ingevoerd. Deze zijn overbodig.

```python
print("Ik","heb","twee","appels","en","een","banaan")
```

is precies hetzelfde als het commando ervoor. De spaties worden dus enkel toegepast
om de leesbaarheid van het programma te vergroten. Het is de gewoonte bij programmeurs om bij functies nooit 
een spatie te typen net na het openingshaakje.

Bij getallen hoef je geen dubbele aanhalingstekens te plaatsen. 
In een `print()` functie kan je tekst en getallen door elkaar gebruiken.

```python
print( "Ik", "heb", 2, "appels", "en", 1, "banaan" )
```
Uiteraard hoef je niet elk woord te scheiden door een komma, maar kan je ook een volledige of een deel van een zin tussen aanhalingstekens plaatsen.