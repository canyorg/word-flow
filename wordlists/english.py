# -*- coding: utf-8 -*-
"""English word lists.

DAILY / ACADEMIC : level -> lines "type|English|Turkish|hint"
         type: n = noun, v = verb, a = adjective, d = adverb / linker, p = phrase / phrasal verb
EN_DE / EN_DE_ACADEMIC : English -> German meaning (academic overrides daily)
"""

# tür|English|Türkçe|ek bilgi (düzensiz fiil / kalıp)
#   n = isim, v = fiil, a = sıfat, d = zarf / bağlaç, p = kalıp / phrasal verb
DAILY = {
"A1.1": """
n|family|aile
n|friend|arkadaş
n|house|ev
n|water|su
n|bread|ekmek
n|day|gün
n|week|hafta
n|city|şehir
n|country|ülke
n|name|isim, ad
n|child|çocuk|çoğul: children
v|be|olmak|am / is / are · was / were · been
v|have|sahip olmak, -si olmak|has · had · had
v|go|gitmek|went · gone
v|come|gelmek|came · come
v|eat|yemek yemek|ate · eaten
v|drink|içmek|drank · drunk
v|live|yaşamak, oturmak
v|speak|konuşmak|spoke · spoken
v|like|sevmek, hoşlanmak
a|big|büyük
a|small|küçük
a|good|iyi
a|happy|mutlu
d|today|bugün
""",
"A1.2": """
n|kitchen|mutfak
n|room|oda
n|table|masa
n|chair|sandalye
n|money|para
n|price|fiyat
n|shop|dükkân
n|vegetable|sebze
n|breakfast|kahvaltı
n|bus stop|otobüs durağı
v|buy|satın almak|bought · bought
v|sleep|uyumak|slept · slept
v|work|çalışmak
v|read|okumak|read · read (okunuşu: /red/)
v|write|yazmak|wrote · written
v|need|ihtiyacı olmak
v|want|istemek
v|open|açmak
v|close|kapatmak
v|wait|beklemek|wait for sb
a|cheap|ucuz
a|expensive|pahalı
a|tired|yorgun
d|always|her zaman
d|tomorrow|yarın
""",
"A2.1": """
n|appointment|randevu
n|bill|fatura, hesap
n|holiday|tatil
n|weather|hava durumu
n|neighbour|komşu
n|key|anahtar
n|rent|kira
n|headache|baş ağrısı
n|pharmacy|eczane
n|ticket|bilet
v|call|aramak (telefonla)
v|forget|unutmak|forgot · forgotten
v|pay|ödemek|paid · paid
v|meet|buluşmak, tanışmak|met · met
v|stay|kalmak
v|know|bilmek, tanımak|knew · known
v|think|düşünmek|thought · thought
v|help|yardım etmek
p|get up|(yataktan) kalkmak|got up
p|look for|(bir şeyi) aramak
a|busy|meşgul
a|sick|hasta
a|fast|hızlı
d|unfortunately|maalesef
d|usually|genellikle
""",
"A2.2": """
n|experience|deneyim
n|job application|iş başvurusu
n|salary|maaş
n|contract|sözleşme
n|exam|sınav
n|difference|fark
n|opinion|görüş, fikir
n|solution|çözüm
n|feeling|his, duygu
n|environment|çevre
v|explain|açıklamak
v|understand|anlamak|understood · understood
v|decide|karar vermek
v|lose|kaybetmek|lost · lost
v|win|kazanmak|won · won
v|prepare|hazırlamak
v|move|taşınmak; hareket etmek
p|find out|öğrenmek, ortaya çıkarmak|found out
p|give up|vazgeçmek, bırakmak|gave up · given up
p|look forward to|dört gözle beklemek|+ -ing
a|important|önemli
a|satisfied|memnun
a|on time|zamanında
d|quite|oldukça
d|recently|son zamanlarda
""",
"B1.1": """
n|requirement|gereklilik, şart
n|opportunity|fırsat
n|responsibility|sorumluluk
n|insurance|sigorta
n|advantage|avantaj
n|disadvantage|dezavantaj
n|reason|sebep
n|result|sonuç
n|goal|hedef
n|behaviour|davranış
v|apply for|başvurmak
v|complain|şikâyet etmek|complain about sth
v|recommend|tavsiye etmek
v|compare|karşılaştırmak
v|describe|tarif etmek, betimlemek
v|improve|geliştirmek
v|avoid|kaçınmak|+ -ing
v|achieve|başarmak, ulaşmak
p|deal with|ilgilenmek, başa çıkmak|dealt with
p|get used to|alışmak|+ -ing
p|take part in|katılmak|took part · taken part
a|honest|dürüst
a|careful|dikkatli
d|therefore|bu nedenle
d|however|ancak
""",
"B1.2": """
n|expectation|beklenti
n|challenge|zorluk, meydan okuma
n|skill|beceri
n|success|başarı
n|relationship|ilişki
n|argument|tartışma; argüman
n|exception|istisna
n|advertisement|reklam
n|customer|müşteri
n|purpose|amaç
v|rely on|güvenmek, bel bağlamak
v|apologise|özür dilemek|apologise for sth
v|convince|ikna etmek
v|claim|iddia etmek
v|postpone|ertelemek
v|depend on|bağlı olmak
v|increase|artmak, artırmak
v|reduce|azaltmak
p|put off|ertelemek|put off · put off
p|carry on|devam etmek
p|run out of|tükenmek, bitmek|ran out · run out
a|curious|meraklı
a|reliable|güvenilir
d|actually|aslında
d|eventually|sonunda
""",
"B2.1": """
n|impact|etki
n|measure|önlem
n|effort|çaba
n|condition|koşul
n|demand|talep
n|attitude|tutum
n|prejudice|önyargı
n|competition|rekabet
n|sustainability|sürdürülebilirlik
v|contribute|katkıda bulunmak|contribute to sth
v|consider|göz önünde bulundurmak
v|overcome|üstesinden gelmek|overcame · overcome
v|enable|mümkün kılmak
v|influence|etkilemek
v|notice|fark etmek
v|refuse|reddetmek|refuse to do sth
p|come up with|(fikir) bulmak|came up with
p|turn down|reddetmek
p|point out|belirtmek, dikkat çekmek
a|obvious|apaçık
a|sufficient|yeterli
a|reasonable|makul
d|nevertheless|buna rağmen
d|apparently|görünüşe göre
""",
"B2.2": """
n|basis|temel
n|addiction|bağımlılık
n|perception|algı
n|restriction|kısıtlama
n|agreement|anlaşma
n|willingness|isteklilik
n|decline|düşüş
n|implementation|uygulama, hayata geçirme
v|emphasise|vurgulamak
v|estimate|tahmin etmek
v|reject|reddetmek
v|contradict|çelişmek; itiraz etmek
v|assume|varsaymak
p|take over|devralmak, üstlenmek|took over · taken over
p|make up for|telafi etmek|made up for
p|get away with|(cezasız) sıyrılmak|got away with
p|look into|incelemek, araştırmak
p|figure out|çözmek, anlamak
a|inevitable|kaçınılmaz
a|considerable|kayda değer
a|reluctant|isteksiz
a|aware|farkında|aware of sth
d|largely|büyük ölçüde
d|if necessary|gerekirse
""",
"C1.1": """
n|assumption|varsayım
n|approach|yaklaşım
n|authority|yetki; otorite
n|suspicion|şüphe
n|recognition|tanınma; takdir
n|misuse|kötüye kullanım
n|vulnerability|zafiyet, savunmasızlık
n|threat|tehdit
n|upturn|toparlanma, yükseliş
v|tackle|(sorunu) ele almak
v|undermine|baltalamak
v|prompt|tetiklemek, yol açmak
v|resolve|çözmek
v|imply|ima etmek
v|acknowledge|kabul etmek
v|strive|çabalamak|strove · striven
p|weigh up|ölçüp biçmek
p|stem from|-den kaynaklanmak
p|bring about|yol açmak|brought about
a|decisive|belirleyici
a|lasting|kalıcı
a|tentative|geçici, deneme niteliğinde
a|compelling|ikna edici, çarpıcı
d|arguably|muhtemelen, tartışmaya açık olsa da
""",
"C1.2": """
n|objection|itiraz
n|scope|kapsam
n|leeway|hareket alanı, esneklik
n|concern|endişe; mesele
n|extent|ölçü, derece
n|hurdle|engel
n|compromise|uzlaşma
v|criticise|eleştirmek
v|pursue|peşinden gitmek, sürdürmek
v|resort to|(çare olarak) başvurmak
v|counteract|karşı koymak
v|address|(sorunu) ele almak
v|question|sorgulamak
p|turn out|ortaya çıkmak|it turned out that…
p|put up with|katlanmak
p|come across|rastlamak|came across
p|rule out|ihtimal dışı bırakmak
a|unavoidable|kaçınılmaz
a|appropriate|uygun
a|relevant|ilgili, alakalı
a|thorough|titiz, kapsamlı
d|anyway|zaten, neyse
d|by and large|genel olarak
""",
"C2.1": """
n|bias|önyargı, taraflılık
n|dilemma|ikilem
n|ulterior motive|art niyet
n|change of heart|fikir değişikliği
n|negligence|ihmal
n|undertaking|girişim, üstlenilen iş
v|denounce|kınamak
v|substantiate|kanıtlamak
v|thwart|engellemek, boşa çıkarmak
v|contemplate|derin düşünmek, tasarlamak
v|loom|(tehdit gibi) belirmek
p|gloss over|üstünkörü geçmek
p|play down|önemsizmiş gibi göstermek
p|carry weight|önem taşımak
p|be on the fence|kararsız olmak
a|blunt|açık sözlü, dobra
a|glaring|bariz, göze batan
a|notwithstanding|-e rağmen
d|by no means|asla, hiçbir şekilde
d|to some extent|bir dereceye kadar
d|as far as possible|mümkün olduğunca
""",
"C2.2": """
n|window dressing|göz boyama
n|balancing act|denge kurma çabası
n|hair-splitting|kılı kırk yarma
n|pitfall|tuzak, gizli tehlike
n|fly in the ointment|işi bozan tek kusur
n|tunnel vision|dar bakış açısı
n|predicament|zor durum
p|go the extra mile|fazlasını yapmak
p|get the short end of the stick|kaybeden taraf olmak
p|sweep under the rug|halının altına süpürmek
p|beat around the bush|lafı dolandırmak
p|put your foot in it|pot kırmak
p|cut corners|işi baştan savma yapmak
p|bite the bullet|dişini sıkmak
p|hit the nail on the head|tam üstüne basmak
v|backfire|ters tepmek
v|snub|takmamak, yüz vermemek
v|equivocate|kaçamak konuşmak
a|terse|kısa ve sert
a|obsolete|modası geçmiş
a|vehement|şiddetli, ateşli
""",
}

# Akademik İngilizce (makale, tez, sunum dili) — ek bilgi: tipik kullanım
ACADEMIC = {
"B1.1": """
n|research|araştırma|conduct research
n|data|veri|collect / analyse data
n|method|yöntem
n|source|kaynak|cite a source
n|evidence|kanıt|provide evidence for
n|analysis|analiz|carry out an analysis
n|factor|etken|a key factor
n|process|süreç
n|structure|yapı
v|define|tanımlamak
v|identify|belirlemek, tespit etmek
v|indicate|göstermek, işaret etmek|results indicate that…
v|occur|meydana gelmek
v|require|gerektirmek
v|assess|değerlendirmek
v|establish|kurmak; ortaya koymak
a|significant|anlamlı, önemli|statistically significant
a|similar|benzer|similar to
a|specific|belirli, özgül
d|furthermore|ayrıca
d|for instance|örneğin
""",
"B1.2": """
n|concept|kavram
n|context|bağlam|in this context
n|framework|çerçeve|theoretical framework
n|hypothesis|hipotez|çoğul: hypotheses
n|outcome|sonuç, çıktı
n|participant|katılımcı
n|sample|örneklem|a sample of 200 students
n|survey|anket
n|variable|değişken
v|interpret|yorumlamak
v|demonstrate|göstermek, kanıtlamak
v|derive|türetmek, elde etmek|derive from
v|obtain|elde etmek
v|investigate|araştırmak, incelemek
a|relevant|ilgili, alakalı
a|consistent|tutarlı|consistent with
a|appropriate|uygun
d|consequently|sonuç olarak
d|in addition|ek olarak
d|whereas|-iken, oysa
""",
"B2.1": """
n|assumption|varsayım|underlying assumption
n|criterion|ölçüt|çoğul: criteria
n|implication|sonuç, çıkarım|implications for
n|limitation|sınırlılık|limitations of the study
n|perspective|bakış açısı
n|phenomenon|olgu|çoğul: phenomena
n|correlation|korelasyon, ilişki|correlation between X and Y
n|trend|eğilim
v|argue|savunmak, ileri sürmek|argue that…
v|illustrate|örneklemek
v|emphasise|vurgulamak
v|evaluate|değerlendirmek
v|clarify|açıklığa kavuşturmak
v|outline|ana hatlarıyla anlatmak
a|crucial|kritik, çok önemli
a|empirical|deneysel, ampirik|empirical evidence
a|subsequent|sonraki
d|thus|böylece
d|nevertheless|yine de
d|in contrast|buna karşın
""",
"B2.2": """
n|methodology|yöntembilim|research methodology
n|validity|geçerlilik
n|reliability|güvenilirlik
n|bias|yanlılık|sampling bias
n|literature|literatür|literature review
n|finding|bulgu|key findings
n|scope|kapsam|beyond the scope of this study
n|distribution|dağılım
v|attribute|atfetmek|attribute X to Y
v|constitute|oluşturmak
v|facilitate|kolaylaştırmak
v|generate|üretmek
v|undertake|üstlenmek, yürütmek|undertook · undertaken
v|justify|gerekçelendirmek
a|comprehensive|kapsamlı
a|preliminary|ön, ilk|preliminary results
a|qualitative|nitel
a|quantitative|nicel
d|respectively|sırasıyla
d|to a large extent|büyük ölçüde
""",
"C1.1": """
n|paradigm|paradigma
n|rationale|gerekçe|the rationale for
n|discourse|söylem
n|discrepancy|tutarsızlık|discrepancy between
n|feasibility|uygulanabilirlik|feasibility study
n|premise|öncül
n|inference|çıkarım|draw an inference
v|corroborate|doğrulamak, desteklemek
v|synthesise|sentezlemek
v|postulate|ileri sürmek, varsaymak
v|elucidate|aydınlatmak, açıklamak
v|delineate|sınırlarını çizmek
v|mitigate|hafifletmek, azaltmak|mitigate the risk
a|inherent|doğasında olan|inherent in
a|robust|sağlam|robust results
a|salient|göze çarpan, belirgin
a|ambiguous|belirsiz, çok anlamlı
d|notably|özellikle
d|conversely|tersine
d|hence|bu nedenle
""",
"C1.2": """
n|caveat|çekince, uyarı
n|nuance|nüans, ince fark
n|trajectory|seyir, gidişat
n|dichotomy|ikilik, ayrım
n|consensus|uzlaşı|reach a consensus
n|heuristic|sezgisel yöntem
v|underpin|temelini oluşturmak
v|reconcile|bağdaştırmak
v|extrapolate|genellemek, ileriye tahmin etmek
v|operationalise|ölçülebilir hale getirmek
v|scrutinise|titizlikle incelemek
v|refute|çürütmek
v|warrant|gerektirmek, haklı kılmak|warrants further research
a|pertinent|yerinde, ilgili
a|tenuous|zayıf (bağlantı)
a|pivotal|kilit, merkezi
a|rigorous|titiz
d|ostensibly|görünüşte
d|inter alia|diğerlerinin yanı sıra
d|albeit|-se de
""",
"C2.1": """
n|epistemology|epistemoloji, bilgi kuramı
n|ontology|ontoloji
n|hegemony|hegemonya
n|tautology|totoloji, gereksiz tekrar
n|corollary|doğal sonuç
n|lacuna|(literatürde) boşluk
v|problematise|sorunsallaştırmak
v|contextualise|bağlama oturtmak
v|engender|doğurmak, yol açmak
v|obfuscate|bulanıklaştırmak
v|preclude|engellemek, olanaksız kılmak
a|idiosyncratic|kendine özgü
a|reductive|indirgemeci
a|ubiquitous|her yerde bulunan
a|axiomatic|apaçık, aksiyomatik
a|tacit|örtük, söylenmeden kabul edilen
d|a fortiori|haydi haydi, evleviyetle
d|ipso facto|bizzat bu nedenle
d|mutatis mutandis|gerekli değişiklikler yapılarak
""",
"C2.2": """
n|heterogeneity|heterojenlik
n|reification|şeyleştirme
n|teleology|teleoloji, ereksellik
n|hermeneutics|yorumbilim
n|verisimilitude|gerçeğe benzerlik
n|praxis|pratik, uygulama
v|instantiate|somutlaştırmak, örneklemek
v|valorise|değer atfetmek, yüceltmek
v|interrogate|(eleştirel) sorgulamak
v|foreground|ön plana çıkarmak
v|elide|atlamak, görmezden gelmek
v|conflate|birbirine karıştırmak
v|vitiate|geçersiz kılmak, bozmak
a|recondite|anlaşılması güç
a|nascent|yeni filizlenen
a|polemical|polemik, tartışmacı
a|germane|konuyla ilgili
d|prima facie|ilk bakışta
d|ceteris paribus|diğer koşullar sabitken
""",
}


EN_DE = {
# daily A1.1
"family": "die Familie", "friend": "der Freund / die Freundin", "house": "das Haus",
"water": "das Wasser", "bread": "das Brot", "day": "der Tag", "week": "die Woche",
"city": "die Stadt", "country": "das Land", "name": "der Name", "child": "das Kind",
"be": "sein", "have": "haben", "go": "gehen", "come": "kommen", "eat": "essen",
"drink": "trinken", "live": "leben, wohnen", "speak": "sprechen", "like": "mögen, gern haben",
"big": "groß", "small": "klein", "good": "gut", "happy": "glücklich, froh", "today": "heute",
# A1.2
"kitchen": "die Küche", "room": "das Zimmer", "table": "der Tisch", "chair": "der Stuhl",
"money": "das Geld", "price": "der Preis", "shop": "das Geschäft, der Laden",
"vegetable": "das Gemüse", "breakfast": "das Frühstück", "bus stop": "die Bushaltestelle",
"buy": "kaufen", "sleep": "schlafen", "work": "arbeiten", "read": "lesen", "write": "schreiben",
"need": "brauchen", "want": "wollen", "open": "öffnen, aufmachen", "close": "schließen, zumachen",
"wait": "warten", "cheap": "billig, günstig", "expensive": "teuer", "tired": "müde",
"always": "immer", "tomorrow": "morgen",
# A2.1
"appointment": "der Termin", "bill": "die Rechnung", "holiday": "der Urlaub",
"weather": "das Wetter", "neighbour": "der Nachbar", "key": "der Schlüssel", "rent": "die Miete",
"headache": "die Kopfschmerzen (Pl.)", "pharmacy": "die Apotheke", "ticket": "die Fahrkarte, das Ticket",
"call": "anrufen", "forget": "vergessen", "pay": "bezahlen", "meet": "treffen, kennenlernen",
"stay": "bleiben", "know": "wissen, kennen", "think": "denken", "help": "helfen",
"get up": "aufstehen", "look for": "suchen", "busy": "beschäftigt", "sick": "krank",
"fast": "schnell", "unfortunately": "leider", "usually": "normalerweise, meistens",
# A2.2
"experience": "die Erfahrung", "job application": "die Bewerbung", "salary": "das Gehalt",
"contract": "der Vertrag", "exam": "die Prüfung", "difference": "der Unterschied",
"opinion": "die Meinung", "solution": "die Lösung", "feeling": "das Gefühl",
"environment": "die Umwelt", "explain": "erklären", "understand": "verstehen",
"decide": "entscheiden", "lose": "verlieren", "win": "gewinnen", "prepare": "vorbereiten",
"move": "umziehen; sich bewegen", "find out": "herausfinden", "give up": "aufgeben",
"look forward to": "sich freuen auf", "important": "wichtig", "satisfied": "zufrieden",
"on time": "pünktlich", "quite": "ziemlich", "recently": "neulich, in letzter Zeit",
# B1.1
"requirement": "die Anforderung, die Voraussetzung", "opportunity": "die Gelegenheit, die Chance",
"responsibility": "die Verantwortung", "insurance": "die Versicherung", "advantage": "der Vorteil",
"disadvantage": "der Nachteil", "reason": "der Grund", "result": "das Ergebnis", "goal": "das Ziel",
"behaviour": "das Verhalten", "apply for": "sich bewerben um", "complain": "sich beschweren",
"recommend": "empfehlen", "compare": "vergleichen", "describe": "beschreiben",
"improve": "verbessern", "avoid": "vermeiden", "achieve": "erreichen", "deal with": "sich kümmern um",
"get used to": "sich gewöhnen an", "take part in": "teilnehmen an", "honest": "ehrlich",
"careful": "vorsichtig", "therefore": "deshalb, daher", "however": "jedoch, allerdings",
# B1.2
"expectation": "die Erwartung", "challenge": "die Herausforderung", "skill": "die Fähigkeit",
"success": "der Erfolg", "relationship": "die Beziehung", "argument": "der Streit; das Argument",
"exception": "die Ausnahme", "advertisement": "die Werbung, die Anzeige", "customer": "der Kunde",
"purpose": "der Zweck", "rely on": "sich verlassen auf", "apologise": "sich entschuldigen",
"convince": "überzeugen", "claim": "behaupten", "postpone": "verschieben", "depend on": "abhängen von",
"increase": "steigen, erhöhen", "reduce": "reduzieren, verringern", "put off": "aufschieben",
"carry on": "weitermachen", "run out of": "ausgehen (es geht mir aus)", "curious": "neugierig",
"reliable": "zuverlässig", "actually": "eigentlich", "eventually": "schließlich, letztendlich",
# B2.1
"impact": "die Auswirkung", "measure": "die Maßnahme", "effort": "die Mühe, der Aufwand",
"condition": "die Bedingung", "demand": "die Forderung; die Nachfrage", "attitude": "die Einstellung",
"prejudice": "das Vorurteil", "competition": "der Wettbewerb", "sustainability": "die Nachhaltigkeit",
"contribute": "beitragen", "consider": "berücksichtigen; in Betracht ziehen", "overcome": "überwinden",
"enable": "ermöglichen", "influence": "beeinflussen", "notice": "bemerken",
"refuse": "sich weigern, ablehnen", "come up with": "sich einfallen lassen",
"turn down": "ablehnen", "point out": "hinweisen auf", "obvious": "offensichtlich",
"sufficient": "ausreichend", "reasonable": "vernünftig, angemessen", "nevertheless": "dennoch",
"apparently": "anscheinend",
# B2.2
"basis": "die Grundlage", "addiction": "die Sucht", "perception": "die Wahrnehmung",
"restriction": "die Einschränkung", "agreement": "die Vereinbarung", "willingness": "die Bereitschaft",
"decline": "der Rückgang", "implementation": "die Umsetzung", "emphasise": "betonen, hervorheben",
"estimate": "schätzen", "reject": "ablehnen", "contradict": "widersprechen", "assume": "annehmen",
"take over": "übernehmen", "make up for": "wiedergutmachen, ausgleichen",
"get away with": "ungestraft davonkommen", "look into": "untersuchen, prüfen",
"figure out": "herausfinden, kapieren", "inevitable": "unvermeidlich", "considerable": "erheblich",
"reluctant": "widerwillig", "aware": "bewusst", "largely": "weitgehend", "if necessary": "gegebenenfalls",
# C1.1
"assumption": "die Annahme", "approach": "der Ansatz", "authority": "die Befugnis; die Behörde",
"suspicion": "der Verdacht", "recognition": "die Anerkennung", "misuse": "der Missbrauch",
"vulnerability": "die Schwachstelle, die Verwundbarkeit", "threat": "die Bedrohung",
"upturn": "der Aufschwung", "tackle": "angehen, in Angriff nehmen", "undermine": "untergraben",
"prompt": "veranlassen, auslösen", "resolve": "lösen, beheben", "imply": "andeuten, implizieren",
"acknowledge": "anerkennen, einräumen", "strive": "streben", "weigh up": "abwägen",
"stem from": "herrühren von", "bring about": "herbeiführen, bewirken", "decisive": "entscheidend",
"lasting": "dauerhaft, nachhaltig", "tentative": "vorläufig, zögerlich",
"compelling": "überzeugend, zwingend", "arguably": "wohl, möglicherweise",
# C1.2
"objection": "der Einwand", "scope": "der Umfang, der Rahmen", "leeway": "der Spielraum",
"concern": "die Sorge; das Anliegen", "extent": "das Ausmaß", "hurdle": "die Hürde",
"compromise": "der Kompromiss", "criticise": "kritisieren, bemängeln", "pursue": "verfolgen",
"resort to": "zurückgreifen auf", "counteract": "entgegenwirken", "address": "ansprechen, angehen",
"question": "hinterfragen", "turn out": "sich herausstellen", "put up with": "sich abfinden mit, ertragen",
"come across": "stoßen auf", "rule out": "ausschließen", "unavoidable": "unumgänglich",
"appropriate": "angemessen", "relevant": "relevant, einschlägig", "thorough": "gründlich",
"anyway": "ohnehin, sowieso", "by and large": "im Großen und Ganzen",
# C2.1
"bias": "die Voreingenommenheit", "dilemma": "die Zwickmühle, das Dilemma",
"ulterior motive": "der Hintergedanke", "change of heart": "der Sinneswandel",
"negligence": "die Fahrlässigkeit", "undertaking": "das Unterfangen", "denounce": "anprangern",
"substantiate": "untermauern", "thwart": "vereiteln", "contemplate": "erwägen",
"loom": "drohen, sich abzeichnen", "gloss over": "beschönigen", "play down": "verharmlosen",
"carry weight": "ins Gewicht fallen", "be on the fence": "unentschlossen sein",
"blunt": "unverblümt", "glaring": "eklatant", "notwithstanding": "ungeachtet",
"by no means": "mitnichten, keineswegs", "to some extent": "gewissermaßen, in gewissem Maße",
"as far as possible": "tunlichst, möglichst",
# C2.2
"window dressing": "die Augenwischerei", "balancing act": "der Spagat, die Gratwanderung",
"hair-splitting": "die Haarspalterei", "pitfall": "der Fallstrick", "fly in the ointment": "der Wermutstropfen",
"tunnel vision": "der Tunnelblick", "predicament": "die Bredouille, die Zwangslage",
"go the extra mile": "sich ins Zeug legen", "get the short end of the stick": "den Kürzeren ziehen",
"sweep under the rug": "unter den Teppich kehren", "beat around the bush": "um den heißen Brei herumreden",
"put your foot in it": "ins Fettnäpfchen treten", "cut corners": "pfuschen, schludern",
"bite the bullet": "in den sauren Apfel beißen", "hit the nail on the head": "den Nagel auf den Kopf treffen",
"backfire": "nach hinten losgehen", "snub": "brüskieren", "equivocate": "ausweichend antworten, lavieren",
"terse": "knapp, lapidar", "obsolete": "veraltet, obsolet", "vehement": "vehement, heftig",
}

# Akademik listede aynı kelime farklı/ek anlamla geçiyorsa burada üzerine yazılır
EN_DE_ACADEMIC = {
# B1.1
"research": "die Forschung", "data": "die Daten (Pl.)", "method": "die Methode", "source": "die Quelle",
"evidence": "der Nachweis, die Belege (Pl.)", "analysis": "die Analyse", "factor": "der Faktor",
"process": "der Prozess", "structure": "die Struktur", "define": "definieren", "identify": "identifizieren, ermitteln",
"indicate": "hindeuten auf, zeigen", "occur": "auftreten", "require": "erfordern", "assess": "bewerten, beurteilen",
"establish": "feststellen; etablieren", "significant": "signifikant, bedeutend", "similar": "ähnlich",
"specific": "spezifisch", "furthermore": "darüber hinaus", "for instance": "beispielsweise",
# B1.2
"concept": "der Begriff, das Konzept", "context": "der Kontext", "framework": "der Rahmen",
"hypothesis": "die Hypothese", "outcome": "das Ergebnis", "participant": "der Teilnehmer, die Teilnehmerin",
"sample": "die Stichprobe", "survey": "die Umfrage", "variable": "die Variable", "interpret": "interpretieren",
"demonstrate": "nachweisen, zeigen", "derive": "ableiten", "obtain": "erhalten, gewinnen",
"investigate": "untersuchen", "relevant": "relevant", "consistent": "übereinstimmend, konsistent",
"appropriate": "angemessen, geeignet", "consequently": "folglich", "in addition": "zusätzlich",
"whereas": "während, wohingegen",
# B2.1
"assumption": "die Annahme", "criterion": "das Kriterium", "implication": "die Implikation, die Folgerung",
"limitation": "die Einschränkung, die Limitation", "perspective": "die Perspektive", "phenomenon": "das Phänomen",
"correlation": "die Korrelation", "trend": "der Trend, die Tendenz", "argue": "argumentieren",
"illustrate": "veranschaulichen", "emphasise": "betonen", "evaluate": "evaluieren, auswerten",
"clarify": "klären", "outline": "skizzieren", "crucial": "entscheidend", "empirical": "empirisch",
"subsequent": "nachfolgend", "thus": "somit", "nevertheless": "dennoch", "in contrast": "im Gegensatz dazu",
# B2.2
"methodology": "die Methodik", "validity": "die Validität, die Gültigkeit", "reliability": "die Reliabilität, die Zuverlässigkeit",
"bias": "die Verzerrung", "literature": "die Fachliteratur", "finding": "der Befund, das Ergebnis",
"scope": "der Rahmen, der Umfang", "distribution": "die Verteilung", "attribute": "zuschreiben",
"constitute": "darstellen, bilden", "facilitate": "erleichtern", "generate": "erzeugen",
"undertake": "durchführen", "justify": "begründen", "comprehensive": "umfassend",
"preliminary": "vorläufig", "qualitative": "qualitativ", "quantitative": "quantitativ",
"respectively": "beziehungsweise, jeweils", "to a large extent": "in hohem Maße",
# C1.1
"paradigm": "das Paradigma", "rationale": "die Begründung", "discourse": "der Diskurs",
"discrepancy": "die Diskrepanz", "feasibility": "die Machbarkeit", "premise": "die Prämisse",
"inference": "die Schlussfolgerung", "corroborate": "bestätigen, erhärten", "synthesise": "synthetisieren",
"postulate": "postulieren", "elucidate": "erläutern", "delineate": "abgrenzen, umreißen",
"mitigate": "mindern, abschwächen", "inherent": "inhärent", "robust": "robust", "salient": "hervorstechend",
"ambiguous": "mehrdeutig", "notably": "insbesondere", "conversely": "umgekehrt", "hence": "daher",
# C1.2
"caveat": "der Vorbehalt", "nuance": "die Nuance", "trajectory": "der Verlauf", "dichotomy": "die Dichotomie",
"consensus": "der Konsens", "heuristic": "die Heuristik", "underpin": "untermauern",
"reconcile": "in Einklang bringen", "extrapolate": "extrapolieren", "operationalise": "operationalisieren",
"scrutinise": "genau prüfen", "refute": "widerlegen", "warrant": "rechtfertigen", "pertinent": "einschlägig, sachdienlich",
"tenuous": "dürftig, schwach", "pivotal": "zentral, ausschlaggebend", "rigorous": "streng, rigoros",
"ostensibly": "angeblich, vordergründig", "inter alia": "unter anderem", "albeit": "wenn auch",
# C2.1
"epistemology": "die Erkenntnistheorie", "ontology": "die Ontologie", "hegemony": "die Hegemonie",
"tautology": "die Tautologie", "corollary": "die logische Folge", "lacuna": "die Forschungslücke",
"problematise": "problematisieren", "contextualise": "kontextualisieren", "engender": "hervorrufen",
"obfuscate": "verschleiern", "preclude": "ausschließen", "idiosyncratic": "eigentümlich, idiosynkratisch",
"reductive": "reduktionistisch", "ubiquitous": "allgegenwärtig", "axiomatic": "selbstverständlich, axiomatisch",
"tacit": "stillschweigend", "a fortiori": "erst recht", "ipso facto": "eo ipso, eben dadurch",
"mutatis mutandis": "sinngemäß",
# C2.2
"heterogeneity": "die Heterogenität", "reification": "die Verdinglichung", "teleology": "die Teleologie",
"hermeneutics": "die Hermeneutik", "verisimilitude": "die Wahrscheinlichkeit, die Glaubwürdigkeit",
"praxis": "die Praxis", "instantiate": "instanziieren, konkretisieren", "valorise": "aufwerten",
"interrogate": "kritisch hinterfragen", "foreground": "in den Vordergrund stellen", "elide": "auslassen, übergehen",
"conflate": "vermengen", "vitiate": "entkräften, beeinträchtigen", "recondite": "abstrus, schwer verständlich",
"nascent": "entstehend, aufkommend", "polemical": "polemisch", "germane": "relevant, zur Sache gehörig",
"prima facie": "auf den ersten Blick", "ceteris paribus": "unter sonst gleichen Bedingungen",
}
