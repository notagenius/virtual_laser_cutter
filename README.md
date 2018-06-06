# virtual_laser_cutter

#### The Use:

Generating 3d model of pieces from .svg file in 3d software (Blender)

working as a virtual laser cutter

#### Demo:

from .svg

![svg](/doc/sample_Box_no_fill.svg)

the script will generate

![top_view](/doc/top_view_render.png)
![side_view](/doc/side_view_render.png)

further virtual assembly can be applied

![assembly](/doc/assembly_render.png)

#### Watch out:

tidy .svg is expected for best result, which means 
- no redundant path, no redundant nodes
- well grouped, one piece one group
- path needs to be filled for proper mesh, e.g.

![svg](/doc/sample_Box_fill.svg)

#### Additional resource:

if you are new to inkscape, and wanna work with laser cutter
[this medium post](https://medium.com/@TSwarper/a-dude-who-thinks-from-the-prespective-of-inkscape-f0fc93917ef1) is my note

#### Utility:

In script 3 parameters need to be set:
- filepath (the .svg file), you can run as many times as you want in one session, every run you wanna update the filepath and move the done model out of the center to avoid overlapping
- texture path. A decent wooden image is provided (I got it from [poliigon](https://www.poliigon.com/) recommend it
- thickness, default is 0.004 which is close to 4mm in real world

and all of the model are scaled 10 times in 3 dimensions

#### ToDo:

Help is welcome
- make it as an extionsion with menu and panel
- make engraving
- enrich the texture with normal for realism

#### Blender vision:

Created with blender 2.79 under Linux

#### Author

ThatWolfieFeeling
