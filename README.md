# Dancestry
Generates adult trolls from arbitrary parentage, loads and saves adult trolls to file.

Original version written in freebasic in late 2017.  Being adapted to Python in early 2019.

=
Approximate version history:
=

V. 0.2.2b: 2019-05-01

-- Height exists, in inches, and can be influenced by both child caste's average height and parents' relative heights.

-- Basic sea genes / phenotype system in progress

V. 0.2.2a: 2019-05-01

-- Make From Slurry will only produce trolls whose blood codes are on the current spectrum selected in blood page.  Make From Parents is unchanged.  Current spectrums are full (350some distinct gradient colors), mini (12 colors), random (randomly generate 360 colors), rust, greens, blues, and purples.

V. 0.2.2: 2019-05-01

-- Can load currently-generated troll into slot 1 or 2, and produce descendants thereof

-- Cannot yet load troll from file

-- Cosmetic Tweaks

-- Save format #6

-- Create Troll From Slurry can be fed specific blood colors and will produce a troll of that caste

-- Gender can be biased by blood color; trolls near jade and tyrian are more likely to be feminine

-- Hornblender can now average length and curliness

V. 0.2.1: 2019-04-29

-- Removed donation system

-- enabled grub from slurry and grub from parents

-- enabled grub name, blood code, gender, horns

-- streamlined horn description code

-- created random bloodcode and horn generators in slurry.py

-- adjusted program to use tuples rather than tcod.Color objects, where possible

-- added "hard-coded" trolls to slurry document

V. 0.2.0a: 2019-04-29

-- Fiddled with color definitions using colorsys.py (downloaded)

-- save file formatting changed, now using version 5

-- enabled blood system based on chibs suggestion; documentation not updated yet

V. 0.2.0: 2019-04-28

-- Converted project to pycharm IDE

-- Split project into multiple files (main/interface, trolldeets, name)

-- began converting project from troll/donation/slurry model to troll/slurry model

-- added basic name generator (needs tuning)

-- added basic horn blender (needs tuning)

-- moved some buttons

V. 0.1.8: 2019-04-21

-- expanded display dramatically

-- added horn description function

-- reformatted troll and donation displays to fit new window size

-- added castenumber function, adjusted blood page display, adjusted caste order

V. 0.1.7b: 2019-04-21

-- Load troll system worked on, not yet functional

-- arrow key navigation worked on, left and right keys not yet functional in submenus.

-- Donations now include and display horn data

-- Working on horn describer.

V. 0.1.7:  2019-04-20

-- Able to select items on left menus in donation page and loading page

-- Code sorted, re-organized, generalized.  Menus are more scaleable.

-- Donation page largely functional; ready for donation format.

-- Unable to load trolls from file, but it'll be quick to add.

V. 0.1.6d: 2019-04-20

-- Submenus enabled, most displays moved down slightly to make room.

-- Basic donation format begun, display page created.

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
