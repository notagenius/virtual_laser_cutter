# virtual laser cutter

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

tidy .svg is expected for decent result, which means 
- no redundant path, no redundant nodes
- well grouped, one piece one group
- path needs to be filled for proper mesh, e.g.

![svg](/doc/sample_Box_fill.svg)

#### Additional resource:

new to inkscape? wanna work with laser cutter?
[this medium post](https://medium.com/@TSwarper/a-dude-who-thinks-from-the-prespective-of-inkscape-f0fc93917ef1) is my note

#### Utility:

3 parameters need to be set in the script:
- filepath (the .svg file), you can run as many times as you want in one session, every run you wanna update the filepath and move the done model out of the center to avoid overlapping
- texture path. a decent wooden image texture is provided (from [poliigon](https://www.poliigon.com/))
- thickness, default value 0.004 which is close to 4mm with the scale of 10 in 3 axises

#### Todo:

- make it as an extionsion with menu and panel
- make engraving
- enrich the texture with normal for realism
Help is welcome

#### Blender vision:

Created with blender 2.79 under Linux

#### Author

ThatWolfieFeeling
01/June/2018
