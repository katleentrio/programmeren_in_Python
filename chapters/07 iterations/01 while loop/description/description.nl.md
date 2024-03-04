Stel dat je de gebruiker vraagt naar vijf getallen, deze optelt
en het totaal weergeeft. Met wat je tot nu toe gezien hebt, 
zou dat code er als volgt kunnen uitzien:

```python
getal1 = int(input( "Getal 1: " ))
getal2 = int(input( "Getal 2: " ))
getal3 = int(input( "Getal 3: " ))
getal4 = int(input( "Getal 4: " ))
getal5 = int(input( "Getal 5: " ))

print( "Totaal is", getal1 + getal2 + getal3 + getal4 + getal5 )
```

Dit lukt nog omdat het aantal gevraagde getallen beperkt is. Maar 
wat als je 100 getallen moet opvragen? Dan zou je bovenstaande regel 100 keer moeten herhalen???
Dit kan eenvoudiger door een loop te gebruiken.

De eerste loop die hier besproken wordt is de **`while` loop**. 
Een `while` statement bestaat uit een test gevolgd door één of meerdere acties, 
waarbij de acties alleen worden uitgevoerd **zolang** de test `True` oplevert.
De syntax van een `while` statement ziet er als volgt uit:

```python
while <boolean expressie>:
    <acties>
```

Net als bij een `if` statement, test een `while` statement een boolean
expressie. Wanneer de expressie `True` oplevert, wordt het blok code
onder de `while` uitgevoerd. In tegenstelling tot een `if` statement 
gaat Python meteen na het uitvoeren van het blok code terug naar
de boolean expressie naast de `while` en test die opnieuw. Wanneer de
expressie nog steeds `True` oplevert, wordt het blok code een tweede maal
uitgevoerd. Na uitvoering keert Python nogmaals terug naar de
boolean expressie, en dit telkens opnieuw tot de boolean
expressie `False` oplevert. Pas dan slaat Python het blok code
onder de `while` over en gaat verder met het vervolg van de code.

Merk op dat als de boolean expressie meteen `False` oplevert het blok code onder de `while`
onmiddellijk wordt overgeslagen, net zoals gebeurt bij een `if` statement.

Dit alles wordt duidelijker met onderstaande voorbeelden.

### `while` loop, een eerste voorbeeld

Voorbeeld: print de nummers 1 tot en met 5\. 
Met een `while` loop kan de code er als volgt uit zien:

```python
num = 1
while num <= 5:
    print( num )
    num += 1
print( "Klaar" )
```

Het stroomdiagram bij deze code ziet er als volgt uit
<a href="#f:chart4" data-reference-type="ref" data-reference="f:chart4">8.1</a>.

![while](media/Chart4en.png "while"){:width="30%" data-caption="Stroomdiagram dat een `while` loop weergeeft."}

Het is van essentieel belang dat je deze code begrijpt. We overlopen elke stap.

De eerste regel initialiseert een variabele `num`en krijgt de waarde 1. Dit 
is de eerste waarde die afgedrukt moet worden.

De `while` loop start en voert de boolean expressie `num <= 5` uit. `num` heeft waarde 1
wat kleiner is dan 5 dus de expressie levert `True`. Het blok code onder de `while` wordt 
uitgevoerd (code met insprong).

De eerste regel van het blok code print de waarde van `num`, dus 1. 
De tweede regel telt 1 op bij de waarde van `num` die nu de waarde 2 krijgt.
Python gaat vervolgens terug naar de boolean expressie. *De laatste print() regel wordt dus nog niet uitgevoerd omdat de loop nog niet afgelopen is.*

Omdat `num` de waarde 2 heeft (nog steeds kleiner dan 5) evalueert de boolean expressie nog steeds als `True`.
Het blok code wordt dus nogmaals uitgevoerd: 2 wordt afgedrukt, `num`
krijgt waarde 3, en de code keert terug bij de boolean expressie.

Dit wordt telkens opnieuw herhaald tot `num` de waarde 6 heeft. 
Nu evalueert de boolean expressie als `False` (6 is immers niet kleiner dan of 
gelijk aan 5). Het blok code (met insprong) wordt
overgeslagen en Python gaat verder met het vervolg van het programma.
In dit voorbeeld is dat de laatste regel code die het woord "Klaar" 
afdrukt, en het programma eindigt.

Wijzig de code hierboven zodat de getallen 1, 3, 5, 7, en 9 afgedrukt
worden. Test uit in Spyder.

### `while` loop, een tweede voorbeeld

Vraag de gebruiker naar vijf getallen en bereken de som. 
De code kan er als volgt uitzien:

```python
totaal = 0
teller = 0
while teller < 5:
    totaal += int(input( "Geef een getal: " ))
    teller += 1

print( "Totaal is", totaal )
```

Bestudeer bovenstaande code. Er worden twee variabelen gebruikt.
`totaal` wordt gebruikt om de som te kunnen berekenen. Deze variabele
start met waarde nul omdat er bij het begin van het programma nog geen getallen
ingegeven zijn en de som dus nul is. Telkens wanneer de loop wordt doorlopen, 
verhoogt de waarde van `totaal` met het ingevoerde getal.
De variabele `teller` wordt gebruikt om na te gaan hoe vaak de loop doorlopen is. 
Bij het begin van het programma is de loop nog niet 
doorlopen dus start `teller` met waarde nul. De loop moet in totaal vijf keer uitgevoerd
worden. De boolean expressie test dus of `teller` kleiner is dan 5. Iedere keer dat 
de loop doorlopen wordt, moet de waarde van `teller` met 1 verhoogd worden zodat na vijf keer doorlopen
de boolean expressie `False` is en overgegaan kan worden naar de rest van de code.

Misschien lijkt het je logischer om `teller` te laten starten bij 1 en `teller <= 5` 
te testen. Dit is echter niet gebruikelijk. Wij gaan dat dan ook niet doen en volgen 
de gebruikspraktijk van programmeurs.

Opmerking: De variabele `teller` is wat programmeurs een "wegwerp
variabele" noemen. Het enige doel van deze variabele is te tellen hoe
vaak de loop doorlopen is. Programmeurs kiezen vaak één-letter namen 
voor dit soort variabelen, meestal `i` of `j`. In het voorbeeld werd voor de
duidelijkheid de naam `teller` gekozen, maar `i` was beter geweest.

Wijzig de code hierboven zodat niet alleen het totaal maar ook het
gemiddelde wordt afgedrukt. Test uit in Spyder.

In het begin van dit hoofdstukje werd een voorbeeldcode gegeven waarbij de gebruiker 
gevraagd werd vijf getallen in te geven. De prompt "Getal `x`: " werd gebruikt, 
waarbij `x` een cijfer voorstel. Kun je de code vanuit "`while` loop, een tweede voorbeeld"
aanpassen zodat de prompt er hetzelfde uitziet als in het beginvoorbeeld? Behoud de loop structuur.

### De `while` loop onder controle van de gebruiker

In voorgaande voorbeeld werd de gebruiker beperkt tot de invoer van vijf getallen. 
Het gebeurt echter regelmatig dat het aantal op te vragen data variabel is
en de gebruiker zoveel getallen kan ingeven als hij wil, inclusief helemaal geen getallen. 
Dat betekent dat je vooraf niet weet hoe vaak de loop doorlopen moet worden maar dat de 
gebruiker dit bepaalt. Er moet dus een mogelijkheid ingebouwd worden waarbij de gebruiker 
aangeeft dat hij klaar is met de invoer.

De code hieronder laat zien hoe je een `while` loop kunt opzetten die de
gebruiker zoveel getallen laat ingeven als gewenst. De gebruiker stopt
met het ingeven van getallen door -in dit geval- een nul in te geven. Het totaal wordt
afgedrukt wanneer de loop beëindigd is.

```python
num = -1                                        # beginwaarde voor num is -1, verschillend van 0
totaal = 0                                      # deze variabele geeft de som, startend bij beginwaarde 0
while num != 0:
    num = int(input( "Geef een getal: " ))      # num krijgt telkens de waarde van het ingevoerde getal
    totaal += num
print( "Totaal is", totaal )
```

Deze code functioneert maar is niet gebruikelijk. Er zitten minimaal twee
schoonheidsfouten in. Ten eerste wordt `num` geïnitialiseerd op -1. Deze
waarde heeft in principe geen betekenis maar moet wel verschillend van 0 
zijn zodat de loop minstens één keer uitgevoerd wordt. Ten tweede stopt 
de loop niet meteen als de gebruiker nul ingeeft. De ingave van de gebruiker
wordt eerst opgeteld bij `totaal`. In dit geval wijzigt de waarde van `totaal` niet.
Maar indien vooraf gesteld wordt dat de gebruiker de loop kan eindigen door 
bijvoorbeeld een negatief getal in te geven, dan klopt het eindtotaal niet meer.

Een mogelijke oplossing ziet er als volgt uit:

```python
num = int(input( "Geef een getal: " ))
totaal = 0
while num != 0:
    totaal += num
    num = int(input( "Geef een nummer: " ))
print( "Totaal is", totaal )
```

Dit lost bovenstaande schoonheidsfouten op, maar introduceert er wel
een nieuwe, namelijk de herhaling van de `input()` functie. 
Hoe je dat kunt oplossen volgt later.

Maak een loop die de gebruiker een aantal getallen laat ingeven totdat
hij nul ingeeft. Druk het totaal en het gemiddelde af. Vergeet
niet te testen met nul getallen ingeven, en met een aantal keer
hetzelfde getal ingeven.

### Eindeloze loops

De code hieronder begint bij nummer 1 en telt nummers op totdat het
een nummer tegenkomt dat gekwadrateerd, deelbaar is door
1000\. De loop bevat een fout. Kijk of je de fout weet te vinden zonder
de code uit te voeren!

```python
nummer = 1
totaal = 0
while (nummer * nummer) % 1000 != 0:
    totaal += nummer
print( "Totaal is", totaal )
```

De titel boven deze paragraaf gaf het antwoord al: deze
code bevat een loop die nooit eindigt. Bij uitvoering lijkt het
alsof het programma "hangt"; wel draait maar niks doet. Het programma is echter 
bezig een nooit-eindigende optelling uit te voeren. `nummer` begint immers bij 1 maar
wordt in de loop nooit gewijzigd. Daarom wordt de boolean expressie nooit
`False`. Dit is een "eindeloze loop." Dit soort loops zijn het grootste
gevaar als je `while` loops implementeert.

Als je deze code uitvoert in IDLE, kun je de uitvoering afbreken door
`Ctrl-C` te drukken.

Om eindeloze loops te voorkomen, maak je er best de gewoonte van, wanneer je begint met het
schrijven van een `while` loop, onmiddellijk een regel code toe te voegen die
een wijziging maakt in hetgeen getest wordt. Bijvoorbeeld, als je schrijft `while i < 10`,
schrijf er dan meteen de regel `i += 1` onder. Daarna voeg je de
rest van de code tussen deze twee regels toe.

Verbeter de code hierboven zodat het geen eindeloze loop meer is.

### `while` loop oefeningen

Oefen een paar eenvoudige `while` loops.

Schrijf code die aftelt. Er wordt begonnen met een specifiek nummer,
bijvoorbeeld 10. Dan telt de code af naar nul, waarbij ieder nummer
geprint wordt (10, 9, 8, …). Nul wordt niet geprint, maar in plaats
daarvan drukt het programma de tekst "Start!" af.

De faculteit van een positief geheel getal is gelijk aan dat getal,
vermenigvuldigd met alle positieve gehele getallen die kleiner zijn
(exclusief nul). Je schrijft de faculteit als het getal met een
uitroepteken erachter. Bijvoorbeeld, de faculteit van 5 is
$$5! = 5 * 4 * 3 * 2 * 1 = 120$$. Schrijf code die de faculteit van een
getal berekent. Test het programma niet met getallen die hoog zijn, want
de faculteit stijgt exponentieel (het is voldoende om tot 10! te
testen). Hint: Om dit met een `while` loop te doen, moet je twee
variabelen gebruiken: één die aan het einde van de loop het antwoord
bevat, en één die de huidige factor bevat. In de loop vermenigvuldig je
het antwoord met de factor, alvorens 1 van de factor af te trekken.
Initialiseer deze variabelen met de juiste waarden voor de loop.
