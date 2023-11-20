**Uitzoeken waar een fout zich bevindt in de code en verbeteren van de code, noemen we de code “debuggen”.**

Een veelvoorkomende oorzaak van functionele fouten in programma's is dat
variabelen andere waarden bevatten dan wat jij verwacht. Bij eenvoudige code vind je mogelijk de fout door de code door te nemen. Dit lukt echter niet altijd. 

Om uit te zoeken en te controleren waar de fout zich precies bevindt in de code,
kan je de namen en waarden van de variabelen printen op cruciale plaatsen. Op die manier kan je detecteren waar het precies fout gaat.

Bekijk en test de volgende code in Spyder. 
*(Ken je de operator % nog? Modulo geeft de rest bij deling.)*

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

Er treedt een foutmelding op bij regel 10. Alles werkt dus nog op regel 9. Om de fout snel op te sporen, kan je tussen regel 9 en 10 een extra regel code zetten, waarbij de waarden van
`nr1`, `nr2`, `nr3` en mogelijk ook `nr1 % nr2` afgedrukt worden. 
`print()` statements kan je zonder problemen tussen bestaande code toevoegen,
deze veranderen immers niets aan de variabelen. Doe de test in Spyder. Wat liep er mis?
