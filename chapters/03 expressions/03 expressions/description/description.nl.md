We beschikken nu over voldoende informatie om met "expressies" aan de slag te gaan.
Bij een expressie worden één of meerdere waarden gecombineerd met
behulp van operatoren zodat een nieuwe waarde ontstaat. 
De waarden kunnen zowel strings, integers als floats zijn.
Expressies zijn dus een vorm van berekeningen.

### Eenvoudige berekeningen

Eenvoudige berekeningen worden gemaakt door twee waarden te combineren
met een operator. Een aantal voor de hand liggende **operatoren** zijn:

| operator | beschrijving |
|:--------:|:------------|
| `+` | optelling |
| `-` | aftrekking |
| `*` | vermenigvuldiging |
| `/` | deling |
| `//` | integer deling |
| `**` | machtsverheffing |
| `%` | modulo |
{:class="table table-striped table-condensed" style="width:auto;margin-left:auto;margin-right:auto;"}


De meeste operatoren zijn algemeen gekend en hoeven geen extra uitleg, 
met uitzondering van de integer deling en modulo.

De **integer deling (//)** is een deling waarbij het resultaat naar beneden 
wordt afgerond naar een geheel getal. Als er floats in
de berekening zitten, blijft het resultaat een float, zij het naar
beneden afgerond. Als de berekening alleen integers omvat, is het
resultaat een integer.

De **modulo operator (%)** geeft de rest bij een deling.
Bijvoorbeeld: 14 gedeeld door 5 is 2.8.
De uitkomst als geheel getal is 2 met een rest van 4. 14
modulo 5 geeft bijgevolg als rest 4.

Hieronder volgen een paar voorbeelden. Bedenk eerst zelf wat het resultaat is,
controleer in Spyder.

```python
print( 15+4 )
print( 15-4 )
print( 15*4 )
print( 15/4 )
print( 15//4 )
print( 15**4 )
print( 15%4 )
```

### Complexe berekeningen

Je mag waarden en operatoren combineren om complexere berekening te maken.
Zonder gebruik van haakjes zal Python de volgorde van bewerkingen respecteren
zoals wij die kennen: eerst haakjes dan machten en wortels, vermenigvuldiging en deling, 
optelling en aftrekking. 
Door haakjes te gebruiken kan je zelf een volgorde van bewerking aanbrengen.

Bekijk de berekening hieronder en probeer te bepalen wat de uitkomst is.
Controleer in Spyder.

```python
print( 5*2-3+4/2 )
```

Een paar opmerkingen bij deze berekening:
-   Python zal als uitkomst een float geven ook al komen er geen decimale getallen voor.
    **Van zodra er een deling in de berekening zit, wordt de uitkomst automatisch een float.**
-   Spaties worden door Python genegeerd. De code hierboven is dus equivalent met:

```python
print( 5 * 2 - 3 + 4 / 2 )
```

of:

```python
print( 5*2 - 3+4    / 2 )
```

Het maakt niet uit hoeveel spaties je rondom de operatoren zet: spaties worden genegeerd 
door Pythong en dienen enkel om de leesbaarheid van de code te verhogen. 
Als je dus eerst $$3+4$$ wilt laten berekenen, moet je er haakjes omheen
zetten.

```python
print( (5*2) - (3+4)/2 )
print( ((5*2)-(3+4)) / 2 )
```

### String expressies

De enige van de hierboven genoemde operatoren die ook voor strings
kunnen gebruikt worden zijn plus ($$+$$) en ster ($$*$$).

De **plus ($$+$$)** gebruik je om **twee strings aan elkaar te**
**"plakken"**. De **ster ($$*$$)** gebruik je met een string en een
integer om een string te maken die een **herhaling van de originele string**
bevat. Test uit in Spyder:

```python
print( "tot"+"ziens" )
print( 3*"hallo" )
print( "tot ziens"*3 )
```

Je kunt geen getal optellen bij een string, of twee strings met elkaar
vermenigvuldigen. Zulke operatoren zijn niet gedefinieerd, en geven
foutmeldingen. Geen van de andere operatoren werkt voor strings.

### Type casting

We bespraken de drie meest voorkomende data types.
Soms moet je een data type of waarde veranderen in een ander data type.
Je kunt dat doen met "type casting" functies.

Een functie heeft een naam en kan parameters hebben die opgegeven worden tussen de
haakjes die achter de naam staan. De functie doet iets met die
parameter en geeft soms een resultaat terug. Zo drukt de functie
`print()` de parameterwaarden af op het scherm maar geeft niets terug.

Type casting functies geven wel een waarde terug. De waarde is (bijna) net hetzelfde als de
parameterwaarde, maar van een verschillend datatype. 
De drie belangrijkste type casting functies zijn:

-   `int()` geeft de parameterwaarde terug als integer (indien
    noodzakelijk afgerond naar beneden)

-   `float()` geeft de parameterwaarde terug als float (waarbij .0
    indien noodzakelijk wordt toegevoegd)

-   `str()` geeft de parameterwaarde terug als string

Test de verschillen tussen de volgende twee regels code:

```python
print( 15/4 )
print( int( 15/4 ) )
```

Of de volgende twee regels:

```python
print( 15+4 )
print( float( 15+4 ) )
```

Eerder was aangegeven dat je de plus-operator niet kunt gebruiken om een
getal aan een string vast te plakken. Als je zoiets toch wilt doen, kun
je gebruik maken van string type casting:

```python
print( "Ik heb " + str( 15 ) + " appels." )
```
