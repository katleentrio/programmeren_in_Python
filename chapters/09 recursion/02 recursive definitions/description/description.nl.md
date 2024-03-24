Een voorbeeld van een recursieve definitie is de definitie van de
faculteit, die ik al heb geïntroduceerd in twee eerdere hoofdstukken. In
die hoofdstukken gaf ik de volgende definitie van de faculteit: de
faculteit van een positief geheel getal is dat getal, vermenigvuldigd
met alle positieve gehele getallen die kleiner zijn (exclusief nul).

Wiskundigen prefereren een recursieve definitie: De faculteit $$n!$$ van
een positief getal $$n$$ wordt als volgt berekend: $$1! = 1$$, en
$$n! = n * (n-1)!$$ voor $$n > 1$$.

Deze definitie is recursief omdat het refereert aan de faculteit van
$$n-1$$ om de faculteit van $$n$$ te definiëren. Dit leidt niet tot
eindeloze recursie, omdat op enig moment $$n$$ gelijk zal zijn aan $$1$$, en
de faculteit van $$1$$ is apart gedefinieerd.

Je kunt de faculteit als een recursieve functie als volgt implementeren:

```python
def faculteit( n ):
    if n <= 1:
        return 1
    return n * faculteit( n-1 )

print( faculteit( 5 ) )
```

Zie hoe deze functie exact de recursieve definitie van de faculteit
volgt: als `n` gelijk is aan 1, retourneert de functie 1, en anders
retourneert het `n` keer de faculteit van `n-1`. (Merk op dat ik
`n <= 1` schreef in plaats van `n == 1` om te voorkomen dat er problemen
ontstaan als de gebruiker de functie aanroept met, bijvoorbeeld, een
negatieve `n`.)

Voor het geval je het problematisch vindt om te begrijpen wat deze
functie doet, beschrijf ik hieronder de aanroepen die de functie doet
als hij wordt aangeroepen met 5 als argument. Ik laat aanroepen
inspringen als een "hoger-niveau aanroep" nog steeds actief is als de
aanroep wordt gemaakt. Een "return" die één inspringing dieper gaat dan
een "aanroep," wordt gegeven in die aanroep, en retourneert de gegeven
waarde.

```python
aanroep faculteit( 5 )
    aanroep faculteit( 4 )
        aanroep faculteit( 3 )
            aanroep faculteit( 2 )
                aanroep faculteit( 1 )
                    return 1
                return 2 * 1
            return 3 * 2
        return 4 * 6
    return 5 * 24
print( 120 )
```

### Wanneer gebruik je recursie

Als je doorhebt hoe de recursieve implementatie van de faculteit werkt,
ziet het er wellicht aantrekkelijk uit. Het is eenvoudig, elegant, en is
eigenlijk best wel "cool." Echter, de iteratieve implementatie van de
faculteit is zeer te prefereren boven de recursieve.

De reden blijkt uit de beschrijving van de aanroepen hierboven. Je ziet
dat voordat de aanroep `faculteit( 1 )` wordt gemaakt, er al vier
aanroepen van `faculteit()` in het geheugen van de computer staan. Als
je de faculteit van 100 zou willen berekenen, komen er niet minder dan
100 aanroepen van faculteit in het geheugen te staan alvorens er waardes
geretourneerd gaan worden. Dit is geen goed idee, en Python zou gebrek
aan (stack) geheugen kunnen krijgen, of heel, heel erg traag worden.

Daartegenover staat dat een iteratieve implementatie van de faculteit
slechts twee variabelen in het geheugen hoeft te houden. Dat is snel en
geeft geen gevaar dat de computer vastloopt. Je moet alleen recursieve
implementaties bouwen als:

-   recursie de meest natuurlijke manier is om de oplossing te
    implementeren; en

-   het recursieve proces gegarandeerd niet te diep gaat.

Iedere recursieve functie kan ook als een iteratief proces gebouwd
worden. Zo nu en dan kom je echter een probleem tegen waarvoor de
recursieve oplossing veel eleganter, leesbaarder, en onderhoudbaarder is
dan de iteratieve variant. In dat geval moet je overwegen een recursieve
oplossing te implementeren.


[^11]: Een data structuur is een manier om een bepaalde soort data in
    het geheugen van de computer op te slaan. Een integer, bijvoorbeeld,
    is een simpele data structuur die precies één geheel getal in het
    geheugen vasthoudt. Er bestaan complexere data structuren, die
    bijvoorbeeld een rij getallen vasthouden. Deze komen in latere
    hoofdstukken aan bod.