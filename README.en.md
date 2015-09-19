# NIP'AJIN Dingbats

[Deutsch](README.md) | [English](README.en.md).

## About

This repository contains the sources for the SIL OFL 1.1 licensed font *NIP'AJIN Dingbats*. It contains a few symbols, that are used in the pen'n'paper role playing game NIP'AJIN:

* `a` - time-after
* `b` - time-before
* `p` - book
* `f` - fist
* `h` - heart
* `s` - shield
* `t` - target

The regular font contains the symbols as bare icons. The bold fond contains the symbols in rounden squares (dice), the italic font in circles.

## Quickstart

The subdirectory `glyphs` contains a `.svg` file for each letter/symbol of the font. A Python script, `generate.py` can convert them into a TrueType font file. It requires FontForge and the FontForge-Pyhton-bindings being installed. Running

```
nipajin-dingbats$ make
```

will create the `.ttf` files into an `out` folder.
