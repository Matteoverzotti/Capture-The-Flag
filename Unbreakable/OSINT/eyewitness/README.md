# eyewitness

## Description

We have just identified an important new eyewitness in a murder case, but they can't seem to remember where they were when it happened. We just know that they were drinking a coffee and watching out the window from across the street.

They had the 3rd room on the corridor, on the 3rd floor. It is very important that we identify the EXACT location, with a very high accuracy (about 3 square meters), so our team can establish the witness' point of view of the crime scene. Failing to do so will allow the criminal to walk free.

Check the attached photo, it might contain some clues.

Flag format: `CTF{SHA256(location)}`

## Solution

We need to find a site that links to 3 and locations, so I searched the internet until I found [https://what3words.com] with the *maps location 3 m^2* query (after trying latitude and longitude, Google Plus Code etc).

* The location in the photo is *Casa Capșa*.
* Since the description said the eyewitness was across the street, that means he is either in the *Capitol Hotel* or the *Old City Gem*.
* It was next to a window, so I pulled out all the squares that appeared to be next to one of the 2 previous buildings

[All Possible Locations](locations.txt)

[Then I generated all possible flags](generate.py)

`python3 generate.py > candidate_flags.txt`

> CTF{ff66ef7b8de117716b0e8b92b0e581c756be3fb6eb1585956bb314cb8fd97894}
