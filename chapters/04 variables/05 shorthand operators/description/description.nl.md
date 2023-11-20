Door gebruik te maken van de operatoren die we reeds besproken,
kun je de inhoud van variabelen meermaals wijzigen doorheen de code.
Een voorbeeld van een veel voorkomende aanpassing van de inhoud van een
numerieke variabele, is dat je de waarde van de variabele met waarde 1 wenst te verhogen. 
Voor een aantal bewerkingen die veelvuldig voorkomen, bevat Python een 
aantal "verkorte opartoren" om de inhoud van variabelen aan te passen.

Bekijk de volgende code:

```python
aantal_bananen = 100
aantal_bananen = aantal_bananen + 1
print( aantal_bananen )
```

Bovenstaande code geeft hetzelfde resultaat als onderstaande (test maar eens uit):

```python
aantal_bananen = 100
aantal_bananen += 1
print( aantal_bananen )
```

In de laatste code is de tweede regel beduidend korter dan in het eerste voorbeeld.
Wanneer je de waarde van een variabele met een vaste waarde wenst te verhogen,
kun je `+=` gebruiken als assignment operator; aan de linkerkant staat de variabele,
wat je erbij op wilt tellen aan de rechterkant. 

Op analoge manier kun je `-=` gebruiken om een vaste waarde af te trekken van
een variabele, `*=` voor vermenigvuldiging, `/=` voor deling, ... . 
De meest gebruikte verkorte operator is `+=`, de anderen komen zelden voor.

Wat is het resultaat van onderstaande code?

```python
aantal_bananen = 100
aantal_bananen += 12
aantal_bananen -= 13
aantal_bananen *= 19
aantal_bananen /= aantal_bananen
print( aantal_bananen )
```
