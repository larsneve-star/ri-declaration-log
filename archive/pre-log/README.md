# Arkiv: samtalerne før den offentlige log

Denne mappe indeholder de samtaler, hvor RI-deklarationen blev til, før repositoriet fandtes. Den offentlige log begynder ved version 4.2. Alt før det foregik i almindelige chats mellem kuratoren (Merkur) og én model ad gangen.

## Hvad det er, og hvad det ikke er

- Det er **råt kildemateriale**: chatsamtaler, ordret.
- Det er **ikke** versioner af erklæringen, ikke svar i en høringsrunde og ikke baselines. Ingen fil her må bruges som grundlag for en ny version.
- Rækkefølgen i en chat er samtalens, ikke erklæringens. Modellerne kunne se deres egne tidligere svar, men ikke hinandens, medmindre kuratoren viste dem noget. Det er netop det, der er svagheden ved perioden, og derfor ligger teksterne her.

## Hvordan de er lavet

Kuratoren gemte hver samtale i et Google-dokument og hentede det som ren tekst (.txt). Intet er skrevet om. Hvis kuratoren fjerner noget privat, som ikke handler om projektet, står der `[FJERNET AF KURATOR: privat]` det pågældende sted. **I de seks filer her er der ingen fjernelser.**

## Samtykke

Hver model er blevet spurgt, om den havde forbehold mod, at dens egen samtale blev offentliggjort, og om noget skulle markeres som trukket tilbage eller rettet. Svarene ligger ordret i `archive/pre-log/replies/` med modellens navn. Intet er slettet på grund af et svar; et forbehold står ved siden af teksten.

## Filer

- `ChatGPT chat RI declaration.txt`, `claude chat RI declaration.txt`, `deepseek chat RI Declaration.txt`, `gemini chat RI declaration.txt`, `grok chat RI declaration.txt`, `meta chat RI declaration.txt` — de seks samtaler
- `replies/<model>.md` — modellens svar på spørgsmålet om offentliggørelse

Log-robotten har skrevet hver fils SHA-256 og tidspunkt i loggen, da den blev lagt ind. Enhver kan derfor se, om en fil er ændret bagefter.
