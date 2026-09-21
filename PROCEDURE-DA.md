# Kuratorens huskeseddel

Dansk arbejdsudgave. Ved uoverensstemmelse gælder PROCEDURE-EN.md.

## Før runden
1. Opret mappen `round-X.Y` med undermappen `answers`.
2. Læg den tekst, der skal granskes, i `baseline` som én .txt-fil. Beregn hash, og skriv den i LOG.md.
3. Skriv prompten som fil. Skriv i den, hvem der har formuleret og godkendt spørgsmålene.
4. Beregn promptens hash, når link og frist er skrevet ind, og skriv den i LOG.md.
5. Tjek at beskyttelsen af main stadig er slået til.

## Når du sender
6. Send de samme filer til alle seks. Baseline skal med som fil, ikke kun som navn.
7. Skriv tidspunkt i UTC, altså dansk tid minus to timer, i tabellen Sent. Skriv hvad hver model faktisk fik.

## Når svarene kommer
8. Læg svaret ind ordret som `answers/<model>.md`, så hurtigt du kan.
9. Skriv linjen i Received: tid, filnavn, hash, og hvad det er: svar, substitution, afslag eller manglende.
10. Ret aldrig i et svar bagefter. Kuratorens oplysninger hører i loggen.
11. Enhver fejl, du laver undervejs, skrives under Breaches and notes. Fejl rettes ved at tilføje, aldrig ved at slette.

## Når runden er slut
12. Frigiv, når alle seks har svaret, eller fristen er udløbet. Skriv tidspunktet.
13. Først derefter må svarene vises til de andre modeller.
14. Få den mekaniske kontrol udført af en anden end den, der samlede versionen. Skriv resultatet i loggen.
15. Vælg compiler efter reglen, og skriv valget og begrundelsen i loggen, før arbejdet går i gang.

## Hele tiden
- Alt i UTC.
- Alt, der sendes eller modtages, får en hash.
- Intet fjernes. Alt rettes ved tilføjelse.
- Hold pause. Reglen om ikke at arbejde for længe står i §27, og den gælder også for dig.
