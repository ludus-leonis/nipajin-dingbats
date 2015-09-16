#!/usr/bin/python
# -*- coding: utf-8 -*-
# simple .svg to .ttf icon font converter, (c) 2015 Markus Leupold-Löwenthal

import fontforge, psMat

def addIcon( font, glyph, svgFileName ):
    "add a svg as icon glyph"
    glyph = font.createChar(glyph)
    glyph.importOutlines(svgFileName)
    glyph.correctDirection()
    glyph.left_side_bearing = glyph.right_side_bearing = 60
    return;

def addDie( font, glyph, svgFileName ):
    "add a svg as die glyph (with a box)"
    glyph = font.createChar(glyph)
    glyph.importOutlines("glyphs/_box.svg")
    glyph.importOutlines(svgFileName)
    glyph.correctDirection()
    glyph.left_side_bearing = glyph.right_side_bearing = 60
    return;

# start with a new font
font = fontforge.font()

# add some meta-data
font.fontname = "NIPAJIN-Dingbats"
font.fullname = "NIP'AJIN Dingbats"
font.familyname = "NIP'AJIN Dingbats"
font.version = "v1.0.1"
font.copyright = "Copyright (c) 2015, LUDUS LEONIS / Markus Leupold-Loewenthal (http://ludus-leonis.com/),\nwith Reserved Font Name \"NIP'AJIN Dingbats\".\n\nThis Font Software is licensed under the SIL Open Font License, Version 1.1.\nThis license is available with a FAQ at: http://scripts.sil.org/OFL"

# add dice symbols
addDie (font, ord('f'), "glyphs/fist.svg")
addDie (font, ord('s'), "glyphs/shield.svg")
addDie (font, ord('h'), "glyphs/heart.svg")

# add other game mechanic symbols
addIcon (font, ord('t'), "glyphs/target.svg")
addIcon (font, ord('b'), "glyphs/time_before.svg")
addIcon (font, ord('a'), "glyphs/time_after.svg")

# add misc symbols
addIcon (font, ord('B'), "glyphs/book.svg")

# export to file
flags = ("opentype", "dummy-dsig", "round", "apple")
font.generate ("out/NIPAJIN-Dingbats.ttf", flags=flags)
font.close()
