# the_island
Not yet very playable ASCII-based adventure game.

## Gameplay
Run the game:
```
[the_island py](./the_island.py)
```

Run the tests:
```
coverage run --source '.' -m unittest -v
coverage report -m
```

Screenshot of our hero(es) waking amidst the dense woods, slowly approaching
the mountains in the north. What dwells there?
```
--------------------------------------------------------------------------------
|                                                                              |
|                                .....           ......                        |
|                               ......      ...............                    |
|                              ......      .................           .....   |
|                    .........................###########......................|
|             ..................###..........##############...........####.....|
|         .............########################################################|
|    .............#############################################################|
|   ..........#################################################################|
|   ........#####################^^^^^^^#######################################|
|   .......##################^^^^^^^^^^^^^#####################################|
|    .....###############^^^^^^^^^^^^##^^^^####################################|
|     ...#############^^^^^^^^^^^########^^^^^^^^^#############################|
|      .############^^^^^^^^^##########@###^^^^^^^^^^^^^#######################|
|      ..########^^^^^^#####################^^^^^^^^^^^^^^^####################|
|     ..########^^^^^##########################################################|
|    ...#######################################################################|
|    ..########################################################################|
|   ..#########################################################################|
|    ...#######################################################################|
|    ......####################################################################|
|~ ~......#####################################################################|
--------------------------------------------------------------------------------
```

## Game description
The game is heavily inspired by rogue and the CBM64 version of Phantasie II.
The player reqruits a band of adventures and goes of adventuring on an island.

### Details
- Turn-based game style
- hjkl for navigation
- Fixed ASCII map for the Island, random generated dungeons/ruins/dimensions
- Stationary as well as moving monsters
- Conecpt of ambush
- No colors, field of view or concept of food or ageing


### What is Implemented
- [X] Basic game objects (tiles, monsters etc)
- [X] Create and display simple map
- [X] Make party move around
- [ ] Character generation
- [ ] Hook up and equip party of adventures
- [ ] Monster generation and random placement
- [ ] Fight system
- [ ] ...with spells
- [ ] Money system
