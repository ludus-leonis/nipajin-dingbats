# NIP'AJIN Dingbats

[Deutsch](README.md) | [English](README.en.md).

## Über

Dieses Repository enthält die Quellen für die SIL OFL 1.1 lizensierte Symbol-Schriftart *NIP'AJIN Dingbats*. Diese enthält eine Handvoll, im Pen'n'Paper Rollenspiel [NIP'AJIN](http://ludus-leonis.com/nipajin) Verwendung findende Symbole:

* `a` - Zeit-danach-Symbol
* `b` - Zeit-davor-Symbol
* `B` - Buch-Symbol
* `f` - Faust-Würfel
* `h` - Herz-Würfel
* `s` - Schild-Würfel
* `t` - Zielscheibe-Symbol

## Schnellanleitung

Im Unterverzeichnis `glyphs` befinden sich für die einzelnen Zeichen/Buchstaben der Schriftart je eine `.svg` Datei. Aus diesen Dateien kann das Python-Script `generate.py` eine TrueType Schrift generieren. Voraussetzung dafür ist, dass [FontForge](http://fontforge.github.io) und die FontForge-Python-Bindings installiert sind. Dann kann mit

```
nipajin-dingbats$ make
```

die `.ttf` Datei erstellt werden. Diese ist nach dem Lauf im Ordner `out` zu finden.
