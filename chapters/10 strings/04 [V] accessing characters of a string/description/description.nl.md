## Moetje

Ik heb al meerdere keren laten zien dat een string een verzameling is
van tekens in een specifieke volgorde. Je kunt de individuele tekens van
een string middels indices benaderen.

### String indices

Ieder teken in een string heeft een positie, en die positie kun je
weergeven door het index nummer van de positie. De indices beginnen bij
0 en lopen op tot aan de lengte van de string. Hieronder zie je het
woord "python" op de eerste regel, met op de tweede en derde regel
indices voor ieder teken in deze string:

| p | y | t | h | o | n |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | 1 | 2 | 3 | 4 | 5 |
| -6 | -5 | -4 | -3 | -2 | -1 |
{:class="table table-striped table-condensed" style="width:auto;margin-left:auto;margin-right:auto;"}

Zoals je kunt zien, kun je positieve indices gebruiken die beginnen met
0 bij de eerste letter van de string, en die oplopen tot het einde van
de string. Je kunt ook negatieve indices gebruiken, die starten met -1
bij de laatste letter van de string, en die aflopen totdat de eerste
letter van de string bereikt is.

De lengte van een string `s` kun je berekenen met `len(s)`; de laatste
letter van de string heeft dus index `len(s)-1`. Met negatieve indices
heeft de eerste letter van de string de index `-len(s)`.

Als een string is opgeslagen in een variabele, dan kun je de individuele
letters van de string benaderen via de variabele naam en de index van de
gevraagde letter tussen vierkante haken (`[]`) rechts ernaast.

```python
fruit = "aardbei"
print( fruit[4] ) 
print( fruit[2] ) 
print( fruit[1] )
print( fruit[-4] )
print( fruit[-2] )
print( fruit[-5] )
print( fruit[-1] )
print( fruit[5] )
```

In principe mag je een index ook gebruiken bij een string die niet in
een variabele staat, bijvoorbeeld, `"aalbes"[3]` is de letter `"b"`. Het
mag duidelijk zijn dat niemand dat ooit doet.

### Strings doorlopen

Ik heb eerder uitgelegd hoe je de tekens van een string kunt doorlopen
middels een `for` loop:

```python
fruit = 'appel'
for teken in fruit:
    print( teken, '- ', end='' )
```

Nu je indices begrijpt, realiseer je je waarschijnlijk wel dat je die
ook kunt gebruiken om een string te doorlopen:

```python
fruit = 'appel'

for i in range( 0, len( fruit ) ):
    print( fruit[i], "- ", end="" )
print()

i = 0
while i < len( fruit ):
    print( fruit[i], "- ", end="" )
    i += 1
```

Als je voldoende hebt aan toegang krijgen tot de individuele tekens in
de string, is de eerste methode, waarbij de constructie
`for <teken> in <string>` wordt gebruikt, verreweg het meest elegant en
leesbaar. Maar soms moet je een probleem oplossen waarbij een andere
methode nodig is.

## Magje

Schrijf een programma dat van een string de indices print van alle
klinkers (a, e, i, o, en u). Dit kan met een `for` loop of een `while`
loop, maar de `while` lijkt iets geschikter.

Schrijf een programma dat twee strings gebruikt. Voor ieder teken in de
eerste string dat in de tweede string precies hetzelfde teken heeft met
precies dezelfde index, druk je het teken en de index af. Pas op voor
een "index out of bounds" runtime error. Test met de strings
`"The Holy Grail"` en `"Life of Brian"`.

Schrijf een functie die een string als argument krijgt, en die dan een
nieuwe string retourneert die hetzelfde is als het argument, maar
waarbij ieder teken dat geen letter is vervangen is door een spatie
(bijvoorbeeld, de uitdrukking `"ph@t l00t"` wordt gewijzigd in
`"ph t l  t"`). Om zo'n functie te schrijven begin je met een lege
string, en doorloopt de tekens van het argument één voor één. Als je een
acceptabel teken tegenkomt, voeg je het toe aan de nieuwe string. Anders
voeg je een spatie toe aan de nieuwe string. Je kunt testen of een teken
acceptabel is met eenvoudige vergelijkingen, bijvoorbeeld, alle kleine
letters kun je herkennen omdat ze de test `ch >= 'a' and ch <= 'z'`
`True` maken.