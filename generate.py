#!/usr/bin/python
# -*- coding: utf-8 -*-
# simple .svg to .ttf icon font converter, (c) 2015 Markus Leupold-Löwenthal

import fontforge
import psMat

def addIcon( font, glyph, svgFileName ):
   "add a svg as icon glyph"
   font.createChar(glyph).importOutlines(svgFileName).correctDirection()
   return;

def addDie( font, glyph, svgFileName ):
   "add a svg as die glyph (with a box)"
   font.createChar(glyph).importOutlines("glyphs/_box.svg").importOutlines(svgFileName).correctDirection()
   return;

font = fontforge.font()

font.fontname = "NIPAJIN-Dingbats"
font.fullname = "NIP'AJIN Dingbats"
font.familyname = "NIP'AJIN Dingbats"
font.version = "v1.0.0"
font.copyright = "Copyright (c) 2015, LUDUS LEONIS / Markus Leupold-Loewenthal (http://ludus-leonis.com/),\nwith Reserved Font Name \"NIP'AJIN Dingbats\".\n\nThis Font Software is licensed under the SIL Open Font License, Version 1.1.\nThis license is available with a FAQ at: http://scripts.sil.org/OFL"

# dice symbols
addDie (font, ord('f'), "glyphs/fist.svg")
addDie (font, ord('s'), "glyphs/shield.svg")
addDie (font, ord('h'), "glyphs/heart.svg")

# other game mechanic symbols
addIcon (font, ord('t'), "glyphs/target.svg")
addIcon (font, ord('b'), "glyphs/time_before.svg")
addIcon (font, ord('a'), "glyphs/time_after.svg")

# misc symbols
addIcon (font, ord('B'), "glyphs/book.svg")

flags = ("opentype", "dummy-dsig", "round", "apple")
font.generate ("out/NIPAJIN-Dingbats.ttf", flags=flags)
font.close()
