# Log-robotten: kuratorens huskeseddel

Robotten skriver loggens rutinelinjer: tider i UTC, filnavne, hashes, frist og frigivelse. Den tilføjer kun linjer, under overskriften **Machine log** nederst i rundens LOG.md. Den ændrer eller sletter aldrig noget, og den rører aldrig et svar.

Du finder den under fanen **Actions** i repositoriet.

## Det gør robotten selv, uden at du gør noget

- **Hver gang en fil lægges ind**, skriver den filnavn, tid og SHA-256 i loggen. Et svar i `answers/` bliver logget med modellens navn.
- **Hvis en fil slettes, omdøbes eller en fastlåst fil ændres**, skriver den en ADVARSEL. Du skriver selv en kort note om hvorfor, som før.
- **Når en compiler afleverer en del** (`compile-X.Y/PART-..md`), sammenligner den straks med baseline og skriver tallene i loggen. Den fulde rapport kommer i mappen `checks`.
- **Hver time** tjekker den fristen. Når alle seks har svaret, eller fristen er udløbet, frigiver den runden og skriver, hvem der mangler.

## Det trykker du selv på

Gå til **Actions**, vælg robotten i listen til venstre, klik **Run workflow**, udfyld formularen, og klik den grønne **Run workflow**.

1. **"1. Freeze a round"**, når baseline og prompt ligger i repositoriet, og før du sender noget. Du skriver rundens nummer, baseline-filen, prompt-filen, eventuelle vedhæftninger og fristen. Robotten skriver frysningen, fristen og hvem der er compiler efter rotationslisten.
2. **"2. Log what was sent to a model"**, lige efter du har sendt til en model. Du vælger modellen på en liste. Hvis modellen fik noget andet end de andre, skriver du det i feltet *deviation*. Robotten skriver tiden.

Svarene lægger du ind som før: `round-X.Y/answers/<model>.md`. Brug navnene claude, gemini, chatgpt, deepseek, grok og meta-ai, så robotten kan genkende dem.

## Det gør du stadig selv

- Sender prompten til modellerne og henter svarene.
- Skriver noter om fejl og beslutninger under *Breaches and notes*.
- Beslutter, hvem der er compiler, hvis rotationen skal fraviges, og skriver hvorfor.

## Hvis noget går galt

- **Rødt kryds i Actions:** tag et skærmbillede, og vis det til din hjælper.
- **GitHub siger, at filen er ændret, mens du redigerer LOG.md:** robotten har skrevet en linje imens. Kopiér din tekst, genindlæs siden, og sæt den ind igen.

Robotten er skrevet af Claude, som selv er en af de seks. Koden ligger åbent i `tools/robot.py` og bør gennemgås af en udefra.
