# hidden-easy

## Description

Something is very well hidden in this image. Do you think you can find it?

Flag format: `CTF{sha256}`

## Solution

Using the `file` command we get the following

```zsh
┌──(matteoverz㉿desktop)-[hidden-easy]
└─$ file hidden.png   
hidden.png: PNG image data, 2350 x 1250, 8-bit/color RGB, non-interlaced
```

The file seems corrupted, so I used the `pngcheck` tool on it:

```zsh
┌──(matteoverz㉿desktop)-[hidden-easy]
└─$ pngcheck hidden.png      
hidden.png  private (invalid?) IDAT row-filter type (255) (warning)
hidden.png  private (invalid?) IDAT row-filter type (207) (warning)
hidden.png  invalid IDAT row-filter type (79)
hidden.png  zlib: inflate error = -5 (buffering error)
ERROR: hidden.png
```

Analyzing the bits in the image we see:

```zsh
┌──(matteoverz㉿desktop)-[hidden-easy]
└─$ xxd hidden.png | tail -n 80 | head -n 30
0001eb10: 2022 2222 2222 2222 2222 2222 22a2 a626   """"""""""""..&
0001eb20: a494 2022 2222 2222 2222 2222 2222 22a2  .. """""""""""".
0001eb30: a626 a494 2022 2222 2222 2222 2222 2222  .&.. """""""""""
0001eb40: 22a2 a626 a494 2022 2222 2222 2222 2222  "..&.. """""""""
0001eb50: 2222 22a2 a626 a494 2022 2222 2222 2222  """..&.. """""""
0001eb60: 2222 2222 22a2 a626 a494 2022 2222 2222  """""..&.. """""
0001eb70: 2222 2222 2222 22a2 a66c 617a 7926 a494  """""""..lazy&..
0001eb80: 2022 2222 2222 2222 2222 2222 22a2 a626   """"""""""""..&
0001eb90: a494 2022 2222 2222 2222 2222 2222 22a2  .. """""""""""".
0001eba0: a626 a494 2022 2222 2222 2222 2222 2222  .&.. """""""""""
0001ebb0: 22a2 a626 a494 2022 2222 2222 2222 2222  "..&.. """""""""
0001ebc0: 2222 22a2 a626 a494 2022 2222 2222 2222  """..&.. """""""
0001ebd0: 2222 2222 22a2 a626 a494 2022 2222 2222  """""..&.. """""
0001ebe0: 2222 2222 2222 22a2 a626 a494 2022 2222  """""""..&.. """
0001ebf0: 2222 2222 2222 2222 22a2 a626 a494 2022  """""""""..&.. "
0001ec00: 2222 2222 2222 2222 2222 22a2 a626 a494  """""""""""..&..
0001ec10: 2022 2222 2222 2222 2222 2222 22a2 a626   """"""""""""..&
0001ec20: a494 2022 2222 2222 2222 2222 2222 22a2  .. """""""""""".
0001ec30: a626 a494 2022 2222 2222 2222 2222 2222  .&.. """""""""""
0001ec40: 22a2 a626 a494 2022 2222 2222 2222 2222  "..&.. """""""""
0001ec50: 2222 22a2 a626 a494 2022 2264 6f67 2222  """..&.. ""dog""
0001ec60: 2222 2222 2222 2222 a2a6 26a4 9420 2222  """"""""..&.. ""
0001ec70: 2222 2222 2222 2222 2222 a2a6 26a4 9420  """"""""""..&.. 
0001ec80: 2222 2222 2222 2222 2222 2222 a2a6 26a4  """"""""""""..&.
0001ec90: 9420 2222 2222 2222 2222 2222 2222 a2a6  . """"""""""""..
0001eca0: 26a4 9420 2222 2222 2222 2222 2222 2222  &.. """"""""""""
0001ecb0: a2a6 26a4 9420 2222 2222 2222 2222 2222  ..&.. """"""""""
0001ecc0: 2222 a2a6 26a4 9420 2222 2222 2222 2222  ""..&.. """"""""
0001ecd0: 2222 2222 a2a6 26a4 9420 2222 2222 2222  """"..&.. """"""
0001ece0: 2222 2222 2222 a2a6 26a4 9420 2222 2222  """"""..&.. """"
```

The phrase "The quick brown fox jumps over the lazy dog" was written all over the place. I knew this was a commonly used sentence for fonts as it contains all the letters, so I decided to run binwalk on it:

```zsh
┌──(matteoverz㉿desktop)-[hidden-easy]
└─$ binwalk hidden.png     

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 2350 x 1250, 8-bit/color RGB, non-interlaced
```

Still nothing, so I just removed those words from the image using sed:

```zsh
┌──(matteoverz㉿desktop)-[hidden-easy]
└─$ sed -E 's/the|quick|brown|fox|jumps|over|lazy|dog//g' hidden.png > hidden2.png
```

We get a valid image and a flag at the bottom, which is not very readable. Letʼs check zsteg:

```zsh
┌──(matteoverz㉿desktop)-[hidden-easy]
└─$ zsteg hidden2.png 
imagedata           .. text: "&&&333333111"
b1,g,lsb,xy         .. text: ["z" repeated 13 times]
b1,g,msb,xy         .. text: "X^^^^^^^^^^^^^"
b1,b,lsb,xy         .. text: "OOOOOOOOOOOOOpsOOOOOOOOOOOOO1s6"
b1,bgr,lsb,xy       .. text: "========================================START========================================CTF{F5FC0A9B8D5550AE82436A19A003DD53F3C76932F501071264A98AB454A1E22D}========================================END========================================\n"
b2,r,msb,xy         .. file: VISX image file
b2,g,msb,xy         .. file: VISX image file
b2,b,msb,xy         .. file: VISX image file
b2,rgb,msb,xy       .. file: VISX image file
b2,bgr,msb,xy       .. file: VISX image file
b4,r,msb,xy         .. text: ["w" repeated 9 times]
b4,g,msb,xy         .. text: ["w" repeated 9 times]
b4,b,msb,xy         .. text: ["w" repeated 9 times]
b4,rgb,msb,xy       .. text: ["w" repeated 27 times]
b4,bgr,msb,xy       .. text: ["w" repeated 28 times]
```

Here is our flag!

> CTF{F5FC0A9B8D5550AE82436A19A003DD53F3C76932F501071264A98AB454A1E22D}
