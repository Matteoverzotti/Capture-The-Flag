# eyewitness

## Description

We have just identified an important new eyewitness in a murder case, but they can't seem to remember where they were when it happened. We just know that they were drinking a coffee and watching out the window from across the street.

They had the 3rd room on the corridor, on the 3rd floor. It is very important that we identify the EXACT location, with a very high accuracy (about 3 square meters), so our team can establish the witness' point of view of the crime scene. Failing to do so will allow the criminal to walk free.

Check the attached photo, it might contain some clues.

Flag format: `CTF{SHA256(location)}`

## Rezolvare

Trebuie să găsim un site care să aibă legătură cu 3 și locații, așa că am căutat pe internet până am găsit [https://what3words.com] cu interogarea maps location 3 (după ce am încercat latitudine și longitudine, Google Plus Code etc.).

* Locația din fotografie este *Casa Capșa*.
* Din moment ce în descriere se spunea că martorul ocular se afla vizavi, asta înseamnă că se află fie în *Hotel Capitol*, fie în *Old City Gem*.
* Era lângă o fereastră, așa că am extras toate pătrățelele care păreau a fi lângă una din cele 2 clădiri anterioare

[Toate Locatiile Posibile](locations.txt)

[Apoi am generat toate steagurile posibile](generate.py)

`python3 generate.py > candidate_flags.txt`

> CTF{ff66ef7b8de117716b0e8b92b0e581c756be3fb6eb1585956bb314cb8fd97894}
