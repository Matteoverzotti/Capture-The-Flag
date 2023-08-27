# dacian

## Description

Who would have thought that Dacians are part of a faction in this game?

Flag format: `CTF{xx_xx_xxx_xxxx_xxxxxxx}`

## Solution

Decompressed the given file using `xz -d dacian.sav.xz`. Then used the command `grep -i "CTF" dacian.sav` to find the flag.

> Ctf{oh_so_you_know_freeciv}
