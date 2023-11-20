In Python neemt een variabele het data type aan van de waarde die erin
wordt opgeslagen. Dit betekent dat als een variabele een nieuwe waarde
krijgt, het data type van de variabele ook kan veranderen. Dit noemt men “soft typing”.
*Ter info: dit is in de meeste andere programmeertalen niet het geval.*
*Daar moet je zelf het data type specificeren op het moment dat de variabele gecreëerd wordt.*
*Dit wordt “hard typing” genoemd.*

We behandelden tot nu toe de data types integer, float en string.
Je kunt het data type van een waarde of variabele steeds controleren / opvragen met
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

