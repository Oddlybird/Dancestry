# Dancestry
Generates adult trolls from arbitrary parentage, loads and saves adult trolls to file.

Original version written in freebasic in late 2017.  Being adapted to Python in early 2019.  The next version is being transferred to java in 2021.

Goal: 0.4.0, major graphical, UI, or back-end update.  The last significant UI -AND- graphics overhauls before 1.0 should be done by 0.5.0.

=
Approximate version history: (x = nonfunctional)
=

V: 0.3.4x: 

-- Enabled mouse movement, converted back from nested dict to class-based

V. 0.3.3x: 

-- Made a pass through genome.py, graphics.py, traits.py (did a bad job), and main.py

-- Program now loads some screens but not others

-- severe troubleshooting needed on trollmakepage, and traits.py.  Not in that order.

V. 0.3.2x: 

-- Converted hornobj, hornset, seagene, and mouth to nested dictionary form.

-- Slurry.py, formattingbs.py names.py, colorgarbage.py, should be done.

-- left:  genome.py, graphics.py, traits.py, main.py.

V. 0.3.1x: 2019-06-08

-- Created Troll Class.  Accidentally broke savefiles.

-- Basic stats included in traits.py; not JSON compatible.  Save .troll files temporarily broken; screenshots still working fine.  Core and secret stats present.  Some bugs left; stat maximums often incorrect.

-- Simple Aspect-calculator included.  Currently bland / not well integrated. Consider adding Aspect icons?

-- Updated stats defaults from if-statement forest to slurry-defined.

-- Began planning splitting seadweller traits into graphics, starting with earfins and eyegills.

-- Began planning combination of all genestrands into one splittable object, so cross-strand interactions are easier (eg: seadweller doubled-teeth, eyelids)

-- Updated Feature Project with subgoals.  Aim to have 0.4.0 be either a significant graphics/display/interface update (full graphical support for all currently statted genestrands + groundwork for later additions, or a significant back-end update for ease-of-use.  More genestrands being added along the way is fine, but only counts for abcd level updates.

-- Created secondary copy of Genome file, containing only resource functions (genecombine, printing to screen, basic graphics, genestrand template) and no setting-specific data.  IE, a blank copy of the engine.  Use later for non-fanwork programs along these lines, and for final revision of this project once it's time for the Complete Rewrite / Redesign.

V. 0.3.0: 2019-06-04

-- Still need to implement horn mount location

-- Bug-fixing

-- Added closed mouth graphic

-- began stat planning

-- hornlengths of secondary horns max out at 1 less than next most important horn

V. 0.2.9b: 2019-06-04

-- Replaced horndescribe with graphical icons.

-- Horn mount location is all that's left to do.

V. 0.2.9: 2019-05-31

-- Upgraded genecombine to include probability weighting

-- added slurry spectrum entries for hair, skin, build, and powers.  Currently vacuous.

-- added 9 mutant horn gene entries and premade trolls that have them

-- enabled all horn control genes, including odd numbers / placements of them.  Description function is still buggy.  Should be replaced with graphical icons.  Goal for 0.3.0 :  graphical icons.

V. 0.2.6: 2019-05-26

-- Writer's block sucks

-- Entire engine transferred from libtcodpy to pygame

-- Teef graphics enabled

-- Save troll to .png enabled

V. 0.2.5a: 2019-05-12

-- added screenshot button to main menu

-- began investigating teef graphics

-- now using save format 9

V. 0.2.5: 2019-05-11

-- Horns now in genestrand format and functioning; multi-horn averager complete.

-- horns by caste defined in slurry (could use review)

-- standardized premade trolls to use more constants from slurry while genetics being designed

-- basic testing of gene results:  as long as you're crossing two trolls of different castes, everything looks great.  Horns, teeth, and seadweller genes have good rates of auto-mutation and inheritance.

-- ready to add new horn metagenes

-- ready to add mouth.describe and new horns.describe

-- Note to self : Move seadweller double-tooth gene to mouth object, remove from seadweller

-- Note to self : Update documentation.

V. 0.2.4: 2019-05-08

-- TEEF, teefblender, teef from slurry, teef averager.

-- Teef still undescribed, undergoing basic testing.

V. 0.2.3d: 2019-05-05

-- split "deets" into deets (functions / utility), and genome (classes for trollobj, genes, etc).

-- added list of genestrand ideas to genome file

-- fleshed out eye, mouth, and tooth objects / genes; still unfinished and nonfunctional.

V. 0.2.3c: 2019-05-05

-- There are now five epigenetic flags controlling whether seadweller traits express or not.  S0 (ears, fins, finger/toe webbing), S1 (gills and waterbreathing), S2 (swim bladders), S3 (bioluminance, teeth genes), and S4 (nictating eyelids, body fins)

V. 0.2.3b: 2019-05-04

-- seadesc's code is prettier, and more functional

-- did planning stage for eye and teeth genes

-- made seadesc describe differences from land dweller / seadweller defaults, not caste norms

V. 0.2.3a: 2019-05-03

-- seadesc is prettier.

V. 0.2.3: 2019-05-03

-- human-readable heightstr, seadesc, horndesc, etc added to troll object.

-- functions to produce said descriptions moved out of horn/seagene objects to be callable from elsewhere

-- new file "formattingbs" added, contains a wordwrap function.

-- slurry contains default genes for land dwellers, seadwellers, and Crazy Mutant Shit

-- slurry contains a spectrum of land vs seadweller

-- Added new default troll, horrible recessive mutant

-- updated display function

-- left a HUGE MESS all throughout the code.

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
