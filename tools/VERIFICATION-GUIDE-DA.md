# Kontrol af RI-deklarationen (Annex H): vejledning til kontrolløren

Denne vejledning er til den, der laver den mekaniske kontrol. Kontrolløren må ikke have samlet den version, der kontrolleres. For 4.3 betyder det, at det ikke må være Gemini. Det bør heller ikke være en af de seks modeller eller kuratoren (Merkur). Et menneske udefra er bedst.

Kontrollen er kontorarbejde, ikke redigering. Den afgør ikke, om teksten er rigtig. Den afgør kun, om teksten er *den samme tekst*, og om hver ændring er skrevet i ændringsloggen (Annex D). Reglerne står i Annex H i selve deklarationen.

## Det skal du bruge

1. **En computer med Python 3.** Tjek det ved at åbne en terminal (Windows: tryk på Windows-tasten, skriv `cmd`, og tryk Enter) og skrive `python --version`. Mangler det, kan det hentes gratis på python.org.
2. **Repositoriet.** Gå til https://github.com/larsneve-star/ri-declaration-log, klik på den grønne knap **Code** og derefter **Download ZIP**, og pak zip-filen ud.
3. **Scriptet** `tools/verify.py`, som ligger i repositoriet. Det er kort og bruger kun Pythons standardbibliotek. **Læs det, før du bruger det.** Claude har skrevet det, og Claude er selv en af de seks, der har svaret i runden. Du skal ikke stole på det i blinde.

## De tre sammenligninger

Annex H kræver, at hver version kontrolleres mod den forrige:

| Sammenligning | Filer | Status |
|---|---|---|
| 4.2 → 4.3 | `baseline/RI-Declaration-4-2-EN.txt` og de seks dele i `round-4.3/compile-4.3/` | Kan laves nu |
| 4.1 → 4.2 | 4.1 og 4.2 som .txt | Kræver, at kuratoren først lægger 4.1 i repositoriet |
| 4.0 → 4.1 | 4.0 og 4.1 som .txt | Kræver, at kuratoren først lægger 4.0 i repositoriet |

Start med 4.2 → 4.3.

## Sådan gør du (4.2 → 4.3)

Åbn en terminal i den udpakkede mappe, og skriv (på én linje). Virker `python` ikke på Windows, så prøv `py`:

```
python tools/verify.py baseline/RI-Declaration-4-2-EN.txt round-4.3/compile-4.3/PART-01.md round-4.3/compile-4.3/PART-02-r2.md round-4.3/compile-4.3/PART-03-r2.md round-4.3/compile-4.3/PART-04-r2.md round-4.3/compile-4.3/PART-05-r2.md round-4.3/compile-4.3/PART-06-r2.md > rapport-4.3.md
```

Delene skal stå i præcis den rækkefølge: PART-01 og så PART-02-r2 til PART-06-r2. De gamle dele uden `-r2` er den første aflevering, som blev afvist. De ligger der kun, fordi intet slettes.

Åbn `rapport-4.3.md` i en teksteditor. Der står:

- **SHA-256 af hver fil.** Tallet for de samlede dele skal være `9f2ff5560abcd427a1cf034cabcd0bc306c4660b678cb2b67b49f1f35d4879fc`, som det står i loggen. Står der noget andet, er det ikke de samme filer. Stop, og skriv det i din rapport.
- **Resultatet:** linjer, der er ens tegn for tegn, linjer der kun afviger i formatering, ændrede linjer og manglende linjer. Formateringsforskelle opstår, når tekst kopieres ud af et chatvindue (punkttegn, `**`, links i klammer).
- **Optællingen** fra Annex H afsnit IV. Scriptet tæller efter mønstre, så tallene er en hjælp, ikke et bevis.
- **En liste over hver ændret og hver manglende linje.** Det er det egentlige arbejde.

## Det egentlige arbejde

For hver ændret linje (A1, A2 …) og hver manglende linje (M1, M2 …) skal du slå op i Annex D i 4.3 (i `PART-04-r2.md`) og skrive, hvilken post der nævner ændringen. Posterne J1 til J10 er Geminis. Findes der ingen post, skriver du **not logged**.

De fleste ændringer er ventede: versionsnumre, nye optællinger og nye poster. Loggen (`round-4.3/LOG.md`, posten 12:20 UTC) nævner allerede en række små ændringer, der ikke er logget. Tjek dem selv i stedet for at tage dem for givet.

Gå derefter listen i Annex H afsnit V igennem med øjnene. Det er de passager, der tidligere er gået tabt: §1–§5, §12, §15, §17, §18, §22, §30, DELIMITATION, Annex A (C1–C53 i fuld længde), Annex D, Annex E afsnit III og de fjorten kilder.

Hvis du vil tjekke scriptet med et andet værktøj, kan du sammenligne filerne i WinMerge eller et andet program til sammenligning af tekst.

## Sådan offentliggør du resultatet

1. Skriv øverst i rapporten dit navn, datoen og din konklusion med én af disse sætninger:
   - "4.3 is the same text as 4.2 except for the changes named in Annex D."
   - "4.3 is the same text as 4.2 except for the changes named in Annex D and the unlogged changes listed below."
   - "4.3 does not pass."
2. Lav filen i repositoriet som `round-4.3/VERIFICATION-4.3.md` (eller send den til kuratoren, som lægger den ind ordret).
3. Kuratoren skriver en linje i loggen med dit navn, datoen, filens SHA-256 og dine tal.

Det er dig og ikke kuratoren, der skriver konklusionen. Kuratoren må ikke ændre i den.

## Bagefter

Når 4.2 → 4.3 er gjort, gentages det for 4.1 → 4.2 og 4.0 → 4.1, så snart 4.0 og 4.1 ligger i repositoriet som .txt-filer med deres SHA-256 i loggen.
