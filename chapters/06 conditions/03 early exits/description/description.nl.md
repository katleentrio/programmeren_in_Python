**Binnen de toepassingen waarvoor wij Python gebruiken, is dit een minder interessant hoofdstukje. Je mag deze activiteit dan ook overslaan.**

Soms wil je onder bepaalde voorwaarden een programma vroegtijdig beëindigen. 
Stel dat het programma input vraagt aan de gebruiker om hier verder mee te werken, maar dat de input aan bepaalde voorwaarden moet voldoen. Wanneer de gebruiker dan een waarde invoert die niet aan de gestelde voorwaarden voldoet, wil je het programma meteen beëindigen. Kijk naar het volgende voorbeeld.

```python
num = int(input( "Geef een geheel getal verschillend van nul: " ))
if num == 0:
    print( "Je had een getal verschillend van nul moeten geven!" )
else:
    print( "Ik deel 10 door ", num )
    print( "Ik tel hier 100 bij op." )
    print( "enzovoort, enzovoort" )
```

Door de `else` tak toe te voegen, voert het programma ofwel de acties uit die horen bij de foutief ingevoerde waarde, ofwel de acties die uitgevoerd moeten worden indien een correcte waarde wordt ingegeven. 
Je kan dit op een elegantere manier oplossen door gebruik te maken van de functie `exit()` die in de module `sys` staat. De code wordt dan:

```python
from sys import exit

if num == 0:
    print( "Je had een getal verschillend van nul moeten geven!" )
    exit()

print( "Ik handel je getal", num, "af" )
print( "Nog meer code" )
print( "Honderden regels code" )
```

Wanneer de gebruiker nu een nul invoert, wordt het programma meteen beeindigd; geen enkele van commando's die volgen na de `exit()` functie worden nog uitgevoerd. 
