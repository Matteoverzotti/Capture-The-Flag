# social-agency

## Description

Dear Agent, as your first task within the Agency, find the last known location of `tecgirwilliam@gmail.com` also called **Tecgir William** without attempting to hack or brute force within any account. All information is of course public. After that maybe we can have that call over Google Hangouts/Meets (or both) about how to clean the cafeteria.

Note: The flag of this code must be generated as such: `CTF{sha256sum('Google Plus Code')}`

## Solution

* In the problem statement, we get the e-mail address and the name of the suspect.
* There is also something related to Google Hangouts.
* I've seen problems like this before, so I simply used `GHunt` to solve all my problems.
* I downloaded GHunt from GitHub, set the cookies and then ran `python3 ghunt.py email tecgirwilliam@gmail.com`.

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

* We see he has a review posted on his Gmail account.
* After visiting the Google Maps link, we see that he has left a 5-star review for Lotrisor Waterfall.
* Clicking on the **PLACE DETAILS** button, we find the Google Plus code of the place (`872J+WX Brezoi`).
* We take it and perform the following steps: `echo -n "872J+WX Brezoi" | sha256sum` .

Having done this, we get a string `sha256sum` which we wrap in `CTF{}`, and this is our flag.

> CTF{e0c34f6ffe1dcc87c67a4fa218b1050da7bb9b9d01871ea7afcb49e55b81257d}
