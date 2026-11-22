# -*- coding: utf-8 -*-
"""English word lists.

DAILY    : A1.1–C2.2 — A1–C1 aligned with the Oxford 3000 / Oxford 5000 CEFR
           levels plus 1500 core concepts; phrasal verbs, connectors and
           idioms up to C2.2
ACADEMIC : B1.1–C2.2 — vocabulary and set phrases for papers, theses and talks
CYBER    : B1.1–C2.2 — professional cybersecurity vocabulary (attacks, networking,
           Linux, web security, crypto & IAM, pentest, SOC/IR, GRC, workplace phrases)
Lines: "type|English|Turkish|hint"
       type: n noun, v verb, a adjective, d adverb / linker, p phrase, w other word
EN_DE* : English -> German meaning
"""

DAILY = {
"A1.1": """
w|to|-e, -a
w|and|ve
w|in|içinde
w|I|ben
w|for|için
w|you|sen
w|you (plural)|siz
w|you (object)|seni
w|it|o (nötr)
w|on|üstünde
w|with|ile
p|and you?|ya sen?
v|be|olmak|am / is / are · was / were · been
v|have|sahip olmak, -si olmak|has · had · had
w|at|-de, kenarında, yanında
w|he|o (erkek)
w|not|değil
w|by|tarafından; yanında
w|but|ama, yine de
w|from|-den, -in
v|have to|-mek zorunda olmak
w|my|benim
w|we|biz
w|or|veya
w|your|senin
w|your (plural)|sizin
w|so|yani, öyleyse
w|his|onun (erkek)
w|me|beni
w|one|bir
w|one (people in general)|(genel özne) insan
w|if|eğer, -dığında
v|can|-ebilmek
v|will|-ecek (gelecek zaman)
w|just|sadece; az önce
v|like|sevmek, hoşlanmak
w|so that|ki (amaç)
w|about|yaklaşık
d|up|yukarı
w|what|ne
d|out|dışarı
w|when|-iken, -den (karşılaştırma), ne zaman
w|more|daha fazla
w|no|hayır, hiçbir, yok
v|do|yapmak, etmek|did · done
w|out of|-den (içinden)
w|who|kim
w|their|onların
w|there|orada, işte
w|which|hangi
w|her|onun (kadın); onu
n|time|zaman
v|get|almak, edinmek|got · got/gotten
v|would|-erdi (şart)
w|she|o (kadın), onlar
n|people|insanlar
w|new|yeni
w|how|nasıl
w|some|bazıları
w|also|de, da
w|them|onları
w|other|diğer
w|our|bizim
w|its|onun (şey/hayvan)
w|than|-den (karşılaştırma)
a|good|iyi
w|only|sadece
w|into|içine
w|him|onu, ona (erkek)
w|two|iki
v|know|bilmek, tanımak|knew · known
v|see|görmek|saw · seen
w|no one|hiç kimse
w|over|üzerinde, hakkında
v|think|düşünmek|thought · thought
v|make|yapmak|made · made
w|then|sonra
w|any|herhangi bir; hiç
p|how are you?|nasılsın?
w|us|bizi, bize
v|want|istemek
n|back|sırt
v|go|gitmek|went · gone
w|because|çünkü, -dığı için
w|because of|yüzünden
n|way|yol, patika
w|much|çok
w|where|nerede
w|very|çok
w|most|en çok
w|just now|tam şu an
w|should|-meli
w|even|hatta
w|where to|nereye
n|May|Mayıs
w|really|gerçekten
w|here|burada
v|need|ihtiyacı olmak
w|right|doğru, sağ
n|year|yıl
n|a work|iş; eser
v|work|çalışmak
n|day|gün
d|too|de/da; fazla
w|why|neden, niçin
w|before|önce
d|off|kapalı; uzağa
v|take|almak|took · taken
w|still|hâlâ, daha
w|where from|nereden
w|never|asla
w|many|çok (sayılabilen)
v|say|söylemek|said · said
n|world|dünya
n|life|hayat
w|great|süper
w|down|aşağı
p|here you are|buyurun
w|through|içinden, vasıtasıyla
n|man|adam, koca
n|love|aşk, sevgi
v|to love|sevmek
w|something|bir şey, biraz
v|look|bakmak
v|use|kullanmak, yararlanmak, kullanmak
w|long|uzun
n|home|ev, yuva
p|how much|ne kadar
w|same|aynı
w|every|her biri
w|both|her ikisi
v|come|gelmek|came · come
w|three|üç
p|both … and|hem ... hem de
n|part|parça, kısım
w|around|etrafında, saat -de
v|find|bulmak|found · found
d|always|her zaman
p|all the best|her şey gönlünce olsun
w|help!|imdat!
v|help|yardım etmek
w|old|eski, yaşlı
n|a help|yardım
p|how many|kaç tane
w|another|başka bir
w|under|altında
w|during|sırasında
n|game|oyun, maç
n|thing|şey
n|house|ev
n|school|okul
n|place|yer, mekân
v|give|vermek|gave · given
w|again|yine
w|next|sonraki
w|next to|yanında
w|without|-siz, olmadan
w|each|her bir
v|must|zorunda olmak
v|end|bitmek
v|show|göstermek|showed · shown
n|an end|son
n|a show|gösteri, program
a|big|büyük
p|how long|ne kadar süre
n|team|ekip, takım
v|feel|hissetmek|felt · felt
n|family|aile
w|please|lütfen, buyurun
v|put (upright)|dikey koymak
w|ever|hiç, şimdiye dek
v|keep|tutmak; devam etmek|kept · kept
a|family (adj.)|ailevi, aile için
w|how come|niçin
n|money|para
v|put on|giymek|put on · put on
w|someone|biri
n|number|sayı
w|left|sol
w|away|uzakta, gitmiş
v|take off|çıkarmak (giysi)|took off · taken off
n|city|şehir
n|name|isim, ad
w|until|-e kadar
n|night|gece
v|play|oynamak
w|a lot|çok, bir sürü
v|to name|ad vermek
n|a play|oyun (tiyatro)
n|company|şirket
w|real|gerçek, hakiki
w|few|az, birkaç
v|let|izin vermek, bırakmak
w|different|farklı
d|however|ancak
n|group|grup
n|week|hafta
v|start|başlamak, başlatmak
n|business|iş; işletme
d|today|bugün
p|my name is …|benim adım ...
w|nothing|hiçbir şey
n|person|kişi
w|anything|herhangi bir şey
v|live|yaşamak, oturmak
w|enough|yeterli
v|change (trains)|aktarma yapmak
n|change (money)|para üstü
n|point|nokta; mesele
w|everything|her şey
v|read|okumak|read · read (okunuşu: /red/)
v|to live|oturmak, yaşamak
w|full (after eating)|tok
w|four|dört
v|mean|demek istemek, düşünmek, anlamına gelmek|meant · meant
v|tell|anlatmak|told · told
w|bad|kötü
w|once|bir kez; bir zamanlar
w|hard|zor; sert
n|water|su
v|stop|durmak, bırakmak, durdurmak
n|music|müzik
n|a stop|durak; duruş
a|small|küçük
w|white|beyaz
v|call|aramak (telefonla)
v|believe|inanmak, sanmak
n|a call|arama, telefon
n|head|kafa
w|yes|evet
n|job|iş
d|far|uzak
v|try|denemek, tatmak
p|good night|iyi geceler
n|line|çizgi
n|first name|ad
n|party|parti
v|run|koşmak|ran · run
n|order|sipariş, görev
v|to order|sipariş vermek
n|country|ülke
p|I'm called …|benim adım ...
v|thank|teşekkür etmek
v|open|açmak
v|try on|denemek (giysi)
p|once more|bir kez daha
w|everyone|herkes
w|black|siyah
w|right away|hemen, birazdan
n|area|bölge
w|together|birlikte
w|maybe|belki
w|five|beş
n|car|araba
n|kind|tür
n|story|hikâye
n|face|yüz
v|hope|ummak
a|important|önemli
n|course|kurs
n|news|haberler
n|health|sağlık
w|thanks|teşekkürler
w|of course|tabii ki
p|how far|ne kadar uzak
n|book|kitap
n|video|video
v|post|paylaşım yapmak
w|young|genç
w|early|erken
n|information|bilgi
w|local|yerel
n|a post|gönderi; posta
w|others|diğerleri
v|talk|konuşmak, sohbet etmek
d|ago|önce (zaman)
n|half (noun)|yarısı
w|often|sık sık
n|fact|gerçek
n|hand|el
v|become|olmak; -ecek (gelecek zaman)|became · become
n|office|ofis
n|problem|sorun
w|true|gerçek
n|south|güney
n|body|vücut
n|food|yemek
v|to pay|ödemek|paid · paid
n|university|üniversite, yüksekokul
v|win|kazanmak|won · won
n|history|tarih, hikâye
w|large|büyük
n|room|oda
p|see you later|sonra görüşürüz
n|girl|kız çocuk
v|remember|hatırlamak
w|anyone|herhangi biri
w|else|başka
w|pretty|oldukça; güzel
n|friend|arkadaş
v|understand|anlamak|understood · understood
n|air|hava
w|nice|kibar, hoş
w|probably|muhtemelen
w|yeah|evet (konuşma dili)
n|past|geçmiş
n|class|sınıf
w|possible|mümkün
n|idea|fikir
a|past (adj.)|geçmiş, önceki
v|close|kapatmak
n|house number|kapı numarası
a|happy|mutlu
p|no problem|sorun değil
p|how often|ne sıklıkta
n|woman|kadın, eş
n|a question|soru
v|wait|beklemek|wait for sb
v|to move (house)|taşınmak
v|ask|sormak
v|leave|terk etmek|left · left
w|special|özel, özellikle
w|late|geç
v|watch|izlemek
n|north|kuzey
n|a watch|kol saati
n|million|milyon
n|morning|sabah
n|working day|iş günü
n|future|gelecek
v|stay|kalmak
n|police|polis
w|short|kısa
w|red|kırmızı
w|soon|yakında
n|age|yaş
n|reason|sebep
v|turn|dönmek, çevirmek
n|a report|rapor
n|a turn|sıra; dönüş
v|buy|satın almak|bought · bought
v|check|kontrol etmek, sınamak
n|form|form
w|yourself|kendin
n|child|çocuk|çoğul: children
p|I don't understand|anlamıyorum
w|but rather|aksine, bilakis
p|either … or|ya ... ya da
n|fire|ateş
n|phone|telefon
n|fun|eğlence
v|to phone|telefon etmek
w|six|altı
w|behind|arkasında
n|building|bina
n|market|pazar
w|near|yakın
v|plan|planlamak
d|quite|oldukça
n|art|sanat
a|easy|kolay
n|a plan|plan
n|west|batı
p|have fun|iyi eğlenceler
w|sometimes|bazen
n|son|oğul
w|ready|hazır
n|front|ön
a|front (adj.)|ön
n|list|liste
n|street|sokak, cadde
p|thank you very much|çok teşekkürler
w|in front of|önünde, önce
v|meet|buluşmak, tanışmak|met · met
v|bring|getirmek|brought · brought
n|example|örnek
n|type|tür
n|college|yüksekokul, kolej
p|good morning|günaydın
n|March|Mart
n|baby|bebek
n|father|baba
n|word|kelime
v|study (at university)|üniversitede okumak
n|song|şarkı
n|a study|çalışma, araştırma
p|see you soon|yakında görüşürüz
n|month|ay
n|human being|insan
w|across|karşıya
n|action|eylem
w|instead of|yerine
n|mother|anne
v|cost|fiyatı olmak|cost · cost
w|main|ana
n|moment|an
n|road|yol
n|town|kasaba
n|a cost|maliyet
v|cut|kesmek|cut · cut
n|summer|yaz
n|wife|eş, karı
v|hear|duymak, dinlemek|heard · heard
n|space|alan; uzay
n|price|fiyat
n|date|tarih
v|miss|kaçırmak
n|project|proje
w|beautiful|güzel
n|land|kara, arazi
w|strong|güçlü
n|June|Haziran
n|parents|ebeveynler
w|similar|benzer
v|include|dahil etmek
n|period|dönem, süre
p|get well soon|geçmiş olsun
w|above|yukarıda
n|film|film
v|share|paylaşmak, bölmek
w|perfect|mükemmel
w|personal|kişisel
n|club|kulüp
a|common|yaygın; ortak
n|April|Nisan
v|happen|olmak, meydana gelmek, gerçekleşmek
n|test|test
n|star|yıldız
v|return|geri dönmek
n|player|oyuncu
v|to test|test etmek
w|online|çevrim içi
n|a return|dönüş; iade
p|I'm fine|iyiyim
n|hour|saat (süre)
n|present|şimdiki zaman, hediye
n|break|mola
n|result|sonuç
v|break (something)|bozmak
n|event|etkinlik, olay
n|member|üye
w|sorry|üzgün
n|July|Temmuz
n|boy|erkek çocuk
v|answer|cevap vermek
v|learn|öğrenmek|learnt · learnt
v|interest|ilgisini çekmek
n|design|tasarım
v|guess|tahmin etmek
n|an answer|cevap
v|to design|tasarlamak
n|a guess|tahmin
n|an interest|ilgi; faiz
n|park|park
n|bank|banka
w|hot|çok sıcak
v|to park|park etmek
n|east|doğu
n|movie|film
n|September|Eylül
n|bill|fatura, hesap
d|usually|genellikle
n|meeting|toplantı, oturum
n|sound|ses
v|to sound|gibi gelmek, kulağa … gelmek
p|I'm sorry|üzgünüm
n|reading|okuma
v|follow|takip etmek
v|stand|ayakta durmak
v|eat|yemek yemek|ate · eaten
n|number (phone|numara
w|blue|mavi
w|green|yeşil
a|fast|hızlı
v|drive|gitmek (araçla)|drove · driven
n|feeling|his, duygu
v|fall|düşmek|fell · fallen
d|fast (adv.)|hızlıca
n|match|maç; kibrit
n|model|model
n|picture|resim, tablo
v|to eat|yemek yemek|ate · eaten
n|key|anahtar
n|science|bilim
w|hey|hey
a|key (adj.)|kilit, en önemli
n|page|sayfa
n|October|Ekim
n|brother|erkek kardeş
v|send|göndermek, yollamak|sent · sent
n|football|futbol
v|hate|nefret etmek
w|natural|doğal
n|style|üslup
n|cup|fincan
n|August|Ağustos
n|November|Kasım
n|dog|köpek
n|language|dil
v|complete|tamamlamak
n|title|başlık; unvan
a|amazing|harika, şaşırtıcı
a|complete (adj.)|tam, eksiksiz
n|January|Ocak
v|enjoy|keyfini çıkarmak
n|website|web sitesi
v|add|toplamak
w|poor|fakir
n|article|makale
n|situation|durum
w|seven|yedi
v|walk|yürümek, koşmak
v|lose|kaybetmek|lost · lost
v|be born|doğmak
n|a walk|yürüyüş
n|hair|saç
n|door|kapı
n|December|Aralık
n|daughter|kız evlat
n|career|kariyer
n|paper|kâğıt
w|modern|modern
w|difficult|zor
w|popular|sevilen, popüler
v|die|ölmek
n|writing|yazı, yazma
n|hospital|hastane
n|bed|yatak
w|okay|tamam
""",
"A1.2": """
v|forget|unutmak|forgot · forgotten
v|listen|dinlemek
n|sea|deniz
n|internet|internet
n|success|başarı
n|practice|uygulama; pratik
w|ten|on
n|father-in-law|kayınpeder
w|below|aşağıda
n|table|masa
v|sleep|uyumak|slept · slept
v|to sleep|uyumak|slept · slept
n|percent|yüzde
n|piece|adet, parça
v|visit|gezmek, ziyaret etmek
n|ball|top
v|build|inşa etmek|built · built
n|card|kart
n|box|kutu
n|note|not
n|a visit|ziyaret
n|living room|oturma odası
n|wall|duvar
v|speak|konuşmak|spoke · spoken
n|late morning|öğleden önce
n|February|Şubat
n|mother-in-law|kaynana
w|married|evli
n|river|nehir
n|culture|kültür
d|tonight|bu gece
v|write|yazmak|wrote · written
n|main course|ana yemek
w|eight|sekiz
n|student (university)|öğrenci (üniversite)
w|funny|komik
n|century|yüzyıl
a|cold (adj.)|soğuk
v|create|yaratmak, oluşturmak
d|tomorrow|yarın
n|eye|göz
n|cold|soğuk algınlığı
p|nice to meet you|memnun oldum
w|brown|kahverengi
n|difference|fark
n|text|metin
n|island|ada
n|capital|başkent; sermaye
a|capital (adj.)|büyük (harf); başlıca
n|radio|radyo
n|station|istasyon
n|husband|koca
v|travel|seyahat etmek
n|message|mesaj, haber
w|interesting|ilginç
n|beginning|başlangıç
v|join|katılmak
n|ice|buz
d|quickly|çabucak
n|travel (noun)|seyahat
w|positive|olumlu
p|see you tomorrow|yarın görüşürüz
n|minute|dakika
w|earlier|daha önce
v|sell|satmak|sold · sold
w|quick|hızlı
a|extra|ekstra, ilave
v|spend|harcamak|spent · spent
n|sun|güneş
n|computer|bilgisayar
n|photo|fotoğraf
v|agree|katılmak, aynı fikirde olmak
n|statement|açıklama
a|clean (adj.)|temiz
v|clean|temizlemek
n|Friday|Cuma
n|train|tren, demiryolu
n|subject|ders (branş)
n|sister|kız kardeş
n|centre|merkez
n|hotel|otel
n|product|ürün
w|nobody|kimse
n|dad|baba
a|interested|ilgili, meraklı
n|letter|mektup; harf
p|you're welcome|rica ederim
n|opinion|görüş, fikir
n|rule|kural
n|floor|zemin, kat
n|weekend|hafta sonu
v|dance|dans etmek
n|a dance|dans
n|Sunday|Pazar
n|spring|ilkbahar
n|beach|plaj
v|imagine|hayal etmek
n|band|müzik grubu
v|wear|giymek, taşımak|wore · worn
w|yesterday|dün
v|finish|bitirmek
v|choose|seçmek|chose · chosen
w|rich|zengin
n|an address|adres
v|drink|içmek|drank · drunk
n|trip|seyahat
v|sit|oturmak|sat · sat
v|grow|büyümek|grew · grown
n|machine|makine
n|a drink|içecek
n|doctor|doktor
n|doctor (female)|doktor (kadın)
n|fish|balık
v|to drink|içmek|drank · drunk
n|winter|kış
v|explain|açıklamak
v|carry|taşımak
n|plant|bitki; fabrika
p|good luck|bol şans
n|shop|dükkân
a|sick|hasta
n|teacher|öğretmen
n|advice|tavsiye
v|to shop|alışveriş yapmak
p|have a good trip|iyi yolculuklar
w|nine|dokuz
n|Saturday|Cumartesi
n|foot|ayak
n|weather|hava durumu
n|camera|kamera
n|meaning|anlam
n|evening|akşam
n|coffee|kahve
n|library|kütüphane
n|activity|faaliyet
n|flight|uçuş
n|an interview|röportaj; mülakat
n|glass|bardak, cam
n|traffic|trafik
n|tree|ağaç
w|slow|yavaş
w|wonderful|harika
v|ride|binmek|rode · ridden
a|fat|şişman
p|good evening|iyi akşamlar
n|partner|partner
n|airport|havalimanı
v|begin|başlamak|began · begun
w|sad|üzgün
w|famous|ünlü
w|twice|iki kez
w|everybody|herkes
n|mouth|ağız
n|bus|otobüs
n|cent|sent
w|fourth|dördüncü
n|health insurance|sağlık sigortası
n|village|köy
n|animal|hayvan
v|draw|çizmek|drew · drawn
n|Monday|Pazartesi
n|adult|yetişkin
w|healthy|sağlıklı
n|window|pencere
n|artist|sanatçı
w|somebody|biri
p|have a nice weekend|iyi hafta sonları
n|bag|çanta
v|to improve|iyileştirmek
n|television|televizyon
w|dangerous|tehlikeli
w|correct|doğru
w|negative|olumsuz
n|dinner|akşam yemeği
v|to decide|karar vermek
n|cat|kedi
w|fifth|beşinci
n|garden|bahçe
a|dear|sevgili; pahalı
n|birthday|doğum günü
n|apple|elma
n|dress|elbise
n|map|harita, kart
n|horse|at
v|wake|uyanmak|woke · woken
v|to dress|giyinmek, giydirmek
n|bus stop|otobüs durağı
a|busy|meşgul
v|fly|uçmak|flew · flown
n|driver|şoför
n|conversation|sohbet
n|farm|çiftlik
n|wine|şarap
w|excited|heyecanlı
n|magazine|dergi
n|arm|kol
n|ground floor|zemin kat
n|tea|çay
n|mountain|dağ
n|sport|spor
n|description|tanım
n|blog|blog
w|hello|merhaba
n|quarter|çeyrek
n|pair|çift
n|afternoon|öğleden sonra
n|flat|daire
n|clothes|giysi
n|plane|uçak
n|festival|kutlama, festival
w|useful|faydalı
w|hundred|yüz
a|cheap|ucuz
a|tired|yorgun
n|museum|müze
n|rain|yağmur
n|boat|tekne
w|fantastic|harika
w|terrible|korkunç
v|to rain|yağmur yağmak
p|good afternoon|iyi günler
n|beer|bira
w|afraid|korkmuş
w|yellow|sarı
n|chair|sandalye
a|expensive|pahalı
n|insurance card|sigorta kartı
n|writer|yazar
n|girlfriend|kız arkadaş
n|sugar|şeker
n|restaurant|restoran
n|shopping|alışveriş
n|exercise|alıştırma
n|email|e-posta
v|to email|e-posta göndermek
v|to exercise|egzersiz yapmak
n|additional costs|yan giderler
n|changing room|deneme kabini
n|mistake|hata
v|teach|öğretmek|taught · taught
n|pool|havuz
n|leg|bacak
n|lunch|öğle yemeği
n|milk|süt
n|holiday|tatil
n|snow|kar
v|discuss|tartışmak
v|laugh|gülmek
w|angry|kızgın
n|a laugh|kahkaha
v|to snow|kar yağmak
w|twenty|yirmi
n|kitchen|mutfak
v|cook|yemek pişirmek
w|quiet|sessiz
n|actor|aktör
n|apartment|daire
n|journey|yolculuk
w|thousand|bin
n|emergency room|acil servis
w|friendly|dostane
v|fill|doldurmak
n|Tuesday|Salı
n|meat|et
n|chicken|tavuk
n|shirt|gömlek
n|bird|kuş
w|false|yanlış
w|orange|turuncu
w|opposite|karşısında
n|Thursday|Perşembe
n|cream|krema
n|public holiday|resmi tatil
n|breakfast|kahvaltı
n|ticket|bilet
n|customer|müşteri
n|salt|tuz
n|newspaper|gazete
n|painting|tablo, resim
n|Wednesday|Çarşamba
n|mile|mil
n|boyfriend|erkek arkadaş
n|dollar|dolar
n|sentence|cümle
n|cheese|peynir
n|fruit|meyve
n|bottle|şişe
n|T-shirt|tişört
n|diet|diyet
v|prefer|tercih etmek
n|detail|detay
a|favourite|en sevdiği
n|parent|ebeveyn
n|programme|program
w|excuse me|affedersiniz, özür dilerim
v|describe|tarif etmek, betimlemek
n|object|nesne
w|dirty|kirli
n|rice|pirinç
v|prepare|hazırlamak
n|concert|konser
n|bathroom|banyo
v|sing|şarkı söylemek|sang · sung
a|exciting|heyecan verici
n|cake|kek, pasta
n|hat|şapka
n|bike|bisiklet
w|pink|pembe
n|theatre|tiyatro
v|paint|resim yapmak, boyamak
n|singer|şarkıcı
a|tall|uzun boylu
n|nose|burun
n|bread|ekmek
n|shower|duş
n|dancing|dans etme
n|colour|renk
n|chocolate|çikolata
n|topic|konu
v|repeat|tekrar etmek
w|grey|gri
n|meal|öğün
n|guitar|gitar
p|neither … nor|ne ... ne de
n|ice cream|dondurma, buz
n|chart|grafik
n|lesson|ders
n|bedroom|yatak odası
v|wash|yıkamak
n|egg|yumurta
n|uncle|amca, dayı
w|hungry|aç
v|compare|karşılaştırmak
n|cooking|yemek yapma
n|actress|kadın oyuncu
n|bath|banyo
n|clock|saat (alet)
n|ear|kulak
n|gym|spor salonu
n|desk|çalışma masası
n|swimming|yüzme
w|boring|sıkıcı
n|worker|işçi
n|flower|çiçek
n|skill|beceri
n|cousin (male)|kuzen (erkek)
n|cousin (female)|kuzen (kız)
n|telephone|telefon
n|mum|anne
p|congratulations|tebrikler
n|butter|tereyağı
n|nurse (male)|hemşire (erkek)
n|vacation|tatil
w|bye|hoşça kal
p|enjoy your meal|afiyet olsun
w|thirty|otuz
v|arrive|varmak
n|pen|kalem
n|honey|bal
v|introduce|tanıtmak
n|routine|rutin
v|spell|hecelemek
n|juice|meyve suyu
n|coat|palto
w|twelve|on iki
n|tennis|tenis
n|glasses|gözlük
w|delicious|lezzetli
n|reader|okur
w|purple|mor
n|jacket|ceket, mont
n|pound|sterlin; libre
n|toilet|tuvalet
n|bread roll|küçük ekmek
n|mouse|fare
n|midnight|gece yarısı
n|piano|piyano
p|goodbye|güle güle, hoşça kalın
n|calendar|takvim
n|phrase|deyim
w|fifty|elli
v|relax|rahatlamak
n|dialogue|diyalog
n|autumn|sonbahar
n|menu|menü
n|exam|sınav
n|lion|aslan
n|grandfather|dede
n|shoe|ayakkabı
n|snake|yılan
n|photograph|fotoğraf
v|climb|tırmanmak
v|swim|yüzmek|swam · swum
n|scientist|bilim insanı
n|dish|yemek; tabak
w|forty|kırk
n|tourist|turist
a|bored|sıkılmış
n|taxi|taksi
n|sheep|koyun
n|boot|bot, çizme
n|cinema|sinema
n|aunt|teyze, hala
n|soup|çorba
n|salad|salata
n|vegetables|sebze
n|classroom|sınıf
n|farmer|çiftçi
w|fifteen|on beş
n|grandmother|büyükanne
n|stairs|merdiven
n|pepper (spice)|biber (baharat)
n|pepper (vegetable)|biber
n|cow|inek
n|pig|domuz
w|cheers|şerefe
n|homework|ödev
n|sandwich|sandviç
w|eleven|on bir
n|ham|jambon
n|grandma|nine (samimi)
n|potato|patates
w|cooked|pişmiş, haşlanmış
n|belly|karın
n|teenager|genç
n|jeans|kot pantolon
n|euro|avro
n|cafe|kafe
n|tooth|diş
n|elephant|fil
n|washing machine|çamaşır makinesi
n|laundry|çamaşır
n|siblings|kardeşler
n|passport|pasaport
a|blonde|sarışın
d|o'clock|saat (tam)
n|rental agreement|kira sözleşmesi
n|pork|domuz eti
n|paragraph|paragraf
n|starter|başlangıç
n|dictionary|sözlük
n|nephew|yeğen (erkek)
n|visitor|ziyaretçi
n|banana|muz
n|spelling|yazım, imla
n|dancer|dansçı
n|bicycle|bisiklet
n|geography|coğrafya
n|skirt|etek
w|sixteen|on altı
n|cough|öksürük
n|pencil|kurşun kalem
n|vegetable|sebze
n|hobby|hobi
w|sixty|altmış
n|garlic|sarımsak
n|pasta|makarna
w|thirteen|on üç
n|onion|soğan
n|umbrella|şemsiye
w|fourteen|on dört
w|yearly|yıllık
n|grandparents|büyükanne ve büyükbaba
n|air conditioning|klima
w|sour|ekşi
w|seventeen|on yedi
d|upstairs|üst katta
n|grandson|torun
n|tomato|domates
n|dessert|tatlı
p|pardon?|efendim?, anlamadım
w|pardon me|pardon
n|niece|yeğen (kız)
w|eighteen|on sekiz
n|sofa|kanepe
n|grandpa|dede (samimi)
n|sausage|sosis, sucuk
w|seventy|yetmiş
n|balcony|balkon
w|vegetarian|vejetaryen
n|backpack|sırt çantası
n|supermarket|süpermarket
n|sweater|kazak
n|gram|gram
n|metre|metre
w|eighty|seksen
n|café|kafe
w|thirsty|susuz
w|salty|tuzlu
n|policeman|polis memuru
n|hallway|koridor
n|strawberry|çilek
n|sunglasses|güneş gözlüğü
w|downstairs|alt katta
w|ninety|doksan
n|stove|ocak
n|doctor's office|muayenehane
n|jumper|kazak
n|trousers|pantolon
n|neighbour|komşu
n|scarf|atkı
n|thirst|susuzluk
n|carrot|havuç
n|waiter|garson
n|allergy|alerji
w|nineteen|on dokuz
n|shampoo|şampuan
w|oneself|kendi
v|tidy up|toplamak, düzenlemek
n|socket|priz
v|practise|alıştırma yapmak
n|surname|soyadı
n|caretaker|apartman görevlisi
n|lemonade|gazoz
n|cucumber|salatalık
n|toothbrush|diş fırçası
n|toothpaste|diş macunu
w|cosy|rahat, sıcak (ortam)
n|dishwasher|bulaşık makinesi
n|armchair|koltuk
n|kilometre|kilometre
n|kilo|kilo
n|housework|ev işi
n|yoghurt|yoğurt
n|postcode|posta kodu
w|punctual|dakik
n|grandparent|büyükanne/büyükbaba
n|washbasin|lavabo
""",
"A2.1": """
v|to have|sahip olmak|had · had
w|all|hepsi
n|a can|teneke kutu
v|to like|hoşlanmak
v|like (a post)|beğenmek (sosyal medya)
a|on time|zamanında
v|get on|binmek|got on · got on
n|good (noun)|iyilik, fayda
w|first|birinci, önce
w|after|-den sonra, -e doğru
v|know (a fact)|bilmek
v|know (a person)|tanımak
v|to think|düşünmek|thought · thought
v|to want|istemek
a|back (adj.)|arka
p|get up|(yataktan) kalkmak|got up
v|to go|gitmek, yürümek|went · gone
v|to get up|kalkmak|got up · got up
v|to may|izni olmak
v|to need|ihtiyacı olmak
n|a need|ihtiyaç
v|to work|çalışmak (makine)
w|at the back|arkada
d|any more|artık (değil)
v|to last|sürmek
w|last|sonuncu, en son
w|while|-iken
p|all right|tamam, uygun
w|best|en iyi
w|such|böyle
a|home (adj.)|ev ile ilgili; yerli
n|a look|bakış; görünüm
n|a use|kullanım
v|used to|eskiden …-erdi
p|look for|(bir şeyi) aramak
v|to come|gelmek|came · come
n|state|devlet
v|get off|inmek|got off · got off
w|between|arasında
w|better|daha iyi
v|look at|incelemek, bakmak
v|to help|yardım etmek
w|little|az
w|since|-den beri
v|own|sahip olmak
w|against|karşı
w|sure|emin
p|find out|öğrenmek, ortaya çıkarmak|found out
v|please (be liked)|hoşuna gitmek
w|might|-ebilir (olasılık)
n|part-time|yarı zamanlı
w|second|ikinci
p|give up|vazgeçmek, bırakmak|gave up · given up
v|to number|numaralandırmak
n|thought|düşünce
n|government|hükümet
w|public|kamuya açık
n|god|tanrı
n|top|tepe; üst
n|care|bakım, özen
n|system|sistem
v|to care|önemsemek; bakmak
n|a start|başlangıç
w|already|zaten, çoktan, hâlihazırda
n|case|durum; dava
v|give back|iade etmek
v|change|değiştirmek, değişmek
d|yet|henüz; yine de
v|to read|okumak|read · read
n|support (noun)|destek
n|power|güç
w|including|dahil
a|based|dayalı; merkezli
a|national|ulusal
v|call (on the phone)|telefonla aramak
n|side|taraf, sayfa
v|take place|gerçekleşmek (etkinlik)
w|less|daha az
w|later|sonra
d|actually|aslında
n|a run|koşu
n|service|hizmet
n|season|mevsim
a|general|genel
a|united|birleşik
n|full-time|tam zamanlı
n|law|kanun
w|whole|bütün
a|following|sonraki, aşağıdaki
n|war|savaş
w|per|başına
n|president|başkan, cumhurbaşkanı
a|working|çalışan; işleyen
w|least|en az
n|a hope|umut
w|able|yapabilen
v|to book|rezervasyon yapmak
w|social|sosyal
n|a talk|konuşma
w|half|yarım
w|single|bekâr
n|mind|zihin
n|level|seviye
v|to mind|sakıncası olmak; dikkat etmek
v|pay|ödemek|paid · paid
n|death|ölüm
n|control (noun)|kontrol
n|guy|adam, herif
n|pay (noun)|maaş, ücret
v|research|araştırmak
w|almost|neredeyse
w|several|birkaç
a|lost|kayıp
w|along|boyunca
n|matter|mesele
v|to matter|önemli olmak
n|a bit|biraz; parça
n|a hit|darbe; hit (şarkı)
v|to understand|anlamak|understood · understood
w|international|uluslararası
a|close (adj.)|yakın
d|past (adv.)|geçerek; geçe
v|to wait|beklemek
n|series|dizi
n|cause|neden
w|human|insan(i)
v|question|sorgulamak
v|to cause|neden olmak
n|a wait|bekleme
v|move|taşınmak; hareket etmek
v|ask (for)|rica etmek
n|community|topluluk
n|data|veri
v|to stay|kalmak
w|light|açık (renk), aydınlık, hafif
w|either|ikisinden biri
a|future (adj.)|gelecekteki
n|a stay|kalış, konaklama
v|to buy|satın almak|bought · bought
w|third|üçüncü
v|report|rapor etmek, bildirmek
w|rather|tercihen
v|to deal|ilgilenmek; dağıtmak
n|heart|kalp
w|further|daha ileri
w|among|arasında
n|a check|kontrol
w|myself|kendim
w|although|-mesine rağmen
n|media|medya
v|act|davranmak; rol yapmak
a|fun (adj.)|eğlenceli
a|major|büyük, önemli
n|education|eğitim
w|final|son
w|according to|-e göre
a|available|mevcut, müsait
v|to meet|buluşmak, isabet etmek|met · met
n|experience|deneyim
n|program|program
w|at the front|önde
n|chance|şans, ihtimal
n|process|süreç
w|outside|dışarıda
w|clear|açık, net
w|himself|kendisi (erkek)
v|come along|birlikte gelmek
n|field|alan, tarla
w|instead|bunun yerine
n|thinking|düşünme, düşünce
n|board|tahta
v|rest|dinlenmek
n|running|koşu
v|fight|savaşmak, mücadele etmek|fought · fought
n|term|terim; dönem
n|a fight|kavga
n|a rest|dinlenme; kalan
n|department|departman
n|energy|enerji
n|site|yer, saha
v|to land|iniş yapmak
d|especially|özellikle
n|a record|kayıt; rekor
n|position|pozisyon, iş yeri
w|likely|muhtemel
v|to film|filme almak
v|lead|yönetmek, yönlendirmek, götürmek|led · led
n|view|manzara
v|hold|tutmak|held · held
w|inside|içeride
n|couple|çift
w|dead|ölü
n|industry|sanayi
n|sense|his; anlam
v|to star|başrolde oynamak
n|middle|orta
v|wish|dilemek
n|training|antrenman
a|middle (adj.)|orta
v|to present|sunmak
n|a wish|dilek
n|society|toplum
w|finally|sonunda, nihayet
n|gold|altın
n|king|kral
n|end of the working day|paydos
n|school report|karne, belge
n|church|kilise
w|alone|yalnız
w|average|ortalama
w|certain|belirli; emin
w|medical|tıbbi
a|original (adj.)|orijinal, ilk
n|role|rol
w|themselves|kendileri
w|exactly|aynen, tam olarak
n|relationship|ilişki
n|director|yönetmen, müdür
n|ground|zemin
v|provide|sağlamak
n|source|kaynak
v|save|biriktirmek, tasarruf etmek, kaydetmek
w|round|yuvarlak
n|rate|oran
n|evidence|kanıt
n|amount|miktar
n|size|beden, boyut
n|step|adım
n|a drive|araba yolculuğu; sürücü
n|a fall|düşüş; sonbahar (ABD)
v|eat (animals)|yem yemek (hayvan)
w|forward|ileri
n|review|inceleme, eleştiri
n|working hours|çalışma saati
n|post office|postane
w|good value|uygun fiyatlı
n|quality|kalite
w|attention|dikkat
n|character|karakter
n|blood|kan
n|oil|yağ
w|serious|ciddi
w|itself|kendisi (şey)
n|stage|aşama; sahne
n|attack|saldırı
n|decision|karar
w|perhaps|belki
v|to attack|saldırmak
v|kill|öldürmek
n|phone call|arama
n|technology|teknik, teknoloji
n|choice|seçenek, çeşit
v|sign|imzalamak
w|simple|basit, kolay
w|foreign|yabancı
v|continue|devam ettirmek
v|increase|artmak, artırmak
n|race|yarış; ırk
v|seem|görünmek
n|code|kod
v|to cover|örtmek; kapsamak
n|an increase|artış
v|pick|seçmek; toplamak
v|to race|yarışmak
n|a sign|işaret; tabela
w|whose|kimin
w|safe|güvenli, emin
w|crazy|çılgın
n|voice|ses
n|figure|rakam; figür
n|goal|hedef
n|army|ordu
w|huge|kocaman
n|sir|efendim, bayım
w|towards|-e doğru
n|earth|toprak, dünya
n|offer|kampanya, teklif
v|to offer|sunmak
v|mark|işaretlemek
w|professional|profesyonel
n|a mark|not; iz
a|missing|kayıp, eksik
n|sleep (noun)|uyku
v|pass (an exam)|(sınavı) geçmek
v|talk on the phone|telefonla konuşmak
v|be missing|eksik olmak
w|dark|koyu, karanlık
w|recent|son, yakın tarihli
w|straight|düz
w|mine|benimki
p|look forward to|dört gözle beklemek|+ -ing
v|to speak|konuşmak|spoke · spoken
n|pain|ağrılar
n|officer|memur, subay
a|included|dahil
n|response|yanıt, tepki
n|rock|kaya; rock müzik
v|shall|-eyim mi? (öneri)
a|specific|belirli, özel
v|to write|yazmak|wrote · written
n|store|mağaza
w|except|hariç
n|effect|etki
n|peace|barış
n|track|iz; parça
n|weight|ağırlık
n|network|ağ
d|recently|son zamanlarda
v|allow|izin vermek
w|normal|normal
v|beat|yenmek; dövmek
n|conference|konferans
a|double (adj.)|çift, iki kat
n|gas|gaz; benzin (ABD)
n|population|nüfus
v|to text|mesaj atmak
v|expect|beklemek (ummak)
v|double|iki katına çıkarmak
n|speed|hız
w|certainly|mutlaka
n|credit|kredi
w|female|kadın, dişi
w|individual|bireysel
w|nearly|neredeyse
w|particular|belirli
n|region|bölge
d|completely|tamamen
n|cross|çarpı, haç
n|focus (noun)|odak
n|a sort|tür, çeşit
n|tour|tur
w|welcome|hoş geldin
v|consider|göz önünde bulundurmak
v|drop|düşürmek
w|fair|adil
n|link|bağlantı
n|sale|satış
n|kid|çocuk
v|to link|bağlamak
n|car park|otopark
w|immediately|derhal
n|nature|doğa
v|note down|not almak
n|movement|hareket
n|scene|sahne
n|manager|müdür, yönetici
n|costs|maliyet
w|wide|geniş, uzak
n|coach|antrenör
v|to train|antrenman yapmak
w|heavy|ağır, zor
d|definitely|kesinlikle
n|gun|silah, tabanca
n|a search|arama
w|wow|vay
n|ability|yetenek
n|knowledge|bilgi
v|search|aramak
v|fit|uymak
n|opportunity|fırsat
n|author|yazar
n|leader|lider
n|material|malzeme
w|regular|düzenli
n|unit|birim
n|fear (noun)|korku
a|fit (adj.)|formda; uygun
n|lady|hanımefendi
n|secretary|sekreter
v|reach|ulaşmak
v|hurt|acıtmak|hurt · hurt
w|stupid|aptal
w|successful|başarılı
n|brain|beyin
w|physical|fiziksel
n|bar|bar; çubuk
a|hurt (adj.)|yaralı; kırgın
n|image|görüntü, imaj
n|degree|mezuniyet, derece
n|direction|yön
n|ship|gemi
w|active|aktif
w|independent|bağımsız
w|none|hiçbiri
w|free of charge|ücretsiz
n|cash|nakit
v|protect|korumak
n|secret|sır
d|clearly|açıkça
n|fan|hayran; vantilatör
n|learning|öğrenme
n|organization|kuruluş
a|secret (adj.)|gizli
n|capital city|başkent
n|skin|cilt
w|sweet|tatlı
w|necessary|gerekli
v|touch|dokunmak
v|dream|rüya görmek, hayal etmek|dreamt · dreamt
n|competition|rekabet
w|easily|kolayca
n|luck|şans
d|anyway|zaten, neyse
n|a dream|rüya, hayal
n|a finish|bitiş
v|to notice|fark etmek, aklında tutmak
w|closed|kapalı
n|disease|hastalık
n|driving|araba sürme
v|to fish|balık tutmak
n|a notice|duyuru; bildirim
n|professor|profesör
v|to carry on|devam etmek
n|crime|suç
w|male|erkek
v|to plant|dikmek
v|to explain|açıklamak
n|purpose|amaç
n|award|ödül
w|broken|kırık
n|a comment|yorum
n|equipment|ekipman
n|working student|öğrenci çalışan
p|on foot|yaya olarak
v|avoid|kaçınmak|+ -ing
v|catch|yakalamak|caught · caught
n|drug|ilaç; uyuşturucu
n|hall|salon; hol
n|pop|pop müzik
n|environment|çevre
n|coast|kıyı
n|city centre|şehir merkezi
n|condition|koşul
n|heat|ısı
v|to heat|ısıtmak
n|queen|kraliçe
n|app|uygulama
v|make worse|kötüleştirmek
n|distance|mesafe
v|accept|kabul etmek, varsaymak
v|receive|karşılamak; almak (sinyal), almak, teslim almak; korumak
w|mobile|mobil
v|serve|hizmet etmek
n|speech|konuşma
n|a ride|yolculuk, gezinti
n|police officer|polis memuru
n|screen|ekran
v|appear|görünmek, çıkmak (yayın)
n|engine|motor
v|lie|yatmak, bulunmak|lay · lain
n|square|kare, meydan, yer
v|worry|endişelenmek, ilgilenmek
n|bottom|dip
w|traditional|geleneksel
a|bottom (adj.)|en alttaki
a|square (adj.)|kare şeklinde
n|structure|yapı
n|solution|çözüm
n|university studies|üniversite eğitimi
n|wind|rüzgâr
w|mostly|çoğunlukla
n|wedding|düğün
w|fresh|taze
v|throw|atmak|threw · thrown
v|count|saymak
w|digital|dijital
n|owner|sahip
n|score|skor
v|realize|fark etmek
v|to score|sayı/gol atmak
a|separate (adj.)|ayrı
n|lake|göl
n|fashion|moda
v|pull|çekmek
n|feature|özellik
n|hill|tepe
n|profile|profil
v|push|itmek
n|seat|koltuk
n|target|hedef
n|benefit|yarar, fayda
n|metal|metal
n|understanding|anlayış
n|primary school|ilkokul
v|rise|yükselmek|rose · risen
w|silver|gümüş
n|ring|yüzük; zil
v|to ring|çalmak (zil/telefon)
v|apply|başvurmak, uygulamak
n|memory|bellek, depolama
v|enter|kaydetmek, yazmak
n|option|seçenek
n|prison|hapishane
a|adult (adj.)|yetişkin
n|method|yöntem
n|winner|kazanan
n|stone|taş
w|wild|vahşi
v|prevent|önlemek
n|trouble|dert
n|camp|kamp
d|extremely|son derece
n|construction site|şantiye, yol çalışması
n|advantage|avantaj
w|impossible|imkânsız
v|produce|üretmek
n|gift|hediye
n|progress|ilerleme
v|shut|kapatmak|shut · shut
n|wood|odun; orman
w|herself|kendisi (kadın)
a|shut (adj.)|kapalı
n|van|minibüs, kamyonet
v|decide|karar vermek
n|bridge|köprü
n|copy|kopya
w|patient|sabırlı
v|to copy|kopyalamak
n|background|arka plan
n|birth|doğum
w|lucky|şanslı
w|neither|hiçbiri
w|onto|üzerine
n|job application|iş başvurusu
n|job interview|iş görüşmesi
w|alive|canlı
n|request|istek
n|vehicle|araç
n|boss|patron
n|stop (bus|durak
n|corner|köşe
v|wake up|uyanmak|woke up · woken up
v|surprise|şaşırtmak
v|develop|gelişmek, geliştirmek
v|suggest|önermek
v|raise|artırmak
w|criminal|suçlu
n|variety|çeşitlilik
w|billion|milyar
v|to farm|çiftçilik yapmak
v|fix|tamir etmek; sabitlemek
n|a fly|sinek
n|guide|rehber
v|to guide|yol göstermek
n|a surprise|sürpriz
w|yours|seninki
w|dry|kuru
""",
"A2.2": """
n|injury|yaralanma
w|lovely|hoş
w|somewhere|bir yerde
n|per cent|yüzde
n|strategy|strateji
n|web|ağ; web
n|traffic light|trafik ışığı
v|exist|var olmak
n|medicine|ilaç
v|taste|tadı olmak
v|to reduce|azaltmak
n|stress|stres
n|audience|seyirci
w|excellent|mükemmel
v|mention|bahsetmek
v|to stress|vurgulamak; strese sokmak
n|a taste|tat; zevk
n|town hall|belediye binası
w|straight ahead|dümdüz
n|credit card|kredi kartı
n|sky|gökyüzü
n|valley|vadi
n|mobile phone|cep telefonu
w|electric|elektrikli
n|mail|posta
n|shape|şekil
n|assistant|asistan, yardımcı
a|flat (adj.)|düz
a|ill|hasta
v|to mail|postalamak
n|teaching|öğretmenlik, öğretim
n|bear|ayı
n|accident|kaza
v|promise|söz vermek
w|anywhere|herhangi bir yer
n|climate|iklim
n|discussion|tartışma
v|remove|kaldırmak
n|alternative|alternatif
n|flying|uçmak, uçuş
n|a promise|söz, vaat
n|moon|ay (gökyüzü)
n|forest|orman
n|crowd|kalabalık
n|ocean|okyanus
n|a suit|takım elbise
n|user|kullanıcı
v|jump|zıplamak, atlamak
w|suddenly|aniden
n|appearance|görünüş
n|a jump|atlama, sıçrama
n|survey|anket
n|train station|tren istasyonu
v|download|indirmek
w|surprised|şaşırmış
w|ancient|antik
w|express|hızlı
n|hero|kahraman
n|joke|şaka
n|planet|gezegen
w|soft|yumuşak
n|transport|taşıma
a|connected|bağlı
n|a download|indirme
n|ending|son, bitiş
v|to joke|şaka yapmak
n|platform|peron, ray
n|route|güzergâh, mesafe
n|lawyer|avukat
v|feed|beslemek|fed · fed
v|smoke|sigara içmek
n|device|cihaz
n|drama|dram
n|schedule|program
n|factor|etken
n|smoke (noun)|duman
v|pack|valiz hazırlamak
n|storm|fırtına
w|weak|zayıf, güçsüz
w|comfortable|rahat
w|everywhere|her yerde
n|hole|delik
v|perform|gerçekleştirmek; sahne almak
n|task|görev
n|climate change|iklim değişikliği
n|a cook|aşçı
n|temperature|sıcaklık
v|smile|gülümsemek
n|argument|tartışma; argüman
w|strange|garip
n|truck|kamyon
n|a smile|gülümseme
p|slowly|yavaş lütfen
w|zero|sıfır
n|neck|boyun, boğaz
w|incredible|inanılmaz
n|novel|roman
n|bowl|kâse
n|context|bağlam
a|worried|endişeli
d|unfortunately|maalesef
w|usual|olağan
n|wave|dalga
w|ourselves|kendimiz
n|cash machine|ATM
v|fail|başarısız olmak
v|fail (an exam)|sınavda kalmak
v|recommend|tavsiye etmek
w|bright|parlak
n|bank sort code|banka kodu
v|switch on|açmak
w|creative|yaratıcı
n|cycle|döngü
w|extreme|aşırı
v|to cycle|bisiklete binmek
a|scared|korkmuş
n|bank transfer|havale
v|hang up|telefonu kapatmak|hung up · hung up
a|careful|dikkatli
v|cry|ağlamak
w|empty|boş
n|danger|tehlike
n|prize|ödül
w|typical|tipik
v|affect|etkilemek
v|blow|esmek; üflemek
n|singing|şarkı söyleme
n|shopping list|alışveriş listesi
v|switch off|kapatmak
n|guest|misafir
n|possibility|olasılık
n|drawing|çizim
v|replace|yerine koymak, değiştirmek
v|chat|sohbet etmek (internette)
v|achieve|başarmak, ulaşmak
w|normally|normalde
n|item|öğe
n|a chat|sohbet
n|button|düğme
n|expert|uzman
v|suppose|varsaymak
n|tool|araç
v|identify|tespit etmek, tanımlamak
n|pattern|örüntü, kalıp
w|anybody|herhangi biri
n|basketball|basketbol
a|expert (adj.)|uzman
n|golf|golf
n|circle|daire
n|roof|çatı
n|plate|tabak
n|tip|bahşiş
v|attend|katılmak
w|brilliant|parlak
w|electronic|elektronik
n|error|hata
n|expression|ifade
n|factory|fabrika
n|manner|tarz
n|personality|kişilik
v|to circle|daire içine almak; dönmek
n|noise|gürültü
v|manage|başarmak, oluşturmak
w|wet|ıslak
v|print|yazdırmak
v|hide|saklamak|hid · hidden
n|advertising|reklamcılık
n|baseball|beyzbol
w|loud|gürültülü
v|burn|yanmak|burnt · burnt
n|height|yükseklik
v|respond|yanıt vermek
a|attractive|çekici
v|calm (sb) down|sakinleştirmek
v|destroy|yok etmek
n|introduction|giriş; tanıştırma
n|pilot|pilot
v|recognize|tanımak
n|smoking|sigara içme
n|lock|kilit, şato
n|comedy|komedi
n|plastic|plastik
a|exact|tam, kesin
v|to lock|kilitlemek
a|musical|müzikal, müzikle ilgili
a|plastic (adj.)|plastik
n|recording|kayıt
n|tie|kravat; beraberlik
v|to tie|bağlamak
n|tower|kule
n|wheel|tekerlek
n|employee|çalışan
n|engineer|mühendis
v|to shower|duş almak
n|lift|asansör
n|tradition|gelenek
v|to lift|kaldırmak
v|contain|içermek
n|permission|izin
n|reply|cevap
n|shoulder|omuz
n|document|belge
v|to reply|yanıtlamak
n|shopping centre|alışveriş merkezi
v|celebrate|kutlamak
v|smell|koklamak, kokmak|smelt · smelt
n|gallery|galeri
n|speaker|konuşmacı
n|a smell|koku
v|earn|kazanmak
n|finger|parmak
n|pocket|cep
n|pants|pantolon (ABD); külot (BrE)
n|soccer|futbol
n|ID card|kimlik
n|mirror|ayna
w|thin|ince
n|bone|kemik
n|gate|kapı
n|gap|açık, fark
n|clothing|giyim
a|everyday|gündelik
n|fishing|balıkçılık
n|parking|park etme
n|cloud|bulut
v|argue|tartışmak, kavga etmek, tartışmak, kavga etmek
w|thick|kalın, şişman
n|adventure|macera
w|awful|berbat
n|soldier|asker
d|carefully|dikkatlice
n|railway|demiryolu
n|a wash|yıkama
n|pet|evcil hayvan
v|wash up|bulaşık yıkamak; durulamak
n|castle|kale
n|charity|hayır kurumu
n|discovery|keşif
w|formal|resmî
n|palace|saray
v|refer|atıfta bulunmak
w|unusual|alışılmadık
w|badly|kötü şekilde
n|fiction|kurgu
w|ideal|ideal
n|explanation|açıklama
a|pleased|memnun
w|helpful|yardımsever
n|electricity|elektrik
n|belt|kemer
w|nervous|gergin
v|solve|çözmek
w|ordinary|sıradan
n|stomach|mide
n|architecture|mimari
n|designer|tasarımcı
a|electrical|elektrikli
n|hockey|hokey
n|lab|laboratuvar
n|virus|virüs
n|illness|hastalık
n|knife|bıçak
v|repair|tamir etmek
v|steal|çalmak|stole · stolen
n|mini-job|mini iş (az ücretli iş)
n|nurse|hemşire
n|sheet|yaprak, sayfa
n|desert|çöl
v|marry|evlenmek
w|nowhere|hiçbir yerde
n|physics|fizik
v|discover|keşfetmek
v|refuse|reddetmek|refuse to do sth
w|abroad|yurt dışı
v|compete|yarışmak
n|disaster|felaket
v|belong|ait olmak
n|journalist|gazeteci
n|lessons|ders (saat)
n|grass|çimen
v|connect|bağlamak
n|passenger|yolcu
n|possession|mülk
n|an experiment|deney
v|collect|toplamak, biriktirmek
w|scary|korkutucu
n|salary|maaş
w|self-employed|serbest çalışan
n|behaviour|davranış
w|asleep|uykuda
n|chemistry|kimya
v|knock|vurmak (kapı)
n|reporter|muhabir
n|twin|ikiz
a|twin (adj.)|ikiz
n|plastic bag|poşet
n|knee|diz
n|column|sütun
v|shake|sallamak|shook · shaken
w|wooden|ahşap
n|uniform|üniforma
n|underground|metro
a|underground (adj.)|yeraltı
n|symbol|sembol
n|chip|cips; çip
n|jazz|caz
v|invite|davet etmek
n|sauce|sos
n|toy|oyuncak
v|fall asleep|uykuya dalmak|fell asleep · fallen asleep
v|succeed|başarılı olmak
v|say goodbye|vedalaşmak
n|furniture|mobilya
n|beef|dana eti
n|celebrity|ünlü
w|intelligent|zeki
n|lifestyle|yaşam tarzı
v|involve|içermek, dahil etmek
a|surprising|şaşırtıcı
n|tourism|turizm
a|classical|klasik
n|instrument|enstrüman, alet
n|arrangement|düzenleme, anlaşma
w|enormous|muazzam
w|rude|kaba
n|spider|örümcek
w|lazy|tembel, çürük
n|habit|alışkanlık
n|swimming pool|yüzme havuzu
n|baker|fırıncı
n|laptop|dizüstü bilgisayar
v|complain|şikâyet etmek|complain about sth
n|brush|fırça
n|chef|aşçı
n|essay|deneme
n|recipe|tarif
n|suggestion|öneri
v|to brush|fırçalamak
d|differently|farklı şekilde
v|to photograph|fotoğrafını çekmek
n|pub|bar, birahane
n|reception|resepsiyon
n|biology|biyoloji
n|bin|çöp kovası
n|employer|işveren
n|school holidays|tatil (okul)
n|duck|ördek
w|clever|akıllı
n|detective|dedektif
d|correctly|doğru şekilde
n|farming|tarım
v|be bored|sıkılmak
v|communicate|iletişim kurmak
v|depend|bağlı olmak
n|pollution|kirlilik
n|customs|gümrük
n|poster|afiş, poster
n|carpet|halı
n|soap|sabun
n|runner|koşucu
d|sadly|ne yazık ki; üzgün şekilde
n|school-leaving exam (A levels)|lise bitirme sınavı
n|grammar|dilbilgisi
n|jam|reçel
n|grammar school|lise
v|react|tepki vermek
n|mathematics|matematik
d|quietly|sessizce
n|zoo|hayvanat bahçesi
n|computer scientist|bilgisayar bilimci
n|lecture|ders (üniversite)
w|blank|boş
n|instruction|talimat
n|invitation|davet
v|to lecture|ders vermek; nutuk atmak
a|teenage|ergen
n|ski|kayak (alet)
v|to ski|kayak yapmak
n|washing|çamaşır
n|stamp|mühür
n|athlete|sporcu
w|happily|mutlulukla
n|lemon|limon
n|laughter|gülüş
v|publish|yayımlamak
n|traffic jam|trafik sıkışıklığı
v|disappear|kaybolmak
n|diary|günlük
v|disagree|katılmamak
n|architect|mimar
n|cartoon|çizgi film; karikatür
v|predict|tahmin etmek
n|trainer|antrenör; spor ayakkabı
w|sunny|güneşli
n|quantity|miktar
n|continent|kıta
n|monkey|maymun
n|motorcycle|motosiklet
n|penny|peni
n|smartphone|akıllı telefon
v|shout|bağırmak
w|unhappy|mutsuz
n|cigarette|sigara
n|a shout|bağırış
n|rabbit|tavşan
n|lamp|lamba
n|oven|fırın
n|tablet|tablet; hap
w|divorced|boşanmış
n|invention|buluş
n|airline|havayolu
n|nut|fındık, ceviz; somun
n|civil servant|memur
n|semester|dönem
n|fork|çatal
n|goat|keçi
n|fridge|buzdolabı
n|instructor|eğitmen
n|musician|müzisyen
v|sail|yelken açmak
v|arrange|düzenlemek
v|borrow|ödünç almak
v|behave|davranmak
n|camping|kamp yapma
n|debts|borç
v|upload|yüklemek
n|sailing|yelkencilik
n|colleague|iş arkadaşı
n|bean|fasulye
a|crowded|kalabalık
v|organize|düzenlemek
n|headache|baş ağrısı
n|ankle|ayak bileği
d|fortunately|neyse ki
w|hers|onunki (kadın)
n|flu|grip
v|employ|istihdam etmek
n|businessman|iş adamı
n|overtime|fazla mesai
n|towel|havlu
n|painter|ressam
n|printer|yazıcı
n|driving licence|ehliyet
n|clearance sale|büyük indirim
v|recognise|tanımak, fark etmek
v|lend|ödünç vermek, almak|lent · lent
w|polite|nazik
n|researcher|araştırmacı
n|fog|sis
n|frog|kurbağa
n|fire brigade|itfaiye
n|spoon|kaşık
n|thief|hırsız
n|pharmacy|eczane
n|suburban train|banliyö treni
n|Wi-Fi|kablosuz internet
n|rubbish|çöp
w|informal|gayriresmî
v|surf|internette gezinmek; sörf yapmak
n|dentist|diş hekimi
v|bark|havlamak
d|secondly|ikinci olarak
n|ruler|cetvel
v|grill|ızgara yapmak
n|advertisement|reklam
n|skiing|kayak sporu
v|shave|tıraş etmek
v|boil|kaynatmak, haşlamak
n|luggage|bagaj
v|glue|yapıştırmak
n|surroundings|çevre
n|kindergarten|anaokulu
d|loudly|yüksek sesle
n|master's degree|yüksek lisans
n|insect|böcek
n|maths|matematik
w|rainy|yağmurlu
n|jewellery|takı
v|do crafts|el işi yapmak
w|firstly|ilk olarak
v|greet|selamlamak
n|petrol|benzin
n|petrol station|benzin istasyonu
n|bakery|fırın
n|intern|stajyer
a|noisy|gürültülü
v|pronounce|telaffuz etmek
v|advertise|reklamını yapmak
v|fetch|alıp getirmek
n|checkout|kasa
n|vocational training|mesleki eğitim
n|charger|şarj aleti
n|pavement|kaldırım
n|internship|staj
n|CV|özgeçmiş
n|sock|çorap
n|debit card|banka kartı
a|curly|kıvırcık
n|scissors|makas
w|windy|rüzgârlı
v|invent|icat etmek
n|programmer|yazılımcı
n|hen|tavuk
n|suitcase|bavul
w|cloudy|bulutlu
n|VAT|KDV
a|tidy|düzenli, derli toplu
v|comb|taramak (saç)
n|listener|dinleyici
n|bachelor's degree|lisans
w|humid|nemli
v|organise|organize etmek
n|traveller|yolcu, gezgin
n|crossroads|kavşak
n|tram|tramvay
n|motorway|otoyol
v|sew|dikiş dikmek|sewed · sewn
n|biscuit|bisküvi
n|timetable|tarife
n|cupboard|dolap
n|youth hostel|gençlik yurdu
n|shopping trolley|alışveriş arabası
v|recycle|geri dönüştürmek
n|cooker|ocak
n|excursion|gezi
n|rooster|horoz
n|electrician|elektrikçi
n|stair|basamak
v|unload|yük boşaltmak; daveti iptal etmek
n|craftsman|zanaatkâr, usta
v|bathe|banyo yapmak
n|lorry|kamyon
n|motorbike|motosiklet
w|foggy|sisli
n|hairdresser|kuaför
v|subtract|çıkarmak (matematik)
n|instalment|taksit
n|eraser|silgi
n|pensioner|emekli
n|salesperson|satıcı
v|refuel|benzin almak
n|butcher's|kasap
v|halve|ikiye bölmek
n|ballpoint pen|tükenmez kalem
n|IBAN|IBAN
n|satnav|navigasyon
""",
"B1.1": """
w|that|şu, o, ki
w|this|bu
n|a will|irade; vasiyet
n|like (noun)|beğeni
v|get on (well)|anlaşmak
w|now|şimdi
w|only (not until)|ancak, ilk olarak
w|these|bunlar
w|by the way|bu arada
w|at most|en fazla
w|those|şunlar
p|most of all|en çok
a|used|kullanılmış
w|in love|âşık
v|to state|belirtmek
v|think over|düşünüp taşınmak
w|back then|o zamanlar
v|go back|geri gitmek
v|give (as a present)|hediye etmek
v|to place|yerleştirmek
p|get used to|alışmak|+ -ing
v|come back|geri gelmek
v|set|oturtmak, koymak|set · set
n|a set|takım, set
p|take part in|katılmak|took part · taken part
n|free time|boş zaman
w|full|dolu
a|live (adj.)|canlı (yayın)
v|to point|işaret etmek
v|to water|sulamak
v|to call|seslenmek, çağırmak
v|to head|yönelmek
a|far (adj.)|uzak
w|though|gerçi, -se de
v|look around|etrafa bakmak
v|to open|açmak
p|put off|ertelemek|put off · put off
v|to face|yüzleşmek; bakmak
a|kind (adj.)|nazik
w|within|içinde
v|set off|yola çıkmak
p|run out of|tükenmek, bitmek|ran out · run out
w|at least|en az
v|to hand|uzatmak, vermek
a|level (adj.)|düz; eşit
n|court|mahkeme
v|take care of|ilgilenmek
v|to win|kazanmak|won · won
n|a win|galibiyet
v|be wrong|yanılmak
v|to close|kapatmak
d|close (adv.)|yakında, yakından
n|move (house)|taşınma
a|due|beklenen; vadesi gelmiş
v|get lost|yolunu kaybetmek
v|be happy|sevinmek
v|say thank you|teşekkür etmek
v|get along|iyi geçinmek
w|whether|-ip -mediğini
n|deal|anlaşma
p|deal with|ilgilenmek, başa çıkmak|dealt with
n|development|gelişme
w|well-known|tanınmış
v|go wrong|başarısız olmak (iş)
n|an act|eylem; yasa
v|to fire|ateş etmek; kovmak
a|living (adj.)|yaşayan
n|a living|geçim
v|to market|pazarlamak
v|pay off|karşılığını vermek
w|political|siyasi
v|take along|yanında götürmek
a|current|şimdiki, güncel
v|to experience|yaşamak, tecrübe etmek
v|to program|programlamak
v|to type|klavyede yazmak
v|meet (up)|buluşmak
p|for example|örneğin
v|to board|binmek (uçak/gemi)
n|a cut|kesik; kesinti
v|to force|zorlamak
n|issue|konu, sorun; sayı
n|force|kuvvet
v|miss (sb)|özlemek
n|sex|cinsiyet; seks
n|account|hesap
w|in total|toplamda
n|a lead|öncülük; ipucu
n|a share|pay; hisse
n|security|güvenlik
w|English|İngilizce
w|hard-working|çalışkan
w|private|özel, kişisel
v|to view|görmek; değerlendirmek
n|public office|resmî daire
v|to result|sonuçlanmak
p|above all|her şeyden önce
n|policy|politika, ilke
v|wish for|dilemek, istemek
n|original|asıl, orijinal
v|press|basmak, itmek
n|the press|basın
a|worth|değer
n|performance|performans
w|cool|serin
n|a value|değer
v|to come across|karşılaşmak (+ Dativ)
n|tax|vergi
v|to tax|vergilendirmek
v|be worth it|değmek
n|production|üretim
n|stuff|şey(ler)
n|management|yönetim
n|range|aralık; yelpaze
v|to trade|ticaret yapmak
w|central|merkezi
n|trade|ticaret
w|upon|üzerine
w|various|çeşitli
n|hate (noun)|nefret
v|to vote|oy vermek
n|property|mülk
n|vote|oy
w|related|akraba
a|involved|dahil, ilgili
w|economic|ekonomik
n|release|yayın; serbest bırakma
v|to release|serbest bırakmak; yayımlamak
a|written|yazılı
v|to lose|kaybetmek|lost · lost
n|cover|kapak
n|election|seçim
w|simply|basitçe
n|staff|personel
n|union|birlik; sendika
d|currently|şu anda
a|financial|mali, finansal
a|legal|yasal, hukuki
w|daily|günlük
n|loss|kayıp
n|version|sürüm
v|pick up|teslim almak
v|to forget|unutmak|forgot · forgotten
v|pass (time)|geçmek (zaman)
v|fall in love|âşık olmak
v|risk|risk almak
n|access|erişim
n|base|temel; üs
w|deep|derin
n|truth|gerçek
v|to access|erişmek
v|to base|dayandırmak
n|a pass|paso; pas
n|a risk|risk
w|Europe|Avrupa
v|fall in love with|-e âşık olmak
v|to look forward to|dört gözle beklemek
n|a mine|maden; mayın
v|to note|not etmek; dikkat etmek
w|allowed|izinli
v|respect|saygı duymak
n|growth|büyüme
n|respect (noun)|saygı
n|standard|standart
v|bring along|yanında getirmek
n|charge|ücret; suçlama
n|album|albüm
v|to charge|ücret almak; şarj etmek; suçlamak
v|to store|depolamak
v|stay behind|geride kalmak
n|treatment|tedavi
n|addition|ekleme
w|ahead|ileride
n|pressure|baskı
a|western|batı, batılı
n|social security|sosyal sigorta
v|sort|ayırmak, sıralamak
n|campaign|kampanya
n|content|içerik
w|despite|-e rağmen
v|to campaign|kampanya yürütmek
a|leading|önde gelen
n|contact|iletişim
w|throughout|boyunca
v|to contact|iletişime geçmek
n|a drop|damla; düşüş
v|to tour|gezmek, turne yapmak
v|drop by|uğramak
w|unless|-medikçe
d|absolutely|kesinlikle
n|safety|güvenlik
n|episode|bölüm
n|collection|koleksiyon
v|to coach|çalıştırmak, koçluk yapmak
a|expected|beklenen
d|particularly|özellikle
w|German|Almanca
n|tax office|vergi dairesi
v|claim|iddia etmek
v|fear|korkmak
w|global|küresel
n|judge|hâkim
n|a claim|iddia; talep
d|generally|genellikle
v|to judge|yargılamak, değerlendirmek
w|plus|artı
w|France|Fransa
w|finished|bitmiş, hazır
n|battle|savaş
v|to rule|yönetmek
d|seriously|ciddi şekilde
w|Russia|Rusya
v|pay attention|dikkat etmek
v|drive past|yanından geçip gitmek
v|wonder|merak etmek
w|worst|en kötü
n|wonder (noun)|hayranlık; mucize
v|turn round|çevirmek, döndürmek
n|impact|etki
n|effort|çaba
w|commercial|ticari
n|lack|eksiklik
n|operation|işlem; ameliyat
n|fighting|çatışma, kavga
v|to impact|etkilemek
v|to lack|yoksun olmak
a|latest|en son
n|marriage|evlilik
w|direct|doğrudan
n|a touch|dokunuş
w|Germany|Almanya
n|doubt|şüphe
n|damage|hasar
w|glad|memnun
v|to damage|hasar vermek
d|directly|doğrudan
v|to doubt|şüphe etmek
n|planning|planlama
p|carry on|devam etmek
w|basic|temel
n|captain|kaptan
w|effective|etkili
w|highly|son derece
n|reality|gerçeklik
n|spot|nokta, yer
w|worse|daha kötü
n|challenge|zorluk, meydan okuma
d|eventually|sonunda
v|make an effort|çaba göstermek
v|comment|yorum yapmak
n|block|blok
n|nation|ulus
w|primary|birincil
w|responsible|sorumlu
n|agreement|anlaşma
v|to award|ödül vermek
v|to block|engellemek
n|killing|öldürme
n|theory|teori
d|therefore|bu nedenle
n|politics|siyaset
v|get worse|kötüleşmek
n|economy|ekonomi
n|application|başvuru
v|sit down|oturmak
w|complex|karmaşık
n|location|konum
n|murder|cinayet
a|located|bulunan, konumlu
v|to murder|öldürmek (cinayet)
v|exchange|değiştirmek (ürün)
n|channel|kanal
w|powerful|güçlü
w|religious|dini
w|royal|kraliyet
n|an exchange|değişim, takas
a|northern|kuzey
n|job centre|iş kurumu
v|lie (tell lies)|yalan söylemek|lied · lied
n|a lie|yalan
a|southern|güney
n|a worry|endişe
v|to lie (down)|uzanmak, yatmak
v|separate|ayırmak
n|brand|marka
w|mental|zihinsel
v|remain|kalmak
w|smart|zeki
n|surface|yüzey
n|a count|sayım
a|covered|kaplı, örtülü
d|previously|daha önce
d|totally|tamamen
v|click|tıklamak
n|generation|nesil
v|to benefit|yararlanmak
n|a click|tıklama
v|to feature|yer vermek, içermek
n|a pull|çekiş
n|a push|itiş
a|sexual|cinsel
v|apply for|başvurmak
n|opening hours|açılış saatleri
v|to apply for|başvurmak
v|waste|israf etmek
v|spread|yaymak|spread · spread
n|supply|arz
n|basis|temel
n|authority|yetki; otorite
n|agent|temsilci, ajan
n|a rise|artış, yükseliş
v|to supply|tedarik etmek
a|waste (adj.)|atık
n|waste (noun)|atık; israf
n|grade|not
n|strength|güç
n|engineering|mühendislik
d|obviously|açıkça, belli ki
v|improve|geliştirmek
w|indeed|gerçekten
n|spirit|ruh
w|till|-e kadar
w|proud|gururlu
v|influence|etkilemek
v|require|gerektirmek
w|apart|ayrı
a|aware|farkında|aware of sth
a|eastern|doğu
n|function|işlev
n|influence (noun)|etki
n|marketing|pazarlama
w|nor|ne de
v|prove|kanıtlamak
n|software|yazılım
n|host|ev sahibi; sunucu
n|length|uzunluk
w|rare|nadir
n|setting|ortam; ayar
n|journal|dergi; günlük
d|possibly|muhtemelen
v|throw away|çöpe atmak
n|connection|bağlantı, hat
n|balance|denge
n|magic|sihir
n|ad|ilan, reklam
v|to balance|dengelemek
a|magic (adj.)|sihirli
n|net|ağ, file
v|to request|rica etmek, talep etmek
n|stick|sopa, çubuk
v|to stick|yapıştırmak
n|responsibility|sorumluluk
v|treat|tedavi etmek; davranmak
n|file|dosya
n|beauty|güzellik
w|technical|teknik
n|youth|gençlik
a|cultural|kültürel
n|roll|rulo; ekmek (küçük)
v|to roll|yuvarlamak
d|slightly|biraz
n|religion|din
v|iron|ütü yapmak
v|appreciate|takdir etmek, değerini bilmek
n|edge|kenar
w|forever|sonsuza dek
n|iron (metal)|demir
a|mad|deli; kızgın
a|prepared|hazır
n|reference|referans, atıf
a|honest|dürüst
v|reduce|azaltmak
n|guard|bekçi
w|nuclear|nükleer
n|reaction|tepki
v|shoot|ateş etmek|shot · shot
w|solid|katı, sağlam
v|to guard|korumak
n|a mention|söz etme
n|port|liman
n|emergency|acil durum
n|fuel|yakıt
v|kick|tekmelemek
w|plenty|bol
n|prince|prens
w|proper|uygun
n|a kick|tekme
w|warm|ılık, sıcak
n|duty|görev
n|path|patika
a|advanced|ileri, gelişmiş
a|alternative (adj.)|alternatif
n|a mix|karışım
v|to mix|karıştırmak
n|spending|harcama
n|official notice|karar yazısı
v|suit|yakışmak, durmak
n|border|sınır
n|enemy|düşman
n|intelligence|zekâ; istihbarat
n|limit|sınır
n|profit|kâr
a|environmental|çevresel
a|fixed|sabit
v|to limit|sınırlamak
w|historical|tarihî
w|native|yerli; ana
n|update|güncelleme
d|originally|aslında, başlangıçta
v|to update|güncellemek
v|be surprised|şaşırmak
n|communication|iletişim
n|flow|akış
w|illegal|yasa dışı
v|to flow|akmak
v|to transport|taşımak
n|entry|giriş
w|scientific|bilimsel
n|candidate|aday
n|payment|ödeme
n|studio|stüdyo
n|a pack|paket
v|to measure|ölçmek
v|get angry|sinirlenmek
n|measure|önlem
n|chain|zincir
w|equal|eşit
n|identity|kimlik
n|chapter|bölüm
d|specifically|özellikle
n|citizens' office|nüfus dairesi
v|fill in|doldurmak
w|approximately|yaklaşık
v|lay|yatırmak, koymak|laid · laid
n|talent|yetenek
a|determined|kararlı
n|an escape|kaçış
v|to escape|kaçmak
d|properly|düzgünce, doğru şekilde
v|determine|belirlemek
n|stadium|stadyum
a|obvious|apaçık
a|experienced|deneyimli
w|whenever|her ne zaman
n|champion|şampiyon
n|editor|editör
w|giant|dev
n|signal|sinyal
n|theme|tema
w|tiny|minicik
n|literature|edebiyat
v|to signal|işaret vermek
d|typically|tipik olarak
v|to wave|el sallamak
v|to recommend|tavsiye etmek
n|wing|kanat
a|essential|temel, şart
n|alcohol|alkol
w|drunk|sarhoş
w|familiar|tanıdık
w|guilty|suçlu
w|unable|yapamayan
w|upset|üzgün
a|medium (adj.)|orta
d|perfectly|mükemmel şekilde
n|goods|ürün, mal
n|bomb|bomba
n|entertainment|eğlence
v|hang|asmak|hung · hung
v|to bomb|bombalamak
a|educational|eğitici, eğitimle ilgili
d|mainly|başlıca, çoğunlukla
n|row|sıra
v|to switch|değiştirmek
n|bell|zil, çan
n|warning|uyarı
v|kiss|öpmek
v|to rent|kiralamak
n|rent|kira
n|attitude|tutum
n|branch|dal; şube
n|flag|bayrak
n|plot|olay örgüsü; arsa
v|represent|temsil etmek
v|admit|itiraf etmek, kabul etmek
n|definition|tanım
n|frame|çerçeve
v|to frame|çerçevelemek
""",
"B1.2": """
n|a kiss|öpücük
v|rent out|kiraya vermek
w|tight|dar
n|shift|vardiya
w|academic|akademik
w|chemical|kimyasal
w|competitive|rekabetçi
n|mess|dağınıklık
n|pleasure|zevk
w|unlike|-in aksine
n|yard|bahçe; yarda
v|afford|(maddi olarak) gücü yetmek
v|tend|eğiliminde olmak
n|category|kategori
d|personally|şahsen
n|Turkey|Türkiye
v|to describe|tarif etmek
v|promote|teşvik etmek; terfi ettirmek
n|consumer|tüketici
n|employment|istihdam
n|importance|önem
n|victim|kurban
d|frequently|sık sık
v|deliver|teslim etmek
n|arrest|tutuklama
w|surely|elbette
v|to arrest|tutuklamak
n|ban|yasak
v|to ban|yasaklamak
v|to tip|bahşiş vermek
w|calm|sakin
n|sight (tourist attraction)|turistik yer
v|quit|işten ayrılmak, çıkarmak
n|client|müşteri
n|weapon|silah
d|heavily|yoğun şekilde, ağır
a|worldwide|dünya çapında
w|hardly|neredeyse hiç
w|secondary|ikincil
n|princess|prenses
n|sample|örnek, numune
v|calm down|sakinleşmek
n|battery|batarya
n|breath|nefes
n|chest|göğüs
n|decade|on yıl
w|immediate|ani, derhal
v|survive|hayatta kalmak
a|engaged|nişanlı; meşgul
d|regularly|düzenli olarak
n|cap|bere
n|trend|eğilim, trend
n|childhood|çocukluk
n|an aim|amaç
v|to aim|hedeflemek
n|campus|kampüs
n|comparison|karşılaştırma
a|injured|yaralı
n|a musical|müzikal
a|organized|düzenli, organize
n|a quote|alıntı
v|to quote|alıntı yapmak
a|valuable|değerli
n|tax ID|vergi numarası
w|fairly|epey
n|graduate|mezun
a|aged|yaşında
v|to graduate|mezun olmak
n|racing|yarış
n|appointment|randevu
n|coal|kömür
v|hunt|avlamak
w|rough|kaba; pürüzlü
d|effectively|etkili şekilde
a|historic|tarihi
n|improvement|gelişme, iyileşme
n|a repeat|tekrar
w|practical|pratik
v|ignore|görmezden gelmek
d|meanwhile|bu arada
w|relative|göreli; akraba
w|sharp|keskin
n|trick|hile
d|naturally|doğal olarak
d|necessarily|zorunlu olarak
n|percentage|yüzde
v|to trick|kandırmak
v|occur|meydana gelmek
w|impressive|etkileyici
a|confused|kafası karışmış
d|strongly|şiddetle, kuvvetle
n|technique|teknik
v|wash (oneself)|yıkanmak
n|atmosphere|atmosfer
n|belief|inanç
n|package|paket
n|poverty|yoksulluk
w|qualified|nitelikli
w|violent|şiddetli
n|contrast|zıtlık
v|to contrast|karşılaştırmak
n|element|öğe
v|to compare|karşılaştırmak
v|suffer|acı çekmek, maruz kalmak
v|encourage|cesaretlendirmek
w|innocent|masum
n|mystery|gizem
n|protest|protesto
w|silent|sessiz
n|photography|fotoğrafçılık
v|to protest|protesto etmek
a|spoken|sözlü, konuşulan
d|successfully|başarıyla
n|happiness|mutluluk, şans
n|mood|keyif, ruh hâli, atmosfer
n|arrival|varış
w|horrible|korkunç
n|muscle|kas
n|passion|tutku
n|producer|yapımcı
a|retired|emekli
n|sand|kum
n|tape|bant
w|confident|kendinden emin
n|custom|gelenek
n|horror|dehşet
w|romantic|romantik
n|label|etiket
v|to label|etiketlemek
n|immigration office|yabancılar dairesi
w|disappointed|hayal kırıklığına uğramış
w|rarely|nadiren
v|assist|yardım etmek
n|ceremony|tören
n|ghost|hayalet
v|participate|katılmak
n|prayer|dua
n|soil|toprak
w|ugly|çirkin
n|diamond|elmas
a|dressed|giyinik
a|odd|tuhaf; tek (sayı)
v|get dressed|giyinmek
n|dust|toz
w|remote|uzak
n|a repair|tamir
n|case worker|dosya sorumlusu
v|explain in detail|izah etmek
n|pot|tencere
v|hire|işe almak
v|confirm|doğrulamak, teyit etmek
n|layer|katman
n|poetry|şiir
v|pray|dua etmek
w|smooth|pürüzsüz
n|string|ip
w|sudden|ani
a|annoying|sinir bozucu
n|conclusion|sonuç
n|rugby|ragbi
n|fitness|fitness
n|friendship|arkadaşlık
n|pan|tava
n|entrance|giriş
v|reflect|yansıtmak, düşünüp taşınmak
n|resource|kaynak
v|bother|rahatsız etmek
w|equally|eşit şekilde
n|liquid|sıvı
n|narrative|anlatı
w|silly|aptalca
n|translation|çeviri
a|liquid (adj.)|sıvı
n|shell|kabuk
v|experiment|deney yapmak
w|suitable|uygun
n|occasion|vesile
d|incredibly|inanılmaz derecede
n|currency|para birimi
n|exhibition|sergi
v|remind|hatırlatmak
n|tongue|dil (organ)
n|seed|tohum
n|summary|özet
n|achievement|başarı, kazanım
n|script|senaryo; betik
n|tube|tüp; metro (Londra)
v|expand|genişletmek
v|know one's way around|bir konuyu iyi bilmek
n|discount|indirim
v|indicate|göstermek, belirtmek
w|fancy|şık
w|grateful|minnettar
n|impression|izlenim
n|leather|deri
n|luxury|lüks
n|cotton|pamuk
n|a knock|vuruş, kapı çalma
a|luxury (adj.)|lüks
n|tail|kuyruk
n|flood|sel
v|to flood|su basmak
n|punishment|ceza
w|brave|cesur
v|commit|taahhüt etmek, adamak
n|difficulty|zorluk
n|intention|niyet
v|pretend|-miş gibi yapmak
n|priest|rahip
n|a shake|sallama; milkshake
n|mother tongue|ana dil
w|occupied|dolu, meşgul
v|invest|yatırım yapmak
n|complaint (return)|şikâyet, iade talebi
w|frozen|donmuş
w|painful|acı verici
n|Federal Employment Agency|iş ajansı
v|define|tanımlamak
n|favour|iyilik
v|investigate|soruşturmak, araştırmak
v|bite|ısırmak|bit · bitten
n|laboratory|laboratuvar
n|relation|ilişki
w|unlikely|olası değil
n|announcement|duyuru
n|a bite|ısırık
n|documentary|belgesel
v|explore|keşfetmek
n|presentation|sunum
n|throat|boğaz
d|similarly|benzer şekilde
a|talented|yetenekli
n|celebration|kutlama
v|rely on|güvenmek, bel bağlamak
a|reliable|güvenilir
a|educated|eğitimli
n|mall|alışveriş merkezi
w|Turkish|Türkçe
n|alarm|alarm
w|peaceful|barışçıl
n|stranger|yabancı
n|volunteer|gönüllü
n|breathing|nefes alma
n|photographer|fotoğrafçı
n|pin|toplu iğne; PIN
v|to pin|iğnelemek, sabitlemek
n|printing|baskı
a|repeated|tekrarlanan
v|to volunteer|gönüllü olmak
v|convince|ikna etmek
v|breathe|nefes almak
v|announce|duyurmak
w|lonely|yalnız
n|pipe|boru
n|powder|toz
n|garage|garaj
n|poem|şiir
v|export|ihraç etmek
w|jealous|kıskanç
n|destination|varış yeri
n|dirt|kir
v|gather|toplamak
v|relate|ilişkilendirmek
n|an export|ihracat
n|robot|robot
n|Switzerland|İsviçre
v|to complain|şikâyet etmek
w|outdoor|açık hava
n|substance|madde
n|departure|kalkış
n|explosion|patlama
n|leaf|yaprak
w|pleasant|hoş
n|portrait|portre
n|a climb|tırmanış
a|folk|halk (müziği vb.)
n|unemployment|işsizlik
n|work permit|çalışma izni
v|highlight|öne çıkarmak, vurgulamak
w|continuous|sürekli
n|fence|çit
n|a highlight|en önemli an
n|nail|tırnak; çivi
n|poet|şair
v|sink|batmak
n|a swim|yüzme
v|depend on|bağlı olmak
v|attract|çekmek
w|generous|cömert
n|prisoner|mahkûm
v|qualify|hak kazanmak, nitelendirmek
n|emotion|duygu
n|excitement|heyecan
w|uncomfortable|rahatsız
n|coin|madeni para
n|ceiling|tavan, battaniye
n|heating|kalorifer
n|assignment|ödev, görev
n|clue|ipucu
n|grain|tahıl
w|unnecessary|gereksiz
n|costume|kostüm
v|examine|incelemek, muayene etmek
n|mixture|karışım
w|gentle|nazik
w|unfair|haksız
v|shine|parlamak
w|shy|utangaç
n|politician|politikacı
v|apologize|özür dilemek
n|bubble|kabarcık
n|gentleman|beyefendi
w|ours|bizimki
w|convenient|kullanışlı
n|earthquake|deprem
a|embarrassing|utandırıcı
n|pension insurance|emeklilik sigortası
v|hurry|acele etmek
n|a hurry|acele
n|profession|meslek
v|combine|birleştirmek
w|keen|istekli
n|a bend|viraj, dönemeç
v|to bend|bükmek, eğilmek
a|fascinating|büyüleyici
n|helicopter|helikopter
n|lip|dudak
n|mud|çamur
v|divide|bölmek (matematik)
w|cruel|zalim
n|keyboard|klavye
n|attraction|cazibe
v|freeze|donmak|froze · frozen
w|mild|ılımlı
n|drum|davul
v|import|ithal etmek
n|hurricane|kasırga
v|pour|dökmek
n|an import|ithalat
n|liability insurance|sorumluluk sigortası
n|bee|arı
v|advise|tavsiye etmek; tahmin etmek
w|indoor|kapalı alan
v|intend|niyet etmek
n|recommendation|tavsiye
n|servant|hizmetçi
n|statue|heykel
w|exhausted|tükenmiş
n|bride|gelin
v|fold|katlamak
w|pale|solgun
n|poison|zehir
v|to poison|zehirlemek
w|Austria|Avusturya
v|concentrate|odaklanmak
v|scan|taramak
n|consequence|sonuç
n|supporter|destekçi
n|toe|ayak parmağı
v|be ashamed|utanmak
n|accommodation|konaklama
v|cheat|hile yapmak
n|rope|ip
n|a cheat|hilekâr
n|tent|çadır
v|retire|emekli olmak
a|embarrassed|mahcup
v|donate|bağışlamak
n|immigrant|göçmen
d|backwards|geriye doğru
v|to reject|reddetmek
n|fur|kürk, tüy
n|cloth|kumaş
n|headline|manşet
n|container|kap; konteyner
n|tin|teneke; konserve kutusu
n|shelf|raf
v|warn|uyarmak
a|disappointing|hayal kırıklığı yaratan
a|relaxed|rahat
n|a sail|yelken
n|registration certificate|ikamet belgesi
n|flour|un
n|cottage|kır evi
w|indirect|dolaylı
n|slice|dilim
v|to slice|dilimlemek
v|weigh|tartmak
n|clause|madde
n|expedition|keşif gezisi
n|residence permit|oturma izni
n|needle|iğne
w|sensible|mantıklı
v|admire|hayran olmak
w|forbidden|yasak
n|underwear|iç çamaşırı
n|prediction|tahmin
w|theirs|onlarınki
n|reservation|çekince; rezervasyon
v|punish|cezalandırmak
a|ambitious|hırslı
a|annoyed|sinirli
v|swap|takas etmek
n|neighbourhood|mahalle
v|consist|-den oluşmak
v|locate|yerini bulmak
v|translate|çevirmek
a|old-fashioned|eski moda
p|luckily|neyse ki
n|receipt|fiş
n|countryside|kırsal
v|educate|eğitmek
n|leisure|boş zaman
n|sculpture|heykel
a|coloured|renkli
v|bake|fırında pişirmek
n|ambition|hırs
n|wool|yün
a|alcoholic|alkollü
a|amazed|hayran, şaşkın
n|broadcasting fee (TV licence)|yayın katkı payı
w|unemployed|işsiz
v|conclude|sonuca varmak; bitirmek
a|relaxing|rahatlatıcı
v|fry|kızartmak
v|bury|gömmek
v|dislike|sevmemek
n|a dislike|hoşlanmama
v|consume|tüketmek
n|qualification|nitelik
w|shiny|parlak
n|curtain|perde
n|diagram|şema
v|entertain|eğlendirmek
v|persuade|ikna etmek
n|competitor|rakip
w|spicy|acı, keskin
v|explode|patlamak
w|unpleasant|tatsız
w|imaginary|hayali
w|jointly|ortaklaşa
w|definite|kesin
n|queue|kuyruk
v|to queue|kuyrukta beklemek
n|sailor|denizci
n|queue number|sıra numarası
n|viewer|izleyici
v|attach|eklemek
n|ingredient|malzeme
a|frightened|korkmuş
n|glove|eldiven
n|nationality|uyruk
n|disadvantage|dezavantaj
d|outdoors|açık havada
w|gladly|memnuniyetle
v|confuse|kafasını karıştırmak
a|frightening|korkutucu
v|apologise|özür dilemek|apologise for sth
n|loneliness|yalnızlık
w|fashionable|modaya uygun
n|symptom|belirti
a|careless|dikkatsiz
a|cheerful|neşeli
d|indoors|içeride
n|similarity|benzerlik
n|organizer|düzenleyici
a|poisonous|zehirli
v|prepare oneself|hazırlanmak
n|tyre|lastik
n|quotation|alıntı; fiyat teklifi
v|revise|gözden geçirmek, revize etmek
v|analyse|analiz etmek
n|boredom|can sıkıntısı
v|annoy|kızdırmak
v|inform oneself|bilgi almak
n|statistic|istatistik
v|mourn|ağıt yakmak, yasını tutmak
v|decorate|süslemek
v|injure|yaralamak
v|lament|yakınmak
v|summarize|özetlemek
v|foresee|önceden görmek|foresaw · foreseen
v|frighten|korkutmak
v|worsen|kötüleştirmek
v|unpack|paketi açmak
v|fasten|sabitlemek
v|get undressed|soyunmak
n|deregistration|kayıt sildirme
""",
"B2.1": """
p|get by|idare etmek, geçinmek
p|get on with|iyi geçinmek, devam etmek
n|being|varlık
n|make-up|makyaj
p|take on|üstlenmek, işe almak
p|back up|desteklemek; yedeklemek
p|make up for|telafi etmek|made up for
p|work out|çözmek; spor yapmak
p|be that as it may|öyle olsa bile
p|take up|başlamak (hobi), yer kaplamak
p|go over|gözden geçirmek
w|high|yüksek
p|give in|pes etmek, boyun eğmek
p|take over|devralmak, üstlenmek|took over · taken over
v|to found|kurmak (kurum)
p|come up with|(fikir) bulmak|came up with
p|that being said|bununla birlikte
p|back down|geri adım atmak
p|go through|(zor bir süreç) yaşamak
w|free|özgür, boş
p|look into|incelemek, araştırmak
p|keep up with|ayak uydurmak
a|so-called|sözde
p|set out|yola koyulmak, ortaya koymak
p|set up|kurmak
p|get away with|(cezasız) sıyrılmak|got away with
p|point out|belirtmek, dikkat çekmek
p|in line with|-ile uyumlu olarak
n|means|araç, yol
p|on the whole|genel olarak
d|in any case|her halükârda
v|to level|düzleştirmek
p|run into|rastlamak; karşılaşmak
p|given that|-diği göz önüne alınırsa
w|wrong|yanlış
p|call off|iptal etmek
w|low|alçak
p|in light of|-ışığında
p|in the long run|uzun vadede
w|former|eski, önceki
n|a current|akıntı; akım
v|to process|işlemek
n|self|benlik
p|bring up|gündeme getirmek, yetiştirmek
v|to issue|çıkarmak, yayımlamak
n|shot|atış; çekim
p|turn down|reddetmek
w|military|askerî
p|account for|açıklamak, -in nedeni olmak
n|county|ilçe, kontluk
p|hold on|beklemek, tutunmak
p|with a view to|-mek amacıyla
p|cut back on|kısmak, azaltmak
p|cut off|kesmek, bağlantıyı koparmak
v|value|değer vermek; tahmin etmek
w|official|resmî
v|trust|güvenmek
w|federal|federal
n|league|lig
a|long-term|uzun vadeli
v|to model|modellemek; mankenlik yapmak
p|hold back|geri tutmak, çekinmek
p|stand out|öne çıkmak
p|follow up|takip etmek, peşini bırakmamak
n|chief|şef
v|lower|indirmek
n|hell|cehennem
n|lord|lord, efendi
v|to stage|sahnelemek
n|terms|şartlar
w|entire|bütün
n|council|konsey
a|super|süper
v|to figure|düşünmek, sanmak
p|fall through|suya düşmek
p|figure out|çözmek, anlamak
n|district|semt
n|minister|bakan
a|limited|sınırlı
a|moving|dokunaklı; hareketli
w|via|üzerinden
n|association|dernek
n|committee|komite
a|potential (adj.)|olası
p|put forward|öne sürmek
p|sort out|halletmek
a|significant|önemli
w|beyond|ötesinde
a|additional|ek, ilave
a|short-term|kısa vadeli
n|construction|inşaat
n|justice|adalet
n|income|gelir
n|majority|çoğunluk
a|clear-cut|net
w|annual|yıllık
w|anymore|artık (olumsuz)
n|contract|sözleşme
n|insurance|sigorta
n|opening|açılış; açıklık
n|administration|yönetim
w|civil|sivil
n|master|usta
n|stock|stok; hisse
n|approach|yaklaşım
n|cancer|kanser
w|multiple|birden çok
w|senior|kıdemli
d|thus|böylece
v|address|(sorunu) ele almak
n|commission|komisyon
a|grand|görkemli, büyük
d|literally|kelimenin tam anlamıyla
v|notice|fark etmek
a|gay|eşcinsel
d|if necessary|gerekirse
w|fully|tamamen
a|associated|ilişkili
p|carry out|yürütmek, gerçekleştirmek
w|holy|kutsal
w|otherwise|yoksa, başka
n|agency|ajans
n|cell|hücre
w|executive|yönetici
n|mass|kütle
n|mission|görev
n|status|durum
n|trial|duruşma; deneme
w|truly|gerçekten
n|division|bölüm
n|freedom|özgürlük
v|attempt|teşebbüs etmek
w|actual|gerçek
w|prior|önceki
n|protection|koruma
w|whom|kimi
n|finding|bulgu
n|species|tür
p|catch up on|telafi etmek
n|demand|talep
n|investment|yatırım
v|to structure|yapılandırmak
n|budget|bütçe
n|faith|inanç
n|fund|fon
n|arms|silahlar
n|estate|mülk; site
a|failed|başarısız
n|hearing|işitme; duruşma
n|rose|gül
v|gain|kazanmak
w|prime|asıl
n|soul|ruh
w|weird|tuhaf
d|apparently|görünüşe göre
n|institute|enstitü
n|chairman|başkan
n|edition|baskı
v|handle|üstesinden gelmek, idare etmek
n|firm|firma
n|a bet|bahis
v|to bet|bahse girmek
n|cast|oyuncu kadrosu
v|to cast|atmak; rol vermek
v|to function|işlemek, çalışmak
n|shooting|silahlı saldırı; çekim
w|tough|zor, sert
n|housing|konut
n|leadership|liderlik
n|fellow|adam; dost
w|unique|eşsiz
n|violence|şiddet
n|aid|yardım
v|to aid|yardım etmek
a|concerned|endişeli; ilgili
n|investigation|soruşturma
w|evil|kötü
n|parliament|meclis
n|core|çekirdek
n|presence|varlık
n|victory|zafer
a|democratic|demokratik
w|classic|klasik
w|entirely|tamamen
n|failure|başarısızlık
w|initial|ilk
w|massive|devasa
w|regional|bölgesel
n|session|oturum
w|toward|-e doğru
w|upper|üst
n|zone|bölge
v|transfer|aktarmak; yayınlamak
a|willing|istekli
n|capacity|kapasite, yetenek
n|governor|vali
w|industrial|sanayi
w|joint|ortak
n|purchase|satın alma
n|steel|çelik
v|ensure|sağlamak, garantiye almak
n|labour|emek
n|command|komut
n|crew|mürettebat
n|proof|kanıt, belge
a|intended|amaçlanan
n|debt|borç
w|domestic|yurt içi; ev içi
v|launch|başlatmak
n|minimum|asgari
v|to survey|anket yapmak; incelemek
n|loan|kredi
w|stuck|sıkışmış
n|appeal|çekicilik, itiraz
w|applied|uygulamalı
w|golden|altın
v|grant|tanımak, vermek
a|appropriate|uygun
n|era|çağ, dönem
n|testing|test etme
w|emotional|duygusal
w|internal|iç
n|sector|sektör
n|strike|grev
n|concern|endişe; mesele
v|maintain|sürdürmek, savunmak
n|advance|ilerleme
n|confidence|güven
w|cute|sevimli
w|fake|sahte
n|finance|finans
v|split|bölmek|split · split
w|urban|kentsel
n|conflict|çatışma
w|corporate|kurumsal
n|debate|tartışma
n|fault|hata, kusur
w|pure|saf
n|revenue|gelir
v|secure|güvence altına almak; yedeklemek
n|aircraft|uçak
n|distribution|dağıtım
a|mixed|karışık
v|bear in mind|akılda tutmak
v|blame|suçlamak
n|coverage|kapsam; haberleştirme
n|display|ekran
n|surgery|ameliyat
n|vision|vizyon; görme
w|besides|ayrıca
d|basically|temelde
n|funding|fon, finansman
n|mode|mod
n|trading|ticaret
n|crisis|kriz
n|mayor|belediye başkanı
w|minor|küçük
n|selection|seçim
n|stream|dere; akış
n|struggle|mücadele
n|jail|hapishane
v|to jail|hapse atmak
n|voting|oylama
v|seek|aramak, peşinde olmak|sought · sought
w|capable|yetenekli
n|combination|kombinasyon
w|conservative|muhafazakâr
n|desire|arzu
n|medium|araç
a|relevant|ilgili, alakalı
n|draft|taslak
n|ID|kimlik
d|largely|büyük ölçüde
n|facility|tesis
n|maximum|azami
n|territory|bölge, toprak
v|reserve|rezervasyon yapmak
n|threat|tehdit
n|info|bilgi
n|a switch|şalter, düğme
a|reasonable|makul
w|aside|bir kenara
n|bond|bağ; tahvil
n|corporation|şirket
v|deserve|hak etmek
n|gender|cinsiyet
n|motion|hareket; önerge
n|resolution|karar; çözünürlük
w|rural|kırsal
n|universe|evren
n|delivery|teslimat
v|register|kaydolmak
a|armed|silahlı
n|assistance|yardım
n|a blow|darbe
n|saving|tasarruf
n|heaven|cennet
n|independence|bağımsızlık
n|load|yük
n|recovery|iyileşme; kurtarma
n|bunch|demet
n|lane|şerit
n|opposition|muhalefet
w|permanent|kalıcı
n|scheme|plan
n|tank|tank
w|weekly|haftalık
n|transportation|ulaşım
v|assume|varsaymak
a|accurate|doğru, isabetli
d|ultimately|nihayetinde
n|creation|yaratma
n|depression|depresyon
n|revolution|devrim
w|severe|şiddetli
n|tournament|turnuva
w|pregnant|hamile
v|excuse|affetmek, mazur görmek
n|counter|gişe
w|hopefully|umarım
n|manufacturing|imalat
n|perspective|bakış açısı
n|crash|kaza
n|depth|derinlik
n|existence|varlık
n|origin|köken
n|panel|panel
n|retail|perakende
n|shame|utanç
n|joy|sevinç
n|carbon|karbon
n|mate|arkadaş
a|nearby|yakındaki
d|somewhat|biraz, bir dereceye kadar
n|relief|rahatlama
w|constant|sabit
n|empire|imparatorluk
n|expansion|genişleme
a|absolute|mutlak
n|cable|kablo
n|championship|şampiyona
n|incident|olay
n|reporting|haber yapma
d|widely|geniş ölçüde
v|contest|itiraz etmek
d|closely|yakından
d|constantly|sürekli
n|motor|motor
n|protein|protein
a|raw|çiğ, ham
n|suffering|acı, ıstırap
a|unknown|bilinmeyen
n|anniversary|yıl dönümü
w|broad|geniş
w|hidden|gizli
n|retirement|emeklilik
w|solar|güneş
w|somehow|bir şekilde
w|ultimate|nihai
d|automatically|otomatik olarak
a|blind|kör
n|fantasy|fantezi
n|steam|buhar
v|conduct|yürütmek, icra etmek
v|witness|tanık olmak
w|brief|kısa
w|external|dış
v|grab|kapmak
n|therapy|terapi
n|defence|savunma
n|fee|ücret, harç
n|commander|komutan
a|detailed|ayrıntılı
a|opposed|karşı
n|defeat|yenilgi
n|democracy|demokrasi
n|suspect|şüpheli
v|swear|yemin etmek; küfretmek|swore · sworn
n|wealth|zenginlik
w|wise|bilge
w|monthly|aylık
a|equivalent|eşdeğer
a|outstanding|üstün, ödenmemiş
n|approval|onay
n|gang|çete
w|inner|iç
v|operate|işletmek
w|visual|görsel
v|get rid of|kurtulmak
n|bush|çalı
n|formation|oluşum
a|surrounding|çevredeki
a|universal|evrensel
a|contemporary|çağdaş
d|initially|başlangıçta
a|extensive|geniş kapsamlı
w|barely|zar zor
n|criticism|eleştiri
n|highway|otoyol
n|inch|inç
w|junior|kıdemsiz
n|jury|jüri
n|monster|canavar
n|philosophy|felsefe
n|pride|gurur
n|tone|ton
w|vast|engin
d|primarily|öncelikle
n|partnership|ortaklık
a|temporary|geçici
a|consistent|tutarlı
n|rescue|kurtarma
v|rush|acele etmek
w|stable|istikrarlı
n|circuit|devre
v|defend|savunmak
n|harm|zarar
n|household|hane
n|proposal|teklif
n|reputation|itibar
w|complicated|karmaşık
n|recognition|tanınma; takdir
n|extent|ölçü, derece
a|audio|ses, işitsel
n|format|biçim
n|healthcare|sağlık hizmetleri
n|immigration|göç (ülkeye)
n|membership|üyelik
v|mount|monte etmek; tırmanmak
d|shortly|kısa süre içinde
v|establish|kurmak, tesis etmek
n|transition|geçiş
w|elsewhere|başka yerde
n|founder|kurucu
w|loose|gevşek
w|offensive|saldırgan; kırıcı
w|ridiculous|gülünç
w|sensitive|hassas
n|shock|şok
n|silence|sessizlik
a|bound|kesin, mutlaka; bağlı
n|extension|uzatma; dahili hat
n|hip|kalça
n|infrastructure|altyapı
a|moral|ahlaki
n|a moral|ders, kıssadan hisse
a|pointed|sivri; iğneleyici
n|assessment|değerlendirme
n|acid|asit
n|anxiety|kaygı
n|penalty|ceza
n|temple|tapınak
a|curious|meraklı
w|alongside|yanında, ile birlikte
n|flash|flaş; parıltı
v|to flash|yanıp sönmek
n|rating|derecelendirme, puan
n|publication|yayın
v|select|seçmek
n|awareness|farkındalık
n|exposure|maruz kalma, görünürlük
v|chase|kovalamak
w|concrete|somut; beton
n|legend|efsane
n|shadow|gölge
n|wage|ücret
n|guarantee|garanti
d|deeply|derinden
n|rank|rütbe
n|tag|etiket
v|to tag|etiketlemek
n|procedure|prosedür, işlem
v|to rank|sıralamak
n|commitment|bağlılık; taahhüt
v|reveal|ortaya çıkarmak, açığa vurmak
n|avenue|bulvar
w|naked|çıplak
w|plain|sade
n|welfare|refah
n|wire|tel
n|pitch|saha; perde (ses)
n|output|çıktı
v|capture|yakalamak
w|efficient|verimli
w|newly|yeni
n|anger|kızgınlık, dert
w|afterwards|ondan sonra
a|comic|komik
n|a comic|çizgi roman
n|economics|ekonomi (bilim)
n|hunting|avcılık
n|kit|takım, set
a|racist|ırkçı
a|sexy|seksi
w|whoever|kim olursa
d|essentially|esasen
n|minority|azınlık
v|boost|artırmak, yükseltmek
n|aspect|yön, boyut
n|priority|öncelik
d|whereas|oysa ki, buna karşın
n|comfort|konfor
n|crack|çatlak
w|dramatic|dramatik
n|evolution|evrim
n|promotion|terfi
n|deck|güverte; deste
d|lately|son zamanlarda
n|rail|ray; korkuluk
n|institution|kurum
n|root|kök
n|decline|düşüş
v|obtain|elde etmek
v|recall|hatırlamak, geri çağırmak
w|decent|düzgün
n|downtown|şehir merkezi
w|insane|deli
w|organic|organik
w|spiritual|manevi
n|delay|gecikme
n|bid|teklif
v|to bid|teklif vermek
a|convinced|ikna olmuş
n|landing|iniş
n|ownership|sahiplik
a|subsequent|sonraki
n|citizen|vatandaş
w|intense|yoğun
n|lifetime|ömür
n|medal|madalya
n|mortgage|ipotek
n|reduction|azalma
w|visible|görünür
w|narrow|dar
d|occasionally|ara sıra
v|associate|ilişkilendirmek
v|to broadcast|yayınlamak
d|potentially|potansiyel olarak
n|a broadcast|yayın
d|increasingly|giderek
n|pace|hız, tempo
d|hence|dolayısıyla
n|angle|açı
w|rapid|hızlı
n|resident|sakin
w|vital|hayati
w|valid|geçerli
d|commonly|genellikle, yaygın olarak
n|forum|forum
a|shaped|şeklinde
n|regulation|düzenleme, mevzuat
n|honour|onur
v|monitor|izlemek, takip etmek
v|settle|yerleşmek, çözüme kavuşturmak
n|agriculture|tarım
n|fraud|dolandırıcılık
w|genuine|gerçek, samimi
n|hook|kanca
n|resort|tatil yeri
n|survival|hayatta kalma
v|regret|üzülmek, pişman olmak
n|programming|programlama
n|publishing|yayıncılık
n|organisation|kuruluş
a|objective|nesnel
v|engage|meşgul etmek, katılmak
v|regard|saymak, addetmek
n|initiative|girişim, inisiyatif
a|comprehensive|kapsamlı
w|automatic|otomatik
n|destruction|yıkım
n|divorce|boşanma
w|extraordinary|olağanüstü
n|headquarters|merkez
n|landscape|manzara
n|privacy|mahremiyet
n|gaming|oyun (video)
n|gene|gen
d|roughly|yaklaşık olarak
n|frequency|sıklık
n|outcome|sonuç
n|consumption|tüketim
w|gorgeous|muhteşem
w|ought to|-meli
v|stretch|esnemek
n|dozen|düzine
n|exit|çıkış
n|exception|istisna
n|tear|gözyaşı
n|breast|göğüs
v|rob|soymak
n|terrorist|terörist
n|input|girdi
n|sequence|dizi, sıra
v|contribute|katkıda bulunmak|contribute to sth
v|deny|inkâr etmek, reddetmek
n|fame|şöhret
w|genetic|genetik
w|instant|anında
w|progressive|ilerici
v|extend|uzatmak
n|principle|ilke
a|impressed|etkilenmiş
d|rapidly|hızla
n|sum|toplam; miktar
v|to sum up|özetlemek
n|contribution|katkı
a|fundamental|temel
n|conservation|koruma
n|genius|deha
w|mechanical|mekanik
w|precious|değerli
n|reward|ödül
n|shore|kıyı
n|trap|tuzak
n|wildlife|yaban hayatı
a|elementary|temel, ilk
a|ethnic|etnik
d|greatly|büyük ölçüde
n|infection|enfeksiyon
n|participation|katılım
n|satellite|uydu
a|sufficient|yeterli
n|complaint|şikâyet
n|component|bileşen
a|apparent|görünen, aşikâr
a|ongoing|süregelen
n|cure|tedavi
w|desperate|çaresiz
n|diversity|çeşitlilik
w|manual|el ile
n|preparation|hazırlık
n|romance|romantizm
n|tissue|doku; mendil
w|virtual|sanal
n|registration|adres kaydı, kayıt
n|courage|cesaret
a|aggressive|saldırgan
n|innovation|yenilik
n|nursing|hemşirelik
n|operator|operatör
n|feedback|geri bildirim
w|biological|biyolojik
n|disorder|bozukluk
w|literary|edebi
n|praise|övgü
n|psychology|psikoloji
n|ruin|harabe
n|slave|köle
w|steady|istikrarlı
v|dare|cesaret etmek
n|database|veritabanı
n|rocket|roket
n|terminal|terminal
a|dynamic|değişken, dinamik
v|enable|mümkün kılmak
n|cooperation|iş birliği
n|affair|mesele; ilişki
n|agenda|gündem
n|craft|zanaat
v|edit|düzenlemek
n|equity|öz sermaye; hakkaniyet
n|fortune|servet; şans
w|partly|kısmen
w|racial|ırksal
n|shield|kalkan
n|wisdom|bilgelik
n|bat|yarasa; sopa
n|darkness|karanlık
n|slide|kaydırak; slayt
v|to slide|kaymak
v|estimate|tahmin etmek
v|rely|güvenmek, dayanmak
n|framework|çerçeve
a|remarkable|kayda değer
n|alien|uzaylı; yabancı
w|awkward|tuhaf, beceriksiz
n|carrier|taşıyıcı
n|fool|aptal
w|overseas|denizaşırı
v|recover|iyileşmek
n|tale|masal
n|certificate|belge, yazı
a|disabled|engelli
v|drag|sürüklemek
n|jet|jet uçağı
n|lighting|aydınlatma
n|timing|zamanlama
n|ton|ton
a|distinct|belirgin, ayrı
n|interaction|etkileşim
a|crucial|çok önemli, kritik
w|dependent|bağımlı
n|globe|küre
v|slip|kaymak
n|specialist|uzman
a|satisfied|memnun
v|submit|teslim etmek
n|consideration|değerlendirme; düşünceli olma
""",
"B2.2": """
n|logo|logo
n|tap|musluk
v|to tap|hafifçe vurmak
v|overcome|üstesinden gelmek|overcame · overcome
w|acceptable|kabul edilebilir
n|auction|açık artırma
n|concentration|yoğunlaşma
w|frequent|sık
w|hilarious|çok komik
n|margin|kenar boşluğu; marj
n|passage|geçit; pasaj
n|stroke|felç; vuruş
w|stunning|çarpıcı
w|wherever|her nerede
a|challenging|zorlayıcı
n|opera|opera
n|a parallel|benzerlik, paralel
a|psychological|psikolojik
n|radiation|radyasyon
a|shocked|şok olmuş
n|tune|melodi
n|mechanism|mekanizma
a|parallel|koşut
v|encounter|karşılaşmak
n|controversy|tartışma, ihtilaf
w|bold|cesur
n|conspiracy|komplo
w|fiscal|mali
n|guardian|vasi
w|homeless|evsiz
n|panic|panik
n|terror|terör
n|examination|muayene
n|requirement|gereklilik, şart
v|pursue|peşinden gitmek, sürdürmek
n|clip|klip; mandal
d|nevertheless|buna rağmen
a|considerable|kayda değer
v|vary|değişkenlik göstermek
w|conventional|geleneksel
n|emperor|imparator
v|forgive|affetmek|forgave · forgiven
w|outer|dış
n|oxygen|oksijen
n|shelter|barınak
w|sooner|daha erken
n|venue|mekân
n|signature|imza
n|brick|tuğla
n|inspector|müfettiş
n|racism|ırkçılık
n|inquiry|araştırma, soruşturma
n|accuracy|doğruluk, isabet
a|diverse|çeşitli, farklı
w|artificial|yapay
n|bullet|mermi
n|tunnel|tünel
n|wound|yara
n|deposit|depozito
d|consistently|tutarlı şekilde
d|formerly|eskiden
a|isolated|izole, yalıtılmış
a|neutral|tarafsız
n|popularity|popülerlik
n|terrorism|terörizm
a|controversial|tartışmalı
w|casual|rahat
w|certified|onaylı
n|expense|masraf
n|invasion|istila
n|maker|yapımcı
w|strict|katı
w|unexpected|beklenmedik
n|usage|kullanım
a|graphic|grafik; açık (şiddet)
d|instantly|anında
n|palm|avuç içi; palmiye
n|rubber|lastik, kauçuk; silgi
n|asset|varlık; değerli şey
n|discipline|bilim dalı
a|dominant|baskın
d|furthermore|ayrıca
d|subsequently|ardından
v|generate|üretmek, oluşturmak
n|imagination|hayal gücü
n|lightning|şimşek
w|nasty|iğrenç
n|pension|emekli maaşı
n|permit|izin belgesi
w|slight|hafif
n|tension|gerilim
n|unity|birlik
w|useless|işe yaramaz
n|fever|ateş
v|delete|silmek
d|accidentally|kazara
a|affordable|uygun fiyatlı
n|canal|kanal
n|completion|tamamlama
n|cruise|gemi turu
n|motivation|motivasyon
n|outfit|kıyafet
d|briefly|kısaca
n|interpretation|yorum
w|bitter|acı
n|clinic|klinik
n|disability|engellilik
w|identical|aynı
w|wealthy|zengin
d|gradually|yavaş yavaş
n|evaluation|değerlendirme
v|demonstrate|göstermek, kanıtlamak
v|implement|hayata geçirmek, uygulamak
w|loyal|sadık
n|occupation|meslek; işgal
n|opponent|rakip
v|resist|direnmek
v|wrap|sarmak
n|patience|sabır
d|additionally|ayrıca
n|bug|böcek; hata
n|cave|mağara
n|punk|punk
d|precisely|tam olarak
v|preserve|korumak, muhafaza etmek
n|emphasis|vurgu
n|insight|içgörü
a|widespread|yaygın
w|distant|uzak
n|nightmare|kâbus
w|overnight|bir gecede
n|bacteria|bakteriler
w|beside|yanında
n|confusion|karışıklık
n|dealer|satıcı, bayi
n|electronics|elektronik
n|exploration|keşif
n|graphics|grafikler
n|nerve|sinir; cesaret
a|sustainable|sürdürülebilir
n|weakness|zayıflık
v|adopt|benimsemek
n|scenario|senaryo
v|trace|izini sürmek
n|perception|algı
v|proceed|devam etmek, ilerlemek
v|restore|eski hâline getirmek
n|significance|önem
v|cancel|iptal etmek
v|collapse|çökmek
w|conscious|bilinçli
n|rival|rakip
n|basement|bodrum
v|acknowledge|kabul etmek
n|bias|önyargı, taraflılık
n|animation|animasyon
a|balanced|dengeli
n|compound|bileşik; site
a|tropical|tropikal
n|decrease|azalma
n|lease|kira sözleşmesi
w|mysterious|gizemli
n|scandal|skandal
n|treasure|hazine
v|resolve|çözmek
a|artistic|sanatsal
n|genre|tür
n|lens|mercek; lens
n|rat|sıçan
n|notion|kavram, fikir
v|embrace|benimsemek, kucaklamak
v|exhibit|sergilemek, göstermek
v|retain|elde tutmak, korumak
n|liability|sorumluluk, yükümlülük
n|creature|yaratık
w|deadly|ölümcül
n|determination|kararlılık
w|infinite|sonsuz
w|realistic|gerçekçi
n|satisfaction|memnuniyet
n|shade|gölge
d|annually|yıllık olarak
n|icon|simge; ikon
n|installation|kurulum
n|marathon|maraton
n|parade|geçit töreni
n|scratch|çizik
v|to scratch|kaşımak, çizmek
d|sometime|bir ara
a|sporting|sportif
d|strictly|kesinlikle; sıkı şekilde
n|teens|ergenlik yılları
d|moreover|üstelik
v|eliminate|ortadan kaldırmak, elemek
n|barrier|engel
n|crop|ürün (tarım)
w|elderly|yaşlı
n|scholarship|burs
w|urgent|acil
w|vertical|dikey
n|wallet|cüzdan
v|inform|bildirmek, bilgilendirmek
v|tackle|(sorunu) ele almak
n|medication|ilaç
n|screening|tarama; gösterim
n|workshop|atölye
v|justify|gerekçelendirmek
n|addiction|bağımlılık
n|accent|aksan
w|awake|uyanık
n|curve|eğri
n|duration|süre
w|immune|bağışık
w|logical|mantıklı
n|peer|akran
v|install|kurmak
v|scream|bağırmak
a|depressed|depresif, bunalımlı
n|inflation|enflasyon
v|lean|yaslanmak, eğilmek
n|organ|organ; org
n|pile|yığın
v|to pile|yığmak
n|tragedy|trajedi
n|prospect|olasılık, ihtimal
a|demanding|zorlayıcı, çok şey isteyen
a|precise|kesin, hassas
v|acquire|edinmek
n|visa|vize
n|disc|disk
n|goodness|iyilik
n|theft|hırsızlık
n|arrow|ok
n|cabin|kabin; kulübe
n|consultant|danışman
a|flexible|esnek
v|owe|borçlu olmak
a|skilled|yetenekli, vasıflı
n|surgeon|cerrah
n|observation|gözlem
n|phenomenon|olgu
a|excessive|aşırı
v|heal|iyileşmek
n|deadline|süre, son tarih
n|colony|koloni
n|curriculum|müfredat
n|journalism|gazetecilik
n|pursuit|peşinde koşma
n|tribe|kabile
w|unfortunate|talihsiz
n|a dive|dalış
v|to dive|dalmak
n|overview|genel bakış
v|urge|ısrarla teşvik etmek
n|preference|tercih
n|proportion|oran
w|editorial|editoryal
w|nowadays|günümüzde
n|artwork|sanat eseri
n|defender|savunmacı
a|entertaining|eğlendirici
d|openly|açıkça
a|promising|umut verici
n|silk|ipek
v|convert|dönüştürmek
a|innovative|yenilikçi
n|hunger|açlık
n|cliff|uçurum
n|lung|akciğer
n|nutrition|beslenme
v|pose|oluşturmak (tehdit)
d|genuinely|gerçekten
a|matching|uyumlu
d|purely|tamamen, sadece
d|severely|ciddi şekilde
a|shocking|şok edici
w|anxious|endişeli
n|forecast|tahmin
w|passionate|tutkulu
n|skull|kafatası
n|bombing|bombalama
n|dairy|süt ürünleri
a|delighted|çok memnun
n|receiver|ahize; alıcı
d|thoroughly|baştan sona
a|inevitable|kaçınılmaz
v|approve|onaylamak
a|beneficial|faydalı
n|fabric|kumaş
w|fabulous|harika
n|myth|efsane
n|variation|değişkenlik
v|dump|atmak, boşaltmak
d|permanently|kalıcı olarak
a|tragic|trajik
v|assess|değerlendirmek
n|assumption|varsayım
v|adjust|ayarlamak, uyarlamak
n|obligation|yükümlülük
w|altogether|tamamen
n|blanket|battaniye
n|flame|alev
w|miserable|perişan
v|scare|korkutmak
n|basket|sepet
a|charming|çekici, sevimli
a|ethical|etik
d|freely|özgürce
n|ink|mürekkep
n|ambulance|ambulans
n|password|şifre
v|observe|gözlemlemek
v|assure|temin etmek, güvence vermek
n|expertise|uzmanlık
w|ashamed|utanmış
n|indication|belirti
w|martial|askerî
w|spectacular|muhteşem
w|technological|teknolojik
n|a cheer|tezahürat
v|to cheer|tezahürat yapmak
n|demonstration|gösteri; gösterim
n|grocery|bakkal; market alışverişi
d|temporarily|geçici olarak
v|accomplish|başarmak, tamamlamak
v|alter|değiştirmek
v|withdraw|geri çekmek, çekilmek
a|adequate|yeterli
n|apology|özür
v|interact|etkileşmek
n|rhythm|ritim
n|stance|duruş
v|beg|yalvarmak; dilenmek
v|declare|ilan etmek; beyan etmek
n|dot|nokta
n|measurement|ölçüm
a|sophisticated|gelişmiş; sofistike
n|warming|ısınma
v|detect|saptamak, tespit etmek
n|thesis|tez, sav
v|comply with|uymak
v|cope|başa çıkmak
v|enhance|geliştirmek, iyileştirmek
v|strengthen|güçlendirmek
v|transform|dönüştürmek
w|magnificent|görkemli
n|placement|yerleştirme; staj
w|shallow|sığ
n|spite|kin
n|sponsor|sponsor
d|emotionally|duygusal olarak
n|workplace|iş yeri
v|reject|reddetmek
n|pill|hap
v|insist|ısrar etmek
n|uncertainty|belirsizlik
v|differ|farklı olmak
v|elect|seçmek
n|ladder|merdiven
n|mineral|mineral
w|modest|alçakgönüllü
n|navigation|navigasyon
d|reasonably|oldukça; makul şekilde
n|analyst|analist
v|abandon|terk etmek, vazgeçmek
d|deliberately|kasten
n|badge|rozet
n|convenience|kolaylık
n|enthusiasm|coşku
n|helmet|kask
v|possess|sahip olmak
n|probability|olasılık
a|confusing|kafa karıştırıcı
n|an extract|alıntı; öz
v|accommodate|barındırmak, uyum sağlatmak
v|evaluate|değerlendirmek, not vermek
n|disappointment|hayal kırıklığı
v|insert|yerleştirmek
n|orchestra|orkestra
n|sympathy|sempati; başsağlığı
n|thumb|başparmak
n|vitamin|vitamin
w|voluntary|gönüllü
n|wheat|buğday
n|wrist|bilek
n|civilization|medeniyet
n|creativity|yaratıcılık
n|disk|disk
v|pause|ara vermek
v|inspire|ilham vermek
n|clerk|memur, katip
n|donation|bağış
n|lottery|piyango
n|publicity|tanıtım
n|survivor|hayatta kalan
d|considerably|önemli ölçüde
d|firmly|sıkıca, kesin olarak
n|recruitment|işe alım
v|negotiate|müzakere etmek
n|expectation|beklenti
a|evident|besbelli
w|bent|eğri
n|entrepreneur|girişimci
n|fossil|fosil
n|honesty|dürüstlük
w|neat|düzenli
n|speculation|spekülasyon
w|steep|dik
d|accurately|doğru şekilde
v|propose|önermek
n|harbour|liman
v|construct|tasarlayıp inşa etmek
w|furious|öfkeli
v|adapt|uyum sağlamak
v|expose|maruz bırakmak, ifşa etmek
n|habitat|yaşam alanı
v|manufacture|üretmek
n|pity|acıma
n|refugee|mülteci
v|satisfy|tatmin etmek
d|desperately|çaresizce
n|gig|konser; iş
n|licence|ruhsat
n|incentive|teşvik
a|convincing|inandırıcı
n|characteristic|özellik
n|delight|zevk
w|fortunate|şanslı
w|harmful|zararlı
w|memorable|unutulmaz
v|sweep|süpürmek|swept · swept
a|thorough|titiz, kapsamlı
v|resign|istifa etmek
n|robbery|soygun
v|rub|ovmak
n|therapist|terapist
n|tendency|eğilim
n|cheek|yanak
n|fraction|kesir; küçük bir kısım
v|melt|erimek
n|puzzle|bulmaca
n|scholar|akademisyen
n|coincidence|tesadüf
n|investor|yatırımcı
n|offence|suç; hakaret
n|bargain|kelepir
n|critic|eleştirmen
w|elegant|zarif
w|hollow|içi boş
n|ballet|bale
d|dramatically|çarpıcı şekilde
a|relieved|rahatlamış
d|consequently|sonuç olarak
v|threaten|tehdit etmek
w|dull|sıkıcı; donuk
n|fare|ücret (bilet)
v|float|yüzmek (su üstü)
n|illusion|yanılsama
w|incorrect|yanlış
v|oppose|karşı çıkmak
n|spice|baharat
w|unconscious|bilinçsiz, baygın
a|risky|riskli
n|workforce|iş gücü
v|arise|ortaya çıkmak, oluşmak|arose · arisen
v|impress|etkilemek
v|occupy|işgal etmek
n|norm|norm
v|exceed|aşmak, geçmek
v|outline|ana hatlarıyla belirtmek
v|impose|dayatmak
n|illustration|görsel örnek
n|collector|koleksiyoncu
w|exotic|egzotik
n|necessity|gereklilik
n|observer|gözlemci
n|shortage|kıtlık
v|stare|dik dik bakmak
a|enjoyable|keyifli
d|terribly|çok; korkunç şekilde
n|monument|anıt
d|inevitably|kaçınılmaz olarak
n|drought|kuraklık
n|gesture|jest
n|historian|tarihçi
n|slope|yamaç
w|stiff|sert
v|unite|birleştirmek
n|balloon|balon
v|rebuild|yeniden inşa etmek
n|mosque|cami
v|recruit|işe almak
a|fond|düşkün
v|emerge|ortaya çıkmak
n|attachment|ek; bağlılık
n|candle|mum
n|choir|koro
n|corridor|koridor
d|critically|eleştirel olarak; ciddi şekilde
v|calculate|hesaplamak
v|distinguish|ayırt etmek
v|consult|danışmak
v|dominate|hâkim olmak
v|swallow|yutmak
w|unacceptable|kabul edilemez
n|economist|ekonomist
d|extensively|kapsamlı şekilde
n|marker|işaretleyici kalem
a|optimistic|iyimser
n|hypothesis|hipotez
v|regulate|düzenlemek
n|booking|rezervasyon
v|prompt|tetiklemek, yol açmak
n|envelope|zarf
w|lively|canlı
n|referee|hakem
n|judgement|yargı; karar
v|clarify|netleştirmek
v|dismiss|reddetmek, işten çıkarmak
v|incorporate|dahil etmek, bünyesine katmak
n|recession|durgunluk
n|composer|besteci
n|elbow|dirsek
n|heel|topuk
w|sincere|içten
v|spill|dökmek
a|enthusiastic|hevesli
d|steadily|istikrarlı şekilde
v|obey|itaat etmek
v|imply|ima etmek
v|convey|iletmek, aktarmak
v|exploit|sömürmek, istismar etmek
a|curved|kavisli
a|depressing|iç karartıcı
n|humour|mizah
a|deliberate|kasıtlı
v|confess|itiraf etmek
n|revision|revizyon
n|certainty|kesinlik
n|decoration|süsleme
d|broadly|genel hatlarıyla
v|accompany|eşlik etmek
n|pupil|öğrenci (okul)
v|interpret|yorumlamak
v|undergo|geçirmek, maruz kalmak
v|absorb|emmek
v|spoil|bozmak; şımartmak
n|suburb|banliyö
w|sympathetic|anlayışlı
n|obesity|obezite
v|evolve|evrilmek, gelişmek
v|restrict|kısıtlamak
w|sticky|yapışkan
n|psychologist|psikolog
d|sufficiently|yeterince
n|mechanic|tamirci
v|distribute|dağıtmak
v|hesitate|tereddüt etmek
v|modify|değiştirmek, uyarlamak
w|probable|olası
n|spokesman|sözcü
v|surround|çevrelemek
d|efficiently|verimli şekilde
n|stall|tezgâh
w|trillion|trilyon
v|exclude|dışlamak, hariç tutmak
v|specify|belirtmek, açıkça saptamak
n|greenhouse|sera
n|negotiation|müzakere
n|participant|katılımcı
n|sustainability|sürdürülebilirlik
n|seminar|seminer
v|relieve|rahatlatmak, hafifletmek
w|comparative|karşılaştırmalı
n|herb|ot
n|textbook|ders kitabı
v|chop|doğramak
d|fundamentally|temelden
d|remarkably|dikkat çekici şekilde
n|interval|aralık
n|packet|paket
n|worm|solucan
n|restriction|kısıtlama
v|reckon|sanmak, hesap etmek
n|accountant|muhasebeci
v|activate|etkinleştirmek
a|amusing|eğlenceli
a|predictable|tahmin edilebilir
n|cue|işaret, ipucu
d|upwards|yukarı doğru
n|notebook|defter
v|whisper|fısıldamak
d|appropriately|uygun şekilde
v|anticipate|önceden tahmin etmek, beklemek
v|undertake|üstlenmek|undertook · undertaken
n|flavour|tat
n|metaphor|mecaz
v|perceive|algılamak
v|integrate|entegre etmek, bütünleştirmek
n|obstacle|engel
n|slogan|slogan
n|sponsorship|sponsorluk
v|illustrate|örneklemek
v|accuse|suçlamak
v|distract|dikkatini dağıtmak
n|litter|çöp (yerlere atılan)
n|limitation|sınırlılık
a|compulsory|zorunlu
n|emission|emisyon, salım
a|folding|katlanır
n|offender|suçlu
v|underestimate|hafife almak
n|trait|özellik, karakter özelliği
v|emphasize|vurgulamak
n|feather|tüy
n|troop|asker birliği
v|reinforce|pekiştirmek, güçlendirmek
v|suspend|askıya almak
v|depart|hareket etmek, ayrılmak (yolculuğa çıkmak)
v|govern|yönetmek, belirlemek
a|astonishing|hayret verici
v|disappoint|hayal kırıklığına uğratmak
v|stimulate|teşvik etmek
v|wander|dolaşmak
v|cite|alıntılamak, kaynak göstermek
v|transmit|iletmek
v|forbid|yasaklamak|forbade · forbidden
v|assign|atamak, görevlendirmek
v|remark|belirtmek, yorum yapmak
n|circumstance|koşul, durum
n|disagreement|anlaşmazlık
d|adequately|yeterli şekilde
n|applicant|başvuran
n|spokesperson|sözcü
n|viewpoint|bakış açısı
n|broadcaster|yayıncı
v|criticize|eleştirmek
n|lyric|şarkı sözü
v|comprise|kapsamak, oluşmak
v|interrupt|kesmek, bölmek
v|invade|istila etmek
n|novelist|romancı
n|sibling|kardeş
a|humorous|esprili
v|motivate|motive etmek
v|isolate|yalıtmak, ayrıştırmak
n|miner|madenci
v|discourage|caydırmak, cesaretini kırmak
v|offend|kırmak, gücendirmek
v|disturb|rahatsız etmek
n|implication|çıkarım, doğuracağı sonuç
w|colourful|rengarenk
v|fulfil|yerine getirmek, karşılamak
n|fragment|parça
a|impatient|sabırsız
n|ethic|etik, ahlak
v|devote|adamak
a|dishonest|dürüst olmayan
v|inherit|miras almak
v|starve|açlıktan ölmek
n|tsunami|tsunami
v|derive|türetmek, elde etmek
v|prohibit|yasaklamak
n|spectator|seyirci
n|litre|litre
v|multiply|çarpmak
v|equip|donatmak
n|ancestor|ata
v|speculate|spekülasyon yapmak
n|criterion|ölçüt
v|compose|bestelemek; oluşturmak
n|globalization|küreselleşme
v|unfold|açılmak; gelişmek
n|questionnaire|anket formu
n|enquiry|soruşturma; bilgi talebi
n|seeker|arayan
v|classify|sınıflandırmak
n|firefighter|itfaiyeci
v|contradict|çelişmek; itiraz etmek
a|foreseeable|öngörülebilir
n|cohesion|dayanışma
v|specialize|uzmanlaşmak
n|guideline|yönerge
n|tonne|ton
d|downwards|aşağı doğru
v|infer|çıkarsamak
n|settler|yerleşimci
n|leaflet|broşür
n|spokeswoman|kadın sözcü
n|protester|protestocu
v|emphasise|vurgulamak
v|erupt|patlamak (yanardağ)
n|firework|havai fişek
v|precede|önce gelmek
v|overestimate|fazla değer vermek
v|terrify|dehşete düşürmek
n|inhabitant|sakin, oturan
v|summarise|özetlemek
""",
"C1.1": """
w|well|iyi; peki
a|long-time|uzun süreli
n|well-being|refah, iyi oluş
v|to top|aşmak; zirvede olmak
p|put up with|katlanmak
n|set-up|düzen, kurulum
p|make sure|emin olmak
d|at times|zaman zaman
p|live up to|(beklentiyi) karşılamak
n|line-up|kadro
d|by and large|genel olarak
p|come to a head|doruğa çıkmak, kızışmak
p|turn out|ortaya çıkmak|it turned out that…
p|go along with|kabul etmek, uymak
p|bring about|yol açmak|brought about
w|fine|iyi; ince
w|total|toplam
d|in view of|karşısında
d|as a result|sonuç olarak
w|whatever|her ne
a|post-war|savaş sonrası
p|come across|rastlamak|came across
p|take into account|hesaba katmak
p|as a matter of fact|aslına bakılırsa
p|step down|görevden çekilmek
p|pass on|aktarmak, devretmek
p|pick up on|fark etmek, yakalamak
p|in respect of|-e ilişkin
p|let alone|bırakın -i, şöyle dursun
v|to rock|sallamak
p|build on|üzerine inşa etmek
p|provided that|şu şartla ki
p|all things considered|her şey göz önüne alındığında
p|drop out|bırakmak, ayrılmak
p|to put it simply|basitçe söylemek gerekirse
p|subject to|-e tabi olarak
n|decision-making|karar verme
p|rule out|ihtimal dışı bırakmak
p|it goes without saying|söylemeye gerek yok ki
p|fall behind|geri kalmak
v|to pop|patlamak; uğramak
a|standing|kalıcı, sürekli
a|long-standing|köklü, uzun süredir var olan
p|draw on|-den yararlanmak
n|remains|kalıntılar
a|high-profile|çok konuşulan, önemli
p|stick to|bağlı kalmak
p|in the wake of|-in ardından
n|bay|koy
a|large-scale|büyük ölçekli
n|vice|kötü alışkanlık
n|attorney|avukat
w|supreme|yüce
n|ray|ışın
n|squad|ekip, takım
n|abuse|istismar
w|liberal|liberal
p|as far as I'm concerned|bana kalırsa
n|ministry|bakanlık
n|passing|geçiş; vefat
p|phase out|kademeli olarak kaldırmak
n|kingdom|krallık
n|suicide|intihar
p|lay off|işten çıkarmak
n|assembly|meclis; montaj
a|solo|solo
n|republic|cumhuriyet
a|non-profit|kâr amacı gütmeyen
n|offering|sunulan ürün; adak
p|take for granted|hazır kabul etmek
a|dedicated|kendini adamış; özel amaçlı
n|senator|senatör
n|storage|depolama
n|academy|akademi
n|combat|çarpışma
n|constitution|anayasa
w|exclusive|özel
n|grace|zarafet
w|latter|ikincisi
n|personnel|personel
n|crown|taç
n|mining|madencilik
a|premier|önde gelen, birinci
n|deputy|yardımcı
n|legislation|mevzuat
n|maintenance|bakım
a|interior|iç
n|the interior|iç kısım
n|resistance|direniş; direnç
w|dumb|aptal
n|peak|zirve
n|reform|reform
a|marine|deniz
p|put into perspective|doğru bakış açısına oturtmak
w|principal|başlıca
n|debut|ilk çıkış
v|to license|lisans vermek
a|presidential|başkanlık
n|shipping|nakliye, kargo
w|clinical|klinik
n|cabinet|kabine; dolap
n|settlement|yerleşim; uzlaşma
w|regardless|ne olursa olsun
n|auto|otomobil
p|regardless of|-e bakılmaksızın
n|chamber|oda
n|province|il
n|gear|vites; donanım
w|superior|üstün
n|the accused|sanık
n|processing|işleme
w|administrative|idari
n|trail|iz, patika
n|angel|melek
n|bonus|ikramiye, bonus
n|enforcement|uygulama, yürütme
a|gross|brüt; iğrenç
n|formula|formül
d|respectively|sırasıyla
n|assault|saldırı
n|replacement|yedek, yerine geçen
n|thread|iplik; konu dizisi
w|rear|arka
w|strategic|stratejik
n|commissioner|komiser
p|on the grounds that|-gerekçesiyle
n|behalf|adına
n|establishment|kuruluş
n|inspiration|ilham
n|memorial|anıt
n|saint|aziz
n|alliance|ittifak
n|crystal|kristal
n|buddy|kanka, dost
n|elite|seçkinler
d|forth|ileri
n|sake|hatır
p|for the sake of|-in hatırına, uğruna
n|bench|bank (oturak)
n|handling|ele alma, kullanım
n|idiot|aptal
p|to a certain extent|bir dereceye kadar
n|efficiency|verimlilik
n|amendment|değişiklik (yasa)
n|enterprise|girişim
w|whilst|-iken
n|bishop|piskopos
a|defensive|savunmacı
n|mill|değirmen; fabrika
n|spin|dönüş
v|to spin|dönmek, döndürmek
p|narrow down|daraltmak, elemek
n|ratio|oran
v|reverse|tersine çevirmek
n|commerce|ticaret
n|funeral|cenaze
n|cop|polis (argo)
n|legacy|miras
n|log|kütük; kayıt
v|to log|kaydetmek
n|sin|günah
n|sword|kılıç
n|ward|koğuş
d|merely|sadece
v|resort to|(çare olarak) başvurmak
n|consent|rıza
n|fate|kader
n|glory|şan
n|heritage|miras
n|logic|mantık
n|residence|ikamet
n|strip|şerit
v|to strip|soymak, çıkarmak
p|with regard to|-e ilişkin
n|ambassador|büyükelçi
n|poll|anket
n|removal|kaldırma
n|corruption|yolsuzluk
n|absence|yokluk
n|liberty|özgürlük
n|representation|temsil
v|swing|sallanmak|swung · swung
a|agricultural|tarımsal
n|ease|kolaylık, rahatlık
v|to ease|hafifletmek
n|rally|miting; ralli
v|to rally|toparlanmak; bir araya gelmek
a|upcoming|yaklaşan
p|sum up|özetlemek
v|foster|teşvik etmek, beslemek
a|prominent|öne çıkan
a|substantial|hatırı sayılır, esaslı
n|compensation|tazminat
n|fleet|filo
n|guidance|rehberlik
w|premium|üstün kalite
w|radical|radikal
w|residential|konut
n|transmission|iletim; şanzıman
a|alert|tetikte
v|to alert|uyarmak
n|arena|arena
n|boom|patlama; ani artış
a|constitutional|anayasal
n|density|yoğunluk
n|pregnancy|hamilelik
n|an alert|uyarı, alarm
n|composition|bileşim, kompozisyon
n|blast|patlama
n|faculty|fakülte
n|humanity|insanlık
n|punch|yumruk
a|communist|komünist
a|legislative|yasama
n|listing|liste, ilan
n|trailer|fragman; römork
w|versus|karşı
n|implementation|uygulama, hayata geçirme
n|footage|görüntü kaydı
n|grave|mezar
n|mask|maske
n|stability|istikrar
n|treaty|antlaşma
n|discrimination|ayrımcılık
n|domain|alan, saha
n|engagement|nişan; katılım
p|stem from|-den kaynaklanmak
w|intellectual|entelektüel
n|involvement|katılım
n|regime|rejim
n|seal|mühür; fok
n|summit|zirve
n|a bow|yay; reverans
v|to bow|eğilmek, selam vermek
n|devil|şeytan
n|hardware|donanım
n|petition|dilekçe
n|stem|sap
a|collective|toplu, ortak
a|eligible|hak sahibi, uygun
n|beast|canavar
n|default|varsayılan
n|execution|idam; uygulama
n|loop|döngü
n|sacrifice|fedakârlık
w|sole|tek
n|worship|ibadet
w|worthy|layık
n|franchise|bayilik; seri
a|integrated|entegre
n|ruling|karar
n|intent|niyet
w|dual|çift
n|filter|filtre
w|mature|olgun
v|pump|pompalamak
n|revenge|intikam
w|spare|yedek
n|bass|bas
n|collaboration|iş birliği
a|experimental|deneysel
n|odds|olasılık; bahis oranı
n|prevention|önleme
n|dispute|anlaşmazlık
n|chaos|kaos
n|dawn|şafak
n|earnings|kazanç
w|moderate|ılımlı
n|quest|arayış
n|utility|fayda; hizmet
n|vessel|gemi; damar
n|copper|bakır
n|pit|çukur
n|weed|yabani ot
n|intervention|müdahale
a|mutual|karşılıklı
n|equality|eşitlik
w|mainstream|ana akım
w|oral|sözlü
n|segment|bölüm
n|spectrum|yelpaze
n|venture|girişim
n|acquisition|edinme; satın alma
v|rip|yırtmak
n|scope|kapsam
n|mercy|merhamet
n|tribute|övgü
n|trigger|tetik
n|gathering|toplantı, buluşma
n|screw|vida
v|to screw|vidalamak
w|beneath|altında
n|conversion|dönüşüm
w|divine|ilahi
w|functional|işlevsel
w|municipal|belediye
w|noble|asil
w|sacred|kutsal
n|suspension|askıya alma
w|toxic|zehirli
n|upgrade|yükseltme
n|abortion|kürtaj
n|copyright|telif hakkı
d|exclusively|yalnızca
a|naval|deniz kuvvetleri
n|spy|casus
v|to spy|casusluk yapmak
n|warrant|arama/tutuklama emri
n|burden|yük, külfet
w|civilian|sivil
n|coalition|koalisyon
n|backing|destek
n|charter|tüzük; kiralama
a|legendary|efsanevi
n|pole|direk; kutup
a|regulatory|düzenleyici
a|serial|seri
v|shed|dökmek; atmak
n|syndrome|sendrom
p|at the expense of|-in pahasına
a|legitimate|meşru
n|amateur|amatör
w|productive|verimli
n|twist|bükülme
n|integrity|dürüstlük
n|custody|velayet; gözaltı
n|fluid|sıvı
n|integration|entegrasyon, uyum
a|magical|büyülü
a|socialist|sosyalist
v|sue|dava açmak
v|advocate|savunmak, desteklemek
a|vulnerable|savunmasız, kırılgan
n|excess|fazlalık
n|gravity|yerçekimi
n|nonsense|saçmalık
n|slavery|kölelik
n|transaction|işlem
n|veteran|gazi
n|backup|yedek
n|creator|yaratıcı
a|operational|işler durumda; operasyonel
v|skip|atlamak
v|snap|kırılmak; çatlamak
n|transformation|dönüşüm
p|shed light on|aydınlatmak
n|dose|doz
a|chronic|kronik
n|diagnosis|teşhis
n|flesh|et (vücut)
n|laser|lazer
n|radar|radar
a|striking|çarpıcı
n|transit|transit; toplu taşıma
n|patch|yama; parça (alan)
n|privilege|ayrıcalık
d|solely|yalnızca
n|blade|bıçak ağzı
n|cargo|kargo
n|bulk|büyük kısım; toptan
a|coastal|kıyı
n|commentary|yorum, anlatım
a|congressional|kongre ile ilgili
n|raid|baskın
n|ranking|sıralama
a|situated|konumlanmış
n|tobacco|tütün
n|a trace|iz
d|partially|kısmen
a|respective|ilgili, sırasıyla
a|accessible|erişilebilir
w|bare|çıplak
w|consecutive|ardışık
w|endless|sonsuz
n|patent|patent
n|classification|sınıflandırma
n|film-maker|film yapımcısı
n|grid|ızgara; şebeke
n|identification|kimlik tespiti
n|lap|kucak; tur
n|liver|karaciğer
a|parliamentary|parlamenter
n|physician|hekim
n|rifle|tüfek
a|structural|yapısal
n|suite|süit
n|verse|dize; kıta
v|substitute|yerine koymak
w|anonymous|anonim
w|beloved|sevgili
w|contrary|aksi
n|loyalty|sadakat
n|propaganda|propaganda
n|testimony|tanıklık
n|adoption|evlat edinme; benimseme
n|attendance|katılım, devam
n|barrel|varil; namlu
v|bless|kutsamak
a|colonial|sömürge
v|crush|ezmek
n|dam|baraj
a|magnetic|manyetik
n|reflection|yansıma; düşünme
a|revolutionary|devrimci
d|simultaneously|aynı anda
n|surveillance|gözetim
n|trophy|kupa
n|compliance|uyum, mevzuata uygunluk
a|partial|kısmi
a|underlying|altta yatan
p|contrary to|-in aksine
v|yield|vermek (sonuç), boyun eğmek
a|preliminary|ön, hazırlık niteliğinde
n|acceptance|kabul
w|vocal|sesli; açık sözlü
n|ash|kül
n|casino|kumarhane
a|indigenous|yerli
n|legislature|yasama organı
n|presidency|başkanlık
n|warrior|savaşçı
n|stake|pay, risk edilen şey
n|strain|gerilim, zorlanma
n|admission|kabul; giriş
n|torture|işkence
v|burst|patlamak
n|cattle|sığır
a|lesbian|lezbiyen
n|portfolio|portföy
n|productivity|verimlilik
n|violation|ihlal
n|protocol|protokol
n|compromise|uzlaşma
n|plug|fiş
n|conviction|inanç, mahkûmiyet
w|corrupt|yozlaşmış
w|harsh|sert
w|judicial|adli
n|provision|hüküm; tedarik
n|trauma|travma
n|beam|kiriş; ışın
a|encouraging|cesaret verici
n|horn|boynuz; korna
n|inspection|denetim
n|intensity|yoğunluk
a|meaningful|anlamlı
n|migration|göç
n|missile|füze
n|patrol|devriye
n|rod|çubuk
a|statistical|istatistiksel
n|courtesy|nezaket
n|embassy|büyükelçilik
n|guilt|suçluluk
n|haven|sığınak
w|lesser|daha az
w|mere|sadece, basit
n|miracle|mucize
w|protective|koruyucu
n|publisher|yayıncı
n|retreat|geri çekilme
n|valve|vana
a|mandatory|zorunlu
n|boundary|sınır
n|breach|ihlal
n|companion|arkadaş
n|consciousness|bilinç
n|in accordance with|-e uygun olarak
n|activist|aktivist
a|alike|benzer
a|corresponding|karşılık gelen
a|engaging|ilgi çekici
d|reportedly|bildirildiğine göre
n|separation|ayrılık
a|applicable|uygulanabilir
n|availability|mevcudiyet, müsaitlik
p|be reflected in|-e yansımak
w|adjacent|bitişik
n|appreciation|takdir
w|athletic|atletik
n|banner|afiş
n|charm|çekicilik
w|electoral|seçimle ilgili
n|entity|varlık, kuruluş
n|interface|arayüz
w|occasional|ara sıra olan
n|ridge|sırt
a|feminist|feminist
n|reminder|hatırlatma
v|resume|devam etmek
a|variable (adj.)|değişken
a|linear|doğrusal
n|variable|değişken
a|lasting|kalıcı
w|alternate|dönüşümlü
n|bankruptcy|iflas
n|closure|kapanış
w|cognitive|bilişsel
w|dental|diş
w|diplomatic|diplomatik
w|eternal|ebedi
n|grip|kavrama
n|handful|avuç dolusu
n|harmony|uyum
w|humble|alçakgönüllü
w|hybrid|melez
w|minimal|asgari
w|molecular|moleküler
w|pathetic|acınası
n|restoration|restorasyon
w|selfish|bencil
n|throne|taht
n|noon|öğle
n|rage|öfke
n|parish|cemaat bölgesi
a|generic|genel, jenerik
n|archives|arşiv
w|brutal|vahşi
n|declaration|beyan
n|distinction|ayrım
w|faithful|sadık
w|fatal|ölümcül
w|fitting|uygun
n|jurisdiction|yargı yetkisi
w|mighty|kudretli
w|monetary|parasal
w|poorly|kötü
n|breakdown|arıza
n|citizenship|vatandaşlık
n|consensus|uzlaşı
n|ally|müttefik
n|rental|kiralama
d|seemingly|görünüşe göre
n|array|dizi, çeşitlilik
a|influential|etkili, nüfuzlu
n|cult|tarikat
w|invisible|görünmez
n|lawsuit|dava
n|leak|sızıntı
n|riot|isyan
v|smash|parçalamak
n|surrender|teslimiyet
w|suspicious|şüpheli
w|tender|şefkatli
n|vacuum|boşluk
n|slot|yuva; zaman aralığı
n|governance|yönetişim
a|overwhelming|ezici, bunaltıcı
n|breed|ırk, cins
n|confirmation|onay
n|contractor|yüklenici
n|diameter|çap
w|glorious|şanlı
n|merchant|tüccar
n|merit|değer, liyakat
n|rebel|asi
n|rotation|dönüş
n|toll|geçiş ücreti; bedel
w|torn|yırtık
w|unbelievable|inanılmaz
w|underneath|altında
w|viral|viral
n|warehouse|depo
n|widow|dul kadın
n|grief|keder
a|subtle|ince
n|duo|ikili
a|frustrated|hayal kırıklığına uğramış
n|gambling|kumar
n|layout|düzen, yerleşim
n|pastor|papaz
a|provincial|taşra; il
a|comparable|karşılaştırılabilir
n|momentum|ivme
n|outlook|görünüm, bakış açısı
a|notable|dikkate değer
n|beard|sakal
n|capability|yetenek
n|curse|lanet
n|drain|gider
n|excellence|mükemmellik
n|hint|ipucu
n|horizon|ufuk
w|hostile|düşmanca
n|nest|yuva
n|nomination|aday gösterme
n|reign|saltanat
n|span|süre, aralık
n|submission|teslim
w|tremendous|muazzam
n|administrator|yönetici
a|nationwide|ülke çapında
a|optical|optik
a|specialized|uzmanlaşmış
v|elaborate|ayrıntılandırmak
n|ballot|oy pusulası
n|cemetery|mezarlık
n|compact|anlaşma
n|deficit|açık
w|halfway|yarı yolda
w|intensive|yoğun
w|intimate|samimi
n|prosecution|kovuşturma
n|pulse|nabız
w|rational|akılcı
n|realm|alan, diyar
n|streak|seri
n|subscription|abonelik
n|tolerance|hoşgörü
d|presumably|muhtemelen
d|allegedly|iddiaya göre
n|blessing|nimet; kutsama
n|demon|iblis
a|interactive|etkileşimli
a|pronounced|belirgin
n|detection|tespit, saptama
w|exceptional|olağanüstü
v|hack|kesmek; hacklemek
n|hatred|nefret
n|majesty|majeste
w|savage|vahşi
w|slim|ince
w|someday|bir gün
n|stack|yığın
w|supportive|destekleyici
w|surgical|cerrahi
n|tide|gelgit
n|warfare|savaş
v|dip|batırmak
a|disturbing|rahatsız edici
n|effectiveness|etkililik
d|frankly|açıkçası
a|medieval|ortaçağ
n|mobility|hareketlilik
n|orientation|yönelim; oryantasyon
n|proceeds|gelir, hasılat
n|spam|istenmeyen e-posta
n|withdrawal|geri çekilme; para çekme
d|nonetheless|buna rağmen
v|comply|uymak, riayet etmek
w|authentic|otantik
n|bolt|cıvata
n|collar|yaka
n|finale|final
n|ignorance|cehalet
w|intermediate|orta düzey
w|mathematical|matematiksel
n|recreation|eğlence
n|sketch|taslak
n|sunset|gün batımı
w|thermal|termal
n|echo|yankı
v|to echo|yankılanmak
n|in the meantime|bu arada
n|pipeline|boru hattı
n|audit|denetim
v|cease|son vermek, kesilmek
v|supplement|takviye etmek, eklemek
n|remainder|geri kalan
n|threshold|eşik
a|thereby|böylece
n|chapel|şapel
n|essence|öz
n|harvest|hasat
n|junk|hurda
n|kidney|böbrek
n|lobby|lobi
n|orbit|yörünge
w|passive|pasif
n|peninsula|yarımada
w|profitable|kârlı
n|sentiment|duygu
n|trunk|gövde; bagaj
w|varied|çeşitli
n|verdict|karar
w|eager|merakla bekleyen
n|mob|kalabalık; mafya
a|tribal|kabile
n|anchor|çapa
n|arch|kemer
w|bizarre|tuhaf
v|bounce|zıplamak
n|consultation|danışma
w|continental|kıtasal
n|dignity|onur
n|ferry|feribot
n|fusion|füzyon
n|inclusion|dahil etme
n|keeper|koruyucu; kaleci
n|liar|yalancı
n|machinery|makineler
n|mansion|konak
n|ritual|ritüel
v|slam|çarpmak
v|subscribe|abone olmak
n|voltage|voltaj
n|width|genişlik
n|workout|antrenman
a|aesthetic|estetik
n|complexity|karmaşıklık
n|ego|ego
n|flexibility|esneklik
n|gut|bağırsak; içgüdü
n|resignation|istifa
d|utterly|tamamen
d|accordingly|buna uygun olarak
n|dimension|boyut
n|equation|denklem
v|extract|çıkarmak, ayıklamak
n|ideology|ideoloji
n|isolation|yalnızlık, izolasyon
d|namely|yani, şöyle ki
n|reasoning|akıl yürütme
d|notably|özellikle, dikkat çekici biçimde
n|bail|kefalet
w|delicate|narin
n|loser|kaybeden
n|massage|masaj
n|precision|hassasiyet
n|preservation|koruma
w|sheer|katıksız
w|stark|sert, çıplak
n|timber|kereste
w|transparent|şeffaf
n|upside|olumlu yan
n|void|boşluk
v|wipe|silmek
n|buck|dolar (argo)
n|harassment|taciz
n|pad|ped; bloknot
v|whip|kırbaçlamak; çırpmak
n|adaptation|uyarlama
a|theoretical|kuramsal
n|magnitude|büyüklük, çap
w|acute|akut
n|chin|çene
w|civic|yurttaşlık
n|coup|darbe
w|crude|ham
n|disposal|bertaraf
w|distinctive|ayırt edici
n|drone|drone
w|institutional|kurumsal
w|interim|geçici
n|outlet|priz; satış yeri
n|pledge|söz, taahhüt
n|portal|portal
n|puppy|köpek yavrusu
n|vaccine|aşı
n|prescription|reçete
n|disclosure|ifşa
p|weigh up|ölçüp biçmek
v|facilitate|kolaylaştırmak
n|interference|müdahale, karışma
n|affiliate|bağlı kuruluş
n|asylum|sığınma
n|barn|ahır
n|cathedral|katedral
n|cluster|küme
n|consistency|tutarlılık
w|deaf|sağır
n|denial|inkâr
n|dock|rıhtım
n|feat|başarı
n|freight|yük
w|inappropriate|uygunsuz
n|infant|bebek
n|insult|hakaret
n|outbreak|salgın, patlak verme
n|perfection|mükemmellik
w|quarterly|üç aylık
w|resistant|dayanıklı
w|skinny|sıska
v|sneak|gizlice girmek
w|sore|ağrıyan
n|spark|kıvılcım
n|straw|saman; pipet
n|successor|halef
w|uncertain|belirsiz
w|whatsoever|hiçbir şekilde
a|instrumental|etkili rol oynayan; enstrümantal
n|probe|soruşturma; sonda
n|rehabilitation|rehabilitasyon
n|injection|iğne, enjeksiyon
a|compelling|ikna edici, çarpıcı
a|irrelevant|konu dışı, ilgisiz
w|absent|yok, eksik
w|acoustic|akustik
w|atomic|atomik
n|bump|tümsek
n|cart|araba
n|cord|kordon
n|defendant|sanık
w|dense|yoğun
n|doctrine|öğreti
n|freshman|birinci sınıf öğrencisi
n|hazard|tehlike
n|hydrogen|hidrojen
w|intact|sağlam
n|intake|alım
n|lawn|çim
w|mistaken|yanılmış
n|pond|gölet
n|prey|av
n|prophet|peygamber
n|referendum|referandum
w|seasonal|mevsimlik
n|sequel|devam filmi
n|whale|balina
n|archive|arşiv
n|suspicion|şüphe
a|inclusive|kapsayıcı
n|bachelor|bekâr erkek; lisans
n|berry|dut, böğürtlen
n|capitalism|kapitalizm
n|caution|dikkat
n|clash|çatışma
w|compatible|uyumlu
n|curiosity|merak
w|explosive|patlayıcı
n|frontier|sınır
v|grasp|kavramak
w|handy|kullanışlı
n|mandate|yetki
n|merger|birleşme
w|portable|taşınabilir
v|slap|tokatlamak
n|succession|ardıllık
w|tactical|taktik
w|thereafter|ondan sonra
n|tuition|öğrenim ücreti
w|wholesale|toptan
a|frustrating|sinir bozucu
n|frustration|hayal kırıklığı
a|scattered|dağınık
n|sexuality|cinsellik
n|configuration|yapılandırma
v|enforce|uygulamak, zorla yürürlüğe koymak
a|explicit|açık, sarih
a|viable|uygulanabilir
d|substantially|önemli ölçüde
n|canvas|tuval
w|circular|dairesel
n|circulation|dolaşım
n|clearance|izin; temizleme
n|comedian|komedyen
n|conscience|vicdan
w|countless|sayısız
n|detention|gözaltı
w|lightly|hafifçe
n|marble|mermer
w|maritime|denizcilik
n|nominee|aday
n|oath|yemin
n|pillow|yastık
n|pirate|korsan
w|polar|kutup
n|revelation|vahiy; ifşa
v|stir|karıştırmak
w|superb|mükemmel
n|toast|kızarmış ekmek; kadeh kaldırma
w|tricky|zor, çetrefil
n|triumph|zafer
n|waist|bel
n|wreck|enkaz
d|explicitly|açıkça
a|architectural|mimari
n|dedication|bağlılık; ithaf
n|reconstruction|yeniden yapılanma
a|renowned|ünlü
d|supposedly|güya
n|wit|nükte, zekâ
a|integral|ayrılmaz, bütünleyici
w|absurd|saçma
w|amid|ortasında
w|binary|ikili
n|blend|karışım
n|brake|fren
n|collision|çarpışma
n|compassion|şefkat
a|appealing|çekici
n|correction|düzeltme
n|documentation|belgeleme
n|mainland|anakara
n|meditation|meditasyon
a|philosophical|felsefi
n|sensitivity|duyarlılık
n|supervisor|amir, yönetici
n|distress|sıkıntı
n|elevator|asansör
v|execute|yürütmek; idam etmek
n|feast|ziyafet
n|hike|yürüyüş; artış
n|homeland|vatan
w|lame|topal; zayıf
n|messenger|haberci
n|plea|savunma; yakarış
n|rhetoric|söylem
n|salvation|kurtuluş
w|secular|laik
n|sigh|iç çekme
w|sovereign|egemen
n|spouse|eş
w|tense|gergin
n|wilderness|vahşi doğa
n|motive|güdü, saik
a|robust|sağlam, güçlü
n|simulation|simülasyon
n|supervision|gözetim
a|thrilled|çok heyecanlı
n|trio|üçlü
n|adviser|danışman
n|anatomy|anatomi
n|chess|satranç
n|generator|jeneratör
v|grind|öğütmek|ground · ground
n|junction|kavşak
n|leap|sıçrama
w|postal|posta
w|profound|derin
n|prosecutor|savcı
n|rebellion|isyan
n|recipient|alıcı
n|refund|iade
w|sober|ayık
v|squeeze|sıkmak
n|terrain|arazi
n|virtue|erdem
""",
"C1.2": """
v|sustain|sürdürmek, ayakta tutmak
n|battlefield|savaş alanı
n|desktop|masaüstü
d|readily|kolayca; seve seve
n|acre|dönüm
v|bloom|çiçek açmak
n|bundle|demet
n|butterfly|kelebek
n|conjunction|bağlaç; birlik
w|costly|pahalı
n|descent|iniş; soy
n|directory|dizin
n|discharge|taburcu; boşaltım
v|dodge|kaçmak
n|halt|duruş
w|implied|örtük
n|inability|yetersizlik
n|mentor|akıl hocası
n|merchandise|mal
n|monk|keşiş
w|orthodox|ortodoks
w|overhead|tepede
w|prone|eğilimli
n|reunion|yeniden bir araya gelme
n|revival|canlanma
n|sanctuary|sığınak
n|siege|kuşatma
n|sleeve|kol (giysi)
n|spine|omurga
n|tenure|görev süresi
n|texture|doku
w|thankful|müteşekkir
n|triangle|üçgen
w|unclear|belirsiz
a|competent|yetkin
n|delegation|heyet
v|hail|övmek; çağırmak
n|indicator|gösterge
n|manuscript|müsvedde, makale metni
n|reliability|güvenilirlik
n|affection|sevgi
n|altitude|rakım
n|debris|enkaz
n|donor|bağışçı
w|fierce|şiddetli
n|gratitude|minnet
n|inequality|eşitsizlik
n|showcase|vitrin
n|subsidiary|yan kuruluş
n|theology|ilahiyat
n|velocity|hız
n|accountability|hesap verebilirlik
n|likelihood|olasılık
d|albeit|her ne kadar öyle olsa da
n|catalogue|katalog
d|continually|sürekli
n|coordinator|koordinatör
a|damaging|zararlı
n|deployment|konuşlandırma; dağıtım
n|genocide|soykırım
n|massacre|katliam
v|sack|kovmak
a|suburban|banliyö
a|troubled|sorunlu
n|ammunition|cephane
n|batch|parti
w|charitable|hayırsever
n|compliment|iltifat
w|exterior|dış
w|feminine|kadınsı
n|fountain|çeşme
n|fury|öfke
n|glance|bakış
n|glow|parıltı
w|humanitarian|insani
n|immunity|bağışıklık
n|liberation|kurtuluş
w|lone|yalnız
n|nickname|lakap
w|offshore|açık deniz
w|optional|isteğe bağlı
n|pioneer|öncü
n|prosperity|refah
n|refuge|sığınak
n|sphere|küre; alan
w|territorial|bölgesel
v|toss|atmak
w|verbal|sözlü
d|arguably|muhtemelen, tartışmaya açık olsa da
n|aftermath|sonrasında yaşananlar
n|transparency|şeffaflık
a|misleading|yanıltıcı
a|persistent|inatçı, kalıcı
p|opt for|-i tercih etmek
w|accountable|hesap verebilir
n|advocacy|savunuculuk
n|aggression|saldırganlık
n|burial|defin
n|clarity|açıklık
w|confidential|gizli
n|discretion|takdir; ağzı sıkılık
n|elevation|yükseklik
n|esteem|itibar
n|hospitality|misafirperverlik
n|hostage|rehine
n|literacy|okuryazarlık
n|particle|parçacık
n|progression|ilerleme
n|reservoir|baraj gölü
n|sensation|duyum; sansasyon
n|spotlight|spot ışığı
w|stern|sert
w|terrific|harika
v|unlock|kilidi açmak
n|vault|kasa; tonoz
n|coordination|koordinasyon
n|lad|delikanlı
n|obsession|takıntı
v|opt|seçmek, tercih etmek
n|rejection|ret
a|adverse|olumsuz, ters
n|biography|biyografi
n|broker|komisyoncu
w|destructive|yıkıcı
n|farewell|veda
n|fist|yumruk
w|fond of|düşkün
w|foolish|aptalca
n|landmark|simge yapı
w|liable|sorumlu
n|midst|orta
n|misery|sefalet
n|nursery|kreş
n|plague|veba
n|solidarity|dayanışma
n|specialty|uzmanlık
w|supernatural|doğaüstü
n|tomb|mezar
v|trim|kırpmak
n|voyage|deniz yolculuğu
n|landlord|ev sahibi
n|browser|tarayıcı
n|cocktail|kokteyl
n|imprisonment|hapis
n|trademark|ticari marka
v|interfere|müdahale etmek, karışmak
v|verify|doğrulamak
n|credibility|güvenilirlik
n|leverage|kaldıraç gücü, nüfuz
n|confession|itiraf
n|geometry|geometri
n|gossip|dedikodu
w|immense|muazzam
n|intersection|kavşak
w|juvenile|çocuk, genç
n|mankind|insanlık
n|militia|milis
w|pointless|anlamsız
n|proximity|yakınlık
w|selective|seçici
n|tribunal|mahkeme
n|villain|kötü adam
n|whistle|düdük
n|adjustment|ayarlama
d|undoubtedly|şüphesiz
n|surplus|fazlalık, artı değer
w|abusive|kötü davranan
n|alley|ara sokak
n|appetite|iştah
n|bully|zorba
n|dynasty|hanedan
n|forehead|alın
w|prospective|olası
w|unaware|habersiz
w|uncommon|nadir
w|underway|devam eden
w|unstable|dengesiz
w|vague|belirsiz
a|inclined|eğilimli
a|problematic|sorunlu
n|processor|işlemci
a|psychiatric|psikiyatrik
a|systematic|sistematik
n|abundance|bolluk
w|antique|antika
n|autonomy|özerklik
n|breeze|esinti
n|commodity|emtia
n|correspondent|muhabir
v|fade|solmak
n|fatigue|yorgunluk
w|fragile|kırılgan
n|instinct|içgüdü
n|irony|ironi
w|lethal|öldürücü
n|logistics|lojistik
n|morality|ahlak
w|mortal|ölümlü
n|radius|yarıçap
n|sovereignty|egemenlik
n|taxpayer|vergi mükellefi
a|cooperative|iş birliğine yatkın
a|prestigious|prestijli
a|symbolic|sembolik
n|correlation|korelasyon, ilişki
v|constitute|oluşturmak, teşkil etmek
a|arbitrary|keyfi
n|allowance|ödenek
w|autonomous|özerk
n|bait|yem
n|compilation|derleme
n|correspondence|yazışma
w|desirable|arzu edilir
w|incomplete|eksik
w|lengthy|uzun
n|levy|vergi
v|mock|alay etmek
n|niche|niş
w|obscure|belirsiz; az bilinen
w|successive|ardışık
w|timely|zamanında
v|utter|söylemek
v|yell|bağırmak
n|carriage|vagon; araba (atlı)
n|manipulation|manipülasyon
n|undergraduate|lisans öğrencisi
n|proposition|önerme
v|disclose|ifşa etmek, açıklamak
n|envy|kıskançlık
n|exile|sürgün
n|monopoly|tekel
n|outrage|öfke
n|paperwork|evrak işi
n|renewal|yenileme
n|slaughter|katliam
n|supplier|tedarikçi
w|tasty|lezzetli
v|testify|tanıklık etmek
v|tolerate|hoş görmek
v|creep|sürünmek, sinsice ilerlemek
n|exploitation|sömürü
n|synthesis|sentez
n|breakthrough|çığır açan gelişme
n|oversight|gözetim, gözden kaçırma
a|inherent|doğasında olan
a|straightforward|dolaysız, anlaşılır
n|decay|çürüme
n|dominance|hâkimiyet
n|imagery|imgeler
n|innocence|masumiyet
n|livestock|çiftlik hayvanları
w|notorious|kötü şöhretli
w|outright|tamamen, açıkça
w|overly|aşırı
n|refusal|ret
n|statute|kanun
w|thoughtful|düşünceli
w|vicious|acımasız
w|wholly|tamamen
n|activation|etkinleştirme
n|critique|eleştiri
n|investigator|müfettiş, araştırmacı
a|organizational|örgütsel
n|discourse|söylem
n|justification|gerekçelendirme
v|endure|dayanmak, katlanmak
n|premise|öncül, dayanak
a|inadequate|yetersiz
a|unprecedented|eşi görülmemiş
n|remedy|çare
n|compression|sıkıştırma
n|decree|kararname
n|despair|umutsuzluk
n|dividend|temettü
n|drift|sürüklenme
n|infinity|sonsuzluk
n|pardon|af
n|predecessor|selef
w|reckless|pervasız
n|redemption|kurtuluş; itfa
n|scent|koku
n|stimulus|uyarıcı
n|surge|ani artış
n|vocabulary|kelime dağarcığı
w|worthless|değersiz
n|willingness|isteklilik
n|assassination|suikast
n|congregation|cemaat
v|coordinate|koordine etmek
a|evolutionary|evrimsel
n|marketplace|pazar yeri
n|methodology|yöntembilim
v|exhaust|tüketmek
n|accord|anlaşma
n|assurance|güvence
n|boycott|boykot
n|cuisine|mutfak (yemek kültürü)
n|doom|kıyamet
v|flee|kaçmak|fled · fled
n|glimpse|bir anlık bakış
w|homemade|ev yapımı
w|infectious|bulaşıcı
w|inferior|aşağı
n|injustice|adaletsizlik
n|masterpiece|başyapıt
n|melody|melodi
n|reliance|bağımlılık
n|retention|tutma, saklama
w|rotten|çürük
n|taxation|vergilendirme
n|temper|huy, öfke
a|reluctant|isteksiz
n|fundraising|bağış toplama
n|memo|not, iç yazışma
a|decisive|belirleyici
v|confront|yüzleşmek, karşı karşıya gelmek
d|predominantly|ağırlıklı olarak
n|coffin|tabut
n|combo|kombinasyon
n|conductor|şef; iletken
w|decorative|dekoratif
w|definitive|kesin
n|epidemic|salgın
n|extraction|çıkarma
n|inheritance|miras
w|primitive|ilkel
w|righteous|doğru, erdemli
v|seize|ele geçirmek
n|skeleton|iskelet
w|vacant|boş
n|vicinity|civar
n|warmth|sıcaklık
a|ironic|ironik
v|minimize|en aza indirmek
d|thankfully|neyse ki
v|curb|dizginlemek, sınırlamak
a|inconsistent|tutarsız
n|bulletin|bülten
w|cautious|temkinli
v|cooperate|iş birliği yapmak
n|faction|hizip
v|gamble|kumar oynamak
w|harmless|zararsız
w|hopeful|umutlu
n|hygiene|hijyen
n|oppression|baskı
n|probation|deneme süresi; şartlı tahliye
n|projection|projeksiyon; tahmin
n|reproduction|üreme; kopya
n|prejudice|önyargı
v|neglect|ihmal etmek
a|capitalist|kapitalist
n|encouragement|cesaretlendirme
a|invalid|geçersiz
v|compensate|telafi etmek, tazmin etmek
v|render|hâle getirmek, sunmak
n|precedent|emsal
n|turnover|devir hızı, ciro
a|prevalent|yaygın
a|questionable|kuşkulu
n|apparatus|aygıt
n|bliss|mutluluk
w|bodily|bedensel
n|buffer|tampon
w|constructive|yapıcı
w|cosmic|kozmik
n|drawer|çekmece
n|ecosystem|ekosistem
w|exempt|muaf
w|faint|zayıf, belli belirsiz
w|foremost|en önde gelen
n|metabolism|metabolizma
w|newborn|yeni doğan
n|parody|parodi
n|parole|şartlı tahliye
n|sociology|sosyoloji
n|traction|çekiş
w|unwanted|istenmeyen
n|variant|varyant
w|wherein|ki orada
n|tenant|kiracı
n|alignment|hizalama; uyum
a|ecological|ekolojik
v|forge|sahtesini yapmak; oluşturmak
a|parental|ebeveyn
v|stab|bıçaklamak
n|hierarchy|hiyerarşi
v|attribute|atfetmek, bağlamak
a|abundant|bol, bereketli
n|objection|itiraz
n|algebra|cebir
n|antenna|anten
n|audition|seçme
v|complement|tamamlamak
v|conquer|fethetmek
n|conquest|fetih
n|continuity|süreklilik
v|crawl|emeklemek
w|credible|inandırıcı
n|digit|rakam
n|drainage|drenaj
n|felony|ağır suç
n|fortress|kale
n|herd|sürü
w|immortal|ölümsüz
n|incumbent|görevdeki kişi
w|insufficient|yetersiz
w|literal|kelimesi kelimesine
w|lunar|ay ile ilgili
w|maternal|anne tarafı
n|memoir|anı
n|modification|değişiklik
n|occurrence|olay
n|offspring|döl, çocuk
n|pathway|yol
n|prohibition|yasak
n|scar|yara izi
n|scripture|kutsal metin
n|simplicity|sadelik
n|trader|tüccar
w|undercover|gizli
n|vegetation|bitki örtüsü
n|vein|damar
n|embarrassment|mahcubiyet
n|fairness|adalet, hakkaniyet
a|ideological|ideolojik
n|insider|içeriden biri
a|neighbouring|komşu
a|biased|önyargılı, taraflı
n|corpse|ceset
n|designation|atama; ad
n|diploma|diploma
v|dispatch|göndermek
n|extinction|yok olma
n|geology|jeoloji
n|mentality|zihniyet
w|phenomenal|olağanüstü
n|shipment|sevkiyat
w|spatial|mekânsal
w|stubborn|inatçı
n|transplant|nakil
n|volcano|yanardağ
n|calculation|hesaplama
n|newsletter|bülten
a|noticeable|fark edilir
n|armour|zırh
w|disciplinary|disiplin
n|endorsement|onay
w|forensic|adli
w|forthcoming|yaklaşan
w|infamous|kötü şöhretli
w|lateral|yanal
w|lifelong|ömür boyu
w|naive|saf
n|prestige|prestij
w|rigid|katı
n|specification|şartname
w|splendid|muhteşem
n|telescope|teleskop
w|unreasonable|makul olmayan
n|valuation|değerleme
v|violate|ihlal etmek
w|vivid|canlı
v|bind|bağlamak
n|conception|kavrayış; döllenme
n|deed|eylem; tapu
n|gallon|galon
n|relevance|ilgi, alaka
v|utilize|yararlanmak
v|merge|birleştirmek
v|initiate|başlatmak
n|scrutiny|yakın inceleme
n|anticipation|beklenti
w|auxiliary|yardımcı
n|baggage|bagaj
n|bounty|ödül
n|contempt|küçümseme
n|endurance|dayanıklılık
n|expenditure|harcama
w|overweight|kilolu
w|potent|güçlü
n|rust|pas
n|seizure|nöbet; el koyma
w|singular|tekil
w|stray|başıboş
w|systemic|sistemik
n|tempo|tempo
n|torch|meşale; el feneri
w|understandable|anlaşılır
w|upright|dik
w|vain|kibirli; boş
n|vanity|kibir
w|worthwhile|zahmete değer
n|emergence|ortaya çıkış
d|ironically|ne gariptir ki
v|nod|başını sallamak
n|allocation|tahsis
d|whereby|ki bununla
v|resemble|benzemek
w|bankrupt|iflas etmiş
v|blink|göz kırpmak
w|childish|çocukça
n|coil|bobin
n|covenant|ahit
n|devotion|bağlılık
n|disgrace|rezalet
w|eventual|nihai
v|excel|üstün olmak
n|greed|açgözlülük
n|inflammation|iltihap
n|magnet|mıknatıs
v|notify|bildirmek
n|pact|pakt
w|paramount|en önemli
n|patron|hami; müşteri
v|regain|yeniden kazanmak
v|renew|yenilemek
n|revolt|isyan
w|rightly|haklı olarak
n|shrine|türbe
v|shrink|küçülmek|shrank · shrunk
w|solitary|yalnız
n|sorrow|keder
n|termination|fesih
n|thigh|uyluk
w|unpaid|ödenmemiş
w|unsuccessful|başarısız
n|warranty|garanti
v|thrive|gelişmek, serpilmek
n|dilemma|ikilem
n|aluminium|alüminyum
n|contention|savunulan görüş
v|strive|çabalamak|strove · striven
a|feasible|yapılabilir
a|flawed|kusurlu
n|aisle|koridor
n|atom|atom
w|bilateral|ikili
v|bleed|kanamak|bled · bled
n|caption|altyazı
v|choke|boğulmak
v|condemn|kınamak
n|disguise|kılık
n|empathy|empati
n|impulse|dürtü
w|incapable|yetersiz
w|insecure|güvensiz
n|knot|düğüm
n|confrontation|yüzleşme, çatışma
n|contributor|katkıda bulunan
n|dismissal|işten çıkarma
n|philosopher|filozof
d|presently|şu anda
n|realization|farkına varma; gerçekleşme
v|steer|yönlendirmek
n|specimen|numune
n|disruption|kesinti, altüst oluş
n|milestone|dönüm noktası
a|marginal|marjinal, sınırda
n|magistrate|sulh hâkimi
n|predator|yırtıcı hayvan
n|tactic|taktik
n|analogy|benzeşim
n|vulnerability|zafiyet, savunmasızlık
v|delegate|yetki devretmek
v|deploy|konuşlandırmak, devreye almak
n|validity|geçerlilik
v|appoint|atamak
n|counterpart|muadil, karşılık
n|a gaze|bakış
v|to gaze|dik dik bakmak
n|indictment|iddianame
n|limb|uzuv
n|transcript|döküm, transkript
v|manipulate|manipüle etmek, yönlendirmek
v|retrieve|geri almak, geri getirmek
a|intriguing|merak uyandıran
n|accomplishment|başarı
n|aide|yardımcı
n|broadband|geniş bant
n|constituency|seçim bölgesi
n|councillor|belediye meclisi üyesi
n|diplomat|diplomat
n|firearm|ateşli silah
v|preach|vaaz vermek
n|solicitor|avukat
a|rigorous|titiz, sıkı
a|unanimous|oybirliğiyle
n|defect|kusur
a|disastrous|felaket
v|drown|boğulmak
n|exclusion|dışlama
v|revive|canlandırmak
n|strand|tel, lif
a|theatrical|tiyatral
n|trustee|mütevelli
n|turnout|katılım oranı
v|manifest|açığa vurmak, tezahür etmek
a|imminent|çok yakın, an meselesi
a|susceptible|duyarlı, açık (etkiye)
w|honourable|onurlu
n|commentator|yorumcu
n|fibre|lif
n|fixture|demirbaş; maç
a|peculiar|tuhaf
v|reside|ikamet etmek
a|vibrant|canlı
v|suppress|bastırmak
n|backlash|sert tepki
n|prevalence|yaygınlık
a|outdated|güncelliğini yitirmiş
a|versatile|çok yönlü
v|accelerate|hızlanmak
n|dependence|bağımlılık
n|dictator|diktatör
n|optimism|iyimserlik
n|proceeding|dava; işlem
v|undermine|baltalamak
v|intervene|araya girmek, müdahale etmek
v|terminate|sonlandırmak
v|withstand|dayanmak, karşı koymak
n|standpoint|bakış açısı
v|slash|kesmek; büyük oranda indirmek
a|plausible|makul, inandırıcı
n|restraint|ölçülülük
v|assemble|toplanmak; monte etmek
n|chunk|parça
n|deficiency|eksiklik
v|dub|lakap takmak; dublaj yapmak
n|incidence|görülme sıklığı
n|query|soru, sorgu
a|coherent|tutarlı
v|portray|tasvir etmek, canlandırmak
v|refrain|kaçınmak, geri durmak
v|endorse|onaylamak, desteklemek
v|align|hizalamak; uyumlu hale getirmek
v|await|beklemek
v|maximize|en üst düzeye çıkarmak
v|plead|yalvarmak; savunmak (mahkeme)
d|seldom|nadiren
n|shareholder|hissedar
n|assertion|iddia
v|inspect|denetlemek, incelemek
n|practitioner|uygulayıcı
v|reproduce|yeniden üretmek
a|empirical|deneysel
a|militant|militan
n|a militant|militan
n|peasant|köylü
n|regulator|düzenleyici kurum
v|assert|savunmak, öne sürmek
v|differentiate|ayırt etmek
v|presume|varsaymak
v|tailor|özel olarak uyarlamak
a|scarce|kıt
n|casualty|kayıp (yaralı/ölü)
n|hostility|düşmanlık
v|soak|ıslatmak
n|spectacle|gösteri
v|attain|elde etmek, ulaşmak
n|benchmark|kıyas ölçütü
n|flaw|kusur
a|proportional|orantılı
n|accusation|suçlama
n|contender|aday, rakip
v|disrupt|kesintiye uğratmak, bozmak
a|redundant|gereksiz, fazlalık
a|cynical|alaycı
n|accumulation|birikim
v|congratulate|tebrik etmek
n|a grin|sırıtma
v|to grin|sırıtmak
v|commence|başlamak
n|resilience|dayanıklılık, direnç
n|adolescent|ergen
n|backdrop|arka plan, fon
n|columnist|köşe yazarı
n|competence|yeterlilik
v|dictate|dikte etmek; dayatmak
v|rotate|döndürmek; nöbetleşe yapmak
a|ambiguous|belirsiz, çift anlamlı
n|concession|taviz; indirim
v|nominate|aday göstermek
v|adhere|bağlı kalmak, uymak
n|parameter|parametre
v|induce|yol açmak, teşvik etmek
a|eminent|seçkin, önde gelen
v|convict|mahkûm etmek
n|subsidy|sübvansiyon
v|vow|yemin etmek
v|contend|iddia etmek
v|amend|düzeltmek, tadil etmek
v|prevail|hüküm sürmek, galip gelmek
n|urgency|aciliyet
a|detrimental|zararlı
a|intricate|karmaşık, ince işlenmiş
n|bureaucracy|bürokrasi
v|cater|yemek hizmeti vermek; hitap etmek
n|educator|eğitimci
n|outsider|yabancı, dışarıdan biri
n|misuse|kötüye kullanım
n|downside|olumsuz taraf
v|mitigate|hafifletmek, azaltmak
v|administer|yönetmek; uygulamak
v|expire|süresi dolmak
v|haunt|musallat olmak
v|indulge|kendini şımartmak
n|inmate|mahkûm
v|prosecute|kovuşturmak
v|dispose|elden çıkarmak, bertaraf etmek
v|overlook|gözden kaçırmak, göz yummak
v|persist|ısrar etmek, sürüp gitmek
n|rationale|gerekçe, mantık
w|favourable|elverişli
v|evacuate|tahliye etmek
v|flourish|gelişmek, serpilmek
n|quota|kota
n|residue|kalıntı
v|weave|dokumak
v|alleviate|hafifletmek, azaltmak
v|uphold|desteklemek, sürdürmek (ilke)
v|conceal|gizlemek
v|erect|dikmek, inşa etmek
n|subscriber|abone
v|collaborate|iş birliği yapmak
v|dedicate|adamak, tahsis etmek
v|oversee|denetlemek, gözetmek
n|persistence|azim, süreklilik
v|boast|övünmek
v|descend|inmek
v|empower|yetkilendirmek, güçlendirmek
v|tighten|sıkılaştırmak
v|correspond|karşılık gelmek, yazışmak
a|resilient|dirençli
n|allegation|iddia
n|outing|gezi
v|provoke|kışkırtmak, tetiklemek
v|weaken|zayıflatmak
v|cling|sıkıca tutunmak
v|dissolve|çözünmek; feshetmek
v|plunge|dalmak; düşmek
v|coincide|çakışmak, aynı anda olmak
v|accumulate|birikmek, biriktirmek
v|concede|kabullenmek, taviz vermek
v|deter|caydırmak
n|foreigner|yabancı
v|postpone|ertelemek
v|abolish|kaldırmak
v|kidnap|kaçırmak (insan)
v|aspire|arzulamak
a|thought-provoking|düşündürücü
v|consolidate|pekiştirmek
n|imbalance|dengesizlik
v|diminish|azalmak, küçültmek
v|simplify|basitleştirmek
v|applaud|alkışlamak
n|enthusiast|meraklı, tutkun
n|extremist|aşırılıkçı
v|stabilize|istikrara kavuşturmak
a|tentative|geçici, deneme niteliğinde
v|heed|dikkate almak
n|contradiction|çelişki
n|endeavour|çaba, girişim
n|counselling|danışmanlık
n|feasibility|yapılabilirlik
n|viability|yaşayabilirlik, uygulanabilirlik
v|inject|enjekte etmek
v|simulate|benzetim yapmak
n|proficiency|yetkinlik
v|enact|yasalaştırmak
n|sanction|yaptırım
n|stereotype|klişe, kalıp yargı
v|cultivate|geliştirmek, yetiştirmek
n|disparity|eşitsizlik, fark
n|reluctance|isteksizlik
v|betray|ihanet etmek
v|defy|meydan okumak
v|divert|yönünü değiştirmek
v|stumble|tökezlemek
n|hurdle|engel
v|depict|betimlemek, tasvir etmek
v|contemplate|derin düşünmek, tasarlamak
v|carve|oymak
v|diagnose|teşhis koymak
n|substitution|ikame, değiştirme
v|compute|hesaplamak
v|validate|doğrulamak, geçerli kılmak
v|conceive|tasarlamak; gebe kalmak
v|embark|gemiye binmek; başlamak
v|hinder|engellemek
a|negligible|ihmal edilebilir
a|pervasive|her yere yayılmış
v|prescribe|reçete yazmak
v|soar|fırlamak, yükselmek
v|vanish|kaybolmak
v|compile|derlemek
n|adversity|zorluk, sıkıntı
n|rumour|söylenti
v|authorize|yetki vermek
v|elevate|yükseltmek
n|guerrilla|gerilla
n|ambiguity|belirsizlik, muğlaklık
n|setback|aksilik, geri adım
n|beneficiary|yararlanıcı, lehtar
v|conserve|korumak; tasarruf etmek
v|discard|atmak
v|stun|sersemletmek; şaşkına çevirmek
v|designate|belirlemek, atamak
v|originate|kaynaklanmak, doğmak
v|exert|(çaba/baskı) uygulamak
v|infect|bulaştırmak
n|insertion|ekleme
a|far-fetched|zorlama, saçma
a|unavoidable|kaçınılmaz
v|pinpoint|tam olarak belirlemek
a|conspicuous|göze çarpan
v|escalate|tırmanmak, büyümek
a|indispensable|vazgeçilmez
v|deem|addetmek
v|inhibit|engellemek, ketlemek
v|loom|(tehdit gibi) belirmek
v|inflict|vermek (zarar)
a|unbiased|tarafsız
v|invoke|başvurmak; anmak
v|forfeit|kaybetmek
v|supervise|denetlemek
n|counsellor|danışman
v|characterize|nitelendirmek
v|allocate|tahsis etmek, ayırmak
n|complication|komplikasyon
v|instruct|talimat vermek
v|linger|oyalanmak; sürmek
n|omission|ihmal, atlama
v|broaden|genişletmek
v|reassure|güven vermek, içini rahatlatmak
a|conclusive|kesin, belirleyici
a|exhaustive|çok kapsamlı, eksiksiz
n|aspiration|arzu, hedef
v|enrich|zenginleştirmek
v|incur|maruz kalmak (masraf)
v|shrug|omuz silkmek
v|denote|belirtmek, işaret etmek
n|discrepancy|tutarsızlık, uyuşmazlık
v|withhold|esirgemek|withheld · withheld
v|compel|zorlamak, mecbur bırakmak
v|refine|inceltmek, iyileştirmek
n|constraint|kısıt
a|predominant|baskın
v|evoke|uyandırmak
n|privatization|özelleştirme
v|proclaim|ilan etmek
n|youngster|genç
v|encompass|kapsamak
a|undisputed|tartışmasız
v|fathom|kavramak
v|widen|genişletmek
v|quantify|nicelleştirmek, sayısallaştırmak
v|denounce|kınamak
v|recount|anlatmak
n|inconsistency|tutarsızlık
v|formulate|formüle etmek
n|misconception|yanlış kanı
v|overturn|bozmak; devirmek
v|shatter|paramparça olmak
v|tempt|baştan çıkarmak
v|entail|gerektirmek, beraberinde getirmek
n|drawback|dezavantaj
v|detain|gözaltına almak
v|criticise|eleştirmek
v|defer|ertelemek
v|unveil|tanıtmak, perdeyi kaldırmak
v|correlate|ilişkilendirmek, bağıntı kurmak
n|imposition|haksız yük
v|counteract|karşı koymak
v|devise|tasarlamak, kurgulamak
v|exaggerate|abartmak
v|confer|danışmak; vermek (unvan)
v|deprive|mahrum bırakmak
v|mobilize|seferber etmek
v|allege|iddia etmek (kanıtsız)
v|condone|göz yummak
v|minimise|en aza indirmek
v|circulate|dolaşmak; dağıtmak
v|embody|somutlaştırmak, cisimleştirmek
a|cumbersome|hantal, kullanışsız
v|intensify|yoğunlaşmak
v|incline|eğilim göstermek
v|deteriorate|kötüleşmek
v|overwhelm|bunaltmak, alt etmek
v|oblige|zorunlu kılmak; iyilik yapmak
n|apprehension|endişe
n|nuance|nüans, ince ayrım
a|sceptical|şüpheci
d|henceforth|bundan böyle
v|distort|çarpıtmak
n|motorist|sürücü
v|unify|birleştirmek
p|insofar as|-diği ölçüde
n|authorisation|yetkilendirme
n|atrocity|vahşet
n|hindrance|engel
a|fluctuating|dalgalanan
v|preside|başkanlık etmek
n|leeway|hareket alanı, esneklik
v|displace|yerinden etmek
v|utilise|kullanmak, yararlanmak
v|embed|yerleştirmek, gömmek
v|impair|zayıflatmak, bozmak
v|confine|sınırlamak, kısıtlamak
v|enquire|bilgi almak, sormak
v|ensue|ardından gelmek
v|obsess|takıntı yapmak
n|villager|köylü
v|imprison|hapsetmek
v|heighten|artırmak
v|reaffirm|yeniden teyit etmek
v|diverge|ayrılmak, sapmak
n|leniency|hoşgörü
v|prioritise|önceliklendirmek
d|demonstrably|kanıtlanabilir şekilde
v|entitle|hak vermek
v|enrol|kaydolmak
v|devastate|harap etmek
n|shortcoming|eksiklik
n|plausibility|inandırıcılık
n|upturn|toparlanma, yükseliş
v|enshrine|güvence altına almak
""",
"C2.1": """
n|ulterior motive|art niyet
n|change of heart|fikir değişikliği
n|negligence|ihmal
n|undertaking|girişim, üstlenilen iş
v|substantiate|kanıtlamak
v|thwart|engellemek, boşa çıkarmak
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
n|ambivalence|ikircik
n|anachronism|anakronizm
n|composure|soğukkanlılık
n|disdain|küçümseme
n|pipe dream|hayal ürünü
n|complacency|rehavet
n|fallacy|safsata, yanılgı
v|appease|yatıştırmak
v|stigmatise|damgalamak
v|evade|kaçmak, kaçınmak
v|erode|aşınmak
v|co-opt|kendine mal etmek
p|wear down|yıpratmak
p|get out of hand|kontrolden çıkmak
p|come to terms with|kabullenmek
p|be at odds with|çelişmek
a|meticulous|titiz
a|flimsy|inandırıcı olmayan
a|outrageous|akıl almaz
a|latent|gizli
a|perfidious|hain
a|irrefutable|çürütülemez
a|hesitant|tereddütlü
d|in passing|laf arasında
n|acumen|keskin zekâ, sezgi
n|alacrity|şevk, istek
n|antipathy|antipati
n|candour|açık sözlülük
n|clout|nüfuz
n|conundrum|bilmece, çıkmaz
n|debacle|fiyasko
n|euphemism|örtmece
n|impasse|çıkmaz
n|predilection|düşkünlük
n|propensity|eğilim
n|tenacity|azim
n|vicissitudes|iniş çıkışlar
v|bolster|desteklemek
v|circumvent|atlatmak
v|corroborate|doğrulamak
v|exacerbate|kötüleştirmek
v|galvanise|harekete geçirmek
v|mollify|yatıştırmak
v|obviate|gereksiz kılmak
v|placate|gönlünü almak
v|relinquish|vazgeçmek
v|repudiate|reddetmek
v|stymie|engellemek
v|vindicate|haklı çıkarmak
a|astute|zeki, kurnaz
a|cogent|ikna edici
a|commensurate|orantılı
a|disingenuous|samimiyetsiz
a|egregious|korkunç, göze batan
a|fastidious|titiz, müşkülpesent
a|gratuitous|gereksiz, sebepsiz
a|inexorable|durdurulamaz
a|nebulous|bulanık
a|perfunctory|baştan savma
a|tenuous|zayıf
d|ostensibly|görünüşte
n|aberration|sapma
n|acquiescence|boyun eğme
n|adulation|aşırı övgü
n|affinity|yakınlık
n|animosity|düşmanlık
n|apathy|ilgisizlik
n|aplomb|soğukkanlılık
n|arrogance|kibir
n|audacity|cüret
n|austerity|kemer sıkma
n|avarice|açgözlülük
n|benevolence|iyilikseverlik
n|bigotry|bağnazlık
n|bravado|kabadayılık
n|brevity|kısalık
n|cacophony|ses kargaşası
n|camaraderie|yoldaşlık
n|clemency|merhamet
n|complicity|suç ortaklığı
n|conjecture|varsayım
n|connoisseur|uzman, ehil
n|contrition|pişmanlık
n|credence|inanç, güven
n|culpability|kusurluluk
n|dearth|kıtlık
n|decorum|edep
n|deference|hürmet
n|demeanour|tavır
n|derision|alay
n|diatribe|ağır eleştiri
n|diligence|özen, çalışkanlık
n|discord|anlaşmazlık
n|duplicity|ikiyüzlülük
n|effrontery|küstahlık
n|eloquence|belâgat
n|enigma|bilmece
n|equanimity|soğukkanlılık
n|euphoria|coşku
n|exasperation|bıkkınlık
n|facade|cephe, görünüş
n|fervour|şevk
n|finesse|incelik
n|folly|ahmaklık
n|fortitude|metanet
n|frivolity|uçarılık
n|futility|beyhudelik
n|gravitas|ağırbaşlılık
n|gullibility|saflık
n|hindsight|geriye dönük anlayış
n|hypocrisy|ikiyüzlülük
n|idiosyncrasy|kendine has özellik
n|ignominy|rezillik
n|impetus|itici güç
n|impunity|cezasızlık
n|inertia|atalet
n|ingenuity|yaratıcılık
n|introspection|iç gözlem
n|lethargy|uyuşukluk
n|longevity|uzun ömür
n|magnanimity|yüce gönüllülük
n|malaise|huzursuzluk
n|malice|kötü niyet
n|melancholy|hüzün
n|mitigation|hafifletme
n|nostalgia|nostalji
n|nuisance|baş belası
n|obstinacy|inatçılık
n|onus|sorumluluk, yük
n|opulence|şatafat
n|paradigm shift|paradigma değişimi
n|parity|eşitlik
n|paucity|azlık
n|perseverance|sebat
n|petulance|huysuzluk
n|plight|kötü durum
n|pragmatism|pragmatizm
n|precedence|öncelik
n|prerogative|ayrıcalık
n|probity|dürüstlük
n|prudence|sağduyu
n|rapport|yakınlık, uyum
n|rebuttal|çürütme
n|recourse|başvuru yolu
n|remorse|vicdan azabı
n|resentment|kırgınlık
n|restitution|tazmin
n|reticence|suskunluk
n|reverence|saygı
n|scepticism|şüphecilik
n|serendipity|hoş tesadüf
n|solace|teselli
n|stigma|damga
n|subterfuge|hile
n|trepidation|endişe
n|ubiquity|her yerde olma
n|veneer|cila, sahte görünüş
n|veracity|doğruluk
n|vigilance|uyanıklık
n|zeal|şevk
v|abdicate|tahttan feragat etmek
v|abhor|tiksinmek
v|admonish|uyarmak
v|allay|yatıştırmak
v|ameliorate|iyileştirmek
v|assuage|dindirmek
v|beguile|büyülemek
v|belittle|küçümsemek
v|berate|azarlamak
v|capitulate|teslim olmak
v|castigate|şiddetle eleştirmek
v|cajole|kandırmak, dil dökmek
v|chastise|cezalandırmak
v|coerce|zorlamak
v|commiserate|teselli etmek
v|concur|aynı görüşte olmak
v|construe|yorumlamak
v|debunk|çürütmek
v|decry|kınamak
v|deride|alay etmek
v|discern|ayırt etmek
v|disparage|kötülemek
v|dissuade|vazgeçirmek
v|elucidate|açıklamak
v|emulate|örnek almak
v|encroach|tecavüz etmek (hak)
v|engender|doğurmak
v|enthral|büyülemek
v|epitomise|simgelemek
v|eschew|kaçınmak
v|exonerate|aklamak
v|expedite|hızlandırmak
v|extol|övmek
v|fabricate|uydurmak
v|flout|hiçe saymak
v|foment|kışkırtmak
v|forgo|vazgeçmek
v|hamper|engellemek
v|harangue|nutuk atmak
v|impede|engellemek
v|implore|yalvarmak
v|incite|kışkırtmak
v|instigate|başlatmak, kışkırtmak
v|jeopardise|tehlikeye atmak
v|languish|sürünmek
v|negate|geçersiz kılmak
v|ostracise|dışlamak
v|pacify|yatıştırmak
v|perpetuate|sürdürmek
v|ponder|derin düşünmek
v|precipitate|hızlandırmak, tetiklemek
v|preclude|engellemek
v|procrastinate|ertelemek
v|proliferate|çoğalmak
v|rebuke|azarlamak
v|recant|sözünü geri almak
v|reciprocate|karşılık vermek
v|reprimand|kınamak
v|rescind|iptal etmek
v|reverberate|yankılanmak
v|scrutinise|incelemek
v|squander|israf etmek
v|stifle|bastırmak
v|subjugate|boyun eğdirmek
v|supplant|yerini almak
v|transcend|aşmak
v|underpin|temellendirmek
v|usurp|gasp etmek
v|vilify|kötülemek
v|waive|feragat etmek
v|wane|azalmak
v|waver|tereddüt etmek
v|wield|kullanmak (güç)
a|abject|sefil
a|acerbic|iğneleyici
a|adamant|kararlı
a|adroit|becerikli
a|affable|cana yakın
a|ambivalent|kararsız
a|amenable|uysal
a|apprehensive|endişeli
a|arcane|gizemli
a|ardent|ateşli
a|articulate|kendini iyi ifade eden
a|auspicious|uğurlu
a|austere|sade, sert
a|banal|bayağı
a|benign|iyi huylu
a|blatant|bariz
a|brusque|sert, kaba
a|callous|duygusuz
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
n|truism|herkesin bildiği gerçek
n|U-turn|U dönüşü
n|litmus test|turnusol testi
n|trifle|önemsiz şey
n|hotchpotch|karmaşa
n|dig|iğneleme
n|pretext|bahane
n|schadenfreude|başkasının zararına sevinme
p|throw in the towel|pes etmek
p|buy a pig in a poke|görmeden almak
p|put on the back burner|rafa kaldırmak
p|not mince one's words|lafını esirgememek
p|put one's cards on the table|açık oynamak
p|think outside the box|kalıpların dışında düşünmek
p|read between the lines|satır arasını okumak
p|add fuel to the fire|yangına körükle gitmek
p|the elephant in the room|herkesin görmezden geldiği sorun
p|a blessing in disguise|hayırlı bir kötülük
p|let the cat out of the bag|ağzından kaçırmak
p|once in a blue moon|kırk yılda bir
a|blasé|bıkkın, umursamaz
a|dubious|şüpheli
a|ephemeral|geçici
a|laconic|kısa ve öz
a|pretentious|iddialı, gösterişçi
a|eccentric|tuhaf
n|anathema|nefret edilen şey
n|chicanery|hile
n|ennui|can sıkıntısı
n|hubris|kibir
n|largesse|cömertlik
n|minutiae|ince ayrıntılar
n|panacea|her derde deva
n|sycophant|dalkavuk
n|vitriol|zehir zemberek söz
n|zeitgeist|çağın ruhu
v|obfuscate|bulanıklaştırmak
v|prevaricate|kıvırmak
v|proselytise|propaganda yapmak
v|vacillate|tereddüt etmek
p|a double-edged sword|iki ucu keskin kılıç
p|bark up the wrong tree|yanlış kapıyı çalmak
p|cut to the chase|sadede gelmek
p|have an axe to grind|kişisel hesabı olmak
p|jump on the bandwagon|modaya uymak
p|move the goalposts|kuralları sonradan değiştirmek
p|play devil's advocate|şeytanın avukatlığını yapmak
p|sit on the fence|tarafsız kalmak
p|the tip of the iceberg|buzdağının görünen yüzü
p|throw caution to the wind|her şeyi göze almak
a|abstruse|anlaşılmaz
a|antediluvian|çok eski kafalı
a|bombastic|tumturaklı
a|insouciant|kaygısız
a|obsequious|dalkavuk
a|pernicious|sinsice zararlı
a|quixotic|hayalperest
a|sanctimonious|ikiyüzlü dindar
a|supercilious|kibirli
a|truculent|kavgacı
a|unctuous|yağcı
a|candid|açık sözlü
a|capricious|kaprisli
a|caustic|yakıcı
a|clandestine|gizli
a|complacent|rehavet içinde
a|conducive|elverişli
a|contentious|tartışmalı
a|copious|bol
a|cursory|üstünkörü
a|daunting|göz korkutucu
a|deft|becerikli
a|despondent|umutsuz
a|diffident|çekingen
a|dilapidated|harap
a|discerning|zevk sahibi
a|disparate|farklı
a|dogmatic|dogmatik
a|ebullient|coşkun
a|eclectic|eklektik
a|efficacious|etkili
a|elusive|yakalanması zor
a|enigmatic|esrarengiz
a|erratic|düzensiz
a|esoteric|ezoterik
a|exemplary|örnek
a|exorbitant|fahiş
a|expedient|uygun, işe yarar
a|facetious|şakacı
a|fallible|yanılabilir
a|fervent|ateşli
a|flagrant|açık, rezil
a|frugal|tutumlu
a|furtive|sinsi
a|gregarious|sosyal
a|haphazard|gelişigüzel
a|heinous|iğrenç
a|histrionic|abartılı
a|idiosyncratic|kendine özgü
a|ignominious|utanç verici
a|immaculate|kusursuz
a|impeccable|kusursuz
a|imperative|zorunlu
a|impetuous|aceleci
a|implacable|yatıştırılamaz
a|incessant|aralıksız
a|incongruous|uyumsuz
a|indefatigable|yorulmak bilmez
a|indelible|silinmez
a|indolent|tembel
a|innate|doğuştan
a|innocuous|zararsız
a|insidious|sinsi
a|intrepid|korkusuz
a|irascible|asabi
a|judicious|akıllıca
a|languid|bitkin
a|lucid|açık, net
a|ludicrous|gülünç
a|magnanimous|yüce gönüllü
a|mundane|sıradan
a|nefarious|kötü
a|nonchalant|kayıtsız
a|nuanced|incelikli
a|obstinate|inatçı
a|ominous|uğursuz
a|onerous|külfetli
a|ostentatious|gösterişli
a|palpable|elle tutulur
a|paltry|önemsiz
a|placid|sakin
a|poignant|dokunaklı
a|pragmatic|pragmatik
a|precarious|güvencesiz
a|prescient|öngörülü
a|pristine|bozulmamış
a|prolific|üretken
a|prudent|ihtiyatlı
a|quaint|şirin, eski tarz
a|rampant|yaygın, dizginsiz
a|recalcitrant|inatçı
a|reticent|ketum
a|sanguine|iyimser
a|scrupulous|titiz
a|scathing|sert, yaralayıcı
a|serene|sakin
a|shrewd|kurnaz
a|spurious|sahte
a|staunch|sadık
a|stoic|sabırlı
a|succinct|öz
a|superfluous|gereksiz
a|surreptitious|gizli
a|taciturn|az konuşan
a|tangible|somut
a|trite|basmakalıp
a|unequivocal|kesin
a|venerable|muhterem
a|verbose|laf kalabalığı yapan
a|vindictive|kinci
a|volatile|değişken
a|wary|tetikte
a|whimsical|kaprisli, hayalperest
a|zealous|gayretli
d|inadvertently|yanlışlıkla
d|perfunctorily|baştan savma
d|vehemently|şiddetle
d|unequivocally|kesinlikle
d|invariably|her zaman
d|wholeheartedly|tüm kalbiyle
d|begrudgingly|isteksizce
p|a far cry from|-den çok uzak
p|a moot point|tartışmalı nokta
p|add insult to injury|yaraya tuz basmak
p|at loggerheads|arası açık
p|beyond the pale|kabul edilemez
p|by the same token|aynı şekilde
p|come full circle|başa dönmek
p|cut both ways|iki tarafı da etkilemek
p|err on the side of caution|temkinli davranmak
p|fall on deaf ears|kulak asılmamak
p|get wind of|kulağına gelmek
p|go against the grain|tabiatına aykırı olmak
p|hold sway|hâkim olmak
p|in the offing|yakında, ufukta
p|keep at bay|uzak tutmak
p|leave no stone unturned|her yolu denemek
p|make headway|ilerleme kaydetmek
p|on tenterhooks|diken üstünde
p|pay lip service to|laf olsun diye desteklemek
p|pull one's weight|üzerine düşeni yapmak
p|rest on one's laurels|başarısıyla yetinmek
p|run the gauntlet|ateş altında kalmak
p|steal someone's thunder|birinin parlayacağı anı çalmak
p|take with a pinch of salt|ihtiyatla karşılamak
p|the writing on the wall|kötü sonun işaretleri
p|throw down the gauntlet|meydan okumak
p|to all intents and purposes|fiilen
p|turn a blind eye|göz yummak
p|up in arms|ayaklanmış
p|vested interest|kişisel çıkar
p|with bated breath|nefesini tutarak
p|a red herring|dikkat dağıtıcı yanlış iz
p|a Pyrrhic victory|pirüs zaferi
p|an uphill battle|zorlu mücadele
p|caught between a rock and a hard place|iki ateş arasında
p|cross the Rubicon|geri dönülmez adım atmak
p|draw the line|sınırı çizmek
p|let sleeping dogs lie|kurcalamamak
p|on the fence|kararsız
p|the last straw|bardağı taşıran son damla
p|touch and go|riskli, belirsiz
""",
}

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
n|approach|yaklaşım
n|aim|amaç
n|chapter|bölüm
n|conclusion|sonuç
n|figure|şekil; rakam
n|introduction|giriş
n|issue|mesele
n|level|düzey
n|period|dönem
n|reference|kaynak, atıf
n|summary|özet
n|table|tablo
n|topic|konu
v|affect|etkilemek
v|discuss|tartışmak
v|explain|açıklamak
v|include|içermek
v|measure|ölçmek
v|provide|sağlamak
v|suggest|önermek; ileri sürmek
v|support|desteklemek
a|common|yaygın
a|current|mevcut, güncel
a|previous|önceki
d|however|ancak
d|therefore|bu nedenle
d|in conclusion|sonuç olarak
d|such as|gibi
v|state|belirtmek, ifade etmek
v|question|sorgulamak
n|series|seri
v|report|raporlamak, bildirmek
v|list|sıralamak
v|project|öngörmek, yansıtmak
v|record|kaydetmek
v|test|sınamak
n|result|sonuç
v|model|modellemek
v|review|gözden geçirmek, derlemek
n|range|aralık, erim
n|stage|aşama
v|note|kaydetmek, belirtmek
n|conference|konferans
n|population|evren, popülasyon
n|focus|odak
n|section|bölüm
d|particularly|özellikle
n|application|uygulama, başvuru
n|condition|koşul
n|scale|ölçek
a|critical|eleştirel, kritik
n|authority|otorite, yetkili kaynak
n|foundation|temel
n|function|işlev
v|prove|kanıtlamak
n|journal|akademik dergi
n|volume|cilt, hacim
v|reduce|indirgemek, azaltmak
n|alternative|seçenek
d|relatively|görece
a|numerous|çok sayıda
d|specifically|özellikle, spesifik olarak
n|phase|evre
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
n|aspect|yön, boyut
n|benefit|fayda
n|category|kategori
n|component|bileşen
n|feature|özellik
n|impact|etki
n|interview|görüşme
n|percentage|yüzde
n|questionnaire|anket formu
n|response|yanıt
n|role|rol
v|achieve|ulaşmak
v|analyse|analiz etmek
v|apply|uygulamak
v|compare|karşılaştırmak
v|conclude|sonuca varmak
v|contrast|karşıtlık kurmak
v|examine|incelemek
v|predict|tahmin etmek
v|refer to|atıfta bulunmak
v|select|seçmek
a|accurate|doğru, kesin
a|available|mevcut
a|major|büyük, önemli
d|moreover|üstelik
d|similarly|benzer şekilde
d|overall|genel olarak
d|on the other hand|öte yandan
d|typically|tipik olarak
v|draft|taslak hazırlamak
n|statistics|istatistik
n|instance|örnek, durum
n|definition|tanım
a|random|rastgele
n|index|dizin, endeks
a|representative|temsil edici
d|significantly|anlamlı biçimde
n|portion|kısım, pay
v|pilot|pilot uygulama yapmak
v|quote|alıntı yapmak
n|comparison|karşılaştırma
v|document|belgelemek
n|convention|teamül, uzlaşım
a|equivalent|eşdeğer
a|contemporary|çağdaş
d|initially|başlangıçta
n|technique|teknik
n|assessment|değerlendirme
n|element|öge
n|formula|formül
n|publication|yayın
v|rank|sıralamak, derecelendirmek
n|explanation|açıklama
n|procedure|prosedür, işlem
v|label|etiketlemek
n|output|çıktı
d|essentially|esasen
n|institution|kurum
n|experiment|deney
v|introduce|tanıtmak, sunmak
n|ratio|oran
d|merely|sadece
n|frequency|sıklık
n|exception|istisna
n|input|girdi
n|data set|veri kümesi
v|depend on|-e bağlı olmak
v|map (out)|haritalamak, planlamak
v|relate to|ilişkilendirmek
v|pertain to|-ile ilgili olmak
n|case study|vaka çalışması
v|restrict to|-ile sınırlamak
n|sample size|örneklem büyüklüğü
p|in terms of|-açısından
p|by contrast|buna karşılık
v|identify with|özdeşleştirmek
n|knowledge gap|bilgi boşluğu
n|response rate|yanıt oranı
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
n|argument|argüman
n|claim|iddia
n|consequence|sonuç
n|dimension|boyut
n|emphasis|vurgu
n|evaluation|değerlendirme
n|indicator|gösterge
n|objective|hedef
n|proportion|oran
n|strategy|strateji
n|theory|kuram
v|acknowledge|kabul etmek
v|adopt|benimsemek
v|anticipate|öngörmek
v|assume|varsaymak
v|categorise|sınıflandırmak
v|challenge|sorgulamak
v|determine|belirlemek
v|enhance|geliştirmek
v|highlight|vurgulamak
v|maintain|sürdürmek; savunmak
a|adequate|yeterli
a|considerable|kayda değer
a|explicit|açık, belirgin
a|potential|olası
d|accordingly|buna uygun olarak
d|primarily|öncelikle
d|to some extent|bir ölçüde
d|with regard to|ile ilgili olarak
n|sequence|dizi, sıra
n|contribution|katkı
n|principle|ilke
n|composition|bileşim, kompozisyon
a|uniform|tekdüze, aynı
n|feedback|geri bildirim
a|sufficient|yeterli
n|domain|alan, saha
a|dynamic|değişken, dinamik
a|collective|toplu, ortak
n|estimate|tahmin
n|interaction|etkileşim
a|distinct|belirgin, ayrı
a|parallel|koşut
n|instrument|araç (ölçüm)
n|intervention|müdahale
n|requirement|gereklilik
n|inquiry|araştırma, soruşturma
n|discipline|bilim dalı
a|dominant|baskın
d|briefly|kısaca
d|precisely|tam olarak
d|solely|yalnızca
v|trace|izini sürmek
n|ethics|etik
n|scenario|senaryo
a|respective|ilgili, sırasıyla
d|partially|kısmen
v|resolve|çözümlemek
n|notion|kavram, fikir
a|partial|kısmi
a|underlying|altta yatan
n|observation|gözlem
a|applicable|uygulanabilir
a|linear|doğrusal
p|control group|kontrol grubu
v|compensate for|telafi etmek
p|taken together|bir bütün olarak ele alındığında
n|margin of error|hata payı
n|research design|araştırma tasarımı
p|with respect to|-e ilişkin olarak
p|on the basis of|-e dayanarak
p|it follows that|buradan şu çıkar ki
n|qualitative data|nitel veri
p|in the same vein|aynı doğrultuda
p|conceptual model|kavramsal model
p|ethical approval|etik kurul onayı
p|informed consent|bilgilendirilmiş onam
n|literature review|literatür taraması
n|quantitative data|nicel veri
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
n|abstract|özet (makale)
n|appendix|ek
n|citation|alıntı, atıf
n|coherence|tutarlılık
n|equation|denklem
n|interpretation|yorum
n|mechanism|mekanizma
n|outlier|aykırı değer
n|peer review|hakem değerlendirmesi
n|significance|anlamlılık
n|supervisor|tez danışmanı
v|allocate|tahsis etmek
v|compile|derlemek
v|conduct|yürütmek
v|confirm|doğrulamak
v|differentiate|ayırt etmek
v|exclude|dışlamak
v|implement|uygulamak
v|infer|çıkarsamak
v|modify|değiştirmek
v|validate|doğrulamak
a|accessible|erişilebilir
a|statistical|istatistiksel
a|valid|geçerli
a|theoretical|kuramsal
d|approximately|yaklaşık
d|subsequently|ardından
d|correspondingly|buna karşılık olarak
v|convert|dönüştürmek
a|generic|genel, jenerik
v|publish|yayımlamak
n|array|dizi, yelpaze
n|dynamics|dinamikler
a|comparable|karşılaştırılabilir
v|observe|gözlemlemek
v|detect|saptamak, tespit etmek
n|graph|grafik
n|median|ortanca
n|thesis|tez, sav
a|likewise|benzer şekilde
n|threshold|eşik
v|accommodate|barındırmak, uyum sağlatmak
v|extract|çıkarmak, ayıklamak
n|axis|eksen
d|namely|yani, şöyle ki
n|adaptation|uyarlama
v|probe|derinlemesine araştırmak
v|propose|önermek
v|weigh|tartmak, değerlendirmek
n|configuration|yapılandırma
n|tendency|eğilim
a|integral|ayrılmaz, bütünleyici
d|explicitly|açıkça
v|aggregate|toplamak, bir araya getirmek
v|locate|konumlandırmak, bulmak
a|optimal|en uygun
v|translate|çevirmek
n|norm|norm
n|illustration|görsel örnek
n|manuscript|müsvedde, makale metni
v|emerge|ortaya çıkmak
n|module|modül
v|verify|doğrulamak
n|credibility|güvenilirlik
a|peer-reviewed|hakemli
v|calculate|hesaplamak
v|regulate|düzenlemek
a|systematic|sistematik
p|research question|araştırma sorusu
n|body of literature|literatür bütünü
n|empirical evidence|ampirik kanıt
n|significance level|anlamlılık düzeyi
n|standard deviation|standart sapma
p|in accordance with|-e uygun olarak
p|as shown in Table 2|Tablo 2'de görüldüğü üzere
p|the extent to which|-in ne ölçüde olduğu
p|the null hypothesis|sıfır hipotezi
p|in the present study|bu çalışmada
p|we hypothesised that|şu hipotezi kurduk
p|confounding variable|karıştırıcı değişken
p|theoretical framework|kuramsal çerçeve
p|this paper argues that|bu çalışma şunu savunmaktadır
p|the data indicate that|veriler şunu göstermektedir
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
n|anomaly|anomali
n|assertion|iddia
n|causality|nedensellik
n|constraint|kısıt
n|contention|savunulan görüş
n|generalisability|genellenebilirlik
n|implementation|uygulama
n|parameter|parametre
n|proposition|önerme
n|rigour|titizlik
n|taxonomy|sınıflandırma
v|advocate|savunmak
v|ascertain|tespit etmek
v|attain|ulaşmak
v|calibrate|kalibre etmek
v|compensate|telafi etmek
v|deduce|tümdengelimle çıkarmak
v|discern|ayırt etmek
v|encompass|kapsamak
v|exemplify|örneklemek
v|formulate|formüle etmek
a|coherent|tutarlı
a|intrinsic|içsel
a|marginal|marjinal
a|plausible|akla yatkın
d|thereby|böylece
d|whereby|ki bununla
d|nonetheless|yine de
n|diagram|şema
a|arbitrary|keyfi
n|synthesis|sentez
v|critique|eleştirel değerlendirme yapmak
n|justification|gerekçelendirme
n|prototype|prototip
a|diagnostic|tanısal
n|bibliography|kaynakça
d|broadly|genel hatlarıyla
d|alternatively|alternatif olarak
a|subjective|öznel
n|hierarchy|hiyerarşi
n|interval|aralık
v|merge|birleştirmek
a|finite|sonlu
n|allocation|tahsis
a|preceding|önceki
a|analytical|çözümleyici
v|perceive|algılamak
n|specimen|numune
n|analogy|benzeşim
n|dissertation|tez (doktora)
v|manifest|açığa vurmak, tezahür etmek
n|terminology|terminoloji
v|cite|alıntılamak, kaynak göstermek
v|transmit|iletmek
d|statistically|istatistiksel olarak
v|approximate|yaklaşık olarak hesaplamak
d|theoretically|kuramsal olarak
v|inspect|denetlemek, incelemek
v|reconsider|yeniden değerlendirmek
v|reproduce|yeniden üretmek
n|practitioner|uygulayıcı
v|assert|savunmak, öne sürmek
v|presume|varsaymak
a|conceptual|kavramsal
a|hypothetical|varsayımsal
p|drawing on the work of|-in çalışmasından yararlanarak
p|prior research suggests|önceki araştırmalar şunu göstermektedir
p|it should be noted that|belirtmek gerekir ki
p|this is consistent with|bu, -ile uyumludur
p|the scope of this paper|bu makalenin kapsamı
p|contrary to expectations|beklentilerin aksine
p|insofar as the data allow|verilerin izin verdiği ölçüde
p|statistically significant|istatistiksel olarak anlamlı
p|it is widely accepted that|genel kabul görmektedir ki
p|further research is needed|daha fazla araştırmaya ihtiyaç var
p|as illustrated in Figure 1|Şekil 1'de gösterildiği gibi
p|in light of these findings|bu bulgular ışığında
p|future work should address|ilerideki çalışmalar -i ele almalıdır
p|the aim of this study is to|bu çalışmanın amacı
p|these findings suggest that|bu bulgular şunu düşündürmektedir
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
n|antecedent|öncül
n|conjecture|varsayım
n|corpus|derlem
n|counterargument|karşı argüman
n|exposition|açıklama
n|paradox|paradoks
n|precedent|emsal
n|proxy|vekil gösterge
n|repercussion|yankı, sonuç
v|adhere to|bağlı kalmak
v|allude to|ima etmek
v|articulate|açıkça ifade etmek
v|consolidate|pekiştirmek
v|contend|iddia etmek
v|culminate|doruğa ulaşmak
v|disseminate|yaymak
v|juxtapose|yan yana koymak
v|presuppose|önceden varsaymak
v|stipulate|şart koşmak
a|contingent|koşullu, bağlı
a|discrete|ayrık
a|implicit|örtük
a|seminal|çığır açan
a|unprecedented|eşi görülmemiş
d|insofar as|-dığı ölçüde
d|notwithstanding|-e rağmen
d|in this regard|bu bağlamda
d|by extension|buna bağlı olarak
v|isolate|yalıtmak, ayrıştırmak
n|equilibrium|denge
v|commence|başlamak
d|inherently|doğası gereği
v|adhere|bağlı kalmak, uymak
a|indicative|gösterge niteliğinde
a|complementary|tamamlayıcı
v|fragment|parçalamak
v|replicate|yinelemek (deneyi), kopyalamak
a|cumulative|birikimli
a|descriptive|betimleyici
v|conform|uygun olmak, uymak
n|dependency|bağımlılık
n|excerpt|alıntı parçası
d|comparatively|görece olarak
v|organise|düzenlemek
v|provoke|kışkırtmak, tetiklemek
a|correlated|ilişkili, bağıntılı
v|coincide|çakışmak, aynı anda olmak
a|concurrent|eşzamanlı
v|speculate|spekülasyon yapmak
n|deduction|tümdengelim
n|variance|varyans
v|simulate|benzetim yapmak
n|continuum|süreklilik
n|replication|yineleme çalışması
a|inverse|ters
v|compute|hesaplamak
n|cohort|kohort, grup
n|deviation|sapma
v|classify|sınıflandırmak
n|coefficient|katsayı
a|interdisciplinary|disiplinlerarası
v|designate|belirlemek, atamak
v|originate|kaynaklanmak, doğmak
a|longitudinal|boylamsal (uzun süreli)
a|predictive|öngörücü
a|unilateral|tek taraflı
a|causal|nedensel
n|acknowledgement|teşekkür bölümü, kabul
p|this raises the question of|bu, şu soruyu doğurmaktadır
p|a substantial proportion of|-in hatırı sayılır bir kısmı
p|the present findings extend|mevcut bulgular -i genişletmektedir
p|to the best of our knowledge|bildiğimiz kadarıyla
p|the underlying assumption is|altta yatan varsayım şudur
p|a possible explanation is that|olası bir açıklama şudur ki
p|beyond the scope of this study|bu çalışmanın kapsamı dışında
p|for the purposes of this study|bu çalışmanın amaçları doğrultusunda
p|a number of studies have shown|bir dizi çalışma göstermiştir ki
p|one limitation of this study is|bu çalışmanın bir sınırlılığı
p|the results are consistent with|sonuçlar -ile tutarlıdır
p|in contrast to previous findings|önceki bulguların aksine
p|little attention has been paid to|-e çok az dikkat gösterilmiştir
p|there is a growing body of evidence|giderek artan bir kanıt bütünü var
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
n|aporia|(felsefi) çıkmaz
n|dialectic|diyalektik
n|exegesis|yorum, tefsir
n|historiography|tarih yazımı
n|ideology|ideoloji
n|positivism|pozitivizm
n|relativism|görecilik
n|subjectivity|öznellik
n|syllogism|kıyas
v|adjudicate|hüküm vermek
v|circumscribe|sınırlamak
v|deconstruct|yapıbozuma uğratmak
v|epitomise|simgelemek
v|explicate|açıklamak
v|marginalise|ötekileştirmek
v|privilege|ayrıcalık tanımak
v|theorise|kuramlaştırmak
a|canonical|kanonik
a|dialectical|diyalektik
a|normative|normatif
a|paradigmatic|paradigmatik
a|post hoc|sonradan
d|in toto|bütünüyle
d|sensu stricto|dar anlamda
d|vis-à-vis|-e karşı, ile ilgili olarak
n|approximation|yaklaşıklık
v|illuminate|aydınlatmak (konuyu)
a|conclusive|kesin
a|exhaustive|tüketici, eksiksiz
a|sequential|ardışık
d|markedly|belirgin biçimde
v|evoke|çağrıştırmak, uyandırmak
a|hierarchical|hiyerarşik
n|guideline|yönerge
n|subsection|alt bölüm
v|denounce|kınamak
v|converge|yakınsamak, birleşmek
n|plagiarism|intihal
d|implicitly|dolaylı olarak
v|correlate|ilişkilendirmek, bağıntı kurmak
v|equate|eşitlemek, denk saymak
v|augment|artırmak, takviye etmek
v|allege|iddia etmek (kanıtsız)
a|exploratory|keşfedici
v|embody|somutlaştırmak, cisimleştirmek
n|footnote|dipnot
v|amplify|güçlendirmek, büyütmek
n|proponent|savunucu
a|hitherto|şimdiye kadar
v|impede|engellemek
a|contextual|bağlamsal
v|mediate|aracılık etmek
v|reiterate|yinelemek
n|schema|şema, çerçeve
a|inconclusive|sonuçsuz, belirsiz
n|predictor|yordayıcı değişken
v|elicit|ortaya çıkarmak, elde etmek (yanıt)
n|causation|nedensellik
n|respondent|katılımcı, yanıtlayan
v|automate|otomatikleştirmek
v|distort|çarpıtmak
v|omit|çıkarmak, atlamak
v|paraphrase|başka sözcüklerle ifade etmek
v|unify|birleştirmek
v|deviate|sapmak
v|solicit|talep etmek, istemek
n|derivation|türetme
a|methodological|yöntemsel
v|invalidate|geçersiz kılmak
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
n|alterity|ötekilik
n|episteme|bilgi düzeni
n|habitus|habitus
n|intertextuality|metinlerarasılık
n|liminality|eşiksellik
n|performativity|performatiflik
n|positionality|konumsallık
n|reflexivity|düşünümsellik
v|abrogate|yürürlükten kaldırmak
v|countenance|hoş görmek
v|essentialise|özcüleştirmek
v|occlude|örtmek, gizlemek
v|reify|şeyleştirmek
v|subsume|kapsamına almak
v|transmute|dönüştürmek
a|aporetic|çıkmaza dair
a|apodictic|kesin
a|hegemonic|hegemonik
a|liminal|eşiksel
a|recursive|özyinelemeli
a|syncretic|bağdaştırmacı
d|pace|(-e) saygıyla katılmayarak
d|sic|aynen böyle (alıntıda)
d|viz.|yani, şöyle ki
v|underscore|altını çizmek, vurgulamak
v|disprove|çürütmek
v|confine|sınırlamak, kısıtlamak
v|fabricate|uydurmak, imal etmek
n|annotation|dipnot, açıklama
d|empirically|ampirik olarak
v|nullify|hükümsüz kılmak
v|substantiate|kanıtlarla desteklemek
v|narrate|anlatmak
v|posit|varsaymak, öne sürmek
v|ascribe|atfetmek
v|authenticate|gerçekliğini doğrulamak
v|transcribe|deşifre etmek, yazıya dökmek
v|supersede|yerini almak, geçersiz kılmak
v|recur|yinelemek, tekrar etmek
v|append|eklemek (sona)
v|characterise|nitelendirmek
v|purport|iddia etmek, öyle görünmek
v|optimise|en iyi duruma getirmek
v|expound|ayrıntılı açıklamak
v|restate|yeniden ifade etmek
n|generalisation|genelleme
v|collate|karşılaştırıp derlemek
v|situate|konumlandırmak
v|enumerate|tek tek saymak
v|rationalise|akla uydurmak, gerekçelendirmek
v|construe|yorumlamak, anlam vermek
v|normalise|normalleştirmek
v|annotate|notlandırmak, açıklama düşmek
v|generalise|genellemek
v|tabulate|tablolaştırmak
v|recapitulate|özetleyerek tekrarlamak
v|conceptualise|kavramsallaştırmak
v|interrelate|karşılıklı ilişkilendirmek
v|hypothesise|hipotez kurmak
v|randomise|rastgeleleştirmek
""",
}

CYBER = {
"B1.1": """
n|asset|varlık (korunacak değer)
n|threat|tehdit
n|threat actor|tehdit aktörü
n|vulnerability|zafiyet, açık
n|exploit|istismar kodu / istismar etmek
n|risk|risk
n|likelihood|olasılık
n|impact|etki, sonuç
n|attack surface|saldırı yüzeyi
n|attack vector|saldırı vektörü
n|blast radius|etki alanı, yayılma çapı
n|confidentiality|gizlilik
n|integrity|bütünlük
n|availability|erişilebilirlik
n|non-repudiation|inkâr edilemezlik
n|authentication|kimlik doğrulama
n|authorisation|yetkilendirme
n|accounting|kayıt tutma, hesap verme
n|least privilege|en az yetki ilkesi
n|defence in depth|katmanlı savunma
n|zero trust|sıfır güven
n|security posture|güvenlik duruşu
n|baseline|temel referans yapılandırma
n|hardening|sıkılaştırma
n|patch|yama
n|patch management|yama yönetimi
n|countermeasure|karşı önlem
n|safeguard|koruyucu tedbir
n|control|kontrol, denetim mekanizması
n|compensating control|telafi edici kontrol
n|mitigation|azaltma, hafifletme
n|remediation|giderme, düzeltme
n|residual risk|artık risk
n|false positive|yanlış pozitif
n|false negative|yanlış negatif
n|true positive|doğru pozitif
n|detection|tespit
n|prevention|önleme
n|response|müdahale
n|recovery|kurtarma
n|resilience|dayanıklılık
n|redundancy|yedeklilik
n|failover|yedeğe geçiş
n|business continuity|iş sürekliliği
n|disaster recovery|felaket kurtarma
n|single point of failure|tek hata noktası
n|security by design|tasarımdan gelen güvenlik
n|fail secure|hata durumunda güvenli kalma
n|trust boundary|güven sınırı
n|threat landscape|tehdit ortamı
p|assess the risk|riski değerlendirmek
p|mitigate the risk|riski azaltmak
p|escalate the incident|olayı üst seviyeye taşımak
p|contain the threat|tehdidi kontrol altına almak
p|remediate the finding|bulguyu gidermek
p|harden the system|sistemi sıkılaştırmak
p|patch the vulnerability|zafiyeti yamalamak
p|enforce the policy|politikayı uygulatmak
p|validate the fix|düzeltmeyi doğrulamak
p|reproduce the issue|sorunu yeniden oluşturmak
p|document the steps|adımları belgelemek
p|raise a ticket|kayıt/talep açmak
p|flag a concern|bir endişeyi işaretlemek
p|walk through the report|raporu adım adım anlatmak
p|follow up on|takibini yapmak
p|loop in the team|ekibi sürece dâhil etmek
p|align with stakeholders|paydaşlarla mutabık kalmak
p|prioritise findings|bulguları önceliklendirmek
p|scope the engagement|projenin kapsamını belirlemek
p|sign off on|onay vermek
""",
"B1.2": """
p|roll out|yaygınlaştırmak, devreye almak
p|roll back|geri almak (değişikliği)
d|decommission|hizmetten çıkarmak
p|whitelist an IP|bir IP'yi izin listesine eklemek
p|revoke access|erişimi iptal etmek
p|grant access|erişim vermek
p|rotate credentials|kimlik bilgilerini yenilemek
p|enable logging|günlük kaydını açmak
p|monitor for anomalies|anormallikleri izlemek
p|correlate events|olayları ilişkilendirmek
p|verify the alert|uyarıyı doğrulamak
p|dismiss as false positive|yanlış pozitif olarak kapatmak
p|conduct a review|inceleme yürütmek
p|present the findings|bulguları sunmak
p|justify the budget|bütçeyi gerekçelendirmek
p|as per our policy|politikamız gereği
p|in line with best practice|iyi uygulamalarla uyumlu olarak
p|subject to approval|onaya tabi olarak
p|pending further investigation|inceleme sürerken, sonuç beklenirken
p|with immediate effect|derhal geçerli olmak üzere
n|packet|paket
n|payload|yük, veri kısmı
n|header|başlık
n|frame|çerçeve
n|protocol|protokol
n|port|port
n|socket|soket
n|handshake|el sıkışma
n|three-way handshake|üçlü el sıkışma
n|subnet|alt ağ
n|gateway|ağ geçidi
n|router|yönlendirici
n|switch|anahtar
n|firewall|güvenlik duvarı
n|next-generation firewall|yeni nesil güvenlik duvarı
n|stateful inspection|durum bilgili denetim
n|access control list (ACL)|erişim kontrol listesi
n|NAT|ağ adresi çevirisi
n|VLAN|sanal yerel ağ
n|network segmentation|ağ segmentasyonu
n|micro-segmentation|mikro segmentasyon
n|DMZ|silahtan arındırılmış bölge
n|proxy|vekil sunucu
n|reverse proxy|ters vekil sunucu
n|load balancer|yük dengeleyici
n|VPN|sanal özel ağ
n|tunnelling|tünelleme
n|port forwarding|port yönlendirme
n|pivoting|başka ağa sıçrama
n|packet capture|paket yakalama
n|sniffing|trafik dinleme
n|traffic analysis|trafik analizi
n|bandwidth|bant genişliği
n|latency|gecikme
n|throughput|iş hacmi, veri geçiş oranı
n|broadcast|yayın (tüm ağa)
n|routing table|yönlendirme tablosu
n|DNS resolution|DNS çözümleme
n|DHCP lease|DHCP kirası
n|TLS|taşıma katmanı güvenliği
n|mutual TLS|karşılıklı TLS
n|certificate pinning|sertifika sabitleme
n|wireless access point|kablosuz erişim noktası
n|rogue access point|sahte erişim noktası
n|evil twin|ikiz sahte ağ
n|deauthentication attack|bağlantı kesme saldırısı
n|WPA2 / WPA3|kablosuz güvenlik standardı
n|egress filtering|çıkış trafiği filtreleme
n|ingress filtering|giriş trafiği filtreleme
n|network tap|ağ dinleme noktası
""",
"B2.1": """
n|kernel|çekirdek
n|process|süreç, işlem
n|daemon|arka plan servisi
n|service|servis
n|shell|kabuk
n|privilege|yetki
n|root|en yetkili kullanıcı
n|sudo|yetkili komut çalıştırma
n|file permission|dosya izni
n|setuid binary|setuid çalıştırılabilir
n|cron job|zamanlanmış görev
n|systemd unit|systemd servis birimi
n|log file|günlük dosyası
n|syslog|sistem günlük protokolü
n|audit trail|denetim izi
n|registry|kayıt defteri (Windows)
n|Active Directory|Active Directory dizin hizmeti
n|domain controller|etki alanı denetleyicisi
n|group policy|grup ilkesi
n|service account|servis hesabı
n|golden ticket|sahte Kerberos bileti (altın bilet)
n|hash|özet değeri
n|pass-the-hash|hash ile kimlik doğrulama saldırısı
n|LSASS dump|LSASS bellek dökümü
n|memory dump|bellek dökümü
n|snapshot|anlık görüntü
n|virtual machine|sanal makine
n|hypervisor|hipervizör
n|container|konteyner
n|image|imaj
n|sandbox|yalıtılmış test ortamı
n|escape (sandbox/container)|yalıtımdan kaçış
n|endpoint|uç nokta
n|agent|ajan yazılımı
n|inventory|envanter
n|asset management|varlık yönetimi
n|configuration drift|yapılandırma sapması
n|golden image|standart kurulum imajı
n|malware|zararlı yazılım
n|ransomware|fidye yazılımı
n|spyware|casus yazılım
n|adware|reklam yazılımı
n|rootkit|rootkit, kök seti
n|bootkit|önyükleme zararlısı
n|trojan|truva atı
n|worm|solucan
n|virus|virüs
n|dropper|yükleyici zararlı
n|loader|yükleyici bileşen
n|wiper|veri silici zararlı
n|keylogger|tuş kaydedici
n|botnet|bot ağı
n|command and control (C2)|komuta kontrol sunucusu
n|beacon|periyodik geri bağlantı sinyali
n|backdoor|arka kapı
n|logic bomb|mantık bombası
n|phishing|oltalama
n|spear phishing|hedefli oltalama
n|whaling|üst yönetime yönelik oltalama
n|smishing|SMS ile oltalama
n|vishing|telefonla oltalama
n|pretexting|bahane uydurma (sosyal mühendislik)
n|baiting|yem atma
n|tailgating|yetkisiz peşinden girme
n|social engineering|sosyal mühendislik
n|business email compromise|kurumsal e-posta dolandırıcılığı
n|credential theft|kimlik bilgisi hırsızlığı
n|credential stuffing|çalıntı kimlik denemesi
n|password spraying|yaygın parola denemesi
n|brute force|kaba kuvvet saldırısı
n|dictionary attack|sözlük saldırısı
n|rainbow table|gökkuşağı tablosu
""",
"B2.2": """
n|man-in-the-middle (MitM)|araya girme saldırısı
n|replay attack|tekrar saldırısı
n|session hijacking|oturum ele geçirme
n|spoofing|kimlik/adres sahteciliği
n|ARP poisoning|ARP zehirlemesi
n|DNS poisoning|DNS zehirlemesi
n|DNS tunnelling|DNS üzerinden tünelleme
n|typosquatting|yazım hatası alan adı kapma
n|watering hole attack|su kaynağı saldırısı
n|supply chain attack|tedarik zinciri saldırısı
n|denial of service (DoS)|hizmet dışı bırakma
n|DDoS|dağıtık hizmet dışı bırakma
n|amplification attack|yükseltme saldırısı
n|zero-day|sıfırıncı gün açığı
n|privilege escalation|yetki yükseltme
n|lateral movement|yatay hareket
n|persistence|kalıcılık sağlama
n|data exfiltration|veri sızdırma
n|data breach|veri ihlali
n|insider threat|iç tehdit
n|advanced persistent threat (APT)|gelişmiş kalıcı tehdit
n|living off the land|sistemin kendi araçlarını kullanma
n|fileless malware|dosyasız zararlı
n|obfuscation|gizleme, karmaşıklaştırma
n|packing|paketleme (zararlıyı gizleme)
a|polymorphic|çok biçimli (zararlı)
n|evasion|atlatma, kaçınma
n|anti-forensics|adli analizi engelleme
n|cryptojacking|izinsiz kripto madenciliği
n|scareware|korkutma yazılımı
n|double extortion|çifte şantaj
n|initial access|ilk erişim
n|dwell time|saldırganın sistemde kalış süresi
n|kill chain|saldırı zinciri
n|injection|enjeksiyon
n|SQL injection|SQL enjeksiyonu
n|command injection|komut enjeksiyonu
n|cross-site scripting (XSS)|siteler arası betik çalıştırma
n|stored XSS|kalıcı XSS
n|reflected XSS|yansıyan XSS
n|cross-site request forgery (CSRF)|siteler arası istek sahteciliği
n|server-side request forgery (SSRF)|sunucu taraflı istek sahteciliği
n|insecure deserialisation|güvensiz seri hâlden çıkarma
n|path traversal|dizin geçişi
n|local file inclusion|yerel dosya dahil etme
n|remote code execution (RCE)|uzaktan kod çalıştırma
n|open redirect|açık yönlendirme
n|clickjacking|tıklama hırsızlığı
n|broken access control|bozuk erişim kontrolü
n|insecure direct object reference (IDOR)|güvensiz doğrudan nesne referansı
n|business logic flaw|iş mantığı açığı
n|race condition|yarış durumu
n|buffer overflow|arabellek taşması
n|heap overflow|yığın taşması
n|stack overflow|yığıt taşması
n|use-after-free|serbest bırakılan belleği kullanma
n|input validation|girdi doğrulama
n|output encoding|çıktı kodlama
""",
"C1.1": """
n|sanitisation|temizleme, arındırma
n|parameterised query|parametreli sorgu
n|prepared statement|hazırlanmış ifade
n|content security policy (CSP)|içerik güvenlik politikası
n|same-origin policy|aynı köken politikası
n|CORS|kökenler arası kaynak paylaşımı
n|security header|güvenlik başlığı
n|rate limiting|istek sınırlama
n|web application firewall (WAF)|web uygulama güvenlik duvarı
n|API gateway|API ağ geçidi
n|token|jeton
n|session cookie|oturum çerezi
n|secure flag|güvenli çerez bayrağı
n|HttpOnly|betikten erişilemez çerez
n|CAPTCHA|bot doğrulama testi
n|dependency|bağımlılık
n|software bill of materials (SBOM)|yazılım bileşen listesi
n|secure coding|güvenli kod yazımı
n|code review|kod incelemesi
n|static analysis (SAST)|statik kod analizi
n|dynamic analysis (DAST)|dinamik uygulama testi
n|fuzzing|rastgele girdi testi
n|secrets management|gizli bilgi yönetimi
n|hardcoded credentials|koda gömülü kimlik bilgisi
n|encryption|şifreleme
n|decryption|şifre çözme
n|plaintext|düz metin
n|ciphertext|şifreli metin
n|cipher|şifre algoritması
n|symmetric encryption|simetrik şifreleme
n|asymmetric encryption|asimetrik şifreleme
n|public key|açık anahtar
n|private key|özel anahtar
n|key exchange|anahtar değişimi
n|key rotation|anahtar döndürme
n|key management|anahtar yönetimi
n|hashing|özetleme
n|salt|tuz (hash'e eklenen rastgele değer)
n|pepper|gizli ek değer
n|digital signature|dijital imza
n|certificate|sertifika
n|certificate authority (CA)|sertifika otoritesi
n|public key infrastructure (PKI)|açık anahtar altyapısı
n|self-signed certificate|kendinden imzalı sertifika
n|revocation|iptal (sertifika)
n|entropy|entropi, rastgelelik
n|nonce|tek kullanımlık değer
n|initialisation vector|başlatma vektörü
n|end-to-end encryption|uçtan uca şifreleme
n|encryption at rest|durağan veri şifreleme
n|encryption in transit|aktarımda şifreleme
n|hardware security module (HSM)|donanım güvenlik modülü
n|identity provider (IdP)|kimlik sağlayıcı
n|single sign-on (SSO)|tek oturum açma
n|federation|kimlik federasyonu
n|SAML|SAML kimlik doğrulama standardı
n|OAuth|OAuth yetkilendirme protokolü
n|OpenID Connect|OIDC kimlik katmanı
n|multi-factor authentication (MFA)|çok faktörlü kimlik doğrulama
n|one-time password (OTP)|tek kullanımlık parola
n|passkey|geçiş anahtarı, şifresiz kimlik
a|biometric|biyometrik
n|role-based access control (RBAC)|rol tabanlı erişim kontrolü
n|attribute-based access control|nitelik tabanlı erişim kontrolü
n|privileged access management (PAM)|ayrıcalıklı erişim yönetimi
n|just-in-time access|anlık/geçici yetki verme
n|identity lifecycle|kimlik yaşam döngüsü
n|provisioning|hesap oluşturma/atama
n|deprovisioning|hesap kapatma
n|access review|erişim gözden geçirmesi
n|segregation of duties|görevler ayrılığı
""",
"C1.2": """
n|penetration test|sızma testi
n|red team|kırmızı takım
n|blue team|mavi takım
n|purple team|mor takım
n|engagement|proje, görev süreci
n|rules of engagement|görev kuralları
n|scope|kapsam
n|in scope / out of scope|kapsam içi / kapsam dışı
n|authorisation letter|yetki mektubu
n|get-out-of-jail letter|yasal muafiyet yazısı
n|black box|kara kutu testi
n|white box|beyaz kutu testi
n|grey box|gri kutu testi
n|reconnaissance|keşif
n|OSINT|açık kaynak istihbaratı
n|footprinting|iz sürme, hedef haritalama
n|enumeration|numaralandırma, listeleme
n|scanning|tarama
n|port scan|port taraması
n|service detection|servis tespiti
n|banner grabbing|servis afişi toplama
n|vulnerability scanning|zafiyet taraması
n|proof of concept (PoC)|kavram kanıtı
n|payload delivery|zararlı yük iletimi
n|shellcode|kabuk kodu
n|reverse shell|ters kabuk bağlantısı
n|bind shell|dinleyen kabuk
n|foothold|ilk tutunma noktası
n|pivot|sıçrama noktası olarak kullanmak
n|post-exploitation|istismar sonrası aşama
n|credential harvesting|kimlik bilgisi toplama
n|password cracking|parola kırma
n|privilege enumeration|yetki listeleme
n|persistence mechanism|kalıcılık yöntemi
n|cleanup|iz temizleme, ortamı eski hâline getirme
n|debrief|değerlendirme toplantısı
n|finding|bulgu
n|severity|önem derecesi
n|CVSS score|CVSS puanı
n|exploitability|istismar edilebilirlik
n|remediation advice|düzeltme önerisi
n|retest|yeniden test
n|executive summary|yönetici özeti
n|technical report|teknik rapor
n|bug bounty|hata ödül programı
n|responsible disclosure|sorumlu açıklama
n|coordinated disclosure|eşgüdümlü açıklama
n|adversary emulation|saldırgan taklidi
n|TTPs|taktikler, teknikler ve prosedürler
n|MITRE ATT&CK|ATT&CK saldırı tekniği çerçevesi
n|threat model|tehdit modeli
n|attack tree|saldırı ağacı
""",
"C2.1": """
n|security operations centre (SOC)|güvenlik operasyon merkezi
n|analyst|analist
n|tier 1 / tier 2|birinci / ikinci seviye destek
n|alert|uyarı
n|alert fatigue|uyarı yorgunluğu
n|triage|önceliklendirme, ilk eleme
n|escalation|üst seviyeye taşıma
n|incident|olay
n|incident response|olay müdahalesi
n|playbook|müdahale kılavuzu
n|runbook|işletim adımları kılavuzu
n|on-call|nöbetçi olma
n|containment|sınırlandırma, kontrol altına alma
n|eradication|tehdidi tamamen temizleme
n|lessons learned|çıkarılan dersler
n|post-mortem|olay sonrası inceleme
n|root cause analysis|kök neden analizi
n|SIEM|güvenlik bilgi ve olay yönetimi
n|log aggregation|günlük toplama
n|correlation rule|korelasyon kuralı
n|use case|kullanım senaryosu (tespit kuralı)
n|detection engineering|tespit mühendisliği
n|signature|imza tabanlı tespit
a|heuristic|sezgisel tespit
n|anomaly detection|anomali tespiti
n|behavioural analysis|davranışsal analiz
n|baseline deviation|normalden sapma
n|EDR|uç nokta tespit ve müdahale
n|XDR|genişletilmiş tespit ve müdahale
n|IDS|saldırı tespit sistemi
n|IPS|saldırı önleme sistemi
n|honeypot|bal küpü tuzak sistemi
n|deception technology|aldatma teknolojisi
n|threat intelligence|tehdit istihbaratı
n|indicator of compromise (IoC)|ihlal göstergesi
n|indicator of attack (IoA)|saldırı göstergesi
n|threat hunting|tehdit avcılığı
n|hypothesis-driven hunt|hipotez temelli avlanma
n|digital forensics|dijital adli bilişim
n|chain of custody|delil zinciri
n|imaging|birebir disk kopyası alma
n|write blocker|yazma engelleyici
n|volatile data|uçucu veri
n|timeline analysis|zaman çizelgesi analizi
n|artefact|iz, kalıntı (adli)
n|malware analysis|zararlı yazılım analizi
n|static analysis|statik analiz
n|dynamic analysis|dinamik analiz
n|reverse engineering|tersine mühendislik
n|sandbox detonation|zararlıyı yalıtılmış ortamda çalıştırma
n|YARA rule|YARA tespit kuralı
n|SOAR|güvenlik orkestrasyonu ve otomasyonu
n|mean time to detect (MTTD)|ortalama tespit süresi
n|mean time to respond (MTTR)|ortalama müdahale süresi
n|false alarm|yanlış alarm
n|tuning|kural ince ayarı
n|whitelisting|beyaz listeye alma
n|blocklisting|engelleme listesi
n|quarantine|karantinaya alma
n|isolation|makineyi ağdan yalıtma
n|kill switch|acil durdurma anahtarı
""",
"C2.2": """
n|governance|yönetişim
n|compliance|uyum, mevzuata uygunluk
n|regulation|düzenleme, mevzuat
n|standard|standart
n|framework|çerçeve
n|policy|politika
n|procedure|prosedür
n|guideline|kılavuz ilke
n|audit|denetim
n|auditor|denetçi
n|audit finding|denetim bulgusu
n|evidence|kanıt, delil
n|attestation|beyan, onaylama
n|certification|sertifikasyon
n|accreditation|akreditasyon
n|gap analysis|boşluk analizi
n|maturity model|olgunluk modeli
n|risk assessment|risk değerlendirmesi
n|risk register|risk kaydı
n|risk appetite|risk iştahı
n|risk tolerance|risk toleransı
n|risk acceptance|riski kabul etme
n|risk transfer|riski devretme (sigorta vb.)
n|risk avoidance|riskten kaçınma
n|inherent risk|doğal risk
n|business impact analysis|iş etki analizi
n|recovery time objective (RTO)|kurtarma süresi hedefi
n|recovery point objective (RPO)|kurtarma noktası hedefi
n|data classification|veri sınıflandırma
n|data retention|veri saklama süresi
n|data minimisation|veri minimizasyonu
n|personal data|kişisel veri
n|data subject|veri sahibi
n|data controller|veri sorumlusu
n|data processor|veri işleyen
n|GDPR|Avrupa Genel Veri Koruma Tüzüğü
n|breach notification|ihlal bildirimi
n|privacy by design|tasarımdan gelen mahremiyet
n|third-party risk|üçüncü taraf riski
n|vendor assessment|tedarikçi değerlendirmesi
n|due diligence|gerekli özen incelemesi
n|service level agreement (SLA)|hizmet seviyesi anlaşması
n|NDA|gizlilik sözleşmesi
n|security awareness training|güvenlik farkındalık eğitimi
n|acceptable use policy|kabul edilebilir kullanım politikası
n|change management|değişiklik yönetimi
n|approval workflow|onay akışı
n|exception request|istisna talebi
""",
}

EN_DE = {'family': 'die Familie',
 'friend': 'der Freund / die Freundin',
 'house': 'das Haus',
 'water': 'das Wasser',
 'bread': 'das Brot',
 'day': 'der Tag',
 'week': 'die Woche',
 'city': 'die Stadt',
 'country': 'das Land',
 'name': 'der Name',
 'child': 'das Kind',
 'be': 'sein',
 'have': 'haben',
 'go': 'gehen',
 'come': 'kommen',
 'eat': 'essen',
 'drink': 'trinken',
 'live': 'leben, wohnen',
 'speak': 'sprechen',
 'like': 'mögen, gern haben',
 'big': 'groß',
 'small': 'klein',
 'good': 'gut',
 'happy': 'glücklich, froh',
 'today': 'heute',
 'kitchen': 'die Küche',
 'room': 'das Zimmer',
 'table': 'der Tisch',
 'chair': 'der Stuhl',
 'money': 'das Geld',
 'price': 'der Preis',
 'shop': 'das Geschäft, der Laden',
 'vegetable': 'das Gemüse',
 'breakfast': 'das Frühstück',
 'bus stop': 'die Bushaltestelle',
 'buy': 'kaufen',
 'sleep': 'schlafen',
 'work': 'arbeiten',
 'read': 'lesen',
 'write': 'schreiben',
 'need': 'brauchen',
 'want': 'wollen',
 'open': 'öffnen, aufmachen',
 'close': 'schließen, zumachen',
 'wait': 'warten',
 'cheap': 'billig, günstig',
 'expensive': 'teuer',
 'tired': 'müde',
 'always': 'immer',
 'tomorrow': 'morgen',
 'appointment': 'der Termin',
 'bill': 'die Rechnung',
 'holiday': 'der Urlaub',
 'weather': 'das Wetter',
 'neighbour': 'der Nachbar',
 'key': 'der Schlüssel',
 'rent': 'die Miete',
 'headache': 'die Kopfschmerzen (Pl.)',
 'pharmacy': 'die Apotheke',
 'ticket': 'die Fahrkarte, das Ticket',
 'call': 'anrufen',
 'forget': 'vergessen',
 'pay': 'bezahlen',
 'meet': 'treffen, kennenlernen',
 'stay': 'bleiben',
 'know': 'wissen, kennen',
 'think': 'denken',
 'help': 'helfen',
 'get up': 'aufstehen',
 'look for': 'suchen',
 'busy': 'beschäftigt',
 'sick': 'krank',
 'fast': 'schnell',
 'unfortunately': 'leider',
 'usually': 'normalerweise, meistens',
 'experience': 'die Erfahrung',
 'job application': 'die Bewerbung',
 'salary': 'das Gehalt',
 'contract': 'der Vertrag',
 'exam': 'die Prüfung',
 'difference': 'der Unterschied',
 'opinion': 'die Meinung',
 'solution': 'die Lösung',
 'feeling': 'das Gefühl',
 'environment': 'die Umwelt',
 'explain': 'erklären',
 'understand': 'verstehen',
 'decide': 'entscheiden',
 'lose': 'verlieren',
 'win': 'gewinnen',
 'prepare': 'vorbereiten',
 'move': 'umziehen; sich bewegen',
 'find out': 'herausfinden',
 'give up': 'aufgeben',
 'look forward to': 'sich freuen auf',
 'important': 'wichtig',
 'satisfied': 'zufrieden',
 'on time': 'pünktlich',
 'quite': 'ziemlich',
 'recently': 'neulich, in letzter Zeit',
 'requirement': 'die Anforderung, die Voraussetzung',
 'opportunity': 'die Gelegenheit, die Chance',
 'responsibility': 'die Verantwortung',
 'insurance': 'die Versicherung',
 'advantage': 'der Vorteil',
 'disadvantage': 'der Nachteil',
 'reason': 'der Grund',
 'result': 'das Ergebnis',
 'goal': 'das Ziel',
 'behaviour': 'das Verhalten',
 'apply for': 'sich bewerben um',
 'complain': 'sich beschweren',
 'recommend': 'empfehlen',
 'compare': 'vergleichen',
 'describe': 'beschreiben',
 'improve': 'verbessern',
 'avoid': 'vermeiden',
 'achieve': 'erreichen',
 'deal with': 'sich kümmern um',
 'get used to': 'sich gewöhnen an',
 'take part in': 'teilnehmen an',
 'honest': 'ehrlich',
 'careful': 'vorsichtig',
 'therefore': 'deshalb, daher',
 'however': 'jedoch, allerdings',
 'expectation': 'die Erwartung',
 'challenge': 'die Herausforderung',
 'skill': 'die Fähigkeit',
 'success': 'der Erfolg',
 'relationship': 'die Beziehung',
 'argument': 'der Streit; das Argument',
 'exception': 'die Ausnahme',
 'advertisement': 'die Werbung, die Anzeige',
 'customer': 'der Kunde',
 'purpose': 'der Zweck',
 'rely on': 'sich verlassen auf',
 'apologise': 'sich entschuldigen',
 'convince': 'überzeugen',
 'claim': 'behaupten',
 'postpone': 'verschieben',
 'depend on': 'abhängen von',
 'increase': 'steigen, erhöhen',
 'reduce': 'reduzieren, verringern',
 'put off': 'aufschieben',
 'carry on': 'weitermachen',
 'run out of': 'ausgehen (es geht mir aus)',
 'curious': 'neugierig',
 'reliable': 'zuverlässig',
 'actually': 'eigentlich',
 'eventually': 'schließlich, letztendlich',
 'impact': 'die Auswirkung',
 'measure': 'die Maßnahme',
 'effort': 'die Mühe, der Aufwand',
 'condition': 'die Bedingung',
 'demand': 'die Forderung; die Nachfrage',
 'attitude': 'die Einstellung',
 'prejudice': 'das Vorurteil',
 'competition': 'der Wettbewerb',
 'sustainability': 'die Nachhaltigkeit',
 'contribute': 'beitragen',
 'consider': 'berücksichtigen; in Betracht ziehen',
 'overcome': 'überwinden',
 'enable': 'ermöglichen',
 'influence': 'beeinflussen',
 'notice': 'bemerken',
 'refuse': 'sich weigern, ablehnen',
 'come up with': 'sich einfallen lassen',
 'turn down': 'ablehnen',
 'point out': 'hinweisen auf',
 'obvious': 'offensichtlich',
 'sufficient': 'ausreichend',
 'reasonable': 'vernünftig, angemessen',
 'nevertheless': 'dennoch',
 'apparently': 'anscheinend',
 'basis': 'die Grundlage',
 'addiction': 'die Sucht',
 'perception': 'die Wahrnehmung',
 'restriction': 'die Einschränkung',
 'agreement': 'die Vereinbarung',
 'willingness': 'die Bereitschaft',
 'decline': 'der Rückgang',
 'implementation': 'die Umsetzung',
 'emphasise': 'betonen, hervorheben',
 'estimate': 'schätzen',
 'reject': 'ablehnen',
 'contradict': 'widersprechen',
 'assume': 'annehmen',
 'take over': 'übernehmen',
 'make up for': 'wiedergutmachen, ausgleichen',
 'get away with': 'ungestraft davonkommen',
 'look into': 'untersuchen, prüfen',
 'figure out': 'herausfinden, kapieren',
 'inevitable': 'unvermeidlich',
 'considerable': 'erheblich',
 'reluctant': 'widerwillig',
 'aware': 'bewusst',
 'largely': 'weitgehend',
 'if necessary': 'gegebenenfalls',
 'assumption': 'die Annahme',
 'approach': 'der Ansatz',
 'authority': 'die Befugnis; die Behörde',
 'suspicion': 'der Verdacht',
 'recognition': 'die Anerkennung',
 'misuse': 'der Missbrauch',
 'vulnerability': 'die Schwachstelle, die Verwundbarkeit',
 'threat': 'die Bedrohung',
 'upturn': 'der Aufschwung',
 'tackle': 'angehen, in Angriff nehmen',
 'undermine': 'untergraben',
 'prompt': 'veranlassen, auslösen',
 'resolve': 'lösen, beheben',
 'imply': 'andeuten, implizieren',
 'acknowledge': 'anerkennen, einräumen',
 'strive': 'streben',
 'weigh up': 'abwägen',
 'stem from': 'herrühren von',
 'bring about': 'herbeiführen, bewirken',
 'decisive': 'entscheidend',
 'lasting': 'dauerhaft, nachhaltig',
 'tentative': 'vorläufig, zögerlich',
 'compelling': 'überzeugend, zwingend',
 'arguably': 'wohl, möglicherweise',
 'objection': 'der Einwand',
 'scope': 'der Umfang, der Rahmen',
 'leeway': 'der Spielraum',
 'concern': 'die Sorge; das Anliegen',
 'extent': 'das Ausmaß',
 'hurdle': 'die Hürde',
 'compromise': 'der Kompromiss',
 'criticise': 'kritisieren, bemängeln',
 'pursue': 'verfolgen',
 'resort to': 'zurückgreifen auf',
 'counteract': 'entgegenwirken',
 'address': 'ansprechen, angehen',
 'question': 'hinterfragen',
 'turn out': 'sich herausstellen',
 'put up with': 'sich abfinden mit, ertragen',
 'come across': 'stoßen auf',
 'rule out': 'ausschließen',
 'unavoidable': 'unumgänglich',
 'appropriate': 'angemessen',
 'relevant': 'relevant, einschlägig',
 'thorough': 'gründlich',
 'anyway': 'ohnehin, sowieso',
 'by and large': 'im Großen und Ganzen',
 'bias': 'die Voreingenommenheit',
 'dilemma': 'die Zwickmühle, das Dilemma',
 'ulterior motive': 'der Hintergedanke',
 'change of heart': 'der Sinneswandel',
 'negligence': 'die Fahrlässigkeit',
 'undertaking': 'das Unterfangen',
 'denounce': 'anprangern',
 'substantiate': 'untermauern',
 'thwart': 'vereiteln',
 'contemplate': 'erwägen',
 'loom': 'drohen, sich abzeichnen',
 'gloss over': 'beschönigen',
 'play down': 'verharmlosen',
 'carry weight': 'ins Gewicht fallen',
 'be on the fence': 'unentschlossen sein',
 'blunt': 'unverblümt',
 'glaring': 'eklatant',
 'notwithstanding': 'ungeachtet',
 'by no means': 'mitnichten, keineswegs',
 'to some extent': 'gewissermaßen, in gewissem Maße',
 'as far as possible': 'tunlichst, möglichst',
 'window dressing': 'die Augenwischerei',
 'balancing act': 'der Spagat, die Gratwanderung',
 'hair-splitting': 'die Haarspalterei',
 'pitfall': 'der Fallstrick',
 'fly in the ointment': 'der Wermutstropfen',
 'tunnel vision': 'der Tunnelblick',
 'predicament': 'die Bredouille, die Zwangslage',
 'go the extra mile': 'sich ins Zeug legen',
 'get the short end of the stick': 'den Kürzeren ziehen',
 'sweep under the rug': 'unter den Teppich kehren',
 'beat around the bush': 'um den heißen Brei herumreden',
 'put your foot in it': 'ins Fettnäpfchen treten',
 'cut corners': 'pfuschen, schludern',
 'bite the bullet': 'in den sauren Apfel beißen',
 'hit the nail on the head': 'den Nagel auf den Kopf treffen',
 'backfire': 'nach hinten losgehen',
 'snub': 'brüskieren',
 'equivocate': 'ausweichend antworten, lavieren',
 'terse': 'knapp, lapidar',
 'obsolete': 'veraltet, obsolet',
 'vehement': 'vehement, heftig',
 'hello': 'hallo',
 'good morning': 'guten Morgen',
 'good afternoon': 'guten Tag',
 'good evening': 'guten Abend',
 'good night': 'gute Nacht',
 'bye': 'tschüss',
 'goodbye': 'auf Wiedersehen',
 'see you later': 'bis später',
 'see you tomorrow': 'bis morgen',
 'see you soon': 'bis bald',
 'yes': 'ja',
 'no': 'nein, kein',
 'maybe': 'vielleicht',
 'please': 'bitte',
 'thanks': 'danke',
 'thank you very much': 'danke schön',
 "you're welcome": 'gern geschehen',
 'excuse me': 'entschuldigung',
 "I'm sorry": 'es tut mir leid',
 'no problem': 'kein Problem',
 'how are you?': "wie geht's?",
 "I'm fine": 'mir geht es gut',
 'and you?': 'und dir?',
 'welcome': 'willkommen',
 'my name is …': 'mein Name ist ...',
 "I'm called …": 'ich heiße ...',
 'nice to meet you': 'freut mich',
 'pardon?': 'wie bitte?',
 "I don't understand": 'ich verstehe nicht',
 'slowly': 'langsam bitte',
 'once more': 'noch einmal',
 'of course': 'natürlich',
 'exactly': 'genau',
 'right': 'stimmt, rechts, richtig',
 'okay': 'okay',
 'all right': 'in Ordnung',
 'good luck': 'viel Glück',
 'have fun': 'viel Spaß',
 'have a good trip': 'gute Reise',
 'enjoy your meal': 'guten Appetit',
 'cheers': 'prost',
 'congratulations': 'herzlichen Glückwunsch',
 'all the best': 'alles Gute',
 'get well soon': 'gute Besserung',
 'have a nice weekend': 'schönes Wochenende',
 'here you are': 'bitte schön',
 'pardon me': 'Verzeihung',
 'attention': 'Achtung',
 'help!': 'Hilfe!',
 'zero': 'null',
 'one': 'eins',
 'two': 'zwei',
 'three': 'drei',
 'four': 'vier',
 'five': 'fünf',
 'six': 'sechs',
 'seven': 'sieben',
 'eight': 'acht',
 'nine': 'neun',
 'ten': 'zehn',
 'eleven': 'elf',
 'twelve': 'zwölf',
 'thirteen': 'dreizehn',
 'fourteen': 'vierzehn',
 'fifteen': 'fünfzehn',
 'sixteen': 'sechzehn',
 'seventeen': 'siebzehn',
 'eighteen': 'achtzehn',
 'nineteen': 'neunzehn',
 'twenty': 'zwanzig',
 'thirty': 'dreißig',
 'forty': 'vierzig',
 'fifty': 'fünfzig',
 'sixty': 'sechzig',
 'seventy': 'siebzig',
 'eighty': 'achtzig',
 'ninety': 'neunzig',
 'hundred': 'hundert',
 'thousand': 'tausend',
 'million': 'die Million',
 'first': 'erste, zuerst',
 'second': 'zweite',
 'third': 'dritte',
 'last': 'letzte, zuletzt',
 'half': 'halb',
 'half (noun)': 'die Hälfte',
 'quarter': 'das Viertel',
 'pair': 'das Paar',
 'dozen': 'das Dutzend',
 'much': 'viel',
 'little': 'wenig',
 'more': 'mehr',
 'less': 'weniger',
 'enough': 'genug',
 'all': 'alle',
 'nothing': 'nichts',
 'something': 'etwas',
 'number': 'die Zahl',
 'number (phone': 'die Nummer',
 'percent': 'das Prozent',
 'piece': 'das Stück',
 'kilo': 'das Kilo',
 'gram': 'das Gramm',
 'litre': 'der Liter',
 'colour': 'die Farbe',
 'red': 'rot',
 'blue': 'blau',
 'yellow': 'gelb',
 'green': 'grün',
 'black': 'schwarz',
 'white': 'weiß',
 'grey': 'grau',
 'brown': 'braun',
 'orange': 'orange',
 'pink': 'rosa',
 'purple': 'lila',
 'colourful': 'bunt',
 'light': 'hell, leicht',
 'dark': 'dunkel',
 'circle': 'der Kreis',
 'square': 'das Quadrat, der Platz',
 'line': 'die Linie',
 'round': 'rund',
 'I': 'ich',
 'you': 'du',
 'he': 'er',
 'she': 'sie',
 'it': 'es',
 'we': 'wir',
 'you (plural)': 'ihr',
 'my': 'mein',
 'your': 'dein',
 'his': 'sein',
 'our': 'unser',
 'your (plural)': 'euer',
 'me': 'mich',
 'you (object)': 'dich',
 'one (people in general)': 'man',
 'this': 'dieser',
 'that': 'jener, dass',
 'every': 'jeder',
 'some': 'einige',
 'others': 'andere',
 'oneself': 'selbst',
 'and': 'und',
 'or': 'oder',
 'but': 'aber, doch',
 'because': 'denn, weil',
 'if': 'wenn',
 'when': 'als, wann',
 'whether': 'ob',
 'although': 'obwohl',
 'so that': 'damit',
 'so': 'also',
 'but rather': 'sondern',
 'both … and': 'sowohl ... als auch',
 'either … or': 'entweder ... oder',
 'neither … nor': 'weder ... noch',
 'in': 'in',
 'at': 'an, bei',
 'on': 'auf',
 'under': 'unter',
 'over': 'über',
 'in front of': 'vor',
 'behind': 'hinter',
 'next to': 'neben',
 'between': 'zwischen',
 'with': 'mit',
 'without': 'ohne',
 'for': 'für',
 'against': 'gegen',
 'from': 'von',
 'to': 'zu',
 'after': 'nach',
 'out of': 'aus',
 'since': 'seit',
 'until': 'bis',
 'through': 'durch',
 'around': 'um',
 'during': 'während',
 'because of': 'wegen',
 'instead of': 'statt',
 'except': 'außer',
 'opposite': 'gegenüber',
 'who': 'wer',
 'what': 'was',
 'where': 'wo',
 'where to': 'wohin',
 'where from': 'woher',
 'how': 'wie',
 'why': 'warum, weshalb',
 'how come': 'wieso',
 'which': 'welcher',
 'how much': 'wie viel',
 'how many': 'wie viele',
 'how long': 'wie lange',
 'how often': 'wie oft',
 'how far': 'wie weit',
 'whom': 'wen',
 'whose': 'wessen',
 'time': 'die Zeit',
 'clock': 'die Uhr',
 'hour': 'die Stunde',
 'minute': 'die Minute',
 'month': 'der Monat',
 'year': 'das Jahr',
 'morning': 'der Morgen',
 'late morning': 'der Vormittag',
 'noon': 'der Mittag',
 'afternoon': 'der Nachmittag',
 'evening': 'der Abend',
 'night': 'die Nacht',
 'yesterday': 'gestern',
 'now': 'jetzt',
 'right away': 'gleich',
 'immediately': 'sofort',
 'later': 'später',
 'earlier': 'früher',
 'soon': 'bald',
 'just now': 'gerade',
 'never': 'nie',
 'sometimes': 'manchmal',
 'often': 'oft',
 'rarely': 'selten',
 'mostly': 'meistens',
 'daily': 'täglich',
 'weekly': 'wöchentlich',
 'monthly': 'monatlich',
 'yearly': 'jährlich',
 'Monday': 'der Montag',
 'Tuesday': 'der Dienstag',
 'Wednesday': 'der Mittwoch',
 'Thursday': 'der Donnerstag',
 'Friday': 'der Freitag',
 'Saturday': 'der Samstag',
 'Sunday': 'der Sonntag',
 'weekend': 'das Wochenende',
 'working day': 'der Werktag',
 'public holiday': 'der Feiertag',
 'January': 'der Januar',
 'February': 'der Februar',
 'March': 'der März',
 'April': 'der April',
 'May': 'der Mai',
 'June': 'der Juni',
 'July': 'der Juli',
 'August': 'der August',
 'September': 'der September',
 'October': 'der Oktober',
 'November': 'der November',
 'December': 'der Dezember',
 'spring': 'der Frühling',
 'summer': 'der Sommer',
 'autumn': 'der Herbst',
 'winter': 'der Winter',
 'season': 'die Jahreszeit',
 'date': 'das Datum',
 'calendar': 'der Kalender',
 'past': 'die Vergangenheit',
 'present': 'die Gegenwart, das Geschenk',
 'future': 'die Zukunft',
 'birthday': 'der Geburtstag',
 'delay': 'die Verspätung',
 'punctual': 'pünktlich',
 'human being': 'der Mensch',
 'people': 'die Leute',
 'person': 'die Person',
 'man': 'der Mann',
 'woman': 'die Frau',
 'boy': 'der Junge',
 'girl': 'das Mädchen',
 'baby': 'das Baby',
 'parents': 'die Eltern',
 'father': 'der Vater',
 'mother': 'die Mutter',
 'son': 'der Sohn',
 'daughter': 'die Tochter',
 'brother': 'der Bruder',
 'sister': 'die Schwester',
 'siblings': 'die Geschwister',
 'grandparents': 'die Großeltern',
 'grandfather': 'der Großvater',
 'grandmother': 'die Großmutter',
 'grandpa': 'der Opa',
 'grandma': 'die Oma',
 'grandson': 'der Enkel',
 'uncle': 'der Onkel',
 'aunt': 'die Tante',
 'cousin (male)': 'der Cousin',
 'cousin (female)': 'die Cousine',
 'nephew': 'der Neffe',
 'niece': 'die Nichte',
 'father-in-law': 'der Schwiegervater',
 'mother-in-law': 'die Schwiegermutter',
 'husband': 'der Ehemann',
 'wife': 'die Ehefrau',
 'partner': 'der Partner',
 'girlfriend': 'die Freundin',
 'colleague': 'der Kollege',
 'guest': 'der Gast',
 'adult': 'der Erwachsene',
 'teenager': 'der Jugendliche',
 'first name': 'der Vorname',
 'surname': 'der Nachname',
 'age': 'das Alter',
 'wedding': 'die Hochzeit',
 'marriage': 'die Ehe',
 'love': 'die Liebe',
 'friendship': 'die Freundschaft',
 'single': 'ledig',
 'married': 'verheiratet',
 'divorced': 'geschieden',
 'pregnant': 'schwanger',
 'related': 'verwandt',
 'body': 'der Körper',
 'head': 'der Kopf',
 'hair': 'das Haar',
 'face': 'das Gesicht',
 'eye': 'das Auge',
 'nose': 'die Nase',
 'mouth': 'der Mund',
 'ear': 'das Ohr',
 'tooth': 'der Zahn',
 'neck': 'der Hals',
 'arm': 'der Arm',
 'hand': 'die Hand',
 'finger': 'der Finger',
 'back': 'der Rücken',
 'belly': 'der Bauch',
 'leg': 'das Bein',
 'knee': 'das Knie',
 'foot': 'der Fuß',
 'skin': 'die Haut',
 'heart': 'das Herz',
 'blood': 'das Blut',
 'health': 'die Gesundheit',
 'illness': 'die Krankheit',
 'healthy': 'gesund',
 'pain': 'die Schmerzen',
 'cold': 'die Erkältung',
 'fever': 'das Fieber',
 'cough': 'der Husten',
 'flu': 'die Grippe',
 'allergy': 'die Allergie',
 'wound': 'die Wunde',
 'accident': 'der Unfall',
 'doctor': 'der Arzt',
 'doctor (female)': 'die Ärztin',
 'dentist': 'der Zahnarzt',
 'hospital': 'das Krankenhaus',
 "doctor's office": 'die Praxis',
 'medicine': 'das Medikament',
 'pill': 'die Tablette',
 'prescription': 'das Rezept',
 'examination': 'die Untersuchung',
 'health insurance': 'die Krankenkasse',
 'insurance card': 'die Versichertenkarte',
 'emergency room': 'die Notaufnahme',
 'ambulance': 'der Krankenwagen',
 'treatment': 'die Behandlung',
 'weak': 'schwach',
 'strong': 'stark',
 'glasses': 'die Brille',
 'to sleep': 'schlafen',
 'rest': 'sich ausruhen',
 'hurt': 'weh tun',
 'feel': 'sich fühlen, fühlen, empfinden',
 'breathe': 'atmen',
 'heal': 'heilen',
 'flat': 'die Wohnung',
 'living room': 'das Wohnzimmer',
 'bedroom': 'das Schlafzimmer',
 'bathroom': 'das Badezimmer',
 'toilet': 'die Toilette',
 'hallway': 'der Flur',
 'balcony': 'der Balkon',
 'garden': 'der Garten',
 'basement': 'der Keller',
 'door': 'die Tür',
 'window': 'das Fenster',
 'wall': 'die Wand',
 'floor': 'der Boden, das Stockwerk',
 'ceiling': 'die Decke',
 'roof': 'das Dach',
 'stairs': 'die Treppe',
 'lift': 'der Aufzug',
 'lock': 'das Schloss',
 'furniture': 'die Möbel',
 'armchair': 'der Sessel',
 'sofa': 'das Sofa',
 'bed': 'das Bett',
 'cupboard': 'der Schrank',
 'shelf': 'das Regal',
 'lamp': 'die Lampe',
 'carpet': 'der Teppich',
 'mirror': 'der Spiegel',
 'picture': 'das Bild',
 'towel': 'das Handtuch',
 'soap': 'die Seife',
 'toothbrush': 'die Zahnbürste',
 'toothpaste': 'die Zahnpasta',
 'shampoo': 'das Shampoo',
 'shower': 'die Dusche',
 'washbasin': 'das Waschbecken',
 'washing machine': 'die Waschmaschine',
 'fridge': 'der Kühlschrank',
 'stove': 'der Herd',
 'oven': 'der Backofen',
 'dishwasher': 'die Spülmaschine',
 'heating': 'die Heizung',
 'air conditioning': 'die Klimaanlage',
 'rubbish': 'der Müll',
 'bin': 'der Mülleimer',
 'socket': 'die Steckdose',
 'plug': 'der Stecker',
 'tenant': 'der Mieter',
 'landlord': 'der Vermieter',
 'additional costs': 'die Nebenkosten',
 'deposit': 'die Kaution',
 'rental agreement': 'der Mietvertrag',
 'caretaker': 'der Hausmeister',
 'street': 'die Straße',
 'house number': 'die Hausnummer',
 'postcode': 'die Postleitzahl',
 'ground floor': 'das Erdgeschoss',
 'move (house)': 'der Umzug',
 'housework': 'die Hausarbeit',
 'clean': 'putzen',
 'tidy up': 'aufräumen',
 'wash': 'waschen',
 'cook': 'kochen',
 'to live': 'wohnen',
 'to rent': 'mieten',
 'to move (house)': 'umziehen',
 'cosy': 'gemütlich',
 'dirty': 'schmutzig',
 'food': 'das Essen',
 'lunch': 'das Mittagessen',
 'dinner': 'das Abendessen',
 'hunger': 'der Hunger',
 'thirst': 'der Durst',
 'hungry': 'hungrig',
 'thirsty': 'durstig',
 'bread roll': 'das Brötchen',
 'butter': 'die Butter',
 'cheese': 'der Käse',
 'egg': 'das Ei',
 'milk': 'die Milch',
 'yoghurt': 'der Joghurt',
 'cream': 'die Sahne',
 'meat': 'das Fleisch',
 'beef': 'das Rindfleisch',
 'chicken': 'das Hähnchen',
 'pork': 'das Schweinefleisch',
 'sausage': 'die Wurst',
 'ham': 'der Schinken',
 'fish': 'der Fisch',
 'soup': 'die Suppe',
 'salad': 'der Salat',
 'vegetables': 'das Gemüse',
 'fruit': 'das Obst',
 'potato': 'die Kartoffel',
 'tomato': 'die Tomate',
 'cucumber': 'die Gurke',
 'onion': 'die Zwiebel',
 'garlic': 'der Knoblauch',
 'carrot': 'die Karotte',
 'pepper (spice)': 'der Pfeffer',
 'pepper (vegetable)': 'die Paprika',
 'rice': 'der Reis',
 'pasta': 'die Nudeln',
 'flour': 'das Mehl',
 'sugar': 'der Zucker',
 'salt': 'das Salz',
 'oil': 'das Öl',
 'apple': 'der Apfel',
 'banana': 'die Banane',
 'lemon': 'die Zitrone',
 'strawberry': 'die Erdbeere',
 'cake': 'der Kuchen',
 'chocolate': 'die Schokolade',
 'ice cream': 'das Eis',
 'honey': 'der Honig',
 'jam': 'die Marmelade',
 'coffee': 'der Kaffee',
 'tea': 'der Tee',
 'juice': 'der Saft',
 'beer': 'das Bier',
 'wine': 'der Wein',
 'lemonade': 'die Limonade',
 'bottle': 'die Flasche',
 'glass': 'das Glas',
 'cup': 'die Tasse',
 'plate': 'der Teller',
 'fork': 'die Gabel',
 'knife': 'das Messer',
 'spoon': 'der Löffel',
 'pot': 'der Topf',
 'pan': 'die Pfanne',
 'restaurant': 'das Restaurant',
 'café': 'das Café',
 'menu': 'die Speisekarte',
 'tip': 'das Trinkgeld',
 'waiter': 'der Kellner',
 'order': 'die Bestellung, der Auftrag',
 'starter': 'die Vorspeise',
 'main course': 'das Hauptgericht',
 'dessert': 'die Nachspeise',
 'ingredient': 'die Zutat',
 'delicious': 'lecker',
 'sweet': 'süß',
 'salty': 'salzig',
 'sour': 'sauer',
 'spicy': 'scharf',
 'fresh': 'frisch',
 'cooked': 'gekocht',
 'to eat': 'essen',
 'to drink': 'trinken',
 'bake': 'backen',
 'fry': 'braten',
 'cut': 'schneiden',
 'try': 'probieren, versuchen',
 'to order': 'bestellen',
 'to pay': 'bezahlen',
 'full (after eating)': 'satt',
 'vegetarian': 'vegetarisch',
 'clothes': 'die Kleidung',
 'shirt': 'das Hemd',
 'T-shirt': 'das T-Shirt',
 'jumper': 'der Pullover',
 'jacket': 'die Jacke',
 'coat': 'der Mantel',
 'trousers': 'die Hose',
 'jeans': 'die Jeans',
 'skirt': 'der Rock',
 'dress': 'das Kleid',
 'sock': 'die Socke',
 'underwear': 'die Unterwäsche',
 'shoe': 'der Schuh',
 'hat': 'der Hut',
 'cap': 'die Mütze',
 'scarf': 'der Schal',
 'belt': 'der Gürtel',
 'bag': 'die Tasche',
 'backpack': 'der Rucksack',
 'umbrella': 'der Regenschirm',
 'jewellery': 'der Schmuck',
 'size': 'die Größe',
 'put on': 'anziehen',
 'take off': 'ausziehen',
 'wear': 'tragen',
 'try on': 'anprobieren',
 'fit': 'passen',
 'suit': 'stehen',
 'tight': 'eng',
 'wide': 'weit, breit',
 'fashionable': 'modisch',
 'comfortable': 'bequem',
 'changing room': 'die Umkleidekabine',
 'laundry': 'die Wäsche',
 'brand': 'die Marke',
 'fashion': 'die Mode',
 'sunglasses': 'die Sonnenbrille',
 'village': 'das Dorf',
 'centre': 'das Zentrum',
 'city centre': 'die Innenstadt',
 'park': 'der Park',
 'bridge': 'die Brücke',
 'river': 'der Fluss',
 'building': 'das Gebäude',
 'church': 'die Kirche',
 'mosque': 'die Moschee',
 'museum': 'das Museum',
 'theatre': 'das Theater',
 'cinema': 'das Kino',
 'library': 'die Bibliothek',
 'school': 'die Schule',
 'university': 'die Universität, die Hochschule',
 'town hall': 'das Rathaus',
 'post office': 'die Post',
 'bank': 'die Bank',
 'hotel': 'das Hotel',
 'store': 'der Laden',
 'supermarket': 'der Supermarkt',
 'bakery': 'die Bäckerei',
 "butcher's": 'die Metzgerei',
 'market': 'der Markt',
 'shopping centre': 'das Einkaufszentrum',
 'petrol station': 'die Tankstelle',
 'car park': 'der Parkplatz',
 'train station': 'der Bahnhof',
 'stop (bus': 'die Haltestelle',
 'airport': 'der Flughafen',
 'harbour': 'der Hafen',
 'stadium': 'das Stadion',
 'swimming pool': 'das Schwimmbad',
 'gym': 'das Fitnessstudio',
 'hairdresser': 'der Friseur',
 'police': 'die Polizei',
 'fire brigade': 'die Feuerwehr',
 'zoo': 'der Zoo',
 'corner': 'die Ecke',
 'crossroads': 'die Kreuzung',
 'traffic light': 'die Ampel',
 'pavement': 'der Gehweg',
 'way': 'der Weg',
 'direction': 'die Richtung',
 'left': 'links',
 'straight ahead': 'geradeaus',
 'above': 'oben',
 'below': 'unten',
 'at the front': 'vorne',
 'at the back': 'hinten',
 'middle': 'die Mitte',
 'side': 'die Seite',
 'near': 'nah',
 'surroundings': 'die Umgebung',
 'place': 'der Ort',
 'area': 'die Gegend',
 'border': 'die Grenze',
 'capital city': 'die Hauptstadt',
 'inhabitant': 'der Einwohner',
 'sight (tourist attraction)': 'die Sehenswürdigkeit',
 'monument': 'das Denkmal',
 'tower': 'der Turm',
 'view': 'die Aussicht',
 'trip': 'die Reise',
 'traffic': 'der Verkehr',
 'car': 'das Auto',
 'bus': 'der Bus',
 'train': 'die Bahn, der Zug',
 'suburban train': 'die S-Bahn',
 'underground': 'die U-Bahn',
 'tram': 'die Straßenbahn',
 'bicycle': 'das Fahrrad',
 'motorbike': 'das Motorrad',
 'taxi': 'das Taxi',
 'plane': 'das Flugzeug',
 'ship': 'das Schiff',
 'driving licence': 'der Führerschein',
 'timetable': 'der Fahrplan',
 'platform': 'das Gleis',
 'exit': 'der Ausgang',
 'entrance': 'der Eingang',
 'departure': 'die Abfahrt',
 'arrival': 'die Ankunft',
 'connection': 'die Verbindung, der Anschluss',
 'change (trains)': 'umsteigen',
 'get on': 'einsteigen',
 'get off': 'aussteigen',
 'drive': 'fahren',
 'fly': 'fliegen',
 'walk': 'laufen',
 'on foot': 'zu Fuß',
 'motorway': 'die Autobahn',
 'speed': 'die Geschwindigkeit',
 'petrol': 'das Benzin',
 'engine': 'der Motor',
 'wheel': 'das Rad',
 'tyre': 'der Reifen',
 'breakdown': 'die Panne',
 'route': 'die Strecke',
 'distance': 'die Entfernung',
 'suitcase': 'der Koffer',
 'luggage': 'das Gepäck',
 'passport': 'der Pass',
 'visa': 'das Visum',
 'ID card': 'der Ausweis',
 'customs': 'der Zoll',
 'booking': 'die Buchung',
 'accommodation': 'die Unterkunft',
 'youth hostel': 'die Jugendherberge',
 'tent': 'das Zelt',
 'school holidays': 'die Ferien',
 'excursion': 'der Ausflug',
 'tour': 'die Tour',
 'tourist': 'der Tourist',
 'map': 'die Karte',
 'satnav': 'das Navi',
 'traffic jam': 'der Stau',
 'construction site': 'die Baustelle',
 'visit': 'besichtigen, besuchen',
 'reserve': 'reservieren',
 'pack': 'packen',
 'arrive': 'ankommen',
 'depart': 'abfahren, abreisen',
 'miss': 'verpassen',
 'to wait': 'warten',
 'safety': 'die Sicherheit',
 'euro': 'der Euro',
 'cent': 'der Cent',
 'checkout': 'die Kasse',
 'receipt': 'die Quittung',
 'salesperson': 'der Verkäufer',
 'shopping': 'der Einkauf',
 'shopping list': 'die Einkaufsliste',
 'shopping trolley': 'der Einkaufswagen',
 'plastic bag': 'die Tüte',
 'offer': 'das Angebot',
 'discount': 'der Rabatt',
 'clearance sale': 'der Ausverkauf',
 'free of charge': 'kostenlos',
 'good value': 'günstig',
 'cash': 'das Bargeld',
 'credit card': 'die Kreditkarte',
 'debit card': 'die EC-Karte',
 'account': 'das Konto',
 'bank transfer': 'die Überweisung',
 'bank sort code': 'die Bankleitzahl',
 'IBAN': 'die IBAN',
 'cash machine': 'der Geldautomat',
 'change (money)': 'das Wechselgeld',
 'tax': 'die Steuer',
 'VAT': 'die Mehrwertsteuer',
 'fee': 'die Gebühr',
 'costs': 'die Kosten',
 'income': 'das Einkommen',
 'save': 'sparen, speichern, retten',
 'spend': 'ausgeben',
 'to buy': 'kaufen',
 'sell': 'verkaufen',
 'cost': 'kosten',
 'exchange': 'umtauschen',
 'give back': 'zurückgeben',
 'guarantee': 'die Garantie',
 'delivery': 'die Lieferung',
 'goods': 'die Ware',
 'product': 'das Produkt',
 'quality': 'die Qualität',
 'amount': 'die Menge',
 'choice': 'die Auswahl',
 'complaint (return)': 'die Reklamation',
 'instalment': 'die Rate',
 'debts': 'die Schulden',
 'to have': 'haben',
 'become': 'werden',
 'can': 'können',
 'must': 'müssen',
 'to want': 'wollen',
 'should': 'sollen',
 'to may': 'dürfen',
 'to like': 'mögen',
 'make': 'machen',
 'do': 'tun',
 'to go': 'gehen',
 'to come': 'kommen',
 'say': 'sagen',
 'to speak': 'sprechen',
 'talk': 'reden, sich unterhalten',
 'ask': 'fragen',
 'answer': 'antworten',
 'see': 'sehen',
 'look': 'schauen',
 'hear': 'hören',
 'listen': 'zuhören',
 'know (a fact)': 'wissen',
 'know (a person)': 'kennen',
 'to think': 'denken',
 'believe': 'glauben',
 'mean': 'meinen, bedeuten',
 'hope': 'hoffen',
 'wish': 'wünschen',
 'to need': 'brauchen',
 'get': 'bekommen',
 'take': 'nehmen',
 'give': 'geben',
 'bring': 'bringen',
 'fetch': 'holen',
 'hold': 'halten',
 'lay': 'legen',
 'put (upright)': 'stellen',
 'set': 'setzen',
 'sit': 'sitzen',
 'lie': 'liegen',
 'to get up': 'aufstehen',
 'wake up': 'aufwachen',
 'fall asleep': 'einschlafen',
 'to stay': 'bleiben',
 'belong': 'gehören',
 'begin': 'beginnen',
 'start': 'anfangen, starten',
 'stop': 'aufhören, stoppen',
 'end': 'enden',
 'finish': 'beenden',
 'to carry on': 'weitermachen',
 'manage': 'schaffen',
 'succeed': 'gelingen',
 'fail': 'scheitern, versagen',
 'to help': 'helfen',
 'thank': 'danken',
 'ask (for)': 'bitten',
 'allow': 'erlauben',
 'forbid': 'verbieten',
 'to decide': 'entscheiden',
 'choose': 'wählen',
 'plan': 'planen',
 'change': 'ändern, sich verändern, wechseln',
 'to improve': 'verbessern',
 'grow': 'wachsen',
 'happen': 'passieren, geschehen',
 'take place': 'stattfinden',
 'to last': 'dauern',
 'to meet': 'treffen',
 'invite': 'einladen',
 'come along': 'mitkommen',
 'accompany': 'begleiten',
 'leave': 'verlassen',
 'say goodbye': 'verabschieden, sich verabschieden',
 'reach': 'erreichen',
 'recognise': 'erkennen',
 'to notice': 'merken',
 'travel': 'reisen',
 'to work': 'funktionieren',
 'exist': 'existieren',
 'enjoy': 'genießen',
 'fear': 'fürchten',
 'trust': 'vertrauen',
 'risk': 'riskieren',
 'be missing': 'fehlen',
 'be bored': 'sich langweilen',
 'annoy': 'ärgern',
 'calm (sb) down': 'beruhigen',
 'surprise': 'überraschen',
 'excuse': 'entschuldigen',
 'profession': 'der Beruf',
 'job': 'der Job',
 'position': 'die Stelle',
 'firm': 'die Firma',
 'company': 'das Unternehmen',
 'office': 'das Büro',
 'boss': 'der Chef',
 'employee': 'der Mitarbeiter',
 'team': 'das Team, die Mannschaft',
 'department': 'die Abteilung',
 'meeting': 'die Besprechung, die Sitzung',
 'task': 'die Aufgabe',
 'project': 'das Projekt',
 'vocational training': 'die Ausbildung',
 'internship': 'das Praktikum',
 'CV': 'der Lebenslauf',
 'job interview': 'das Vorstellungsgespräch',
 'working hours': 'die Arbeitszeit',
 'overtime': 'die Überstunde',
 'break': 'die Pause',
 'shift': 'die Schicht',
 'end of the working day': 'der Feierabend',
 'full-time': 'die Vollzeit',
 'part-time': 'die Teilzeit',
 'mini-job': 'der Minijob',
 'working student': 'der Werkstudent',
 'unemployed': 'arbeitslos',
 'self-employed': 'selbstständig',
 'teacher': 'der Lehrer',
 'engineer': 'der Ingenieur',
 'lawyer': 'der Anwalt',
 'baker': 'der Bäcker',
 'driver': 'der Fahrer',
 'police officer': 'der Polizist',
 'nurse (male)': 'der Krankenpfleger',
 'nurse': 'die Krankenschwester',
 'craftsman': 'der Handwerker',
 'electrician': 'der Elektriker',
 'mechanic': 'der Mechaniker',
 'programmer': 'der Programmierer',
 'computer scientist': 'der Informatiker',
 'architect': 'der Architekt',
 'artist': 'der Künstler',
 'journalist': 'der Journalist',
 'civil servant': 'der Beamte',
 'student (university)': 'der Student',
 'intern': 'der Praktikant',
 'pensioner': 'der Rentner',
 'earn': 'verdienen',
 'lead': 'leiten, führen',
 'apply': 'bewerben, anwenden',
 'hire': 'einstellen',
 'quit': 'kündigen',
 'career': 'die Karriere',
 'promotion': 'die Beförderung',
 'ability': 'die Fähigkeit',
 'kindergarten': 'der Kindergarten',
 'primary school': 'die Grundschule',
 'grammar school': 'das Gymnasium',
 'lessons': 'der Unterricht',
 'subject': 'das Fach',
 'class': 'die Klasse',
 'course': 'der Kurs',
 'lecture': 'die Vorlesung',
 'seminar': 'das Seminar',
 'pupil': 'der Schüler',
 'professor': 'der Professor',
 'homework': 'die Hausaufgabe',
 'test': 'der Test',
 'grade': 'die Note',
 'school report': 'das Zeugnis',
 'school-leaving exam (A levels)': 'das Abitur',
 'university studies': 'das Studium',
 'degree': 'der Abschluss, der Grad',
 "bachelor's degree": 'der Bachelor',
 "master's degree": 'der Master',
 'semester': 'das Semester',
 'book': 'das Buch',
 'notebook': 'das Heft',
 'sheet': 'das Blatt',
 'paper': 'das Papier',
 'pen': 'der Stift',
 'pencil': 'der Bleistift',
 'ballpoint pen': 'der Kugelschreiber',
 'eraser': 'der Radiergummi',
 'ruler': 'das Lineal',
 'scissors': 'die Schere',
 'board': 'die Tafel',
 'desk': 'der Schreibtisch',
 'dictionary': 'das Wörterbuch',
 'grammar': 'die Grammatik',
 'word': 'das Wort',
 'sentence': 'der Satz',
 'text': 'der Text',
 'exercise': 'die Übung',
 'mistake': 'der Fehler',
 'example': 'das Beispiel',
 'topic': 'das Thema',
 'knowledge': 'das Wissen',
 'learn': 'lernen',
 'study (at university)': 'studieren',
 'teach': 'lehren',
 'to explain': 'erklären',
 'to understand': 'verstehen',
 'practise': 'üben',
 'repeat': 'wiederholen',
 'to read': 'lesen',
 'to write': 'schreiben',
 'calculate': 'rechnen',
 'pass (an exam)': 'bestehen',
 'fail (an exam)': 'durchfallen',
 'maths': 'die Mathematik',
 'physics': 'die Physik',
 'chemistry': 'die Chemie',
 'biology': 'die Biologie',
 'history': 'die Geschichte',
 'geography': 'die Erdkunde',
 'art': 'die Kunst',
 'music': 'die Musik',
 'nature': 'die Natur',
 'sun': 'die Sonne',
 'moon': 'der Mond',
 'star': 'der Stern',
 'sky': 'der Himmel',
 'cloud': 'die Wolke',
 'rain': 'der Regen',
 'snow': 'der Schnee',
 'wind': 'der Wind',
 'storm': 'der Sturm',
 'fog': 'der Nebel',
 'temperature': 'die Temperatur',
 'warm': 'warm',
 'hot': 'heiß',
 'cool': 'kühl',
 'sunny': 'sonnig',
 'cloudy': 'bewölkt',
 'rainy': 'regnerisch',
 'windy': 'windig',
 'foggy': 'neblig',
 'dry': 'trocken',
 'wet': 'nass',
 'humid': 'feucht',
 'mountain': 'der Berg',
 'valley': 'das Tal',
 'forest': 'der Wald',
 'tree': 'der Baum',
 'flower': 'die Blume',
 'grass': 'das Gras',
 'lake': 'der See',
 'sea': 'das Meer',
 'beach': 'der Strand',
 'island': 'die Insel',
 'coast': 'die Küste',
 'stone': 'der Stein',
 'earth': 'die Erde',
 'world': 'die Welt',
 'air': 'die Luft',
 'fire': 'das Feuer',
 'climate change': 'der Klimawandel',
 'energy': 'die Energie',
 'animal': 'das Tier',
 'pet': 'das Haustier',
 'dog': 'der Hund',
 'cat': 'die Katze',
 'horse': 'das Pferd',
 'cow': 'die Kuh',
 'sheep': 'das Schaf',
 'goat': 'die Ziege',
 'pig': 'das Schwein',
 'hen': 'das Huhn',
 'rooster': 'der Hahn',
 'duck': 'die Ente',
 'bird': 'der Vogel',
 'mouse': 'die Maus',
 'rabbit': 'das Kaninchen',
 'bear': 'der Bär',
 'lion': 'der Löwe',
 'elephant': 'der Elefant',
 'snake': 'die Schlange',
 'bee': 'die Biene',
 'insect': 'das Insekt',
 'tail': 'der Schwanz',
 'wing': 'der Flügel',
 'fur': 'das Fell',
 'bark': 'bellen',
 'eat (animals)': 'fressen',
 'feed': 'füttern',
 'wild': 'wild',
 'computer': 'der Computer',
 'laptop': 'der Laptop',
 'mobile phone': 'das Handy',
 'smartphone': 'das Smartphone',
 'telephone': 'das Telefon',
 'screen': 'der Bildschirm',
 'keyboard': 'die Tastatur',
 'file': 'die Datei',
 'program': 'das Programm',
 'software': 'die Software',
 'app': 'die App',
 'internet': 'das Internet',
 'website': 'die Webseite',
 'email': 'die E-Mail',
 'message': 'die Nachricht',
 'password': 'das Passwort',
 'user': 'der Benutzer',
 'data': 'die Daten',
 'memory': 'der Speicher',
 'Wi-Fi': 'das WLAN',
 'battery': 'der Akku',
 'charger': 'das Ladegerät',
 'phone call': 'der Anruf',
 'call (on the phone)': 'anrufen',
 'talk on the phone': 'telefonieren',
 'send': 'schicken, senden',
 'download': 'herunterladen',
 'upload': 'hochladen',
 'delete': 'löschen',
 'click': 'klicken',
 'search': 'suchen',
 'find': 'finden',
 'install': 'installieren',
 'switch off': 'ausschalten',
 'switch on': 'einschalten',
 'television': 'der Fernseher',
 'photo': 'das Foto',
 'video': 'das Video',
 'technology': 'die Technik',
 'to shower': 'duschen',
 'bathe': 'baden',
 'comb': 'kämmen',
 'shave': 'rasieren',
 'note down': 'notieren',
 'organise': 'organisieren',
 'paint': 'malen',
 'draw': 'zeichnen',
 'do crafts': 'basteln',
 'expect': 'erwarten',
 'swim': 'schwimmen',
 'jump': 'springen',
 'climb': 'klettern',
 'smoke': 'rauchen',
 'surf': 'surfen',
 'chat': 'chatten',
 'post': 'posten',
 'like (a post)': 'liken',
 'comment': 'kommentieren',
 'print': 'drucken',
 'scan': 'scannen',
 'grill': 'grillen',
 'wash up': 'spülen',
 'iron': 'bügeln',
 'sew': 'nähen',
 'glue': 'kleben',
 'hang up': 'auflegen',
 'unload': 'ausladen',
 'to park': 'parken',
 'refuel': 'tanken',
 'sort': 'sortieren',
 'look at': 'betrachten',
 'check': 'prüfen',
 'enter': 'eintragen',
 'advise': 'raten',
 'warn': 'warnen',
 'threaten': 'drohen',
 'return': 'zurückkehren',
 'disappear': 'verschwinden',
 'appear': 'erscheinen',
 'arise': 'entstehen',
 'develop': 'sich entwickeln, entwickeln',
 'make worse': 'verschlimmern',
 'secure': 'sichern',
 'halve': 'halbieren',
 'double': 'verdoppeln',
 'multiply': 'multiplizieren',
 'add': 'addieren',
 'subtract': 'subtrahieren',
 'divide': 'dividieren',
 'distinguish': 'unterscheiden',
 'arrange': 'ordnen',
 'Germany': 'Deutschland',
 'Turkey': 'die Türkei',
 'Austria': 'Österreich',
 'Switzerland': 'die Schweiz',
 'France': 'Frankreich',
 'Russia': 'Russland',
 'Europe': 'Europa',
 'language': 'die Sprache',
 'German': 'Deutsch',
 'Turkish': 'Türkisch',
 'English': 'Englisch',
 'mother tongue': 'die Muttersprache',
 'foreigner': 'der Ausländer',
 'nationality': 'die Nationalität',
 'citizenship': 'die Staatsangehörigkeit',
 'culture': 'die Kultur',
 'tradition': 'die Tradition',
 'religion': 'die Religion',
 'society': 'die Gesellschaft',
 'government': 'die Regierung',
 'state': 'der Staat',
 'politics': 'die Politik',
 'law': 'das Gesetz',
 'freedom': 'die Freiheit',
 'newspaper': 'die Zeitung',
 'news': 'die Nachrichten',
 'problem': 'das Problem',
 'sport': 'der Sport',
 'game': 'das Spiel',
 'football': 'der Fußball',
 'swimming': 'das Schwimmen',
 'running': 'das Laufen',
 'fitness': 'das Fitness',
 'training': 'das Training',
 'player': 'der Spieler',
 'coach': 'der Trainer',
 'victory': 'der Sieg',
 'ball': 'der Ball',
 'free time': 'die Freizeit',
 'hobby': 'das Hobby',
 'song': 'das Lied',
 'film': 'der Film',
 'series': 'die Serie',
 'concert': 'das Konzert',
 'party': 'die Party',
 'festival': 'das Fest',
 'celebration': 'die Feier',
 'reading': 'das Lesen',
 'cooking': 'das Kochen',
 'to win': 'gewinnen',
 'to lose': 'verlieren',
 'play': 'spielen',
 'to train': 'trainieren',
 'relax': 'sich entspannen',
 'celebrate': 'feiern',
 'dance': 'tanzen',
 'sing': 'singen',
 'public office': 'das Amt',
 "citizens' office": 'das Bürgeramt',
 'immigration office': 'die Ausländerbehörde',
 'tax office': 'das Finanzamt',
 'job centre': 'das Jobcenter',
 'Federal Employment Agency': 'die Agentur für Arbeit',
 'registration': 'die Anmeldung',
 'deregistration': 'die Abmeldung',
 'certificate': 'die Bescheinigung',
 'form': 'das Formular',
 'application': 'der Antrag',
 'official notice': 'der Bescheid',
 'signature': 'die Unterschrift',
 'stamp': 'der Stempel',
 'copy': 'die Kopie',
 'original': 'das Original',
 'deadline': 'die Frist',
 'proof': 'der Nachweis',
 'registration certificate': 'die Meldebescheinigung',
 'residence permit': 'die Aufenthaltserlaubnis',
 'work permit': 'die Arbeitserlaubnis',
 'tax ID': 'die Steuer-ID',
 'social security': 'die Sozialversicherung',
 'pension insurance': 'die Rentenversicherung',
 'liability insurance': 'die Haftpflichtversicherung',
 'broadcasting fee (TV licence)': 'der Rundfunkbeitrag',
 'case worker': 'der Sachbearbeiter',
 'counter': 'der Schalter',
 'queue number': 'die Wartenummer',
 'opening hours': 'die Öffnungszeiten',
 'to apply for': 'beantragen',
 'fill in': 'ausfüllen',
 'submit': 'einreichen',
 'sign': 'unterschreiben',
 'extend': 'verlängern',
 'bring along': 'mitbringen',
 'pick up': 'abholen',
 'register': 'anmelden',
 'allowed': 'erlaubt',
 'forbidden': 'verboten',
 'necessary': 'nötig',
 'valid': 'gültig',
 'to forget': 'vergessen',
 'remember': 'erinnern',
 'to compare': 'vergleichen',
 'to describe': 'beschreiben',
 'tell': 'erzählen',
 'report': 'berichten, melden',
 'show': 'zeigen',
 'translate': 'übersetzen',
 'pronounce': 'aussprechen',
 'to open': 'öffnen',
 'to close': 'schließen',
 'press': 'drücken',
 'pull': 'ziehen',
 'throw': 'werfen',
 'catch': 'fangen',
 'fall': 'fallen',
 'to lift': 'heben',
 'build': 'bauen',
 'repair': 'reparieren',
 'break (something)': 'kaputt machen',
 'use': 'benutzen, verwenden, nutzen',
 'collect': 'sammeln',
 'share': 'teilen',
 'distribute': 'verteilen',
 'swap': 'tauschen',
 'lend': 'leihen',
 'own': 'besitzen',
 'discover': 'entdecken',
 'inform': 'mitteilen, informieren',
 'argue': 'streiten, sich streiten',
 'discuss': 'diskutieren',
 'promise': 'versprechen',
 'lie (tell lies)': 'lügen',
 'disturb': 'stören',
 'hurry': 'beeilen',
 'observe': 'beobachten',
 'pay attention': 'aufpassen',
 'take care of': 'kümmern',
 'worry': 'sorgen, sich sorgen',
 'protect': 'schützen',
 'fight': 'kämpfen',
 'interest': 'interessieren',
 'please (be liked)': 'gefallen',
 'to love': 'lieben',
 'hate': 'hassen',
 'laugh': 'lachen',
 'cry': 'weinen',
 'smile': 'lächeln',
 'kiss': 'küssen',
 'to call': 'rufen',
 'scream': 'schreien',
 'smell': 'riechen',
 'taste': 'schmecken',
 'touch': 'berühren',
 'weigh': 'wiegen',
 'to measure': 'messen',
 'count': 'zählen',
 'rent out': 'vermieten',
 'deliver': 'liefern',
 'follow': 'folgen',
 'to recommend': 'empfehlen',
 'suggest': 'vorschlagen',
 'to offer': 'anbieten',
 'accept': 'annehmen, akzeptieren',
 'to reject': 'ablehnen',
 'run': 'rennen',
 'dream': 'träumen',
 'bad': 'schlecht',
 'long': 'lang',
 'short': 'kurz',
 'high': 'hoch',
 'low': 'niedrig',
 'narrow': 'schmal',
 'thick': 'dick',
 'thin': 'dünn',
 'heavy': 'schwer',
 'new': 'neu',
 'old': 'alt',
 'young': 'jung',
 'modern': 'modern',
 'slow': 'langsam',
 'loud': 'laut',
 'quiet': 'leise',
 'full': 'voll',
 'empty': 'leer',
 'closed': 'geschlossen',
 'wrong': 'falsch',
 'true': 'wahr',
 'possible': 'möglich',
 'impossible': 'unmöglich',
 'simple': 'einfach',
 'difficult': 'schwierig',
 'complicated': 'kompliziert',
 'interesting': 'interessant',
 'boring': 'langweilig',
 'beautiful': 'schön',
 'nice': 'nett',
 'friendly': 'freundlich',
 'polite': 'höflich',
 'calm': 'ruhig',
 'nervous': 'nervös',
 'hard-working': 'fleißig',
 'lazy': 'faul',
 'clever': 'klug',
 'stupid': 'dumm',
 'dangerous': 'gefährlich',
 'safe': 'sicher',
 'free': 'frei',
 'occupied': 'besetzt',
 'ready': 'bereit',
 'finished': 'fertig',
 'useful': 'nützlich',
 'popular': 'beliebt',
 'well-known': 'bekannt',
 'foreign': 'fremd',
 'similar': 'ähnlich',
 'different': 'verschieden',
 'special': 'besonders',
 'normal': 'normal',
 'real': 'echt',
 'private': 'privat',
 'public': 'öffentlich',
 'poor': 'arm',
 'rich': 'reich',
 'sad': 'traurig',
 'funny': 'lustig',
 'serious': 'ernst',
 'proud': 'stolz',
 'brave': 'mutig',
 'patient': 'geduldig',
 'successful': 'erfolgreich',
 'helpful': 'hilfsbereit',
 'creative': 'kreativ',
 'practical': 'praktisch',
 'perfect': 'perfekt',
 'wonderful': 'wunderbar',
 'great': 'toll',
 'solve': 'lösen',
 'fasten': 'befestigen',
 'obey': 'gehorchen',
 'give (as a present)': 'schenken',
 'borrow': 'ausleihen',
 'invest': 'investieren',
 'come back': 'zurückkommen',
 'go back': 'zurückgehen',
 'set off': 'losfahren',
 'take along': 'mitnehmen',
 'throw away': 'wegwerfen',
 'unpack': 'auspacken',
 'mark': 'markieren',
 'to copy': 'kopieren',
 'transfer': 'übertragen',
 'connect': 'verbinden',
 'separate': 'trennen',
 'to come across': 'begegnen',
 'receive': 'empfangen, erhalten',
 'admire': 'bewundern',
 'complete': 'ergänzen',
 'prove': 'beweisen',
 'worsen': 'verschlechtern',
 'expand': 'erweitern',
 'to reduce': 'reduzieren',
 'raise': 'erhöhen',
 'experiment': 'experimentieren',
 'pause': 'pausieren',
 'continue': 'fortsetzen',
 'interrupt': 'unterbrechen',
 'drop by': 'vorbeikommen',
 'drive past': 'vorbeifahren',
 'turn round': 'umdrehen',
 'stay behind': 'zurückbleiben',
 'treat': 'behandeln',
 'regret': 'bedauern',
 'lament': 'beklagen',
 'mourn': 'beweinen',
 'miss (sb)': 'vermissen',
 'value': 'schätzen',
 'respect': 'respektieren',
 'tolerate': 'tolerieren',
 'ignore': 'ignorieren',
 'analyse': 'analysieren',
 'research': 'recherchieren',
 'explain in detail': 'erläutern',
 'evaluate': 'bewerten',
 'define': 'definieren',
 'construct': 'konstruieren',
 'produce': 'produzieren',
 'consume': 'konsumieren',
 'export': 'exportieren',
 'import': 'importieren',
 'waste': 'verschwenden',
 'to test': 'testen',
 'go wrong': 'misslingen',
 'foresee': 'vorhersehen',
 'thrive': 'gedeihen',
 'pass (time)': 'vergehen',
 'joy': 'die Freude',
 'happiness': 'das Glück',
 'grief': 'die Trauer',
 'stress': 'der Stress',
 'rage': 'die Wut',
 'anger': 'der Ärger',
 'courage': 'der Mut',
 'patience': 'die Geduld',
 'boredom': 'die Langeweile',
 'loneliness': 'die Einsamkeit',
 'character': 'der Charakter',
 'mood': 'die Laune, die Stimmung',
 'laughter': 'das Lachen',
 'tear': 'die Träne',
 'be happy': 'sich freuen',
 'get angry': 'sich ärgern',
 'be ashamed': 'sich schämen',
 'fall in love': 'sich verlieben',
 'be surprised': 'sich wundern',
 'calm down': 'sich beruhigen',
 'excited': 'aufgeregt',
 'disappointed': 'enttäuscht',
 'surprised': 'überrascht',
 'in love': 'verliebt',
 'furious': 'wütend',
 'jealous': 'eifersüchtig',
 'shy': 'schüchtern',
 'eager': 'gespannt',
 'exhausted': 'erschöpft',
 'very': 'sehr',
 'fairly': 'ziemlich',
 'almost': 'fast',
 'only': 'nur',
 'also': 'auch',
 'still': 'noch',
 'already': 'schon, bereits',
 'only (not until)': 'erst',
 'again': 'wieder',
 'above all': 'vor allem',
 'for example': 'zum Beispiel',
 'by the way': 'übrigens',
 'really': 'wirklich',
 'certainly': 'bestimmt',
 'probably': 'wahrscheinlich',
 'hopefully': 'hoffentlich',
 'luckily': 'zum Glück',
 'suddenly': 'plötzlich',
 'finally': 'endlich, schließlich',
 'then': 'dann',
 'afterwards': 'danach',
 'together': 'zusammen',
 'alone': 'allein',
 'jointly': 'gemeinsam',
 'everywhere': 'überall',
 'there': 'dort, da',
 'here': 'hier',
 'outside': 'draußen',
 'inside': 'drinnen',
 'away': 'weg',
 'further': 'weiter',
 'otherwise': 'sonst',
 'hardly': 'kaum',
 'not': 'nicht',
 'gladly': 'gern',
 'rather': 'lieber',
 'most of all': 'am liebsten',
 'at least': 'mindestens',
 'at most': 'höchstens',
 'approximately': 'ungefähr',
 'about': 'etwa',
 'normally': 'normalerweise',
 'in total': 'insgesamt',
 'besides': 'außerdem',
 'even': 'sogar',
 'back then': 'damals',
 'determine': 'festlegen',
 'introduce': 'vorstellen',
 'prepare oneself': 'sich vorbereiten',
 'meet (up)': 'sich treffen',
 'sit down': 'sich setzen',
 'wash (oneself)': 'sich waschen',
 'get dressed': 'sich anziehen',
 'get undressed': 'sich ausziehen',
 'fall in love with': 'sich verlieben in',
 'say thank you': 'sich bedanken',
 'concentrate': 'sich konzentrieren',
 'wish for': 'sich wünschen',
 'be worth it': 'sich lohnen',
 'pay off': 'sich auszahlen',
 'think over': 'sich überlegen',
 'be wrong': 'sich irren',
 'inform oneself': 'sich informieren',
 'to complain': 'sich beklagen',
 'get lost': 'sich verlaufen',
 'make an effort': 'sich anstrengen',
 "know one's way around": 'sich auskennen',
 'dare': 'sich trauen',
 'get worse': 'sich verschlechtern',
 'to look forward to': 'sich freuen auf',
 'look around': 'sich umsehen',
 'get on (well)': 'sich verstehen',
 'get along': 'sich vertragen',
 'adapt': 'sich anpassen',
 'consequence': 'die Folge',
 'commitment': 'die Verpflichtung',
 'complaint': 'die Beschwerde',
 'feature': 'das Merkmal',
 'habit': 'die Gewohnheit',
 'majority': 'die Mehrheit',
 'minority': 'die Minderheit',
 'access': 'der Zugang',
 'cooperation': 'die Zusammenarbeit',
 'doubt': 'der Zweifel',
 'require': 'erfordern',
 'promote': 'fördern; befördern',
 'comply with': 'einhalten',
 'justify': 'begründen, rechtfertigen',
 'assess': 'beurteilen',
 'bear in mind': 'bedenken',
 'carry out': 'durchführen',
 'keep up with': 'Schritt halten mit',
 'run into': 'stoßen auf',
 'sort out': 'regeln, klären',
 'work out': 'herausfinden; trainieren',
 'go through': 'durchmachen',
 'mutual': 'gegenseitig',
 'significant': 'bedeutend',
 'clear-cut': 'eindeutig',
 'presumably': 'vermutlich',
 'increasingly': 'zunehmend',
 'in any case': 'jedenfalls',
 'arrangement': 'die Absprache',
 'dispute': 'die Auseinandersetzung',
 'component': 'der Bestandteil',
 'overview': 'der Überblick',
 'tendency': 'die Tendenz',
 'ratio': 'das Verhältnis',
 'prediction': 'die Vorhersage',
 'cohesion': 'der Zusammenhalt',
 'relief': 'die Erleichterung',
 'negotiate': 'verhandeln',
 'prefer': 'bevorzugen',
 'include': 'einbeziehen',
 'neglect': 'vernachlässigen',
 'underestimate': 'unterschätzen',
 'overestimate': 'überschätzen',
 'summarise': 'zusammenfassen',
 'represent': 'vertreten',
 'put forward': 'vorbringen',
 'back up': 'unterstützen; sichern',
 'stand out': 'herausragen',
 'fall through': 'scheitern, platzen',
 'catch up on': 'nachholen',
 'foreseeable': 'absehbar',
 'controversial': 'umstritten',
 'objective': 'sachlich',
 'temporary': 'vorübergehend, befristet',
 'explicitly': 'ausdrücklich',
 'consequently': 'folglich',
 'meanwhile': 'mittlerweile',
 'incentive': 'der Anreiz',
 'intervention': 'der Eingriff',
 'achievement': 'die Errungenschaft',
 'gap': 'die Lücke, das Gefälle',
 'principle': 'der Grundsatz',
 'accountability': 'die Rechenschaftspflicht',
 'reservation': 'der Vorbehalt; die Reservierung',
 'imposition': 'die Zumutung',
 'initiate': 'einleiten',
 'grant': 'gewähren',
 'contest': 'anfechten',
 'reaffirm': 'bekräftigen',
 'exhaust': 'ausschöpfen, erschöpfen',
 'perceive': 'wahrnehmen',
 'illustrate': 'veranschaulichen',
 'clarify': 'verdeutlichen',
 'shed light on': 'beleuchten',
 'put into perspective': 'relativieren',
 'be reflected in': 'sich niederschlagen in',
 'take for granted': 'als selbstverständlich ansehen',
 'live up to': 'gerecht werden',
 'far-fetched': 'abwegig',
 'invalid': 'ungültig',
 'coherent': 'schlüssig',
 'indispensable': 'unabdingbar',
 'in view of': 'angesichts',
 'nonetheless': 'gleichwohl',
 'as a result': 'infolgedessen',
 'demonstrably': 'nachweislich',
 'remedy': 'die Abhilfe',
 'occasion': 'der Anlass',
 'apprehension': 'die Befürchtung',
 'downside': 'die Kehrseite',
 'imbalance': 'das Missverhältnis',
 'leniency': 'die Nachsicht',
 'omission': 'das Versäumnis',
 'restraint': 'die Zurückhaltung',
 'heed': 'beherzigen',
 'condone': 'dulden',
 'forfeit': 'einbüßen',
 'deem': 'erachten',
 'fathom': 'ergründen',
 'evoke': 'hervorrufen',
 'endorse': 'gutheißen',
 'withhold': 'vorenthalten',
 'enshrine': 'verankern',
 'come to a head': 'sich zuspitzen',
 'make sure': 'sich vergewissern',
 'build on': 'anknüpfen an',
 'go along with': 'mitmachen',
 'undisputed': 'unstrittig',
 'deliberate': 'absichtlich',
 'at times': 'bisweilen',
 'henceforth': 'fortan',
 'primarily': 'vorrangig',
 'occasionally': 'gelegentlich',
 'ambivalence': 'die Ambivalenz',
 'anachronism': 'der Anachronismus',
 'composure': 'die Besonnenheit',
 'disdain': 'die Geringschätzung',
 'pipe dream': 'das Hirngespinst',
 'complacency': 'die Selbstgefälligkeit',
 'fallacy': 'der Trugschluss',
 'integrity': 'die Integrität',
 'appease': 'beschwichtigen',
 'stigmatise': 'brandmarken',
 'evade': 'sich entziehen',
 'erode': 'erodieren',
 'conceal': 'verbergen, kaschieren',
 'co-opt': 'vereinnahmen',
 'impose': 'aufzwingen',
 'wear down': 'zermürben',
 'get out of hand': 'ausufern',
 'come to terms with': 'sich abfinden mit',
 'be at odds with': 'im Widerspruch stehen zu',
 'meticulous': 'akribisch',
 'flimsy': 'fadenscheinig',
 'outrageous': 'empörend, hanebüchen',
 'latent': 'latent',
 'perfidious': 'perfide',
 'subtle': 'subtil',
 'irrefutable': 'unwiderlegbar',
 'hesitant': 'zögerlich',
 'in passing': 'beiläufig',
 'truism': 'die Binsenweisheit',
 'U-turn': 'die Kehrtwende',
 'litmus test': 'der Lackmustest',
 'trifle': 'die Lappalie',
 'hotchpotch': 'das Sammelsurium',
 'dig': 'der Seitenhieb',
 'pretext': 'der Vorwand',
 'schadenfreude': 'die Schadenfreude',
 'throw in the towel': 'das Handtuch werfen',
 'buy a pig in a poke': 'die Katze im Sack kaufen',
 'put on the back burner': 'auf die lange Bank schieben',
 "not mince one's words": 'kein Blatt vor den Mund nehmen',
 "put one's cards on the table": 'mit offenen Karten spielen',
 'think outside the box': 'über den Tellerrand schauen',
 'read between the lines': 'zwischen den Zeilen lesen',
 'add fuel to the fire': 'Öl ins Feuer gießen',
 'the elephant in the room': 'das offensichtliche Tabuthema',
 'a blessing in disguise': 'ein Glück im Unglück',
 'let the cat out of the bag': 'die Katze aus dem Sack lassen',
 'once in a blue moon': 'alle Jubeljahre',
 'blasé': 'blasiert',
 'dubious': 'zweifelhaft, dubios',
 'ephemeral': 'vergänglich',
 'laconic': 'lakonisch',
 'pretentious': 'prätentiös',
 'eccentric': 'exzentrisch, verschroben',
 'abandon': 'aufgeben, verlassen',
 'accomplish': 'vollbringen, erreichen',
 'accumulate': 'ansammeln, anhäufen',
 'adjust': 'anpassen, einstellen',
 'admit': 'zugeben, eingestehen',
 'advocate': 'befürworten, sich einsetzen für',
 'afford': 'sich leisten können',
 'alleviate': 'lindern',
 'allocate': 'zuweisen, bereitstellen',
 'alter': 'ändern',
 'amend': 'ändern, berichtigen',
 'anticipate': 'vorhersehen, erwarten',
 'appreciate': 'schätzen, zu schätzen wissen',
 'approve': 'genehmigen, billigen',
 'assign': 'zuweisen, beauftragen',
 'assure': 'versichern, zusichern',
 'attain': 'erreichen, erlangen',
 'attempt': 'versuchen',
 'attribute': 'zuschreiben',
 'blame': 'beschuldigen, die Schuld geben',
 'boost': 'steigern, ankurbeln',
 'broaden': 'erweitern',
 'cease': 'aufhören, einstellen',
 'collaborate': 'zusammenarbeiten',
 'commit': 'sich verpflichten; begehen',
 'compel': 'zwingen',
 'compensate': 'ausgleichen, entschädigen',
 'compile': 'zusammenstellen',
 'comply': 'einhalten, befolgen',
 'comprise': 'umfassen, bestehen aus',
 'concede': 'einräumen, zugestehen',
 'conduct': 'durchführen, leiten',
 'confirm': 'bestätigen',
 'confront': 'konfrontieren, sich stellen',
 'consist': 'bestehen aus',
 'constitute': 'darstellen, bilden',
 'consult': 'konsultieren, sich beraten',
 'convey': 'vermitteln, übermitteln',
 'cope': 'bewältigen, zurechtkommen',
 'correspond': 'entsprechen; korrespondieren',
 'cultivate': 'pflegen, kultivieren',
 'curb': 'eindämmen, zügeln',
 'dedicate': 'widmen',
 'defer': 'aufschieben',
 'delegate': 'delegieren',
 'demonstrate': 'zeigen, nachweisen',
 'denote': 'bezeichnen, bedeuten',
 'deny': 'leugnen, verweigern',
 'depict': 'darstellen, schildern',
 'deploy': 'einsetzen, bereitstellen',
 'derive': 'ableiten, gewinnen',
 'deter': 'abschrecken',
 'devise': 'ersinnen, entwerfen',
 'diminish': 'verringern, abnehmen',
 'disclose': 'offenlegen',
 'discourage': 'entmutigen, abraten',
 'dismiss': 'entlassen; abtun',
 'displace': 'verdrängen, vertreiben',
 'dispose': 'entsorgen',
 'disrupt': 'stören, unterbrechen',
 'diverge': 'auseinandergehen, abweichen',
 'elaborate': 'näher ausführen',
 'eliminate': 'beseitigen',
 'embrace': 'annehmen, begrüßen',
 'encounter': 'begegnen, stoßen auf',
 'endure': 'ertragen, aushalten',
 'enforce': 'durchsetzen',
 'engage': 'beschäftigen; sich beteiligen',
 'enhance': 'verbessern, steigern',
 'ensure': 'sicherstellen, gewährleisten',
 'entail': 'mit sich bringen',
 'establish': 'gründen, festlegen',
 'evolve': 'sich entwickeln',
 'exaggerate': 'übertreiben',
 'exceed': 'überschreiten',
 'exclude': 'ausschließen',
 'exert': 'ausüben',
 'exhibit': 'zeigen, ausstellen',
 'exploit': 'ausbeuten, ausnutzen',
 'expose': 'aussetzen; aufdecken',
 'facilitate': 'erleichtern',
 'foster': 'fördern',
 'fulfil': 'erfüllen',
 'generate': 'erzeugen',
 'govern': 'regieren, bestimmen',
 'handle': 'bewältigen, handhaben',
 'hesitate': 'zögern',
 'hinder': 'behindern',
 'highlight': 'hervorheben',
 'identify': 'identifizieren, erkennen',
 'impair': 'beeinträchtigen',
 'implement': 'umsetzen',
 'incline': 'neigen zu',
 'incorporate': 'einbeziehen, integrieren',
 'indicate': 'hinweisen auf, anzeigen',
 'induce': 'herbeiführen, auslösen',
 'inhibit': 'hemmen',
 'insist': 'bestehen auf',
 'inspire': 'inspirieren',
 'integrate': 'integrieren',
 'interfere': 'sich einmischen, stören',
 'interpret': 'interpretieren, deuten',
 'intervene': 'eingreifen',
 'investigate': 'ermitteln, untersuchen',
 'involve': 'beinhalten, einbeziehen',
 'maintain': 'aufrechterhalten; behaupten',
 'manipulate': 'manipulieren',
 'mitigate': 'mildern, abschwächen',
 'modify': 'modifizieren, ändern',
 'monitor': 'überwachen',
 'obtain': 'erhalten, erlangen',
 'occur': 'vorkommen, auftreten',
 'outline': 'skizzieren, umreißen',
 'oversee': 'beaufsichtigen',
 'overlook': 'übersehen',
 'persist': 'fortbestehen, beharren',
 'persuade': 'überreden',
 'pinpoint': 'genau bestimmen',
 'portray': 'darstellen, porträtieren',
 'preserve': 'bewahren, erhalten',
 'prevail': 'sich durchsetzen, vorherrschen',
 'prevent': 'verhindern',
 'prioritise': 'priorisieren',
 'proceed': 'fortfahren',
 'prohibit': 'verbieten',
 'qualify': 'sich qualifizieren; einschränken',
 'quantify': 'quantifizieren',
 'reassure': 'beruhigen',
 'recall': 'sich erinnern; zurückrufen',
 'reckon': 'schätzen, meinen',
 'recruit': 'anwerben, einstellen',
 'refine': 'verfeinern',
 'reflect': 'widerspiegeln; nachdenken',
 'refrain': 'unterlassen, sich enthalten',
 'regard': 'betrachten als',
 'reinforce': 'verstärken',
 'relieve': 'entlasten, lindern',
 'rely': 'sich verlassen auf',
 'remark': 'bemerken',
 'render': 'machen zu; erbringen',
 'resemble': 'ähneln',
 'restore': 'wiederherstellen',
 'restrict': 'beschränken',
 'retain': 'behalten, bewahren',
 'retrieve': 'abrufen, zurückholen',
 'reveal': 'enthüllen, offenbaren',
 'reverse': 'umkehren',
 'revise': 'überarbeiten',
 'seek': 'suchen, anstreben',
 'settle': 'sich niederlassen; beilegen',
 'simplify': 'vereinfachen',
 'specify': 'festlegen, angeben',
 'strengthen': 'stärken',
 'substitute': 'ersetzen',
 'suffer': 'leiden',
 'supervise': 'beaufsichtigen',
 'supplement': 'ergänzen',
 'suppress': 'unterdrücken',
 'sustain': 'aufrechterhalten',
 'tailor': 'maßschneidern, anpassen',
 'tend': 'neigen, tendieren',
 'terminate': 'beenden, kündigen',
 'transform': 'verwandeln',
 'undergo': 'durchlaufen, sich unterziehen',
 'undertake': 'übernehmen',
 'unveil': 'enthüllen, vorstellen',
 'uphold': 'aufrechterhalten (Prinzip)',
 'urge': 'eindringlich auffordern',
 'utilise': 'nutzen, verwenden',
 'validate': 'validieren, bestätigen',
 'vary': 'variieren',
 'verify': 'überprüfen',
 'weaken': 'schwächen',
 'withdraw': 'zurückziehen, abheben',
 'withstand': 'standhalten',
 'witness': 'bezeugen, miterleben',
 'yield': 'ergeben, liefern; nachgeben',
 'accuracy': 'die Genauigkeit',
 'adversity': 'die Widrigkeit',
 'aftermath': 'die Nachwirkungen (Pl.)',
 'ambiguity': 'die Mehrdeutigkeit',
 'appeal': 'der Reiz; der Einspruch',
 'aspect': 'der Aspekt',
 'awareness': 'das Bewusstsein',
 'backlash': 'die Gegenreaktion',
 'barrier': 'die Barriere, das Hindernis',
 'benchmark': 'der Maßstab, der Richtwert',
 'breakthrough': 'der Durchbruch',
 'burden': 'die Last, die Belastung',
 'capacity': 'die Kapazität',
 'circumstance': 'der Umstand',
 'consensus': 'der Konsens',
 'constraint': 'die Einschränkung',
 'contradiction': 'der Widerspruch',
 'controversy': 'die Kontroverse',
 'conviction': 'die Überzeugung; die Verurteilung',
 'credibility': 'die Glaubwürdigkeit',
 'criterion': 'das Kriterium',
 'discrepancy': 'die Diskrepanz',
 'disparity': 'die Ungleichheit',
 'disruption': 'die Störung, der Umbruch',
 'drawback': 'der Nachteil',
 'efficiency': 'die Effizienz',
 'emphasis': 'die Betonung',
 'endeavour': 'das Bestreben',
 'expertise': 'das Fachwissen, die Expertise',
 'exposure': 'die Exposition, die Sichtbarkeit',
 'feasibility': 'die Machbarkeit',
 'flaw': 'der Fehler, der Mangel',
 'framework': 'der Rahmen',
 'hindrance': 'das Hindernis',
 'implication': 'die Implikation, die Folge',
 'inconsistency': 'die Inkonsistenz',
 'initiative': 'die Initiative',
 'insight': 'die Einsicht, der Einblick',
 'intent': 'die Absicht',
 'interference': 'die Einmischung',
 'leverage': 'der Hebel, der Einfluss',
 'liability': 'die Haftung',
 'likelihood': 'die Wahrscheinlichkeit',
 'magnitude': 'das Ausmaß, die Größenordnung',
 'milestone': 'der Meilenstein',
 'misconception': 'das Missverständnis, der Irrglaube',
 'momentum': 'die Dynamik, der Schwung',
 'motive': 'das Motiv',
 'nuance': 'die Nuance',
 'obligation': 'die Verpflichtung',
 'obstacle': 'das Hindernis',
 'outcome': 'das Ergebnis',
 'outlook': 'die Aussicht, der Ausblick',
 'oversight': 'die Aufsicht; das Versehen',
 'pace': 'das Tempo',
 'pattern': 'das Muster',
 'persistence': 'die Beharrlichkeit',
 'perspective': 'die Perspektive',
 'plausibility': 'die Plausibilität',
 'precedent': 'der Präzedenzfall',
 'preference': 'die Vorliebe, die Präferenz',
 'premise': 'die Prämisse',
 'prevalence': 'die Verbreitung, die Häufigkeit',
 'priority': 'die Priorität',
 'proficiency': 'die Kompetenz, die Fertigkeit',
 'proportion': 'der Anteil, das Verhältnis',
 'prospect': 'die Aussicht',
 'rationale': 'die Begründung',
 'reasoning': 'die Argumentation',
 'reluctance': 'das Widerstreben',
 'remainder': 'der Rest',
 'resilience': 'die Resilienz, die Widerstandskraft',
 'resource': 'die Ressource',
 'scrutiny': 'die genaue Prüfung',
 'setback': 'der Rückschlag',
 'shortcoming': 'der Mangel, das Defizit',
 'significance': 'die Bedeutung',
 'stake': 'der Anteil; das, was auf dem Spiel steht',
 'standpoint': 'der Standpunkt',
 'strain': 'die Belastung, die Anspannung',
 'surplus': 'der Überschuss',
 'threshold': 'die Schwelle',
 'trait': 'das Merkmal, der Wesenszug',
 'transition': 'der Übergang',
 'transparency': 'die Transparenz',
 'trend': 'der Trend',
 'turnover': 'der Umsatz; die Fluktuation',
 'uncertainty': 'die Unsicherheit',
 'urgency': 'die Dringlichkeit',
 'validity': 'die Gültigkeit',
 'viability': 'die Tragfähigkeit',
 'abundant': 'reichlich',
 'accessible': 'zugänglich',
 'accurate': 'genau',
 'adequate': 'angemessen, ausreichend',
 'adverse': 'nachteilig, ungünstig',
 'ambiguous': 'mehrdeutig',
 'apparent': 'offensichtlich, scheinbar',
 'arbitrary': 'willkürlich',
 'beneficial': 'vorteilhaft',
 'biased': 'voreingenommen',
 'competent': 'kompetent',
 'comprehensive': 'umfassend',
 'conclusive': 'schlüssig, eindeutig',
 'consistent': 'konsistent, folgerichtig',
 'conspicuous': 'auffällig',
 'convincing': 'überzeugend',
 'crucial': 'entscheidend',
 'cumbersome': 'umständlich, schwerfällig',
 'demanding': 'anspruchsvoll',
 'detrimental': 'schädlich',
 'diverse': 'vielfältig',
 'eligible': 'berechtigt, infrage kommend',
 'eminent': 'herausragend, bedeutend',
 'essential': 'wesentlich, unerlässlich',
 'evident': 'offenkundig',
 'excessive': 'übermäßig',
 'exhaustive': 'erschöpfend, lückenlos',
 'explicit': 'ausdrücklich, explizit',
 'extensive': 'umfangreich',
 'feasible': 'machbar',
 'flawed': 'fehlerhaft',
 'fluctuating': 'schwankend',
 'fundamental': 'grundlegend',
 'imminent': 'unmittelbar bevorstehend',
 'inadequate': 'unzureichend',
 'inclusive': 'inklusiv',
 'inconsistent': 'widersprüchlich',
 'influential': 'einflussreich',
 'inherent': 'inhärent',
 'innovative': 'innovativ',
 'intricate': 'kompliziert, verwickelt',
 'intriguing': 'faszinierend',
 'irrelevant': 'irrelevant',
 'legitimate': 'legitim, rechtmäßig',
 'mandatory': 'verpflichtend',
 'marginal': 'geringfügig, marginal',
 'misleading': 'irreführend',
 'negligible': 'vernachlässigbar',
 'notable': 'bemerkenswert',
 'noticeable': 'spürbar, merklich',
 'ongoing': 'fortlaufend, laufend',
 'outdated': 'überholt',
 'outstanding': 'herausragend; ausstehend',
 'overwhelming': 'überwältigend',
 'persistent': 'hartnäckig, anhaltend',
 'pervasive': 'allgegenwärtig',
 'plausible': 'plausibel',
 'precise': 'präzise',
 'predominant': 'vorherrschend',
 'preliminary': 'vorläufig',
 'prevalent': 'weit verbreitet',
 'prominent': 'prominent, herausragend',
 'proportional': 'verhältnismäßig',
 'questionable': 'fragwürdig',
 'redundant': 'überflüssig',
 'remarkable': 'bemerkenswert',
 'resilient': 'widerstandsfähig',
 'rigorous': 'streng, gründlich',
 'robust': 'robust',
 'scarce': 'knapp',
 'straightforward': 'unkompliziert',
 'subsequent': 'nachfolgend',
 'substantial': 'beträchtlich',
 'susceptible': 'anfällig',
 'unanimous': 'einstimmig',
 'unbiased': 'unvoreingenommen',
 'unprecedented': 'beispiellos',
 'versatile': 'vielseitig',
 'viable': 'tragfähig, realisierbar',
 'vulnerable': 'verwundbar',
 'widespread': 'weit verbreitet',
 'deliberately': 'absichtlich',
 'inevitably': 'zwangsläufig',
 'notably': 'insbesondere',
 'predominantly': 'überwiegend',
 'substantially': 'erheblich',
 'thereby': 'dadurch',
 'ultimately': 'letztendlich',
 'account for': 'erklären, ausmachen',
 'back down': 'einen Rückzieher machen',
 'bring up': 'zur Sprache bringen; großziehen',
 'call off': 'absagen',
 'cut back on': 'einsparen bei',
 'cut off': 'abschneiden, trennen',
 'draw on': 'zurückgreifen auf',
 'drop out': 'abbrechen, aussteigen',
 'fall behind': 'in Rückstand geraten',
 'follow up': 'nachverfolgen, nachhaken',
 'get by': 'über die Runden kommen',
 'get on with': 'gut auskommen mit; weitermachen',
 'give in': 'nachgeben',
 'go over': 'durchgehen, überprüfen',
 'hold back': 'zurückhalten',
 'hold on': 'warten, festhalten',
 'lay off': 'entlassen',
 'narrow down': 'eingrenzen',
 'opt for': 'sich entscheiden für',
 'pass on': 'weitergeben',
 'phase out': 'schrittweise abschaffen',
 'pick up on': 'mitbekommen, aufgreifen',
 'set out': 'aufbrechen; darlegen',
 'set up': 'einrichten, gründen',
 'step down': 'zurücktreten',
 'stick to': 'sich halten an',
 'sum up': 'zusammenfassen',
 'take on': 'übernehmen; einstellen',
 'take up': 'anfangen (Hobby); einnehmen',
 'albeit': 'wenn auch',
 'all things considered': 'alles in allem',
 'as a matter of fact': 'tatsächlich, eigentlich',
 "as far as I'm concerned": 'was mich betrifft',
 'at the expense of': 'auf Kosten von',
 'be that as it may': 'wie dem auch sei',
 'contrary to': 'im Gegensatz zu',
 'for the sake of': 'um … willen',
 'given that': 'angesichts der Tatsache, dass',
 'hence': 'daher',
 'in light of': 'angesichts',
 'in line with': 'im Einklang mit',
 'in respect of': 'hinsichtlich',
 'in the long run': 'auf lange Sicht',
 'in the wake of': 'im Zuge von, nach',
 'insofar as': 'insofern als',
 'it goes without saying': 'es versteht sich von selbst',
 'let alone': 'geschweige denn',
 'on the grounds that': 'mit der Begründung, dass',
 'on the whole': 'im Großen und Ganzen',
 'provided that': 'vorausgesetzt, dass',
 'regardless of': 'unabhängig von',
 'subject to': 'vorbehaltlich',
 'take into account': 'berücksichtigen',
 'that being said': 'davon abgesehen',
 'thus': 'somit',
 'to a certain extent': 'bis zu einem gewissen Grad',
 'to put it simply': 'einfach ausgedrückt',
 'whereas': 'während, wohingegen',
 'with a view to': 'mit dem Ziel',
 'with regard to': 'in Bezug auf',
 'acumen': 'der Scharfsinn',
 'alacrity': 'die Bereitwilligkeit',
 'antipathy': 'die Abneigung',
 'candour': 'die Offenheit',
 'clout': 'der Einfluss',
 'conundrum': 'das Rätsel',
 'debacle': 'das Debakel',
 'euphemism': 'der Euphemismus',
 'impasse': 'die Sackgasse',
 'predilection': 'die Vorliebe',
 'propensity': 'der Hang, die Neigung',
 'tenacity': 'die Hartnäckigkeit',
 'vicissitudes': 'die Wechselfälle',
 'bolster': 'stärken, stützen',
 'circumvent': 'umgehen',
 'corroborate': 'bestätigen',
 'exacerbate': 'verschärfen',
 'galvanise': 'aufrütteln',
 'mollify': 'besänftigen',
 'obviate': 'erübrigen',
 'placate': 'beschwichtigen',
 'relinquish': 'aufgeben, abtreten',
 'repudiate': 'zurückweisen',
 'stymie': 'behindern',
 'vindicate': 'rechtfertigen',
 'astute': 'scharfsinnig',
 'cogent': 'stichhaltig',
 'commensurate': 'angemessen',
 'disingenuous': 'unaufrichtig',
 'egregious': 'ungeheuerlich',
 'fastidious': 'pingelig',
 'gratuitous': 'unnötig, grundlos',
 'inexorable': 'unaufhaltsam',
 'nebulous': 'vage',
 'perfunctory': 'oberflächlich',
 'tenuous': 'schwach, dürftig',
 'ostensibly': 'angeblich',
 'anathema': 'ein Gräuel',
 'chicanery': 'die Schikane',
 'ennui': 'die Langeweile',
 'hubris': 'die Hybris',
 'largesse': 'die Freigebigkeit',
 'minutiae': 'die Einzelheiten',
 'panacea': 'das Allheilmittel',
 'sycophant': 'der Speichellecker',
 'vitriol': 'die Gehässigkeit',
 'zeitgeist': 'der Zeitgeist',
 'obfuscate': 'verschleiern',
 'prevaricate': 'ausweichen',
 'proselytise': 'missionieren',
 'vacillate': 'schwanken',
 'a double-edged sword': 'ein zweischneidiges Schwert',
 'bark up the wrong tree': 'auf dem Holzweg sein',
 'cut to the chase': 'zur Sache kommen',
 'have an axe to grind': 'ein persönliches Interesse verfolgen',
 'jump on the bandwagon': 'auf den Zug aufspringen',
 'move the goalposts': 'die Spielregeln ändern',
 "play devil's advocate": 'den Advocatus Diaboli spielen',
 'sit on the fence': 'sich nicht festlegen',
 'the tip of the iceberg': 'die Spitze des Eisbergs',
 'throw caution to the wind': 'alle Vorsicht in den Wind schlagen',
 'abstruse': 'abstrus',
 'antediluvian': 'vorsintflutlich',
 'bombastic': 'schwülstig',
 'insouciant': 'unbekümmert',
 'obsequious': 'unterwürfig',
 'pernicious': 'verderblich',
 'quixotic': 'weltfremd, idealistisch',
 'sanctimonious': 'scheinheilig',
 'supercilious': 'hochnäsig',
 'truculent': 'streitlustig',
 'unctuous': 'salbungsvoll',
 'just': 'nur; gerade',
 'other': 'andere',
 'than': 'als',
 'into': 'in … hinein',
 'these': 'diese',
 'well': 'gut; nun',
 'most': 'am meisten',
 'before': 'vor; bevor',
 'many': 'viele',
 'those': 'jene',
 'life': 'das Leben',
 'down': 'hinunter',
 'while': 'während',
 'best': 'am besten',
 'such': 'solch',
 'home': 'das Zuhause',
 'same': 'gleich',
 'both': 'beide',
 'part': 'der Teil',
 'better': 'besser',
 'another': 'ein anderer',
 'next': 'nächste',
 'sure': 'sicher',
 'ever': 'jemals',
 'keep': 'behalten; weitermachen',
 'might': 'könnte',
 'someone': 'jemand',
 'once': 'einmal; einst',
 'group': 'die Gruppe',
 'business': 'das Geschäft',
 'care': 'die Pflege, die Sorgfalt',
 'system': 'das System',
 'anything': 'irgendetwas',
 'case': 'der Fall',
 'point': 'der Punkt',
 'hard': 'schwer; hart',
 'power': 'die Macht, die Kraft',
 'kind': 'die Art',
 'whole': 'ganz',
 'least': 'am wenigsten',
 'within': 'innerhalb',
 'able': 'fähig',
 'early': 'früh',
 'information': 'die Information',
 'local': 'lokal, örtlich',
 'social': 'sozial',
 'court': 'das Gericht',
 'fact': 'die Tatsache',
 'mind': 'der Geist, der Verstand',
 'death': 'der Tod',
 'large': 'groß',
 'several': 'mehrere',
 'along': 'entlang',
 'anyone': 'irgendjemand',
 'else': 'sonst',
 'matter': 'die Angelegenheit',
 'pretty': 'ziemlich; hübsch',
 'idea': 'die Idee',
 'international': 'international',
 'cause': 'die Ursache',
 'human': 'menschlich',
 'community': 'die Gemeinschaft',
 'late': 'spät',
 'watch': 'zuschauen, ansehen',
 'either': 'einer von beiden',
 'deal': 'der Deal, das Geschäft',
 'turn': 'drehen, abbiegen',
 'among': 'unter',
 'development': 'die Entwicklung',
 'media': 'die Medien (Pl.)',
 'phone': 'das Telefon',
 'political': 'politisch',
 'education': 'die Bildung',
 'final': 'letzte, endgültig',
 'former': 'ehemalig',
 'front': 'die Vorderseite',
 'type': 'der Typ',
 'chance': 'die Chance',
 'across': 'über, quer',
 'action': 'die Handlung',
 'clear': 'klar',
 'field': 'das Feld',
 'instead': 'stattdessen',
 'main': 'Haupt-',
 'moment': 'der Moment',
 'road': 'die Straße',
 'town': 'die Kleinstadt',
 'fine': 'gut; fein',
 'force': 'die Kraft',
 'space': 'der Raum; der Weltraum',
 'term': 'der Begriff; die Amtszeit',
 'land': 'das Land',
 'site': 'der Standort',
 'total': 'gesamt',
 'likely': 'wahrscheinlich',
 'military': 'militärisch',
 'personal': 'persönlich',
 'security': 'die Sicherheit',
 'couple': 'das Paar',
 'dead': 'tot',
 'industry': 'die Industrie',
 'online': 'online',
 'sense': 'der Sinn',
 'event': 'das Ereignis',
 'member': 'das Mitglied',
 'sorry': 'es tut mir leid',
 'design': 'das Design',
 'guess': 'raten, vermuten',
 'average': 'durchschnittlich',
 'certain': 'bestimmt; sicher',
 'medical': 'medizinisch',
 'performance': 'die Leistung',
 'director': 'der Direktor',
 'ground': 'der Boden',
 'sound': 'der Klang',
 'official': 'offiziell',
 'production': 'die Produktion',
 'rate': 'die Rate',
 'stuff': 'das Zeug',
 'whatever': 'was auch immer',
 'federal': 'Bundes-',
 'management': 'das Management',
 'step': 'der Schritt',
 'central': 'zentral',
 'forward': 'vorwärts',
 'science': 'die Wissenschaft',
 'trade': 'der Handel',
 'upon': 'auf',
 'various': 'verschiedene',
 'chief': 'der Chef',
 'natural': 'natürlich',
 'property': 'das Eigentum',
 'style': 'der Stil',
 'vote': 'die Stimme',
 'economic': 'wirtschaftlich',
 'title': 'der Titel',
 'article': 'der Artikel',
 'attack': 'der Angriff',
 'decision': 'die Entscheidung',
 'entire': 'gesamt',
 'perhaps': 'vielleicht',
 'release': 'die Veröffentlichung',
 'situation': 'die Situation',
 'council': 'der Rat',
 'cover': 'der Umschlag',
 'election': 'die Wahl',
 'race': 'das Rennen',
 'seem': 'scheinen',
 'simply': 'einfach',
 'staff': 'das Personal',
 'union': 'die Union; die Gewerkschaft',
 'crazy': 'verrückt',
 'loss': 'der Verlust',
 'voice': 'die Stimme',
 'army': 'die Armee',
 'huge': 'riesig',
 'practice': 'die Praxis; die Übung',
 'base': 'die Basis',
 'deep': 'tief',
 'professional': 'professionell',
 'truth': 'die Wahrheit',
 'card': 'die Karte',
 'district': 'der Bezirk',
 'recent': 'kürzlich',
 'straight': 'gerade',
 'growth': 'das Wachstum',
 'officer': 'der Beamte, der Offizier',
 'charge': 'die Gebühr; die Anklage',
 'effect': 'die Wirkung',
 'peace': 'der Frieden',
 'track': 'die Spur; der Titel',
 'weight': 'das Gewicht',
 'addition': 'die Ergänzung',
 'ahead': 'voraus',
 'association': 'der Verein, der Verband',
 'pressure': 'der Druck',
 'capital': 'die Hauptstadt; das Kapital',
 'committee': 'der Ausschuss',
 'beginning': 'der Anfang',
 'campaign': 'die Kampagne',
 'content': 'der Inhalt',
 'credit': 'der Kredit',
 'despite': 'trotz',
 'female': 'weiblich',
 'individual': 'individuell',
 'join': 'beitreten',
 'nearly': 'fast',
 'particular': 'bestimmt, besonders',
 'region': 'die Region',
 'contact': 'der Kontakt',
 'drop': 'fallen lassen',
 'fair': 'fair',
 'link': 'der Link',
 'positive': 'positiv',
 'sale': 'der Verkauf',
 'throughout': 'während, überall in',
 'beyond': 'jenseits',
 'quick': 'schnell',
 'unless': 'es sei denn',
 'agree': 'zustimmen',
 'construction': 'der Bau',
 'justice': 'die Gerechtigkeit',
 'movement': 'die Bewegung',
 'scene': 'die Szene',
 'statement': 'die Aussage',
 'collection': 'die Sammlung',
 'author': 'der Autor',
 'global': 'global',
 'judge': 'der Richter',
 'leader': 'der Anführer',
 'material': 'das Material',
 'nobody': 'niemand',
 'regular': 'regelmäßig',
 'unit': 'die Einheit',
 'annual': 'jährlich',
 'anymore': 'nicht mehr',
 'battle': 'die Schlacht',
 'brain': 'das Gehirn',
 'physical': 'körperlich',
 'rule': 'die Regel',
 'active': 'aktiv',
 'administration': 'die Verwaltung',
 'civil': 'zivil',
 'defence': 'die Verteidigung',
 'independent': 'unabhängig',
 'master': 'der Meister',
 'none': 'keiner',
 'stock': 'der Vorrat; die Aktie',
 'wonder': 'sich fragen',
 'worst': 'am schlimmsten',
 'commercial': 'kommerziell',
 'imagine': 'sich vorstellen',
 'lack': 'der Mangel',
 'multiple': 'mehrere',
 'operation': 'der Betrieb; die Operation',
 'organisation': 'die Organisation',
 'secret': 'das Geheimnis',
 'senior': 'leitend, älter',
 'direct': 'direkt',
 'easily': 'leicht',
 'luck': 'das Glück',
 'damage': 'der Schaden',
 'disease': 'die Krankheit',
 'glad': 'froh',
 'machine': 'die Maschine',
 'basic': 'grundlegend',
 'captain': 'der Kapitän',
 'carry': 'tragen',
 'crime': 'das Verbrechen',
 'effective': 'wirksam',
 'fully': 'vollständig',
 'highly': 'höchst',
 'male': 'männlich',
 'plant': 'die Pflanze; das Werk',
 'reality': 'die Realität',
 'spot': 'die Stelle',
 'worse': 'schlimmer',
 'advice': 'der Rat',
 'award': 'die Auszeichnung',
 'block': 'der Block',
 'broken': 'kaputt',
 'holy': 'heilig',
 'nation': 'die Nation',
 'primary': 'primär',
 'responsible': 'verantwortlich',
 'agency': 'die Agentur',
 'camera': 'die Kamera',
 'cell': 'die Zelle',
 'drug': 'das Medikament; die Droge',
 'economy': 'die Wirtschaft',
 'executive': 'leitend',
 'mass': 'die Masse',
 'mission': 'die Mission',
 'status': 'der Status',
 'trial': 'der Prozess; der Versuch',
 'truly': 'wirklich',
 'activity': 'die Aktivität',
 'complex': 'komplex',
 'division': 'die Abteilung',
 'flight': 'der Flug',
 'heat': 'die Hitze',
 'location': 'der Ort',
 'murder': 'der Mord',
 'actual': 'tatsächlich',
 'channel': 'der Kanal',
 'mobile': 'mobil',
 'powerful': 'mächtig',
 'prior': 'vorherig',
 'protection': 'der Schutz',
 'religious': 'religiös',
 'ride': 'fahren, reiten',
 'royal': 'königlich',
 'serve': 'dienen',
 'speech': 'die Rede',
 'bottom': 'der Boden',
 'famous': 'berühmt',
 'investment': 'die Investition',
 'traditional': 'traditionell',
 'twice': 'zweimal',
 'digital': 'digital',
 'mental': 'geistig',
 'owner': 'der Besitzer',
 'remain': 'bleiben',
 'score': 'der Spielstand',
 'smart': 'klug',
 'surface': 'die Oberfläche',
 'budget': 'das Budget',
 'faith': 'der Glaube',
 'fund': 'der Fonds',
 'generation': 'die Generation',
 'hill': 'der Hügel',
 'profile': 'das Profil',
 'push': 'drücken',
 'seat': 'der Sitz',
 'target': 'das Ziel',
 'gain': 'gewinnen',
 'prime': 'Haupt-',
 'rise': 'steigen',
 'silver': 'silbern',
 'soul': 'die Seele',
 'spread': 'verbreiten',
 'supply': 'das Angebot, die Versorgung',
 'weird': 'seltsam',
 'institute': 'das Institut',
 'option': 'die Option',
 'prison': 'das Gefängnis',
 'somebody': 'jemand',
 'strength': 'die Stärke',
 'correct': 'richtig',
 'indeed': 'tatsächlich',
 'negative': 'negativ',
 'spirit': 'der Geist',
 'till': 'bis',
 'trouble': 'der Ärger',
 'apart': 'getrennt',
 'gift': 'das Geschenk',
 'progress': 'der Fortschritt',
 'shut': 'schließen',
 'wood': 'das Holz; der Wald',
 'background': 'der Hintergrund',
 'birth': 'die Geburt',
 'host': 'der Gastgeber',
 'labour': 'die Arbeit',
 'length': 'die Länge',
 'lucky': 'glücklich',
 'neither': 'keiner von beiden',
 'rare': 'selten',
 'setting': 'die Umgebung; die Einstellung',
 'tough': 'hart',
 'alive': 'lebendig',
 'balance': 'das Gleichgewicht',
 'fellow': 'der Kerl',
 'magic': 'die Magie',
 'request': 'die Anfrage',
 'vehicle': 'das Fahrzeug',
 'wake': 'aufwachen',
 'beauty': 'die Schönheit',
 'conversation': 'das Gespräch',
 'criminal': 'kriminell',
 'farm': 'der Bauernhof',
 'technical': 'technisch',
 'unique': 'einzigartig',
 'variety': 'die Vielfalt',
 'violence': 'die Gewalt',
 'youth': 'die Jugend',
 'edge': 'die Kante',
 'evil': 'böse',
 'forever': 'für immer',
 'injury': 'die Verletzung',
 'lovely': 'schön',
 'magazine': 'die Zeitschrift',
 'parliament': 'das Parlament',
 'somewhere': 'irgendwo',
 'audience': 'das Publikum',
 'core': 'der Kern',
 'description': 'die Beschreibung',
 'excellent': 'ausgezeichnet',
 'guard': 'die Wache',
 'mention': 'erwähnen',
 'nuclear': 'nuklear',
 'presence': 'die Anwesenheit',
 'reaction': 'die Reaktion',
 'shoot': 'schießen',
 'solid': 'fest, solide',
 'classic': 'klassisch',
 'electric': 'elektrisch',
 'emergency': 'der Notfall',
 'entirely': 'völlig',
 'failure': 'das Scheitern',
 'fuel': 'der Kraftstoff',
 'initial': 'anfänglich',
 'kick': 'treten',
 'mail': 'die Post',
 'massive': 'massiv',
 'plenty': 'reichlich',
 'prince': 'der Prinz',
 'proper': 'richtig',
 'regional': 'regional',
 'session': 'die Sitzung',
 'shape': 'die Form',
 'toward': 'in Richtung',
 'upper': 'obere',
 'zone': 'die Zone',
 'anywhere': 'irgendwo',
 'boat': 'das Boot',
 'climate': 'das Klima',
 'discussion': 'die Diskussion',
 'duty': 'die Pflicht',
 'fantastic': 'fantastisch',
 'governor': 'der Gouverneur',
 'industrial': 'industriell',
 'joint': 'gemeinsam',
 'path': 'der Pfad',
 'purchase': 'der Kauf',
 'remove': 'entfernen',
 'steel': 'der Stahl',
 'terrible': 'schrecklich',
 'afraid': 'ängstlich',
 'command': 'der Befehl',
 'crew': 'die Crew',
 'crowd': 'die Menge',
 'enemy': 'der Feind',
 'intelligence': 'die Intelligenz; der Geheimdienst',
 'limit': 'die Grenze',
 'ocean': 'der Ozean',
 'profit': 'der Gewinn',
 'appearance': 'das Aussehen',
 'attorney': 'der Anwalt',
 'debt': 'die Schuld',
 'domestic': 'inländisch; häuslich',
 'historical': 'historisch',
 'honour': 'die Ehre',
 'launch': 'starten',
 'minimum': 'das Minimum',
 'native': 'einheimisch; Mutter-',
 'supreme': 'oberste',
 'update': 'das Update',
 'writer': 'der Schriftsteller',
 'ancient': 'antik',
 'communication': 'die Kommunikation',
 'express': 'Express-',
 'flow': 'der Fluss',
 'hero': 'der Held',
 'illegal': 'illegal',
 'joke': 'der Witz',
 'loan': 'das Darlehen',
 'planet': 'der Planet',
 'soft': 'weich',
 'stuck': 'festgefahren',
 'transport': 'der Transport',
 'applied': 'angewandt',
 'device': 'das Gerät',
 'drama': 'das Drama',
 'entry': 'der Eintrag',
 'golden': 'golden',
 'pool': 'das Becken',
 'schedule': 'der Zeitplan',
 'scientific': 'wissenschaftlich',
 'abuse': 'der Missbrauch',
 'angry': 'wütend',
 'candidate': 'der Kandidat',
 'emotional': 'emotional',
 'hole': 'das Loch',
 'internal': 'intern',
 'liberal': 'liberal',
 'payment': 'die Zahlung',
 'perform': 'ausführen; auftreten',
 'sector': 'der Sektor',
 'strike': 'der Streik',
 'studio': 'das Studio',
 'actor': 'der Schauspieler',
 'advance': 'der Fortschritt',
 'apartment': 'die Wohnung',
 'chain': 'die Kette',
 'confidence': 'das Vertrauen',
 'cute': 'süß',
 'equal': 'gleich',
 'fake': 'gefälscht',
 'finance': 'die Finanzen (Pl.)',
 'identity': 'die Identität',
 'journey': 'die Reise',
 'split': 'teilen',
 'urban': 'städtisch',
 'conflict': 'der Konflikt',
 'corporate': 'Unternehmens-',
 'debate': 'die Debatte',
 'fault': 'der Fehler',
 'fill': 'füllen',
 'pure': 'rein',
 'revenue': 'der Umsatz',
 'strange': 'seltsam',
 'talent': 'das Talent',
 'truck': 'der Lastwagen',
 'coverage': 'die Abdeckung; die Berichterstattung',
 'display': 'die Anzeige',
 'false': 'falsch',
 'incredible': 'unglaublich',
 'ministry': 'das Ministerium',
 'novel': 'der Roman',
 'surgery': 'die Operation',
 'vision': 'die Vision; das Sehvermögen',
 'champion': 'der Meister',
 'crisis': 'die Krise',
 'editor': 'der Redakteur',
 'giant': 'riesig',
 'kingdom': 'das Königreich',
 'mayor': 'der Bürgermeister',
 'minor': 'gering',
 'selection': 'die Auswahl',
 'signal': 'das Signal',
 'stream': 'der Bach; der Strom',
 'struggle': 'der Kampf',
 'theme': 'das Thema',
 'tiny': 'winzig',
 'usual': 'üblich',
 'wave': 'die Welle',
 'alcohol': 'der Alkohol',
 'assembly': 'die Versammlung; die Montage',
 'bright': 'hell',
 'capable': 'fähig',
 'combination': 'die Kombination',
 'conservative': 'konservativ',
 'desire': 'der Wunsch',
 'drunk': 'betrunken',
 'familiar': 'vertraut',
 'guilty': 'schuldig',
 'medium': 'das Medium',
 'unable': 'unfähig',
 'upset': 'aufgebracht',
 'bomb': 'die Bombe',
 'cycle': 'der Zyklus',
 'entertainment': 'die Unterhaltung',
 'extreme': 'extrem',
 'facility': 'die Einrichtung',
 'hang': 'hängen',
 'maximum': 'das Maximum',
 'republic': 'die Republik',
 'territory': 'das Gebiet',
 'aside': 'beiseite',
 'bond': 'die Bindung; die Anleihe',
 'corporation': 'der Konzern',
 'danger': 'die Gefahr',
 'deserve': 'verdienen',
 'gender': 'das Geschlecht',
 'mile': 'die Meile',
 'motion': 'die Bewegung; der Antrag',
 'prize': 'der Preis',
 'resolution': 'der Beschluss; die Auflösung',
 'rural': 'ländlich',
 'typical': 'typisch',
 'universe': 'das Universum',
 'branch': 'der Ast; die Filiale',
 'favour': 'der Gefallen',
 'flag': 'die Flagge',
 'heaven': 'der Himmel',
 'independence': 'die Unabhängigkeit',
 'load': 'die Last',
 'plot': 'die Handlung; das Grundstück',
 'possibility': 'die Möglichkeit',
 'academic': 'akademisch',
 'bunch': 'der Haufen',
 'chemical': 'chemisch',
 'competitive': 'wettbewerbsfähig',
 'diet': 'die Ernährung',
 'item': 'der Gegenstand',
 'lane': 'die Spur',
 'mess': 'das Durcheinander',
 'opposition': 'die Opposition',
 'permanent': 'dauerhaft',
 'pleasure': 'das Vergnügen',
 'scheme': 'das Programm, der Plan',
 'storage': 'die Lagerung',
 'tank': 'der Tank',
 'unlike': 'anders als',
 'yard': 'der Hof',
 'button': 'der Knopf',
 'combat': 'der Kampf',
 'constitution': 'die Verfassung',
 'consumer': 'der Verbraucher',
 'creation': 'die Schöpfung',
 'depression': 'die Depression',
 'employment': 'die Beschäftigung',
 'exclusive': 'exklusiv',
 'expert': 'der Experte',
 'grace': 'die Anmut',
 'importance': 'die Bedeutung',
 'latter': 'letzterer',
 'object': 'das Objekt',
 'personnel': 'das Personal',
 'revolution': 'die Revolution',
 'severe': 'schwer',
 'suppose': 'annehmen',
 'tool': 'das Werkzeug',
 'tournament': 'das Turnier',
 'victim': 'das Opfer',
 'arrest': 'die Festnahme',
 'attend': 'teilnehmen',
 'brilliant': 'brillant',
 'crash': 'der Unfall',
 'depth': 'die Tiefe',
 'deputy': 'der Stellvertreter',
 'electronic': 'elektronisch',
 'error': 'der Fehler',
 'existence': 'die Existenz',
 'expression': 'der Ausdruck',
 'factory': 'die Fabrik',
 'legislation': 'die Gesetzgebung',
 'maintenance': 'die Wartung',
 'manner': 'die Art und Weise',
 'origin': 'der Ursprung',
 'panel': 'das Gremium',
 'personality': 'die Persönlichkeit',
 'retail': 'der Einzelhandel',
 'shame': 'die Schande',
 'surely': 'sicherlich',
 'client': 'der Kunde',
 'constant': 'ständig',
 'dumb': 'dumm',
 'empire': 'das Reich',
 'expansion': 'die Expansion',
 'hide': 'verstecken',
 'weapon': 'die Waffe',
 'anniversary': 'der Jahrestag',
 'broad': 'breit',
 'burn': 'brennen',
 'height': 'die Höhe',
 'hidden': 'versteckt',
 'peak': 'der Gipfel',
 'reform': 'die Reform',
 'respond': 'antworten',
 'retirement': 'der Ruhestand',
 'secondary': 'sekundär',
 'solar': 'Solar-',
 'somehow': 'irgendwie',
 'ultimate': 'letzte, ultimativ',
 'breath': 'der Atem',
 'brief': 'kurz',
 'chest': 'die Brust',
 'decade': 'das Jahrzehnt',
 'destroy': 'zerstören',
 'external': 'extern',
 'grab': 'schnappen',
 'immediate': 'sofortig',
 'licence': 'die Lizenz',
 'principal': 'hauptsächlich',
 'survive': 'überleben',
 'therapy': 'die Therapie',
 'childhood': 'die Kindheit',
 'clinical': 'klinisch',
 'comedy': 'die Komödie',
 'defeat': 'die Niederlage',
 'democracy': 'die Demokratie',
 'plastic': 'das Plastik',
 'suspect': 'der Verdächtige',
 'swear': 'schwören; fluchen',
 'wealth': 'der Reichtum',
 'wise': 'weise',
 'approval': 'die Genehmigung',
 'contain': 'enthalten',
 'gang': 'die Bande',
 'graduate': 'der Absolvent',
 'inner': 'innere',
 'neighbourhood': 'die Nachbarschaft',
 'operate': 'betreiben',
 'permission': 'die Erlaubnis',
 'reply': 'die Antwort',
 'shoulder': 'die Schulter',
 'visual': 'visuell',
 'barely': 'kaum',
 'cabinet': 'das Kabinett; der Schrank',
 'coal': 'die Kohle',
 'criticism': 'die Kritik',
 'gallery': 'die Galerie',
 'highway': 'die Autobahn',
 'hunt': 'jagen',
 'inch': 'der Zoll',
 'junior': 'Junior-',
 'jury': 'die Jury',
 'monster': 'das Monster',
 'philosophy': 'die Philosophie',
 'pride': 'der Stolz',
 'rough': 'grob; rau',
 'settlement': 'die Siedlung; der Vergleich',
 'speaker': 'der Redner',
 'tone': 'der Ton',
 'vast': 'riesig',
 'meal': 'die Mahlzeit',
 'pocket': 'die Tasche',
 'regardless': 'trotzdem',
 'relative': 'relativ; der Verwandte',
 'rescue': 'die Rettung',
 'rush': 'eilen',
 'sharp': 'scharf',
 'stable': 'stabil',
 'trick': 'der Trick',
 'bone': 'der Knochen',
 'chamber': 'die Kammer',
 'chart': 'das Diagramm',
 'circuit': 'der Schaltkreis',
 'defend': 'verteidigen',
 'gate': 'das Tor',
 'harm': 'der Schaden',
 'household': 'der Haushalt',
 'impressive': 'beeindruckend',
 'lesson': 'die Lektion',
 'proposal': 'der Vorschlag',
 'province': 'die Provinz',
 'reputation': 'der Ruf',
 'adventure': 'das Abenteuer',
 'atmosphere': 'die Atmosphäre',
 'awful': 'schrecklich',
 'belief': 'der Glaube',
 'elsewhere': 'anderswo',
 'founder': 'der Gründer',
 'gear': 'der Gang; die Ausrüstung',
 'loose': 'locker',
 'offensive': 'offensiv; beleidigend',
 'package': 'das Paket',
 'poverty': 'die Armut',
 'qualified': 'qualifiziert',
 'ridiculous': 'lächerlich',
 'sensitive': 'empfindlich',
 'shock': 'der Schock',
 'silence': 'die Stille',
 'soldier': 'der Soldat',
 'superior': 'überlegen',
 'violent': 'gewalttätig',
 'acid': 'die Säure',
 'administrative': 'administrativ',
 'anxiety': 'die Angst',
 'castle': 'die Burg',
 'charity': 'die Wohltätigkeit',
 'discovery': 'die Entdeckung',
 'encourage': 'ermutigen',
 'formal': 'formell',
 'innocent': 'unschuldig',
 'mystery': 'das Rätsel',
 'palace': 'der Palast',
 'penalty': 'die Strafe',
 'protest': 'der Protest',
 'refer': 'verweisen',
 'silent': 'still',
 'temple': 'der Tempel',
 'trail': 'der Pfad',
 'unusual': 'ungewöhnlich',
 'assault': 'der Angriff',
 'badly': 'schlecht',
 'bath': 'das Bad',
 'chase': 'jagen',
 'concrete': 'konkret; Beton-',
 'fiction': 'die Fiktion',
 'horrible': 'schrecklich',
 'ideal': 'ideal',
 'legend': 'die Legende',
 'muscle': 'der Muskel',
 'passion': 'die Leidenschaft',
 'producer': 'der Produzent',
 'shadow': 'der Schatten',
 'wage': 'der Lohn',
 'avenue': 'die Allee',
 'confident': 'selbstbewusst',
 'custom': 'der Brauch',
 'electricity': 'der Strom',
 'horror': 'der Schrecken',
 'naked': 'nackt',
 'plain': 'schlicht',
 'rear': 'hintere',
 'romantic': 'romantisch',
 'strategic': 'strategisch',
 'welfare': 'das Wohlergehen',
 'wire': 'der Draht',
 'worker': 'der Arbeiter',
 'assist': 'unterstützen',
 'behalf': 'im Namen von',
 'capture': 'erfassen, fangen',
 'ceremony': 'die Zeremonie',
 'efficient': 'effizient',
 'establishment': 'die Einrichtung',
 'ghost': 'das Gespenst',
 'newly': 'neu',
 'ordinary': 'gewöhnlich',
 'participate': 'teilnehmen',
 'prayer': 'das Gebet',
 'soil': 'der Boden',
 'stomach': 'der Magen',
 'ugly': 'hässlich',
 'comfort': 'der Komfort',
 'crack': 'der Riss',
 'dramatic': 'dramatisch',
 'dust': 'der Staub',
 'evolution': 'die Evolution',
 'inspiration': 'die Inspiration',
 'remote': 'abgelegen',
 'steal': 'stehlen',
 'alliance': 'das Bündnis',
 'crystal': 'der Kristall',
 'decent': 'anständig',
 'desert': 'die Wüste',
 'downtown': 'die Innenstadt',
 'insane': 'wahnsinnig',
 'layer': 'die Schicht',
 'marry': 'heiraten',
 'nowhere': 'nirgendwo',
 'organic': 'biologisch',
 'poetry': 'die Poesie',
 'pray': 'beten',
 'smooth': 'glatt',
 'spiritual': 'spirituell',
 'string': 'die Schnur',
 'sudden': 'plötzlich',
 'abroad': 'im Ausland',
 'bother': 'stören',
 'citizen': 'der Bürger',
 'compete': 'konkurrieren',
 'disaster': 'die Katastrophe',
 'equally': 'gleichermaßen',
 'intense': 'intensiv',
 'lifetime': 'die Lebenszeit',
 'liquid': 'die Flüssigkeit',
 'medal': 'die Medaille',
 'mortgage': 'die Hypothek',
 'narrative': 'die Erzählung',
 'reduction': 'die Verringerung',
 'silly': 'albern',
 'translation': 'die Übersetzung',
 'visible': 'sichtbar',
 'amendment': 'die Änderung',
 'angle': 'der Winkel',
 'enterprise': 'das Unternehmen',
 'passenger': 'der Fahrgast',
 'possession': 'der Besitz',
 'rapid': 'schnell',
 'resident': 'der Bewohner',
 'suitable': 'geeignet',
 'vital': 'lebenswichtig',
 'whilst': 'während',
 'agriculture': 'die Landwirtschaft',
 'commerce': 'der Handel',
 'currency': 'die Währung',
 'exhibition': 'die Ausstellung',
 'fraud': 'der Betrug',
 'funeral': 'die Beerdigung',
 'genuine': 'echt',
 'hook': 'der Haken',
 'remind': 'erinnern',
 'resort': 'der Ferienort',
 'routine': 'die Routine',
 'scary': 'gruselig',
 'spell': 'buchstabieren',
 'survival': 'das Überleben',
 'tongue': 'die Zunge',
 'asleep': 'schlafend',
 'automatic': 'automatisch',
 'consent': 'die Zustimmung',
 'destruction': 'die Zerstörung',
 'divorce': 'die Scheidung',
 'extraordinary': 'außergewöhnlich',
 'fate': 'das Schicksal',
 'glory': 'der Ruhm',
 'headquarters': 'die Zentrale',
 'heritage': 'das Erbe',
 'landscape': 'die Landschaft',
 'logic': 'die Logik',
 'privacy': 'die Privatsphäre',
 'residence': 'der Wohnsitz',
 'ambassador': 'der Botschafter',
 'consumption': 'der Verbrauch',
 'fancy': 'schick',
 'gorgeous': 'wunderschön',
 'grateful': 'dankbar',
 'impression': 'der Eindruck',
 'knock': 'klopfen',
 'leather': 'das Leder',
 'luxury': 'der Luxus',
 'ought to': 'sollte',
 'poll': 'die Umfrage',
 'removal': 'die Entfernung',
 'reporter': 'der Reporter',
 'stretch': 'dehnen',
 'absence': 'die Abwesenheit',
 'fame': 'der Ruhm',
 'flood': 'die Überschwemmung',
 'genetic': 'genetisch',
 'instant': 'sofortig',
 'liberty': 'die Freiheit',
 'progressive': 'fortschrittlich',
 'representation': 'die Vertretung',
 'swing': 'schwingen',
 'twin': 'der Zwilling',
 'column': 'die Spalte',
 'compensation': 'die Entschädigung',
 'conservation': 'der Naturschutz',
 'difficulty': 'die Schwierigkeit',
 'fleet': 'die Flotte',
 'genius': 'das Genie',
 'guidance': 'die Anleitung',
 'intention': 'die Absicht',
 'mechanical': 'mechanisch',
 'precious': 'kostbar',
 'premium': 'Premium-',
 'pretend': 'so tun als ob',
 'priest': 'der Priester',
 'radical': 'radikal',
 'residential': 'Wohn-',
 'reward': 'die Belohnung',
 'shake': 'schütteln',
 'shore': 'das Ufer',
 'transmission': 'die Übertragung; das Getriebe',
 'trap': 'die Falle',
 'wildlife': 'die Tierwelt',
 'wooden': 'hölzern',
 'blast': 'die Explosion',
 'cure': 'die Heilung',
 'desperate': 'verzweifelt',
 'diversity': 'die Vielfalt',
 'faculty': 'die Fakultät',
 'frozen': 'gefroren',
 'humanity': 'die Menschheit',
 'manual': 'manuell',
 'painful': 'schmerzhaft',
 'preparation': 'die Vorbereitung',
 'punch': 'der Schlag',
 'romance': 'die Romanze',
 'tissue': 'das Gewebe; das Taschentuch',
 'virtual': 'virtuell',
 'biological': 'biologisch',
 'bite': 'beißen',
 'disorder': 'die Störung',
 'footage': 'das Filmmaterial',
 'grave': 'das Grab',
 'laboratory': 'das Labor',
 'literary': 'literarisch',
 'mask': 'die Maske',
 'midnight': 'die Mitternacht',
 'praise': 'das Lob',
 'psychology': 'die Psychologie',
 'relation': 'die Beziehung',
 'ruin': 'die Ruine',
 'slave': 'der Sklave',
 'stability': 'die Stabilität',
 'steady': 'stetig',
 'symbol': 'das Symbol',
 'treaty': 'der Vertrag',
 'unlikely': 'unwahrscheinlich',
 'affair': 'die Angelegenheit; die Affäre',
 'agenda': 'die Tagesordnung',
 'craft': 'das Handwerk',
 'edit': 'bearbeiten',
 'equity': 'das Eigenkapital; die Gerechtigkeit',
 'fortune': 'das Vermögen; das Glück',
 'intellectual': 'intellektuell',
 'involvement': 'die Beteiligung',
 'partly': 'teilweise',
 'phrase': 'die Wendung',
 'racial': 'rassistisch, Rassen-',
 'regime': 'das Regime',
 'seal': 'das Siegel; die Robbe',
 'shield': 'der Schild',
 'summit': 'der Gipfel',
 'throat': 'der Hals',
 'wisdom': 'die Weisheit',
 'alien': 'der Außerirdische',
 'awkward': 'unbeholfen',
 'beast': 'das Biest',
 'carrier': 'der Träger',
 'celebrity': 'der Promi',
 'default': 'der Standard',
 'dialogue': 'der Dialog',
 'execution': 'die Hinrichtung; die Ausführung',
 'fool': 'der Narr',
 'intelligent': 'intelligent',
 'loop': 'die Schleife',
 'overseas': 'in Übersee',
 'recover': 'sich erholen',
 'sacrifice': 'das Opfer',
 'sole': 'einzig',
 'tale': 'das Märchen',
 'worship': 'die Anbetung',
 'worthy': 'würdig',
 'alarm': 'der Alarm',
 'dependent': 'abhängig',
 'dual': 'doppelt',
 'filter': 'der Filter',
 'globe': 'der Globus',
 'mature': 'reif',
 'peaceful': 'friedlich',
 'pump': 'pumpen',
 'revenge': 'die Rache',
 'slip': 'ausrutschen',
 'spare': 'Ersatz-',
 'specialist': 'der Spezialist',
 'stranger': 'der Fremde',
 'volunteer': 'der Freiwillige',
 'acceptable': 'akzeptabel',
 'auction': 'die Auktion',
 'chaos': 'das Chaos',
 'concentration': 'die Konzentration',
 'dawn': 'die Morgendämmerung',
 'earnings': 'die Einnahmen (Pl.)',
 'frequent': 'häufig',
 'hilarious': 'urkomisch',
 'margin': 'der Rand; die Marge',
 'moderate': 'gemäßigt',
 'passage': 'die Passage',
 'quest': 'die Suche',
 'stroke': 'der Schlaganfall; der Schlag',
 'stunning': 'atemberaubend',
 'utility': 'der Nutzen; der Versorger',
 'vessel': 'das Schiff; das Gefäß',
 'wherever': 'wo auch immer',
 'announce': 'ankündigen',
 'bold': 'mutig',
 'conspiracy': 'die Verschwörung',
 'equality': 'die Gleichheit',
 'fiscal': 'fiskalisch',
 'guardian': 'der Vormund',
 'homeless': 'obdachlos',
 'mainstream': 'Mainstream-',
 'oral': 'mündlich',
 'panic': 'die Panik',
 'segment': 'das Segment',
 'spectrum': 'das Spektrum',
 'terror': 'der Terror',
 'venture': 'das Unternehmen',
 'conventional': 'herkömmlich',
 'emperor': 'der Kaiser',
 'enormous': 'enorm',
 'forgive': 'vergeben',
 'lonely': 'einsam',
 'mercy': 'die Gnade',
 'outer': 'äußere',
 'oxygen': 'der Sauerstoff',
 'pipe': 'das Rohr',
 'powder': 'das Pulver',
 'rude': 'unhöflich',
 'shelter': 'die Unterkunft',
 'sooner': 'früher',
 'tribute': 'die Hommage',
 'trigger': 'der Auslöser',
 'venue': 'der Veranstaltungsort',
 'artificial': 'künstlich',
 'beneath': 'unter',
 'bullet': 'die Kugel',
 'conversion': 'die Umwandlung',
 'destination': 'das Ziel',
 'dirt': 'der Schmutz',
 'divine': 'göttlich',
 'functional': 'funktional',
 'gather': 'sammeln',
 'municipal': 'städtisch',
 'noble': 'edel',
 'relate': 'in Beziehung setzen',
 'sacred': 'heilig',
 'suspension': 'die Suspendierung',
 'toxic': 'giftig',
 'tunnel': 'der Tunnel',
 'upgrade': 'das Upgrade',
 'brush': 'die Bürste',
 'casual': 'lässig',
 'certified': 'zertifiziert',
 'chef': 'der Koch',
 'civilian': 'zivil',
 'coalition': 'die Koalition',
 'essay': 'der Aufsatz',
 'expense': 'die Ausgabe',
 'invasion': 'die Invasion',
 'maker': 'der Hersteller',
 'outdoor': 'im Freien',
 'recipe': 'das Rezept',
 'strict': 'streng',
 'substance': 'die Substanz',
 'suggestion': 'der Vorschlag',
 'unexpected': 'unerwartet',
 'usage': 'der Gebrauch',
 'amateur': 'der Amateur',
 'explosion': 'die Explosion',
 'imagination': 'die Vorstellungskraft',
 'leaf': 'das Blatt',
 'lightning': 'der Blitz',
 'nasty': 'ekelhaft',
 'pension': 'die Rente',
 'permit': 'die Genehmigung',
 'pleasant': 'angenehm',
 'portrait': 'das Porträt',
 'productive': 'produktiv',
 'slight': 'leicht',
 'tension': 'die Spannung',
 'twist': 'die Wendung',
 'unity': 'die Einheit',
 'useless': 'nutzlos',
 'bitter': 'bitter',
 'clinic': 'die Klinik',
 'continuous': 'kontinuierlich',
 'detective': 'der Detektiv',
 'disability': 'die Behinderung',
 'excess': 'der Überschuss',
 'fence': 'der Zaun',
 'gravity': 'die Schwerkraft',
 'identical': 'identisch',
 'nonsense': 'der Unsinn',
 'scientist': 'der Wissenschaftler',
 'slavery': 'die Sklaverei',
 'transaction': 'die Transaktion',
 'veteran': 'der Veteran',
 'wealthy': 'wohlhabend',
 'attract': 'anziehen',
 'communicate': 'kommunizieren',
 'depend': 'abhängen',
 'dose': 'die Dosis',
 'generous': 'großzügig',
 'loyal': 'treu',
 'occupation': 'der Beruf; die Besetzung',
 'opponent': 'der Gegner',
 'prisoner': 'der Gefangene',
 'resist': 'widerstehen',
 'wrap': 'einwickeln',
 'blade': 'die Klinge',
 'cargo': 'die Fracht',
 'distant': 'entfernt',
 'emotion': 'das Gefühl',
 'excitement': 'die Aufregung',
 'nightmare': 'der Albtraum',
 'overnight': 'über Nacht',
 'uncomfortable': 'unbequem',
 'assignment': 'die Aufgabe',
 'bare': 'nackt',
 'cancel': 'absagen',
 'clue': 'der Hinweis',
 'collapse': 'zusammenbrechen',
 'conscious': 'bewusst',
 'consecutive': 'aufeinanderfolgend',
 'endless': 'endlos',
 'grain': 'das Getreide',
 'patent': 'das Patent',
 'rival': 'der Rivale',
 'unnecessary': 'unnötig',
 'anonymous': 'anonym',
 'beloved': 'geliebt',
 'contrary': 'gegenteilig',
 'decrease': 'die Abnahme',
 'gentle': 'sanft',
 'lease': 'der Mietvertrag',
 'loyalty': 'die Treue',
 'mysterious': 'geheimnisvoll',
 'propaganda': 'die Propaganda',
 'scandal': 'der Skandal',
 'testimony': 'die Zeugenaussage',
 'treasure': 'der Schatz',
 'unfair': 'unfair',
 'acceptance': 'die Akzeptanz',
 'creature': 'das Geschöpf',
 'deadly': 'tödlich',
 'determination': 'die Entschlossenheit',
 'infinite': 'unendlich',
 'politician': 'der Politiker',
 'react': 'reagieren',
 'realistic': 'realistisch',
 'satisfaction': 'die Zufriedenheit',
 'shade': 'der Schatten',
 'vocal': 'stimmlich; lautstark',
 'admission': 'die Zulassung; der Eintritt',
 'convenient': 'bequem',
 'crop': 'die Ernte',
 'earthquake': 'das Erdbeben',
 'elderly': 'älter',
 'scholarship': 'das Stipendium',
 'torture': 'die Folter',
 'urgent': 'dringend',
 'vertical': 'senkrecht',
 'wallet': 'die Brieftasche',
 'accent': 'der Akzent',
 'awake': 'wach',
 'blank': 'leer',
 'corrupt': 'korrupt',
 'curve': 'die Kurve',
 'duration': 'die Dauer',
 'harsh': 'hart',
 'immune': 'immun',
 'instruction': 'die Anweisung',
 'invitation': 'die Einladung',
 'judicial': 'gerichtlich',
 'logical': 'logisch',
 'peer': 'der Gleichaltrige',
 'provision': 'die Bestimmung; die Bereitstellung',
 'trauma': 'das Trauma',
 'acquire': 'erwerben',
 'boundary': 'die Grenze',
 'breach': 'der Verstoß',
 'combine': 'kombinieren',
 'companion': 'der Begleiter',
 'consciousness': 'das Bewusstsein',
 'courtesy': 'die Höflichkeit',
 'disc': 'die Scheibe',
 'embassy': 'die Botschaft',
 'goodness': 'die Güte',
 'guilt': 'die Schuld',
 'haven': 'der Zufluchtsort',
 'keen': 'eifrig',
 'lesser': 'geringer',
 'mere': 'bloß',
 'miracle': 'das Wunder',
 'protective': 'schützend',
 'publisher': 'der Verlag',
 'retreat': 'der Rückzug',
 'theft': 'der Diebstahl',
 'valve': 'das Ventil',
 'adjacent': 'angrenzend',
 'appreciation': 'die Wertschätzung',
 'athletic': 'sportlich',
 'banner': 'das Banner',
 'charm': 'der Charme',
 'colony': 'die Kolonie',
 'cruel': 'grausam',
 'curriculum': 'der Lehrplan',
 'electoral': 'Wahl-',
 'entity': 'die Einheit, das Gebilde',
 'interface': 'die Schnittstelle',
 'journalism': 'der Journalismus',
 'occasional': 'gelegentlich',
 'pursuit': 'die Verfolgung, das Streben',
 'ridge': 'der Grat',
 'tribe': 'der Stamm',
 'unfortunate': 'bedauerlich',
 'alternate': 'abwechselnd',
 'athlete': 'der Athlet',
 'attraction': 'die Anziehung',
 'bankruptcy': 'die Insolvenz',
 'closure': 'die Schließung',
 'cognitive': 'kognitiv',
 'dental': 'Zahn-',
 'diplomatic': 'diplomatisch',
 'editorial': 'redaktionell',
 'eternal': 'ewig',
 'freeze': 'frieren',
 'grip': 'der Griff',
 'handful': 'die Handvoll',
 'happily': 'glücklich',
 'harmony': 'die Harmonie',
 'humble': 'bescheiden',
 'hybrid': 'hybrid',
 'mild': 'mild',
 'minimal': 'minimal',
 'molecular': 'molekular',
 'nowadays': 'heutzutage',
 'pathetic': 'erbärmlich',
 'restoration': 'die Restaurierung',
 'selfish': 'egoistisch',
 'throne': 'der Thron',
 'archives': 'das Archiv',
 'brutal': 'brutal',
 'cliff': 'die Klippe',
 'declaration': 'die Erklärung',
 'distinction': 'die Unterscheidung',
 'faithful': 'treu',
 'fatal': 'tödlich',
 'fitting': 'passend',
 'hurricane': 'der Hurrikan',
 'jurisdiction': 'die Zuständigkeit',
 'lung': 'die Lunge',
 'mighty': 'mächtig',
 'monetary': 'monetär',
 'nutrition': 'die Ernährung',
 'poorly': 'schlecht',
 'pose': 'darstellen',
 'pour': 'gießen',
 'anxious': 'ängstlich',
 'cult': 'der Kult',
 'diary': 'das Tagebuch',
 'disagree': 'widersprechen',
 'forecast': 'die Vorhersage',
 'indoor': 'Innen-',
 'intend': 'beabsichtigen',
 'invisible': 'unsichtbar',
 'lawsuit': 'die Klage',
 'leak': 'das Leck',
 'passionate': 'leidenschaftlich',
 'recommendation': 'die Empfehlung',
 'riot': 'der Aufruhr',
 'servant': 'der Diener',
 'skull': 'der Schädel',
 'smash': 'zerschlagen',
 'statue': 'die Statue',
 'surrender': 'die Kapitulation',
 'suspicious': 'verdächtig',
 'tender': 'zärtlich',
 'vacuum': 'das Vakuum',
 'breed': 'die Rasse',
 'bride': 'die Braut',
 'confirmation': 'die Bestätigung',
 'contractor': 'der Auftragnehmer',
 'diameter': 'der Durchmesser',
 'fabric': 'der Stoff',
 'fabulous': 'fabelhaft',
 'fold': 'falten',
 'glorious': 'glorreich',
 'merchant': 'der Händler',
 'merit': 'der Verdienst',
 'myth': 'der Mythos',
 'pale': 'blass',
 'poison': 'das Gift',
 'rebel': 'der Rebell',
 'rotation': 'die Drehung',
 'toll': 'die Maut; der Tribut',
 'torn': 'zerrissen',
 'unbelievable': 'unglaublich',
 'underneath': 'unterhalb',
 'variation': 'die Variation',
 'viral': 'viral',
 'warehouse': 'das Lager',
 'widow': 'die Witwe',
 'altogether': 'insgesamt',
 'beard': 'der Bart',
 'blanket': 'die Decke',
 'capability': 'die Fähigkeit',
 'curse': 'der Fluch',
 'drain': 'der Abfluss',
 'excellence': 'die Exzellenz',
 'flame': 'die Flamme',
 'hint': 'der Hinweis',
 'horizon': 'der Horizont',
 'hostile': 'feindselig',
 'miserable': 'elend',
 'nest': 'das Nest',
 'nomination': 'die Nominierung',
 'quantity': 'die Menge',
 'reign': 'die Herrschaft',
 'scare': 'erschrecken',
 'span': 'die Spanne',
 'submission': 'die Einreichung',
 'supporter': 'der Unterstützer',
 'tremendous': 'enorm',
 'ashamed': 'beschämt',
 'ballot': 'der Stimmzettel',
 'cemetery': 'der Friedhof',
 'cheat': 'betrügen',
 'compact': 'der Pakt',
 'deficit': 'das Defizit',
 'halfway': 'auf halbem Weg',
 'indication': 'der Hinweis',
 'intensive': 'intensiv',
 'intimate': 'intim',
 'martial': 'kriegerisch',
 'prosecution': 'die Strafverfolgung',
 'pulse': 'der Puls',
 'rational': 'rational',
 'realm': 'das Reich',
 'rope': 'das Seil',
 'shout': 'schreien',
 'spectacular': 'spektakulär',
 'streak': 'die Serie, die Strähne',
 'subscription': 'das Abonnement',
 'technological': 'technologisch',
 'tolerance': 'die Toleranz',
 'unhappy': 'unglücklich',
 'apology': 'die Entschuldigung',
 'exceptional': 'außergewöhnlich',
 'hack': 'hacken',
 'hatred': 'der Hass',
 'interact': 'interagieren',
 'majesty': 'die Majestät',
 'retire': 'in Rente gehen',
 'rhythm': 'der Rhythmus',
 'savage': 'wild',
 'slim': 'schlank',
 'someday': 'eines Tages',
 'stack': 'der Stapel',
 'stance': 'die Haltung',
 'supportive': 'unterstützend',
 'surgical': 'chirurgisch',
 'tide': 'die Gezeiten (Pl.)',
 'warfare': 'die Kriegsführung',
 'authentic': 'authentisch',
 'bolt': 'der Bolzen',
 'collar': 'der Kragen',
 'donate': 'spenden',
 'finale': 'das Finale',
 'flavour': 'der Geschmack',
 'ignorance': 'die Unwissenheit',
 'immigrant': 'der Einwanderer',
 'intermediate': 'mittlere',
 'invention': 'die Erfindung',
 'magnificent': 'prächtig',
 'mathematical': 'mathematisch',
 'placement': 'die Platzierung; das Praktikum',
 'recreation': 'die Erholung',
 'shallow': 'seicht',
 'sketch': 'die Skizze',
 'spite': 'die Bosheit',
 'sponsor': 'der Sponsor',
 'sunset': 'der Sonnenuntergang',
 'thermal': 'thermisch',
 'chapel': 'die Kapelle',
 'cloth': 'das Tuch',
 'differ': 'sich unterscheiden',
 'elect': 'wählen',
 'essence': 'das Wesen',
 'harvest': 'die Ernte',
 'headline': 'die Schlagzeile',
 'junk': 'der Kram',
 'kidney': 'die Niere',
 'ladder': 'die Leiter',
 'lobby': 'die Lobby',
 'mineral': 'das Mineral',
 'modest': 'bescheiden',
 'orbit': 'die Umlaufbahn',
 'paragraph': 'der Absatz',
 'passive': 'passiv',
 'peninsula': 'die Halbinsel',
 'profitable': 'profitabel',
 'sentiment': 'die Stimmung',
 'trunk': 'der Stamm; der Kofferraum',
 'varied': 'abwechslungsreich',
 'verdict': 'das Urteil',
 'anchor': 'der Anker',
 'arch': 'der Bogen',
 'badge': 'das Abzeichen',
 'bizarre': 'bizarr',
 'bounce': 'abprallen',
 'consultation': 'die Beratung',
 'continental': 'kontinental',
 'convenience': 'die Bequemlichkeit',
 'dignity': 'die Würde',
 'enthusiasm': 'die Begeisterung',
 'ferry': 'die Fähre',
 'fusion': 'die Fusion',
 'helmet': 'der Helm',
 'inclusion': 'die Einbeziehung',
 'keeper': 'der Hüter; der Torwart',
 'liar': 'der Lügner',
 'machinery': 'die Maschinen (Pl.)',
 'mansion': 'die Villa',
 'possess': 'besitzen',
 'probability': 'die Wahrscheinlichkeit',
 'ritual': 'das Ritual',
 'slam': 'zuschlagen',
 'subscribe': 'abonnieren',
 'voltage': 'die Spannung',
 'width': 'die Breite',
 'workout': 'das Training',
 'bail': 'die Kaution',
 'delicate': 'zart',
 'disappointment': 'die Enttäuschung',
 'insert': 'einfügen',
 'loser': 'der Verlierer',
 'massage': 'die Massage',
 'musician': 'der Musiker',
 'orchestra': 'das Orchester',
 'precision': 'die Präzision',
 'preservation': 'die Erhaltung',
 'sail': 'segeln',
 'sheer': 'rein',
 'stark': 'krass',
 'sympathy': 'das Mitgefühl',
 'thumb': 'der Daumen',
 'timber': 'das Holz',
 'transparent': 'transparent',
 'upside': 'der Vorteil',
 'visitor': 'der Besucher',
 'vitamin': 'das Vitamin',
 'void': 'die Leere',
 'voluntary': 'freiwillig',
 'wheat': 'der Weizen',
 'wipe': 'wischen',
 'wrist': 'das Handgelenk',
 'acute': 'akut',
 'behave': 'sich benehmen',
 'chin': 'das Kinn',
 'civic': 'bürgerlich',
 'clerk': 'der Sachbearbeiter',
 'cottage': 'das Häuschen',
 'coup': 'der Putsch',
 'crude': 'roh',
 'disposal': 'die Entsorgung',
 'distinctive': 'unverwechselbar',
 'donation': 'die Spende',
 'drone': 'die Drohne',
 'indirect': 'indirekt',
 'institutional': 'institutionell',
 'interim': 'vorläufig',
 'lottery': 'die Lotterie',
 'outlet': 'die Steckdose; die Verkaufsstelle',
 'pledge': 'das Versprechen',
 'portal': 'das Portal',
 'publicity': 'die Öffentlichkeit',
 'puppy': 'der Welpe',
 'slice': 'die Scheibe',
 'survivor': 'der Überlebende',
 'vaccine': 'der Impfstoff',
 'affiliate': 'das Partnerunternehmen',
 'asylum': 'das Asyl',
 'barn': 'die Scheune',
 'bent': 'gebogen',
 'cathedral': 'der Dom',
 'clause': 'die Klausel',
 'cluster': 'der Cluster',
 'consistency': 'die Konsistenz',
 'dancer': 'der Tänzer',
 'deaf': 'taub',
 'denial': 'die Leugnung',
 'dock': 'das Dock',
 'entrepreneur': 'der Unternehmer',
 'expedition': 'die Expedition',
 'feat': 'die Leistung',
 'fossil': 'das Fossil',
 'freight': 'die Fracht',
 'honesty': 'die Ehrlichkeit',
 'inappropriate': 'unangemessen',
 'infant': 'der Säugling',
 'insult': 'die Beleidigung',
 'neat': 'ordentlich',
 'outbreak': 'der Ausbruch',
 'perfection': 'die Perfektion',
 'quarterly': 'vierteljährlich',
 'resistant': 'beständig',
 'skinny': 'dünn',
 'sneak': 'schleichen',
 'sore': 'wund',
 'spark': 'der Funke',
 'speculation': 'die Spekulation',
 'steep': 'steil',
 'straw': 'das Stroh; der Strohhalm',
 'successor': 'der Nachfolger',
 'uncertain': 'unsicher',
 'whatsoever': 'überhaupt',
 'absent': 'abwesend',
 'acoustic': 'akustisch',
 'atomic': 'atomar',
 'bean': 'die Bohne',
 'bump': 'die Beule',
 'cart': 'der Wagen',
 'cord': 'die Schnur',
 'defendant': 'der Angeklagte',
 'dense': 'dicht',
 'doctrine': 'die Doktrin',
 'freshman': 'der Erstsemester',
 'habitat': 'der Lebensraum',
 'hazard': 'die Gefahr',
 'hydrogen': 'der Wasserstoff',
 'intact': 'intakt',
 'intake': 'die Aufnahme',
 'lawn': 'der Rasen',
 'manufacture': 'herstellen',
 'mistaken': 'irrtümlich',
 'needle': 'die Nadel',
 'pity': 'das Mitleid',
 'pond': 'der Teich',
 'prey': 'die Beute',
 'prophet': 'der Prophet',
 'referendum': 'die Volksabstimmung',
 'refugee': 'der Flüchtling',
 'satisfy': 'befriedigen',
 'seasonal': 'saisonal',
 'sensible': 'vernünftig',
 'sequel': 'die Fortsetzung',
 'whale': 'der Wal',
 'ankle': 'der Knöchel',
 'armour': 'die Rüstung',
 'bachelor': 'der Junggeselle; der Bachelor',
 'berry': 'die Beere',
 'capitalism': 'der Kapitalismus',
 'caution': 'die Vorsicht',
 'characteristic': 'das Merkmal',
 'clash': 'der Zusammenstoß',
 'compatible': 'kompatibel',
 'curiosity': 'die Neugier',
 'delight': 'die Freude',
 'explosive': 'explosiv',
 'fortunate': 'glücklich',
 'frontier': 'die Grenze',
 'grasp': 'begreifen',
 'handy': 'praktisch',
 'harmful': 'schädlich',
 'mandate': 'das Mandat',
 'memorable': 'unvergesslich',
 'merger': 'die Fusion',
 'portable': 'tragbar',
 'slap': 'ohrfeigen',
 'succession': 'die Nachfolge',
 'sweep': 'fegen',
 'tactical': 'taktisch',
 'thereafter': 'danach',
 'tuition': 'die Studiengebühr',
 'wholesale': 'Großhandels-',
 'canvas': 'die Leinwand',
 'cheek': 'die Wange',
 'circular': 'kreisförmig',
 'circulation': 'der Kreislauf',
 'clearance': 'die Freigabe; die Räumung',
 'comedian': 'der Komiker',
 'conscience': 'das Gewissen',
 'countless': 'unzählig',
 'detention': 'die Haft',
 'employ': 'beschäftigen',
 'fraction': 'der Bruchteil',
 'lightly': 'leicht',
 'marble': 'der Marmor',
 'maritime': 'maritim',
 'melt': 'schmelzen',
 'nominee': 'der Nominierte',
 'oath': 'der Eid',
 'pillow': 'das Kissen',
 'pirate': 'der Pirat',
 'polar': 'polar',
 'puzzle': 'das Rätsel',
 'revelation': 'die Enthüllung',
 'scholar': 'der Gelehrte',
 'stir': 'umrühren',
 'superb': 'hervorragend',
 'toast': 'der Toast; der Trinkspruch',
 'tricky': 'knifflig',
 'triumph': 'der Triumph',
 'waist': 'die Taille',
 'wreck': 'das Wrack',
 'absurd': 'absurd',
 'amid': 'inmitten',
 'bargain': 'das Schnäppchen',
 'binary': 'binär',
 'blend': 'die Mischung',
 'brake': 'die Bremse',
 'collision': 'die Kollision',
 'compassion': 'das Mitgefühl',
 'critic': 'der Kritiker',
 'distress': 'die Not',
 'elegant': 'elegant',
 'elevator': 'der Aufzug',
 'execute': 'ausführen; hinrichten',
 'feast': 'das Festmahl',
 'hike': 'die Wanderung; die Erhöhung',
 'hollow': 'hohl',
 'homeland': 'die Heimat',
 'lame': 'lahm',
 'messenger': 'der Bote',
 'plea': 'das Plädoyer',
 'punish': 'bestrafen',
 'rhetoric': 'die Rhetorik',
 'salvation': 'die Erlösung',
 'secular': 'säkular',
 'sigh': 'der Seufzer',
 'sovereign': 'souverän',
 'spouse': 'der Ehepartner',
 'tense': 'angespannt',
 'wilderness': 'die Wildnis',
 'adviser': 'der Berater',
 'anatomy': 'die Anatomie',
 'chess': 'das Schach',
 'dull': 'langweilig; stumpf',
 'fare': 'der Fahrpreis',
 'float': 'schweben, treiben',
 'generator': 'der Generator',
 'grind': 'mahlen',
 'illusion': 'die Illusion',
 'incorrect': 'falsch',
 'junction': 'die Kreuzung',
 'leap': 'der Sprung',
 'oppose': 'ablehnen, sich widersetzen',
 'postal': 'Post-',
 'profound': 'tiefgreifend',
 'prosecutor': 'der Staatsanwalt',
 'rebellion': 'die Rebellion',
 'recipient': 'der Empfänger',
 'refund': 'die Rückerstattung',
 'sober': 'nüchtern',
 'spice': 'das Gewürz',
 'squeeze': 'drücken',
 'terrain': 'das Gelände',
 'unconscious': 'bewusstlos',
 'virtue': 'die Tugend',
 'acre': 'der Morgen (Fläche)',
 'bloom': 'blühen',
 'bundle': 'das Bündel',
 'butterfly': 'der Schmetterling',
 'conjunction': 'die Konjunktion; die Verbindung',
 'costly': 'kostspielig',
 'descent': 'der Abstieg; die Abstammung',
 'directory': 'das Verzeichnis',
 'discharge': 'die Entlassung; die Entladung',
 'dodge': 'ausweichen',
 'halt': 'der Halt',
 'implied': 'implizit',
 'impress': 'beeindrucken',
 'inability': 'die Unfähigkeit',
 'mentor': 'der Mentor',
 'merchandise': 'die Ware',
 'monk': 'der Mönch',
 'occupy': 'besetzen',
 'orthodox': 'orthodox',
 'overhead': 'oben',
 'painter': 'der Maler',
 'prone': 'anfällig',
 'reunion': 'das Wiedersehen',
 'revival': 'die Wiederbelebung',
 'sanctuary': 'die Zuflucht',
 'siege': 'die Belagerung',
 'sleeve': 'der Ärmel',
 'spine': 'die Wirbelsäule',
 'tenure': 'die Amtszeit',
 'texture': 'die Textur',
 'thankful': 'dankbar',
 'triangle': 'das Dreieck',
 'unclear': 'unklar',
 'affection': 'die Zuneigung',
 'altitude': 'die Höhe',
 'countryside': 'das Land',
 'debris': 'die Trümmer (Pl.)',
 'donor': 'der Spender',
 'educate': 'erziehen, bilden',
 'fierce': 'heftig',
 'gratitude': 'die Dankbarkeit',
 'inequality': 'die Ungleichheit',
 'leisure': 'die Freizeit',
 'sculpture': 'die Skulptur',
 'showcase': 'das Schaufenster',
 'subsidiary': 'die Tochtergesellschaft',
 'theology': 'die Theologie',
 'velocity': 'die Geschwindigkeit',
 'ambition': 'der Ehrgeiz',
 'ammunition': 'die Munition',
 'batch': 'die Charge',
 'charitable': 'wohltätig',
 'collector': 'der Sammler',
 'compliment': 'das Kompliment',
 'exotic': 'exotisch',
 'exterior': 'äußere',
 'feminine': 'weiblich',
 'fountain': 'der Brunnen',
 'fury': 'die Wut',
 'glance': 'der Blick',
 'glow': 'das Leuchten',
 'humanitarian': 'humanitär',
 'immunity': 'die Immunität',
 'liberation': 'die Befreiung',
 'lone': 'einsam',
 'necessity': 'die Notwendigkeit',
 'nickname': 'der Spitzname',
 'observer': 'der Beobachter',
 'offshore': 'Offshore-',
 'optional': 'optional',
 'pioneer': 'der Pionier',
 'prosperity': 'der Wohlstand',
 'refuge': 'die Zuflucht',
 'shortage': 'der Mangel',
 'sphere': 'die Kugel; der Bereich',
 'stare': 'starren',
 'territorial': 'territorial',
 'toss': 'werfen',
 'verbal': 'verbal',
 'wool': 'die Wolle',
 'accountable': 'verantwortlich',
 'advocacy': 'die Interessenvertretung',
 'aggression': 'die Aggression',
 'burial': 'die Beerdigung',
 'clarity': 'die Klarheit',
 'confidential': 'vertraulich',
 'discretion': 'das Ermessen; die Diskretion',
 'drought': 'die Dürre',
 'elevation': 'die Erhöhung',
 'esteem': 'die Wertschätzung',
 'gesture': 'die Geste',
 'historian': 'der Historiker',
 'hospitality': 'die Gastfreundschaft',
 'hostage': 'die Geisel',
 'literacy': 'die Lesefähigkeit',
 'particle': 'das Teilchen',
 'progression': 'der Fortschritt',
 'reservoir': 'der Stausee',
 'sensation': 'die Empfindung; die Sensation',
 'slope': 'der Hang',
 'spotlight': 'das Rampenlicht',
 'stern': 'streng',
 'stiff': 'steif',
 'terrific': 'großartig',
 'unite': 'vereinen',
 'unlock': 'entsperren',
 'vault': 'der Tresor; das Gewölbe',
 'biography': 'die Biografie',
 'broker': 'der Makler',
 'bury': 'begraben',
 'destructive': 'zerstörerisch',
 'dislike': 'nicht mögen',
 'farewell': 'der Abschied',
 'fist': 'die Faust',
 'fond of': 'angetan von',
 'foolish': 'töricht',
 'landmark': 'das Wahrzeichen',
 'liable': 'haftbar',
 'midst': 'die Mitte',
 'misery': 'das Elend',
 'nursery': 'die Kinderkrippe',
 'plague': 'die Pest',
 'solidarity': 'die Solidarität',
 'specialty': 'die Spezialität',
 'supernatural': 'übernatürlich',
 'tomb': 'das Grab',
 'trim': 'kürzen',
 'voyage': 'die Seereise',
 'attachment': 'der Anhang; die Bindung',
 'candle': 'die Kerze',
 'choir': 'der Chor',
 'confession': 'das Geständnis',
 'corridor': 'der Korridor',
 'geometry': 'die Geometrie',
 'gossip': 'der Klatsch',
 'immense': 'immens',
 'intersection': 'die Kreuzung',
 'juvenile': 'jugendlich',
 'mankind': 'die Menschheit',
 'militia': 'die Miliz',
 'pointless': 'sinnlos',
 'proximity': 'die Nähe',
 'qualification': 'die Qualifikation',
 'selective': 'selektiv',
 'shiny': 'glänzend',
 'thief': 'der Dieb',
 'tribunal': 'das Tribunal',
 'villain': 'der Schurke',
 'whistle': 'die Pfeife',
 'abusive': 'beleidigend, missbräuchlich',
 'alley': 'die Gasse',
 'appetite': 'der Appetit',
 'bully': 'der Tyrann',
 'dominate': 'dominieren',
 'dynasty': 'die Dynastie',
 'forehead': 'die Stirn',
 'informal': 'informell',
 'prospective': 'künftig',
 'swallow': 'schlucken',
 'unacceptable': 'inakzeptabel',
 'unaware': 'ahnungslos',
 'uncommon': 'ungewöhnlich',
 'underway': 'im Gange',
 'unstable': 'instabil',
 'vague': 'vage',
 'abundance': 'die Fülle',
 'antique': 'antik',
 'autonomy': 'die Autonomie',
 'breeze': 'die Brise',
 'commodity': 'die Ware',
 'correspondent': 'der Korrespondent',
 'curtain': 'der Vorhang',
 'envelope': 'der Umschlag',
 'fade': 'verblassen',
 'fatigue': 'die Erschöpfung',
 'fragile': 'zerbrechlich',
 'instinct': 'der Instinkt',
 'irony': 'die Ironie',
 'lethal': 'tödlich',
 'lively': 'lebhaft',
 'logistics': 'die Logistik',
 'morality': 'die Moral',
 'mortal': 'sterblich',
 'radius': 'der Radius',
 'referee': 'der Schiedsrichter',
 'sovereignty': 'die Souveränität',
 'taxpayer': 'der Steuerzahler',
 'allowance': 'die Zulage',
 'autonomous': 'autonom',
 'bait': 'der Köder',
 'compilation': 'die Zusammenstellung',
 'correspondence': 'die Korrespondenz',
 'desirable': 'wünschenswert',
 'favourable': 'günstig',
 'incomplete': 'unvollständig',
 'lengthy': 'langwierig',
 'levy': 'die Abgabe',
 'mock': 'verspotten',
 'niche': 'die Nische',
 'obscure': 'obskur; unbekannt',
 'recession': 'die Rezession',
 'successive': 'aufeinanderfolgend',
 'timely': 'rechtzeitig',
 'utter': 'äußern',
 'yell': 'schreien',
 'elbow': 'der Ellbogen',
 'envy': 'der Neid',
 'exile': 'das Exil',
 'heel': 'die Ferse',
 'monopoly': 'das Monopol',
 'outrage': 'die Empörung',
 'paperwork': 'der Papierkram',
 'renewal': 'die Erneuerung',
 'sincere': 'aufrichtig',
 'slaughter': 'das Gemetzel',
 'spill': 'verschütten',
 'supplier': 'der Lieferant',
 'tasty': 'lecker',
 'testify': 'aussagen',
 'decay': 'der Verfall',
 'dominance': 'die Vorherrschaft',
 'entertain': 'unterhalten',
 'imagery': 'die Bildsprache',
 'innocence': 'die Unschuld',
 'livestock': 'das Vieh',
 'notorious': 'berüchtigt',
 'outright': 'völlig, offen',
 'overly': 'übermäßig',
 'refusal': 'die Ablehnung',
 'statute': 'das Gesetz',
 'thoughtful': 'nachdenklich, aufmerksam',
 'vicious': 'bösartig',
 'wholly': 'gänzlich',
 'compression': 'die Kompression',
 'confess': 'gestehen',
 'decree': 'das Dekret',
 'despair': 'die Verzweiflung',
 'dividend': 'die Dividende',
 'drift': 'die Drift',
 'infinity': 'die Unendlichkeit',
 'pardon': 'die Begnadigung',
 'predecessor': 'der Vorgänger',
 'reckless': 'rücksichtslos',
 'redemption': 'die Erlösung; die Tilgung',
 'revision': 'die Überarbeitung',
 'scent': 'der Duft',
 'stimulus': 'der Reiz',
 'surge': 'der Anstieg',
 'vocabulary': 'der Wortschatz',
 'worthless': 'wertlos',
 'absorb': 'aufnehmen',
 'accord': 'das Abkommen',
 'assurance': 'die Zusicherung',
 'boycott': 'der Boykott',
 'competitor': 'der Konkurrent',
 'cuisine': 'die Küche',
 'doom': 'das Verhängnis',
 'flee': 'fliehen',
 'glimpse': 'der flüchtige Blick',
 'homemade': 'hausgemacht',
 'honourable': 'ehrenhaft',
 'infectious': 'ansteckend',
 'inferior': 'minderwertig',
 'injustice': 'die Ungerechtigkeit',
 'masterpiece': 'das Meisterwerk',
 'melody': 'die Melodie',
 'reliance': 'die Abhängigkeit',
 'retention': 'die Beibehaltung',
 'rotten': 'faul',
 'spoil': 'verderben; verwöhnen',
 'suburb': 'der Vorort',
 'sympathetic': 'verständnisvoll',
 'taxation': 'die Besteuerung',
 'temper': 'das Temperament',
 'coffin': 'der Sarg',
 'combo': 'die Kombination',
 'conductor': 'der Dirigent; der Leiter',
 'decorative': 'dekorativ',
 'definitive': 'endgültig',
 'epidemic': 'die Epidemie',
 'explode': 'explodieren',
 'extraction': 'die Gewinnung',
 'inheritance': 'das Erbe',
 'minimise': 'minimieren',
 'primitive': 'primitiv',
 'righteous': 'rechtschaffen',
 'seize': 'ergreifen',
 'skeleton': 'das Skelett',
 'sticky': 'klebrig',
 'unpleasant': 'unangenehm',
 'vacant': 'frei, leer',
 'vicinity': 'die Umgebung',
 'warmth': 'die Wärme',
 'bulletin': 'das Bulletin',
 'cautious': 'vorsichtig',
 'cooperate': 'zusammenarbeiten',
 'counsellor': 'der Berater',
 'faction': 'die Fraktion',
 'gamble': 'spielen, wetten',
 'harmless': 'harmlos',
 'hopeful': 'hoffnungsvoll',
 'hygiene': 'die Hygiene',
 'imaginary': 'imaginär',
 'oppression': 'die Unterdrückung',
 'probable': 'wahrscheinlich',
 'probation': 'die Probezeit; die Bewährung',
 'projection': 'die Projektion; die Prognose',
 'reproduction': 'die Fortpflanzung; die Reproduktion',
 'spokesman': 'der Sprecher',
 'surround': 'umgeben',
 'apparatus': 'der Apparat',
 'bliss': 'die Glückseligkeit',
 'bodily': 'körperlich',
 'buffer': 'der Puffer',
 'constructive': 'konstruktiv',
 'cosmic': 'kosmisch',
 'definite': 'bestimmt',
 'drawer': 'die Schublade',
 'ecosystem': 'das Ökosystem',
 'exempt': 'befreit',
 'faint': 'schwach',
 'foremost': 'vorderste',
 'greenhouse': 'das Gewächshaus',
 'metabolism': 'der Stoffwechsel',
 'newborn': 'neugeboren',
 'parody': 'die Parodie',
 'parole': 'die Bewährung',
 'queue': 'die Warteschlange',
 'sociology': 'die Soziologie',
 'traction': 'die Traktion',
 'unwanted': 'unerwünscht',
 'variant': 'die Variante',
 'wherein': 'worin',
 'algebra': 'die Algebra',
 'antenna': 'die Antenne',
 'audition': 'das Vorsprechen',
 'comparative': 'vergleichend',
 'complement': 'ergänzen',
 'conquer': 'erobern',
 'conquest': 'die Eroberung',
 'continuity': 'die Kontinuität',
 'crawl': 'kriechen',
 'credible': 'glaubwürdig',
 'digit': 'die Ziffer',
 'drainage': 'die Entwässerung',
 'felony': 'das Verbrechen',
 'fortress': 'die Festung',
 'herb': 'das Kraut',
 'herd': 'die Herde',
 'immortal': 'unsterblich',
 'incumbent': 'der Amtsinhaber',
 'insufficient': 'unzureichend',
 'literal': 'wörtlich',
 'lunar': 'Mond-',
 'maternal': 'mütterlich',
 'memoir': 'die Memoiren (Pl.)',
 'modification': 'die Änderung',
 'occurrence': 'das Vorkommen',
 'offspring': 'der Nachwuchs',
 'pathway': 'der Weg',
 'prohibition': 'das Verbot',
 'scar': 'die Narbe',
 'scripture': 'die Heilige Schrift',
 'simplicity': 'die Einfachheit',
 'textbook': 'das Lehrbuch',
 'trader': 'der Händler',
 'undercover': 'verdeckt',
 'vegetation': 'die Vegetation',
 'vein': 'die Ader',
 'accountant': 'der Buchhalter',
 'activate': 'aktivieren',
 'corpse': 'die Leiche',
 'designation': 'die Bezeichnung',
 'diploma': 'das Diplom',
 'dispatch': 'versenden',
 'extinction': 'das Aussterben',
 'geology': 'die Geologie',
 'mentality': 'die Mentalität',
 'phenomenal': 'phänomenal',
 'shipment': 'die Lieferung',
 'spatial': 'räumlich',
 'stubborn': 'stur',
 'transplant': 'die Transplantation',
 'volcano': 'der Vulkan',
 'attach': 'anhängen',
 'disciplinary': 'disziplinarisch',
 'endorsement': 'die Billigung',
 'forensic': 'forensisch',
 'forthcoming': 'bevorstehend',
 'infamous': 'berüchtigt',
 'lateral': 'seitlich',
 'lifelong': 'lebenslang',
 'naive': 'naiv',
 'prestige': 'das Prestige',
 'rigid': 'starr',
 'specification': 'die Spezifikation',
 'splendid': 'prächtig',
 'telescope': 'das Teleskop',
 'unreasonable': 'unvernünftig',
 'valuation': 'die Bewertung',
 'violate': 'verletzen',
 'vivid': 'lebhaft',
 'anticipation': 'die Vorfreude, die Erwartung',
 'authorisation': 'die Genehmigung',
 'auxiliary': 'Hilfs-',
 'baggage': 'das Gepäck',
 'bounty': 'die Belohnung',
 'contempt': 'die Verachtung',
 'endurance': 'die Ausdauer',
 'expenditure': 'die Ausgaben (Pl.)',
 'overweight': 'übergewichtig',
 'potent': 'stark',
 'rust': 'der Rost',
 'seizure': 'der Anfall; die Beschlagnahme',
 'singular': 'einzigartig',
 'stray': 'streunend',
 'systemic': 'systemisch',
 'tempo': 'das Tempo',
 'torch': 'die Fackel; die Taschenlampe',
 'understandable': 'verständlich',
 'upright': 'aufrecht',
 'vain': 'eitel; vergeblich',
 'vanity': 'die Eitelkeit',
 'whisper': 'flüstern',
 'worthwhile': 'lohnend',
 'bankrupt': 'bankrott',
 'blink': 'blinzeln',
 'childish': 'kindisch',
 'coil': 'die Spule',
 'covenant': 'der Bund',
 'devotion': 'die Hingabe',
 'disgrace': 'die Schande',
 'eventual': 'letztendlich',
 'excel': 'sich auszeichnen',
 'firstly': 'erstens',
 'greed': 'die Gier',
 'greet': 'begrüßen',
 'inflammation': 'die Entzündung',
 'magnet': 'der Magnet',
 'metaphor': 'die Metapher',
 'notify': 'benachrichtigen',
 'pact': 'der Pakt',
 'paramount': 'vorrangig',
 'patron': 'der Gönner; der Kunde',
 'regain': 'zurückgewinnen',
 'renew': 'erneuern',
 'revolt': 'der Aufstand',
 'rightly': 'zu Recht',
 'rumour': 'das Gerücht',
 'shrine': 'der Schrein',
 'shrink': 'schrumpfen',
 'solitary': 'einsam',
 'sorrow': 'der Kummer',
 'termination': 'die Kündigung',
 'thigh': 'der Oberschenkel',
 'unpaid': 'unbezahlt',
 'unsuccessful': 'erfolglos',
 'warranty': 'die Garantie',
 'aisle': 'der Gang',
 'atom': 'das Atom',
 'bilateral': 'bilateral',
 'bleed': 'bluten',
 'caption': 'die Bildunterschrift',
 'choke': 'ersticken',
 'condemn': 'verurteilen',
 'disguise': 'die Verkleidung',
 'downstairs': 'unten',
 'empathy': 'die Empathie',
 'impulse': 'der Impuls',
 'incapable': 'unfähig',
 'insecure': 'unsicher',
 'knot': 'der Knoten',
 'aberration': 'die Abweichung',
 'acquiescence': 'die Einwilligung',
 'adulation': 'die Lobhudelei',
 'affinity': 'die Affinität',
 'animosity': 'die Feindseligkeit',
 'apathy': 'die Apathie',
 'aplomb': 'die Gelassenheit',
 'arrogance': 'die Arroganz',
 'audacity': 'die Kühnheit',
 'austerity': 'die Sparpolitik',
 'avarice': 'die Habgier',
 'benevolence': 'das Wohlwollen',
 'bigotry': 'die Engstirnigkeit',
 'bravado': 'die Prahlerei',
 'brevity': 'die Kürze',
 'cacophony': 'die Kakophonie',
 'camaraderie': 'die Kameradschaft',
 'clemency': 'die Milde',
 'complicity': 'die Mittäterschaft',
 'conjecture': 'die Vermutung',
 'connoisseur': 'der Kenner',
 'contrition': 'die Reue',
 'credence': 'der Glaube',
 'culpability': 'die Schuldhaftigkeit',
 'dearth': 'der Mangel',
 'decorum': 'der Anstand',
 'deference': 'die Ehrerbietung',
 'demeanour': 'das Auftreten',
 'derision': 'der Spott',
 'diatribe': 'die Schmährede',
 'diligence': 'der Fleiß',
 'discord': 'die Zwietracht',
 'duplicity': 'die Doppelzüngigkeit',
 'effrontery': 'die Unverschämtheit',
 'eloquence': 'die Beredsamkeit',
 'enigma': 'das Rätsel',
 'equanimity': 'der Gleichmut',
 'euphoria': 'die Euphorie',
 'exasperation': 'die Verärgerung',
 'facade': 'die Fassade',
 'fervour': 'die Inbrunst',
 'finesse': 'das Fingerspitzengefühl',
 'folly': 'die Torheit',
 'fortitude': 'die Standhaftigkeit',
 'frivolity': 'die Leichtfertigkeit',
 'futility': 'die Vergeblichkeit',
 'gravitas': 'die Würde',
 'gullibility': 'die Leichtgläubigkeit',
 'hindsight': 'die Rückschau',
 'hypocrisy': 'die Heuchelei',
 'idiosyncrasy': 'die Eigenart',
 'ignominy': 'die Schmach',
 'impetus': 'der Antrieb',
 'impunity': 'die Straflosigkeit',
 'inertia': 'die Trägheit',
 'ingenuity': 'der Einfallsreichtum',
 'introspection': 'die Selbstbeobachtung',
 'lethargy': 'die Lethargie',
 'longevity': 'die Langlebigkeit',
 'magnanimity': 'die Großmut',
 'malaise': 'das Unbehagen',
 'malice': 'die Bosheit',
 'melancholy': 'die Melancholie',
 'mitigation': 'die Milderung',
 'nostalgia': 'die Nostalgie',
 'nuisance': 'das Ärgernis',
 'obstinacy': 'die Hartnäckigkeit',
 'onus': 'die Last, die Pflicht',
 'opulence': 'die Üppigkeit',
 'paradigm shift': 'der Paradigmenwechsel',
 'parity': 'die Parität',
 'paucity': 'die Knappheit',
 'perseverance': 'die Beharrlichkeit',
 'petulance': 'die Gereiztheit',
 'plight': 'die Notlage',
 'pragmatism': 'der Pragmatismus',
 'precedence': 'der Vorrang',
 'prerogative': 'das Vorrecht',
 'probity': 'die Redlichkeit',
 'prudence': 'die Umsicht',
 'rapport': 'der Draht, die Beziehung',
 'rebuttal': 'die Widerlegung',
 'recourse': 'der Rückgriff',
 'remorse': 'die Reue',
 'resentment': 'der Groll',
 'restitution': 'die Rückerstattung',
 'reticence': 'die Zurückhaltung',
 'reverence': 'die Ehrfurcht',
 'scepticism': 'die Skepsis',
 'serendipity': 'der glückliche Zufall',
 'solace': 'der Trost',
 'stigma': 'das Stigma',
 'subterfuge': 'die List',
 'trepidation': 'die Beklommenheit',
 'ubiquity': 'die Allgegenwart',
 'veneer': 'die Fassade',
 'veracity': 'die Wahrhaftigkeit',
 'vigilance': 'die Wachsamkeit',
 'zeal': 'der Eifer',
 'abdicate': 'abdanken',
 'abhor': 'verabscheuen',
 'admonish': 'ermahnen',
 'allay': 'zerstreuen (Bedenken)',
 'ameliorate': 'verbessern',
 'assuage': 'lindern',
 'beguile': 'betören',
 'belittle': 'herabsetzen',
 'berate': 'ausschimpfen',
 'capitulate': 'kapitulieren',
 'castigate': 'geißeln',
 'cajole': 'beschwatzen',
 'chastise': 'züchtigen',
 'coerce': 'nötigen',
 'commiserate': 'mitfühlen',
 'concur': 'übereinstimmen',
 'construe': 'auslegen',
 'debunk': 'entlarven',
 'decry': 'anprangern',
 'deride': 'verhöhnen',
 'discern': 'erkennen',
 'disparage': 'herabsetzen',
 'dissuade': 'abraten',
 'elucidate': 'erläutern',
 'emulate': 'nacheifern',
 'encroach': 'übergreifen',
 'engender': 'hervorrufen',
 'enthral': 'fesseln',
 'epitomise': 'verkörpern',
 'eschew': 'meiden',
 'exonerate': 'entlasten',
 'expedite': 'beschleunigen',
 'extol': 'preisen',
 'fabricate': 'erfinden',
 'flout': 'missachten',
 'foment': 'schüren',
 'forgo': 'verzichten',
 'hamper': 'behindern',
 'harangue': 'eine Strafpredigt halten',
 'impede': 'behindern',
 'implore': 'anflehen',
 'incite': 'aufhetzen',
 'instigate': 'anstiften',
 'jeopardise': 'gefährden',
 'languish': 'schmachten',
 'negate': 'aufheben',
 'ostracise': 'ausgrenzen',
 'pacify': 'beruhigen',
 'perpetuate': 'fortführen',
 'ponder': 'grübeln',
 'precipitate': 'auslösen',
 'preclude': 'ausschließen',
 'procrastinate': 'aufschieben',
 'proliferate': 'sich ausbreiten',
 'rebuke': 'zurechtweisen',
 'recant': 'widerrufen',
 'reciprocate': 'erwidern',
 'reprimand': 'rügen',
 'rescind': 'aufheben',
 'reverberate': 'nachhallen',
 'scrutinise': 'prüfen',
 'squander': 'vergeuden',
 'stifle': 'unterdrücken',
 'subjugate': 'unterwerfen',
 'supplant': 'verdrängen',
 'transcend': 'übersteigen',
 'underpin': 'untermauern',
 'usurp': 'an sich reißen',
 'vilify': 'verunglimpfen',
 'waive': 'verzichten auf',
 'wane': 'schwinden',
 'waver': 'schwanken',
 'wield': 'ausüben',
 'abject': 'erbärmlich',
 'acerbic': 'bissig',
 'adamant': 'unnachgiebig',
 'adroit': 'geschickt',
 'affable': 'umgänglich',
 'ambivalent': 'ambivalent',
 'amenable': 'zugänglich',
 'apprehensive': 'besorgt',
 'arcane': 'geheimnisvoll',
 'ardent': 'leidenschaftlich',
 'articulate': 'redegewandt',
 'auspicious': 'vielversprechend',
 'austere': 'streng, karg',
 'banal': 'banal',
 'benign': 'gutartig',
 'blatant': 'offenkundig',
 'brusque': 'schroff',
 'callous': 'gefühllos',
 'candid': 'offen',
 'capricious': 'launisch',
 'caustic': 'ätzend',
 'clandestine': 'heimlich',
 'complacent': 'selbstgefällig',
 'conducive': 'förderlich',
 'contentious': 'strittig',
 'copious': 'reichlich',
 'cursory': 'flüchtig',
 'cynical': 'zynisch',
 'daunting': 'entmutigend',
 'deft': 'geschickt',
 'despondent': 'niedergeschlagen',
 'diffident': 'schüchtern',
 'dilapidated': 'baufällig',
 'discerning': 'anspruchsvoll',
 'disparate': 'ungleichartig',
 'dogmatic': 'dogmatisch',
 'ebullient': 'überschwänglich',
 'eclectic': 'eklektisch',
 'efficacious': 'wirksam',
 'elusive': 'schwer fassbar',
 'empirical': 'empirisch',
 'enigmatic': 'rätselhaft',
 'erratic': 'unberechenbar',
 'esoteric': 'esoterisch',
 'exemplary': 'vorbildlich',
 'exorbitant': 'überhöht',
 'expedient': 'zweckdienlich',
 'facetious': 'witzelnd',
 'fallible': 'fehlbar',
 'fervent': 'inbrünstig',
 'flagrant': 'eklatant',
 'frugal': 'sparsam',
 'furtive': 'verstohlen',
 'gregarious': 'gesellig',
 'haphazard': 'planlos',
 'heinous': 'abscheulich',
 'histrionic': 'theatralisch',
 'idiosyncratic': 'eigenwillig',
 'ignominious': 'schmachvoll',
 'immaculate': 'makellos',
 'impeccable': 'tadellos',
 'imperative': 'unerlässlich',
 'impetuous': 'ungestüm',
 'implacable': 'unversöhnlich',
 'incessant': 'unaufhörlich',
 'incongruous': 'unpassend',
 'indefatigable': 'unermüdlich',
 'indelible': 'unauslöschlich',
 'indolent': 'träge',
 'innate': 'angeboren',
 'innocuous': 'harmlos',
 'insidious': 'heimtückisch',
 'intrepid': 'unerschrocken',
 'irascible': 'jähzornig',
 'judicious': 'umsichtig',
 'languid': 'matt',
 'lucid': 'klar',
 'ludicrous': 'lächerlich',
 'magnanimous': 'großmütig',
 'mundane': 'alltäglich',
 'nefarious': 'ruchlos',
 'nonchalant': 'lässig',
 'nuanced': 'differenziert',
 'obstinate': 'starrsinnig',
 'ominous': 'unheilvoll',
 'onerous': 'belastend',
 'ostentatious': 'protzig',
 'palpable': 'spürbar',
 'paltry': 'dürftig',
 'placid': 'ruhig',
 'poignant': 'ergreifend',
 'pragmatic': 'pragmatisch',
 'precarious': 'prekär',
 'prescient': 'vorausschauend',
 'pristine': 'unberührt',
 'prolific': 'produktiv',
 'prudent': 'umsichtig',
 'quaint': 'malerisch',
 'rampant': 'grassierend',
 'recalcitrant': 'widerspenstig',
 'reticent': 'zurückhaltend',
 'sanguine': 'zuversichtlich',
 'scrupulous': 'gewissenhaft',
 'scathing': 'vernichtend',
 'serene': 'gelassen',
 'shrewd': 'scharfsinnig',
 'spurious': 'unecht',
 'staunch': 'unerschütterlich',
 'stoic': 'stoisch',
 'succinct': 'prägnant',
 'superfluous': 'überflüssig',
 'surreptitious': 'heimlich',
 'taciturn': 'wortkarg',
 'tangible': 'greifbar',
 'trite': 'abgedroschen',
 'unequivocal': 'unmissverständlich',
 'venerable': 'ehrwürdig',
 'verbose': 'weitschweifig',
 'vindictive': 'rachsüchtig',
 'volatile': 'volatil',
 'wary': 'vorsichtig',
 'whimsical': 'verspielt',
 'zealous': 'eifrig',
 'inadvertently': 'versehentlich',
 'perfunctorily': 'oberflächlich',
 'vehemently': 'vehement',
 'unequivocally': 'unmissverständlich',
 'invariably': 'ausnahmslos',
 'wholeheartedly': 'von ganzem Herzen',
 'begrudgingly': 'widerwillig',
 'a far cry from': 'weit entfernt von',
 'a moot point': 'eine strittige Frage',
 'add insult to injury': 'noch eins draufsetzen',
 'at loggerheads': 'im Clinch',
 'beyond the pale': 'indiskutabel',
 'by the same token': 'ebenso',
 'come full circle': 'sich schließt der Kreis',
 'cut both ways': 'ein zweischneidiges Schwert sein',
 'err on the side of caution': 'lieber vorsichtig sein',
 'fall on deaf ears': 'auf taube Ohren stoßen',
 'get wind of': 'Wind bekommen von',
 'go against the grain': 'gegen den Strich gehen',
 'hold sway': 'vorherrschen',
 'in the offing': 'bevorstehend',
 'keep at bay': 'in Schach halten',
 'leave no stone unturned': 'nichts unversucht lassen',
 'make headway': 'vorankommen',
 'on tenterhooks': 'wie auf glühenden Kohlen',
 'pay lip service to': 'ein Lippenbekenntnis ablegen',
 "pull one's weight": 'seinen Beitrag leisten',
 "rest on one's laurels": 'sich auf seinen Lorbeeren ausruhen',
 'run the gauntlet': 'Spießruten laufen',
 "steal someone's thunder": 'jemandem die Schau stehlen',
 'take with a pinch of salt': 'mit Vorsicht genießen',
 'the writing on the wall': 'die Zeichen an der Wand',
 'throw down the gauntlet': 'den Fehdehandschuh hinwerfen',
 'to all intents and purposes': 'praktisch',
 'turn a blind eye': 'ein Auge zudrücken',
 'up in arms': 'in Aufruhr',
 'vested interest': 'ein persönliches Interesse',
 'with bated breath': 'mit angehaltenem Atem',
 'a red herring': 'eine falsche Fährte',
 'a Pyrrhic victory': 'ein Pyrrhussieg',
 'an uphill battle': 'ein harter Kampf',
 'caught between a rock and a hard place': 'zwischen Baum und Borke',
 'cross the Rubicon': 'den Rubikon überschreiten',
 'draw the line': 'die Grenze ziehen',
 'let sleeping dogs lie': 'keine schlafenden Hunde wecken',
 'on the fence': 'unentschlossen',
 'the last straw': 'der Tropfen, der das Fass zum Überlaufen bringt',
 'touch and go': 'auf Messers Schneide',
 'by': 'von; neben',
 'have to': 'müssen',
 'will': 'werden (Futur)',
 'up': 'nach oben, hinauf',
 'out': 'hinaus, draußen',
 'their': 'ihr (Plural)',
 'her': 'ihr; sie',
 'would': 'würde',
 'them': 'sie, ihnen',
 'its': 'sein, ihr (Sache)',
 'him': 'ihn, ihm',
 'no one': 'niemand',
 'any': 'irgendein; kein',
 'us': 'uns',
 'a work': 'die Arbeit; das Werk',
 'too': 'auch; zu (viel)',
 'off': 'aus; weg',
 'a help': 'die Hilfe',
 'thing': 'das Ding, die Sache',
 'each': 'jeder (einzelne)',
 'an end': 'das Ende',
 'a show': 'die Show, die Sendung',
 'family (adj.)': 'Familien-, familienfreundlich',
 'a lot': 'viel, eine Menge',
 'to name': 'nennen, benennen',
 'a play': 'das Theaterstück',
 'few': 'wenige',
 'let': 'lassen',
 'everything': 'alles',
 'a stop': 'die Haltestelle; der Halt',
 'a call': 'der Anruf',
 'far': 'weit',
 'everyone': 'jeder, alle',
 'story': 'die Geschichte',
 'a post': 'der Beitrag; die Post',
 'ago': 'vor (zeitlich)',
 'south': 'der Süden',
 'yeah': 'ja (ugs.)',
 'past (adj.)': 'vergangen',
 'a question': 'die Frage',
 'north': 'der Norden',
 'a watch': 'die Armbanduhr',
 'a report': 'der Bericht',
 'a turn': 'die Reihe; die Kurve',
 'yourself': 'dich selbst, selbst',
 'fun': 'der Spaß',
 'to phone': 'anrufen',
 'easy': 'leicht, einfach',
 'a plan': 'der Plan',
 'west': 'der Westen',
 'front (adj.)': 'vorder-',
 'list': 'die Liste',
 'college': 'das College, die Fachhochschule',
 'a study': 'die Studie',
 'a cost': 'die Kosten',
 'period': 'der Zeitraum, die Periode',
 'club': 'der Verein, der Klub',
 'common': 'häufig; gemeinsam',
 'a return': 'die Rückkehr; die Rückgabe',
 'an answer': 'die Antwort',
 'to design': 'entwerfen, gestalten',
 'a guess': 'die Vermutung',
 'an interest': 'das Interesse; die Zinsen',
 'east': 'der Osten',
 'movie': 'der Film',
 'to sound': 'klingen',
 'stand': 'stehen',
 'fast (adv.)': 'schnell',
 'match': 'das Spiel; das Streichholz',
 'model': 'das Modell',
 'hey': 'hey',
 'key (adj.)': 'Schlüssel-, wesentlich',
 'page': 'die Seite',
 'amazing': 'erstaunlich, toll',
 'complete (adj.)': 'vollständig',
 'be born': 'geboren werden',
 'a walk': 'der Spaziergang',
 'die': 'sterben',
 'writing': 'das Schreiben',
 'box': 'die Schachtel, die Kiste',
 'note': 'die Notiz',
 'a visit': 'der Besuch',
 'tonight': 'heute Abend',
 'century': 'das Jahrhundert',
 'cold (adj.)': 'kalt',
 'create': 'schaffen, erstellen',
 'capital (adj.)': 'groß (Buchstabe); Haupt-',
 'radio': 'das Radio',
 'station': 'der Bahnhof, die Station',
 'ice': 'das Eis',
 'quickly': 'schnell',
 'travel (noun)': 'das Reisen',
 'extra': 'zusätzlich, extra',
 'clean (adj.)': 'sauber',
 'dad': 'der Papa',
 'interested': 'interessiert',
 'letter': 'der Brief; der Buchstabe',
 'a dance': 'der Tanz',
 'band': 'die Band',
 'an address': 'die Adresse',
 'a drink': 'das Getränk',
 'to shop': 'einkaufen',
 'meaning': 'die Bedeutung',
 'an interview': 'das Interview; das Vorstellungsgespräch',
 'fat': 'dick',
 'everybody': 'jeder, alle',
 'fourth': 'vierter',
 'fifth': 'fünfter',
 'dear': 'lieb; teuer',
 'to dress': 'sich anziehen',
 'blog': 'der Blog',
 'to rain': 'regnen',
 'to email': 'mailen',
 'to exercise': 'trainieren, Sport treiben',
 'a laugh': 'das Lachen',
 'to snow': 'schneien',
 'painting': 'das Gemälde',
 'boyfriend': 'der Freund (Partner)',
 'dollar': 'der Dollar',
 'detail': 'das Detail',
 'favourite': 'Lieblings-',
 'parent': 'der Elternteil',
 'programme': 'das Programm, die Sendung',
 'exciting': 'spannend',
 'bike': 'das Fahrrad',
 'singer': 'der Sänger',
 'tall': 'groß',
 'dancing': 'das Tanzen',
 'guitar': 'die Gitarre',
 'actress': 'die Schauspielerin',
 'mum': 'die Mama',
 'vacation': 'der Urlaub',
 'tennis': 'das Tennis',
 'reader': 'der Leser',
 'pound': 'das Pfund',
 'piano': 'das Klavier',
 'photograph': 'das Foto',
 'dish': 'das Gericht; die Schüssel',
 'bored': 'gelangweilt',
 'boot': 'der Stiefel',
 'classroom': 'das Klassenzimmer',
 'farmer': 'der Bauer, der Landwirt',
 'sandwich': 'das Sandwich',
 'cafe': 'das Café',
 'blonde': 'blond',
 "o'clock": 'Uhr',
 'spelling': 'die Rechtschreibung',
 'upstairs': 'oben, nach oben',
 'sweater': 'der Pullover',
 'metre': 'der Meter',
 'policeman': 'der Polizist',
 'kilometre': 'der Kilometer',
 'grandparent': 'der Großelternteil',
 'a can': 'die Dose',
 'good (noun)': 'das Gute',
 'back (adj.)': 'hinter-, Hinter-',
 'a need': 'der Bedarf, das Bedürfnis',
 'any more': 'nicht mehr',
 'home (adj.)': 'Heim-, häuslich',
 'a look': 'der Blick; das Aussehen',
 'a use': 'der Gebrauch, die Verwendung',
 'used to': 'früher (pflegte zu)',
 'to number': 'nummerieren',
 'thought': 'der Gedanke',
 'god': 'der Gott',
 'top': 'die Spitze; das Oberteil',
 'to care': 'sich kümmern',
 'a start': 'der Anfang, der Start',
 'yet': 'noch; schon',
 'support (noun)': 'die Unterstützung',
 'including': 'einschließlich',
 'based': 'basierend; ansässig',
 'national': 'national',
 'a run': 'der Lauf',
 'service': 'der Dienst, der Service',
 'general': 'allgemein',
 'united': 'vereint',
 'following': 'folgend',
 'war': 'der Krieg',
 'per': 'pro',
 'president': 'der Präsident',
 'working': 'arbeitend; funktionierend',
 'a hope': 'die Hoffnung',
 'to book': 'buchen',
 'a talk': 'das Gespräch; der Vortrag',
 'level': 'das Niveau, die Stufe',
 'to mind': 'etwas dagegen haben; aufpassen',
 'control (noun)': 'die Kontrolle',
 'guy': 'der Typ',
 'pay (noun)': 'die Bezahlung, der Lohn',
 'lost': 'verloren',
 'to matter': 'wichtig sein',
 'a bit': 'ein bisschen; das Stück',
 'a hit': 'der Schlag; der Hit',
 'close (adj.)': 'nah',
 'past (adv.)': 'vorbei',
 'to cause': 'verursachen',
 'a wait': 'das Warten',
 'future (adj.)': 'zukünftig',
 'a stay': 'der Aufenthalt',
 'to deal': 'sich befassen; handeln',
 'a check': 'die Kontrolle, die Prüfung',
 'myself': 'mich selbst, selbst',
 'act': 'handeln; schauspielern',
 'fun (adj.)': 'lustig, unterhaltsam',
 'major': 'bedeutend, Haupt-',
 'according to': 'laut, gemäß',
 'available': 'verfügbar',
 'process': 'der Prozess, der Vorgang',
 'himself': 'sich, selbst',
 'thinking': 'das Denken',
 'a fight': 'der Kampf, die Schlägerei',
 'a rest': 'die Pause; der Rest',
 'to land': 'landen',
 'especially': 'besonders',
 'a record': 'die Aufzeichnung; der Rekord',
 'to film': 'filmen',
 'to star': 'die Hauptrolle spielen',
 'middle (adj.)': 'mittlere',
 'to present': 'präsentieren',
 'a wish': 'der Wunsch',
 'gold': 'das Gold',
 'king': 'der König',
 'original (adj.)': 'ursprünglich, original',
 'role': 'die Rolle',
 'themselves': 'sich selbst',
 'provide': 'bereitstellen',
 'source': 'die Quelle',
 'evidence': 'der Beweis',
 'a drive': 'die Fahrt; das Laufwerk',
 'a fall': 'der Sturz; der Herbst (AmE)',
 'review': 'die Rezension, die Überprüfung',
 'itself': 'sich (selbst)',
 'stage': 'die Phase; die Bühne',
 'to attack': 'angreifen',
 'kill': 'töten',
 'code': 'der Code',
 'to cover': 'bedecken; abdecken',
 'an increase': 'die Zunahme, der Anstieg',
 'pick': 'auswählen; pflücken',
 'to race': 'rennen, ein Rennen fahren',
 'a sign': 'das Zeichen; das Schild',
 'figure': 'die Zahl; die Figur',
 'sir': 'der Herr',
 'towards': 'in Richtung, gegenüber',
 'a mark': 'die Note; die Markierung',
 'missing': 'fehlend, vermisst',
 'sleep (noun)': 'der Schlaf',
 'mine': 'meiner',
 'included': 'inbegriffen',
 'response': 'die Antwort, die Reaktion',
 'rock': 'der Fels; der Rock',
 'shall': 'sollen (Vorschlag)',
 'specific': 'bestimmt, spezifisch',
 'network': 'das Netzwerk',
 'beat': 'schlagen, besiegen',
 'conference': 'die Konferenz',
 'double (adj.)': 'doppelt',
 'gas': 'das Gas; das Benzin (AmE)',
 'population': 'die Bevölkerung',
 'to text': 'eine SMS schreiben',
 'completely': 'völlig',
 'cross': 'das Kreuz',
 'focus (noun)': 'der Fokus, der Schwerpunkt',
 'a sort': 'die Art, die Sorte',
 'kid': 'das Kind',
 'to link': 'verbinden, verlinken',
 'manager': 'der Manager, der Leiter',
 'definitely': 'definitiv, auf jeden Fall',
 'gun': 'die Waffe, die Pistole',
 'a search': 'die Suche',
 'wow': 'wow',
 'fear (noun)': 'die Angst',
 'fit (adj.)': 'fit; passend',
 'lady': 'die Dame',
 'secretary': 'der Sekretär',
 'bar': 'die Bar; die Stange',
 'hurt (adj.)': 'verletzt; gekränkt',
 'image': 'das Bild, das Image',
 'clearly': 'deutlich',
 'fan': 'der Fan; der Ventilator',
 'learning': 'das Lernen',
 'organization': 'die Organisation',
 'secret (adj.)': 'geheim',
 'a dream': 'der Traum',
 'a finish': 'das Ende, das Ziel',
 'driving': 'das Fahren',
 'to fish': 'angeln',
 'a notice': 'der Aushang; die Mitteilung',
 'to plant': 'pflanzen',
 'a comment': 'der Kommentar',
 'equipment': 'die Ausrüstung',
 'hall': 'die Halle; der Flur',
 'pop': 'der Pop',
 'to heat': 'erhitzen, heizen',
 'queen': 'die Königin',
 'a ride': 'die Fahrt',
 'bottom (adj.)': 'unterste',
 'square (adj.)': 'quadratisch',
 'structure': 'die Struktur',
 'realize': 'erkennen, merken',
 'to score': 'ein Tor schießen, punkten',
 'separate (adj.)': 'getrennt',
 'benefit': 'der Vorteil, der Nutzen',
 'metal': 'das Metall',
 'understanding': 'das Verständnis',
 'ring': 'der Ring; das Klingeln',
 'to ring': 'klingeln, anrufen',
 'adult (adj.)': 'erwachsen',
 'method': 'die Methode',
 'winner': 'der Gewinner',
 'camp': 'das Lager, das Camp',
 'extremely': 'äußerst',
 'herself': 'sich selbst',
 'shut (adj.)': 'geschlossen',
 'van': 'der Lieferwagen',
 'onto': 'auf (hinauf)',
 'billion': 'die Milliarde',
 'to farm': 'Landwirtschaft betreiben',
 'fix': 'reparieren; befestigen',
 'a fly': 'die Fliege',
 'guide': 'der Führer, der Reiseleiter',
 'to guide': 'führen',
 'a surprise': 'die Überraschung',
 'yours': 'deiner, Ihrer',
 'per cent': 'das Prozent',
 'strategy': 'die Strategie',
 'web': 'das Netz; das Web',
 'to stress': 'betonen; stressen',
 'a taste': 'der Geschmack',
 'assistant': 'der Assistent',
 'flat (adj.)': 'flach',
 'ill': 'krank',
 'to mail': 'schicken, mailen',
 'teaching': 'das Unterrichten',
 'alternative': 'die Alternative',
 'flying': 'das Fliegen',
 'a promise': 'das Versprechen',
 'a suit': 'der Anzug',
 'a jump': 'der Sprung',
 'survey': 'die Umfrage',
 'connected': 'verbunden',
 'a download': 'der Download',
 'ending': 'das Ende, der Schluss',
 'to joke': 'scherzen',
 'factor': 'der Faktor',
 'smoke (noun)': 'der Rauch',
 'a cook': 'der Koch',
 'a smile': 'das Lächeln',
 'bowl': 'die Schüssel',
 'context': 'der Kontext',
 'worried': 'besorgt',
 'ourselves': 'uns selbst',
 'to cycle': 'Rad fahren',
 'scared': 'ängstlich',
 'affect': 'beeinflussen',
 'blow': 'wehen; blasen',
 'singing': 'das Singen',
 'drawing': 'die Zeichnung',
 'replace': 'ersetzen',
 'a chat': 'der Plausch, der Chat',
 'anybody': 'irgendjemand',
 'basketball': 'der Basketball',
 'expert (adj.)': 'fachkundig',
 'golf': 'das Golf',
 'to circle': 'einkreisen; kreisen',
 'noise': 'der Lärm',
 'advertising': 'die Werbung',
 'baseball': 'der Baseball',
 'attractive': 'attraktiv',
 'introduction': 'die Einleitung; die Vorstellung',
 'pilot': 'der Pilot',
 'recognize': 'erkennen',
 'smoking': 'das Rauchen',
 'exact': 'genau',
 'to lock': 'abschließen',
 'musical': 'musikalisch',
 'plastic (adj.)': 'Plastik-',
 'recording': 'die Aufnahme',
 'tie': 'die Krawatte; das Unentschieden',
 'to tie': 'binden',
 'document': 'das Dokument',
 'to reply': 'antworten',
 'a smell': 'der Geruch',
 'pants': 'die Hose; die Unterhose (BrE)',
 'soccer': 'der Fußball',
 'clothing': 'die Kleidung',
 'everyday': 'alltäglich',
 'fishing': 'das Angeln',
 'parking': 'das Parken',
 'carefully': 'vorsichtig, sorgfältig',
 'railway': 'die Eisenbahn',
 'a wash': 'die Wäsche',
 'explanation': 'die Erklärung',
 'pleased': 'zufrieden, erfreut',
 'architecture': 'die Architektur',
 'designer': 'der Designer',
 'electrical': 'elektrisch',
 'hockey': 'das Hockey',
 'lab': 'das Labor',
 'virus': 'das Virus',
 'an experiment': 'das Experiment',
 'twin (adj.)': 'Zwillings-',
 'uniform': 'die Uniform',
 'underground (adj.)': 'unterirdisch',
 'chip': 'die Pommes; der Chip',
 'jazz': 'der Jazz',
 'sauce': 'die Soße',
 'toy': 'das Spielzeug',
 'lifestyle': 'der Lebensstil',
 'surprising': 'überraschend',
 'tourism': 'der Tourismus',
 'classical': 'klassisch',
 'instrument': 'das Instrument',
 'spider': 'die Spinne',
 'to brush': 'bürsten, putzen',
 'differently': 'anders',
 'to photograph': 'fotografieren',
 'pub': 'die Kneipe',
 'reception': 'der Empfang, die Rezeption',
 'employer': 'der Arbeitgeber',
 'correctly': 'richtig',
 'farming': 'die Landwirtschaft',
 'pollution': 'die Verschmutzung',
 'poster': 'das Plakat',
 'runner': 'der Läufer',
 'sadly': 'leider; traurig',
 'mathematics': 'die Mathematik',
 'quietly': 'leise',
 'to lecture': 'eine Vorlesung halten',
 'teenage': 'jugendlich',
 'ski': 'der Ski',
 'to ski': 'Ski fahren',
 'washing': 'die Wäsche',
 'publish': 'veröffentlichen',
 'cartoon': 'der Zeichentrickfilm; die Karikatur',
 'predict': 'vorhersagen',
 'trainer': 'der Trainer; der Turnschuh',
 'continent': 'der Kontinent',
 'monkey': 'der Affe',
 'motorcycle': 'das Motorrad',
 'penny': 'der Penny, der Pfennig',
 'cigarette': 'die Zigarette',
 'a shout': 'der Schrei',
 'tablet': 'das Tablet; die Tablette',
 'airline': 'die Fluggesellschaft',
 'nut': 'die Nuss; die Mutter',
 'instructor': 'der Lehrer, der Ausbilder',
 'camping': 'das Camping',
 'sailing': 'das Segeln',
 'crowded': 'überfüllt',
 'organize': 'organisieren',
 'fortunately': 'glücklicherweise',
 'hers': 'ihrer',
 'businessman': 'der Geschäftsmann',
 'printer': 'der Drucker',
 'researcher': 'der Forscher',
 'frog': 'der Frosch',
 'secondly': 'zweitens',
 'skiing': 'das Skifahren',
 'boil': 'kochen',
 'loudly': 'laut',
 'noisy': 'laut',
 'advertise': 'werben',
 'curly': 'lockig',
 'invent': 'erfinden',
 'tidy': 'ordentlich',
 'listener': 'der Zuhörer',
 'traveller': 'der Reisende',
 'biscuit': 'der Keks',
 'recycle': 'recyceln',
 'cooker': 'der Herd',
 'stair': 'die Stufe',
 'lorry': 'der Lkw',
 'a will': 'der Wille; das Testament',
 'like (noun)': 'der Like, die Vorliebe',
 'used': 'gebraucht',
 'to state': 'angeben, erklären',
 'to place': 'platzieren, legen',
 'a set': 'der Satz, das Set',
 'live (adj.)': 'live; lebend',
 'to point': 'zeigen',
 'to water': 'gießen',
 'to head': 'steuern, sich begeben',
 'far (adj.)': 'fern, weit',
 'though': 'obwohl',
 'to face': 'sich stellen; gegenüberliegen',
 'kind (adj.)': 'freundlich, nett',
 'to hand': 'reichen',
 'level (adj.)': 'eben; gleich',
 'a win': 'der Sieg',
 'close (adv.)': 'nah',
 'due': 'fällig',
 'an act': 'die Tat; das Gesetz',
 'to fire': 'schießen; feuern',
 'living (adj.)': 'lebend',
 'a living': 'der Lebensunterhalt',
 'to market': 'vermarkten',
 'current': 'aktuell',
 'to experience': 'erleben',
 'to program': 'programmieren',
 'to type': 'tippen',
 'to board': 'einsteigen',
 'a cut': 'der Schnitt; die Kürzung',
 'to force': 'zwingen',
 'issue': 'das Thema, das Problem; die Ausgabe',
 'sex': 'das Geschlecht; der Sex',
 'a lead': 'die Führung; der Hinweis',
 'a share': 'der Anteil; die Aktie',
 'to view': 'betrachten',
 'to result': 'sich ergeben',
 'policy': 'die Politik, die Richtlinie',
 'the press': 'die Presse',
 'worth': 'wert',
 'a value': 'der Wert',
 'to tax': 'besteuern',
 'range': 'die Bandbreite, das Sortiment',
 'to trade': 'handeln',
 'hate (noun)': 'der Hass',
 'to vote': 'wählen, abstimmen',
 'involved': 'beteiligt',
 'to release': 'freilassen; veröffentlichen',
 'written': 'schriftlich',
 'currently': 'derzeit',
 'financial': 'finanziell',
 'legal': 'legal, rechtlich',
 'version': 'die Version',
 'to access': 'zugreifen',
 'to base': 'basieren',
 'a pass': 'der Ausweis; der Pass (Sport)',
 'a risk': 'das Risiko',
 'a mine': 'das Bergwerk; die Mine',
 'to note': 'notieren; bemerken',
 'respect (noun)': 'der Respekt',
 'standard': 'der Standard',
 'album': 'das Album',
 'to charge': 'berechnen; laden; anklagen',
 'to store': 'speichern, lagern',
 'western': 'westlich',
 'to campaign': 'sich einsetzen',
 'leading': 'führend',
 'to contact': 'kontaktieren',
 'a drop': 'der Tropfen; der Rückgang',
 'to tour': 'bereisen, touren',
 'absolutely': 'absolut, völlig',
 'episode': 'die Folge, die Episode',
 'to coach': 'trainieren, coachen',
 'expected': 'erwartet',
 'particularly': 'besonders',
 'a claim': 'die Behauptung; der Anspruch',
 'generally': 'im Allgemeinen',
 'to judge': 'beurteilen',
 'plus': 'plus',
 'to rule': 'regieren',
 'seriously': 'ernsthaft',
 'wonder (noun)': 'das Staunen; das Wunder',
 'fighting': 'die Kämpfe',
 'to impact': 'sich auswirken',
 'to lack': 'fehlen, mangeln',
 'latest': 'neueste',
 'a touch': 'die Berührung',
 'to damage': 'beschädigen',
 'directly': 'direkt',
 'to doubt': 'zweifeln',
 'planning': 'die Planung',
 'to award': 'verleihen',
 'to block': 'blockieren',
 'killing': 'die Tötung',
 'theory': 'die Theorie',
 'located': 'gelegen',
 'to murder': 'ermorden',
 'an exchange': 'der Austausch',
 'northern': 'nördlich',
 'a lie': 'die Lüge',
 'southern': 'südlich',
 'a worry': 'die Sorge',
 'a count': 'die Zählung',
 'covered': 'bedeckt',
 'previously': 'vorher',
 'totally': 'total, völlig',
 'to benefit': 'profitieren',
 'a click': 'der Klick',
 'to feature': 'aufweisen, zeigen',
 'a pull': 'der Zug',
 'a push': 'der Stoß',
 'sexual': 'sexuell',
 'agent': 'der Vertreter, der Agent',
 'to lie (down)': 'liegen',
 'a rise': 'der Anstieg',
 'to supply': 'liefern, versorgen',
 'waste (adj.)': 'Abfall-',
 'waste (noun)': 'der Abfall; die Verschwendung',
 'engineering': 'die Technik, das Ingenieurwesen',
 'obviously': 'offensichtlich',
 'eastern': 'östlich',
 'function': 'die Funktion',
 'influence (noun)': 'der Einfluss',
 'marketing': 'das Marketing',
 'nor': 'noch',
 'journal': 'die Fachzeitschrift; das Tagebuch',
 'possibly': 'möglicherweise',
 'ad': 'die Anzeige',
 'to balance': 'ausgleichen, balancieren',
 'magic (adj.)': 'magisch, Zauber-',
 'net': 'das Netz',
 'to request': 'anfordern, bitten',
 'stick': 'der Stock',
 'to stick': 'kleben',
 'cultural': 'kulturell',
 'roll': 'die Rolle; das Brötchen',
 'to roll': 'rollen',
 'slightly': 'leicht, etwas',
 'iron (metal)': 'das Eisen',
 'mad': 'verrückt; wütend',
 'prepared': 'vorbereitet, bereit',
 'reference': 'der Verweis, die Referenz',
 'to guard': 'bewachen',
 'a mention': 'die Erwähnung',
 'port': 'der Hafen',
 'a kick': 'der Tritt',
 'advanced': 'fortgeschritten',
 'alternative (adj.)': 'alternativ',
 'a mix': 'die Mischung',
 'to mix': 'mischen',
 'spending': 'die Ausgaben',
 'environmental': 'Umwelt-, ökologisch',
 'fixed': 'fest',
 'to limit': 'begrenzen',
 'originally': 'ursprünglich',
 'to update': 'aktualisieren',
 'to flow': 'fließen',
 'to transport': 'transportieren',
 'a pack': 'die Packung',
 'chapter': 'das Kapitel',
 'specifically': 'speziell, ausdrücklich',
 'determined': 'entschlossen',
 'an escape': 'die Flucht',
 'to escape': 'fliehen, entkommen',
 'properly': 'richtig, ordentlich',
 'experienced': 'erfahren',
 'whenever': 'wann immer',
 'literature': 'die Literatur',
 'to signal': 'signalisieren',
 'typically': 'typischerweise',
 'to wave': 'winken',
 'medium (adj.)': 'mittel',
 'perfectly': 'perfekt',
 'to bomb': 'bombardieren',
 'educational': 'pädagogisch, Bildungs-',
 'mainly': 'hauptsächlich',
 'row': 'die Reihe',
 'to switch': 'wechseln, umschalten',
 'bell': 'die Glocke, die Klingel',
 'warning': 'die Warnung',
 'definition': 'die Definition',
 'frame': 'der Rahmen',
 'to frame': 'einrahmen',
 'a kiss': 'der Kuss',
 'category': 'die Kategorie',
 'personally': 'persönlich',
 'frequently': 'häufig',
 'to arrest': 'verhaften',
 'ban': 'das Verbot',
 'to ban': 'verbieten',
 'to tip': 'Trinkgeld geben',
 'heavily': 'stark, schwer',
 'worldwide': 'weltweit',
 'princess': 'die Prinzessin',
 'sample': 'die Probe',
 'engaged': 'verlobt; besetzt',
 'regularly': 'regelmäßig',
 'an aim': 'das Ziel',
 'to aim': 'zielen, anstreben',
 'campus': 'der Campus',
 'comparison': 'der Vergleich',
 'injured': 'verletzt',
 'a musical': 'das Musical',
 'organized': 'organisiert',
 'a quote': 'das Zitat',
 'to quote': 'zitieren',
 'valuable': 'wertvoll',
 'aged': 'im Alter von',
 'to graduate': 'den Abschluss machen',
 'racing': 'der Rennsport',
 'effectively': 'wirksam',
 'historic': 'historisch',
 'improvement': 'die Verbesserung',
 'a repeat': 'die Wiederholung',
 'naturally': 'natürlich',
 'necessarily': 'notwendigerweise',
 'percentage': 'der Prozentsatz',
 'to trick': 'austricksen',
 'confused': 'verwirrt',
 'strongly': 'stark',
 'technique': 'die Technik',
 'contrast': 'der Kontrast',
 'to contrast': 'gegenüberstellen',
 'element': 'das Element',
 'photography': 'die Fotografie',
 'to protest': 'protestieren',
 'spoken': 'gesprochen',
 'successfully': 'erfolgreich',
 'retired': 'pensioniert',
 'sand': 'der Sand',
 'tape': 'das Klebeband; das Band',
 'label': 'das Etikett',
 'to label': 'beschriften',
 'diamond': 'der Diamant',
 'dressed': 'angezogen',
 'odd': 'seltsam; ungerade',
 'a repair': 'die Reparatur',
 'annoying': 'nervig',
 'conclusion': 'der Schluss, die Schlussfolgerung',
 'rugby': 'das Rugby',
 'liquid (adj.)': 'flüssig',
 'shell': 'die Schale, die Muschel',
 'incredibly': 'unglaublich',
 'seed': 'der Samen',
 'summary': 'die Zusammenfassung',
 'script': 'das Drehbuch; das Skript',
 'tube': 'die Röhre; die U-Bahn (London)',
 'cotton': 'die Baumwolle',
 'a knock': 'das Klopfen',
 'luxury (adj.)': 'Luxus-',
 'to flood': 'überfluten',
 'punishment': 'die Strafe',
 'a shake': 'das Schütteln; der Shake',
 'announcement': 'die Ankündigung',
 'a bite': 'der Biss',
 'documentary': 'der Dokumentarfilm',
 'explore': 'erkunden',
 'presentation': 'die Präsentation',
 'similarly': 'ebenso',
 'talented': 'talentiert',
 'educated': 'gebildet',
 'mall': 'das Einkaufszentrum',
 'breathing': 'das Atmen',
 'photographer': 'der Fotograf',
 'pin': 'die Nadel; die PIN',
 'to pin': 'anstecken, anheften',
 'printing': 'der Druck',
 'repeated': 'wiederholt',
 'to volunteer': 'sich freiwillig melden',
 'garage': 'die Garage',
 'poem': 'das Gedicht',
 'an export': 'der Export',
 'robot': 'der Roboter',
 'a climb': 'der Aufstieg',
 'folk': 'Volks-',
 'unemployment': 'die Arbeitslosigkeit',
 'a highlight': 'der Höhepunkt',
 'nail': 'der Nagel',
 'poet': 'der Dichter',
 'sink': 'sinken',
 'a swim': 'das Schwimmen',
 'coin': 'die Münze',
 'costume': 'das Kostüm',
 'examine': 'untersuchen',
 'mixture': 'die Mischung',
 'shine': 'scheinen, glänzen',
 'apologize': 'sich entschuldigen',
 'bubble': 'die Blase',
 'gentleman': 'der Herr',
 'ours': 'unserer',
 'embarrassing': 'peinlich',
 'a hurry': 'die Eile',
 'a bend': 'die Kurve',
 'to bend': 'biegen, sich bücken',
 'fascinating': 'faszinierend',
 'helicopter': 'der Hubschrauber',
 'lip': 'die Lippe',
 'mud': 'der Schlamm',
 'drum': 'die Trommel',
 'an import': 'der Import',
 'to poison': 'vergiften',
 'toe': 'der Zeh',
 'a cheat': 'der Betrüger',
 'embarrassed': 'verlegen',
 'backwards': 'rückwärts',
 'container': 'der Behälter',
 'tin': 'das Blech; die Dose',
 'disappointing': 'enttäuschend',
 'relaxed': 'entspannt',
 'a sail': 'das Segel',
 'to slice': 'in Scheiben schneiden',
 'theirs': 'ihrer',
 'ambitious': 'ehrgeizig',
 'annoyed': 'verärgert',
 'locate': 'ausfindig machen',
 'old-fashioned': 'altmodisch',
 'coloured': 'farbig',
 'alcoholic': 'alkoholisch',
 'amazed': 'erstaunt',
 'conclude': 'folgern; abschließen',
 'relaxing': 'entspannend',
 'a dislike': 'die Abneigung',
 'diagram': 'das Diagramm',
 'to queue': 'Schlange stehen',
 'sailor': 'der Seemann',
 'viewer': 'der Zuschauer',
 'frightened': 'verängstigt',
 'glove': 'der Handschuh',
 'outdoors': 'draußen',
 'confuse': 'verwirren',
 'frightening': 'beängstigend',
 'symptom': 'das Symptom',
 'careless': 'unvorsichtig',
 'cheerful': 'fröhlich',
 'indoors': 'drinnen',
 'similarity': 'die Ähnlichkeit',
 'organizer': 'der Organisator',
 'poisonous': 'giftig',
 'quotation': 'das Zitat; das Angebot',
 'statistic': 'die Statistik',
 'decorate': 'dekorieren',
 'injure': 'verletzen',
 'summarize': 'zusammenfassen',
 'frighten': 'erschrecken',
 'being': 'das Wesen',
 'make-up': 'das Make-up',
 'to found': 'gründen',
 'so-called': 'sogenannt',
 'means': 'das Mittel',
 'to level': 'ebnen',
 'a current': 'die Strömung; der Strom',
 'to process': 'verarbeiten',
 'self': 'das Selbst',
 'to issue': 'ausstellen, herausgeben',
 'shot': 'der Schuss; die Aufnahme',
 'county': 'die Grafschaft, der Landkreis',
 'league': 'die Liga',
 'long-term': 'langfristig',
 'to model': 'modellieren',
 'lower': 'senken',
 'hell': 'die Hölle',
 'lord': 'der Herr, der Lord',
 'to stage': 'inszenieren',
 'terms': 'die Bedingungen',
 'super': 'super',
 'to figure': 'glauben, sich denken',
 'minister': 'der Minister',
 'limited': 'begrenzt',
 'moving': 'bewegend',
 'via': 'über',
 'potential (adj.)': 'möglich, potenziell',
 'additional': 'zusätzlich',
 'short-term': 'kurzfristig',
 'opening': 'die Eröffnung; die Öffnung',
 'cancer': 'der Krebs',
 'commission': 'die Kommission; die Provision',
 'grand': 'großartig, Groß-',
 'literally': 'buchstäblich',
 'gay': 'schwul',
 'associated': 'verbunden',
 'finding': 'das Ergebnis, der Befund',
 'species': 'die Art',
 'to structure': 'strukturieren',
 'arms': 'die Waffen',
 'estate': 'das Anwesen; die Wohnsiedlung',
 'failed': 'gescheitert',
 'hearing': 'das Gehör; die Anhörung',
 'rose': 'die Rose',
 'chairman': 'der Vorsitzende',
 'edition': 'die Ausgabe',
 'a bet': 'die Wette',
 'to bet': 'wetten',
 'cast': 'die Besetzung',
 'to cast': 'werfen; besetzen',
 'to function': 'funktionieren',
 'shooting': 'die Schießerei; der Dreh',
 'housing': 'der Wohnraum',
 'leadership': 'die Führung',
 'aid': 'die Hilfe',
 'to aid': 'helfen',
 'concerned': 'besorgt; betroffen',
 'investigation': 'die Untersuchung, die Ermittlung',
 'democratic': 'demokratisch',
 'willing': 'bereit',
 'intended': 'beabsichtigt',
 'to survey': 'befragen; überblicken',
 'era': 'die Ära',
 'testing': 'das Testen',
 'aircraft': 'das Flugzeug',
 'distribution': 'die Verteilung',
 'mixed': 'gemischt',
 'basically': 'im Grunde',
 'funding': 'die Finanzierung',
 'mode': 'der Modus',
 'trading': 'der Handel',
 'jail': 'das Gefängnis',
 'to jail': 'einsperren',
 'voting': 'die Abstimmung',
 'draft': 'der Entwurf',
 'ID': 'der Ausweis',
 'info': 'die Info',
 'a switch': 'der Schalter',
 'armed': 'bewaffnet',
 'assistance': 'die Unterstützung',
 'a blow': 'der Schlag',
 'saving': 'die Ersparnis',
 'recovery': 'die Erholung; die Wiederherstellung',
 'transportation': 'der Transport',
 'manufacturing': 'die Herstellung',
 'carbon': 'der Kohlenstoff',
 'mate': 'der Kumpel',
 'nearby': 'nahe gelegen',
 'somewhat': 'etwas, ziemlich',
 'absolute': 'absolut',
 'cable': 'das Kabel',
 'championship': 'die Meisterschaft',
 'incident': 'der Vorfall',
 'reporting': 'die Berichterstattung',
 'widely': 'weithin',
 'closely': 'eng, genau',
 'constantly': 'ständig',
 'motor': 'der Motor',
 'protein': 'das Protein',
 'raw': 'roh',
 'suffering': 'das Leiden',
 'unknown': 'unbekannt',
 'automatically': 'automatisch',
 'blind': 'blind',
 'fantasy': 'die Fantasie',
 'steam': 'der Dampf',
 'commander': 'der Kommandant',
 'detailed': 'detailliert',
 'opposed': 'dagegen',
 'get rid of': 'loswerden',
 'bush': 'der Busch',
 'formation': 'die Bildung, die Formation',
 'surrounding': 'umliegend',
 'universal': 'universell, allgemein',
 'partnership': 'die Partnerschaft',
 'audio': 'Audio-',
 'format': 'das Format',
 'healthcare': 'das Gesundheitswesen',
 'immigration': 'die Einwanderung',
 'membership': 'die Mitgliedschaft',
 'mount': 'montieren; besteigen',
 'shortly': 'in Kürze',
 'bound': 'sicher; gebunden',
 'extension': 'die Verlängerung; die Durchwahl',
 'hip': 'die Hüfte',
 'infrastructure': 'die Infrastruktur',
 'moral': 'moralisch',
 'a moral': 'die Moral',
 'pointed': 'spitz; gezielt',
 'alongside': 'neben, zusammen mit',
 'flash': 'der Blitz',
 'to flash': 'blinken',
 'rating': 'die Bewertung',
 'deeply': 'zutiefst',
 'rank': 'der Rang',
 'tag': 'das Etikett, der Tag',
 'to tag': 'markieren',
 'pitch': 'das Spielfeld; die Tonhöhe',
 'comic': 'komisch',
 'a comic': 'der Comic',
 'economics': 'die Wirtschaftswissenschaft',
 'hunting': 'die Jagd',
 'kit': 'die Ausrüstung, das Set',
 'racist': 'rassistisch',
 'sexy': 'sexy',
 'whoever': 'wer auch immer',
 'deck': 'das Deck; das Kartenspiel',
 'lately': 'in letzter Zeit',
 'rail': 'die Schiene; das Geländer',
 'bid': 'das Angebot, das Gebot',
 'to bid': 'bieten',
 'convinced': 'überzeugt',
 'landing': 'die Landung',
 'ownership': 'das Eigentum',
 'associate': 'verbinden, assoziieren',
 'to broadcast': 'senden, übertragen',
 'potentially': 'möglicherweise',
 'commonly': 'häufig',
 'forum': 'das Forum',
 'shaped': 'förmig',
 'programming': 'die Programmierung',
 'publishing': 'das Verlagswesen',
 'gaming': 'das Gaming',
 'gene': 'das Gen',
 'roughly': 'ungefähr',
 'breast': 'die Brust',
 'rob': 'ausrauben',
 'terrorist': 'der Terrorist',
 'impressed': 'beeindruckt',
 'rapidly': 'rasch',
 'sum': 'die Summe',
 'to sum up': 'zusammenfassen',
 'elementary': 'elementar, Grund-',
 'ethnic': 'ethnisch',
 'greatly': 'erheblich',
 'infection': 'die Infektion',
 'participation': 'die Teilnahme',
 'satellite': 'der Satellit',
 'aggressive': 'aggressiv',
 'innovation': 'die Innovation',
 'nursing': 'die Krankenpflege',
 'operator': 'der Betreiber, der Bediener',
 'database': 'die Datenbank',
 'rocket': 'die Rakete',
 'terminal': 'das Terminal',
 'bat': 'die Fledermaus; der Schläger',
 'darkness': 'die Dunkelheit',
 'slide': 'die Rutsche; die Folie',
 'to slide': 'rutschen, gleiten',
 'disabled': 'behindert',
 'drag': 'ziehen',
 'jet': 'der Jet',
 'lighting': 'die Beleuchtung',
 'timing': 'das Timing',
 'ton': 'die Tonne',
 'consideration': 'die Überlegung; die Rücksicht',
 'logo': 'das Logo',
 'tap': 'der Wasserhahn',
 'to tap': 'tippen, klopfen',
 'challenging': 'herausfordernd',
 'opera': 'die Oper',
 'a parallel': 'die Parallele',
 'psychological': 'psychologisch',
 'radiation': 'die Strahlung',
 'shocked': 'schockiert',
 'tune': 'die Melodie',
 'clip': 'der Clip; die Klammer',
 'brick': 'der Ziegel',
 'inspector': 'der Inspektor',
 'racism': 'der Rassismus',
 'consistently': 'durchgehend',
 'formerly': 'früher',
 'isolated': 'isoliert',
 'neutral': 'neutral',
 'popularity': 'die Beliebtheit',
 'terrorism': 'der Terrorismus',
 'graphic': 'grafisch; drastisch',
 'instantly': 'sofort',
 'palm': 'die Handfläche; die Palme',
 'rubber': 'der Gummi; der Radiergummi',
 'accidentally': 'versehentlich',
 'affordable': 'erschwinglich',
 'canal': 'der Kanal',
 'completion': 'die Fertigstellung',
 'cruise': 'die Kreuzfahrt',
 'motivation': 'die Motivation',
 'outfit': 'das Outfit',
 'gradually': 'allmählich',
 'additionally': 'zusätzlich',
 'bug': 'der Käfer; der Fehler',
 'cave': 'die Höhle',
 'punk': 'der Punk',
 'bacteria': 'die Bakterien',
 'beside': 'neben',
 'confusion': 'die Verwirrung',
 'dealer': 'der Händler',
 'electronics': 'die Elektronik',
 'exploration': 'die Erforschung',
 'graphics': 'die Grafik',
 'nerve': 'der Nerv; der Mut',
 'sustainable': 'nachhaltig',
 'weakness': 'die Schwäche',
 'animation': 'die Animation',
 'balanced': 'ausgewogen',
 'compound': 'die Verbindung; das Gelände',
 'tropical': 'tropisch',
 'artistic': 'künstlerisch',
 'genre': 'das Genre',
 'lens': 'die Linse; das Objektiv',
 'rat': 'die Ratte',
 'annually': 'jährlich',
 'icon': 'das Symbol; die Ikone',
 'installation': 'die Installation',
 'marathon': 'der Marathon',
 'parade': 'die Parade',
 'scratch': 'der Kratzer',
 'to scratch': 'kratzen',
 'sometime': 'irgendwann',
 'sporting': 'sportlich, Sport-',
 'strictly': 'streng',
 'teens': 'die Teenagerjahre',
 'medication': 'das Medikament',
 'screening': 'die Untersuchung; die Vorführung',
 'workshop': 'die Werkstatt, der Workshop',
 'depressed': 'deprimiert',
 'inflation': 'die Inflation',
 'lean': 'sich lehnen',
 'organ': 'das Organ; die Orgel',
 'pile': 'der Haufen',
 'to pile': 'stapeln',
 'tragedy': 'die Tragödie',
 'arrow': 'der Pfeil',
 'cabin': 'die Kabine; die Hütte',
 'consultant': 'der Berater',
 'flexible': 'flexibel',
 'owe': 'schulden',
 'skilled': 'qualifiziert',
 'surgeon': 'der Chirurg',
 'a dive': 'der Tauchgang; der Sprung',
 'to dive': 'tauchen',
 'artwork': 'das Kunstwerk',
 'defender': 'der Verteidiger',
 'entertaining': 'unterhaltsam',
 'openly': 'offen',
 'promising': 'vielversprechend',
 'silk': 'die Seide',
 'genuinely': 'wirklich',
 'matching': 'passend',
 'purely': 'rein',
 'severely': 'schwer',
 'shocking': 'schockierend',
 'bombing': 'der Bombenanschlag',
 'dairy': 'die Milchprodukte',
 'delighted': 'hocherfreut',
 'receiver': 'der Hörer; der Empfänger',
 'thoroughly': 'gründlich',
 'dump': 'abladen',
 'permanently': 'dauerhaft',
 'tragic': 'tragisch',
 'basket': 'der Korb',
 'charming': 'charmant',
 'ethical': 'ethisch',
 'freely': 'frei',
 'ink': 'die Tinte',
 'a cheer': 'der Jubel',
 'to cheer': 'jubeln',
 'demonstration': 'die Demonstration',
 'grocery': 'der Lebensmittelladen',
 'temporarily': 'vorübergehend',
 'beg': 'betteln, anflehen',
 'declare': 'erklären; deklarieren',
 'dot': 'der Punkt',
 'measurement': 'die Messung',
 'sophisticated': 'ausgeklügelt; kultiviert',
 'warming': 'die Erwärmung',
 'emotionally': 'emotional',
 'workplace': 'der Arbeitsplatz',
 'navigation': 'die Navigation',
 'reasonably': 'ziemlich; vernünftig',
 'confusing': 'verwirrend',
 'an extract': 'der Auszug',
 'civilization': 'die Zivilisation',
 'creativity': 'die Kreativität',
 'disk': 'die Festplatte, die Scheibe',
 'considerably': 'beträchtlich',
 'firmly': 'fest',
 'recruitment': 'die Personalbeschaffung',
 'accurately': 'genau',
 'desperately': 'verzweifelt',
 'gig': 'der Auftritt',
 'resign': 'zurücktreten, kündigen',
 'robbery': 'der Raub',
 'rub': 'reiben',
 'therapist': 'der Therapeut',
 'coincidence': 'der Zufall',
 'investor': 'der Investor',
 'offence': 'die Straftat; die Beleidigung',
 'ballet': 'das Ballett',
 'dramatically': 'drastisch',
 'relieved': 'erleichtert',
 'risky': 'riskant',
 'workforce': 'die Belegschaft',
 'enjoyable': 'angenehm',
 'terribly': 'schrecklich',
 'balloon': 'der Ballon',
 'rebuild': 'wieder aufbauen',
 'fond': 'gern haben',
 'critically': 'kritisch',
 'economist': 'der Ökonom',
 'extensively': 'ausgiebig',
 'marker': 'der Marker',
 'optimistic': 'optimistisch',
 'judgement': 'das Urteil',
 'composer': 'der Komponist',
 'enthusiastic': 'begeistert',
 'steadily': 'stetig',
 'curved': 'gebogen',
 'depressing': 'deprimierend',
 'humour': 'der Humor',
 'certainty': 'die Gewissheit',
 'decoration': 'die Dekoration',
 'obesity': 'die Fettleibigkeit',
 'psychologist': 'der Psychologe',
 'sufficiently': 'ausreichend',
 'efficiently': 'effizient',
 'stall': 'der Stand',
 'trillion': 'die Billion',
 'negotiation': 'die Verhandlung',
 'chop': 'hacken, klein schneiden',
 'fundamentally': 'grundlegend',
 'remarkably': 'bemerkenswert',
 'amusing': 'amüsant',
 'predictable': 'vorhersehbar',
 'cue': 'das Stichwort',
 'upwards': 'aufwärts',
 'appropriately': 'angemessen',
 'slogan': 'der Slogan',
 'sponsorship': 'das Sponsoring',
 'accuse': 'beschuldigen',
 'distract': 'ablenken',
 'litter': 'der Müll',
 'compulsory': 'verpflichtend',
 'emission': 'die Emission',
 'folding': 'Klapp-',
 'offender': 'der Täter',
 'emphasize': 'betonen',
 'feather': 'die Feder',
 'troop': 'die Truppe',
 'suspend': 'aussetzen, suspendieren',
 'astonishing': 'erstaunlich',
 'disappoint': 'enttäuschen',
 'stimulate': 'anregen',
 'wander': 'umherwandern',
 'disagreement': 'die Meinungsverschiedenheit',
 'adequately': 'angemessen',
 'applicant': 'der Bewerber',
 'spokesperson': 'der Sprecher',
 'viewpoint': 'der Standpunkt',
 'broadcaster': 'der Sender',
 'criticize': 'kritisieren',
 'lyric': 'der Liedtext',
 'invade': 'einmarschieren',
 'novelist': 'der Romanautor',
 'sibling': 'das Geschwister',
 'humorous': 'humorvoll',
 'motivate': 'motivieren',
 'miner': 'der Bergmann',
 'offend': 'beleidigen',
 'fragment': 'das Fragment',
 'impatient': 'ungeduldig',
 'ethic': 'die Ethik',
 'devote': 'widmen',
 'dishonest': 'unehrlich',
 'inherit': 'erben',
 'starve': 'verhungern',
 'tsunami': 'der Tsunami',
 'spectator': 'der Zuschauer',
 'equip': 'ausstatten',
 'ancestor': 'der Vorfahr',
 'compose': 'komponieren; verfassen',
 'globalization': 'die Globalisierung',
 'unfold': 'entfalten',
 'enquiry': 'die Anfrage',
 'seeker': 'der Suchende',
 'firefighter': 'der Feuerwehrmann',
 'specialize': 'sich spezialisieren',
 'tonne': 'die Tonne',
 'downwards': 'abwärts',
 'settler': 'der Siedler',
 'leaflet': 'das Flugblatt, der Prospekt',
 'spokeswoman': 'die Sprecherin',
 'protester': 'der Demonstrant',
 'erupt': 'ausbrechen',
 'firework': 'das Feuerwerk',
 'precede': 'vorausgehen',
 'terrify': 'in Angst versetzen',
 'long-time': 'langjährig',
 'well-being': 'das Wohlbefinden',
 'to top': 'übertreffen',
 'set-up': 'der Aufbau',
 'line-up': 'die Aufstellung',
 'post-war': 'Nachkriegs-',
 'to rock': 'schaukeln',
 'decision-making': 'die Entscheidungsfindung',
 'to pop': 'platzen; vorbeischauen',
 'standing': 'ständig',
 'long-standing': 'langjährig',
 'remains': 'die Überreste',
 'high-profile': 'prominent',
 'bay': 'die Bucht',
 'large-scale': 'groß angelegt',
 'vice': 'das Laster',
 'ray': 'der Strahl',
 'squad': 'die Mannschaft, der Trupp',
 'passing': 'das Vorbeigehen; das Ableben',
 'suicide': 'der Selbstmord',
 'solo': 'Solo-',
 'non-profit': 'gemeinnützig',
 'offering': 'das Angebot; die Opfergabe',
 'dedicated': 'engagiert; eigens dafür',
 'senator': 'der Senator',
 'academy': 'die Akademie',
 'crown': 'die Krone',
 'mining': 'der Bergbau',
 'premier': 'führend, Premier-',
 'interior': 'innere, Innen-',
 'the interior': 'das Innere',
 'resistance': 'der Widerstand',
 'marine': 'Meeres-',
 'debut': 'das Debüt',
 'to license': 'lizenzieren',
 'presidential': 'Präsidentschafts-',
 'shipping': 'der Versand',
 'auto': 'das Auto',
 'the accused': 'der Angeklagte',
 'processing': 'die Verarbeitung',
 'angel': 'der Engel',
 'bonus': 'der Bonus, die Prämie',
 'enforcement': 'die Durchsetzung',
 'gross': 'brutto; eklig',
 'replacement': 'der Ersatz',
 'thread': 'der Faden; der Thread',
 'commissioner': 'der Kommissar',
 'memorial': 'das Denkmal',
 'saint': 'der Heilige',
 'buddy': 'der Kumpel',
 'elite': 'die Elite',
 'forth': 'weiter, hervor',
 'sake': 'um … willen',
 'bench': 'die Bank',
 'handling': 'die Handhabung',
 'idiot': 'der Idiot',
 'bishop': 'der Bischof',
 'defensive': 'defensiv',
 'mill': 'die Mühle; das Werk',
 'spin': 'die Drehung',
 'to spin': 'drehen',
 'cop': 'der Bulle',
 'legacy': 'das Erbe',
 'log': 'der Holzklotz; das Protokoll',
 'to log': 'protokollieren',
 'sin': 'die Sünde',
 'sword': 'das Schwert',
 'ward': 'die Station',
 'strip': 'der Streifen',
 'to strip': 'abziehen; sich ausziehen',
 'corruption': 'die Korruption',
 'agricultural': 'landwirtschaftlich',
 'ease': 'die Leichtigkeit',
 'to ease': 'lindern',
 'rally': 'die Kundgebung; die Rallye',
 'to rally': 'sich sammeln; sich erholen',
 'upcoming': 'bevorstehend',
 'alert': 'wachsam',
 'to alert': 'alarmieren, warnen',
 'arena': 'die Arena',
 'boom': 'der Boom',
 'constitutional': 'verfassungsmäßig',
 'density': 'die Dichte',
 'pregnancy': 'die Schwangerschaft',
 'communist': 'kommunistisch',
 'legislative': 'gesetzgebend',
 'listing': 'die Auflistung, das Inserat',
 'trailer': 'der Trailer; der Anhänger',
 'versus': 'gegen',
 'discrimination': 'die Diskriminierung',
 'a bow': 'der Bogen; die Verbeugung',
 'to bow': 'sich verbeugen',
 'devil': 'der Teufel',
 'hardware': 'die Hardware',
 'petition': 'die Petition',
 'stem': 'der Stiel, der Stamm',
 'franchise': 'das Franchise',
 'integrated': 'integriert',
 'ruling': 'das Urteil',
 'bass': 'der Bass',
 'collaboration': 'die Zusammenarbeit',
 'experimental': 'experimentell',
 'odds': 'die Chancen; die Quote',
 'copper': 'das Kupfer',
 'pit': 'die Grube',
 'weed': 'das Unkraut',
 'acquisition': 'der Erwerb; die Übernahme',
 'rip': 'reißen',
 'gathering': 'das Treffen',
 'screw': 'die Schraube',
 'to screw': 'schrauben',
 'abortion': 'die Abtreibung',
 'copyright': 'das Urheberrecht',
 'exclusively': 'ausschließlich',
 'naval': 'Marine-',
 'spy': 'der Spion',
 'to spy': 'spionieren',
 'warrant': 'der Haftbefehl, der Durchsuchungsbefehl',
 'backing': 'die Unterstützung',
 'charter': 'die Charta; der Charter',
 'legendary': 'legendär',
 'pole': 'die Stange; der Pol',
 'regulatory': 'regulatorisch',
 'serial': 'Serien-',
 'shed': 'vergießen; abwerfen',
 'syndrome': 'das Syndrom',
 'custody': 'das Sorgerecht; die Haft',
 'fluid': 'die Flüssigkeit',
 'integration': 'die Integration',
 'magical': 'magisch',
 'socialist': 'sozialistisch',
 'sue': 'verklagen',
 'backup': 'die Sicherung, das Backup',
 'creator': 'der Schöpfer',
 'operational': 'betriebsbereit',
 'skip': 'überspringen',
 'snap': 'zerbrechen; schnappen',
 'transformation': 'die Verwandlung',
 'chronic': 'chronisch',
 'diagnosis': 'die Diagnose',
 'flesh': 'das Fleisch',
 'laser': 'der Laser',
 'radar': 'das Radar',
 'striking': 'auffallend',
 'transit': 'der Transit; der Nahverkehr',
 'bulk': 'die Masse; der Großteil',
 'coastal': 'Küsten-',
 'commentary': 'der Kommentar',
 'congressional': 'Kongress-',
 'raid': 'die Razzia',
 'ranking': 'die Rangliste',
 'situated': 'gelegen',
 'tobacco': 'der Tabak',
 'a trace': 'die Spur',
 'classification': 'die Klassifizierung',
 'film-maker': 'der Filmemacher',
 'grid': 'das Raster; das Netz',
 'identification': 'die Identifizierung',
 'lap': 'der Schoß; die Runde',
 'liver': 'die Leber',
 'parliamentary': 'parlamentarisch',
 'physician': 'der Arzt',
 'rifle': 'das Gewehr',
 'structural': 'strukturell',
 'suite': 'die Suite',
 'verse': 'der Vers',
 'adoption': 'die Adoption; die Annahme',
 'attendance': 'die Anwesenheit',
 'barrel': 'das Fass; der Lauf',
 'bless': 'segnen',
 'colonial': 'kolonial',
 'crush': 'zerquetschen',
 'dam': 'der Damm',
 'magnetic': 'magnetisch',
 'reflection': 'das Spiegelbild; die Überlegung',
 'revolutionary': 'revolutionär',
 'simultaneously': 'gleichzeitig',
 'surveillance': 'die Überwachung',
 'trophy': 'die Trophäe',
 'ash': 'die Asche',
 'casino': 'das Kasino',
 'indigenous': 'einheimisch, indigen',
 'legislature': 'die Legislative',
 'presidency': 'die Präsidentschaft',
 'warrior': 'der Krieger',
 'burst': 'platzen',
 'cattle': 'das Vieh',
 'lesbian': 'lesbisch',
 'portfolio': 'das Portfolio',
 'productivity': 'die Produktivität',
 'violation': 'der Verstoß',
 'beam': 'der Balken; der Strahl',
 'encouraging': 'ermutigend',
 'horn': 'das Horn; die Hupe',
 'inspection': 'die Inspektion',
 'intensity': 'die Intensität',
 'meaningful': 'sinnvoll',
 'migration': 'die Migration',
 'missile': 'die Rakete',
 'patrol': 'die Patrouille',
 'rod': 'die Stange',
 'in accordance with': 'gemäß',
 'activist': 'der Aktivist',
 'alike': 'ähnlich',
 'corresponding': 'entsprechend',
 'engaging': 'fesselnd',
 'reportedly': 'angeblich',
 'separation': 'die Trennung',
 'feminist': 'feministisch',
 'reminder': 'die Erinnerung',
 'resume': 'wieder aufnehmen',
 'variable (adj.)': 'variabel',
 'parish': 'die Gemeinde',
 'ally': 'der Verbündete',
 'rental': 'die Miete, der Verleih',
 'seemingly': 'scheinbar',
 'slot': 'der Schlitz; das Zeitfenster',
 'duo': 'das Duo',
 'frustrated': 'frustriert',
 'gambling': 'das Glücksspiel',
 'layout': 'das Layout',
 'pastor': 'der Pastor',
 'provincial': 'Provinz-',
 'administrator': 'der Administrator',
 'nationwide': 'landesweit',
 'optical': 'optisch',
 'specialized': 'spezialisiert',
 'allegedly': 'angeblich',
 'blessing': 'der Segen',
 'demon': 'der Dämon',
 'interactive': 'interaktiv',
 'pronounced': 'ausgeprägt',
 'dip': 'eintauchen',
 'disturbing': 'verstörend',
 'effectiveness': 'die Wirksamkeit',
 'frankly': 'offen gesagt',
 'medieval': 'mittelalterlich',
 'mobility': 'die Mobilität',
 'orientation': 'die Orientierung',
 'proceeds': 'der Erlös',
 'spam': 'der Spam',
 'withdrawal': 'der Rückzug; die Abhebung',
 'echo': 'das Echo',
 'to echo': 'widerhallen',
 'in the meantime': 'in der Zwischenzeit',
 'pipeline': 'die Pipeline',
 'mob': 'die Menge; der Mob',
 'tribal': 'Stammes-',
 'aesthetic': 'ästhetisch',
 'complexity': 'die Komplexität',
 'ego': 'das Ego',
 'flexibility': 'die Flexibilität',
 'gut': 'der Darm; das Bauchgefühl',
 'resignation': 'der Rücktritt, die Kündigung',
 'utterly': 'völlig',
 'buck': 'der Dollar (ugs.)',
 'harassment': 'die Belästigung',
 'pad': 'das Polster; der Block',
 'whip': 'peitschen; schlagen',
 'disclosure': 'die Offenlegung',
 'instrumental': 'maßgeblich; instrumental',
 'probe': 'die Untersuchung; die Sonde',
 'rehabilitation': 'die Rehabilitation',
 'archive': 'das Archiv',
 'frustrating': 'frustrierend',
 'frustration': 'die Frustration',
 'scattered': 'verstreut',
 'sexuality': 'die Sexualität',
 'architectural': 'architektonisch',
 'dedication': 'die Hingabe; die Widmung',
 'reconstruction': 'der Wiederaufbau',
 'renowned': 'renommiert',
 'supposedly': 'angeblich',
 'wit': 'der Witz, der Geist',
 'appealing': 'ansprechend',
 'correction': 'die Korrektur',
 'documentation': 'die Dokumentation',
 'mainland': 'das Festland',
 'meditation': 'die Meditation',
 'philosophical': 'philosophisch',
 'sensitivity': 'die Empfindlichkeit',
 'simulation': 'die Simulation',
 'supervision': 'die Aufsicht',
 'thrilled': 'begeistert',
 'trio': 'das Trio',
 'battlefield': 'das Schlachtfeld',
 'desktop': 'der Desktop',
 'readily': 'bereitwillig',
 'delegation': 'die Delegation',
 'hail': 'feiern; herbeirufen',
 'catalogue': 'der Katalog',
 'continually': 'ständig',
 'coordinator': 'der Koordinator',
 'damaging': 'schädlich',
 'deployment': 'der Einsatz',
 'genocide': 'der Völkermord',
 'massacre': 'das Massaker',
 'sack': 'feuern',
 'suburban': 'vorstädtisch',
 'troubled': 'problematisch',
 'coordination': 'die Koordination',
 'lad': 'der Junge',
 'obsession': 'die Besessenheit',
 'opt': 'sich entscheiden',
 'rejection': 'die Ablehnung',
 'browser': 'der Browser',
 'cocktail': 'der Cocktail',
 'imprisonment': 'die Haft',
 'trademark': 'das Markenzeichen',
 'adjustment': 'die Anpassung',
 'undoubtedly': 'zweifellos',
 'inclined': 'geneigt',
 'problematic': 'problematisch',
 'processor': 'der Prozessor',
 'psychiatric': 'psychiatrisch',
 'cooperative': 'kooperativ',
 'prestigious': 'angesehen',
 'symbolic': 'symbolisch',
 'carriage': 'der Wagen; die Kutsche',
 'manipulation': 'die Manipulation',
 'undergraduate': 'der Student (Bachelor)',
 'creep': 'kriechen, schleichen',
 'exploitation': 'die Ausbeutung',
 'activation': 'die Aktivierung',
 'critique': 'die Kritik',
 'investigator': 'der Ermittler',
 'organizational': 'organisatorisch',
 'assassination': 'das Attentat',
 'congregation': 'die Gemeinde',
 'coordinate': 'koordinieren',
 'evolutionary': 'evolutionär',
 'marketplace': 'der Marktplatz',
 'fundraising': 'die Spendensammlung',
 'memo': 'das Memo',
 'ironic': 'ironisch',
 'minimize': 'minimieren',
 'thankfully': 'zum Glück',
 'capitalist': 'kapitalistisch',
 'encouragement': 'die Ermutigung',
 'alignment': 'die Ausrichtung',
 'ecological': 'ökologisch',
 'forge': 'fälschen; schmieden',
 'parental': 'elterlich',
 'stab': 'erstechen',
 'embarrassment': 'die Verlegenheit',
 'fairness': 'die Fairness',
 'ideological': 'ideologisch',
 'insider': 'der Insider',
 'neighbouring': 'benachbart',
 'calculation': 'die Berechnung',
 'newsletter': 'der Newsletter',
 'bind': 'binden',
 'conception': 'die Vorstellung; die Empfängnis',
 'deed': 'die Tat; die Urkunde',
 'gallon': 'die Gallone',
 'relevance': 'die Relevanz',
 'utilize': 'nutzen',
 'emergence': 'das Aufkommen',
 'ironically': 'ironischerweise',
 'nod': 'nicken',
 'aluminium': 'das Aluminium',
 'confrontation': 'die Konfrontation',
 'contributor': 'der Beitragende',
 'dismissal': 'die Entlassung',
 'philosopher': 'der Philosoph',
 'presently': 'derzeit',
 'realization': 'die Erkenntnis; die Verwirklichung',
 'steer': 'lenken',
 'magistrate': 'der Friedensrichter',
 'predator': 'das Raubtier',
 'tactic': 'die Taktik',
 'appoint': 'ernennen',
 'counterpart': 'das Gegenstück, der Amtskollege',
 'a gaze': 'der Blick',
 'to gaze': 'starren',
 'indictment': 'die Anklage',
 'limb': 'das Glied',
 'transcript': 'das Protokoll, die Abschrift',
 'accomplishment': 'die Leistung',
 'aide': 'der Berater, der Assistent',
 'broadband': 'das Breitband',
 'constituency': 'der Wahlkreis',
 'councillor': 'der Stadtrat',
 'diplomat': 'der Diplomat',
 'firearm': 'die Schusswaffe',
 'preach': 'predigen',
 'solicitor': 'der Anwalt',
 'defect': 'der Defekt',
 'disastrous': 'katastrophal',
 'drown': 'ertrinken',
 'exclusion': 'der Ausschluss',
 'revive': 'wiederbeleben',
 'strand': 'die Strähne, der Strang',
 'theatrical': 'theatralisch',
 'trustee': 'der Treuhänder',
 'turnout': 'die Wahlbeteiligung',
 'commentator': 'der Kommentator',
 'fibre': 'die Faser',
 'fixture': 'die Installation; das Spiel',
 'peculiar': 'eigenartig',
 'reside': 'wohnen',
 'vibrant': 'lebendig',
 'accelerate': 'beschleunigen',
 'dependence': 'die Abhängigkeit',
 'dictator': 'der Diktator',
 'optimism': 'der Optimismus',
 'proceeding': 'das Verfahren',
 'slash': 'aufschlitzen; drastisch kürzen',
 'assemble': 'sich versammeln; zusammenbauen',
 'chunk': 'das Stück',
 'deficiency': 'der Mangel',
 'dub': 'nennen; synchronisieren',
 'incidence': 'die Häufigkeit',
 'query': 'die Anfrage',
 'align': 'ausrichten',
 'await': 'erwarten',
 'maximize': 'maximieren',
 'plead': 'flehen; plädieren',
 'seldom': 'selten',
 'shareholder': 'der Aktionär',
 'militant': 'militant',
 'a militant': 'der Militante',
 'peasant': 'der Bauer',
 'regulator': 'die Aufsichtsbehörde',
 'casualty': 'das Opfer',
 'hostility': 'die Feindseligkeit',
 'soak': 'einweichen',
 'spectacle': 'das Spektakel',
 'accusation': 'der Vorwurf',
 'contender': 'der Anwärter',
 'accumulation': 'die Anhäufung',
 'congratulate': 'gratulieren',
 'a grin': 'das Grinsen',
 'to grin': 'grinsen',
 'adolescent': 'der Jugendliche',
 'backdrop': 'der Hintergrund',
 'columnist': 'der Kolumnist',
 'competence': 'die Kompetenz',
 'dictate': 'diktieren',
 'rotate': 'drehen; rotieren',
 'concession': 'das Zugeständnis; die Ermäßigung',
 'nominate': 'nominieren',
 'convict': 'verurteilen',
 'subsidy': 'die Subvention',
 'vow': 'geloben',
 'bureaucracy': 'die Bürokratie',
 'cater': 'bewirten; ausrichten auf',
 'educator': 'der Pädagoge',
 'outsider': 'der Außenseiter',
 'administer': 'verwalten; verabreichen',
 'expire': 'ablaufen',
 'haunt': 'heimsuchen',
 'indulge': 'sich gönnen',
 'inmate': 'der Häftling',
 'prosecute': 'strafrechtlich verfolgen',
 'evacuate': 'evakuieren',
 'flourish': 'gedeihen',
 'quota': 'die Quote',
 'residue': 'der Rückstand',
 'weave': 'weben',
 'erect': 'errichten',
 'subscriber': 'der Abonnent',
 'boast': 'prahlen',
 'descend': 'hinabsteigen',
 'empower': 'befähigen',
 'tighten': 'verschärfen, festziehen',
 'allegation': 'die Anschuldigung',
 'outing': 'der Ausflug',
 'cling': 'sich klammern',
 'dissolve': 'auflösen',
 'plunge': 'stürzen',
 'abolish': 'abschaffen',
 'kidnap': 'entführen',
 'aspire': 'anstreben',
 'thought-provoking': 'zum Nachdenken anregend',
 'applaud': 'applaudieren',
 'enthusiast': 'der Enthusiast',
 'extremist': 'der Extremist',
 'stabilize': 'stabilisieren',
 'counselling': 'die Beratung',
 'inject': 'injizieren',
 'enact': 'erlassen',
 'sanction': 'die Sanktion',
 'stereotype': 'das Klischee',
 'betray': 'verraten',
 'defy': 'trotzen',
 'divert': 'umleiten',
 'stumble': 'stolpern',
 'carve': 'schnitzen',
 'diagnose': 'diagnostizieren',
 'substitution': 'der Ersatz',
 'conceive': 'sich ausdenken; empfangen',
 'embark': 'an Bord gehen; beginnen',
 'prescribe': 'verschreiben',
 'soar': 'in die Höhe schnellen',
 'vanish': 'verschwinden',
 'authorize': 'genehmigen',
 'elevate': 'erhöhen',
 'guerrilla': 'der Guerillakämpfer',
 'beneficiary': 'der Begünstigte',
 'conserve': 'erhalten; sparen',
 'discard': 'wegwerfen',
 'stun': 'betäuben; verblüffen',
 'infect': 'infizieren',
 'insertion': 'das Einfügen',
 'escalate': 'eskalieren',
 'inflict': 'zufügen',
 'invoke': 'sich berufen auf',
 'characterize': 'charakterisieren',
 'complication': 'die Komplikation',
 'instruct': 'anweisen',
 'linger': 'verweilen',
 'aspiration': 'das Streben',
 'enrich': 'bereichern',
 'incur': 'verursachen, auf sich ziehen',
 'shrug': 'mit den Schultern zucken',
 'privatization': 'die Privatisierung',
 'proclaim': 'verkünden',
 'youngster': 'der Jugendliche',
 'widen': 'erweitern',
 'recount': 'erzählen',
 'overturn': 'aufheben; umkippen',
 'shatter': 'zerschmettern',
 'tempt': 'verlocken',
 'detain': 'festhalten',
 'confer': 'beraten; verleihen',
 'deprive': 'berauben',
 'mobilize': 'mobilisieren',
 'circulate': 'zirkulieren; verbreiten',
 'intensify': 'verstärken',
 'deteriorate': 'sich verschlechtern',
 'overwhelm': 'überwältigen',
 'oblige': 'verpflichten; gefällig sein',
 'sceptical': 'skeptisch',
 'motorist': 'der Autofahrer',
 'atrocity': 'die Gräueltat',
 'preside': 'den Vorsitz führen',
 'embed': 'einbetten',
 'enquire': 'sich erkundigen',
 'ensue': 'folgen',
 'obsess': 'besessen sein',
 'villager': 'der Dorfbewohner',
 'imprison': 'inhaftieren',
 'heighten': 'steigern',
 'entitle': 'berechtigen',
 'enrol': 'sich einschreiben',
 'devastate': 'verwüsten',
 'equivalent': 'gleichwertig, äquivalent',
 'contemporary': 'zeitgenössisch',
 'initially': 'anfangs',
 'assessment': 'die Bewertung',
 'publication': 'die Veröffentlichung',
 'select': 'auswählen',
 'procedure': 'das Verfahren',
 'to rank': 'einstufen',
 'output': 'der Output, die Ausgabe',
 'essentially': 'im Wesentlichen',
 'institution': 'die Institution',
 'root': 'die Wurzel',
 'a broadcast': 'die Sendung, die Übertragung',
 'regulation': 'die Regulierung',
 'frequency': 'die Häufigkeit',
 'input': 'der Input, die Eingabe',
 'sequence': 'die Abfolge, die Sequenz',
 'contribution': 'der Beitrag',
 'feedback': 'das Feedback, die Rückmeldung',
 'dynamic': 'dynamisch',
 'distinct': 'eindeutig, verschieden',
 'interaction': 'die Wechselwirkung',
 'mechanism': 'der Mechanismus',
 'parallel': 'parallel',
 'inquiry': 'die Untersuchung',
 'asset': 'der Vermögenswert; der Vorteil',
 'discipline': 'die Disziplin, das Fachgebiet',
 'dominant': 'dominant',
 'furthermore': 'darüber hinaus',
 'subsequently': 'anschließend',
 'briefly': 'kurz',
 'interpretation': 'die Interpretation',
 'evaluation': 'die Bewertung',
 'precisely': 'genau',
 'adopt': 'übernehmen',
 'scenario': 'das Szenario',
 'trace': 'nachverfolgen',
 'notion': 'die Vorstellung, der Begriff',
 'moreover': 'außerdem',
 'observation': 'die Beobachtung',
 'phenomenon': 'das Phänomen',
 'convert': 'umwandeln',
 'detect': 'erkennen, nachweisen',
 'thesis': 'die These; die Abschlussarbeit',
 'analyst': 'der Analyst',
 'accommodate': 'unterbringen, berücksichtigen',
 'propose': 'vorschlagen',
 'norm': 'die Norm',
 'illustration': 'die Illustration',
 'emerge': 'hervorgehen, auftauchen',
 'hypothesis': 'die Hypothese',
 'regulate': 'regulieren',
 'broadly': 'im Großen und Ganzen',
 'participant': 'der Teilnehmer, die Teilnehmerin',
 'interval': 'das Intervall',
 'packet': 'das Päckchen',
 'worm': 'der Wurm',
 'limitation': 'die Einschränkung, die Limitation',
 'cite': 'zitieren',
 'transmit': 'übertragen',
 'isolate': 'isolieren',
 'speculate': 'spekulieren',
 'questionnaire': 'der Fragebogen',
 'classify': 'klassifizieren',
 'guideline': 'die Richtlinie',
 'infer': 'folgern',
 'formula': 'die Formel',
 'respectively': 'beziehungsweise, jeweils',
 'merely': 'lediglich',
 'an alert': 'die Warnung, der Alarm',
 'composition': 'die Zusammensetzung',
 'domain': 'der Bereich, die Domäne',
 'engagement': 'die Verlobung; das Engagement',
 'collective': 'kollektiv, gemeinsam',
 'prevention': 'die Prävention',
 'patch': 'der Flicken; das Stück',
 'privilege': 'das Privileg',
 'solely': 'ausschließlich',
 'partially': 'teilweise',
 'respective': 'jeweilig',
 'compliance': 'die Compliance, die Einhaltung',
 'partial': 'teilweise, partiell',
 'underlying': 'zugrunde liegend',
 'protocol': 'das Protokoll',
 'statistical': 'statistisch',
 'applicable': 'anwendbar',
 'availability': 'die Verfügbarkeit',
 'linear': 'linear',
 'variable': 'die Variable',
 'generic': 'generisch, allgemein',
 'array': 'die Reihe, die Palette',
 'governance': 'die Governance',
 'comparable': 'vergleichbar',
 'detection': 'die Erkennung',
 'audit': 'das Audit, die Prüfung',
 'accordingly': 'dementsprechend',
 'dimension': 'die Dimension',
 'equation': 'die Gleichung',
 'extract': 'extrahieren',
 'ideology': 'die Ideologie',
 'isolation': 'die Isolation',
 'namely': 'nämlich',
 'adaptation': 'die Anpassung',
 'theoretical': 'theoretisch',
 'injection': 'die Spritze, die Injektion',
 'configuration': 'die Konfiguration',
 'integral': 'integral, wesentlich',
 'supervisor': 'der Vorgesetzte',
 'indicator': 'der Indikator',
 'manuscript': 'das Manuskript',
 'reliability': 'die Reliabilität, die Zuverlässigkeit',
 'systematic': 'systematisch',
 'correlation': 'die Korrelation',
 'proposition': 'die These, der Satz',
 'synthesis': 'die Synthese',
 'discourse': 'der Diskurs',
 'justification': 'die Begründung, die Rechtfertigung',
 'methodology': 'die Methodik',
 'hierarchy': 'die Hierarchie',
 'merge': 'zusammenführen',
 'allocation': 'die Zuweisung',
 'whereby': 'wodurch',
 'contention': 'die These',
 'specimen': 'die Probe',
 'analogy': 'die Analogie',
 'manifest': 'sich manifestieren',
 'assertion': 'die Behauptung',
 'inspect': 'prüfen, inspizieren',
 'practitioner': 'der Praktiker',
 'reproduce': 'reproduzieren',
 'assert': 'behaupten, geltend machen',
 'differentiate': 'unterscheiden',
 'presume': 'vermuten',
 'commence': 'beginnen',
 'adhere': 'sich halten an, einhalten',
 'parameter': 'der Parameter',
 'contend': 'behaupten',
 'provoke': 'provozieren, auslösen',
 'coincide': 'zusammenfallen',
 'consolidate': 'festigen',
 'simulate': 'simulieren',
 'compute': 'berechnen',
 'designate': 'bestimmen, benennen',
 'originate': 'entstammen',
 'encompass': 'umfassen',
 'formulate': 'formulieren',
 'correlate': 'korrelieren',
 'allege': 'behaupten (ohne Beweis)',
 'embody': 'verkörpern',
 'distort': 'verzerren',
 'unify': 'vereinheitlichen',
 'confine': 'beschränken'}

EN_DE_ACADEMIC = {'research': 'die Forschung',
 'data': 'die Daten (Pl.)',
 'method': 'die Methode',
 'source': 'die Quelle',
 'evidence': 'der Nachweis, die Belege (Pl.)',
 'analysis': 'die Analyse',
 'factor': 'der Faktor',
 'process': 'der Prozess',
 'structure': 'die Struktur',
 'define': 'definieren',
 'identify': 'identifizieren, ermitteln',
 'indicate': 'hindeuten auf, zeigen',
 'occur': 'auftreten',
 'require': 'erfordern',
 'assess': 'bewerten, beurteilen',
 'establish': 'feststellen; etablieren',
 'significant': 'signifikant, bedeutend',
 'similar': 'ähnlich',
 'specific': 'spezifisch',
 'furthermore': 'darüber hinaus',
 'for instance': 'beispielsweise',
 'concept': 'der Begriff, das Konzept',
 'context': 'der Kontext',
 'framework': 'der Rahmen',
 'hypothesis': 'die Hypothese',
 'outcome': 'das Ergebnis',
 'participant': 'der Teilnehmer, die Teilnehmerin',
 'sample': 'die Stichprobe',
 'survey': 'die Umfrage',
 'variable': 'die Variable',
 'interpret': 'interpretieren',
 'demonstrate': 'nachweisen, zeigen',
 'derive': 'ableiten',
 'obtain': 'erhalten, gewinnen',
 'investigate': 'untersuchen',
 'relevant': 'relevant',
 'consistent': 'übereinstimmend, konsistent',
 'appropriate': 'angemessen, geeignet',
 'consequently': 'folglich',
 'in addition': 'zusätzlich',
 'whereas': 'während, wohingegen',
 'assumption': 'die Annahme',
 'criterion': 'das Kriterium',
 'implication': 'die Implikation, die Folgerung',
 'limitation': 'die Einschränkung, die Limitation',
 'perspective': 'die Perspektive',
 'phenomenon': 'das Phänomen',
 'correlation': 'die Korrelation',
 'trend': 'der Trend, die Tendenz',
 'argue': 'argumentieren',
 'illustrate': 'veranschaulichen',
 'emphasise': 'betonen',
 'evaluate': 'evaluieren, auswerten',
 'clarify': 'klären',
 'outline': 'skizzieren',
 'crucial': 'entscheidend',
 'empirical': 'empirisch',
 'subsequent': 'nachfolgend',
 'thus': 'somit',
 'nevertheless': 'dennoch',
 'in contrast': 'im Gegensatz dazu',
 'methodology': 'die Methodik',
 'validity': 'die Validität, die Gültigkeit',
 'reliability': 'die Reliabilität, die Zuverlässigkeit',
 'bias': 'die Verzerrung',
 'literature': 'die Fachliteratur',
 'finding': 'der Befund, das Ergebnis',
 'scope': 'der Rahmen, der Umfang',
 'distribution': 'die Verteilung',
 'attribute': 'zuschreiben',
 'constitute': 'darstellen, bilden',
 'facilitate': 'erleichtern',
 'generate': 'erzeugen',
 'undertake': 'durchführen',
 'justify': 'begründen',
 'comprehensive': 'umfassend',
 'preliminary': 'vorläufig',
 'qualitative': 'qualitativ',
 'quantitative': 'quantitativ',
 'respectively': 'beziehungsweise, jeweils',
 'to a large extent': 'in hohem Maße',
 'paradigm': 'das Paradigma',
 'rationale': 'die Begründung',
 'discourse': 'der Diskurs',
 'discrepancy': 'die Diskrepanz',
 'feasibility': 'die Machbarkeit',
 'premise': 'die Prämisse',
 'inference': 'die Schlussfolgerung',
 'corroborate': 'bestätigen, erhärten',
 'synthesise': 'synthetisieren',
 'postulate': 'postulieren',
 'elucidate': 'erläutern',
 'delineate': 'abgrenzen, umreißen',
 'mitigate': 'mindern, abschwächen',
 'inherent': 'inhärent',
 'robust': 'robust',
 'salient': 'hervorstechend',
 'ambiguous': 'mehrdeutig',
 'notably': 'insbesondere',
 'conversely': 'umgekehrt',
 'hence': 'daher',
 'caveat': 'der Vorbehalt',
 'nuance': 'die Nuance',
 'trajectory': 'der Verlauf',
 'dichotomy': 'die Dichotomie',
 'consensus': 'der Konsens',
 'heuristic': 'die Heuristik',
 'underpin': 'untermauern',
 'reconcile': 'in Einklang bringen',
 'extrapolate': 'extrapolieren',
 'operationalise': 'operationalisieren',
 'scrutinise': 'genau prüfen',
 'refute': 'widerlegen',
 'warrant': 'rechtfertigen',
 'pertinent': 'einschlägig, sachdienlich',
 'tenuous': 'dürftig, schwach',
 'pivotal': 'zentral, ausschlaggebend',
 'rigorous': 'streng, rigoros',
 'ostensibly': 'angeblich, vordergründig',
 'inter alia': 'unter anderem',
 'albeit': 'wenn auch',
 'epistemology': 'die Erkenntnistheorie',
 'ontology': 'die Ontologie',
 'hegemony': 'die Hegemonie',
 'tautology': 'die Tautologie',
 'corollary': 'die logische Folge',
 'lacuna': 'die Forschungslücke',
 'problematise': 'problematisieren',
 'contextualise': 'kontextualisieren',
 'engender': 'hervorrufen',
 'obfuscate': 'verschleiern',
 'preclude': 'ausschließen',
 'idiosyncratic': 'eigentümlich, idiosynkratisch',
 'reductive': 'reduktionistisch',
 'ubiquitous': 'allgegenwärtig',
 'axiomatic': 'selbstverständlich, axiomatisch',
 'tacit': 'stillschweigend',
 'a fortiori': 'erst recht',
 'ipso facto': 'eo ipso, eben dadurch',
 'mutatis mutandis': 'sinngemäß',
 'heterogeneity': 'die Heterogenität',
 'reification': 'die Verdinglichung',
 'teleology': 'die Teleologie',
 'hermeneutics': 'die Hermeneutik',
 'verisimilitude': 'die Wahrscheinlichkeit, die Glaubwürdigkeit',
 'praxis': 'die Praxis',
 'instantiate': 'instanziieren, konkretisieren',
 'valorise': 'aufwerten',
 'interrogate': 'kritisch hinterfragen',
 'foreground': 'in den Vordergrund stellen',
 'elide': 'auslassen, übergehen',
 'conflate': 'vermengen',
 'vitiate': 'entkräften, beeinträchtigen',
 'recondite': 'abstrus, schwer verständlich',
 'nascent': 'entstehend, aufkommend',
 'polemical': 'polemisch',
 'germane': 'relevant, zur Sache gehörig',
 'prima facie': 'auf den ersten Blick',
 'ceteris paribus': 'unter sonst gleichen Bedingungen',
 'approach': 'der Ansatz',
 'aim': 'das Ziel',
 'chapter': 'das Kapitel',
 'conclusion': 'die Schlussfolgerung',
 'figure': 'die Abbildung; die Zahl',
 'introduction': 'die Einleitung',
 'issue': 'die Frage, das Problem',
 'level': 'das Niveau',
 'period': 'der Zeitraum',
 'reference': 'der Verweis, die Quelle',
 'summary': 'die Zusammenfassung',
 'table': 'die Tabelle',
 'topic': 'das Thema',
 'affect': 'beeinflussen',
 'discuss': 'erörtern, diskutieren',
 'explain': 'erklären',
 'include': 'einschließen',
 'measure': 'messen',
 'provide': 'bereitstellen, liefern',
 'suggest': 'vorschlagen; nahelegen',
 'support': 'unterstützen',
 'common': 'verbreitet, üblich',
 'current': 'aktuell',
 'previous': 'vorherig',
 'however': 'jedoch',
 'therefore': 'daher',
 'in conclusion': 'abschließend',
 'such as': 'wie zum Beispiel',
 'aspect': 'der Aspekt',
 'benefit': 'der Nutzen',
 'category': 'die Kategorie',
 'component': 'die Komponente',
 'feature': 'das Merkmal',
 'impact': 'die Auswirkung',
 'interview': 'das Interview',
 'percentage': 'der Prozentsatz',
 'questionnaire': 'der Fragebogen',
 'response': 'die Antwort, die Reaktion',
 'role': 'die Rolle',
 'achieve': 'erreichen',
 'analyse': 'analysieren',
 'apply': 'anwenden',
 'compare': 'vergleichen',
 'conclude': 'schlussfolgern',
 'contrast': 'gegenüberstellen',
 'examine': 'untersuchen',
 'predict': 'vorhersagen',
 'refer to': 'sich beziehen auf',
 'select': 'auswählen',
 'accurate': 'genau',
 'available': 'verfügbar',
 'major': 'bedeutend',
 'moreover': 'außerdem',
 'similarly': 'ebenso',
 'overall': 'insgesamt',
 'on the other hand': 'andererseits',
 'argument': 'das Argument',
 'claim': 'die Behauptung',
 'consequence': 'die Folge',
 'dimension': 'die Dimension',
 'emphasis': 'die Betonung',
 'evaluation': 'die Bewertung',
 'indicator': 'der Indikator',
 'objective': 'die Zielsetzung',
 'proportion': 'der Anteil',
 'strategy': 'die Strategie',
 'theory': 'die Theorie',
 'acknowledge': 'anerkennen',
 'adopt': 'übernehmen',
 'anticipate': 'vorwegnehmen, erwarten',
 'assume': 'annehmen',
 'categorise': 'kategorisieren',
 'challenge': 'infrage stellen',
 'determine': 'bestimmen',
 'enhance': 'steigern, verbessern',
 'highlight': 'hervorheben',
 'maintain': 'aufrechterhalten; behaupten',
 'adequate': 'angemessen',
 'considerable': 'beträchtlich',
 'explicit': 'explizit',
 'potential': 'potenziell',
 'accordingly': 'dementsprechend',
 'primarily': 'in erster Linie',
 'to some extent': 'in gewissem Maße',
 'with regard to': 'hinsichtlich',
 'abstract': 'das Abstract',
 'appendix': 'der Anhang',
 'citation': 'das Zitat',
 'coherence': 'die Kohärenz',
 'equation': 'die Gleichung',
 'interpretation': 'die Interpretation',
 'mechanism': 'der Mechanismus',
 'outlier': 'der Ausreißer',
 'peer review': 'das Peer-Review',
 'significance': 'die Signifikanz',
 'supervisor': 'der Betreuer',
 'allocate': 'zuweisen',
 'compile': 'zusammenstellen',
 'conduct': 'durchführen',
 'confirm': 'bestätigen',
 'differentiate': 'unterscheiden',
 'exclude': 'ausschließen',
 'implement': 'umsetzen',
 'infer': 'folgern',
 'modify': 'modifizieren',
 'validate': 'validieren',
 'accessible': 'zugänglich',
 'statistical': 'statistisch',
 'valid': 'gültig, valide',
 'theoretical': 'theoretisch',
 'approximately': 'ungefähr',
 'subsequently': 'anschließend',
 'correspondingly': 'entsprechend',
 'anomaly': 'die Anomalie',
 'assertion': 'die Behauptung',
 'causality': 'die Kausalität',
 'constraint': 'die Einschränkung',
 'contention': 'die These',
 'generalisability': 'die Verallgemeinerbarkeit',
 'implementation': 'die Umsetzung',
 'parameter': 'der Parameter',
 'proposition': 'die These, der Satz',
 'rigour': 'die Strenge',
 'taxonomy': 'die Taxonomie',
 'advocate': 'befürworten',
 'ascertain': 'feststellen',
 'attain': 'erreichen',
 'calibrate': 'kalibrieren',
 'compensate': 'ausgleichen',
 'deduce': 'ableiten',
 'discern': 'erkennen, unterscheiden',
 'encompass': 'umfassen',
 'exemplify': 'veranschaulichen',
 'formulate': 'formulieren',
 'coherent': 'kohärent',
 'intrinsic': 'intrinsisch',
 'marginal': 'marginal',
 'plausible': 'plausibel',
 'thereby': 'dadurch',
 'whereby': 'wodurch',
 'nonetheless': 'nichtsdestotrotz',
 'antecedent': 'der Vorläufer',
 'conjecture': 'die Vermutung',
 'corpus': 'das Korpus',
 'counterargument': 'das Gegenargument',
 'exposition': 'die Darlegung',
 'paradox': 'das Paradoxon',
 'precedent': 'der Präzedenzfall',
 'proxy': 'die Proxy-Variable',
 'repercussion': 'die Auswirkung',
 'adhere to': 'sich halten an',
 'allude to': 'anspielen auf',
 'articulate': 'artikulieren',
 'consolidate': 'festigen',
 'contend': 'behaupten',
 'culminate': 'gipfeln',
 'disseminate': 'verbreiten',
 'juxtapose': 'gegenüberstellen',
 'presuppose': 'voraussetzen',
 'stipulate': 'festlegen',
 'contingent': 'abhängig',
 'discrete': 'diskret',
 'implicit': 'implizit',
 'seminal': 'bahnbrechend',
 'unprecedented': 'beispiellos',
 'insofar as': 'insofern als',
 'notwithstanding': 'ungeachtet',
 'in this regard': 'in dieser Hinsicht',
 'by extension': 'im weiteren Sinne',
 'aporia': 'die Aporie',
 'dialectic': 'die Dialektik',
 'exegesis': 'die Exegese',
 'historiography': 'die Geschichtsschreibung',
 'ideology': 'die Ideologie',
 'positivism': 'der Positivismus',
 'relativism': 'der Relativismus',
 'subjectivity': 'die Subjektivität',
 'syllogism': 'der Syllogismus',
 'adjudicate': 'urteilen',
 'circumscribe': 'eingrenzen',
 'deconstruct': 'dekonstruieren',
 'epitomise': 'verkörpern',
 'explicate': 'explizieren',
 'marginalise': 'marginalisieren',
 'privilege': 'bevorzugen',
 'theorise': 'theoretisieren',
 'canonical': 'kanonisch',
 'dialectical': 'dialektisch',
 'normative': 'normativ',
 'paradigmatic': 'paradigmatisch',
 'post hoc': 'nachträglich',
 'in toto': 'insgesamt',
 'sensu stricto': 'im engeren Sinne',
 'vis-à-vis': 'gegenüber',
 'alterity': 'die Alterität',
 'episteme': 'die Episteme',
 'habitus': 'der Habitus',
 'intertextuality': 'die Intertextualität',
 'liminality': 'die Liminalität',
 'performativity': 'die Performativität',
 'positionality': 'die Positionalität',
 'reflexivity': 'die Reflexivität',
 'abrogate': 'aufheben',
 'countenance': 'dulden, gutheißen',
 'essentialise': 'essentialisieren',
 'occlude': 'verdecken',
 'reify': 'verdinglichen',
 'subsume': 'subsumieren',
 'transmute': 'umwandeln',
 'aporetic': 'aporetisch',
 'apodictic': 'apodiktisch',
 'hegemonic': 'hegemonial',
 'liminal': 'liminal',
 'recursive': 'rekursiv',
 'syncretic': 'synkretistisch',
 'pace': 'bei allem Respekt vor',
 'sic': 'sic',
 'viz.': 'nämlich',
 'state': 'angeben, feststellen',
 'question': 'hinterfragen',
 'series': 'die Reihe, die Serie',
 'report': 'berichten',
 'list': 'auflisten',
 'project': 'prognostizieren',
 'record': 'aufzeichnen, erfassen',
 'test': 'testen',
 'result': 'das Ergebnis',
 'model': 'modellieren',
 'review': 'überprüfen; rezensieren',
 'range': 'der Bereich, die Spannweite',
 'stage': 'die Phase, das Stadium',
 'note': 'festhalten, anmerken',
 'conference': 'die Konferenz, die Tagung',
 'population': 'die Grundgesamtheit, die Population',
 'focus': 'der Fokus',
 'section': 'der Abschnitt',
 'particularly': 'insbesondere',
 'application': 'die Anwendung; die Bewerbung',
 'condition': 'die Bedingung',
 'scale': 'die Skala',
 'critical': 'kritisch',
 'authority': 'die Autorität',
 'foundation': 'die Grundlage',
 'function': 'die Funktion',
 'prove': 'beweisen',
 'journal': 'die Fachzeitschrift',
 'volume': 'der Band; das Volumen',
 'reduce': 'reduzieren',
 'alternative': 'die Alternative',
 'relatively': 'relativ',
 'numerous': 'zahlreich',
 'specifically': 'spezifisch, gezielt',
 'phase': 'die Phase',
 'typically': 'typischerweise',
 'draft': 'entwerfen',
 'statistics': 'die Statistik',
 'instance': 'der Fall, das Beispiel',
 'definition': 'die Definition',
 'random': 'zufällig',
 'index': 'der Index',
 'representative': 'repräsentativ',
 'significantly': 'signifikant, erheblich',
 'portion': 'der Anteil',
 'pilot': 'pilotieren, erproben',
 'quote': 'zitieren',
 'comparison': 'der Vergleich',
 'document': 'dokumentieren',
 'convention': 'die Konvention',
 'equivalent': 'gleichwertig, äquivalent',
 'contemporary': 'zeitgenössisch',
 'initially': 'anfangs',
 'technique': 'die Technik',
 'assessment': 'die Bewertung',
 'element': 'das Element',
 'formula': 'die Formel',
 'publication': 'die Veröffentlichung',
 'rank': 'einstufen, ranken',
 'explanation': 'die Erklärung',
 'procedure': 'das Verfahren',
 'label': 'kennzeichnen',
 'output': 'der Output, die Ausgabe',
 'essentially': 'im Wesentlichen',
 'institution': 'die Institution',
 'experiment': 'das Experiment',
 'introduce': 'einführen, vorstellen',
 'ratio': 'das Verhältnis',
 'merely': 'lediglich',
 'frequency': 'die Häufigkeit',
 'exception': 'die Ausnahme',
 'input': 'der Input, die Eingabe',
 'sequence': 'die Abfolge, die Sequenz',
 'contribution': 'der Beitrag',
 'principle': 'das Prinzip',
 'composition': 'die Zusammensetzung',
 'uniform': 'einheitlich',
 'feedback': 'das Feedback, die Rückmeldung',
 'sufficient': 'ausreichend',
 'domain': 'der Bereich, die Domäne',
 'dynamic': 'dynamisch',
 'collective': 'kollektiv, gemeinsam',
 'estimate': 'die Schätzung',
 'interaction': 'die Wechselwirkung',
 'distinct': 'eindeutig, verschieden',
 'parallel': 'parallel',
 'instrument': 'das Instrument',
 'intervention': 'die Intervention',
 'requirement': 'die Anforderung',
 'inquiry': 'die Untersuchung',
 'discipline': 'die Disziplin, das Fachgebiet',
 'dominant': 'dominant',
 'briefly': 'kurz',
 'precisely': 'genau',
 'solely': 'ausschließlich',
 'trace': 'nachverfolgen',
 'ethics': 'die Ethik',
 'scenario': 'das Szenario',
 'respective': 'jeweilig',
 'partially': 'teilweise',
 'resolve': 'auflösen, lösen',
 'notion': 'die Vorstellung, der Begriff',
 'partial': 'teilweise, partiell',
 'underlying': 'zugrunde liegend',
 'observation': 'die Beobachtung',
 'applicable': 'anwendbar',
 'linear': 'linear',
 'convert': 'umwandeln',
 'generic': 'generisch, allgemein',
 'publish': 'veröffentlichen',
 'array': 'die Reihe, die Palette',
 'dynamics': 'die Dynamik',
 'comparable': 'vergleichbar',
 'observe': 'beobachten',
 'detect': 'erkennen, nachweisen',
 'graph': 'der Graph, die Grafik',
 'median': 'der Median',
 'thesis': 'die These; die Abschlussarbeit',
 'likewise': 'ebenso',
 'threshold': 'der Schwellenwert',
 'accommodate': 'unterbringen, berücksichtigen',
 'extract': 'extrahieren',
 'axis': 'die Achse',
 'namely': 'nämlich',
 'adaptation': 'die Anpassung',
 'probe': 'untersuchen, sondieren',
 'propose': 'vorschlagen',
 'weigh': 'abwägen',
 'configuration': 'die Konfiguration',
 'tendency': 'die Tendenz',
 'integral': 'integral, wesentlich',
 'explicitly': 'ausdrücklich',
 'aggregate': 'aggregieren, zusammenfassen',
 'locate': 'lokalisieren',
 'optimal': 'optimal',
 'translate': 'übersetzen',
 'norm': 'die Norm',
 'illustration': 'die Illustration',
 'manuscript': 'das Manuskript',
 'emerge': 'hervorgehen, auftauchen',
 'module': 'das Modul',
 'verify': 'verifizieren',
 'credibility': 'die Glaubwürdigkeit',
 'peer-reviewed': 'begutachtet (peer-reviewed)',
 'calculate': 'berechnen',
 'regulate': 'regulieren',
 'systematic': 'systematisch',
 'diagram': 'das Diagramm',
 'arbitrary': 'willkürlich',
 'synthesis': 'die Synthese',
 'critique': 'kritisch bewerten',
 'justification': 'die Begründung, die Rechtfertigung',
 'prototype': 'der Prototyp',
 'diagnostic': 'diagnostisch',
 'bibliography': 'das Literaturverzeichnis',
 'broadly': 'im Großen und Ganzen',
 'alternatively': 'alternativ',
 'subjective': 'subjektiv',
 'hierarchy': 'die Hierarchie',
 'interval': 'das Intervall',
 'merge': 'zusammenführen',
 'finite': 'endlich',
 'allocation': 'die Zuweisung',
 'preceding': 'vorhergehend',
 'analytical': 'analytisch',
 'perceive': 'wahrnehmen',
 'specimen': 'die Probe',
 'analogy': 'die Analogie',
 'dissertation': 'die Dissertation',
 'manifest': 'sich manifestieren',
 'terminology': 'die Terminologie',
 'cite': 'zitieren',
 'transmit': 'übertragen',
 'statistically': 'statistisch',
 'approximate': 'annähern, näherungsweise berechnen',
 'theoretically': 'theoretisch',
 'inspect': 'prüfen, inspizieren',
 'reconsider': 'überdenken',
 'reproduce': 'reproduzieren',
 'practitioner': 'der Praktiker',
 'assert': 'behaupten, geltend machen',
 'presume': 'vermuten',
 'conceptual': 'konzeptionell',
 'hypothetical': 'hypothetisch',
 'isolate': 'isolieren',
 'equilibrium': 'das Gleichgewicht',
 'commence': 'beginnen',
 'inherently': 'naturgemäß',
 'adhere': 'sich halten an, einhalten',
 'indicative': 'indikativ, hinweisend',
 'complementary': 'ergänzend, komplementär',
 'fragment': 'fragmentieren',
 'replicate': 'replizieren',
 'cumulative': 'kumulativ',
 'descriptive': 'deskriptiv',
 'conform': 'entsprechen, sich anpassen',
 'dependency': 'die Abhängigkeit',
 'excerpt': 'der Auszug',
 'comparatively': 'vergleichsweise',
 'organise': 'organisieren',
 'provoke': 'provozieren, auslösen',
 'correlated': 'korreliert',
 'coincide': 'zusammenfallen',
 'concurrent': 'gleichzeitig',
 'speculate': 'spekulieren',
 'deduction': 'die Deduktion',
 'variance': 'die Varianz',
 'simulate': 'simulieren',
 'continuum': 'das Kontinuum',
 'replication': 'die Replikation',
 'inverse': 'umgekehrt, invers',
 'compute': 'berechnen',
 'cohort': 'die Kohorte',
 'deviation': 'die Abweichung',
 'classify': 'klassifizieren',
 'coefficient': 'der Koeffizient',
 'interdisciplinary': 'interdisziplinär',
 'designate': 'bestimmen, benennen',
 'originate': 'entstammen',
 'longitudinal': 'longitudinal',
 'predictive': 'prädiktiv',
 'unilateral': 'einseitig',
 'causal': 'kausal',
 'acknowledgement': 'die Danksagung; die Anerkennung',
 'approximation': 'die Annäherung',
 'illuminate': 'beleuchten',
 'conclusive': 'schlüssig',
 'exhaustive': 'erschöpfend',
 'sequential': 'sequenziell',
 'markedly': 'deutlich',
 'evoke': 'hervorrufen',
 'hierarchical': 'hierarchisch',
 'guideline': 'die Richtlinie',
 'subsection': 'der Unterabschnitt',
 'denounce': 'anprangern',
 'converge': 'konvergieren, zusammenlaufen',
 'plagiarism': 'das Plagiat',
 'implicitly': 'implizit',
 'correlate': 'korrelieren',
 'equate': 'gleichsetzen',
 'augment': 'erweitern, ergänzen',
 'allege': 'behaupten (ohne Beweis)',
 'exploratory': 'explorativ',
 'embody': 'verkörpern',
 'footnote': 'die Fußnote',
 'amplify': 'verstärken',
 'proponent': 'der Befürworter',
 'hitherto': 'bislang',
 'impede': 'behindern',
 'contextual': 'kontextuell',
 'mediate': 'vermitteln',
 'reiterate': 'wiederholen, bekräftigen',
 'schema': 'das Schema',
 'inconclusive': 'nicht schlüssig',
 'predictor': 'der Prädiktor',
 'elicit': 'hervorlocken, ermitteln',
 'causation': 'die Kausalität',
 'respondent': 'der Befragte',
 'automate': 'automatisieren',
 'distort': 'verzerren',
 'omit': 'auslassen',
 'paraphrase': 'paraphrasieren',
 'unify': 'vereinheitlichen',
 'deviate': 'abweichen',
 'solicit': 'erbitten, einholen',
 'derivation': 'die Herleitung',
 'methodological': 'methodisch',
 'invalidate': 'entkräften, ungültig machen',
 'underscore': 'unterstreichen',
 'disprove': 'widerlegen',
 'confine': 'beschränken',
 'fabricate': 'fälschen; herstellen',
 'annotation': 'die Anmerkung',
 'empirically': 'empirisch',
 'nullify': 'annullieren',
 'substantiate': 'untermauern',
 'narrate': 'erzählen',
 'posit': 'postulieren',
 'ascribe': 'zuschreiben',
 'authenticate': 'authentifizieren, beglaubigen',
 'transcribe': 'transkribieren',
 'supersede': 'ablösen, ersetzen',
 'recur': 'wiederkehren',
 'append': 'anhängen',
 'characterise': 'charakterisieren',
 'purport': 'vorgeben, angeblich sein',
 'optimise': 'optimieren',
 'expound': 'ausführlich darlegen',
 'restate': 'neu formulieren',
 'generalisation': 'die Verallgemeinerung',
 'collate': 'zusammentragen, abgleichen',
 'situate': 'verorten',
 'enumerate': 'aufzählen',
 'rationalise': 'rationalisieren',
 'construe': 'auslegen, deuten',
 'normalise': 'normalisieren',
 'annotate': 'annotieren, kommentieren',
 'generalise': 'verallgemeinern',
 'tabulate': 'tabellarisch darstellen',
 'recapitulate': 'rekapitulieren',
 'conceptualise': 'konzeptualisieren',
 'interrelate': 'in Beziehung setzen',
 'hypothesise': 'Hypothesen aufstellen',
 'randomise': 'randomisieren',
 'data set': 'der Datensatz',
 'depend on': 'abhängen von',
 'map (out)': 'kartieren, planen',
 'relate to': 'in Beziehung setzen',
 'pertain to': 'betreffen',
 'case study': 'die Fallstudie',
 'restrict to': 'beschränken auf',
 'sample size': 'die Stichprobengröße',
 'in terms of': 'im Hinblick auf',
 'by contrast': 'im Gegensatz dazu',
 'identify with': 'sich identifizieren mit',
 'knowledge gap': 'die Forschungslücke',
 'response rate': 'die Rücklaufquote',
 'control group': 'die Kontrollgruppe',
 'compensate for': 'ausgleichen',
 'taken together': 'zusammengenommen',
 'margin of error': 'die Fehlertoleranz, die Fehlermarge',
 'research design': 'das Forschungsdesign',
 'with respect to': 'in Bezug auf',
 'on the basis of': 'auf der Grundlage von',
 'it follows that': 'daraus folgt, dass',
 'qualitative data': 'qualitative Daten (Pl.)',
 'in the same vein': 'in diesem Sinne',
 'conceptual model': 'das konzeptionelle Modell',
 'ethical approval': 'das Ethikvotum',
 'informed consent': 'die informierte Einwilligung',
 'literature review': 'die Literaturübersicht',
 'quantitative data': 'quantitative Daten (Pl.)',
 'research question': 'die Forschungsfrage',
 'body of literature': 'der Forschungsstand',
 'empirical evidence': 'die empirische Evidenz',
 'significance level': 'das Signifikanzniveau',
 'standard deviation': 'die Standardabweichung',
 'in accordance with': 'in Übereinstimmung mit',
 'as shown in Table 2': 'wie in Tabelle 2 ersichtlich',
 'the extent to which': 'inwieweit',
 'the null hypothesis': 'die Nullhypothese',
 'in the present study': 'in der vorliegenden Studie',
 'we hypothesised that': 'wir haben die Hypothese aufgestellt, dass',
 'confounding variable': 'die Störvariable',
 'theoretical framework': 'der theoretische Rahmen',
 'this paper argues that': 'in dieser Arbeit wird argumentiert, dass',
 'the data indicate that': 'die Daten zeigen, dass',
 'drawing on the work of': 'in Anlehnung an die Arbeit von',
 'prior research suggests': 'frühere Forschung legt nahe',
 'it should be noted that': 'es ist darauf hinzuweisen, dass',
 'this is consistent with': 'dies steht im Einklang mit',
 'the scope of this paper': 'der Rahmen dieser Arbeit',
 'contrary to expectations': 'entgegen den Erwartungen',
 'insofar as the data allow': 'soweit die Daten es zulassen',
 'statistically significant': 'statistisch signifikant',
 'it is widely accepted that': 'es ist allgemein anerkannt, dass',
 'further research is needed': 'weitere Forschung ist erforderlich',
 'as illustrated in Figure 1': 'wie in Abbildung 1 dargestellt',
 'in light of these findings': 'angesichts dieser Befunde',
 'future work should address': 'künftige Arbeiten sollten … behandeln',
 'the aim of this study is to': 'Ziel dieser Studie ist es, …',
 'these findings suggest that': 'diese Befunde legen nahe, dass',
 'this raises the question of': 'dies wirft die Frage auf',
 'a substantial proportion of': 'ein erheblicher Anteil von',
 'the present findings extend': 'die vorliegenden Befunde erweitern',
 'to the best of our knowledge': 'nach unserem besten Wissen',
 'the underlying assumption is': 'die zugrunde liegende Annahme ist',
 'a possible explanation is that': 'eine mögliche Erklärung ist, dass',
 'beyond the scope of this study': 'über den Rahmen dieser Studie hinaus',
 'for the purposes of this study': 'für die Zwecke dieser Studie',
 'a number of studies have shown': 'mehrere Studien haben gezeigt',
 'one limitation of this study is': 'eine Limitation dieser Studie ist',
 'the results are consistent with': 'die Ergebnisse stimmen überein mit',
 'in contrast to previous findings': 'im Gegensatz zu früheren Befunden',
 'little attention has been paid to': '… wurde bisher wenig beachtet',
 'there is a growing body of evidence': 'es gibt zunehmend Belege'}

EN_DE_CYBER = {'asset': 'der Vermögenswert, das Asset',
 'threat': 'die Bedrohung',
 'threat actor': 'der Bedrohungsakteur',
 'vulnerability': 'die Schwachstelle',
 'exploit': 'der Exploit; ausnutzen',
 'risk': 'das Risiko',
 'likelihood': 'die Eintrittswahrscheinlichkeit',
 'impact': 'die Auswirkung',
 'attack surface': 'die Angriffsfläche',
 'attack vector': 'der Angriffsvektor',
 'blast radius': 'der Schadensradius',
 'confidentiality': 'die Vertraulichkeit',
 'integrity': 'die Integrität',
 'availability': 'die Verfügbarkeit',
 'non-repudiation': 'die Nichtabstreitbarkeit',
 'authentication': 'die Authentifizierung',
 'authorisation': 'die Autorisierung',
 'accounting': 'die Protokollierung (Accounting)',
 'least privilege': 'das Prinzip der geringsten Rechte',
 'defence in depth': 'die gestaffelte Verteidigung (Defense in Depth)',
 'zero trust': 'Zero Trust',
 'security posture': 'die Sicherheitslage',
 'baseline': 'die Baseline, die Referenzkonfiguration',
 'hardening': 'die Härtung',
 'patch': 'der Patch',
 'patch management': 'das Patch-Management',
 'countermeasure': 'die Gegenmaßnahme',
 'safeguard': 'die Schutzmaßnahme',
 'control': 'die Kontrolle, die Sicherheitsmaßnahme',
 'compensating control': 'die kompensierende Kontrolle',
 'mitigation': 'die Risikominderung',
 'remediation': 'die Behebung',
 'residual risk': 'das Restrisiko',
 'false positive': 'das False Positive, der Fehlalarm',
 'false negative': 'das False Negative',
 'true positive': 'das True Positive',
 'detection': 'die Erkennung',
 'prevention': 'die Prävention',
 'response': 'die Reaktion',
 'recovery': 'die Wiederherstellung',
 'resilience': 'die Resilienz',
 'redundancy': 'die Redundanz',
 'failover': 'das Failover',
 'business continuity': 'die Geschäftskontinuität',
 'disaster recovery': 'die Notfallwiederherstellung (Disaster Recovery)',
 'single point of failure': 'der Single Point of Failure',
 'security by design': 'Security by Design',
 'fail secure': 'ausfallsicher (fail secure)',
 'trust boundary': 'die Vertrauensgrenze',
 'threat landscape': 'die Bedrohungslage',
 'assess the risk': 'das Risiko bewerten',
 'mitigate the risk': 'das Risiko mindern',
 'escalate the incident': 'den Vorfall eskalieren',
 'contain the threat': 'die Bedrohung eindämmen',
 'remediate the finding': 'den Befund beheben',
 'harden the system': 'das System härten',
 'patch the vulnerability': 'die Schwachstelle patchen',
 'enforce the policy': 'die Richtlinie durchsetzen',
 'validate the fix': 'die Korrektur verifizieren',
 'reproduce the issue': 'das Problem reproduzieren',
 'document the steps': 'die Schritte dokumentieren',
 'raise a ticket': 'ein Ticket erstellen',
 'flag a concern': 'ein Bedenken melden',
 'walk through the report': 'den Bericht durchgehen',
 'follow up on': 'nachfassen bei',
 'loop in the team': 'das Team einbeziehen',
 'align with stakeholders': 'sich mit den Stakeholdern abstimmen',
 'prioritise findings': 'Befunde priorisieren',
 'scope the engagement': 'den Auftragsumfang festlegen',
 'sign off on': 'freigeben, abzeichnen',
 'roll out': 'ausrollen',
 'roll back': 'zurückrollen',
 'decommission': 'außer Betrieb nehmen',
 'whitelist an IP': 'eine IP auf die Allowlist setzen',
 'revoke access': 'den Zugriff entziehen',
 'grant access': 'Zugriff gewähren',
 'rotate credentials': 'Zugangsdaten rotieren',
 'enable logging': 'die Protokollierung aktivieren',
 'monitor for anomalies': 'auf Anomalien überwachen',
 'correlate events': 'Ereignisse korrelieren',
 'verify the alert': 'den Alarm verifizieren',
 'dismiss as false positive': 'als Fehlalarm schließen',
 'conduct a review': 'eine Überprüfung durchführen',
 'present the findings': 'die Befunde präsentieren',
 'justify the budget': 'das Budget begründen',
 'as per our policy': 'gemäß unserer Richtlinie',
 'in line with best practice': 'im Einklang mit Best Practices',
 'subject to approval': 'vorbehaltlich der Genehmigung',
 'pending further investigation': 'bis zur weiteren Untersuchung',
 'with immediate effect': 'mit sofortiger Wirkung',
 'packet': 'das Paket',
 'payload': 'die Nutzlast, der Payload',
 'header': 'der Header',
 'frame': 'der Frame',
 'protocol': 'das Protokoll',
 'port': 'der Port',
 'socket': 'der Socket',
 'handshake': 'der Handshake',
 'three-way handshake': 'der Drei-Wege-Handshake',
 'subnet': 'das Subnetz',
 'gateway': 'das Gateway',
 'router': 'der Router',
 'switch': 'der Switch',
 'firewall': 'die Firewall',
 'next-generation firewall': 'die Next-Generation-Firewall',
 'stateful inspection': 'die Stateful Inspection',
 'access control list (ACL)': 'die Zugriffskontrollliste (ACL)',
 'NAT': 'NAT (Netzwerkadressübersetzung)',
 'VLAN': 'das VLAN',
 'network segmentation': 'die Netzwerksegmentierung',
 'micro-segmentation': 'die Mikrosegmentierung',
 'DMZ': 'die DMZ',
 'proxy': 'der Proxy',
 'reverse proxy': 'der Reverse Proxy',
 'load balancer': 'der Load Balancer, der Lastverteiler',
 'VPN': 'das VPN',
 'tunnelling': 'das Tunneling',
 'port forwarding': 'die Portweiterleitung',
 'pivoting': 'das Pivoting',
 'packet capture': 'der Paketmitschnitt',
 'sniffing': 'das Sniffing',
 'traffic analysis': 'die Verkehrsanalyse',
 'bandwidth': 'die Bandbreite',
 'latency': 'die Latenz',
 'throughput': 'der Durchsatz',
 'broadcast': 'der Broadcast',
 'routing table': 'die Routingtabelle',
 'DNS resolution': 'die DNS-Auflösung',
 'DHCP lease': 'die DHCP-Lease',
 'TLS': 'TLS',
 'mutual TLS': 'mutual TLS (mTLS)',
 'certificate pinning': 'das Certificate Pinning',
 'wireless access point': 'der WLAN-Zugangspunkt',
 'rogue access point': 'der Rogue Access Point',
 'evil twin': 'der Evil Twin',
 'deauthentication attack': 'der Deauthentication-Angriff',
 'WPA2 / WPA3': 'WPA2 / WPA3',
 'egress filtering': 'die Egress-Filterung',
 'ingress filtering': 'die Ingress-Filterung',
 'network tap': 'der Netzwerk-TAP',
 'kernel': 'der Kernel',
 'process': 'der Prozess',
 'daemon': 'der Daemon, der Dienst',
 'service': 'der Dienst',
 'shell': 'die Shell',
 'privilege': 'das Recht, die Berechtigung',
 'root': 'root',
 'sudo': 'sudo',
 'file permission': 'die Dateiberechtigung',
 'setuid binary': 'das Setuid-Binary',
 'cron job': 'der Cronjob',
 'systemd unit': 'die systemd-Unit',
 'log file': 'die Logdatei',
 'syslog': 'Syslog',
 'audit trail': 'der Prüfpfad, der Audit-Trail',
 'registry': 'die Registry',
 'Active Directory': 'Active Directory',
 'domain controller': 'der Domänencontroller',
 'group policy': 'die Gruppenrichtlinie',
 'service account': 'das Dienstkonto',
 'golden ticket': 'das Golden Ticket',
 'hash': 'der Hash',
 'pass-the-hash': 'Pass-the-Hash',
 'LSASS dump': 'der LSASS-Dump',
 'memory dump': 'der Speicherabzug',
 'snapshot': 'der Snapshot',
 'virtual machine': 'die virtuelle Maschine',
 'hypervisor': 'der Hypervisor',
 'container': 'der Container',
 'image': 'das Image',
 'sandbox': 'die Sandbox',
 'escape (sandbox/container)': 'der Ausbruch (Sandbox/Container)',
 'endpoint': 'der Endpunkt',
 'agent': 'der Agent',
 'inventory': 'das Inventar',
 'asset management': 'das Asset-Management',
 'configuration drift': 'die Konfigurationsabweichung',
 'golden image': 'das Golden Image',
 'malware': 'die Schadsoftware, die Malware',
 'ransomware': 'die Ransomware, die Erpressersoftware',
 'spyware': 'die Spyware',
 'adware': 'die Adware',
 'rootkit': 'das Rootkit',
 'bootkit': 'das Bootkit',
 'trojan': 'der Trojaner',
 'worm': 'der Wurm',
 'virus': 'der Virus',
 'dropper': 'der Dropper',
 'loader': 'der Loader',
 'wiper': 'der Wiper',
 'keylogger': 'der Keylogger',
 'botnet': 'das Botnetz',
 'command and control (C2)': 'Command and Control (C2)',
 'beacon': 'der Beacon',
 'backdoor': 'die Hintertür',
 'logic bomb': 'die logische Bombe',
 'phishing': 'das Phishing',
 'spear phishing': 'das Spear-Phishing',
 'whaling': 'das Whaling',
 'smishing': 'das Smishing',
 'vishing': 'das Vishing',
 'pretexting': 'das Pretexting',
 'baiting': 'das Baiting, der Köder',
 'tailgating': 'das Tailgating',
 'social engineering': 'das Social Engineering',
 'business email compromise': 'der CEO-Betrug (Business Email Compromise)',
 'credential theft': 'der Diebstahl von Zugangsdaten',
 'credential stuffing': 'das Credential Stuffing',
 'password spraying': 'das Password Spraying',
 'brute force': 'der Brute-Force-Angriff',
 'dictionary attack': 'der Wörterbuchangriff',
 'rainbow table': 'die Rainbow Table',
 'man-in-the-middle (MitM)': 'der Man-in-the-Middle-Angriff',
 'replay attack': 'der Replay-Angriff',
 'session hijacking': 'das Session Hijacking',
 'spoofing': 'das Spoofing',
 'ARP poisoning': 'das ARP-Spoofing',
 'DNS poisoning': 'das DNS-Poisoning',
 'DNS tunnelling': 'das DNS-Tunneling',
 'typosquatting': 'das Typosquatting',
 'watering hole attack': 'der Watering-Hole-Angriff',
 'supply chain attack': 'der Lieferkettenangriff',
 'denial of service (DoS)': 'der Denial-of-Service-Angriff (DoS)',
 'DDoS': 'der DDoS-Angriff',
 'amplification attack': 'der Amplification-Angriff',
 'zero-day': 'die Zero-Day-Lücke',
 'privilege escalation': 'die Rechteausweitung',
 'lateral movement': 'die laterale Bewegung',
 'persistence': 'die Persistenz',
 'data exfiltration': 'die Datenexfiltration',
 'data breach': 'die Datenpanne',
 'insider threat': 'der Innentäter',
 'advanced persistent threat (APT)': 'die APT (fortgeschrittene, andauernde Bedrohung)',
 'living off the land': 'Living off the Land',
 'fileless malware': 'die dateilose Malware',
 'obfuscation': 'die Verschleierung',
 'packing': 'das Packing',
 'polymorphic': 'polymorph',
 'evasion': 'die Umgehung',
 'anti-forensics': 'Anti-Forensik',
 'cryptojacking': 'das Cryptojacking',
 'scareware': 'die Scareware',
 'double extortion': 'die doppelte Erpressung',
 'initial access': 'der Erstzugriff',
 'dwell time': 'die Verweildauer',
 'kill chain': 'die Kill Chain',
 'injection': 'die Injection',
 'SQL injection': 'die SQL-Injection',
 'command injection': 'die Command Injection',
 'cross-site scripting (XSS)': 'Cross-Site-Scripting (XSS)',
 'stored XSS': 'Stored XSS',
 'reflected XSS': 'Reflected XSS',
 'cross-site request forgery (CSRF)': 'Cross-Site Request Forgery (CSRF)',
 'server-side request forgery (SSRF)': 'Server-Side Request Forgery (SSRF)',
 'insecure deserialisation': 'die unsichere Deserialisierung',
 'path traversal': 'die Path Traversal',
 'local file inclusion': 'die Local File Inclusion',
 'remote code execution (RCE)': 'die Remote Code Execution (RCE)',
 'open redirect': 'die offene Weiterleitung',
 'clickjacking': 'das Clickjacking',
 'broken access control': 'die fehlerhafte Zugriffskontrolle',
 'insecure direct object reference (IDOR)': 'IDOR (unsichere direkte Objektreferenz)',
 'business logic flaw': 'der Logikfehler',
 'race condition': 'die Race Condition',
 'buffer overflow': 'der Pufferüberlauf',
 'heap overflow': 'der Heap-Überlauf',
 'stack overflow': 'der Stack-Überlauf',
 'use-after-free': 'Use-after-free',
 'input validation': 'die Eingabevalidierung',
 'output encoding': 'die Ausgabekodierung',
 'sanitisation': 'die Bereinigung',
 'parameterised query': 'die parametrisierte Abfrage',
 'prepared statement': 'das Prepared Statement',
 'content security policy (CSP)': 'die Content Security Policy (CSP)',
 'same-origin policy': 'die Same-Origin-Policy',
 'CORS': 'CORS',
 'security header': 'der Sicherheitsheader',
 'rate limiting': 'die Ratenbegrenzung',
 'web application firewall (WAF)': 'die Web Application Firewall (WAF)',
 'API gateway': 'das API-Gateway',
 'token': 'das Token',
 'session cookie': 'das Session-Cookie',
 'secure flag': 'das Secure-Flag',
 'HttpOnly': 'HttpOnly',
 'CAPTCHA': 'das CAPTCHA',
 'dependency': 'die Abhängigkeit',
 'software bill of materials (SBOM)': 'die Software-Stückliste (SBOM)',
 'secure coding': 'sicheres Programmieren',
 'code review': 'das Code-Review',
 'static analysis (SAST)': 'die statische Codeanalyse (SAST)',
 'dynamic analysis (DAST)': 'die dynamische Analyse (DAST)',
 'fuzzing': 'das Fuzzing',
 'secrets management': 'das Secrets-Management',
 'hardcoded credentials': 'fest codierte Zugangsdaten',
 'encryption': 'die Verschlüsselung',
 'decryption': 'die Entschlüsselung',
 'plaintext': 'der Klartext',
 'ciphertext': 'der Geheimtext, der Chiffretext',
 'cipher': 'die Chiffre',
 'symmetric encryption': 'die symmetrische Verschlüsselung',
 'asymmetric encryption': 'die asymmetrische Verschlüsselung',
 'public key': 'der öffentliche Schlüssel',
 'private key': 'der private Schlüssel',
 'key exchange': 'der Schlüsselaustausch',
 'key rotation': 'die Schlüsselrotation',
 'key management': 'das Schlüsselmanagement',
 'hashing': 'das Hashing',
 'salt': 'der Salt',
 'pepper': 'der Pepper',
 'digital signature': 'die digitale Signatur',
 'certificate': 'das Zertifikat',
 'certificate authority (CA)': 'die Zertifizierungsstelle (CA)',
 'public key infrastructure (PKI)': 'die Public-Key-Infrastruktur (PKI)',
 'self-signed certificate': 'das selbstsignierte Zertifikat',
 'revocation': 'der Widerruf',
 'entropy': 'die Entropie',
 'nonce': 'die Nonce',
 'initialisation vector': 'der Initialisierungsvektor',
 'end-to-end encryption': 'die Ende-zu-Ende-Verschlüsselung',
 'encryption at rest': 'die Verschlüsselung ruhender Daten',
 'encryption in transit': 'die Transportverschlüsselung',
 'hardware security module (HSM)': 'das Hardware-Sicherheitsmodul (HSM)',
 'identity provider (IdP)': 'der Identitätsanbieter (IdP)',
 'single sign-on (SSO)': 'Single Sign-on (SSO)',
 'federation': 'die Föderation',
 'SAML': 'SAML',
 'OAuth': 'OAuth',
 'OpenID Connect': 'OpenID Connect',
 'multi-factor authentication (MFA)': 'die Multi-Faktor-Authentifizierung (MFA)',
 'one-time password (OTP)': 'das Einmalpasswort (OTP)',
 'passkey': 'der Passkey',
 'biometric': 'biometrisch',
 'role-based access control (RBAC)': 'die rollenbasierte Zugriffskontrolle (RBAC)',
 'attribute-based access control': 'die attributbasierte Zugriffskontrolle',
 'privileged access management (PAM)': 'das Privileged Access Management (PAM)',
 'just-in-time access': 'der Just-in-Time-Zugriff',
 'identity lifecycle': 'der Identitätslebenszyklus',
 'provisioning': 'die Bereitstellung (Provisioning)',
 'deprovisioning': 'die Deprovisionierung',
 'access review': 'die Zugriffsprüfung',
 'segregation of duties': 'die Funktionstrennung',
 'penetration test': 'der Penetrationstest',
 'red team': 'das Red Team',
 'blue team': 'das Blue Team',
 'purple team': 'das Purple Team',
 'engagement': 'der Auftrag, das Projekt',
 'rules of engagement': 'die Rules of Engagement',
 'scope': 'der Umfang, der Scope',
 'in scope / out of scope': 'im Scope / außerhalb des Scopes',
 'authorisation letter': 'das Autorisierungsschreiben',
 'get-out-of-jail letter': 'die Freistellungserklärung',
 'black box': 'der Blackbox-Test',
 'white box': 'der Whitebox-Test',
 'grey box': 'der Greybox-Test',
 'reconnaissance': 'die Aufklärung',
 'OSINT': 'OSINT',
 'footprinting': 'das Footprinting',
 'enumeration': 'die Enumeration',
 'scanning': 'das Scannen',
 'port scan': 'der Portscan',
 'service detection': 'die Diensterkennung',
 'banner grabbing': 'das Banner Grabbing',
 'vulnerability scanning': 'der Schwachstellenscan',
 'proof of concept (PoC)': 'der Proof of Concept (PoC)',
 'payload delivery': 'die Payload-Auslieferung',
 'shellcode': 'der Shellcode',
 'reverse shell': 'die Reverse Shell',
 'bind shell': 'die Bind Shell',
 'foothold': 'der Brückenkopf, der Foothold',
 'pivot': 'pivotieren',
 'post-exploitation': 'die Post-Exploitation',
 'credential harvesting': 'das Sammeln von Zugangsdaten',
 'password cracking': 'das Knacken von Passwörtern',
 'privilege enumeration': 'die Rechte-Enumeration',
 'persistence mechanism': 'der Persistenzmechanismus',
 'cleanup': 'die Bereinigung (Cleanup)',
 'debrief': 'die Nachbesprechung',
 'finding': 'der Befund',
 'severity': 'der Schweregrad',
 'CVSS score': 'der CVSS-Wert',
 'exploitability': 'die Ausnutzbarkeit',
 'remediation advice': 'die Behebungsempfehlung',
 'retest': 'der Retest',
 'executive summary': 'die Management-Zusammenfassung',
 'technical report': 'der technische Bericht',
 'bug bounty': 'das Bug-Bounty-Programm',
 'responsible disclosure': 'die verantwortungsvolle Offenlegung',
 'coordinated disclosure': 'die koordinierte Offenlegung',
 'adversary emulation': 'die Angreiferemulation',
 'TTPs': 'TTPs (Taktiken, Techniken, Prozeduren)',
 'MITRE ATT&CK': 'MITRE ATT&CK',
 'threat model': 'das Bedrohungsmodell',
 'attack tree': 'der Angriffsbaum',
 'security operations centre (SOC)': 'das Security Operations Center (SOC)',
 'analyst': 'der Analyst',
 'tier 1 / tier 2': 'Level 1 / Level 2',
 'alert': 'der Alarm, die Warnung',
 'alert fatigue': 'die Alarmmüdigkeit',
 'triage': 'die Triage',
 'escalation': 'die Eskalation',
 'incident': 'der Sicherheitsvorfall',
 'incident response': 'die Vorfallsreaktion (Incident Response)',
 'playbook': 'das Playbook',
 'runbook': 'das Runbook',
 'on-call': 'die Rufbereitschaft',
 'containment': 'die Eindämmung',
 'eradication': 'die Beseitigung',
 'lessons learned': 'die Lessons Learned',
 'post-mortem': 'die Nachanalyse (Post-Mortem)',
 'root cause analysis': 'die Ursachenanalyse',
 'SIEM': 'SIEM',
 'log aggregation': 'die Log-Aggregation',
 'correlation rule': 'die Korrelationsregel',
 'use case': 'der Use Case',
 'detection engineering': 'das Detection Engineering',
 'signature': 'die Signatur',
 'heuristic': 'heuristisch',
 'anomaly detection': 'die Anomalieerkennung',
 'behavioural analysis': 'die Verhaltensanalyse',
 'baseline deviation': 'die Abweichung von der Baseline',
 'EDR': 'EDR',
 'XDR': 'XDR',
 'IDS': 'IDS (Angriffserkennungssystem)',
 'IPS': 'IPS (Angriffsverhinderungssystem)',
 'honeypot': 'der Honeypot',
 'deception technology': 'die Deception-Technologie',
 'threat intelligence': 'die Bedrohungsaufklärung (Threat Intelligence)',
 'indicator of compromise (IoC)': 'der Kompromittierungsindikator (IoC)',
 'indicator of attack (IoA)': 'der Angriffsindikator (IoA)',
 'threat hunting': 'das Threat Hunting',
 'hypothesis-driven hunt': 'die hypothesengetriebene Jagd',
 'digital forensics': 'die digitale Forensik',
 'chain of custody': 'die Beweismittelkette',
 'imaging': 'die forensische Abbilderstellung',
 'write blocker': 'der Schreibblocker',
 'volatile data': 'flüchtige Daten (Pl.)',
 'timeline analysis': 'die Zeitlinienanalyse',
 'artefact': 'das Artefakt',
 'malware analysis': 'die Malware-Analyse',
 'static analysis': 'die statische Analyse',
 'dynamic analysis': 'die dynamische Analyse',
 'reverse engineering': 'das Reverse Engineering',
 'sandbox detonation': 'die Sandbox-Detonation',
 'YARA rule': 'die YARA-Regel',
 'SOAR': 'SOAR',
 'mean time to detect (MTTD)': 'die mittlere Erkennungszeit (MTTD)',
 'mean time to respond (MTTR)': 'die mittlere Reaktionszeit (MTTR)',
 'false alarm': 'der Fehlalarm',
 'tuning': 'das Tuning, die Feinabstimmung',
 'whitelisting': 'das Whitelisting',
 'blocklisting': 'das Blocklisting',
 'quarantine': 'die Quarantäne',
 'isolation': 'die Isolierung',
 'kill switch': 'der Notausschalter (Kill Switch)',
 'governance': 'die Governance',
 'compliance': 'die Compliance, die Einhaltung',
 'regulation': 'die Regulierung',
 'standard': 'der Standard',
 'framework': 'das Rahmenwerk',
 'policy': 'die Richtlinie',
 'procedure': 'das Verfahren',
 'guideline': 'die Leitlinie',
 'audit': 'das Audit, die Prüfung',
 'auditor': 'der Auditor, der Prüfer',
 'audit finding': 'die Audit-Feststellung',
 'evidence': 'der Nachweis, das Beweismittel',
 'attestation': 'die Bestätigung, die Attestierung',
 'certification': 'die Zertifizierung',
 'accreditation': 'die Akkreditierung',
 'gap analysis': 'die Gap-Analyse',
 'maturity model': 'das Reifegradmodell',
 'risk assessment': 'die Risikobewertung',
 'risk register': 'das Risikoregister',
 'risk appetite': 'die Risikobereitschaft',
 'risk tolerance': 'die Risikotoleranz',
 'risk acceptance': 'die Risikoakzeptanz',
 'risk transfer': 'der Risikotransfer',
 'risk avoidance': 'die Risikovermeidung',
 'inherent risk': 'das inhärente Risiko',
 'business impact analysis': 'die Business-Impact-Analyse',
 'recovery time objective (RTO)': 'das Wiederherstellungszeitziel (RTO)',
 'recovery point objective (RPO)': 'das Wiederherstellungspunktziel (RPO)',
 'data classification': 'die Datenklassifizierung',
 'data retention': 'die Datenaufbewahrung',
 'data minimisation': 'die Datenminimierung',
 'personal data': 'personenbezogene Daten (Pl.)',
 'data subject': 'die betroffene Person',
 'data controller': 'der Verantwortliche (Datenschutz)',
 'data processor': 'der Auftragsverarbeiter',
 'GDPR': 'die DSGVO',
 'breach notification': 'die Meldung einer Datenpanne',
 'privacy by design': 'Privacy by Design',
 'third-party risk': 'das Drittanbieterrisiko',
 'vendor assessment': 'die Lieferantenbewertung',
 'due diligence': 'die Sorgfaltsprüfung (Due Diligence)',
 'service level agreement (SLA)': 'das Service-Level-Agreement (SLA)',
 'NDA': 'die Geheimhaltungsvereinbarung (NDA)',
 'security awareness training': 'die Sicherheitsschulung',
 'acceptable use policy': 'die Nutzungsrichtlinie',
 'change management': 'das Änderungsmanagement',
 'approval workflow': 'der Genehmigungsworkflow',
 'exception request': 'der Ausnahmeantrag'}
