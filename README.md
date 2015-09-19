# NIP'AJIN Dingbats

[Deutsch](README.md) | [English](README.en.md).

## Über

Dieses Repository enthält die Quellen für die SIL OFL 1.1 lizensierte Symbol-Schriftart *NIP'AJIN Dingbats*. Diese enthält eine Handvoll, im Pen'n'Paper Rollenspiel [NIP'AJIN](http://ludus-leonis.com/nipajin) Verwendung findende Symbole:

* `a` - Zeit-danach
* `b` - Zeit-davor
* `f` - Faust
* `h` - Herz
* `p` - Buch
* `s` - Schild
* `t` - Zielscheibe

Der reguläre Schriftschnitt enthält die Symbole auf "weißem" Grund. Der fette Schnitt enthält die Symbole in abgerundeten Quadraten (Würfel), der kursive Schnitt in Kreisen.

## Schnellanleitung

Im Unterverzeichnis `glyphs` befinden sich für die einzelnen Zeichen/Buchstaben der Schriftart je eine `.svg` Datei. Aus diesen Dateien kann das Python-Script `generate.py` eine TrueType Schriftfamlie generieren. Voraussetzung dafür ist, dass [FontForge](http://fontforge.github.io) und die FontForge-Python-Bindings installiert sind. Dann können mit

```
nipajin-dingbats$ make
```

die `.ttf` Dateien erstellt werden. Diese sind nach dem Lauf im Ordner `out` zu finden.
