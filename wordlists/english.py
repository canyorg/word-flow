# -*- coding: utf-8 -*-
"""English word lists.

DAILY    : A1.1–C2.2 — 1500 core concepts (A1–B1), C1 general vocabulary,
           phrasal verbs, connectors and idioms up to C2.2
ACADEMIC : B1.1–C2.2 — vocabulary and set phrases for papers, theses and talks
CYBER    : B1.1–C2.2 — professional cybersecurity vocabulary (attacks, networking,
           Linux, web security, crypto & IAM, pentest, SOC/IR, GRC, workplace phrases)
Lines: "type|English|Turkish|hint"
       type: n noun, v verb, a adjective, d adverb / linker, p phrase, w other word
EN_DE* : English -> German meaning
"""

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
w|hello|merhaba
p|good morning|günaydın
p|good afternoon|iyi günler
p|good evening|iyi akşamlar
p|good night|iyi geceler
w|bye|hoşça kal
p|goodbye|güle güle, hoşça kalın
p|see you later|sonra görüşürüz
p|see you tomorrow|yarın görüşürüz
p|see you soon|yakında görüşürüz
w|yes|evet
w|no|hayır, hiçbir, yok
w|maybe|belki
w|please|lütfen, buyurun
w|thanks|teşekkürler
p|thank you very much|çok teşekkürler
p|you're welcome|rica ederim
w|excuse me|affedersiniz, özür dilerim
p|I'm sorry|üzgünüm
p|no problem|sorun değil
p|how are you?|nasılsın?
p|I'm fine|iyiyim
p|and you?|ya sen?
w|welcome|hoş geldin
p|my name is …|benim adım ...
p|I'm called …|benim adım ...
p|nice to meet you|memnun oldum
p|pardon?|efendim?, anlamadım
p|I don't understand|anlamıyorum
p|slowly|yavaş lütfen
p|once more|bir kez daha
w|of course|tabii ki
w|exactly|aynen, tam olarak
w|right|doğru, sağ
w|okay|tamam
p|all right|tamam, uygun
p|good luck|bol şans
p|have fun|iyi eğlenceler
p|have a good trip|iyi yolculuklar
p|enjoy your meal|afiyet olsun
w|cheers|şerefe
p|congratulations|tebrikler
p|all the best|her şey gönlünce olsun
p|get well soon|geçmiş olsun
p|have a nice weekend|iyi hafta sonları
p|here you are|buyurun
w|pardon me|pardon
w|attention|dikkat
w|help!|imdat!
w|zero|sıfır
w|one|bir
w|two|iki
w|three|üç
w|four|dört
w|five|beş
w|six|altı
w|seven|yedi
w|eight|sekiz
w|nine|dokuz
w|ten|on
w|eleven|on bir
w|twelve|on iki
w|thirteen|on üç
w|fourteen|on dört
w|fifteen|on beş
w|sixteen|on altı
w|seventeen|on yedi
w|eighteen|on sekiz
w|nineteen|on dokuz
w|twenty|yirmi
w|thirty|otuz
w|forty|kırk
w|fifty|elli
w|sixty|altmış
w|seventy|yetmiş
w|eighty|seksen
w|ninety|doksan
w|hundred|yüz
w|thousand|bin
n|million|milyon
w|first|birinci, önce
w|second|ikinci
w|third|üçüncü
w|last|sonuncu, en son
w|half|yarım
n|half (noun)|yarısı
n|quarter|çeyrek
n|pair|çift
n|dozen|düzine
w|much|çok
w|little|az
w|more|daha fazla
w|less|daha az
w|enough|yeterli
w|all|hepsi
w|nothing|hiçbir şey
w|something|bir şey, biraz
n|number|sayı
n|number (phone|numara
n|percent|yüzde
n|piece|adet, parça
n|kilo|kilo
n|gram|gram
n|litre|litre
n|colour|renk
w|red|kırmızı
w|blue|mavi
w|yellow|sarı
w|green|yeşil
w|black|siyah
w|white|beyaz
w|grey|gri
w|brown|kahverengi
w|orange|turuncu
w|pink|pembe
w|purple|mor
w|colourful|rengarenk
w|light|açık (renk), aydınlık, hafif
w|dark|koyu, karanlık
n|circle|daire
n|square|kare, meydan, yer
n|line|çizgi
w|round|yuvarlak
w|I|ben
w|you|sen
w|he|o (erkek)
w|she|o (kadın), onlar
w|it|o (nötr)
w|we|biz
w|you (plural)|siz
w|my|benim
w|your|senin
w|his|onun (erkek)
w|our|bizim
w|your (plural)|sizin
w|me|beni
w|you (object)|seni
w|one (people in general)|(genel özne) insan
w|this|bu
w|that|şu, o, ki
w|every|her biri
w|some|bazıları
w|others|diğerleri
w|oneself|kendi
w|and|ve
w|or|veya
w|but|ama, yine de
w|because|çünkü, -dığı için
w|if|eğer, -dığında
w|when|-iken, -den (karşılaştırma), ne zaman
w|whether|-ip -mediğini
w|although|-mesine rağmen
w|so that|ki (amaç)
w|so|yani, öyleyse
w|but rather|aksine, bilakis
p|both … and|hem ... hem de
p|either … or|ya ... ya da
p|neither … nor|ne ... ne de
w|in|içinde
w|at|-de, kenarında, yanında
w|on|üstünde
w|under|altında
w|over|üzerinde, hakkında
w|in front of|önünde, önce
w|behind|arkasında
w|next to|yanında
w|between|arasında
w|with|ile
w|without|-siz, olmadan
w|for|için
w|against|karşı
w|from|-den, -in
w|to|-e, -a
w|after|-den sonra, -e doğru
w|out of|-den (içinden)
w|since|-den beri
w|until|-e kadar
w|through|içinden, vasıtasıyla
w|around|etrafında, saat -de
w|during|sırasında
w|because of|yüzünden
w|instead of|yerine
w|except|hariç
w|opposite|karşısında
w|who|kim
w|what|ne
w|where|nerede
w|where to|nereye
w|where from|nereden
w|how|nasıl
w|why|neden, niçin
w|how come|niçin
w|which|hangi
p|how much|ne kadar
p|how many|kaç tane
p|how long|ne kadar süre
p|how often|ne sıklıkta
p|how far|ne kadar uzak
w|whom|kimi
w|whose|kimin
n|time|zaman
n|clock|saat (alet)
n|hour|saat (süre)
n|minute|dakika
n|month|ay
n|year|yıl
n|morning|sabah
n|late morning|öğleden önce
n|noon|öğle
n|afternoon|öğleden sonra
n|evening|akşam
n|night|gece
w|yesterday|dün
w|now|şimdi
w|right away|hemen, birazdan
w|immediately|derhal
w|later|sonra
w|earlier|daha önce
w|soon|yakında
w|just now|tam şu an
w|never|asla
w|sometimes|bazen
w|often|sık sık
w|rarely|nadiren
w|mostly|çoğunlukla
w|daily|günlük
w|weekly|haftalık
w|monthly|aylık
w|yearly|yıllık
n|Monday|Pazartesi
n|Tuesday|Salı
n|Wednesday|Çarşamba
n|Thursday|Perşembe
n|Friday|Cuma
n|Saturday|Cumartesi
n|Sunday|Pazar
n|weekend|hafta sonu
n|working day|iş günü
n|public holiday|resmi tatil
n|January|Ocak
n|February|Şubat
n|March|Mart
n|April|Nisan
n|May|Mayıs
n|June|Haziran
n|July|Temmuz
n|August|Ağustos
n|September|Eylül
n|October|Ekim
n|November|Kasım
n|December|Aralık
n|spring|ilkbahar
n|summer|yaz
n|autumn|sonbahar
n|winter|kış
n|season|mevsim
n|date|tarih
n|calendar|takvim
n|past|geçmiş
n|present|şimdiki zaman, hediye
n|future|gelecek
n|birthday|doğum günü
n|delay|gecikme
w|punctual|dakik
n|human being|insan
n|people|insanlar
n|person|kişi
n|man|adam, koca
n|woman|kadın, eş
n|boy|erkek çocuk
n|girl|kız çocuk
n|baby|bebek
n|parents|ebeveynler
n|father|baba
n|mother|anne
n|son|oğul
n|daughter|kız evlat
n|brother|erkek kardeş
n|sister|kız kardeş
n|siblings|kardeşler
n|grandparents|büyükanne ve büyükbaba
n|grandfather|dede
n|grandmother|büyükanne
n|grandpa|dede (samimi)
n|grandma|nine (samimi)
n|grandson|torun
n|uncle|amca, dayı
n|aunt|teyze, hala
n|cousin (male)|kuzen (erkek)
n|cousin (female)|kuzen (kız)
n|nephew|yeğen (erkek)
n|niece|yeğen (kız)
n|father-in-law|kayınpeder
n|mother-in-law|kaynana
n|husband|koca
n|wife|eş, karı
n|partner|partner
n|girlfriend|kız arkadaş
n|colleague|iş arkadaşı
n|guest|misafir
n|adult|yetişkin
n|teenager|genç
n|first name|ad
n|surname|soyadı
n|age|yaş
n|wedding|düğün
n|marriage|evlilik
n|love|aşk, sevgi
n|friendship|arkadaşlık
w|single|bekâr
w|married|evli
w|divorced|boşanmış
w|pregnant|hamile
w|related|akraba
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
n|body|vücut
n|head|kafa
n|hair|saç
n|face|yüz
n|eye|göz
n|nose|burun
n|mouth|ağız
n|ear|kulak
n|tooth|diş
n|neck|boyun, boğaz
n|arm|kol
n|hand|el
n|finger|parmak
n|back|sırt
n|belly|karın
n|leg|bacak
n|knee|diz
n|foot|ayak
n|skin|cilt
n|heart|kalp
n|blood|kan
n|health|sağlık
n|illness|hastalık
w|healthy|sağlıklı
n|pain|ağrılar
n|cold|soğuk algınlığı
n|fever|ateş
n|cough|öksürük
n|flu|grip
n|allergy|alerji
n|wound|yara
n|accident|kaza
n|doctor|doktor
n|doctor (female)|doktor (kadın)
n|dentist|diş hekimi
n|hospital|hastane
n|doctor's office|muayenehane
n|medicine|ilaç
n|pill|hap
n|prescription|reçete
n|examination|muayene
n|health insurance|sağlık sigortası
n|insurance card|sigorta kartı
n|emergency room|acil servis
n|ambulance|ambulans
n|treatment|tedavi
w|weak|zayıf, güçsüz
w|strong|güçlü
n|glasses|gözlük
v|to sleep|uyumak|slept · slept
v|rest|dinlenmek
v|hurt|acıtmak|hurt · hurt
v|feel|hissetmek|felt · felt
v|breathe|nefes almak
v|heal|iyileşmek
n|flat|daire
n|living room|oturma odası
n|bedroom|yatak odası
n|bathroom|banyo
n|toilet|tuvalet
n|hallway|koridor
n|balcony|balkon
n|garden|bahçe
n|basement|bodrum
n|door|kapı
n|window|pencere
n|wall|duvar
n|floor|zemin, kat
n|ceiling|tavan, battaniye
n|roof|çatı
n|stairs|merdiven
n|lift|asansör
n|lock|kilit, şato
n|furniture|mobilya
n|armchair|koltuk
n|sofa|kanepe
n|bed|yatak
n|cupboard|dolap
n|shelf|raf
n|lamp|lamba
n|carpet|halı
n|mirror|ayna
n|picture|resim, tablo
n|towel|havlu
n|soap|sabun
n|toothbrush|diş fırçası
n|toothpaste|diş macunu
n|shampoo|şampuan
n|shower|duş
n|washbasin|lavabo
n|washing machine|çamaşır makinesi
n|fridge|buzdolabı
n|stove|ocak
n|oven|fırın
n|dishwasher|bulaşık makinesi
n|heating|kalorifer
n|air conditioning|klima
n|rubbish|çöp
n|bin|çöp kovası
n|socket|priz
n|plug|fiş
n|tenant|kiracı
n|landlord|ev sahibi
n|additional costs|yan giderler
n|deposit|depozito
n|rental agreement|kira sözleşmesi
n|caretaker|apartman görevlisi
n|street|sokak, cadde
n|house number|kapı numarası
n|postcode|posta kodu
n|ground floor|zemin kat
n|move (house)|taşınma
n|housework|ev işi
v|clean|temizlemek
v|tidy up|toplamak, düzenlemek
v|wash|yıkamak
v|cook|yemek pişirmek
v|to live|oturmak, yaşamak
v|to rent|kiralamak
v|to move (house)|taşınmak
w|cosy|rahat, sıcak (ortam)
w|dirty|kirli
n|food|yemek
n|lunch|öğle yemeği
n|dinner|akşam yemeği
n|hunger|açlık
n|thirst|susuzluk
w|hungry|aç
w|thirsty|susuz
n|bread roll|küçük ekmek
n|butter|tereyağı
n|cheese|peynir
n|egg|yumurta
n|milk|süt
n|yoghurt|yoğurt
n|cream|krema
n|meat|et
n|beef|dana eti
n|chicken|tavuk
n|pork|domuz eti
n|sausage|sosis, sucuk
n|ham|jambon
n|fish|balık
n|soup|çorba
n|salad|salata
n|vegetables|sebze
n|fruit|meyve
n|potato|patates
n|tomato|domates
n|cucumber|salatalık
n|onion|soğan
n|garlic|sarımsak
n|carrot|havuç
n|pepper (spice)|biber (baharat)
n|pepper (vegetable)|biber
n|rice|pirinç
n|pasta|makarna
n|flour|un
n|sugar|şeker
n|salt|tuz
n|oil|yağ
n|apple|elma
n|banana|muz
n|lemon|limon
n|strawberry|çilek
n|cake|kek, pasta
n|chocolate|çikolata
n|ice cream|dondurma, buz
n|honey|bal
n|jam|reçel
n|coffee|kahve
n|tea|çay
n|juice|meyve suyu
n|beer|bira
n|wine|şarap
n|lemonade|gazoz
n|bottle|şişe
n|glass|bardak, cam
n|cup|fincan
n|plate|tabak
n|fork|çatal
n|knife|bıçak
n|spoon|kaşık
n|pot|tencere
n|pan|tava
n|restaurant|restoran
n|café|kafe
n|menu|menü
n|tip|bahşiş
n|waiter|garson
n|order|sipariş, görev
n|starter|başlangıç
n|main course|ana yemek
n|dessert|tatlı
n|ingredient|malzeme
w|delicious|lezzetli
w|sweet|tatlı
w|salty|tuzlu
w|sour|ekşi
w|spicy|acı, keskin
w|fresh|taze
w|cooked|pişmiş, haşlanmış
v|to eat|yemek yemek|ate · eaten
v|to drink|içmek|drank · drunk
v|bake|fırında pişirmek
v|fry|kızartmak
v|cut|kesmek|cut · cut
v|try|denemek, tatmak
v|to order|sipariş vermek
v|to pay|ödemek|paid · paid
w|full (after eating)|tok
w|vegetarian|vejetaryen
n|clothes|giysi
n|shirt|gömlek
n|T-shirt|tişört
n|jumper|kazak
n|jacket|ceket, mont
n|coat|palto
n|trousers|pantolon
n|jeans|kot pantolon
n|skirt|etek
n|dress|elbise
n|sock|çorap
n|underwear|iç çamaşırı
n|shoe|ayakkabı
n|hat|şapka
n|cap|bere
n|scarf|atkı
n|belt|kemer
n|bag|çanta
n|backpack|sırt çantası
n|umbrella|şemsiye
n|jewellery|takı
n|size|beden, boyut
v|put on|giymek|put on · put on
v|take off|çıkarmak (giysi)|took off · taken off
v|wear|giymek, taşımak|wore · worn
v|try on|denemek (giysi)
v|fit|uymak
v|suit|yakışmak, durmak
w|tight|dar
w|wide|geniş, uzak
w|fashionable|modaya uygun
w|comfortable|rahat
n|changing room|deneme kabini
n|laundry|çamaşır
n|brand|marka
n|fashion|moda
n|sunglasses|güneş gözlüğü
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
n|village|köy
n|centre|merkez
n|city centre|şehir merkezi
n|park|park
n|bridge|köprü
n|river|nehir
n|building|bina
n|church|kilise
n|mosque|cami
n|museum|müze
n|theatre|tiyatro
n|cinema|sinema
n|library|kütüphane
n|school|okul
n|university|üniversite, yüksekokul
n|town hall|belediye binası
n|post office|postane
n|bank|banka
n|hotel|otel
n|store|mağaza
n|supermarket|süpermarket
n|bakery|fırın
n|butcher's|kasap
n|market|pazar
n|shopping centre|alışveriş merkezi
n|petrol station|benzin istasyonu
n|car park|otopark
n|train station|tren istasyonu
n|stop (bus|durak
n|airport|havalimanı
n|harbour|liman
n|stadium|stadyum
n|swimming pool|yüzme havuzu
n|gym|spor salonu
n|hairdresser|kuaför
n|police|polis
n|fire brigade|itfaiye
n|zoo|hayvanat bahçesi
n|corner|köşe
n|crossroads|kavşak
n|traffic light|trafik ışığı
n|pavement|kaldırım
n|way|yol, patika
n|direction|yön
w|left|sol
w|straight ahead|dümdüz
w|above|yukarıda
w|below|aşağıda
w|at the front|önde
w|at the back|arkada
n|middle|orta
n|side|taraf, sayfa
w|near|yakın
n|surroundings|çevre
n|place|yer, mekân
n|area|bölge
n|border|sınır
n|capital city|başkent
n|inhabitant|sakin, oturan
n|sight (tourist attraction)|turistik yer
n|monument|anıt
n|tower|kule
n|view|manzara
n|trip|seyahat
n|traffic|trafik
n|car|araba
n|bus|otobüs
n|train|tren, demiryolu
n|suburban train|banliyö treni
n|underground|metro
n|tram|tramvay
n|bicycle|bisiklet
n|motorbike|motosiklet
n|taxi|taksi
n|plane|uçak
n|ship|gemi
n|driving licence|ehliyet
n|timetable|tarife
n|platform|peron, ray
n|exit|çıkış
n|entrance|giriş
n|departure|kalkış
n|arrival|varış
n|connection|bağlantı, hat
v|change (trains)|aktarma yapmak
v|get on|binmek|got on · got on
v|get off|inmek|got off · got off
v|drive|gitmek (araçla)|drove · driven
v|fly|uçmak|flew · flown
v|walk|yürümek, koşmak
p|on foot|yaya olarak
n|motorway|otoyol
n|speed|hız
n|petrol|benzin
n|engine|motor
n|wheel|tekerlek
n|tyre|lastik
n|breakdown|arıza
n|route|güzergâh, mesafe
n|distance|mesafe
n|suitcase|bavul
n|luggage|bagaj
n|passport|pasaport
n|visa|vize
n|ID card|kimlik
n|customs|gümrük
n|booking|rezervasyon
n|accommodation|konaklama
n|youth hostel|gençlik yurdu
n|tent|çadır
n|school holidays|tatil (okul)
n|excursion|gezi
n|tour|tur
n|tourist|turist
n|map|harita, kart
n|satnav|navigasyon
n|traffic jam|trafik sıkışıklığı
n|construction site|şantiye, yol çalışması
v|visit|gezmek, ziyaret etmek
v|reserve|rezervasyon yapmak
v|pack|valiz hazırlamak
v|arrive|varmak
v|depart|hareket etmek, ayrılmak (yolculuğa çıkmak)
v|miss|kaçırmak
v|to wait|beklemek
n|safety|güvenlik
n|euro|avro
n|cent|sent
n|checkout|kasa
n|receipt|fiş
n|salesperson|satıcı
n|shopping|alışveriş
n|shopping list|alışveriş listesi
n|shopping trolley|alışveriş arabası
n|plastic bag|poşet
n|offer|kampanya, teklif
n|discount|indirim
n|clearance sale|büyük indirim
w|free of charge|ücretsiz
w|good value|uygun fiyatlı
n|cash|nakit
n|credit card|kredi kartı
n|debit card|banka kartı
n|account|hesap
n|bank transfer|havale
n|bank sort code|banka kodu
n|IBAN|IBAN
n|cash machine|ATM
n|change (money)|para üstü
n|tax|vergi
n|VAT|KDV
n|fee|ücret, harç
n|costs|maliyet
n|income|gelir
v|save|biriktirmek, tasarruf etmek, kaydetmek
v|spend|harcamak|spent · spent
v|to buy|satın almak|bought · bought
v|sell|satmak|sold · sold
v|cost|fiyatı olmak|cost · cost
v|exchange|değiştirmek (ürün)
v|give back|iade etmek
n|guarantee|garanti
n|delivery|teslimat
n|goods|ürün, mal
n|product|ürün
n|quality|kalite
n|amount|miktar
n|choice|seçenek, çeşit
n|complaint (return)|şikâyet, iade talebi
n|instalment|taksit
n|debts|borç
v|to have|sahip olmak|had · had
v|become|olmak; -ecek (gelecek zaman)|became · become
v|can|-ebilmek
v|must|zorunda olmak
v|to want|istemek
w|should|-meli
v|to may|izni olmak
v|to like|hoşlanmak
v|make|yapmak|made · made
v|do|yapmak, etmek|did · done
v|to go|gitmek, yürümek|went · gone
v|to come|gelmek|came · come
v|say|söylemek|said · said
v|to speak|konuşmak|spoke · spoken
v|talk|konuşmak, sohbet etmek
v|ask|sormak
v|answer|cevap vermek
v|see|görmek|saw · seen
v|look|bakmak
v|hear|duymak, dinlemek|heard · heard
v|listen|dinlemek
v|know (a fact)|bilmek
v|know (a person)|tanımak
v|to think|düşünmek|thought · thought
v|believe|inanmak, sanmak
v|mean|demek istemek, düşünmek, anlamına gelmek|meant · meant
v|hope|ummak
v|wish|dilemek
v|to need|ihtiyacı olmak
v|get|almak, edinmek|got · got/gotten
v|take|almak|took · taken
v|give|vermek|gave · given
v|bring|getirmek|brought · brought
v|fetch|alıp getirmek
v|hold|tutmak|held · held
v|lay|yatırmak, koymak|laid · laid
v|put (upright)|dikey koymak
v|set|oturtmak, koymak|set · set
v|sit|oturmak|sat · sat
v|lie|yatmak, bulunmak|lay · lain
v|to get up|kalkmak|got up · got up
v|wake up|uyanmak|woke up · woken up
v|fall asleep|uykuya dalmak|fell asleep · fallen asleep
v|to stay|kalmak
v|belong|ait olmak
v|begin|başlamak|began · begun
v|start|başlamak, başlatmak
v|stop|durmak, bırakmak, durdurmak
v|end|bitmek
v|finish|bitirmek
v|to carry on|devam etmek
v|manage|başarmak, oluşturmak
v|succeed|başarılı olmak
v|fail|başarısız olmak
v|to help|yardım etmek
v|thank|teşekkür etmek
v|ask (for)|rica etmek
v|allow|izin vermek
v|forbid|yasaklamak|forbade · forbidden
v|to decide|karar vermek
v|choose|seçmek|chose · chosen
v|plan|planlamak
v|change|değiştirmek, değişmek
v|to improve|iyileştirmek
v|grow|büyümek|grew · grown
v|happen|olmak, meydana gelmek, gerçekleşmek
v|take place|gerçekleşmek (etkinlik)
v|to last|sürmek
v|to meet|buluşmak, isabet etmek|met · met
v|invite|davet etmek
v|come along|birlikte gelmek
v|accompany|eşlik etmek
v|leave|terk etmek|left · left
v|say goodbye|vedalaşmak
v|reach|ulaşmak
v|recognise|tanımak, fark etmek
v|to notice|fark etmek, aklında tutmak
v|travel|seyahat etmek
v|to work|çalışmak (makine)
v|exist|var olmak
v|enjoy|keyfini çıkarmak
v|fear|korkmak
v|trust|güvenmek
v|risk|risk almak
v|be missing|eksik olmak
v|be bored|sıkılmak
v|annoy|kızdırmak
v|calm (sb) down|sakinleştirmek
v|surprise|şaşırtmak
v|excuse|affetmek, mazur görmek
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
n|profession|meslek
n|job|iş
n|position|pozisyon, iş yeri
n|firm|firma
n|company|şirket
n|office|ofis
n|boss|patron
n|employee|çalışan
n|team|ekip, takım
n|department|departman
n|meeting|toplantı, oturum
n|task|görev
n|project|proje
n|vocational training|mesleki eğitim
n|internship|staj
n|CV|özgeçmiş
n|job interview|iş görüşmesi
n|working hours|çalışma saati
n|overtime|fazla mesai
n|break|mola
n|shift|vardiya
n|end of the working day|paydos
n|full-time|tam zamanlı
n|part-time|yarı zamanlı
n|mini-job|mini iş (az ücretli iş)
n|working student|öğrenci çalışan
w|unemployed|işsiz
w|self-employed|serbest çalışan
n|teacher|öğretmen
n|engineer|mühendis
n|lawyer|avukat
n|baker|fırıncı
n|driver|şoför
n|police officer|polis memuru
n|nurse (male)|hemşire (erkek)
n|nurse|hemşire
n|craftsman|zanaatkâr, usta
n|electrician|elektrikçi
n|mechanic|tamirci
n|programmer|yazılımcı
n|computer scientist|bilgisayar bilimci
n|architect|mimar
n|artist|sanatçı
n|journalist|gazeteci
n|civil servant|memur
n|student (university)|öğrenci (üniversite)
n|intern|stajyer
n|pensioner|emekli
v|earn|kazanmak
v|lead|yönetmek, yönlendirmek, götürmek|led · led
v|apply|başvurmak, uygulamak
v|hire|işe almak
v|quit|işten ayrılmak, çıkarmak
n|career|kariyer
n|promotion|terfi
n|ability|yetenek
n|kindergarten|anaokulu
n|primary school|ilkokul
n|grammar school|lise
n|lessons|ders (saat)
n|subject|ders (branş)
n|class|sınıf
n|course|kurs
n|lecture|ders (üniversite)
n|seminar|seminer
n|pupil|öğrenci (okul)
n|professor|profesör
n|homework|ödev
n|test|test
n|grade|not
n|school report|karne, belge
n|school-leaving exam (A levels)|lise bitirme sınavı
n|university studies|üniversite eğitimi
n|degree|mezuniyet, derece
n|bachelor's degree|lisans
n|master's degree|yüksek lisans
n|semester|dönem
n|book|kitap
n|notebook|defter
n|sheet|yaprak, sayfa
n|paper|kâğıt
n|pen|kalem
n|pencil|kurşun kalem
n|ballpoint pen|tükenmez kalem
n|eraser|silgi
n|ruler|cetvel
n|scissors|makas
n|board|tahta
n|desk|çalışma masası
n|dictionary|sözlük
n|grammar|dilbilgisi
n|word|kelime
n|sentence|cümle
n|text|metin
n|exercise|alıştırma
n|mistake|hata
n|example|örnek
n|topic|konu
n|knowledge|bilgi
v|learn|öğrenmek|learnt · learnt
v|study (at university)|üniversitede okumak
v|teach|öğretmek|taught · taught
v|to explain|açıklamak
v|to understand|anlamak|understood · understood
v|practise|alıştırma yapmak
v|repeat|tekrar etmek
v|to read|okumak|read · read
v|to write|yazmak|wrote · written
v|calculate|hesaplamak
v|pass (an exam)|(sınavı) geçmek
v|fail (an exam)|sınavda kalmak
n|maths|matematik
n|physics|fizik
n|chemistry|kimya
n|biology|biyoloji
n|history|tarih, hikâye
n|geography|coğrafya
n|art|sanat
n|music|müzik
n|nature|doğa
n|sun|güneş
n|moon|ay (gökyüzü)
n|star|yıldız
n|sky|gökyüzü
n|cloud|bulut
n|rain|yağmur
n|snow|kar
n|wind|rüzgâr
n|storm|fırtına
n|fog|sis
n|temperature|sıcaklık
w|warm|ılık, sıcak
w|hot|çok sıcak
w|cool|serin
w|sunny|güneşli
w|cloudy|bulutlu
w|rainy|yağmurlu
w|windy|rüzgârlı
w|foggy|sisli
w|dry|kuru
w|wet|ıslak
w|humid|nemli
n|mountain|dağ
n|valley|vadi
n|forest|orman
n|tree|ağaç
n|flower|çiçek
n|grass|çimen
n|lake|göl
n|sea|deniz
n|beach|plaj
n|island|ada
n|coast|kıyı
n|stone|taş
n|earth|toprak, dünya
n|world|dünya
n|air|hava
n|fire|ateş
n|climate change|iklim değişikliği
n|energy|enerji
n|animal|hayvan
n|pet|evcil hayvan
n|dog|köpek
n|cat|kedi
n|horse|at
n|cow|inek
n|sheep|koyun
n|goat|keçi
n|pig|domuz
n|hen|tavuk
n|rooster|horoz
n|duck|ördek
n|bird|kuş
n|mouse|fare
n|rabbit|tavşan
n|bear|ayı
n|lion|aslan
n|elephant|fil
n|snake|yılan
n|bee|arı
n|insect|böcek
n|tail|kuyruk
n|wing|kanat
n|fur|kürk, tüy
v|bark|havlamak
v|eat (animals)|yem yemek (hayvan)
v|feed|beslemek|fed · fed
w|wild|vahşi
n|computer|bilgisayar
n|laptop|dizüstü bilgisayar
n|mobile phone|cep telefonu
n|smartphone|akıllı telefon
n|telephone|telefon
n|screen|ekran
n|keyboard|klavye
n|file|dosya
n|program|program
n|software|yazılım
n|app|uygulama
n|internet|internet
n|website|web sitesi
n|email|e-posta
n|message|mesaj, haber
n|password|şifre
n|user|kullanıcı
n|data|veri
n|memory|bellek, depolama
n|Wi-Fi|kablosuz internet
n|battery|batarya
n|charger|şarj aleti
n|phone call|arama
v|call (on the phone)|telefonla aramak
v|talk on the phone|telefonla konuşmak
v|send|göndermek, yollamak|sent · sent
v|download|indirmek
v|upload|yüklemek
v|delete|silmek
v|click|tıklamak
v|search|aramak
v|find|bulmak|found · found
v|install|kurmak
v|switch off|kapatmak
v|switch on|açmak
n|television|televizyon
n|photo|fotoğraf
n|video|video
n|technology|teknik, teknoloji
v|to shower|duş almak
v|bathe|banyo yapmak
v|comb|taramak (saç)
v|shave|tıraş etmek
v|note down|not almak
v|organise|organize etmek
v|paint|resim yapmak, boyamak
v|draw|çizmek|drew · drawn
v|do crafts|el işi yapmak
v|expect|beklemek (ummak)
v|swim|yüzmek|swam · swum
v|jump|zıplamak, atlamak
v|climb|tırmanmak
v|smoke|sigara içmek
v|surf|internette gezinmek; sörf yapmak
v|chat|sohbet etmek (internette)
v|post|paylaşım yapmak
v|like (a post)|beğenmek (sosyal medya)
v|comment|yorum yapmak
v|print|yazdırmak
v|scan|taramak
v|grill|ızgara yapmak
v|wash up|bulaşık yıkamak; durulamak
v|iron|ütü yapmak
v|sew|dikiş dikmek|sewed · sewn
v|glue|yapıştırmak
v|hang up|telefonu kapatmak|hung up · hung up
v|unload|yük boşaltmak; daveti iptal etmek
v|to park|park etmek
v|refuel|benzin almak
v|sort|ayırmak, sıralamak
v|look at|incelemek, bakmak
v|check|kontrol etmek, sınamak
v|enter|kaydetmek, yazmak
v|advise|tavsiye etmek; tahmin etmek
v|warn|uyarmak
v|threaten|tehdit etmek
v|return|geri dönmek
v|disappear|kaybolmak
v|appear|görünmek, çıkmak (yayın)
v|arise|ortaya çıkmak, oluşmak|arose · arisen
v|develop|gelişmek, geliştirmek
v|make worse|kötüleştirmek
v|secure|güvence altına almak; yedeklemek
v|halve|ikiye bölmek
v|double|iki katına çıkarmak
v|multiply|çarpmak
v|add|toplamak
v|subtract|çıkarmak (matematik)
v|divide|bölmek (matematik)
v|distinguish|ayırt etmek
v|arrange|düzenlemek
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
w|Germany|Almanya
n|Turkey|Türkiye
w|Austria|Avusturya
n|Switzerland|İsviçre
w|France|Fransa
w|Russia|Rusya
w|Europe|Avrupa
n|language|dil
w|German|Almanca
w|Turkish|Türkçe
w|English|İngilizce
n|mother tongue|ana dil
n|foreigner|yabancı
n|nationality|uyruk
n|citizenship|vatandaşlık
n|culture|kültür
n|tradition|gelenek
n|religion|din
n|society|toplum
n|government|hükümet
n|state|devlet
n|politics|siyaset
n|law|kanun
n|freedom|özgürlük
n|newspaper|gazete
n|news|haberler
n|problem|sorun
n|sport|spor
n|game|oyun, maç
n|football|futbol
n|swimming|yüzme
n|running|koşu
n|fitness|fitness
n|training|antrenman
n|player|oyuncu
n|coach|antrenör
n|victory|zafer
n|ball|top
n|free time|boş zaman
n|hobby|hobi
n|song|şarkı
n|film|film
n|series|dizi
n|concert|konser
n|party|parti
n|festival|kutlama, festival
n|celebration|kutlama
n|reading|okuma
n|cooking|yemek yapma
v|to win|kazanmak|won · won
v|to lose|kaybetmek|lost · lost
v|play|oynamak
v|to train|antrenman yapmak
v|relax|rahatlamak
v|celebrate|kutlamak
v|dance|dans etmek
v|sing|şarkı söylemek|sang · sung
n|public office|resmî daire
n|citizens' office|nüfus dairesi
n|immigration office|yabancılar dairesi
n|tax office|vergi dairesi
n|job centre|iş kurumu
n|Federal Employment Agency|iş ajansı
n|registration|adres kaydı, kayıt
n|deregistration|kayıt sildirme
n|certificate|belge, yazı
n|form|form
n|application|başvuru
n|official notice|karar yazısı
n|signature|imza
n|stamp|mühür
n|copy|kopya
n|original|asıl, orijinal
n|deadline|süre, son tarih
n|proof|kanıt, belge
n|registration certificate|ikamet belgesi
n|residence permit|oturma izni
n|work permit|çalışma izni
n|tax ID|vergi numarası
n|social security|sosyal sigorta
n|pension insurance|emeklilik sigortası
n|liability insurance|sorumluluk sigortası
n|broadcasting fee (TV licence)|yayın katkı payı
n|case worker|dosya sorumlusu
n|counter|gişe
n|queue number|sıra numarası
n|opening hours|açılış saatleri
v|to apply for|başvurmak
v|fill in|doldurmak
v|submit|teslim etmek
v|sign|imzalamak
v|extend|uzatmak
v|bring along|yanında getirmek
v|pick up|teslim almak
v|register|kaydolmak
w|allowed|izinli
w|forbidden|yasak
w|necessary|gerekli
w|valid|geçerli
v|to forget|unutmak|forgot · forgotten
v|remember|hatırlamak
v|to compare|karşılaştırmak
v|to describe|tarif etmek
v|tell|anlatmak|told · told
v|report|rapor etmek, bildirmek
v|show|göstermek|showed · shown
v|translate|çevirmek
v|pronounce|telaffuz etmek
v|to open|açmak
v|to close|kapatmak
v|press|basmak, itmek
v|pull|çekmek
v|throw|atmak|threw · thrown
v|catch|yakalamak|caught · caught
v|fall|düşmek|fell · fallen
v|to lift|kaldırmak
v|build|inşa etmek|built · built
v|repair|tamir etmek
v|break (something)|bozmak
v|use|kullanmak, yararlanmak, kullanmak
v|collect|toplamak, biriktirmek
v|share|paylaşmak, bölmek
v|distribute|dağıtmak
v|swap|takas etmek
v|lend|ödünç vermek, almak|lent · lent
v|own|sahip olmak
v|discover|keşfetmek
v|inform|bildirmek, bilgilendirmek
v|argue|tartışmak, kavga etmek, tartışmak, kavga etmek
v|discuss|tartışmak
v|promise|söz vermek
v|lie (tell lies)|yalan söylemek|lied · lied
v|disturb|rahatsız etmek
v|hurry|acele etmek
v|observe|gözlemlemek
v|pay attention|dikkat etmek
v|take care of|ilgilenmek
v|worry|endişelenmek, ilgilenmek
v|protect|korumak
v|fight|savaşmak, mücadele etmek|fought · fought
v|interest|ilgisini çekmek
v|please (be liked)|hoşuna gitmek
v|to love|sevmek
v|hate|nefret etmek
v|laugh|gülmek
v|cry|ağlamak
v|smile|gülümsemek
v|kiss|öpmek
v|to call|seslenmek, çağırmak
v|scream|bağırmak
v|smell|koklamak, kokmak|smelt · smelt
v|taste|tadı olmak
v|touch|dokunmak
v|weigh|tartmak
v|to measure|ölçmek
v|count|saymak
v|rent out|kiraya vermek
v|deliver|teslim etmek
v|follow|takip etmek
v|to recommend|tavsiye etmek
v|suggest|önermek
v|to offer|sunmak
v|accept|kabul etmek, varsaymak
v|to reject|reddetmek
v|run|koşmak|ran · run
v|dream|rüya görmek, hayal etmek|dreamt · dreamt
w|bad|kötü
w|long|uzun
w|short|kısa
w|high|yüksek
w|low|alçak
w|narrow|dar
w|thick|kalın, şişman
w|thin|ince
w|heavy|ağır, zor
w|new|yeni
w|old|eski, yaşlı
w|young|genç
w|modern|modern
w|slow|yavaş
w|loud|gürültülü
w|quiet|sessiz
w|full|dolu
w|empty|boş
w|closed|kapalı
w|wrong|yanlış
w|true|gerçek
w|possible|mümkün
w|impossible|imkânsız
w|simple|basit, kolay
w|difficult|zor
w|complicated|karmaşık
w|interesting|ilginç
w|boring|sıkıcı
w|beautiful|güzel
w|nice|kibar, hoş
w|friendly|dostane
w|polite|nazik
w|calm|sakin
w|nervous|gergin
w|hard-working|çalışkan
w|lazy|tembel, çürük
w|clever|akıllı
w|stupid|aptal
w|dangerous|tehlikeli
w|safe|güvenli, emin
w|free|özgür, boş
w|occupied|dolu, meşgul
w|ready|hazır
w|finished|bitmiş, hazır
w|useful|faydalı
w|popular|sevilen, popüler
w|well-known|tanınmış
w|foreign|yabancı
w|similar|benzer
w|different|farklı
w|special|özel, özellikle
w|normal|normal
w|real|gerçek, hakiki
w|private|özel, kişisel
w|public|kamuya açık
w|poor|fakir
w|rich|zengin
w|sad|üzgün
w|funny|komik
w|serious|ciddi
w|proud|gururlu
w|brave|cesur
w|patient|sabırlı
w|successful|başarılı
w|helpful|yardımsever
w|creative|yaratıcı
w|practical|pratik
w|perfect|mükemmel
w|wonderful|harika
w|great|süper
v|solve|çözmek
v|fasten|sabitlemek
v|obey|itaat etmek
v|give (as a present)|hediye etmek
v|borrow|ödünç almak
v|invest|yatırım yapmak
v|come back|geri gelmek
v|go back|geri gitmek
v|set off|yola çıkmak
v|take along|yanında götürmek
v|throw away|çöpe atmak
v|unpack|paketi açmak
v|mark|işaretlemek
v|to copy|kopyalamak
v|transfer|aktarmak; yayınlamak
v|connect|bağlamak
v|separate|ayırmak
v|to come across|karşılaşmak (+ Dativ)
v|receive|karşılamak; almak (sinyal), almak, teslim almak; korumak
v|admire|hayran olmak
v|complete|tamamlamak
v|prove|kanıtlamak
v|worsen|kötüleştirmek
v|expand|genişletmek
v|to reduce|azaltmak
v|raise|artırmak
v|experiment|deney yapmak
v|pause|ara vermek
v|continue|devam ettirmek
v|interrupt|kesmek, bölmek
v|drop by|uğramak
v|drive past|yanından geçip gitmek
v|turn round|çevirmek, döndürmek
v|stay behind|geride kalmak
v|treat|tedavi etmek; davranmak
v|regret|üzülmek, pişman olmak
v|lament|yakınmak
v|mourn|ağıt yakmak, yasını tutmak
v|miss (sb)|özlemek
v|value|değer vermek; tahmin etmek
v|respect|saygı duymak
v|tolerate|hoş görmek
v|ignore|görmezden gelmek
v|analyse|analiz etmek
v|research|araştırmak
v|explain in detail|izah etmek
v|evaluate|değerlendirmek, not vermek
v|define|tanımlamak
v|construct|tasarlayıp inşa etmek
v|produce|üretmek
v|consume|tüketmek
v|export|ihraç etmek
v|import|ithal etmek
v|waste|israf etmek
v|to test|test etmek
v|go wrong|başarısız olmak (iş)
v|foresee|önceden görmek|foresaw · foreseen
v|thrive|gelişmek, serpilmek
v|pass (time)|geçmek (zaman)
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
n|joy|sevinç
n|happiness|mutluluk, şans
n|grief|keder
n|stress|stres
n|rage|öfke
n|anger|kızgınlık, dert
n|courage|cesaret
n|patience|sabır
n|boredom|can sıkıntısı
n|loneliness|yalnızlık
n|character|karakter
n|mood|keyif, ruh hâli, atmosfer
n|laughter|gülüş
n|tear|gözyaşı
v|be happy|sevinmek
v|get angry|sinirlenmek
v|be ashamed|utanmak
v|fall in love|âşık olmak
v|be surprised|şaşırmak
v|calm down|sakinleşmek
w|excited|heyecanlı
w|disappointed|hayal kırıklığına uğramış
w|surprised|şaşırmış
w|in love|âşık
w|furious|öfkeli
w|jealous|kıskanç
w|shy|utangaç
w|eager|merakla bekleyen
w|exhausted|tükenmiş
w|very|çok
w|fairly|epey
w|almost|neredeyse
w|only|sadece
w|also|de, da
w|still|hâlâ, daha
w|already|zaten, çoktan, hâlihazırda
w|only (not until)|ancak, ilk olarak
w|again|yine
p|above all|her şeyden önce
p|for example|örneğin
w|by the way|bu arada
w|really|gerçekten
w|certainly|mutlaka
w|probably|muhtemelen
w|hopefully|umarım
p|luckily|neyse ki
w|suddenly|aniden
w|finally|sonunda, nihayet
w|then|sonra
w|afterwards|ondan sonra
w|together|birlikte
w|alone|yalnız
w|jointly|ortaklaşa
w|everywhere|her yerde
w|there|orada, işte
w|here|burada
w|outside|dışarıda
w|inside|içeride
w|away|uzakta, gitmiş
w|further|daha ileri
w|otherwise|yoksa, başka
w|hardly|neredeyse hiç
w|not|değil
w|gladly|memnuniyetle
w|rather|tercihen
p|most of all|en çok
w|at least|en az
w|at most|en fazla
w|approximately|yaklaşık
w|about|yaklaşık
w|normally|normalde
w|in total|toplamda
w|besides|ayrıca
w|even|hatta
w|back then|o zamanlar
v|determine|belirlemek
v|introduce|tanıtmak
v|prepare oneself|hazırlanmak
v|meet (up)|buluşmak
v|sit down|oturmak
v|wash (oneself)|yıkanmak
v|get dressed|giyinmek
v|get undressed|soyunmak
v|fall in love with|-e âşık olmak
v|say thank you|teşekkür etmek
v|concentrate|odaklanmak
v|wish for|dilemek, istemek
v|be worth it|değmek
v|pay off|karşılığını vermek
v|think over|düşünüp taşınmak
v|be wrong|yanılmak
v|inform oneself|bilgi almak
v|to complain|şikâyet etmek
v|get lost|yolunu kaybetmek
v|make an effort|çaba göstermek
v|know one's way around|bir konuyu iyi bilmek
v|dare|cesaret etmek
v|get worse|kötüleşmek
v|to look forward to|dört gözle beklemek
v|look around|etrafa bakmak
v|get on (well)|anlaşmak
v|get along|iyi geçinmek
v|adapt|uyum sağlamak
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
n|consequence|sonuç
n|commitment|bağlılık; taahhüt
n|complaint|şikâyet
n|feature|özellik
n|habit|alışkanlık
n|majority|çoğunluk
n|minority|azınlık
n|access|erişim
n|cooperation|iş birliği
n|doubt|şüphe
v|require|gerektirmek
v|promote|teşvik etmek; terfi ettirmek
v|comply with|uymak
v|justify|gerekçelendirmek
v|assess|değerlendirmek
v|bear in mind|akılda tutmak
p|carry out|yürütmek, gerçekleştirmek
p|keep up with|ayak uydurmak
p|run into|rastlamak; karşılaşmak
p|sort out|halletmek
p|work out|çözmek; spor yapmak
p|go through|(zor bir süreç) yaşamak
a|mutual|karşılıklı
a|significant|önemli
a|clear-cut|net
d|presumably|muhtemelen
d|increasingly|giderek
d|in any case|her halükârda
v|appreciate|takdir etmek, değerini bilmek
v|attempt|teşebbüs etmek
v|blame|suçlamak
v|ensure|sağlamak, garantiye almak
v|handle|üstesinden gelmek, idare etmek
v|maintain|sürdürmek, savunmak
v|prevent|önlemek
v|seek|aramak, peşinde olmak|sought · sought
n|appeal|çekicilik, itiraz
n|capacity|kapasite, yetenek
a|essential|temel, şart
p|back down|geri adım atmak
p|get by|idare etmek, geçinmek
p|get on with|iyi geçinmek, devam etmek
p|give in|pes etmek, boyun eğmek
p|go over|gözden geçirmek
p|set out|yola koyulmak, ortaya koymak
p|set up|kurmak
p|take on|üstlenmek, işe almak
p|take up|başlamak (hobi), yer kaplamak
p|be that as it may|öyle olsa bile
p|in line with|-ile uyumlu olarak
p|that being said|bununla birlikte
d|thus|böylece
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
n|arrangement|düzenleme, anlaşma
n|dispute|anlaşmazlık
n|component|bileşen
n|overview|genel bakış
n|tendency|eğilim
n|ratio|oran
n|prediction|tahmin
n|cohesion|dayanışma
n|relief|rahatlama
v|negotiate|müzakere etmek
v|prefer|tercih etmek
v|include|dahil etmek
v|neglect|ihmal etmek
v|underestimate|hafife almak
v|overestimate|fazla değer vermek
v|summarise|özetlemek
v|represent|temsil etmek
p|put forward|öne sürmek
p|back up|desteklemek; yedeklemek
p|stand out|öne çıkmak
p|fall through|suya düşmek
p|catch up on|telafi etmek
a|foreseeable|öngörülebilir
a|controversial|tartışmalı
a|objective|nesnel
a|temporary|geçici
d|explicitly|açıkça
d|consequently|sonuç olarak
d|meanwhile|bu arada
v|admit|itiraf etmek, kabul etmek
v|advocate|savunmak, desteklemek
v|afford|(maddi olarak) gücü yetmek
v|boost|artırmak, yükseltmek
v|commit|taahhüt etmek, adamak
v|conduct|yürütmek, icra etmek
v|confirm|doğrulamak, teyit etmek
v|demonstrate|göstermek, kanıtlamak
v|deny|inkâr etmek, reddetmek
v|eliminate|ortadan kaldırmak, elemek
v|embrace|benimsemek, kucaklamak
v|encounter|karşılaşmak
v|engage|meşgul etmek, katılmak
v|establish|kurmak, tesis etmek
v|exhibit|sergilemek, göstermek
v|foster|teşvik etmek, beslemek
v|generate|üretmek, oluşturmak
v|highlight|öne çıkarmak, vurgulamak
v|identify|tespit etmek, tanımlamak
v|implement|hayata geçirmek, uygulamak
v|indicate|göstermek, belirtmek
v|investigate|soruşturmak, araştırmak
v|involve|içermek, dahil etmek
v|monitor|izlemek, takip etmek
v|obtain|elde etmek
v|occur|meydana gelmek
v|preserve|korumak, muhafaza etmek
v|proceed|devam etmek, ilerlemek
v|qualify|hak kazanmak, nitelendirmek
v|recall|hatırlamak, geri çağırmak
v|reflect|yansıtmak, düşünüp taşınmak
v|regard|saymak, addetmek
v|rely|güvenmek, dayanmak
v|restore|eski hâline getirmek
v|retain|elde tutmak, korumak
v|reveal|ortaya çıkarmak, açığa vurmak
v|reverse|tersine çevirmek
v|settle|yerleşmek, çözüme kavuşturmak
v|substitute|yerine koymak
v|suffer|acı çekmek, maruz kalmak
v|tend|eğiliminde olmak
v|urge|ısrarla teşvik etmek
v|vary|değişkenlik göstermek
v|witness|tanık olmak
v|yield|vermek (sonuç), boyun eğmek
n|accuracy|doğruluk, isabet
n|aspect|yön, boyut
n|awareness|farkındalık
n|barrier|engel
n|burden|yük, külfet
n|consensus|uzlaşı
n|controversy|tartışma, ihtilaf
n|conviction|inanç, mahkûmiyet
n|efficiency|verimlilik
n|emphasis|vurgu
n|exposure|maruz kalma, görünürlük
n|framework|çerçeve
n|initiative|girişim, inisiyatif
n|insight|içgörü
n|intent|niyet
n|liability|sorumluluk, yükümlülük
n|outcome|sonuç
n|pace|hız, tempo
n|pattern|örüntü, kalıp
n|perspective|bakış açısı
n|preference|tercih
n|priority|öncelik
n|proportion|oran
n|prospect|olasılık, ihtimal
n|resource|kaynak
n|significance|önem
n|stake|pay, risk edilen şey
n|strain|gerilim, zorlanma
n|transition|geçiş
n|trend|eğilim, trend
a|accessible|erişilebilir
a|accurate|doğru, isabetli
a|apparent|görünen, aşikâr
a|comprehensive|kapsamlı
a|consistent|tutarlı
a|crucial|çok önemli, kritik
a|demanding|zorlayıcı, çok şey isteyen
a|diverse|çeşitli, farklı
a|eligible|hak sahibi, uygun
a|excessive|aşırı
a|extensive|geniş kapsamlı
a|fundamental|temel
a|innovative|yenilikçi
a|legitimate|meşru
a|mandatory|zorunlu
a|ongoing|süregelen
a|outstanding|üstün, ödenmemiş
a|precise|kesin, hassas
a|preliminary|ön, hazırlık niteliğinde
a|prominent|öne çıkan
a|remarkable|kayda değer
a|subsequent|sonraki
a|substantial|hatırı sayılır, esaslı
a|vulnerable|savunmasız, kırılgan
a|widespread|yaygın
d|ultimately|nihayetinde
p|account for|açıklamak, -in nedeni olmak
p|bring up|gündeme getirmek, yetiştirmek
p|call off|iptal etmek
p|cut back on|kısmak, azaltmak
p|cut off|kesmek, bağlantıyı koparmak
p|follow up|takip etmek, peşini bırakmamak
p|hold back|geri tutmak, çekinmek
p|hold on|beklemek, tutunmak
p|given that|-diği göz önüne alınırsa
d|hence|dolayısıyla
p|in light of|-ışığında
p|in the long run|uzun vadede
p|on the whole|genel olarak
d|whereas|oysa ki, buna karşın
p|with a view to|-mek amacıyla
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
n|incentive|teşvik
n|intervention|müdahale
n|achievement|başarı, kazanım
n|gap|açık, fark
n|principle|ilke
n|accountability|hesap verebilirlik
n|reservation|çekince; rezervasyon
n|imposition|haksız yük
v|initiate|başlatmak
v|grant|tanımak, vermek
v|contest|itiraz etmek
v|reaffirm|yeniden teyit etmek
v|exhaust|tüketmek
v|perceive|algılamak
v|illustrate|örneklemek
v|clarify|netleştirmek
p|shed light on|aydınlatmak
p|put into perspective|doğru bakış açısına oturtmak
p|be reflected in|-e yansımak
p|take for granted|hazır kabul etmek
p|live up to|(beklentiyi) karşılamak
a|far-fetched|zorlama, saçma
a|invalid|geçersiz
a|coherent|tutarlı
a|indispensable|vazgeçilmez
d|in view of|karşısında
d|nonetheless|buna rağmen
d|as a result|sonuç olarak
d|demonstrably|kanıtlanabilir şekilde
v|abandon|terk etmek, vazgeçmek
v|accomplish|başarmak, tamamlamak
v|adjust|ayarlamak, uyarlamak
v|alter|değiştirmek
v|anticipate|önceden tahmin etmek, beklemek
v|approve|onaylamak
v|assign|atamak, görevlendirmek
v|assure|temin etmek, güvence vermek
v|attain|elde etmek, ulaşmak
v|attribute|atfetmek, bağlamak
v|cease|son vermek, kesilmek
v|compensate|telafi etmek, tazmin etmek
v|comply|uymak, riayet etmek
v|comprise|kapsamak, oluşmak
v|confront|yüzleşmek, karşı karşıya gelmek
v|consist|-den oluşmak
v|constitute|oluşturmak, teşkil etmek
v|consult|danışmak
v|convey|iletmek, aktarmak
v|cope|başa çıkmak
v|curb|dizginlemek, sınırlamak
v|delegate|yetki devretmek
v|deploy|konuşlandırmak, devreye almak
v|disclose|ifşa etmek, açıklamak
v|dismiss|reddetmek, işten çıkarmak
v|elaborate|ayrıntılandırmak
v|endure|dayanmak, katlanmak
v|enforce|uygulamak, zorla yürürlüğe koymak
v|enhance|geliştirmek, iyileştirmek
v|evolve|evrilmek, gelişmek
v|exceed|aşmak, geçmek
v|exclude|dışlamak, hariç tutmak
v|exploit|sömürmek, istismar etmek
v|expose|maruz bırakmak, ifşa etmek
v|facilitate|kolaylaştırmak
v|govern|yönetmek, belirlemek
v|hesitate|tereddüt etmek
v|incorporate|dahil etmek, bünyesine katmak
v|insist|ısrar etmek
v|inspire|ilham vermek
v|integrate|entegre etmek, bütünleştirmek
v|interfere|müdahale etmek, karışmak
v|interpret|yorumlamak
v|intervene|araya girmek, müdahale etmek
v|manipulate|manipüle etmek, yönlendirmek
v|modify|değiştirmek, uyarlamak
v|outline|ana hatlarıyla belirtmek
v|persuade|ikna etmek
v|portray|tasvir etmek, canlandırmak
v|reckon|sanmak, hesap etmek
v|recruit|işe almak
v|refrain|kaçınmak, geri durmak
v|reinforce|pekiştirmek, güçlendirmek
v|relieve|rahatlatmak, hafifletmek
v|remark|belirtmek, yorum yapmak
v|render|hâle getirmek, sunmak
v|resemble|benzemek
v|restrict|kısıtlamak
v|retrieve|geri almak, geri getirmek
v|specify|belirtmek, açıkça saptamak
v|strengthen|güçlendirmek
v|supplement|takviye etmek, eklemek
v|suppress|bastırmak
v|sustain|sürdürmek, ayakta tutmak
v|tailor|özel olarak uyarlamak
v|terminate|sonlandırmak
v|transform|dönüştürmek
v|undergo|geçirmek, maruz kalmak
v|undertake|üstlenmek|undertook · undertaken
v|verify|doğrulamak
v|withdraw|geri çekmek, çekilmek
v|withstand|dayanmak, karşı koymak
n|aftermath|sonrasında yaşananlar
n|backlash|sert tepki
n|benchmark|kıyas ölçütü
n|breakthrough|çığır açan gelişme
n|circumstance|koşul, durum
n|credibility|güvenilirlik
n|disruption|kesinti, altüst oluş
n|expertise|uzmanlık
n|flaw|kusur
n|interference|müdahale, karışma
n|leverage|kaldıraç gücü, nüfuz
n|likelihood|olasılık
n|magnitude|büyüklük, çap
n|milestone|dönüm noktası
n|momentum|ivme
n|motive|güdü, saik
n|obligation|yükümlülük
n|obstacle|engel
n|outlook|görünüm, bakış açısı
n|oversight|gözetim, gözden kaçırma
n|precedent|emsal
n|premise|öncül, dayanak
n|prevalence|yaygınlık
n|reasoning|akıl yürütme
n|remainder|geri kalan
n|scrutiny|yakın inceleme
n|standpoint|bakış açısı
n|surplus|fazlalık, artı değer
n|threshold|eşik
n|trait|özellik, karakter özelliği
n|transparency|şeffaflık
n|turnover|devir hızı, ciro
n|uncertainty|belirsizlik
n|validity|geçerlilik
a|abundant|bol, bereketli
a|adequate|yeterli
a|adverse|olumsuz, ters
a|arbitrary|keyfi
a|beneficial|faydalı
a|biased|önyargılı, taraflı
a|competent|yetkin
a|convincing|inandırıcı
a|evident|besbelli
a|explicit|açık, sarih
a|feasible|yapılabilir
a|flawed|kusurlu
a|imminent|çok yakın, an meselesi
a|inadequate|yetersiz
a|inclusive|kapsayıcı
a|inconsistent|tutarsız
a|influential|etkili, nüfuzlu
a|inherent|doğasında olan
a|intriguing|merak uyandıran
a|irrelevant|konu dışı, ilgisiz
a|marginal|marjinal, sınırda
a|misleading|yanıltıcı
a|notable|dikkate değer
a|noticeable|fark edilir
a|outdated|güncelliğini yitirmiş
a|overwhelming|ezici, bunaltıcı
a|persistent|inatçı, kalıcı
a|plausible|makul, inandırıcı
a|prevalent|yaygın
a|proportional|orantılı
a|questionable|kuşkulu
a|rigorous|titiz, sıkı
a|robust|sağlam, güçlü
a|scarce|kıt
a|straightforward|dolaysız, anlaşılır
a|susceptible|duyarlı, açık (etkiye)
a|unanimous|oybirliğiyle
a|unprecedented|eşi görülmemiş
a|versatile|çok yönlü
a|viable|uygulanabilir
d|deliberately|kasten
d|inevitably|kaçınılmaz olarak
d|notably|özellikle, dikkat çekici biçimde
d|predominantly|ağırlıklı olarak
d|substantially|önemli ölçüde
a|thereby|böylece
p|drop out|bırakmak, ayrılmak
p|fall behind|geri kalmak
p|pass on|aktarmak, devretmek
p|pick up on|fark etmek, yakalamak
p|step down|görevden çekilmek
d|albeit|her ne kadar öyle olsa da
p|all things considered|her şey göz önüne alındığında
p|as a matter of fact|aslına bakılırsa
p|in respect of|-e ilişkin
p|it goes without saying|söylemeye gerek yok ki
p|let alone|bırakın -i, şöyle dursun
p|provided that|şu şartla ki
p|subject to|-e tabi olarak
p|take into account|hesaba katmak
p|to put it simply|basitçe söylemek gerekirse
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
n|remedy|çare
n|occasion|vesile
n|apprehension|endişe
n|downside|olumsuz taraf
n|imbalance|dengesizlik
n|leniency|hoşgörü
n|omission|ihmal, atlama
n|restraint|ölçülülük
v|heed|dikkate almak
v|condone|göz yummak
v|forfeit|kaybetmek
v|deem|addetmek
v|fathom|kavramak
v|evoke|uyandırmak
v|endorse|onaylamak, desteklemek
v|withhold|esirgemek|withheld · withheld
v|enshrine|güvence altına almak
p|come to a head|doruğa çıkmak, kızışmak
p|make sure|emin olmak
p|build on|üzerine inşa etmek
p|go along with|kabul etmek, uymak
a|undisputed|tartışmasız
a|deliberate|kasıtlı
d|at times|zaman zaman
d|henceforth|bundan böyle
d|primarily|öncelikle
d|occasionally|ara sıra
v|accumulate|birikmek, biriktirmek
v|alleviate|hafifletmek, azaltmak
v|allocate|tahsis etmek, ayırmak
v|amend|düzeltmek, tadil etmek
v|broaden|genişletmek
v|collaborate|iş birliği yapmak
v|compel|zorlamak, mecbur bırakmak
v|compile|derlemek
v|concede|kabullenmek, taviz vermek
v|correspond|karşılık gelmek, yazışmak
v|cultivate|geliştirmek, yetiştirmek
v|dedicate|adamak, tahsis etmek
v|defer|ertelemek
v|denote|belirtmek, işaret etmek
v|depict|betimlemek, tasvir etmek
v|derive|türetmek, elde etmek
v|deter|caydırmak
v|devise|tasarlamak, kurgulamak
v|diminish|azalmak, küçültmek
v|discourage|caydırmak, cesaretini kırmak
v|displace|yerinden etmek
v|dispose|elden çıkarmak, bertaraf etmek
v|disrupt|kesintiye uğratmak, bozmak
v|diverge|ayrılmak, sapmak
v|entail|gerektirmek, beraberinde getirmek
v|exaggerate|abartmak
v|exert|(çaba/baskı) uygulamak
v|fulfil|yerine getirmek, karşılamak
v|hinder|engellemek
v|impair|zayıflatmak, bozmak
v|incline|eğilim göstermek
v|induce|yol açmak, teşvik etmek
v|inhibit|engellemek, ketlemek
v|mitigate|hafifletmek, azaltmak
v|oversee|denetlemek, gözetmek
v|overlook|gözden kaçırmak, göz yummak
v|persist|ısrar etmek, sürüp gitmek
v|pinpoint|tam olarak belirlemek
v|prevail|hüküm sürmek, galip gelmek
v|prioritise|önceliklendirmek
v|prohibit|yasaklamak
v|quantify|nicelleştirmek, sayısallaştırmak
v|reassure|güven vermek, içini rahatlatmak
v|refine|inceltmek, iyileştirmek
v|revise|gözden geçirmek, revize etmek
v|simplify|basitleştirmek
v|supervise|denetlemek
v|unveil|tanıtmak, perdeyi kaldırmak
v|uphold|desteklemek, sürdürmek (ilke)
v|utilise|kullanmak, yararlanmak
v|validate|doğrulamak, geçerli kılmak
v|weaken|zayıflatmak
n|adversity|zorluk, sıkıntı
n|ambiguity|belirsizlik, muğlaklık
n|constraint|kısıt
n|contradiction|çelişki
n|criterion|ölçüt
n|discrepancy|tutarsızlık, uyuşmazlık
n|disparity|eşitsizlik, fark
n|drawback|dezavantaj
n|endeavour|çaba, girişim
n|feasibility|yapılabilirlik
n|hindrance|engel
n|implication|çıkarım, doğuracağı sonuç
n|inconsistency|tutarsızlık
n|misconception|yanlış kanı
n|nuance|nüans, ince ayrım
n|persistence|azim, süreklilik
n|plausibility|inandırıcılık
n|proficiency|yetkinlik
n|rationale|gerekçe, mantık
n|reluctance|isteksizlik
n|resilience|dayanıklılık, direnç
n|setback|aksilik, geri adım
n|shortcoming|eksiklik
n|urgency|aciliyet
n|viability|yaşayabilirlik, uygulanabilirlik
a|ambiguous|belirsiz, çift anlamlı
a|conclusive|kesin, belirleyici
a|conspicuous|göze çarpan
a|cumbersome|hantal, kullanışsız
a|detrimental|zararlı
a|eminent|seçkin, önde gelen
a|exhaustive|çok kapsamlı, eksiksiz
a|fluctuating|dalgalanan
a|intricate|karmaşık, ince işlenmiş
a|negligible|ihmal edilebilir
a|pervasive|her yere yayılmış
a|predominant|baskın
a|redundant|gereksiz, fazlalık
a|resilient|dirençli
a|unbiased|tarafsız
p|draw on|-den yararlanmak
p|lay off|işten çıkarmak
p|narrow down|daraltmak, elemek
p|opt for|-i tercih etmek
p|phase out|kademeli olarak kaldırmak
p|stick to|bağlı kalmak
p|sum up|özetlemek
p|as far as I'm concerned|bana kalırsa
p|at the expense of|-in pahasına
p|contrary to|-in aksine
p|for the sake of|-in hatırına, uğruna
p|in the wake of|-in ardından
p|insofar as|-diği ölçüde
p|on the grounds that|-gerekçesiyle
p|regardless of|-e bakılmaksızın
p|to a certain extent|bir dereceye kadar
p|with regard to|-e ilişkin
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
n|ambivalence|ikircik
n|anachronism|anakronizm
n|composure|soğukkanlılık
n|disdain|küçümseme
n|pipe dream|hayal ürünü
n|complacency|rehavet
n|fallacy|safsata, yanılgı
n|integrity|dürüstlük
v|appease|yatıştırmak
v|stigmatise|damgalamak
v|evade|kaçmak, kaçınmak
v|erode|aşınmak
v|conceal|gizlemek
v|co-opt|kendine mal etmek
v|impose|dayatmak
p|wear down|yıpratmak
p|get out of hand|kontrolden çıkmak
p|come to terms with|kabullenmek
p|be at odds with|çelişmek
a|meticulous|titiz
a|flimsy|inandırıcı olmayan
a|outrageous|akıl almaz
a|latent|gizli
a|perfidious|hain
a|subtle|ince
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
 'unctuous': 'salbungsvoll'}

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
