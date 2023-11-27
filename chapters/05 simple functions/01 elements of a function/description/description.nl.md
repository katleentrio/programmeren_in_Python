Je kunt een functie beschouwen als een "zwarte doos": je kunt er gegevens
instoppen (parameters) en resultaten uit halen (return value) zonder dat je hoeft te weten
hoe de functie precies werkt of hoe de code in de functie eruit ziet.
Het enige dat je moet kennen zijn de naam, de parameters, en de
return value. 

Deze drie elementen worden hieronder één voor één besproken.

### Functienamen

Iedere functie heeft een naam. Gewoonlijk is dit een korte beschrijving van wat 
de functie doet. Vrijwel alle standaard Python functienamen bestaan uit kleine letters.
*Je kan ook zelf een functie aanmaken. Let bij de naamgeving dan op het volgende:*
*-   Functienamen bestaan alleen uit letters, cijfers en underscores.*
*-   Functienamen mogen niet starten met een cijfer.*
Wij beperken ons hier tot het gebruik van bestaande functies.

In code wordt de functienaam steeds gevolgd door een openings- en sluithaakje, waartussen
de parameters worden opgegeven. Wanneer je nu in een tekst refereert naar een functie, 
is het de gewoonte om ook daar achter de naam van de functie een openings- en sluithaakje te zetten. 

### Parameters

Sommige functies hebben parameters nodig om te kunnen werken.
Die parameters worden opgegeven bij het oproepen van de
betreffende functie. Ze worden **tussen de haakjes** geplaatst
**achter de functienaam**. Als er meerdere parameters vereist zijn, 
worden ze **gescheiden door komma's**.

De parameters zijn waarden die de programmeur aan de functie geeft om
te verwerken. Voorbeelden:
-   de functie `int()` wordt aangeroepen met één parameter: de waarde die door de functie omgezet zal worden naar een integer.
-   de functie `print()` kan worden opgeroepen met een willekeurig aantal parameters (ook nul) die de functie op het scherm zal tonen, waarna de functie naar een nieuwe regel op het scherm springt.

Algemeen genomen kan een functie de waarde van een parameter niet wijzigen.
Bekijk de volgende code:

```python
x = 1.56
print( int( x ) )
print( x )
```

Het eerste printcommando toont 1 op het scherm, het tweede 1.56.
Door `int()` tussen de haakjes van de `print()` functie te 
plaatsen, wordt de waarde van de variabele `x` dus niet gewijzigd naar
een integer. Dit betekent dat de functie geen toegang heeft tot de 
variabelen die als parameters gebruikt worden, maar dat de functie 
kopieën krijgt van de waarden die in de parameters staan.

Indien een functie meerdere parameters nodig heeft, is de volgorde waarin
deze gegeven worden belangrijk.
Voorbeeld de standaard functie `pow()`: deze voert een machtsverheffing uit 
en vereist twee parameters; het grondtal is de eerste, de exponent de tweede.

```python
grondtal = 2
exponent = 3
print( pow( grondtal, exponent ) )
```

De volgende code geeft een ander antwoord dan de vorige. De functie houdt
enkel met de volgorde.

```python
grondtal = 2
exponent = 3
print( pow( exponent, grondtal ) ) # verwarrende keuze variabele namen 
```

Wanneer je een functie aanroept met parameterwaarden waarmee de functie
niet kan werken, leidt dit meestal tot "runtime errors" (fouten tijdens
de uitvoering van code). Zo leiden beide regels in de volgende code tot
runtime errors.

```python
x = pow( 3, "2" ) # `pow()` aanroepen met strings
y = int( "twee-en-een-half" ) # `int()`aanroepen met een string die geen integer bevat
```

### Return value

Een functie heeft vaak een return value; het **resultaat na uitvoering van de functie**.
Als een functie een waarde teruggeeft, kun je die verder in je code gebruiken
door deze in een variabele te stoppen door een assignement. Je kan de return value ook 
onmiddelijk printen. Onderstaande code bevat een voorbeeld van beide mogelijkheden.

```python
x = 2.1
y = '3'
z = int( x )
print( z )
print( int( y ) )
```

In de laatste regel van bovenstaande code wordt de `int()` functie als parameter van 
de `print()` functie ingevoerd. In dit geval wordt de aanroep van `int()` eerst
uitgevoerd, daarna `print()`. De return value van `int()` is de uiteindelijke
parameter voor `print()`.

Niet alle functies geven een return value. Zo geeft `print()` geen waarde terug.
Dit kan tot vreemd gedrag van je code leiden. Bekijk volgende code en
bedenkt wat er uiteindelijk op het scherm getoond zal worden:

```python
print( print( "Hello, world!" ) )
```

Deze code drukt twee regels af. De eerste regel bevat de tekst
"Hello, world!", de tweede het woord **"None"**. Voor de laatste `print()`
functie is dus **geen parameter ingevoerd**.
We bekijken even in detail hoe Python deze regel code verwerkt.

Wanneer Python de code uitvoert, zal eerst de tweede `print()` functie worden
uitgevoerd; "Hello, world!" verschijnt op het scherm en de cursor verspringt 
naar de volgende regel. De tweede `print()` functie is eveneens het argument van de eerste 
`print()` functie. Vermits `print()` geen return value heeft, is er niets dat 
afgedrukt kan worden door de eerste `print()` functie; `None` verschijnt op het scherm.

`None` is een speciale waarde die aangeeft dat er helemaal "geen waarde" is.
`None` is geen string, geen float, geen integer; het is niets.
Dus wees voorzichting met het aanroepen van een functie als parameter;
als de functie geen return value heeft, kunnen er vreemde dingen
gebeuren.
