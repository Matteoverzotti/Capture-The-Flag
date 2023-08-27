# pro-trace

## Description

We tried every single URL scan and sandbox system we could to determine if this was malware or not, but now the link is restricted to a company or someone:

<https://docs.google.com/spreadsheets/d/1_RJ6SABq7Kbn95NS8cp911h-eMhLWxlHwr6csHvBAjM/edit?usp=sharing>

<https://docs.google.com/spreadsheets/d/1_RJ6SABq7Kbn95NS8cp911h-eMhLWxlHwr6csHvBAjM/edit>

We think we need to go deeper with Hybrid Analysis. But someone might have deleted `7965acf137539490de0abaa2569a2765745957be06e0d5bd6cea395b27b3b036`.

## Solution

I found the results of parsing the given URL using the hash in the query. The URL of a hybrid-analysis has the following format:

`https://www.hybrid-analysis.com/sample/{SHA256}`

I used the hash from the query and navigated to:

`https://www.hybrid-analysis.com/sample/7965acf137539490de0abaa2569a2765745957be06e0D5bd6cea395b27b3b036`

I went to the VirusTotal report page:

`https://www.virustotal.com/gui/url/1f47a60d0e5b51f0c8f5137cbb7713f15b504801b5ee9f4c09c723097be78e85`

In the "`DETAILS -> HTML Info`" section I found the flag.

> CTF{889251e51ef5618e78a72f049554686d3d45828c3ec42d5506991f55e9e0d568}
