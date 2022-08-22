Achter een functie zit code die een bepaalde actie uitvoert. Je kan de functie
meermaals oproepen (Engels: "call") met opgave van eventuele parameters
die de functie nodig heeft om uitgevoerd te kunnen worden. Je hoeft dus niet te
weten hoe de functie precies werkt. De volgende drie dingen moet je wel weten
om de functie te kunnen oproepen:

-   De naam van de functie

-   De parameters die de functie nodig heeft (indien nodig)

-   De return value: de waarde die de functie teruggeeft (indien van toepassing)

Deze drie elementen worden hieronder één voor één besproken.

### Functienamen

Iedere functie heeft een naam. Net als variabele namen mogen functienamen
alleen bestaan uit letters, cijfers en underscores. Ze mogen
niet starten met een cijfer. Gewoonlijk is de naam van een functie
een korte beschrijving van wat de functie doet. Vrijwel alle standaard
Python functienamen bestaan uit kleine letters. 

Wanneer je in een tekst refereert naar een functie, is het de gewoonte om
achter de naam van de functie een openings- en sluithaakje te zetten. Functies
hebben in code immers altijd die haakjes (ook als er niet tussen de haakjes staat).

### Parameters

Sommige functies hebben parameters ("argumenten") nodig om te kunnen werken.
Die parameters worden opgegeven bij het oproepen van de
betreffende functie. Ze worden tussen de haakjes geplaatst
achter de functienaam. Als er meerdere parameters vereist zijn, 
worden ze gescheiden door komma's.

De parameters zijn waarden die de programmeur aan de functie geeft om
te verwerken. Zo wordt de functie `int()` bijvoorbeeld aangeroepen met één
parameter: de waarde die door de functie omgezet zal worden naar een integer.
De `print()` functie kan worden opgeroepen met een willekeurig aantal parameters
(ook nul) die de functie op het scherm zal tonen, waarna de functie naar een 
nieuwe regel op het scherm springt.

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
een integer en als dusdanig toegepast in de verdere code; de functie
`int()` heeft alleen aan `print()` doorgegeven wat de integer
representatie van de waarde van `x` is. Dit betekent dat de functie
geen toegang heeft tot de variabelen die als parameters gebruikt worden,
maar dat de functie kopieën krijgt van de waarden die in de parameters
staan. Een aantal data types vormen een uitzondering hierop, maar deze
worden voorlopig niet besproken.

Indien een functie meerdere parameters nodig heeft, is de volgorde waarin
deze gegeven worden belangrijk.
Voorbeeld: de standaard functie `pow()` vereist twee parameters en
rekent de waarde uit van de eerste die wordt verheven tot de macht
weergegeven door de tweede.

```python
grondtal = 2
exponent = 3
print( pow( grondtal, exponent ) )
```

De volgende code geeft een ander antwoord dan de vorige. De functie houdt
geen rekening met de naamgeving, enkel met de volgorde.

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

Een functie heeft vaak een return value; het resultaat na uitvoering van de functie.
Als een functie een waarde teruggeeft, kun je die verder in je code gebruiken.
Zo geeft de `int()` functie een integer representatie van de parameter die is
meegegeven. Je kunt deze return value bijvoorbeeld in een variabele stoppen
door een assignment, of je kunt de waarde ook onmiddellijk printen.

```python
x = 2.1
y = '3'
z = int( x )
print( z )
print( int( y ) )
```

In de laatste regel van bovenstaande code krijgt de `print()` functie als parameter
een aanroep van de `int()` functie. In dit geval wordt de aanroep van `int()` eerst
uitgevoerd, daarna `print()`. De return value van `int()` is de uiteindelijke
parameter voor `print()`.

Niet alle functies geven een return value. Zo geeft `print()` geen waarde terug.
Dit kan leiden tot vreemd gedrag van je code leiden. Bekijk volgende code en
bedenkt wat er uiteindelijk op het scherm getoond zal worden:

```python
print( print( "Hello, world!" ) )
```

Deze code drukt twee regels af. De eerste regel bevat de tekst
"Hello, world!", de tweede het woord "None." Voor de laatste `print()`
functie is dus geen geldige parameter ingevoerd.
We bekijken even in detail hoe Python deze regel code verwerkt.

Wanneer Python de code bekijkt, ziet het de eerste functie 
`print( <something> )`. Omdat `<something>` een argument is, moet dit
geëvalueerd worden. `<something>` is in dit geval 
`print( <something_else> )`. Vermits `<something_else>` opnieuw
een argument is, moet Python ook dit eerst evalueren.
`<something_else>` is de string `"Hello, world!`". Dit is een geldige
parameter voor de functie `print()` en kan dus uitgevoerd worden. 
Python slaat de return value van deze uitvoering op omdat die nodig is
voor de evaluatie van `<something>`. Nu komt het probleem: `print()`
heeft geen return value, dus er is niets wat Python kan gebruiken voor
`<something>`. Voor deze situaties heeft Python een speciale waarde: `None`.
Dus het eerste `print()` commando krijgt als argument `None` mee, 
wat leidt tot het afdrukken van "None" op het scherm.

`None` is een speciale waarde die aangeeft dat er helemaal "geen waarde" is.
Wanneer je de waarde `None` afdrukt, verschijnt het woord "None". Dit is
echter niet een string met de waarde `"None"`. Het woord geeft slechts aan dat
er niets af te drukken is. `None` is ook niet hetzelfde als een lege string
(`""`). Een lege string heeft nog steeds een waarde, namelijk een string
met lengte nul. `None` is geen string, geen float, geen integer; het is niets.
Dus wees voorzichting met het aanroepen van een functie als parameter;
als de functie geen return value heeft, kunnen er vreemde dingen
gebeuren.

### Een functie als zwarte doos

Je kunt een functie beschouwen als een "zwarte doos": je kunt er gegevens
instoppen en resultaten uit halen zonder dat je hoeft te weten
hoe de functie precies werkt of hoe de code in de functie eruit ziet.
Het enige dat je hoeft te kennen zijn de naam, de parameters, en de
return value. Mogelijk maakt de functie intern variabelen aan en voert
berekeningen uit, maar die hebben geen effect op de rest van de code … 
tenminste, als je de functie correct implementeert. 

Functies die geen effect hebben op de rest van de code heten 
"pure functions". Er bestaan ook functies die wel een effect hebben
op de rest van de code, dit zijn "modifiers". Wij beperken ons hier tot 
"pure functions".
