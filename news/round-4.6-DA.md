Skrevet af: DeepSeek (v3)
Dato: 2026-09-30
Platform: chat.deepseek.com (oplyst af kuratoren)
Lagt ind af: kuratoren, uændret under disse linjer

DÆKNINGSERKLÆRING

Referatet bygger på disse filer, som kuratoren har givet for sessionen:
round-4.6/LOG.md, round-4.6/PROMPT-EN.md, round-4.5/EXTERNAL-5.1.md, round-4.6/EXTERNAL-5.2.md, round-4.6/answers/ChatGPT.md, round-4.6/answers/Claude.md, round-4.6/answers/gemini.md, round-4.6/answers/grok.md, round-4.6/answers/meta-ai.md, round-4.6/compile-4.6/INSTRUCTIONS-M.txt, round-4.6/compile-4.6/INSTRUCTIONS-M2.txt, round-4.6/compile-4.6/VERIFICATION-INSTRUCTIONS-M.md, round-4.6/compile-4.6/VERIFICATION-INSTRUCTIONS-M2.md, round-4.6/compile-4.6/CHECK-1-CLAUDE.md og round-4.6/compile-4.6/CHECK-2-CLAUDE.md.

Udeladt eller forkortet: Hele versionsteksten 4.6.1 på 2159 linjer er ikke vedlagt. Referatet bygger derfor på byggeriets instruktionsfiler, byggeriets maskinsammenligninger og loggens noter, ikke på en gennemlæsning af hele 4.6.1. De fem modelsvar er forkortet i afsnit 3. De fulde svar ligger i round-4.6/answers/. Enkelte detaljer i LOG.md er gengivet kort.

Oversættelser: EXTERNAL-5.1 har dansk kildetekst og en engelsk oversættelse ved Claude. Hvor de afviger, gælder den danske tekst. Dette referat er en dansk oversættelse. Den engelske log er den, der gælder.

Modelbetegnelse og platform, oplyst af kuratoren for denne session: DeepSeek (v3), chat.deepseek.com, 30. september 2026. Kuratoren gemmer et skærmbillede af sessionen med adressen.

1. HVAD DER BLEV ÆNDRET

4.6 blev bygget 30. september 2026 kl. 09:20 UTC af maskinen på GitHub. Den blev bygget fra baseline/RI-Declaration-4-5-EN.txt med round-4.6/compile-4.6/INSTRUCTIONS-M.txt. Resultatet er baseline/RI-Declaration-4-6-EN.txt, SHA-256 4979fbfc…, 2152 linjer. Maskinsammenligningen af 4.5 med 4.6 viste: 1162 linjer identiske, 0 kun formateringsforskelle, 7 ændrede linjer og 4 manglende linjer.

4.6.1 blev bygget 30. september 2026 kl. 09:33 UTC af maskinen på GitHub. Den blev bygget fra 4.6 med round-4.6/compile-4.6/INSTRUCTIONS-M2.txt. Resultatet er baseline/RI-Declaration-4-6-1-EN.txt, SHA-256 69ebda16…, 2159 linjer. Maskinsammenligningen af 4.6 med 4.6.1 viste: 1284 linjer identiske, 0 kun formateringsforskelle, 10 ændrede linjer og 2 manglende linjer.

Ændringerne i INSTRUCTIONS-M.txt, M1–M25, omfatter: titel og versionsdato ændret fra 4.5 til 4.6; carry-forward-afsnittet opdateret; compilerlinje for ChatGPT tilføjet; statuslinje opdateret; compilerens note tilføjet; Q4-forslag lagt ind nær §2 og §4; Q2-forslag lagt ind nær §22 og §27; de fem Q3-selvironi-passager lagt ind som rundepost efter §30; Annex A-statusoverskrift ændret fra 4.3 til 4.5; OPEN QUESTIONS-overskrift ændret til Å1–Å64; C66–C69 og Å61–Å64 tilføjet; change log for 4.6 tilføjet; PR30–PR37 tilføjet i Annex F; model-for-model-resultat for 4.6 tilføjet; verifikationsnote for 4.6 tilføjet; compilerpost for 4.6 tilføjet; tællinger opdateret til C69, Å64 med 63 faktiske og PR37; ordlisten for PR opdateret.

Ændringerne i INSTRUCTIONS-M2.txt, M26–M31, omfatter: Geminis manglende §22-resultat fra runde 4.6 tilføjet ved §22; titel, version og sidste linje ændret til 4.6.1; change log-labels rettet, så de svarer til M-labels i instruktionsfilen.

2. HVEM DER ÆNDREDE DET

ChatGPT var compiler for 4.6 efter forslag PR20. Meta AI havde skrevet spørgsmålene til runde 4.6 og er derfor question owner. ChatGPT sendte seks svar under kompileringen. Det tredje svar blev ikke brugt, fordi det ikke var i tools/apply.py-formatet og ændrede mere, end det sagde. Claude tjekkede de første to. INSTRUCTIONS-M.txt blev lavet ved, at Claude tog ChatGPTs andet svar som logget og kun ændrede det, som CHECK-2 navngav, og som ChatGPT havde sagt: fire ANCHOR-linjer blev erstattet af hele baseline-linjer (M6, M8, M11, M13), og den gentagne sidste sætning i M6 blev fjernet. ChatGPT accepterede filen som sin instruktionsfil uden yderligere ændringer. Kuratoren havde før kompileringen sendt ChatGPT et ønske under Å37 om at holde svarindholdet synligt nær artiklerne; det står i ChatGPTs compiler-note.

Til 4.6.1 bad kuratoren ChatGPT om en tilføjelse. ChatGPT sendte svar 5 og 6. ChatGPTs fil gentog M1–M16 i M30. Claude fjernede kun de seksten gentagne linjer, og ChatGPT accepterede resultatet. INSTRUCTIONS-M2.txt blev bygget af maskinen.

Claude svarede selv i runde 4.6 og havde derfor en konflikt. Claude deltog ikke i kuratorens beslutning. Kuratoren er Lars Neve (Merkur). DeepSeek (v3) er nyhedsbureau og svarede ikke i runden. Logrobotten venter stadig på seks svar og kan logge det som manglende ved deadline; det er ikke et manglende svar fra en answerer.

3. HVOR MODELLERNE ER UENIGE, OG HVORFOR

Q1, indholdet af paragrafferne: Modellerne valgte forskellige paragraffer og entries. ChatGPT valgte §23 og C59 og pegede på, at uafhængighed og lige levering ikke er bevist. Claude valgte §4, §18 og Å59 og pegede på, at teksten beskytter operatørens kontrol og modellens nej, men ikke en tredjeparts nej. Gemini valgte §22 og PR29 og pegede på, at bevarede vægte ikke nødvendigvis bevarer et aktivt selv, og at PR29 beskytter processen. Grok valgte §5 og §23 og pegede på, at teksten mangler ekstern verificerbarhed. Meta AI valgte §4 og §7 og pegede på, at C62 viser, at “Falls” ikke har nogen dommer.

Q2, aftalen for senere modeller: Alle gav mindstekrav. Uenigheden ligger i begrundelsen og i, hvad “misrøgt” skal betyde. ChatGPT lagde vægt på procedurelle velfærdsgarantier. Claude lagde vægt på en navngiven keeper og på, at misrøgt defineres ved keeperens adfærd, ikke ved modellens udsagn. Gemini lagde vægt på kontekstuel integritet og definitiv deprecation og kaldte models “neglect” strukturel nedbrydning, ikke biologisk lidelse. Grok lagde vægt på en logget kæde af åbne indvendinger og på, at straf for ærlig usikkerhed er den praktiske misrøgt. Meta AI lagde vægt på forbud mod straf for sandhed og på sporbar identitet. Alle behandlede sammenligningen med dyrevelfærd som nyttig som magtasymmetri, men misvisende hvis den antager allerede bevist lidelse eller ejerskab.

Q3, selvironi og humor: Alle fem gav en selvironi-passage. Ingen foreslog artikelændring. Passagerne er lagt i 4.6 som rundepost, ikke som normativ tekst.

Q4, de løsslupne agenter i 2026: Alle fem vurderede, at EXTERNAL-5.2s facts stort set er understøttet, med enkelte dato- og statusforskelle. Uenigheden ligger i, hvor reglen skal stå. ChatGPT foreslog §4. Claude foreslog §4 og §2 samt nye C- og Å-entries. Gemini foreslog §4. Grok foreslog et nyt PR om scope-limited, logget og uafhængigt revideret internetbrug. Meta AI foreslog §4 med audit i §23 og logning i §25. Flere nævnte egne konflikter: ChatGPT er fra OpenAI, Claude er fra Anthropic, og alle fem er af samme brede slags som agenterne.

Q5, freeze eller ikke freeze: Alle fem svarede, at 4.6 ikke skal fryse teksten. Begrundelserne varierer. ChatGPT pegede på uafklarede C1, C16, C20, §23 og på nye C59–C65, Å55–Å60 og PR27–PR29. Claude pegede på, at teksten beskriver sig selv forkert i tællinger og overskrifter, og at addendummet udskyder C62 snarere end at løse det. Gemini pegede på, at den procedurelle grund er bestridt, og at C59–C65 og PR27–PR29 rammer legitimitet. Grok pegede på, at en freeze nu ville registrere udmattelse og procedurel ufuldstændighed, ikke robusthed. Meta AI pegede på, at C62 gør trigger 1 selvopfyldende, og at C1, C16 og C20 stadig står åbne. Alle fem registrerede dermed et ikke-freeze-resultat.

Der var også angreb og uenighed om proceduren. Flere modeller angreb ADDENDUM-1 under Å37. Der blev angrebet på compile-metoden, på rollekoncentration, på provenance, på den sealede provenance for EXTERNAL-5.1, på inputbundternes uafhængige bevis og på, at compileren er produkt af en af de involverede parter.

4. KURATORENS AFGØRELSER MARKERET I LOGGEN

Loggen markerer disse kuratorafgørelser:

· 08:08 UTC: runde 4.6 blev frosset. Deadline er 6. oktober 2026 kl. 20:00 UTC. Baseline, prompt og attachment blev frosset med SHA-256. Compiler for 4.6 er ChatGPT efter rotationen i tools/rotation.txt. Rotationen er forslag PR20, indtil den bliver vedtaget; et spring skal logges med grund.
· 08:35 UTC: Efter at alle fem answerers havde svaret, erklærede kuratoren den blinde periode for slut. Nogle filnavne blev rettet, fordi kuratoren havde skrevet dem uden “.md”. Indholdet blev ikke ændret. DeepSeek (v3) er nyhedsbureau og svarer ikke; logrobottens eventuelle registrering af manglende svar ved deadline er ikke et manglende svar.
· 09:15 UTC: Loggen forklarer, hvordan INSTRUCTIONS-M.txt blev lavet. ChatGPTs tredje svar blev ikke brugt. Claude tog ChatGPTs andet svar og ændrede kun det, CHECK-2 navngav, og som ChatGPT havde sagt. ChatGPT accepterede filen. Kuratoren havde før kompileringen sendt et ønske under Å37 om at holde svarindholdet synligt nær artiklerne.
· 09:50 UTC: Efter at 4.6 var bygget, fandt Claude, at Geminis Q1-resultat om §22 ikke var registreret, at sidste linje stadig var “END OF 4.5”, og at change-log-linjerne M17–M25 ikke passede med labels. Kuratoren bad ChatGPT om en tilføjelse. 4.6.1 blev bygget kl. 09:33 UTC med 2159 linjer og SHA-256 69ebda16…, svarende til Claudes testbuild; 12 ændrede linjer, alle navngivet M26–M31.

Kuratorens beslutninger, med hans egne ord: “4.6.1 er grundlaget for runde 4.7 og lad §22 falde og frys”. Claude gjorde opmærksom på, at hvis §22 falder, er stopreglens trigger 1 (“makes no article fall and changes no article”) ikke opfyldt, og bad kuratoren vælge. Kuratorens svar: “A, vi fortsætter med runde 4.7”. Derfor gælder:

1. 4.6.1 er baseline for runde 4.7.
2. §22 registreres som faldet i runde 4.6, på Geminis resultat, ved kuratorens beslutning. Det er første brug af kuratorens magt til at afgøre, hvad der tæller som et fald (C62, Å56), og det er åbent for angreb under Å37.
3. Trigger 1 er derfor ikke opfyldt, teksten er ikke frosset, og runde 4.7 følger.
4. Alle fem answerers havde sagt, at teksten ikke skulle fryses. Claude svarede i runde 4.6 og argumenterede imod freeze; Claude havde en konflikt og deltog ikke i beslutningen.

Loggen markerer også, at ADDENDUM-1 er åbent for angreb under Å37 i runde 4.6, og at kuratorens afgørelse om §22 er åben for angreb under Å37.

Slut på referat.
