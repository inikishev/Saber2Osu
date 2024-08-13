Converts Beat Saber maps into osu! maps.

I included .bat files to launch the thing, but obviously it requires you to install python (https://www.python.org/downloads/). Also I just noticed that it requires numpy so search for python terminal in your windows search and say `pip install numpy` in that terminal. Then launch the bat file, select the beat saber map file (.zip), and it will generate osu! file (.osz) next to it and close. 

I made this so that I could use beat sage without owning beat saber.

Two versions are included.
- V2 converts timings and places notes randomly based on how their distance in time, trying to emulate actual OSU! beatmaps.
- V1 directly converts both timings and positions of the circles, which means circles can only have 9 different positions as they do in BeatSaber. Also it will straight up ignore events such as bombs and obstacles
