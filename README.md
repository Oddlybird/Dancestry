# Dancestry
Generates adult trolls from arbitrary parentage, loads and saves adult trolls to file.

Original version written in freebasic in late 2017.  Being adapted to Python in early 2019.


Future goals: (approximate) 

0.6.0 - Create grub from Parents + Slurry

0.5.0 - Create fully random grub from just slurry

0.3.0 - Functional default slurry

0.2.9 - functional Slurry Object

0.2.0 - Functional Donation Object

0.0.x - menu and format upgrades


=
Approximate version history:
=

V. 0.1.6c: 2019-04-18

-- began planning slurry format, created =bloodlines= and =donations= caverns(currently unused)

-- Planned menus


V. 0.1.6b: 2019-04-08

-- Enabled moving selection point off of the main menu.

-- Having trouble making button-grid navicable via btn object or function

-- Organized functions by which module they Would go in if I figure out how to do that.

V. 0.1.6a: 2019-04-08

-- Created blood color page, rearranged codes by hue, rewrote reference in ancestral cave readme.

-- Updated Ancestral Cave's Readme.txt with info about making your own trolls by hand

V. 0.1.5: 2019-04-07

-- No more crashes if files are not where expected (loads default/null troll instead)

-- Will not save over existing trolls if there is already one with that name (appends a number instead)

-- Can view contents of Ancestral Cave in-program.

-- Spent a few hours dicking around with blood code combos.  Reverted changes.


V. 0.1.4: 2019-04-07

-- Can swap between Parent and Generate Grub screens

-- Can create non-random troll on Grub screen

-- Can save Grub to file, in folder

-- Bug : Program will crash if Libbie or Lester are absent.


V. 0.1.3: 2019-04-06 - 2019-04-07

-- Keyboard interface and menu capability

-- Displayed trolls have a background color based on their blood code

-- getcaste(b) currently unused, but present.

-- Readme updated, version history added


V. 0.1.2: 2019-04-05

-- JSON and LIBTCODPY enabled

-- Converted from console program to opening its own window

-- Loads and displays two example trolls (lester pebble and libbie pickle) automatically


V. 0.1.1: 2019-04-05

-- can Save and load trolls from file.
