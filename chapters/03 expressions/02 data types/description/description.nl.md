Alle data hebben een eigen data type. Het programma moet het data type kennen om er mee te kunnen werken. 
De drie belangrijkste data types die je op dit moment moet kennen zijn strings, integers, en
floats.

### String

Een string is een **tekst**, die bestaat uit nul of meerdere tekens tussen
aanhalingstekens. Je mag zowel dubbele als enkele aanhalingstekens
gebruiken, bijvoorbeeld: `"appel"` is equivalent met `'appel'`. 
Uitzondering hierop: als in de tekst een enkel aanhalingsteken voorkomt, moet je de tekst tussen dubbele aanhalingstekens plaatsen vb `"mango's"` is een correcte string, `'mango's'` niet en kan problemen geven in de code. Analoog voor een dubbel aanhalingsteken in een string.

*Ter info: Python herkent alleen "rechte" aanhalingstekens en niet "ronde."
Tekstverwerkers gebruiken soms ronde aanhalingstekens. Als je dus om wat 
voor reden dan ook Python code kopieert vanuit een
tekstverwerker kan dit mogelijk problemen geven.*

### Integer

Integers zijn **gehele getallen** die positief, negatief, of nul kunnen
zijn. Er is een zekere grens aan hoe groot integers kunnen worden, maar voor 
de meeste toepassingen kom je nooit aan die grenzen toe.

Gebruik geen scheidingstekens tussen de veelvouden van 1000 om ze leesbaarder te maken. Je
moet het getal 1 miljard dus schrijven als `1000000000`.

### Float

Floats zijn **decimale getallen**. Merk op dat je in Python een **punt** moet
gebruiken als decimaal-scheidingsteken, en geen komma. Bijvoorbeeld, `3.14159265`.
Ook een float is begrensd, maar ook hier is het onwaarschijnlijk dat je ooit de maximale grootte bereikt.

`13` is een integer. Wil je dat dit getal een float is, dan kan je dat doen door 
er `.0` achter te zetten. `13.0` is een float. Beide getallen geven dezelfde waarde weer.
