Een veelvoorkomende oorzaak van functionele fouten in programma's is dat
variabelen andere waarden bevatten dan die jij verwacht.
Om uit te zoeken waar de fout zich precies bevindt in de code
kan je de namen en waarden van de variabelen printen op cruciale plaatsen.

Bekijk de volgende code. Deze geeft een foutmelding bij uitvoering.
*Ken je de operator % nog? Modulo geeft de rest bij deling*

```python
nr1 = 5
nr2 = 4
nr3 = 5
print( nr3 / (nr1 % nr2) )
nr1 = nr1 + 1
print( nr3 / (nr1 % nr2) )
nr1 = nr1 + 1
print( nr3 / (nr1 % nr2) )
nr1 = nr1 + 1
print( nr3 / (nr1 % nr2) )
```

Bij eenvoudige code vind je misschien snel de fout door de code door te nemen.
Dit lukt echter niet altijd meteen.  
Wanneer je dit programma uitvoert, krijg je als feedback dat er een fout ontdekt 
wordt op regel 10. Alles werkt dus nog op regel 9. Je kan dus
een extra regel code zetten tussen regel 9 en 10 waarbij de waarde van
`nr1`, `nr2`, `nr3` en mogelijk ook `nr1 % nr2` afgedrukt wordt. Zo ontdek je
waarschijnlijk sneller wat er misloopt. 
`print()` statements kan je zonder problemen tussen bestaande code toevoegen,
deze veranderen immers niets aan de variabelen.

Het uitzoeken waar de fout zich bevindt in, en verbeteren van de code, noemen we de code “debuggen”. 