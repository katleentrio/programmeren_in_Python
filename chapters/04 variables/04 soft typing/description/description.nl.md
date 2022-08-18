Alle variabelen hebben een data type. In veel programmeertalen wordt het
data type van een variabele gespecificeerd op het moment dat de
variabele gecreëerd wordt. Zo zet je in bijvoorbeeld C++ het type van een
variabele voor de variabele naam op het moment dat je de variabele
definieert:

```python
int secs_per_week = 7 * 24 * 60 * 60;
```

Dit wordt “hard typing” genoemd. Wanneer je nu een
waarde in een variabele probeert te stoppen van het verkeerde
type, kan het programma een foutmelding geven. Dit is een voordeel want
hierdoor kunnen een aantal vervelende problemen vermeden worden 
die kunnen optreden tijdens het schrijven of uitvoeren van een programma.

Dit is niet zo in Python. Je geeft in Python geen vast type aan een variabele,
maar de variabele neemt het type aan van de waarde die erin
is opgeslagen. Dit betekent dat als een variabele een nieuwe waarde
krijgt, het type ook kan veranderen. Dit noemt men “soft typing”.

We behandelden tot nu toe de data types integer, float, en string.
Je kunt het data type van een waarde of variabele steeds controleren met
behulp van de functie `type()`.

```python
a = 3
print( type( a ) )
a = 3.0
print( type( a ) )
a = "3.0"
print( type( a ) )
```

Je kunt operatoren gebruiken om berekeningen te maken tussen variabelen.
Omdat variabelen een type hebben, past de toepassing van operatoren zich
aan aan de types van de variabelen. We verduidelijken dit aan de hand van onderstaand
voorbeeld. In de code wordt de optelling ($$+$$) twee keer
gebruikt, doch telkens met een andere toepassing in functie van de variabele types.

```python
a = 1
b = 4
c = "1"
d = "4"
print( a + b )
print( c + d )
```

Omdat `a` en `b` beide getallen zijn, is de $$+$$ in `a + b` de numerieke
optelling. Omdat `c` en `d` beide strings zijn, is de $$+$$ in `c + d` de
“concatenate” operator en plakt dus beide strings aan elkaar.

Wat toont de code hieronder? Denk erover na, en voer dan de code uit.
Zorg dat je snapt wat er gebeurt.

```python
naam = "John Cleese"
print( "naam" )
```

Hoe kan je er voor zorgen dat de naam van een bekend lid van Monty
Python wordt getoond?

*(Antwoord eerste vraag: naam. Oplossing tweede vraag: verwijder de aanhalingstekens
zodat de string gewijzigd wordt in de variabele naam)*

