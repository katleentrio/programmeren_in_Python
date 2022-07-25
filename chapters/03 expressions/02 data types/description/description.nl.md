Voor we aan de slag gaan met expressies, moet ik ook de data types bespreken. 
De drie belangrijkste data types die je op dit moment moet kennen zijn strings, integers, en
floats.

### Strings

Een string is een tekst, die bestaat uit nul of meerdere tekens tussen
aanhalingstekens. Je mag zowel dubbele als enkele aanhalingstekens
gebruiken, bijvoorbeeld: `"appel"` is
equivalent met `'appel'`. Er is echter wel een uitzondering: als in 
je tekst een enkel aanhalingsteken voorkomt,
moet je de tekst tussen dubbele aanhalingstekens plaatsen om problemen te voorkomen;
dus `"mango's"` is een correcte string, terwijl
`'mango's'` niet correct is. Hetzelfde geldt natuurlijk voor een dubbel
aanhalingsteken in een string, die dan omsloten moet worden door enkele
aanhalingstekens.

Als er in je string zowel dubbele als enkele
aanhalingstekens voorkomen, kan je dat oplossen door in de string een
"backslash" (`\`) op te nemen voor ieder dubbel of enkel aanhalingsteken
dat in de string staat. Dit vertelt Python dat dat aanhalingsteken
behandeld moet worden als een teken in de string, en niet als een
afsluiting van de string. Dus `'mango\'s'` is een correcte string, wat
je kunt zien als je hem probeert te printen:

```python
print( 'mango\'s' )
```

Maar wat moet je doen als je een echte backslash wilt opnemen in de
string en die backslash moet dan ook nog eens staan voor een dubbel of
enkel aanhalingsteken? Dat kun je oplossen door voor de backslash een
extra backslash op te nemen. In het voorbeeld hieronder geeft de eerste 
backslash aan dat de volgende een teken van de string is, de derde backslash
maakt op zijn beurt een teken van het enkel aanhalingsteken:

```python
print( 'mango\\\'s' )
```

Dit komt echter niet zo dikwijls voor. Momenteel is het dan ook 
voldoende om te weten dat een string een tekst is die omsloten is
door dubbele of enkele aanhalingstekens.

Let erop dat je in Python programma's alleen "rechte" aanhalingstekens gebruikt
en niet "ronde." Deze laatste worden niet herkend door Python.
Tekstverwerkers gebruiken soms ronde aanhalingstekens. 
Als je om wat voor reden dan ook Python code kopieert van of naar een
tekstverwerker, zou het kunnen gebeuren dat je aanhalingstekens
gewijzigd worden naar ronde. Kijk daarvoor uit.

### Integers

Integers zijn gehele getallen, die positief of negatief (of nul) kunnen
zijn. Er is een zekere grens aan hoe groot integers kunnen worden, 
afhankelijk van je computer en besturingssysteem. Voor de meeste
toepassingen maakt dit niet uit, en kom je nooit aan die grenzen toe.

Als je integers in Python gebruikt, mag je ze niet schrijven met
scheidingstekens tussen de veelvouden van 1000 om ze leesbaarder te maken. Je
moet het getal 1 miljard dus schrijven als `1000000000` en niet als
`1,000,000,000` (de Engelse conventie) of `1.000.000.000`.

### Floats

Floats, wat de afkorting is voor "floating-point getallen" ("gebroken
getallen"), zijn decimale getallen. Bijvoorbeeld, `3.14159265` is
een float. Merk op dat je in Python een punt in plaats van een komma moet
gebruiken als decimaal-scheider.

Als je een integer hebt die je wilt gebruiken als float, kun je dat doen
door er `.0` achter te zetten. Bijvoorbeeld, `13` is een integer, maar
`13.0` is een float. Ze geven nog steeds dezelfde waarde weer, en als je
ze in code met elkaar vergelijkt (dat bespreek ik in hoofdstuk
<a href="#ch:conditions" data-reference-type="ref" data-reference="ch:conditions">7</a>),
dan zal Python stellen dat ze hetzelfde zijn.

Ook aan de grootte en precisie van floats zijn er bepaalde begrenzingen, maar ook hier is het onwaarschijnlijk 
dat je ooit de maximale groottes bereikt,
aangezien Python wetenschappelijke notatie voor grote getallen gebruikt.

Door de manier waarop Python floats opslaat, kunnen bepaalde getallen
niet precies vastgelegd worden. Bijvoorbeeld, het statement
`print( (431 / 100) * 100 )` geeft als antwoord 430.99999999999994 en
niet 431 zoals je zou verwachten. Als je weet dat de uitkomst van een
berekening waarin floats zitten een integer moet zijn, dan doe je er
goed aan om de uitkomst af te ronden naar het dichtstbijzijnde gehele
getal. Dat kun je doen met behulp van de `round()` functie die ik
bespreek in hoofdstuk
<a href="#ch:simplefunctions" data-reference-type="ref" data-reference="ch:simplefunctions">6</a>.
