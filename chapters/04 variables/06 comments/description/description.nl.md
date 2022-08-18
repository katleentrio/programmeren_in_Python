Tot hiertoe was de code die je opstelde steeds vrij eenvoudig en
beperkt in lengte. Dit is echter meestal niet het geval. 
Om een meer complexere en langere code vlot te kunnen lezen
en goed te weten welke stappen er precies worden uitgevoerd,
is het gebruik van commentaarregels aan te raden.
Commentaarregels zijn teksten in code die door Python genegeerd worden
tijdens de uitvoering, maar die bedoeld zijn om
specifieke delen van de code uit te leggen.

Je kunt op twee manieren commentaar schrijven in Python code.

-   **Regelcommentaar** door gebruik te maken van de "hash mark" (\#) voor
    de commentaar-tekst.
    Alles wat op dezelfde regel code rechts van de markering staat, 
    is commentaar en wordt genegeerd door Python.
    Uiteraard geldt dit niet indien de hash mark deel uitmaakt van een string.

-   **Blokcommentaar** door gebruik te maken van drie aanhalingstekens voor 
    en drie aanhalingstekens achter de commentaar-tekst.
    Alles wat tussen de drie aanhalingstekens staat, is commentaar en 
    wordt genegeerd door Python. In tegenstelling tot bij regelcommentaar
    mag een blokcommentaar meerdere regels beslaan.
    Blokcommentaar moet steeds aan het begin van een regel starten en kan 
    niet gebruikt worden in een code-blok dat inspringt.

De volgende code laat voorbeelden zien van beide manieren van
becommentariëren:

```python
# Voorbeeld van invoegen van commentaar in code.
# De hash mark geldt enkel per regel en moet dus herhaald worden
# indien de commentaar meerdere regels beslaat.
print( "Iets..." ) # Dat wat rechts van het teken staat is commentaar.
"""Blokcommentaar geef je door gebruik te maken van 
drievoudige aanhalingstekens. Dit soort commentaar mag
meerdere regels beslaan.""" 
'''Blokcommentaar kan geplaatst worden tussen drie dubbele of 
tussen drie enkele aanhalingstekens.'''
print( "Klaar." )
```
