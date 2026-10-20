import json,re,sys
S=sys.argv[1]
T={}
for l in open(S+'/az20.txt',encoding='utf-8'):
    i,_,t=l.rstrip('\n').partition(' '); T[int(i)]=t
def rep(i,a,b):
    assert a in T[i],(i,a); return T[i].replace(a,b)

C={}; A={}
C[34]=rep(34,"su diverse piattaforme online e/o sul proprio sito internet;","sugli account intestati al Mandante presso le diverse piattaforme online, nonché sul proprio sito internet;")
C[27]=rep(27,"a fornire agli Ospiti i servizi accessori alla locazione meglio definiti","a fornire agli Ospiti, in nome e per conto del Mandante, i servizi meglio definiti")
C[37]="determinare i corrispettivi da richiedere agli Ospiti, secondo quanto previsto dall’art. 6;"
C[43]="gestione dell’imposta di soggiorno: calcolo degli importi dovuti, richiesta agli Ospiti, compilazione della relativa dichiarazione e predisposizione del prospetto per il versamento al Comune, che è effettuato dal Mandante;"
C[47]="verificare, attraverso l’accesso al gestionale, l’avvenuto pagamento delle prenotazioni prima del check-in; i canoni sono incassati direttamente dal Mandante ai sensi dell’art. 10;"
C[48]="richiedere adeguati depositi cauzionali o garanzie in caso di locazione superiore a giorni 30, da versarsi direttamente al Mandante;"
C[53]="rimuovere senza indugio, alla cessazione del rapporto, ogni riferimento, informazione, fotografia ed in genere contenuto anche multimediale relativo all’Immobile dal proprio sito internet e restituire al Mandante la gestione esclusiva degli annunci e degli account a lui intestati, fatto salvo quanto previsto dall’art. 17 per le Prenotazioni Future."
C[54]="Nel dettaglio, i servizi che il Property Manager si impegna a fornire agli Ospiti, in nome e per conto del Mandante, sono:"
C[57]=rep(57,"nonché riscossione dell’imposta di soggiorno con contestuale emissione","nonché richiesta del pagamento dell’imposta di soggiorno con emissione")
C[88]="I corrispettivi delle locazioni, sia brevi sia di media durata, sono incassati direttamente dal Mandante ai sensi dell’art. 10. Il Property Manager non incassa canoni di locazione per conto del Mandante."
A[88]=[{"text":"Gli annunci pubblicati sulle piattaforme di prenotazione e i relativi account restano intestati al Mandante, che ne conserva la titolarità, ivi comprese le recensioni ricevute. Il Mandante concede al Property Manager l’accesso a tali account, in qualità di co-host o di utente autorizzato, per tutta la durata del Contratto; alla cessazione del Contratto il Property Manager restituisce al Mandante la gestione esclusiva degli annunci, fermo quanto previsto dall’art. 17.","like":88}]
C[89]=None
C[92]="In particolare, per ogni prenotazione il Property Manager emette, in nome e per conto del Mandante, la fattura o altro documento fiscale del Mandante all’Ospite, ove richiesto dalla normativa, secondo il regime IVA applicabile ai canoni, che il Mandante comunica per iscritto al Property Manager prima dell’avvio delle locazioni. L’importo di tale documento è pari al corrispettivo complessivo pagato dall’Ospite, esclusa l’imposta di soggiorno."
C[93]=None; C[94]=None
C[100]=rep(100,"che gestisce ai sensi dell’art. 12","che il conduttore versa direttamente al Mandante")
C[120]="Incassi, fatturazione e pagamenti"
C[122]="Al termine di ciascun mese solare il Property Manager emette fattura al Mandante per il compenso di cui all’art. 11 maturato sui pernottamenti del mese, oltre IVA, unitamente agli eventuali costi a carico del Mandante sostenuti dal Property Manager nel medesimo mese, e mette a disposizione il rendiconto delle prenotazioni di cui all’art. 4. Il Mandante provvede al pagamento entro 15 (quindici) giorni dal ricevimento della fattura."
C[123]="Detti pagamenti sono effettuati mediante bonifico bancario sul c/c intestato al Property Manager al seguente IBAN: _______________________________"
C[124]="I costi sostenuti dal Property Manager per conto del Mandante sono addebitati nella fattura mensile verso presentazione del relativo giustificativo. Eventuali contestazioni del Mandante in merito alle spese addebitate dovranno pervenire, per iscritto, al Property Manager entro e non oltre il termine di 30 giorni dalla presentazione dei giustificativi."
C[130]=None
C[137]=rep(137,"dei versamenti da lui dovuti in forza di Contratto a Pubbliche Amministrazioni (ad es: imposta di soggiorno) anche di natura fiscale (ad es.: ritenute di legge ove previste) ed in genere dei pagamenti o prestazioni dovute a terzi in forza di Contratto.","delle dichiarazioni relative all’imposta di soggiorno poste a suo carico dal presente Contratto ed in genere delle prestazioni dovute a terzi in forza di Contratto.")
C[139]=None
C[175]=rep(175,"Può essere trattenuto dalle somme da versare al Mandante ai sensi dell’art. 10.","È fatturato dal Property Manager e pagato dal Mandante ai sensi dell’art. 10.")
C[176]=rep(176,"di versamento delle somme maturate","di fatturazione e pagamento dei compensi maturati")
C[185]=None
C[192]="la mancata messa a disposizione dell’Immobile e degli accessi agli account delle piattaforme di prenotazione entro 10 giorni dalla ricezione della lettera di messa in mora;"
C[196]=None

FEE_DEF=" Per “Costo del Pernottamento”"+T[128].split(" Per “Costo del Pernottamento”")[1]
def fee(pct,word,extra=""):
    return f"Per l’attività di gestione e per i servizi di cui all’art. 2, al Property Manager spetta un compenso pari al {pct}% ({word} per cento) del Costo del Pernottamento di ciascuna prenotazione{extra}, oltre IVA."+FEE_DEF

# Gestione completa (Edil)
E=dict(C)
E[118]="Il Mandante autorizza espressamente il Property Manager ad avvalersi, per lo svolgimento delle attività tecniche, operative, fiscali e contabili oggetto del presente Contratto, di collaboratori e soggetti terzi (a titolo esemplificativo: addetti alle pulizie, lavanderie, manutentori, consulenti), ognuno per quanto di competenza. Il Property Manager risponde dell’operato di tali soggetti come del fatto proprio. I relativi costi sono a carico del Property Manager, ad eccezione di quelli che il presente Contratto pone a carico del Mandante, ossia i servizi di pulizia, biancheria e lavanderia (art. 11), le manutenzioni (art. 13) e gli Interventi in Loco nei casi previsti dall’art. 14. Le commissioni delle piattaforme di prenotazione sono sostenute direttamente dal Mandante."
E[121]="I canoni di locazione, gli eventuali depositi cauzionali e ogni altra somma pagata dagli Ospiti sono incassati direttamente dal Mandante, tramite le piattaforme di prenotazione su account a lui intestati ovvero sul conto corrente a lui intestato. Il Mandante restituisce i depositi cauzionali al termine del rapporto, previa verifica dei locali da parte del Property Manager e sulla base delle sue indicazioni."
E[128]=fee(20,"venti")
E[129]="Restano a carico del Mandante tutti i costi, ordinari e straordinari, relativi all’Immobile e alla sua gestione, tra cui, a titolo esemplificativo: le commissioni delle piattaforme di prenotazione e dei sistemi di pagamento, che il Mandante sostiene direttamente; i servizi di pulizia, biancheria e lavanderia; i prodotti di cortesia e i materiali di consumo; le manutenzioni di cui all’art. 13; gli Interventi in Loco a carico del Mandante ai sensi dell’art. 14. I costi sostenuti dal Property Manager per conto del Mandante sono addebitati nella fattura mensile ai sensi dell’art. 10 e dettagliati nel rendiconto mensile di cui all’art. 4."
E[136]="È altresì responsabile della richiesta del deposito cauzionale o di idonee garanzie previste per le locazioni di media durata, nonché dello svolgimento delle attività di controllo previste nella fase di check-out. Il Property Manager risponde degli eventuali danni o ammanchi che avrebbe potuto rilevare e contestare all’Ospite mediante l’ordinaria diligenza richiesta nell’esecuzione dell’incarico e che non siano stati rilevati o contestati per sua negligenza."
E[149]=rep(149,"Tale importo potrà essere trattenuto dalle somme da versare al Mandante ai sensi dell’art. 10.","Tale importo è addebitato nella fattura mensile ai sensi dell’art. 10.")
E[164]=rep(164,"possono essere trattenuti dalle somme da versare al Mandante ai sensi dell’art. 10.","sono addebitati nella fattura mensile ai sensi dell’art. 10.")

# Gestione da remoto (Alex, Ilaria)
R=dict(C)
R[33]="curare, sulla base del materiale fotografico e video fornito dal Mandante o realizzato da professionisti da lui incaricati, ogni attività utile al fine dell’efficace promozione dell’Immobile su canali online e offline;"
R[34]=rep(34,"corredati da foto tratte dal book fotografico e,","corredati dal materiale fotografico disponibile e,").replace("su diverse piattaforme online e/o sul proprio sito internet;","sugli account intestati al Mandante presso le diverse piattaforme online, nonché sul proprio sito internet;")
R[50]=None
R[51]=rep(51,", trasmettendo il relativo preventivo secondo quanto previsto dall’art. 13;",", secondo quanto previsto dall’art. 13;")
R[59]=rep(59,"dal personale addetto alle pulizie,","dal personale addetto alle pulizie incaricato dal Mandante,")
R[60]=None; R[61]=None
R[62]="Eventuali servizi extra richiesti dagli Ospiti quali, a mero titolo esemplificativo, organizzazione di servizi di trasferimento, di visite guidate e di altre esperienze; le pulizie o i cambi di biancheria durante il soggiorno sono organizzati in coordinamento con il personale incaricato dal Mandante."
R[75]="Il Mandante garantisce che le chiavi o i dispositivi di accesso all’Immobile siano messi a disposizione degli Ospiti secondo le modalità concordate con il Property Manager (a titolo esemplificativo: cassetta di sicurezza, serratura elettronica) e comunica tempestivamente al Property Manager i relativi codici e ogni loro variazione."
R[118]="Il Mandante autorizza espressamente il Property Manager ad avvalersi, per lo svolgimento delle attività tecniche, operative, fiscali e contabili oggetto del presente Contratto, di collaboratori e soggetti terzi (a titolo esemplificativo: consulenti, fornitori di servizi informatici), ognuno per quanto di competenza. Il Property Manager risponde dell’operato di tali soggetti come del fatto proprio. I relativi costi sono a carico del Property Manager. Restano a carico del Mandante, che li sostiene direttamente, i servizi di pulizia, biancheria e lavanderia, le commissioni delle piattaforme di prenotazione e le manutenzioni (art. 13)."
R[121]="I canoni di locazione, gli eventuali depositi cauzionali e ogni altra somma pagata dagli Ospiti sono incassati direttamente dal Mandante, tramite le piattaforme di prenotazione su account a lui intestati ovvero sul conto corrente a lui intestato. Il Mandante restituisce i depositi cauzionali al termine del rapporto, previa verifica dei locali da parte del personale da lui incaricato."
R[129]="Restano a carico del Mandante, che li sostiene direttamente, tutti i costi, ordinari e straordinari, relativi all’Immobile e alla sua gestione, tra cui, a titolo esemplificativo: le commissioni delle piattaforme di prenotazione e dei sistemi di pagamento; i servizi di pulizia, biancheria e lavanderia, svolti da personale da lui incaricato; i prodotti di cortesia e i materiali di consumo; le manutenzioni di cui all’art. 13. Gli eventuali costi sostenuti dal Property Manager per conto del Mandante sono addebitati nella fattura mensile ai sensi dell’art. 10 e dettagliati nel rendiconto mensile di cui all’art. 4."
R[136]="È altresì responsabile della richiesta del deposito cauzionale o di idonee garanzie previste per le locazioni di media durata. Le verifiche dello stato dell’Immobile al check-out sono svolte dal personale incaricato dal Mandante; il Property Manager risponde della tempestiva contestazione all’Ospite e alle piattaforme di prenotazione dei danni o ammanchi che tale personale gli abbia segnalato."
R[148]="Ogni intervento di manutenzione deve essere preventivamente concordato con il Mandante. Il Property Manager, rilevata direttamente o su segnalazione degli Ospiti la necessità di un intervento, ne dà tempestiva comunicazione al Mandante, che provvede a far eseguire l’intervento a propria cura e spese tramite fornitori di propria fiducia. Il Property Manager si coordina con il Mandante e con i fornitori per l’accesso all’Immobile compatibilmente con le prenotazioni in corso."
R[149]=None
R[150]="Restano in ogni caso a carico del Mandante le conseguenze della mancata o ritardata esecuzione degli interventi necessari (a titolo esemplificativo: rimborsi o indennizzi riconosciuti agli Ospiti, cancellazioni, blocco del calendario)."
R[151]="Nei soli casi di urgenza, ossia quando il ritardo potrebbe causare pericolo per persone o cose, danni all’Immobile o compromettere l’utilizzo dell’Immobile da parte degli Ospiti presenti (a titolo esemplificativo: perdite d’acqua, guasti agli impianti elettrico, idraulico o di riscaldamento), e il Mandante non sia raggiungibile in tempo utile, il Property Manager è autorizzato a contattare i fornitori indicati dal Mandante o, in mancanza, fornitori locali, per disporre gli interventi strettamente necessari fino a un importo massimo di euro 200,00 (duecento/00) per singolo intervento, dandone tempestiva comunicazione al Mandante. Tali costi sono a carico del Mandante e gli sono fatturati direttamente dal fornitore."
R[153]="Servizi in loco e accesso degli Ospiti"
R[154]="Il servizio affidato al Property Manager è svolto interamente da remoto e non comprende interventi presso l’Immobile, né i servizi di pulizia, biancheria e lavanderia, che restano a cura e spese del Mandante, direttamente o tramite personale da lui incaricato. Il Mandante comunica al Property Manager i recapiti di un referente locale reperibile durante i soggiorni."
R[155]="In caso di problemi di accesso degli Ospiti all’Immobile o di altre esigenze che richiedano la presenza presso l’Immobile, il Property Manager assiste l’Ospite da remoto e ne dà immediata comunicazione al referente locale del Mandante, che provvede all’intervento. I relativi costi sono a carico del Mandante, salvo che il problema derivi da comportamento negligente del Property Manager (a titolo esemplificativo: la comunicazione all’Ospite di istruzioni o codici di accesso errati o incompleti), nel qual caso i costi dell’intervento sono a carico del Property Manager."
R[156]="Resta salvo il diritto di rivalsa nei confronti dell’Ospite responsabile, anche mediante le procedure di rimborso previste dalle piattaforme di prenotazione."
for i in range(157,165): R[i]=None
R[229]="14) Servizi in loco e accesso degli Ospiti;"

def units(n):
    word={2:"due",4:"quattro"}[n]
    u="; ".join(f"({k}) sita in ______________________ (____), Via ______________________ n. ____, interno ____, piano ____, NCEU del Comune di ______________________ Foglio ____, Mapp. ____, Sub. ____, Cat. ____" for k in range(1,n+1))
    return f"Il Mandante è proprietario (ovvero titolare di altro diritto reale o personale di godimento) delle seguenti {n} ({word}) unità immobiliari, ciascuna oggetto di un distinto annuncio sulle piattaforme di prenotazione (di seguito, singolarmente e congiuntamente, l’“Immobile”, intendendosi ogni riferimento all’Immobile contenuto nel presente Contratto riferito a ciascuna di esse): {u};"

AL=dict(R); AL[10]=units(4)
AL[127]=rep(127,"servizio fotografico, creazione e ottimizzazione degli annunci","ottimizzazione degli annunci, configurazione del gestionale")
AL[128]=fee(10,"dieci")+" Al Property Manager spetta inoltre, per l’utilizzo del gestionale Kross Booking, un canone mensile di euro 9,00 (nove/00) oltre IVA per ciascun annuncio gestito, pari a complessivi euro 36,00 (trentasei/00) oltre IVA al mese per i 4 (quattro) annunci gestiti alla data di sottoscrizione, fatturato con il compenso mensile ai sensi dell’art. 10."

IL=dict(R); IL[10]=units(2)
IL[127]=rep(127,"servizio fotografico, creazione e ottimizzazione degli annunci","ottimizzazione degli annunci, migrazione al gestionale Kross Booking")
IL[128]=fee(10,"dieci"," relativa ai 2 (due) annunci gestiti")
IA=dict(A)
IA[69]=[{"text":"All’avvio della gestione il Property Manager cura il passaggio dal gestionale attualmente utilizzato dal Mandante al gestionale Kross Booking, trasferendo annunci, calendari, tariffe e prenotazioni in essere in modo da garantire la continuità delle prenotazioni. Il Mandante collabora fornendo gli accessi e le informazioni necessari e, completato il passaggio, può consultare i dati delle prenotazioni tramite il Portale Proprietari di cui al comma precedente.","like":69}]
IA[115]=[{"text":"Il Property Manager cura la comunicazione con il consulente fiscale indicato dal Mandante, al quale trasmette con cadenza mensile i dati e la documentazione relativi alle prenotazioni, agli incassi, alle commissioni delle piattaforme di prenotazione, all’imposta di soggiorno e ai compensi del Property Manager, e con il quale si coordina affinché tutti gli adempimenti fiscali connessi alle locazioni siano assolti correttamente e nei termini. Restano in capo al Mandante e al suo consulente fiscale la tenuta della contabilità e la presentazione delle dichiarazioni fiscali.","like":115}]

for name,sets,aft in [("Edil_Valtellina",E,A),("Alex_Biancotti",AL,A),("Ilaria_Negri",IL,IA)]:
    json.dump({"set":{str(k):v for k,v in sets.items()},"after":{str(k):v for k,v in aft.items()}},open(f"{S}/clienti_az/{name}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")
