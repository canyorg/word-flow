# -*- coding: utf-8 -*-
"""English word lists.

DAILY    : A1.1–C2.2 — foundation built from the same 1500 core concepts as the
           German list, plus phrasal verbs and idioms in the upper levels
ACADEMIC : B1.1–C2.2 — vocabulary for papers, theses and talks
Lines: "type|English|Turkish|hint"
         type: n = noun, v = verb, a = adjective, d = adverb / linker,
               p = phrase / phrasal verb, w = other word
EN_DE / EN_DE_ACADEMIC : English -> German meaning (academic overrides daily)
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
 'eccentric': 'exzentrisch, verschroben'}

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
 'viz.': 'nämlich'}
