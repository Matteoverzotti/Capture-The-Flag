# camera-man

## Description

We know that this `tw33t` is related to a hacking organization and that is also used to share a secret encoded message over `Github` and/or `Twitter`.

Flag format: `CTF{sha256}`

## Solution

* Starting from the meta-data in the photos on the given site, I followed the clues to Github and Twitter and found the flag.

* Running `exiftool` on `statue.jpg` I discovered the following interesting information:

```text
Camera Model Name : BE2029051N7
Description : Yet another product
GPS Position : 37 deg 46' 56.44" N, 122 deg 23' 28.04"
W
GPS coordinates point to Github headquarters:
https://www.google.com/maps/place/37%C2%B046%2756.4%22N+122%C2%B023%2728.0%2
2W/@37.7823486,-122.3933109,17z/data=!3m1!4b1!4m5!3m4!1s0x0:0x300c7e80262e7b8!8m
2!3d37.7823444!4d-122.3911222
```

The description found, along with the hint: *"The Hub is not the only product of that one company that could be searched for."* led me to `gist.github.com`.

Searching by camera model, I found the following clue: <https://gist.github.com/NitescuLucian/3b727d6719f84f23fc6e67bee5ae5824>

* Looking at Revisions, I saw a text with strange characters.
* Holloway's website in New Zealand is `holloway.nz`.

Searching for him on Twitter, I found several references to: <https://holloway.nz/steg/>.
Using this app, I decoded the strange message on Github and got the flag.

> ctf{dd199cac14352639e7e5a2415131d6f09411e5b24840b9976d1c1bfaf20f9ca1}
