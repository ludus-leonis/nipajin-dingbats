#!/usr/bin/python
# -*- coding: utf-8 -*-
# simple .svg to .ttf icon font converter, (c) 2015 Markus Leupold-Löwenthal

import fontforge, psMat

fontname = "NIPAJIN-Dingbats"
fullname = "NIP'AJIN Dingbats"
familyname = "NIP'AJIN Dingbats"
version = "v1.0.1"
copyright = "Copyright (c) 2015, LUDUS LEONIS / Markus Leupold-Loewenthal (http://ludus-leonis.com/),\nwith Reserved Font Name \"NIP'AJIN Dingbats\".\n\nThis Font Software is licensed under the SIL Open Font License, Version 1.1.\nThis license is available with a FAQ at: http://scripts.sil.org/OFL"

def getGlyphWidth(glyph):
    "determine width of a given glyph"
    box = glyph.boundingBox()
    return box[2] - box[0]

def getGlyphHeight(glyph):
    "determine height of a given glyph"
    box = glyph.boundingBox()
    return box[3] - box[1]

def addIcon( font, glyph, svgFileName ):
    "add a svg as icon glyph"
    glyph = font.createChar(glyph)
    glyph.importOutlines(svgFileName)
    glyph.correctDirection()
    return;

def addDie( font, glyph, svgFileName, yOffset = 0 ):
    "add a svg as die glyph (with a box)"
    scale = 0.75
    glyph = font.createChar(glyph)

    # get and store true width for later, as it will get distorted
    glyph.importOutlines("glyphs/_box.svg")
    width = glyph.width
    glyph.clear()

    # put icon in a die/box
    glyph.importOutlines(svgFileName)
    glyph.transform(psMat.scale(scale))
    glyph.transform(psMat.translate(1000 * (1 - scale) / 2, yOffset + 1000 * (1 - scale) / 2 - 200 * (1 - scale)))
    glyph.importOutlines("glyphs/_box.svg")
    glyph.correctDirection()

    glyph.width = width
    return;

def addCircle( font, glyph, svgFileName, yOffset = 0 ):
    "add a svg as die glyph (with a box)"
    scale = 0.75
    glyph = font.createChar(glyph)

    # get and store true width for later, as it will get distorted
    glyph.importOutlines("glyphs/_circle.svg")
    width = glyph.width
    glyph.clear()

    # put icon in a die/box
    glyph.importOutlines(svgFileName)
    glyph.transform(psMat.scale(scale))
    glyph.transform(psMat.translate(1000 * (1 - scale) / 2, yOffset + 1000 * (1 - scale) / 2 - 200 * (1 - scale)))
    glyph.importOutlines("glyphs/_circle.svg")
    glyph.correctDirection()

    glyph.width = width
    return;

# start with a new font
regular = fontforge.font()  # shape only
bold    = fontforge.font()  # box shapes
italic  = fontforge.font()  # circle shapes

# add some meta-data
regular.fontname = fontname + "-Regular"
regular.fullname = fullname
regular.familyname = familyname
regular.version = version
regular.copyright = copyright
bold.fontname = fontname + "-Bold"
bold.fullname = fullname + " Bold"
bold.familyname = familyname
bold.version = version
bold.copyright = copyright
bold.fontname = fontname + "-Italic"
bold.fullname = fullname + " Italic"
bold.familyname = familyname
bold.version = version
bold.copyright = copyright

# add symbols
addIcon   (regular, ord('f'), "glyphs/fist.svg")
addDie    (bold,    ord('f'), "glyphs/fist.svg")
addCircle (italic,  ord('f'), "glyphs/fist.svg")

addIcon   (regular, ord('s'), "glyphs/shield.svg")
addDie    (bold,    ord('s'), "glyphs/shield.svg")
addCircle (italic,  ord('s'), "glyphs/shield.svg")

addIcon   (regular, ord('h'), "glyphs/heart.svg")
addDie    (bold,    ord('h'), "glyphs/heart.svg")
addCircle (italic,  ord('h'), "glyphs/heart.svg", -20)

addIcon   (regular, ord('p'), "glyphs/book.svg")
addDie    (bold,    ord('p'), "glyphs/book.svg")
addCircle (italic,  ord('p'), "glyphs/book.svg")

addIcon   (regular, ord('t'), "glyphs/target.svg")
addDie    (bold,    ord('t'), "glyphs/target.svg")
addCircle (italic,  ord('t'), "glyphs/target.svg")

# add other game mechanic symbols
addIcon (regular, ord('b'), "glyphs/time_before.svg")
addIcon (bold,    ord('b'), "glyphs/time_before.svg")
addIcon (italic,  ord('b'), "glyphs/time_before.svg")

addIcon (regular, ord('a'), "glyphs/time_after.svg")
addIcon (bold,    ord('a'), "glyphs/time_after.svg")
addIcon (italic,  ord('a'), "glyphs/time_after.svg")

# export to files
flags = ("opentype", "dummy-dsig", "round", "apple")

regular.generate ("out/NIPAJIN-Dingbats.ttf", flags=flags)
regular.close()

bold.generate ("out/NIPAJIN-Dingbats-Bold.ttf", flags=flags)
bold.close()

italic.generate ("out/NIPAJIN-Dingbats-Italic.ttf", flags=flags)
italic.close()
