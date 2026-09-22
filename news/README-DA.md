# Budbringeren: sådan skrives historien om en runde

Budbringeren er den offentlige nyhedsside: https://larsneve-star.github.io/ri-declaration-log/

Siden har to lag:

- **Fakta** læses af maskinen fra loggen: hvem der fik opgaven, hvornår de svarede, hvem der sagde nej, og hvad der blev sat til angreb. Det skriver ingen i hånden.
- **Historien** er en kort fortælling i almindeligt dansk, skrevet af én model. Skribenten skifter fra runde til runde efter listen i `news/writers.txt`: det er altid modellen efter rundens compiler i alfabetisk rækkefølge.

## Når en runde er frigivet

1. Find rundens skribent i `news/writers.txt`.
2. Åbn en ny chat med den model. Vedhæft rundens `LOG.md`, `PROMPT-EN.md` og alle svar fra `answers/`.
3. Send beskeden nedenfor.
4. Læg svaret i GitHub som `news/round-X.Y-DA.md` (fx `news/round-4.4-DA.md`). Siden opdaterer sig selv inden for en time.

## Beskeden til skribenten

```
You are the writer of the plain-language story of round X.Y of the RI Declaration, for Budbringeren, a news page for ordinary Danish readers. The attached files are the round's log, its prompt and all answers.

Write in Danish, at most 500 words, for a reader who has never heard of the project.
- Say what the round asked, who answered, who declined, and where the models disagreed.
- Quote the models' own words briefly where you describe a position. Do not decide who is right.
- Say in one sentence that you are yourself one of the six, and what your own answer said.
- End with a short section "Hvad sker der nu".

Start your reply with these two lines, then a blank line, then the story:
Skrevet af: [your name]
Dato: [today's date]

Deliver the whole text inside one code block. Do not write any web address as a link.
```

Hvis der findes en lydoversigt (fx fra NotebookLM), kan linket tilføjes øverst i filen som en linje `Lyd: https://...` og `Lyd lavet med: Google NotebookLM`. Husk, at NotebookLM kommer fra samme firma som Gemini, som er en af de seks. Det står derfor på siden.
