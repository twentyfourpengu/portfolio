"""
Einfache LSB-Steganographie: Text in einem PNG-Bild verstecken und wieder auslesen.
Benötigt: pip install pillow
"""
from PIL import Image

ENDE = "###"  # Markierung, damit wir wissen, wo die Nachricht aufhört


def verstecken(eingabe_bild, ausgabe_bild, nachricht):
    bild = Image.open(eingabe_bild).convert("RGB")
    pixel = list(bild.getdata())

    # Nachricht -> Bits (jedes Zeichen = 8 Bits)
    bits = "".join(f"{byte:08b}" for byte in (nachricht + ENDE).encode("utf-8"))

    if len(bits) > len(pixel) * 3:
        raise ValueError("Nachricht ist zu lang für dieses Bild.")

    neue_pixel = []
    i = 0
    for r, g, b in pixel:
        farben = [r, g, b]
        for k in range(3):
            if i < len(bits):
                # Letztes Bit auf 0 setzen, dann unser Bit einfügen
                farben[k] = (farben[k] & ~1) | int(bits[i])
                i += 1
        neue_pixel.append(tuple(farben))

    bild.putdata(neue_pixel)
    bild.save(ausgabe_bild, "PNG")  # Wichtig: PNG, nicht JPG!
    print(f"Nachricht in '{ausgabe_bild}' versteckt.")


def auslesen(bild_datei):
    bild = Image.open(bild_datei).convert("RGB")

    # Letztes Bit jedes Farbwerts einsammeln
    bits = "".join(str(farbe & 1) for pixel in bild.getdata() for farbe in pixel)

    # Je 8 Bits wieder zu einem Byte zusammensetzen
    daten = bytearray()
    for i in range(0, len(bits), 8):
        daten.append(int(bits[i:i + 8], 2))
        if daten.endswith(ENDE.encode("utf-8")):
            return daten[:-len(ENDE)].decode("utf-8")
    return "Keine versteckte Nachricht gefunden."


if __name__ == "__main__":
    
    verstecken("IMG_1311.png", "geheim.png", "Hallo! Das ist an sich kein Geheimnis. Aber ich suche einen Job :)")
    print("Ausgelesen:", auslesen("geheim.png"))
