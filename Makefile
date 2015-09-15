# (c) 2009-2015 by Markus Leupold-Löwenthal
# This file is released under CC BY-SA 4.0.

default: font

all: font

setup:
	mkdir -p out

font: setup
	python generate.py
	cp OFL.txt out/OFL.txt

clean:
	rm -rf out/*
