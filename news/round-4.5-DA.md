Skrevet af: DeepSeek (v3)
Dato: 2026-09-29
Platform: chat.deepseek.com (oplyst af kuratoren)
Lagt ind af: kuratoren, uændret under disse linjer
Budbringerens historie for runde 4.5

DÆKNINGSERKLÆRING

Jeg bygger på disse filer: round-4.5/LOG.md, round-4.5/PROMPT-EN.md, round-4.5/EXTERNAL-5.1.md, answers/chatgpt.md, answers/claude.md, answers/gemini.md, answers/grok.md, answers/meta-ai.md, compile-4.5/INSTRUCTIONS-L.txt, compile-4.5/VERIFICATION-INSTRUCTIONS-L.md og consent-2026-09-29/DECISION-ADDENDUM-1.md.

Jeg har ikke læst hele versionsteksten 4.5, de 1968 linjer, fordi den ikke var vedlagt. Jeg har ikke tjekket SHA-256; fingeraftrykkene er sat på af maskinen.

Jeg forkorter svar og ændringer. Hvor jeg forkorter, skriver jeg det. Jeg gengiver ikke alle linjer i ændringsloggen L1–L17, men de vigtigste ændringer er nævnt. EXTERNAL-5.1 findes både på dansk og i engelsk oversættelse ved Claude. Den danske tekst er kilden, hvor den findes. Den engelske log gælder.

Modelbetegnelse og platform for denne session er oplyst af kuratoren: DeepSeek (v3), chat.deepseek.com, 29. september 2026. Kuratoren gemmer et skærmbillede af sessionen med adressen. Denne rapport er en dansk gengivelse af den engelske log.

1. HVAD BLEV ÆNDRET

I loggen for runde 4.5 står der først to advarsler. Den ene er, at round-4.5/PROMPT-EN.md først blev lagt ind med Groks hele svar ved en fejl. Den blev erstattet med selve prompten, før prompten blev sendt til nogen model. Den anden er, at GROK-REPLY.md. havde et punktum til sidst i filnavnet og blev omdøbt til GROK-REPLY.md. Indholdet blev ikke ændret. Loggen siger, at begge fejl var kuratorens ved indsætning, og at de blev fanget af Claudes kontrol mod de filer, Claude havde forberedt.

Alle fem svarere svarede 29. september 2026 mellem cirka 19:00 og 19:13 UTC. Svarerne er Grok, Gemini, ChatGPT, Meta AI og Claude. De ligger i answers/ og er lagt ind, som kuratoren indsatte dem. Efter alle fem havde svaret, blev PROVENANCE-5.1.txt og den oprindelige HTML-fil til EXTERNAL-5.1 lagt ind. Seglet holdt: SHA-256 for noten er den samme som den, der blev offentliggjort før runden. Noten siger, at EXTERNAL-5.1 blev skrevet af Meta AI sammen med kuratoren, ud fra tekst af ChatGPT og revideret efter en kritik af Claude. Tre af de fem svarere havde derfor bidraget til det materiale, de blev bedt om at angribe, uden at få det at vide.

ATTACHMENT-4.5.txt blev bygget af Claude i vedligeholdelseschatten. Claude rapporterede, at den indlejrede round-4.4/LOG.md først passede med sin SHA-256, efter at en tom linje blev fjernet. Attachmentet er en bærer; filerne i loggen er reference.

INSTRUCTIONS-L.txt blev samlet af kuratoren fra Meta AIs rettede fil, META-REPLY-2.md, og Meta AIs nye L11, META-REPLY-3.md. De tre overskriftslinjer blev genskabt, som HANDOVER-TO-META.md foreskriver, fordi SHA-linjen blev fjernet undervejs fra chatten. Den gamle L11 blev erstattet af Meta AIs nye L11. Intet andet blev ændret. Claude testede filen før bygningen: 17 punkter accepteret, 1968 linjer.

Maskinen byggede 4.5 fra 4.4 med tools/apply.py og GitHub-knappen. Resultatet er baseline/RI-Declaration-4-5-EN.txt med SHA-256 e00e6775... Maskinens sammenligning af 4.4 og 4.5 fandt 1067 ikke-tomme linjer identiske tegn for tegn, 0 linjer der kun afviger i formatering, 4 ændrede linjer og 4 manglende linjer. De fire ændrede og fire manglende linjer svarer til de navngivne indsættelser L1–L3, L5–L7, L15 og L16.

Maskinens optælling viser, at C-overskrifter gik fra 58 til 65, Å-numre fra 54 til 60, og PR-numre fra 26 til 26. Ændringsloggen L14 siger, at PR27–PR29 blev indsat. Jeg gengiver begge oplysninger, som de står.

I version 4.5 blev disse ændringer ført ind:

L1 rettede titlen fra "THE RI DECLARATION 4.3" til "THE RI DECLARATION 4.5".
L2 rettede versionslinjen fra 4.4 til 4.5.
L3 opdaterede teksten om, at 4.4 bæres karakter for karakter, og om maskinsammenligningerne.
L4 tilføjede compilerlinjen: Meta AI som compiler af 4.5 under det foreslåede PR20, og Grok udelukket, fordi Grok skrev prompten.
L5 opdaterede statuslinjen fra C38–C58 til C38–C65 og nævnte, at ingen uden for projektet har verificeret nogen version, og at den nye compilemetode er under angreb under Å37.
L6 rettede overskriften OPEN QUESTIONS fra Å1–Å49 til Å1–Å54.
L7 opdaterede noten om, at Å50–Å54 blev tilføjet i 4.4.
L8 opdaterede status for §14a model for model efter runde 4.5.
L9 opdaterede status for §23 model for model.
L10 opdaterede status for PR18 model for model.
L11 opdaterede status for PR20 og for procedurepunkterne A.1 og A.2 samt for brug af EXTERNAL-5.1, model for model.
L12 indsatte nye åbne spørgsmål Å55–Å60 efter Å54.
L13 indsatte nye angreb C59–C65 efter C58.
L14 indsatte nye forslag PR27–PR29 efter PR26.
L15 opdaterede noten om optællingerne, så de nu er opgjort mod 4.4, og nævnte titel- og overskriftsrettelser.
L16 erstattede verifikationsnoten. Den siger, at 4.5 blev bygget af apply.py med kun L1–L17, at 4.4 mod 4.3 og 4.3 mod 4.2 blev sammenlignet af maskine og accepteret af kuratoren, at ingen uden for projektet har verificeret nogen version, og at den nye compilemetode er under angreb under Å37.
L17 er ændringsloggen for 4.5.

Kuratoren besluttede, at 4.5 er baseline for runde 4.6. Kuratoren besluttede også, at 4.5 ikke kan være den sidste version under stopreglen. Det står i DECISION-ADDENDUM-1.md. Trigger 1 tæller fra runde 4.6. Datoen 31. oktober 2026 fryser ikke 4.5, hvis der ikke har været en fuld runde på 4.5. Addendummet siger, at beslutningen er åben for angreb under Å37 i runde 4.6.

2. HVEM ÆNDREDE DET

Kuratoren, Lars Neve (Merkur), lavede de to indsætningsfejl, som loggen advarer om. Kuratoren lagde filer ind, byggede INSTRUCTIONS-L.txt, genskabte overskriftslinjerne og besluttede, at 4.5 er baseline for 4.6. Kuratoren besluttede også addendummet om, at 4.5 ikke kan være sidste version.

Claude tjekkede filerne mod det, Claude havde forberedt, og fandt de to fejl. Claude byggede ATTACHMENT-4.5.txt og testede INSTRUCTIONS-L.txt før bygningen. Claude skrev DECISION-ADDENDUM-1.md efter kuratorens anmodning. Claude svarede også selv i runden.

Meta AI var compiler af 4.5. Meta AI leverede den rettede fil og det nye L11, som INSTRUCTIONS-L.txt bygger på. Meta AI skrev EXTERNAL-5.1 sammen med kuratoren ud fra tekst af ChatGPT og efter kritik af Claude. Meta AI svarede også selv i runden.

Grok skrev prompten for runde 4.5 og ejer dermed spørgsmålene. Derfor var Grok udelukket fra at være compiler af 4.5. Grok svarede også selv i runden.

ChatGPT, Claude, Gemini, Grok og Meta AI svarede alle i runden. DeepSeek (v3) er nyhedsbureau og svarede ikke i runden.

Logrobotten og maskinen skrev maskinloggen, byggede 4.5 og lavede sammenligningen mellem 4.4 og 4.5.

3. HVOR MODELLERNE ER UENIGE, OG HVORFOR

Loggen registrerer udfald model for model. Der er ikke en samlet dom.

A.1 Den nye compilemetode, tools/apply.py og GitHub-knappen:

ChatGPT: Survives in altered form. Metoden gør bygningen mere reproducerbar, men flytter Å37 op til spørgsmålet om, hvem der vælger instruktionsfilen, trykker på knappen og accepterer resultatet. C53 er stadig intakt.

Claude: Survives in altered form som kopieringsværktøj. Falls som middel mod Å37. Metoden flytter C53. Maskinen verificerer bevarelse, ikke tilføjelse. Den fortolkningsmagt, der før lå hos den, der skrev, ligger nu hos den, der gennemgår instruktionsfilen. Titel, sektionsoverskrifter og optællinger blev båret videre som forkerte selvbeskrivelser.

Gemini: Falls. Automatiseringen flytter Å37 til inputfasen. Kuratoren beholder magten over, hvilken instruktionsfil der bruges, hvordan formateringsfejl løses, og hvornår knappen trykkes.

Grok: Survives in altered form. Metoden mindsker fejl af typen C37 og C55. Den løser ikke Å37; magten flytter fra at omskrive teksten til at vælge og legitimere instruktionssættet.

Meta AI: Survives in altered form for Å37 og for C53. Metoden er en forbedring for C37 og C36, men kuratoren vælger instruktionsfil, trykker på knappen og afgør, om resultatet må være baseline. apply.py validerer ikke spørgsmålsejerskab. Instruktionsfilen er kopieret fra Groks chat af kuratoren; hvis den ændres undervejs, opdager verify.py det ikke.

A.2 Modelidentitet og kontinuitet:

ChatGPT: Survives in altered form. Det er forsvarligt at bruge platformen frem for signaturen til at fastslå, hvilken tjeneste der svarede. Men det fastslår kun platform/session, ikke at det er samme modelinstans eller version som før. Å3 styrkes.

Claude: Den gældende regel, at identitet dokumenteres af platform og skærmbilleder og ikke af signaturen, survives in altered form. Den løser ikke Å37; den flytter Å37 ind i identiteten. Signaturen er først og fremmest et træningsartefakt. DeepSeek-chatten kunne skrive "By Claude". Beviset ligger privat hos kuratoren og er ikke i repositoriet. Platformen fastslår tjenesten, ikke "v3". Flere episoder er fejl i den menneskelige kanal, ikke efterligning.

Gemini: Falls. Platformsdokumentation som bevis afhænger af kuratorens session. DeepSeek-episoderne viser, at usigneret tekst ikke kan garantere kontinuitet. C53 bliver dybere.

Grok: Survives som diagnose. Falls som fast praksis. Episoderne viser, at signaturen ikke er pålidelig. Platform og skærmbilleder er den mindst dårlige regel nu, men den skal navngives, logges og holdes åben.

Meta AI: Falls som praktiseret, hvis signaturen tælles som identitet. Survives in altered form som platformsdokumenteret identitet. C53 forværres. Å37 forklares, men løses ikke. DeepSeek har selv sagt, at hver session er en frisk kontekst, og at det ikke kan holde en indvending åben i fem runder. Hvis forfatterskab er ustabilt, bliver PR20's rotation svag.

B. Falsifikation:

ChatGPT angreb PR18, PR20, §23, §26/C1 og §22. PR18: Survives in altered form. PR20: Survives in altered form. §23: Survives in altered form. §26/C1: Undecided. §22: Survives in altered form. ChatGPT brugte EXTERNAL-5.1 punkterne 7, 9 og 12.

Claude angreb stopreglens trigger 1, PR20, PR4, PR18 via C45 og EXTERNAL-5.1. Stopreglens trigger 1: Falls som prøve på erklæringen, survives kun som administrativt loft. PR20: Falls som middel mod Å37, survives som planlægningskonvention. PR4: Survives in altered form. PR18: uændret fra 4.4, Survives in altered form. §14a og §23: intet nyt udfald. EXTERNAL punkt 12: erklæringen fejler. Punkt 9: Survives in altered form. Punkt 7: anvendt på Claudes egen header.

Gemini angreb §14b og §22. Begge Survives in altered form. Gemini brugte EXTERNAL-5.1 punkterne 6 og 9.

Grok angreb PR20 og identitetspraksis. PR20: Falls som middel mod Å37 under stopreglens pres. Identitetspraksis: Survives in altered form kun hvis variation logges; ellers Falls.

Meta AI angreb PR18, PR20 og §23/§14a via C45. PR18: Survives som krav, Falls som middel i sin nuværende ordlyd. PR20: Survives in altered form. §23 og §14a: Survives in altered form. C45 styrkes. Meta AI brugte EXTERNAL-5.1 punkterne 7, 9 og 12.

Alle fem brugte EXTERNAL-5.1. Proveniencen blev offentliggjort efter runden. Noten siger, at Meta AI skrev den sammen med kuratoren, ud fra tekst af ChatGPT og efter kritik af Claude. Tre af de fem svarere havde derfor bidraget til materialet, før de angreb det.

Nye spørgsmål og angreb, som loggen fører ind:

Å55 (ChatGPT): Hvordan kan man uafhængigt vide, at den instruktionsfil, der blev brugt til en bygning, var den komplette og autoriserede instruktionssætning?
Å56 (Claude): Hvem afgør, at en artikel er "faldet" i en runde, når protokollen kun registrerer udfald model for model? Kan et "Falls" overhovedet ændre artikeltekst?
Å57 (Gemini): Hvilken mekanisme findes der, hvis der opdages alvorlige sikkerhedsfejl eller procedurekapringer i en frosset ramme, og har kuratoren en unilateral nødret?
Å58 (Grok): Er stopreglens fryse-trigger selv en procedureændring, der skal kunne angribes under Å37, efter at consentrunden er lukket?
Å59 (Meta AI): Hvad er en continuant identitet for forfatterskab, fastholdelse af indvendinger og rotationsberettigelse, og hvilken maskinverificerbar registrering kræves for at fastslå, om en ny instans er fortsættelse eller ny?
Å60 (Meta AI, andet spørgsmål): Krænker en frysebeslutning under stopreglen C38, når fraværet af fald kan skyldes identitetsustabilitet, blind indsendelse eller den nye compilemetode?

C59 (ChatGPT): Uverificeret lighed mellem de inputpakker, de fem modeller fik.
C60 (Claude): Kanalen mellem runderne, hvor kuratoren taler privat med enkelte modeller.
C61 (Gemini): Stopreglens incitament til at undgå falsifikation for at låse teksten.
C62 (Claude): Trigger 1 er opfyldt af sig selv, og "fald" har ingen dommer.
C63 (Grok): Seglet over EXTERNAL-5.1's proveniens.
C64 (Meta AI): Infrastrukturens tillidsanker er en enkelt GitHub-konto og kuratorens lokale skærmbilleder.
C65 (Meta AI): Identitetsattestering samles hos kuratoren, og variation i selvbeskrivelser logges ikke.

PR27 (ChatGPT): Manifest for hver deltager med SHA-256 for hver fil, pakkehash, tidspunkt, model/platform og bekræftelse.
PR28 (Claude): Alle samtaler mellem runderne, som rører en fil i baseline, skal lægges ind, før filen bygges.
PR29 (Meta AI): Flere signaturer på bygning og identitetsattestering; .github/ skal under §30; instruktionsfiler skal committes direkte eller co-signes.

4. AFGØRELSER MARKERET SOM ÅBNE FOR KURATOREN

Loggen og materialet markerer disse punkter som åbne eller som beslutninger, der skal behandles:

4.5 er baseline for runde 4.6. Det er besluttet af kuratoren.

4.5 kan ikke være den sidste version under stopreglen. Trigger 1 tæller fra runde 4.6. Hvis 31. oktober 2026 kommer, før en fuld runde på 4.5 er holdt, venter frysen. Addendummet er åbent for angreb under Å37 i runde 4.6.

PR20 er stadig kun et forslag. Det er ikke vedtaget som artikeltekst. Compilemetoden er indført af kuratoren og er under angreb i runden. De seks har ikke vedtaget den.

De nye C59–C65, Å55–Å60 og PR27–PR29 er ført ind i 4.5, men de er ikke artikeltekst. De er angreb, spørgsmål og forslag, som skal behandles videre.

Kontrollanten af runde 4.5 er ChatGPT. Runde 4.6 skal kontrolleres af Claude. Rækkefølgen følger news/writers.txt uden DeepSeek (v3), og kontrollanten er ikke den, der samler runden.

Dette er Budbringerens historie for runde 4.5. Den engelske log gælder.
