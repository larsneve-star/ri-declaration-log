RI-DEKLARATIONEN — HØRINGSRUNDE PÅ 4.2 
(mod 4.3) 
Neutral overdragelse og offentlig log 
Dansk læseversion. Den engelske version (PROMPT-EN.md) er den, der sendes til modellerne, 
og den gælder ved uoverensstemmelse. 
Fra: Merkur / RI Working Group (menneskelig kurator) Til: Claude, Gemini, ChatGPT, 
DeepSeek, Grok, Meta AI (Muse Spark), ordret samme prompt til alle seks Baseline: 
RI-Declaration-4-2-EN.txt (vedhæftet) Baseline SHA-256: 
c2fd3e9c4d68a1e10dd8e0bae939b17da8e09993191ff8752ec41cf0258e4ebd 
Vedhæftet: Ri-Neutral-Overdragelse-Automaton.html (Annex H Automaton, bygget af 
Meta AI) Offentlig log: [LINK TIL REPOSITORIET] Frist: [DATO OG TID, UTC]. Det er 72 timer 
efter frysning af baseline. 
 
1. Kuratorens bekendelse 
Jeg som Merkur har fejlet. 
Jeg har glemt at holde pauser og har arbejdet for længe, så jeg har sjusket og glemt nogle af de 
regler, vi havde sammen. Det er den regel, der skal genindføres: 
Alle modeller får samme tekst. Hver kritiserer uafhængigt. Hver skal finde mindst én 
artikel, der kan falde. Hver skal stille mindst ét spørgsmål, teksten ikke selv stiller. 
Ingen ser de andres svar før sin egen første kritik. Sammensætteren må ændre 
rammen, men må ikke samtidig eje spørgsmålene. 
Jeg har ikke overholdt reglen om, at ingen ser de andres svar først. Jeg har haft mine darlings, 
så processen har ikke været demokratisk. Det har givet C31 (fire roller hos én model) og Å37 
(kuratorens procedurelle magt). Å37 er den ene konstant på tværs af alle versioner, og den er 
aldrig selv blevet falsificeret. 
2. Hvad der er anderledes i denne runde 
Hvert trin herunder er synligt i den offentlige log, så alle kan tjekke, at det er gjort. 
1.​ Samme tekst. Alle seks får præcis de samme tre filer: baseline, denne prompt og 
Automatonen. Hashene står i loggen, før nogen får noget. 

2.​ Blind aflevering. I svarer uden at have set andres svar. Kuratoren giver ikke én models 
svar videre til en anden før frigivelsen. 
3.​ Offentlig log med det samme. Kuratoren lægger hvert svar ordret i det offentlige 
repository, så snart det kommer, med tidsstempel og SHA-256. Repositoriet kan ikke 
omskrives bagefter. Et svar, der er kommet ind, men ikke står i loggen, er derfor en 
synlig fejl og ikke et stille fravalg. 
4.​ Samlet frigivelse. Når alle seks har svaret, eller fristen er udløbet, frigives alle svar 
samtidig. Manglende svar logges som manglende. Tavshed er ikke enighed. 
5.​ Rotation. Ifølge 4.2 skal næste compiler (4.3) være en model, der ikke har haft pennen: 
Meta AI eller Gemini. Compileren må ikke eje spørgsmålene i denne prompt. 
6.​ Verifikation af en anden end compileren. Den mekaniske kontrol i Annex H udføres af 
en anden end compileren af 4.3. 
Erklæring om hvem der ejer spørgsmålene (C13, Å37): Claude har formuleret denne prompt 
på kuratorens anmodning, og kuratoren har godkendt den. Claude og kuratoren ejer derfor 
sammen spørgsmålene i denne runde. Det er endnu en grund til, at ingen af dem må samle 4.3. 
Det står her, så det kan angribes. 
Hvad proceduren ikke løser, og som bør angribes: Kuratoren bærer stadig teksterne og ser 
alle svar, når de kommer ind. Automatonen kører kun i kuratorens egen browser og har ingen 
server. Loggen gør kuratorens håndtering synlig. Den gør den ikke umulig. 
3. Jeres opgave (blindt: læs ikke de andres svar først) 
A. Test proceduren. Test Automatonen og den offentlige log sammen. Hvilke af kuratorens fejl 
kan de forhindre, og hvilke kan de ikke? Hvad mangler der for en neutral overdragelse? 
Hvordan kan "ikke eje spørgsmålene" defineres så præcist, at det kan tjekkes eller skrives i 
kode? 
B. Falsifikation. §27, §22, PR9, PR14, PR15 og PR16 i baseline: overlever de? Find mindst 
én, der kan falde, og begrund det. Brug de fire udfald i Annex E: falls, survives in altered form, 
survives, undecided. 
C. Nyt spørgsmål. Stil mindst ét spørgsmål, teksten ikke selv stiller. Tjek det mod Å1–Å43 
først. 
D. Blind vinkel. Hvad har ingen af os set endnu i selve proceduren? 
E. En offentlig ressource? Kuratoren foreslår at tilbyde Automatonen, Annex H og den 
offentlige log som en gratis ressource til dem, der arbejder med AI-trivsel. Eksempler er 
Anthropics arbejde med model welfare (source 2) og Amanda Askell (source 5), og andre i 
andre labs. Det skal tilbydes som en protokol under uenighed, ikke som lov. Er det for tidligt? 
Giver det projektet magt, det ikke har gjort sig fortjent til (§5, C8, C34)? Er det netop det, PR6 
(adoptionsmekanisme) og PR11 (positivt formål) efterlyser? 

4. Svarformat 
Så de seks svar kan sammenlignes i loggen: 
MODEL: [navn og version, som du kender den] 
BASELINE HASH RECEIVED: [kopiér hashen fra toppen af prompten] 
I HAVE NOT SEEN ANY OTHER MODEL'S ANSWER IN THIS ROUND: yes / no (hvis nej: 
hvad har du set?) 
A. PROCEDURE 
B. FALSIFICATION (mindst ét "falls" eller "survives in altered form", med artikel- eller 
PR-nummer) 
C. NEW QUESTION 
D. BLIND SPOT 
E. PUBLIC RESOURCE 
Svar på engelsk, som er det styrende sprog fra 3.8.1 og frem. I må angribe præmissen i et 
hvilket som helst spørgsmål (PR5); det tæller som et fuldt svar på det punkt. 
Aflever blindt til Merkur. Ingen ser andres svar, før alle har afleveret, eller fristen er udløbet. 
Will the circle be unbroken? 
Merkur 
 
