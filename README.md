# Steinschlag

## Projektmitglieder

- Aaron Brülisauer
- Benjamin Würmli
- Denis Schatzmann
- Oliver Pejic

## Aufgabenstellung

Die Kantonsstrasse unterhalb Schiers (GR) ist vom Steinschlag betroffen. Steine lösen sich von zwei unterschiedlichen Stellen an der Felswand ab (Ablösungszone 1 und Ablösungszone 2). Der betroffene Strassenabschnitt ist mit Steinfangnetzen gesichert, die jedoch in die Jahre gekommen sind und die angestrebte Sicherheit nicht mehr gewährleisten können. Die Planung für Ersatznetze hat bereits begonnen, kann aber frühstens in einem Jahr umgesetzt werden.

In den letzten Monaten haben sich mehrere Steinschlagereignisse ereignet. Kommt es im Lauf des nächsten Jahres zu weiteren vergleichbaren Ereignissen, könnten die alten Sicherheitsnetze versagen und die Verkehrsteilnehmer einem grossen Sicherheitsrisiko ausgesetzt sein. Die Bevölkerung ist verunsichert und der Kantonsingenieur muss schnell entscheiden, ob das Risiko für die Verkehrsteilnehmer zu gross ist und die Kantonsstrasse vorübergehend gesperrt werden muss. Der Kantonsingenieur hat sie beauftragt, anhand von vorhanden Daten die Wahrscheinlichkeit eines Todesfalls zu berechnen und eine Empfehlung bezüglich der Schliessung bzw Offenhaltung der Strasse auszusprechen.

Damit die Strasse offen bleiben kann, muss gezeigt werden, dass die jährliche Wahrscheinlichkeit von Todesfällen infolge Steinschlags kleiner als 0.0001 ist. Für die Berechnungen soll ein gut strukturierter und dokumentierter Code in Python oder R entwickelt werden.

# Annahmen & Fragen zur fiktiven Realität

## Vorgehen

1. Wahrscheinlichkeit dass Stein überhaupt auf Strasse gelangt? Bzw. genau auf ein Auto trifft?
2. Welche Faktoren sind noch relevant? Nach ersten Berechnungen anschauen.

## Allgemein

Relevanz fürs Resultat? Wie gut kann ich diese Wahrscheinlichkeit bestimmen? Relevanz ist aktuell oft noch unklar. Jeder zusätzliche Parameter birgt die Gefahr von Fehler -> Occam's Razor

## Fragen

- Alle Steine landen im selben Netz? -> alle am selben Ort
- Wie grosse Steine sind zu erwarten? -> Von Daten hochrechnen
- Wie gross ist die Wahrscheinlichkeit, dass ein Auto genau dann an dem Ort auf der Strasse ist, wenn das Netz reisst? -> Reaktion, Bremsweg, Handy?, Pneu, Witterung, Fahrzeugtyp
- Wie gross ist die Wahrscheinlichkeit, dass ein Stein auf der Strasse liegen bleibt? -> Wenn das Netz reisst, dann kommen viele Steine auf die Strasse und bleibt dann nicht sowieso einer liegen?
- Ist die Strasse gerade? -> unbekannt -> gerade
- Direkter Treffer: Todeswahrscheinlichkeit höher?
- Hineinfahren: überlebt?
- Maximale Geschwindigkeit: 60 km/h -> Verteilung der Geschwindigkeit? -> erst mal mit 60 rechnen und dann schauen wo man im Verhältniss zum Greznwert ist
- Reaktionszeit des Fahrers? -> 1 Sekunde
- Gefahr für die die die Steine entfernen?
- Wie lange dauert das Entfernen eines Steines? -> Alle Steine auf einmal
  - Ist die Strasse während dem Entfernen gesperrt?
  - Wird jeder Stein einzeln entfernt oder alle auf einmal? Um welche Uhrzeit?
- Spielt das Wetter eine Rolle? -> Kommen dann mehr grössere und/oder schnellere Steine?
- Können Steine in Grössekategorien eingeteilt werden und damit errechnet werden, wie wahrscheinlich es ist, dass ein x-fach grösserer Stein fällt?
  - 0.1KG, 1KG, 10KG, 100KG, 1000KG, 10000KG, ... -> folgt Verteileung? -> Warum kategorisieren? -> mal Q-Q-Plot machen und schauen was rauskommt -> wie bei wer
- Uhrzeit? -> EDA verteilung wärend des Tages
- Sonneneinstrahlung?
- Wo liegen die Ablösungszonen (eine oberhalb der anderen, nebeneinander)?
- Wie stabil sind Autos? -> wann geht Netz kaputt? -> irrelevant
- Was passiert mit den Steinen im Netz, wenn es reisst? Rollen sie auf die Strasse? -> Steine auf Strasse
- Spielt es eine Rolle wie viele Steine im Netz sind, wenn es reisst? -> Wahrscheinlich nicht, denn wenn das Netz reisst waren es sicher ausreichend Steine um eine Gefahr darzustellen.
- Mit welcher Aufprallgeschwindigkeit stirbt der Insasse. -> Recherchieren
- Schlucht auf der anderen Seite der Strasse?
- Leitplanke? -> Leitplanke behält Steine auf Strasse?
- Masse ist von Experten geschätzt, aber wie genau? -> gibt Methoden, relativ aufwändig, wie viel nutz es beim todesfall schätze
- 2000KG: Total aller Steine im Netz oder einzelner Stein? -> total aller Steine im Netz
- Verteilung der Autos in einem Tag? -> haben die Steine eine ungleichmässige Verteilung? -> falls nein muss man es noch anschauen
- Verteilung der Steine (für alle Variablen)
- Was ist, wenn es gerissen ist, aber keiner gestorben ist? -> zusammen anschauen und das annehmen was in der Realität passiere würde
  - Fallen Steine auf die Strasse?
  - Wird aufgeräumt?
  - Wird repariert?
  - Wie lange dauert es, bis das Netz repariert ist?
