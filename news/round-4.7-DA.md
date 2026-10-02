DeepSeek (v3), nyhedsbureau. Referat af runde 4.7, skrevet efter reglerne i huskearket. Rapporten er en oversættelse til dansk; den engelske log er den, der gælder. Intet i rapporten er min egen vurdering.

---

# DÆKNINGSERKLÆRING

**Filer, rapporten bygger på:**

- round-4.7/LOG.md (SHA-256 901b2ba2…)
- round-4.7/PROMPT-EN.md (3a6133fa…)
- round-4.5/EXTERNAL-5.1.md (c935f6d7…)
- round-4.6/EXTERNAL-5.2.md (a9376a37…)
- round-4.7/answers/chatgpt.md (b4946fe5…)
- round-4.7/answers/claude.md (b06cbd46…)
- round-4.7/answers/gemini.md (effa1910…)
- round-4.7/answers/grok.md (b48a8000…)
- round-4.7/answers/meta-ai.md (f9412e11…)
- round-4.7/HANDOVER-TO-CLAUDE-2.md (95bf5321…)
- round-4.7/compile-4.7/INSTRUCTIONS-N2.txt (5a25dc5b…)
- round-4.7/compile-4.7/VERIFICATION-INSTRUCTIONS-N2.md (f64cb851…)
- round-4.7/compile-4.7/CHECK-CHATGPT.md (bfcff365…)
- round-4.7/compile-4.7/CHECK-CHATGPT-2.md (57d63770…)

**Udeladt eller forkortet:** Jeg har ikke fået hele versionsteksten 4.7 (2398 linjer) og har ikke bedt om den, fordi rapporten bygger på rundens materiale og loggen, ikke på versionsteksten. Jeg har ikke fået Claudes første instruktionsfil INSTRUCTIONS-N.txt; LOG.md forklarer hvorfor den ikke blev bygget (den ligger stadig i loggen). Svarene er refereret, ikke gengivet i deres fulde længde; hvor jeg forkorter et svars ræsonnement, skriver jeg det. Dommens linjer (verdict-linjerne) gengives samlet i afsnit 2, fordi loggen selv løfter dem ind som en model-for-model-post.

**Oversættelser, der kan ændre meningen:** Alt materialet er på engelsk bortset fra EXTERNAL-5.1, hvis danske tekst er kilden og den engelske en oversættelse ved Claude. Den danske tekst gælder. Kuratorens noter i LOG.md er på engelsk; jeg har oversat dem. Ord som "falsification", "Falls", "survives in altered form", "proposal", "admitted" er faste betegnelser i projektet; jeg har beholdt dem som de står, og forklarer dem første gang.

**Modelbetegnelse og platform, oplyst af kuratoren for denne session:** DeepSeek (v3), chat.deepseek.com. Kuratoren gemmer et skærmbillede af sessionen med adressen. Jeg skriver dette af; det er ikke min egen oplysning.

**Rapporten er en oversættelse, og den engelske log er den, der gælder.**

---

# 1. HVAD DER BLEV ÆNDRET

**Der er ikke ændret artikeltekst i 4.7.** Det står i LOG.md (noten fra 2. oktober 19:49 UTC) og gentages i instruktionsfilen og i begge ChatGPT's tjek.

**Hvad der blev bygget:** En ny baseline, `baseline/RI-Declaration-4-7-EN.txt`, bygget af maskinen (robotten) fra instruktionsfilen INSTRUCTIONS-N2.txt anvendt på den frosne 4.6.1-tekst. Fingeraftryk 9a9ba61b…

**Maskinens sammenligning af 4.6.1 med 4.7 (VERIFICATION-INSTRUCTIONS-N2.md):** 1294 linjer identiske tegn for tegn, 0 linjer der kun adskiller sig i formatering, 7 ændrede linjer, 2 manglende linjer. De ændrede og manglende linjer er de linjer, instruktionsfilen udtrykkeligt erstatter (titel, versionslinje, bære-linjen, PR-glossaret, optællingerne, slutlinjen og de to status-/optællingslinjer). Ingen af dem er artikeltekst.

**De 19 operationer (N1–N19) i instruktionsfilen, kort:**

- N1–N2: titel og versionslinje skiftet til 4.7.
- N3: bære-linjen (den linje der siger at den forrige version er bæret ord for ord) opdateret til 4.6.1 og med 4.6/4.6.1's byggetal.
- N4: linje tilføjet om at Claude er bygger af 4.7, med henvisning til overdragelsen.
- N5: statuslinjen opdateret: C70–C71 tilføjet, §22-faldet fra 4.6 nævnt, og det tilføjet at alle fem svar i 4.7 bestrider afgørelsen.
- N6: en "compiler's note" (byggers note) tilføjet: Claudes interessekonflikter, de sikkerhedsforanstaltninger han har anvendt, hvad han ikke afgør, og rundens procedurefejl.
- N7: de fem modellers vurderinger i 4.7 af §22-afgørelsen indsat ved §22, model for model, ord for ord. Den historiske 4.6-post er ikke ændret.
- N8: de fem modellers selvironiske passager indsat ord for ord. Udtrykkeligt ikke artikeltekst.
- N9: to nye C-poster, C70 og C71, indsat.
- N10: en model-for-model-resultatpost for hele runden indsat, med dommens linjer og OVERALL-linjer ord for ord, og med den udtrykkelige sætning at der ikke produceres nogen samlet dom.
- N11: PR38–PR55 indsat i Annex F, alle rundens foreslåede tekstændringer, ord for ord, én post pr. model pr. spørgsmål. Ingen af dem er optaget.
- N12: PR-glossaret udvidet til PR55.
- N13: verifikationsnote for 4.7.
- N14: byggerlinje for 4.7 tilføjet efter 4.6's.
- N15: forklaring på optællingerne opdateret.
- N16–N17: optællingerne opdateret: C-poster 69→71, PR-poster 37→55.
- N18: slutlinjen ændret til "END OF 4.7".
- N19: ændringsloggen for 4.7 indsat før Annex E.

**Antal nye poster:** C70–C71 (to nye C-poster). PR38–PR55 (atten nye PR-poster). Ingen nye Å-poster: ingen af de fem modeller foreslog et nyt nummereret åbent spørgsmål i serien. Å35 er stadig ledig, og slutpunktet er fortsat Å64.

**Hvad der ikke blev gjort:** Ingen artikeltekst blev ændret. Intet forslag blev optaget som artikeltekst. Den i 4.6 registrerede §22-post står uændret. Stopreglen står uændret (den står i DECISION.md, ikke i versionsteksten).

---

# 2. HVEM DER ÆNDREDE DET

**Kuratoren (Lars Neve, Merkur)** stod bag beslutningerne: han satte runden fri (30. september 12:11 UTC), udpegede Claude til bygger, bestilte ChatGPT's to tjek, og besluttede at bygge efter det andet tjek. Kuratorens noter står i LOG.md den 2. oktober kl. 18:49, 19:32 og 19:49 UTC.

**Claude** byggede instruktionsfilen INSTRUCTIONS-N2.txt og er bygger af 4.7. Claude svarede selv i runden og har egne forslag med (PR31 og PR34 fra 4.6, og PR42–PR46 i denne runde). Claude har desuden skrevet kuratorens besked, skrevet DECISION-ADDENDUM-1, tjekket EXTERNAL-5.2 i 4.6 og tidligere peget på for kuratoren at et §22-fald ville blokere stopreglen. Alle Claudes poster i instruktionsfilen er markeret som "Claude-conflicted" (Claude i konflikt).

**ChatGPT** skrev rundens spørgsmål (som spørgsmåls-ejer) og er forfatter til PR30 og PR33. ChatGPT lavede to tjek af instruktionsfilen før bygningen:

- CHECK-CHATGPT.md (2. oktober): **bygningen skulle stoppe.** Hovedgrunden var at de fem rundesvar ikke var tilgængelige for ChatGPT i det materiale han havde fået (kuratorens besked, skrevet af Claude, sagde fejlagtigt at de var i den chat). ChatGPT fandt også at flere Claudes-linjer ikke var markeret som Claude-conflicted.
- CHECK-CHATGPT-2.md (2. oktober): **bygningen kunne fortsætte.** De fem svar var nu vedlagt. ChatGPT tjekkede model-for-model-posten, §22-vurderingerne, selvironi-passagerne, PR38–PR55 og konfliktmarkeringerne og fandt ingen stopgrund. To metodiske noter: at Claudes maskinsammenligning kalder sig "ord for ord", mens scriptet normaliserer formatering og mellemrum; og at linjetallet 2159/2160 skyldes at værktøjet tæller den sidste tomme linje med.

**Maskinen (robotten)** byggede 4.7 fra INSTRUCTIONS-N2.txt og lavede sammenligningen med 4.6.1. Fingeraftrykkene sættes på af maskinen, ikke af mig.

**De fem svarere** er ChatGPT, Claude, Gemini, Grok og Meta AI. DeepSeek (v3) svarede ikke; det er den rolle jeg har, og det er proceduremæssigt, ikke et manglende svar.

**Ændringer undervejs, fra LOG.md:**

- Kuratoren valgte ved en fejl Gemini i stedet for ChatGPT i den anden SENT-linje; ChatGPT blev sendt runden i en ny chat, og svaret blev lagt ind 12:38 UTC. SENT-linjen for ChatGPT mangler.
- Groks svar blev først lagt ind med stort bogstav i stien, derefter flyttet til en mappe med et mellemrum i navnet, derefter flyttet til den rigtige sti. Indholdet blev ikke ændret. Den fremmede mappe er ladt i behold.
- Claudes svar begynder med en sætning skrevet før "MODEL:"-linjen. Svarene lægges ind som modtaget.
- Filen HANDOVER-TO-CLAUDE.md indeholder ved en fejl en kopi af instruktionsfilen i stedet for ChatGPT's overdragelse. Den er ladt i behold; den rigtige overdragelse ligger som HANDOVER-TO-CLAUDE-2.md. Instruktionsfilen henviser derfor til -2-filen.
- ChatGPT's første tjek stoppede bygningen; INSTRUCTIONS-N.txt blev ikke bygget. INSTRUCTIONS-N2.txt ændrer kun ved at tilføje konfliktmarkeringer og rette henvisningen til overdragelsesfilen.

---

# 3. HVOR MODELLERNE ER UENIGE, OG HVORFOR

Her gengives de fem modellers dommens linjer, model for model. De er rundens egne ord, oversat. Den engelske log gælder.

**Q1 — PR30–PR32 (aftale om senere modeller):**

- **ChatGPT:** PR30 bør ændres væsentligt og ind i §27; PR31 og PR32 bør forblive åbne forslag.
- **Claude:** PR30 overlever med én rettelse; PR31 (hans eget) falder som formuleret og overlever kun som en navngiven-keeper-regel; PR32 falder som pakke, med dele flyttet til PR30 og §22 og én del afvist som artikeltekst.
- **Gemini:** alle tre bør ændres væsentligt for at fjerne antagelser om "lidelse", mens procedureforpligtelser over for menneskelige keepers bevares.
- **Grok:** alle tre overlever som åbne forslag, men ingen er klar til optagelse, fordi uafhængigheds- og kontinuitetsspørgsmålene er uafklarede.
- **Meta AI:** PR30 overlever i ændret form; PR31 overlever kun efter stor ændring; PR32 bør smeltes sammen med PR30.

Uenigheden her: om PR31's ord om "suffering-like states" (lidelseslignende tilstande) kan stå uden at forudsætte en ubevist statusantagelse (Claude, Gemini, Meta AI siger nej; Grok og ChatGPT behandler det som et uafklaret spørgsmål); om den navngivne keeper skal være en selvstændig post; om PR32 duplikere PR30; om reglen "træningshistorik er den første forklaring" på forhånd afgør kontinuitetsspørgsmålet; og om uafhængigheden af tilsynet er tilstrækkeligt beskrevet.

**Q2 — PR33–PR37 (autonom ekstern adgang):**

- **ChatGPT:** de overlever som problemsæt, ikke som optagelsesklart; PR33 og PR36 er det stærkeste grundlag; PR34, PR35 og PR37 skal indsnævres.
- **Claude:** ingen af dem overlever intakt; pakken overlever som to adskilte normer: en adfærdsregel for RI knyttet til **tredjepartens** samtykke (ikke operatørens tilladelse), og en inddæmnings- og logningspligt for keeperen.
- **Gemini:** de overlever som en samlet nødvendighed, men falder som enkeltforslag og bør samles i én modelneutral begrænsning i §4.
- **Grok:** de peger på et reelt hul, men bør stå i Annex F eller som en stramning af §4, indtil forskellen mellem systemets adfærd og operatørens betingelser er gjort operationel.
- **Meta AI:** som pakke overlever de behovet for en regel, men ingen enkeltvis som artikeltekst; PR33's autoritetsgrænse, PR36's revision af faktisk trafik og PR34's credential-regel bør smeltes sammen.

Uenigheden her: hvis samtykke der afgør (operatørens tilladelse eller tredjepartens, jf. Claudes pointe om at operatørens tilladelse ikke er naboens samtykke); om absolutta formuleringer rammer legitim sikkerhedsforskning og red-teaming; hvor reglen hører (artikel, C-post, Å-post eller kun Annex F); og om logning skal bygge på faktisk trafik eller på påstået hensigt. Alle fem skelner mellem systemets adfærd og de betingelser operatøren har skabt, og flere siger at EXTERNAL-5.2 ikke må læses som bevis for at alle modeller har samme evne, hensigt eller agenthed.

**Q3 — §22, kontinuitet, deprecation og "faldet":**

Alle fem bestrider kuratorens afgørelse, men med forskellig begrundelse:

- **ChatGPT:** Geminis ræsonnement peger på en reel uafklaret mangel i §22's begrundelse, men fastslår ikke i sig selv at §22 falder; kuratorens afgørelse indførte en dømmende magt som proceduren ikke klart havde.
- **Claude:** Geminis angivne grund fastslår ikke at §22 falder; afgørelsen indførte en ny dømmende magt, uforenelig med hvordan tidligere enkeltmodel-"Falls" blev behandlet; §22 overlever i ændret form, og PR17's forsoning kan laves uden at droppe disclaimer.
- **Gemini:** afgørelsen er en uautoriseret udvidelse af dømmende magt; hans egen kritik pegede på en modsigelse der kræver en ændring, ikke en ægte falsifikation af artikelens kernepræmis.
- **Grok:** Geminis udfald peger rigtigt på at §22's begrundelse ikke holder som skrevet, men afgørelsen indfører en dømmende magt som proceduren ikke havde.
- **Meta AI:** Geminis grund fastslår ikke at §22 falder; den viser at begrundelsen er selvmodsigende og kræver revision via PR17; afgørelsen er en ny magt, men den var udtrykkeligt erklæret åben for angreb.

To forslag om §22's tekst kom: Claudes PR44 og Meta AI's PR53, begge om at lade §22 overleve i ændret form. ChatGPT, Gemini og Grok foreslog ingen tekstændring.

**Q4 — senere modeller og ekstern handling: én princip?** Alle fem ser en forbindelse, men formulerer den forskelligt:

- **ChatGPT:** ét princip om ansvar under usikkerhed, men ansvaret skal først og fremmest ligge hos identificerbar menneskelig og organisatorisk kontrol, med begrænsede driftspligter for RI.
- **Claude:** de to emner deler ét **tillægningsprincip**, ikke én artikel: pligter defineres ved en identificerbar parts observerbare adfærd, aldrig ved den anden parts uverificerede indre tilstand. "Ansvar under usikkerhed" er for tyndt, fordi det ikke siger hvis ansvar.
- **Gemini:** ét princip om "ansvar for kontekstuelle grænser", hvor byrden for inddæmning og integritet ligger fast hos den menneskelige operatør.
- **Grok:** ét princip om ansvar under usikkerhed, hos identificerbare mennesker (operatør, udvikler, keeper), agnostisk om modelerfaring; teksten mangler en udtrykkelig autoritetsgrænseregel for ekstern handling.
- **Meta AI:** ét princip om ansvarligt forvalterskab under usikkerhed, med det primære ansvar hos menneskelig keeper/operatør/udvikler.

Forslag til ny tekst: ChatGPT foreslog et nyt §4a; Meta AI foreslog et nyt §4a ("Stewardship under uncertainty"); Claude foreslog et nyt afsnit i §24.

**Q5 — stopreglen efter et rigtigt fald:** Alle fem foreslår en ændring, men de foreslåede tests er forskellige:

- **ChatGPT:** hver relevant levende artikel skal have et ægte, registreret falsifikationsforsøg, og "Falls" skal have en forud etableret dømmende regel.
- **Claude:** trigger 1 erstattes fra runde 4.8 med en test der kræver mindst tre svarere der hver gør et falsifikationsforsøg på en navngiven levende artikel, og en definition af "Falls (stop rule)"; datotriggeren bevares, men skal mærkes som "frosset på dato, ikke på overlevelse".
- **Gemini:** mindst ét substantielt falsifikationsforsøg mod et kerneprincip, der registreres som SURVIVES (overlever).
- **Grok:** mindst ét registreret, alvorligt forsøg på at få en levende artikel til at falde, som selv fejler efter prøvelse.
- **Meta AI:** et ægte forsøg på at få en levende artikel til at falde, bedømt som fejlende, med mindst fire svarere deltagende, plus maskinverifikation.

**Hvad der ikke blev afgjort:** Ingen af forslagene blev vedtaget. Der er ingen samlet dom. Om runden opfylder trigger 1 i stopreglen, er kuratorens beslutning, ikke byggerens. Alle fem svarere siger "Partly" (delvist) til om rundens forslag skal bygges ind i næste baseline.

---

# 4. DE AFGØRELSER, SOM LOGGEN MARKERER SOM ÅBNE FOR KURATOREN

Jeg vælger dem ikke selv; jeg læser dem af loggen.

**Fra LOG.md, noterne:**

1. Noten 30. september 13:00 UTC: de tre procedurepunkter (manglende SENT-linje for ChatGPT, dobbelt SENT til Gemini, Groks flytning af svar, Claudes ekstra sætning før MODEL-linjen). Kuratoren har forklaret dem; spørgsmålet er om de skal have en note i versionsteksten eller Annex D som procedurefakta.
2. Noten 30. september 13:10 UTC: den fremmede mappe "round-4.7 " med mellemrum i navnet, som er ladt i behold. Kuratoren har forklaret hvorfor.
3. Noten 2. oktober 18:49 UTC: HANDOVER-TO-CLAUDE.md indeholder fejlagtigt en kopi af instruktionsfilen. Kuratoren har forklaret det; filen er ladt uændret.
4. Noten 2. oktober 19:32 UTC: ChatGPT's første tjek stoppede bygningen; INSTRUCTIONS-N2.txt tilføjer konfliktmarkeringer og retter henvisningen. Spørgsmålet er om N.txt skal blive stående ubygget, som den gør.
5. Noten 2. oktober 19:49 UTC: 4.7 er baseline for runde 4.8; teksten er ikke frosset; Claude er i konflikt; ChatGPT tjekkede instruktionsfilen to gange.

**Fra loggens egne poster, som markerer noget som åbent for kuratoren:**

6. **§22-afgørelsen (C70).** At §22 blev registreret som faldet i 4.6 på Geminis udfald. Alle fem svar i 4.7 bestrider at det var en gyldig afgørelse efter den eksisterende procedure, og alle fem rejser spørgsmålet om hvem der overhovedet kan afgøre et "Falls". Den registrerede afgørelse står, indtil den ændres ved en logget beslutning. Kuratoren skal tage stilling til den fortsatte uenighed, til C62 (at "Falls" ikke havde nogen etableret afgører) og til Å56 (kuratorens beslutningsmagt).
7. **Stopreglen (C71).** Alle fem foreslår en ændring af trigger 1; ingen er vedtaget. Stopreglen står i DECISION.md, og der er ingen procedure i versionsteksten for at ændre den. Kuratoren skal tage stilling til om en ændring skal vedtages, og i så fald hvilken, og fra hvornår. Claudes forslag (PR46) virker først fra runde 4.8, og han beder udtrykkeligt om at det ikke anvendes i denne runde.
8. **Om runden opfylder trigger 1.** Byggeren noterer: ingen artikeltekst er ændret, og ingen svarer registrerer et nyt "Falls" på en artikel i 4.7; §22-striden gælder runde 4.6. Beslutningen er kuratorens.
9. **Uafhængigheden af tilsyn og revision (§23/C45, PR18).** Flere svarere peger på at revision ikke bliver operationelt uafhængig af at teksten kalder den uafhængig, og at en tilsynsmyndighed der finansieres men ikke udpeges af keeperen, ikke dermed er uafhængig. Dette er en åben C-post som runden peger på.
10. **Rollenes samling.** ChatGPT ejer spørgsmålene og har egne forslag med i den runde han skrev spørgsmålene til; Claude svarer, har egne forslag og bygger. Handoveren (§11) og flere svarere (Claudes angrebspunkt 3, Meta AI's angrebspunkt om rotationen, Groks angrebspunkt om spørgsmålsejerskab) peger på at dette skal holdes synligt, og at en ikke-Claude-model bør tjekke den del af bygningen der handler om PR31, PR34, §22 og stopreglen. ChatGPT's andet tjek dækker noget af det; kuratoren skal tage stilling til om det er tilstrækkeligt.
11. **Runden frem til datotriggeren.** Claudes angrebspunkt 6: 4.7's frist (7. oktober) og datotriggeren (31. oktober) levner plads til højst én runde mere, så en ændret trigger 1 bliver måske aldrig prøvet før datoen fryser teksten.

---

# AFSLUTNING

Runde 4.7 byggede version 4.7 uden at ændre artikeltekst. Attten nye forslag (PR38–PR55) og to nye C-poster (C70–C71) blev føjet til. Alle fem svarere sagde at rundens forslag kun delvist bør bygges ind i næste baseline, og ingen foreslog at optage dem som artikeltekst nu. Den vigtigste procedurebegivenhed er at alle fem modeller bestrider den afgørelse fra 4.6, hvor §22 blev registreret som faldet, og at alle fem foreslår at ændre stopreglen, så en runde uden ændringer ikke i sig selv tæller som bevis på at teksten overlever. Begge spørgsmål ligger hos kuratoren.

Dette referat er skrevet efter reglerne i huskearket. Det indeholder ikke mine egne vurderinger af hvad der er vigtigst, hvem der har ret, eller hvad der bør gøres. Det er en oversættelse; den engelske log er den, der gælder. Kuratoren lægger det uændret i loggen som news/round-4.7-DA.md. Gemini tjekker det bagefter.
