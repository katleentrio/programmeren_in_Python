Nu komen we eindelijk tot de essentie van dit hoofdstuk: "expressies". Bij een expressie worden 
één of meerdere waarden gecombineerd met
behulp van operatoren zodat een nieuwe waarde ontstaat. 
De waarden kunnen zowel strings, integers als floats zijn.
Expressies zijn dus een vorm van berekeningen.

### Eenvoudige berekeningen

Eenvoudige berekeningen worden gemaakt door twee waarden te combineren
met een operator. Een aantal voor de hand liggende operatoren
zijn:

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

De meeste operatoren zijn gekend, behalve
misschien de integer deling en modulo.

De integer deling (//) (ook wel genoemd "floor division") is een
deling waarbij het resultaat naar beneden wordt afgerond naar een geheel getal. Als er floats in
de berekening zitten, blijft het resultaat een float, zij het naar
beneden afgerond. Als de berekening alleen integers omvat, is het
resultaat een integer.

De modulo operator (%) geeft de rest bij een deling.
Bijvoorbeeld: als ik 14 deel door 5, is de uitkomst 2.8.
De uitkomst als geheel getal is 2 met een rest van 4. 14
modulo 5 geeft bijgevolg als rest 4.

Hier volgen een paar voorbeelden:

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
Zonder gebruik van haakjes zal Python de volgorde van bewerkingen respecteren:
haakjes, exponenten, vermenigvuldiging en deling, optelling en aftrekking. 
Worteltrekken is een vorm van machtsverheffen.
Door haakjes te gebruiken kan je zelf een volgorde van bewerking aanbrengen.

Bekijk de berekening hieronder en probeer te bepalen wat de uitkomst is.

```python
print( 5*2-3+4/2 )
```

Het resultaat is 9
Een paar opmerkingen bij deze berekening:
-   Python zal als uitkomst een float geven ook al komen er geen decimale getallen voor.
    Van zodra er een deling in de berekening zit, wordt de uitkomst automatisch een float.
-   Spaties worden door Python genegeerd. De code hierboven is dus equivalent met:

```python
print( 5 * 2 - 3 + 4 / 2 )
```

of:

```python
print( 5*2 - 3+4    / 2 )
```

Het maakt niet uit hoeveel spaties je rondom de operatoren zet: spaties worden genegeerd.
Als je eerst $$3+4$$ wilt laten berekenen, moet je er haakjes omheen
zetten. Spaties kunnen leesbaarheid verhogen als je ze goed toepast,
maar voor Python zijn ze betekenisloos.

```python
print( (5*2) - (3+4)/2 )
print( ((5*2)-(3+4)) / 2 )
```

### String expressies

Een aantal van de hierboven genoemde operatoren kunnen ook voor strings
worden gebruikt, maar niet allemaal.

De enige operatoren die je kunt gebruiken zijn plus ($$+$$) en ster ($$*$$). 
Je kunt de plus ($$+$$) gebruiken om twee strings aan elkaar te
"plakken," en je kunt de ster ($$*$$) gebruiken met een string en een
integer om een string te maken die een herhaling van de originele string
bevat. Zie hier:

```python
print( "tot"+"ziens" )
print( 3*"hallo" )
print( "tot ziens"*3 )
```

Je kunt geen getal optellen bij een string, of twee strings met elkaar
vermenigvuldigen. Zulke operatoren zijn niet gedefinieerd, en geven
foutmeldingen. Geen van de andere operatoren werkt voor strings.

### Type casting

Soms moet je een data type of waarde veranderen in een ander data type.
Je kunt dat doen met "type casting" functies.

In latere hoofdstukken
(<a href="#ch:simplefunctions" data-reference-type="ref" data-reference="ch:simplefunctions">6</a>
en
<a href="#ch:functions" data-reference-type="ref" data-reference="ch:functions">9</a>)
ga ik in detail op functies in, maar voor nu is het voldoende als je
weet dat een functie een naam heeft en parameters kan hebben tussen de
haakjes die achter de naam staan. De functie doet iets met die
parameters en geeft een resultaat terug. Bijvoorbeeld, de functie
`print()` drukt de parameter-waarden af op het scherm, en geeft niks
terug.

Type casting functies nemen de parameter-waarde die tussen de haakjes is
gegeven, en geven een waarde terug die (bijna) hetzelfde is als de
parameter waarde, maar van een verschillend datatype. De drie belangrijkste
type casting functies zijn:

-   `int()` geeft de parameter waarde terug als integer (indien
    noodzakelijk afgerond naar beneden)

-   `float()` geeft de parameter waarde terug als float (waarbij .0
    indien noodzakelijk wordt toegevoegd)

-   `str()` geeft de parameter waarde terug als string

Bekijk de verschillen tussen de volgende twee regels code:

```python
print( 15/4 )
print( int( 15/4 ) )
```

Of de volgende twee regels:

```python
print( 15+4 )
print( float( 15+4 ) )
```

Ik had al aangegeven dat je de plus-operator niet kunt gebruiken om een
getal aan een string vast te plakken. Als je zoiets toch wilt doen, kun
je een oplossing maken met behulp van string type casting:

```python
print( "Ik heb " + str( 15 ) + " appels." )
```
