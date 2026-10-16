(german documentation)
# 🐶 LSB-Steganographie in Python

Ein kleines Python-Projekt, das Textnachrichten unsichtbar in PNG-Bildern versteckt und wieder ausliest.

Die beiden Bilder unten sehen identisch aus. In einem davon steckt eine Nachricht.

| Original | Mit versteckter Nachricht |
|:---:|:---:|
| ![Original](IMG_1311.png) | ![Mit Nachricht](geheim.png) |

---

## Wie funktioniert das?

Jedes Pixel eines Bildes besteht aus drei Farbwerten: **Rot, Grün und Blau**, jeweils zwischen 0 und 255. Als Binärzahl hat jeder Wert 8 Bits:

```
200 = 1100100[0]
              ↑
     Least Significant Bit (LSB)
```

Das letzte Bit (Least Significant Bit) hat den geringsten Einfluss auf die Farbe. Ändert man es, verschiebt sich der Wert um höchstens 1, also z. B. von 200 auf 201. Für das menschliche Auge ist dieser Unterschied nicht wahrnehmbar.

Genau dort wird die Nachricht gespeichert:

1. Die Nachricht wird in UTF-8-Bytes und dann in Bits umgewandelt (8 Bits pro Zeichen).
2. Eine Endmarkierung (`###`) wird angehängt, damit das Programm beim Auslesen weiß, wo die Nachricht aufhört.
3. Jedes Bit der Nachricht ersetzt das letzte Bit eines Farbwerts. Pro Pixel passen also 3 Bits.
4. Das Bild wird verlustfrei als PNG gespeichert.

Beim Auslesen läuft das Ganze rückwärts: Alle letzten Bits werden eingesammelt, zu Bytes zusammengesetzt und so lange gelesen, bis die Endmarkierung auftaucht.

---

## Was wurde verändert?

Das Differenzbild zeigt, welche Pixel sich zwischen Original und verändertem Bild unterscheiden:

![Differenzbild](unterschied.png)

Fast das gesamte Bild ist schwarz, also unverändert. Nur in der **oberen linken Ecke** gibt es eine winzige Linie veränderter Pixel, denn dort beginnt das Skript zu schreiben.

Die Beispielnachricht hat 66 Zeichen. Zusammen mit der Endmarkierung sind das 69 Bytes, also 552 Bits. Bei 3 Bits pro Pixel werden damit **maximal 184 Pixel** berührt. Tatsächlich ändern sich sogar weniger, weil ungefähr die Hälfte der Bits zufällig schon den richtigen Wert hat.

---

## Installation

Voraussetzung ist Python 3 sowie die Bildbibliothek Pillow:

```bash
pip install pillow
```

---

## Verwendung

### Nachricht verstecken

```python
from stego import verstecken

verstecken("IMG_1311.png", "geheim.png", "Meine geheime Nachricht")
```

### Nachricht auslesen

```python
from stego import auslesen

print(auslesen("geheim.png"))
```

### Direkt ausführen

```bash
python stego.py
```

Das versteckt die Beispielnachricht in `IMG_1311.png`, speichert das Ergebnis als `geheim.png` und liest die Nachricht anschließend zur Kontrolle wieder aus.

---

## Kapazität

Wie viel Text in ein Bild passt, hängt von seiner Größe ab:

```
max. Bytes = (Breite × Höhe × 3) / 8  −  3 (Endmarkierung)
```

Ein Bild mit 1920 × 1080 Pixeln kann also rund **777.000 Bytes** aufnehmen. Ist die Nachricht zu lang, bricht das Skript mit einer Fehlermeldung ab.

---

## Grenzen und Hinweise

**Nur verlustfreie Formate.** Die Nachricht überlebt nur in PNG (oder anderen verlustfreien Formaten). JPG-Kompression verändert genau die niedrigsten Bits und zerstört die Nachricht dabei. Das gilt auch für Plattformen wie LinkedIn, WhatsApp oder Instagram, die Bilder beim Hochladen neu komprimieren. Das Original-PNG in diesem Repository enthält die Nachricht noch.

**Keine Verschlüsselung.** Die Nachricht ist versteckt, aber nicht geschützt. Wer weiß, wonach er suchen muss, kann sie mit wenigen Zeilen Code auslesen. Für echte Vertraulichkeit sollte der Text vorher verschlüsselt werden.

**Statistisch erkennbar.** Einfache LSB-Steganographie lässt sich mit statistischen Verfahren (z. B. Chi-Quadrat-Analyse) nachweisen, besonders bei langen Nachrichten. Fortgeschrittene Verfahren verteilen die Bits zufällig über das Bild oder nutzen andere Ansätze.

**Endmarkierung im Text.** Enthält die Nachricht selbst die Zeichenfolge `###`, wird sie beim Auslesen an dieser Stelle abgeschnitten. Eine robustere Lösung wäre, die Länge der Nachricht am Anfang mitzuspeichern.

**Transparenz geht verloren.** Das Bild wird nach RGB konvertiert, ein vorhandener Alpha-Kanal wird dabei entfernt.

---

## Mögliche Erweiterungen

- Längenangabe statt Endmarkierung
- Verschlüsselung der Nachricht vor dem Verstecken (z. B. mit AES)
- Verteilung der Bits auf zufällige Pixel anhand eines Passworts
- Verstecken von Dateien statt nur Text
- Kommandozeilen-Interface mit `argparse`
- Automatische Erzeugung eines verstärkten Differenzbildes

---

## Projektstruktur

```
├── stego.py          # Verstecken und Auslesen
├── IMG_1311.png      # Originalbild
├── geheim.png        # Bild mit versteckter Nachricht
├── unterschied.png   # Differenzbild
└── README.md
```

---

## Und was steht nun drin?

Probier es aus:

```bash
python -c "from stego import auslesen; print(auslesen('geheim.png'))"
```

Kleiner Spoiler: Es ist an sich kein Geheimnis. 😉

---

## Kontakt

Ich bin aktuell auf der Suche nach einer neuen Stelle im IT-Bereich. Wenn dich das Projekt interessiert hat, freue ich mich über eine Nachricht:

- LinkedIn: [Dein Profil](https://www.linkedin.com/in/lan-anh-chung)
