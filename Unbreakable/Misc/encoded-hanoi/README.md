# decoded-hanoi

## Description

Haters said that the game is broken. Prove them wrong.

Flag format: `CTF{sha256}`

## Solution

After we connect to the server using `netcat`, we are given a bunch of strings encoded in various encodings, such as `base64, base85, hexadecimal and decimal`.

The first text says:

```text
Welcome, traveler. Let's play a few games. Here's the only command I will accept:

Move the top disk of tower {x} to tower {y} ({x} and {y} are numbers from 1 to 3)

Let's begin!

```

It is clear that now we have to play the towers of hanoi game, but we can't do it by hand, so we need to write a [script](script.py) that does that for us.

> CTF{c8690500015d8e4395c0459c24c6a79ac1d828dd4190eb48b958aaf57bda83f7}
