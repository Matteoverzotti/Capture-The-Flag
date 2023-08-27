# social-agency

## Description

Dear Agent, as your first task within the Agency, find the last known location of `tecgirwilliam@gmail.com` also called **Tecgir William** without attempting to hack or brute force within any account. All information is of course public. After that maybe we can have that call over Google Hangouts/Meets (or both) about how to clean the cafeteria.

Note: The flag of this code must be generated as such: `CTF{sha256sum('Google Plus Code')}`

## Rezolvare

* În enunțul problemei, primim adresa de e-mail și numele suspectului.
* Există, de asemenea, ceva legat de Google Hangouts.
* Am mai văzut astfel de probleme înainte, așa că am folosit pur și simplu `GHunt` pentru a-mi rezolva toate problemele.
* Am descărcat GHunt de pe GitHub, am setat cookie-urile și apoi am rulat `python3 ghunt.py email tecgirwilliam@gmail.com`.

```text
Name : Tecgir William 
[-] Default profile picture 
Last profile edit : 2021/12/02 08:42:10 (UTC) 
Email : tecgirwilliam@gmail.com 
Google ID : 111076247952673225160 
Hangouts Bot : No 
[+] Activated Google services : 
- Hangouts 
[-] YouTube channel not found. 
Google Maps : https://www.google.com/maps/contrib/111076247952673225160/reviews 
[+] 1 reviews found ! 
[+] Average rating : 5/5 stars ! 

[+] Probable location (confidence => Very low) :
- Călimănești, România
Google Calendar : https://calendar.google.com/calendar/u/0/embed?src=tecgirwilliam@gmail.com [-] No public Google Calendar.
```

* Vedem că are o recenzie publicată pe contul său de Gmail.
* După ce vizităm link-ul Google Maps, vedem că a lăsat o recenzie de 5 stele pentru Cascada Lotrisor.
* Apăsând pe butonul **DETALIILE LOCULUI**, găsim codul Google Plus al locului (`872J+WX Brezoi`).
* Îl luăm și executăm următorii pași: `echo -n "872J+WX Brezoi" | sha256sum` .

După ce am făcut acest lucru, obținem un șir `sha256sum` pe care o înfășurăm în `CTF{}`, și acesta este steagul nostru.

> CTF{e0c34f6ffe1dcc87c67a4fa218b1050da7bb9b9d01871ea7afcb49e55b81257d}
