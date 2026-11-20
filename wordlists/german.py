# -*- coding: utf-8 -*-
"""German word lists.

GERMAN          : general, A1.1–C2.2 — 1500 core words + 500-verb list (A1–B1),
                  C1 vocabulary mirrored from the English C1 list, advanced words
                  and idioms up to C2.2
GERMAN_ACADEMIC : B1.1–C2.2 — academic German (mirrors the English academic list)
GERMAN_CYBER    : B1.1–C2.2 — cybersecurity German (mirrors the English cyber list)
Lines: "type|German|Turkish|hint"   type: n noun, v verb, p phrase, w other word
DE_EN*          : German -> English meaning
"""

GERMAN = {
"A1.1": """
n|der Mann|adam
n|die Frau|kadın
n|das Kind|çocuk
n|der Name|isim, ad
n|das Haus|ev
n|die Wohnung|daire, ev
n|das Wasser|su
n|das Brot|ekmek
n|der Kaffee|kahve
n|der Tag|gün
n|die Woche|hafta
n|die Stadt|şehir
n|das Land|ülke
n|die Sprache|dil
n|der Freund|arkadaş (erkek)
n|die Familie|aile
n|die Mutter|anne
n|der Vater|baba
v|sein|olmak|er ist · ist gewesen
v|haben|sahip olmak, -si olmak|er hat · hat gehabt
v|heißen|adı ... olmak|er heißt · hat geheißen
v|kommen|gelmek|er kommt · ist gekommen
v|wohnen|oturmak, ikamet etmek|er wohnt · hat gewohnt
v|sprechen|konuşmak|er spricht · hat gesprochen
v|trinken|içmek|er trinkt · hat getrunken
v|essen|yemek yemek|er isst · hat gegessen
v|lernen|öğrenmek|er lernt · hat gelernt
v|machen|yapmak|er macht · hat gemacht
w|gut|iyi
w|groß|büyük
w|klein|küçük
w|heute|bugün
w|hallo|merhaba
p|guten Morgen|günaydın
p|guten Tag|iyi günler
p|guten Abend|iyi akşamlar
p|gute Nacht|iyi geceler
w|tschüss|hoşça kal
p|auf Wiedersehen|güle güle / hoşça kalın
p|bis später|sonra görüşürüz
p|bis morgen|yarın görüşürüz
p|bis bald|yakında görüşürüz
w|ja|evet
w|nein|hayır
w|vielleicht|belki
w|bitte|lütfen / buyurun
w|danke|teşekkürler
p|danke schön|çok teşekkürler
p|gern geschehen|rica ederim
w|entschuldigung|affedersiniz / özür dilerim
p|es tut mir leid|üzgünüm
p|kein Problem|sorun değil
p|wie geht's?|nasılsın?
p|mir geht es gut|iyiyim
p|und dir?|ya sen?
w|willkommen|hoş geldin
p|herzlich willkommen|hoş geldiniz
p|mein Name ist ...|benim adım ...
p|ich heiße ...|benim adım ...
p|freut mich|memnun oldum
p|wie bitte?|efendim? / anlamadım
p|ich verstehe nicht|anlamıyorum
p|langsam bitte|yavaş lütfen
p|noch einmal|bir kez daha
w|natürlich|tabii ki
w|genau|aynen / tam olarak
w|stimmt|doğru
w|okay|tamam
p|in Ordnung|tamam / uygun
p|viel Glück|bol şans
p|viel Spaß|iyi eğlenceler
p|gute Reise|iyi yolculuklar
p|guten Appetit|afiyet olsun
w|prost|şerefe
p|herzlichen Glückwunsch|tebrikler
p|alles Gute|her şey gönlünce olsun
p|gute Besserung|geçmiş olsun
p|schönes Wochenende|iyi hafta sonları
p|bitte schön|buyurun
w|Verzeihung|pardon
w|Achtung|dikkat
w|Hilfe!|imdat!
w|null|sıfır
w|eins|bir
w|zwei|iki
w|drei|üç
w|vier|dört
w|fünf|beş
w|sechs|altı
w|sieben|yedi
w|acht|sekiz
w|neun|dokuz
w|zehn|on
w|elf|on bir
w|zwölf|on iki
w|dreizehn|on üç
w|vierzehn|on dört
w|fünfzehn|on beş
w|sechzehn|on altı
w|siebzehn|on yedi
w|achtzehn|on sekiz
w|neunzehn|on dokuz
w|zwanzig|yirmi
w|dreißig|otuz
w|vierzig|kırk
w|fünfzig|elli
w|sechzig|altmış
w|siebzig|yetmiş
w|achtzig|seksen
w|neunzig|doksan
w|hundert|yüz
w|tausend|bin
n|die Million|milyon
w|erste|birinci
w|zweite|ikinci
w|dritte|üçüncü
w|letzte|sonuncu
w|halb|yarım
n|die Hälfte|yarısı
n|das Viertel|çeyrek
n|das Paar|çift
n|das Dutzend|düzine
w|viel|çok
w|wenig|az
w|mehr|daha fazla
w|weniger|daha az
w|genug|yeterli
w|alle|hepsi
w|nichts|hiçbir şey
w|etwas|bir şey / biraz
n|die Zahl|sayı
n|die Nummer|numara
n|das Prozent|yüzde
n|das Stück|adet / parça
n|das Kilo|kilo
n|das Gramm|gram
n|der Liter|litre
n|die Farbe|renk
w|rot|kırmızı
w|blau|mavi
w|gelb|sarı
w|grün|yeşil
w|schwarz|siyah
w|weiß|beyaz
w|grau|gri
w|braun|kahverengi
w|orange|turuncu
w|rosa|pembe
w|lila|mor
w|bunt|rengarenk
w|hell|açık (renk) / aydınlık
w|dunkel|koyu / karanlık
n|der Kreis|daire
n|das Quadrat|kare
n|die Linie|çizgi
w|rund|yuvarlak
w|ich|ben
w|du|sen
w|er|o (erkek)
w|sie|o (kadın) / onlar
w|es|o (nötr)
w|wir|biz
w|ihr|siz
w|mein|benim
w|dein|senin
w|unser|bizim
w|euer|sizin
w|mich|beni
w|dich|seni
w|mir|bana
w|dir|sana
w|man|(genel özne) insan
w|der|(eril artikel)
w|die|(dişil artikel)
w|das|(nötr artikel)
w|ein|bir (eril/nötr)
w|eine|bir (dişil)
w|kein|hiçbir / yok
w|dieser|bu
w|jener|şu / o
w|jeder|her biri
w|einige|bazıları
w|andere|diğerleri
w|selbst|kendi
w|und|ve
w|oder|veya
w|aber|ama
w|denn|çünkü
w|weil|çünkü / -dığı için
w|dass|ki / -dığını
w|wenn|eğer / -dığında
w|als|-iken / -den (karşılaştırma)
w|ob|-ip -mediğini
w|obwohl|-mesine rağmen
w|damit|ki (amaç)
w|also|yani / öyleyse
w|sondern|aksine / bilakis
p|sowohl ... als auch|hem ... hem de
p|entweder ... oder|ya ... ya da
p|weder ... noch|ne ... ne de
w|in|içinde
w|an|-de / kenarında
w|auf|üstünde
w|unter|altında
w|über|üzerinde / hakkında
w|vor|önünde / önce
w|hinter|arkasında
w|neben|yanında
w|zwischen|arasında
w|bei|yanında / -de
w|mit|ile
w|ohne|-siz / olmadan
w|für|için
w|gegen|karşı
w|von|-den / -in
w|zu|-e / -a
w|nach|-den sonra / -e doğru
w|aus|-den (içinden)
w|seit|-den beri
w|bis|-e kadar
w|durch|içinden / vasıtasıyla
w|um|etrafında / saat -de
w|während|sırasında
w|wegen|yüzünden
w|statt|yerine
w|außer|hariç
w|gegenüber|karşısında
w|wer|kim
w|was|ne
w|wo|nerede
w|wohin|nereye
w|woher|nereden
w|wann|ne zaman
w|wie|nasıl
w|warum|neden
w|wieso|niçin
w|weshalb|niçin
w|welcher|hangi
p|wie viel|ne kadar
p|wie viele|kaç tane
p|wie lange|ne kadar süre
p|wie oft|ne sıklıkta
p|wie weit|ne kadar uzak
w|wem|kime
w|wen|kimi
w|wessen|kimin
n|die Frage|soru
n|die Zeit|zaman
n|die Stunde|saat (süre)
n|die Minute|dakika
n|die Sekunde|saniye
n|der Monat|ay
n|das Jahr|yıl
n|der Morgen|sabah
n|der Vormittag|öğleden önce
n|der Mittag|öğle
n|der Nachmittag|öğleden sonra
n|der Abend|akşam
n|die Nacht|gece
w|gestern|dün
w|übermorgen|öbür gün
w|vorgestern|evvelki gün
w|jetzt|şimdi
w|gleich|hemen / birazdan
w|sofort|derhal
w|später|sonra
w|früher|daha önce
w|bald|yakında
w|gerade|tam şu an
w|nie|asla
w|manchmal|bazen
w|oft|sık sık
w|selten|nadiren
w|meistens|çoğunlukla
w|täglich|günlük
w|wöchentlich|haftalık
w|monatlich|aylık
w|jährlich|yıllık
n|der Montag|Pazartesi
n|der Dienstag|Salı
n|der Mittwoch|Çarşamba
n|der Donnerstag|Perşembe
n|der Freitag|Cuma
n|der Samstag|Cumartesi
n|der Sonntag|Pazar
n|das Wochenende|hafta sonu
n|der Werktag|iş günü
n|der Feiertag|resmi tatil
n|der Januar|Ocak
n|der Februar|Şubat
n|der März|Mart
n|der April|Nisan
n|der Mai|Mayıs
n|der Juni|Haziran
n|der Juli|Temmuz
n|der August|Ağustos
n|der September|Eylül
n|der Oktober|Ekim
n|der November|Kasım
n|der Dezember|Aralık
n|der Frühling|ilkbahar
n|der Sommer|yaz
n|der Herbst|sonbahar
n|der Winter|kış
n|die Jahreszeit|mevsim
n|das Datum|tarih
n|der Kalender|takvim
n|die Vergangenheit|geçmiş
n|die Gegenwart|şimdiki zaman
n|die Zukunft|gelecek
n|der Geburtstag|doğum günü
n|die Verspätung|gecikme
n|der Mensch|insan
n|die Leute|insanlar
n|die Person|kişi
n|der Junge|erkek çocuk
n|das Mädchen|kız çocuk
n|das Baby|bebek
n|die Eltern|ebeveynler
n|der Sohn|oğul
n|die Tochter|kız evlat
n|der Bruder|erkek kardeş
n|die Schwester|kız kardeş
n|die Geschwister|kardeşler
n|die Großeltern|büyükanne ve büyükbaba
n|der Großvater|dede
n|die Großmutter|büyükanne
n|der Opa|dede (samimi)
n|die Oma|nine (samimi)
n|der Enkel|torun
n|der Onkel|amca / dayı
n|die Tante|teyze / hala
n|der Cousin|kuzen (erkek)
n|die Cousine|kuzen (kız)
n|der Neffe|yeğen (erkek)
n|die Nichte|yeğen (kız)
n|der Schwiegervater|kayınpeder
n|die Schwiegermutter|kaynana
n|der Ehemann|koca
n|die Ehefrau|eş / karı
n|der Partner|partner
n|die Freundin|kız arkadaş
n|der Gast|misafir
n|der Erwachsene|yetişkin
n|der Jugendliche|genç
n|der Vorname|ad
n|der Nachname|soyadı
n|das Alter|yaş
n|die Hochzeit|düğün
n|die Ehe|evlilik
n|die Liebe|aşk / sevgi
n|die Freundschaft|arkadaşlık
w|ledig|bekâr
w|verheiratet|evli
w|geschieden|boşanmış
w|schwanger|hamile
w|verwandt|akraba
""",
"A1.2": """
n|der Bahnhof|tren istasyonu
n|der Bus|otobüs
n|die Straße|cadde, sokak
n|das Zimmer|oda
n|die Küche|mutfak
n|der Tisch|masa
n|der Stuhl|sandalye
n|das Bett|yatak
n|die Uhr|saat
n|das Geld|para
n|der Preis|fiyat
n|der Supermarkt|süpermarket
n|das Obst|meyve
n|das Gemüse|sebze
n|die Milch|süt
n|der Arzt|doktor
v|gehen|gitmek, yürümek|er geht · ist gegangen
v|fahren|(araçla) gitmek|er fährt · ist gefahren
v|kaufen|satın almak|er kauft · hat gekauft
v|kosten|(fiyatı) tutmak|es kostet · hat gekostet
v|brauchen|ihtiyacı olmak|er braucht · hat gebraucht
v|möchten|istemek (kibar)|ich möchte · er möchte
v|nehmen|almak|er nimmt · hat genommen
v|schlafen|uyumak|er schläft · hat geschlafen
v|arbeiten|çalışmak|er arbeitet · hat gearbeitet
v|spielen|oynamak|er spielt · hat gespielt
v|lesen|okumak|er liest · hat gelesen
v|schreiben|yazmak|er schreibt · hat geschrieben
w|teuer|pahalı
w|billig|ucuz
w|morgen|yarın
w|immer|her zaman
n|der Körper|vücut
n|das Haar|saç
n|das Gesicht|yüz
n|das Auge|göz
n|die Nase|burun
n|der Mund|ağız
n|das Ohr|kulak
n|der Zahn|diş
n|der Hals|boyun / boğaz
n|der Arm|kol
n|die Hand|el
n|der Finger|parmak
n|der Rücken|sırt
n|das Bein|bacak
n|das Knie|diz
n|der Fuß|ayak
n|die Haut|cilt
n|das Herz|kalp
n|das Blut|kan
n|die Krankheit|hastalık
w|gesund|sağlıklı
n|die Schmerzen|ağrılar
n|die Kopfschmerzen|baş ağrısı
n|das Fieber|ateş
n|der Husten|öksürük
n|die Grippe|grip
n|die Allergie|alerji
n|die Wunde|yara
n|der Unfall|kaza
n|die Ärztin|doktor (kadın)
n|der Zahnarzt|diş hekimi
n|das Krankenhaus|hastane
n|die Praxis|muayenehane
n|das Medikament|ilaç
n|die Tablette|hap
n|das Rezept|reçete
n|die Untersuchung|muayene
n|die Krankenkasse|sağlık sigortası
n|die Versichertenkarte|sigorta kartı
n|die Notaufnahme|acil servis
n|der Krankenwagen|ambulans
n|die Behandlung|tedavi
w|schwach|zayıf / güçsüz
w|stark|güçlü
n|die Brille|gözlük
v|sich ausruhen|dinlenmek
v|weh tun|acıtmak
v|sich fühlen|hissetmek
v|atmen|nefes almak
v|heilen|iyileşmek
n|das Wohnzimmer|oturma odası
n|das Schlafzimmer|yatak odası
n|das Badezimmer|banyo
n|die Toilette|tuvalet
n|der Flur|koridor
n|der Balkon|balkon
n|der Garten|bahçe
n|der Keller|bodrum
n|die Tür|kapı
n|das Fenster|pencere
n|die Wand|duvar
n|der Boden|zemin
n|die Decke|tavan / battaniye
n|das Dach|çatı
n|die Treppe|merdiven
n|der Aufzug|asansör
n|das Schloss|kilit / şato
n|die Möbel|mobilya
n|der Sessel|koltuk
n|das Sofa|kanepe
n|der Schrank|dolap
n|das Regal|raf
n|die Lampe|lamba
n|das Licht|ışık
n|der Teppich|halı
n|der Spiegel|ayna
n|das Bild|resim / tablo
n|das Handtuch|havlu
n|die Seife|sabun
n|die Zahnbürste|diş fırçası
n|die Zahnpasta|diş macunu
n|das Shampoo|şampuan
n|die Dusche|duş
n|das Waschbecken|lavabo
n|die Waschmaschine|çamaşır makinesi
n|der Kühlschrank|buzdolabı
n|der Herd|ocak
n|der Backofen|fırın
n|die Spülmaschine|bulaşık makinesi
n|die Heizung|kalorifer
n|die Klimaanlage|klima
n|der Mülleimer|çöp kovası
n|die Steckdose|priz
n|der Stecker|fiş
n|der Mieter|kiracı
n|der Vermieter|ev sahibi
n|die Nebenkosten|yan giderler
n|die Kaution|depozito
n|der Mietvertrag|kira sözleşmesi
n|der Hausmeister|apartman görevlisi
n|die Adresse|adres
n|die Hausnummer|kapı numarası
n|die Postleitzahl|posta kodu
n|das Stockwerk|kat
n|das Erdgeschoss|zemin kat
n|der Umzug|taşınma
n|die Hausarbeit|ev işi
v|putzen|temizlemek
v|aufräumen|toplamak / düzenlemek
v|waschen|yıkamak
v|kochen|yemek pişirmek
v|mieten|kiralamak
w|gemütlich|rahat / sıcak (ortam)
w|sauber|temiz
w|schmutzig|kirli
n|das Essen|yemek
n|das Getränk|içecek
n|das Frühstück|kahvaltı
n|das Mittagessen|öğle yemeği
n|das Abendessen|akşam yemeği
n|der Hunger|açlık
n|der Durst|susuzluk
w|hungrig|aç
w|durstig|susuz
n|das Brötchen|küçük ekmek
n|die Butter|tereyağı
n|der Käse|peynir
n|das Ei|yumurta
n|der Joghurt|yoğurt
n|die Sahne|krema
n|das Fleisch|et
n|das Rindfleisch|dana eti
n|das Hähnchen|tavuk
n|das Schweinefleisch|domuz eti
n|die Wurst|sosis / sucuk
n|der Schinken|jambon
n|der Fisch|balık
n|die Suppe|çorba
n|der Salat|salata
n|die Kartoffel|patates
n|die Tomate|domates
n|die Gurke|salatalık
n|die Zwiebel|soğan
n|der Knoblauch|sarımsak
n|die Karotte|havuç
n|der Pfeffer|biber (baharat)
n|die Paprika|biber
n|der Reis|pirinç
n|die Nudeln|makarna
n|das Mehl|un
n|der Zucker|şeker
n|das Salz|tuz
n|das Öl|yağ
n|der Apfel|elma
n|die Banane|muz
n|die Orange|portakal
n|die Zitrone|limon
n|die Erdbeere|çilek
n|der Kuchen|kek / pasta
n|die Schokolade|çikolata
n|das Eis|dondurma / buz
n|der Honig|bal
n|die Marmelade|reçel
n|der Tee|çay
n|der Saft|meyve suyu
n|das Bier|bira
n|der Wein|şarap
n|die Limonade|gazoz
n|die Flasche|şişe
n|das Glas|bardak / cam
n|die Tasse|fincan
n|der Teller|tabak
n|die Gabel|çatal
n|das Messer|bıçak
n|der Löffel|kaşık
n|der Topf|tencere
n|die Pfanne|tava
n|das Restaurant|restoran
n|das Café|kafe
n|die Speisekarte|menü
n|das Trinkgeld|bahşiş
n|der Kellner|garson
n|die Bestellung|sipariş
n|die Vorspeise|başlangıç
n|das Hauptgericht|ana yemek
n|die Nachspeise|tatlı
n|die Zutat|malzeme
w|lecker|lezzetli
w|süß|tatlı
w|salzig|tuzlu
w|sauer|ekşi
w|scharf|acı / keskin
w|frisch|taze
w|gekocht|pişmiş / haşlanmış
v|backen|fırında pişirmek
v|braten|kızartmak
v|schneiden|kesmek
v|probieren|denemek / tatmak
v|bestellen|sipariş vermek
w|satt|tok
w|vegetarisch|vejetaryen
n|die Kleidung|giysi
n|das Hemd|gömlek
n|das T-Shirt|tişört
n|der Pullover|kazak
n|die Jacke|ceket / mont
n|der Mantel|palto
n|die Hose|pantolon
n|die Jeans|kot pantolon
n|der Rock|etek
n|das Kleid|elbise
n|die Socke|çorap
n|die Unterwäsche|iç çamaşırı
n|der Schuh|ayakkabı
n|der Hut|şapka
n|die Mütze|bere
n|der Schal|atkı
n|der Gürtel|kemer
n|die Tasche|çanta
n|der Rucksack|sırt çantası
n|der Regenschirm|şemsiye
n|der Schmuck|takı
n|die Größe|beden / boyut
v|anziehen|giymek
v|ausziehen|çıkarmak (giysi)
v|tragen|giymek / taşımak
v|anprobieren|denemek (giysi)
v|passen|uymak
v|stehen|yakışmak / durmak
w|eng|dar
w|weit|geniş / uzak
w|modisch|modaya uygun
w|bequem|rahat
n|die Umkleidekabine|deneme kabini
n|die Wäsche|çamaşır
n|die Marke|marka
n|die Mode|moda
n|die Sonnenbrille|güneş gözlüğü
""",
"A2.1": """
n|der Termin|randevu
n|die Rechnung|fatura, hesap
n|der Urlaub|tatil, izin
n|die Reise|seyahat
n|das Wetter|hava durumu
n|der Regen|yağmur
n|die Erkältung|soğuk algınlığı
n|der Kopf|baş, kafa
n|der Bauch|karın
n|die Apotheke|eczane
n|der Schlüssel|anahtar
n|die Miete|kira
n|der Nachbar|komşu
n|die Arbeit|iş
n|der Kollege|iş arkadaşı
v|anrufen|telefon etmek, aramak|er ruft an · hat angerufen
v|aufstehen|(yataktan) kalkmak|er steht auf · ist aufgestanden
v|einkaufen|alışveriş yapmak|er kauft ein · hat eingekauft
v|anfangen|başlamak|er fängt an · hat angefangen
v|aufhören|bırakmak, durmak|er hört auf · hat aufgehört
v|helfen|yardım etmek (+ Dativ)|er hilft · hat geholfen
v|warten|beklemek|er wartet · hat gewartet
v|bezahlen|ödemek|er bezahlt · hat bezahlt
v|vergessen|unutmak|er vergisst · hat vergessen
v|treffen|buluşmak, karşılaşmak|er trifft · hat getroffen
v|bleiben|kalmak|er bleibt · ist geblieben
v|wissen|bilmek|er weiß · hat gewusst
v|denken|düşünmek|er denkt · hat gedacht
w|müde|yorgun
w|krank|hasta
w|schnell|hızlı
w|leider|maalesef
n|das Dorf|köy
n|das Zentrum|merkez
n|die Innenstadt|şehir merkezi
n|der Platz|meydan / yer
n|der Park|park
n|die Brücke|köprü
n|der Fluss|nehir
n|das Gebäude|bina
n|die Kirche|kilise
n|die Moschee|cami
n|das Museum|müze
n|das Theater|tiyatro
n|das Kino|sinema
n|die Bibliothek|kütüphane
n|die Schule|okul
n|die Universität|üniversite
n|das Rathaus|belediye binası
n|die Post|postane
n|die Bank|banka
n|das Hotel|otel
n|das Geschäft|dükkân
n|der Laden|mağaza
n|die Bäckerei|fırın
n|die Metzgerei|kasap
n|der Markt|pazar
n|das Einkaufszentrum|alışveriş merkezi
n|die Tankstelle|benzin istasyonu
n|der Parkplatz|otopark
n|die Haltestelle|durak
n|der Flughafen|havalimanı
n|der Hafen|liman
n|das Stadion|stadyum
n|das Schwimmbad|yüzme havuzu
n|das Fitnessstudio|spor salonu
n|der Friseur|kuaför
n|die Polizei|polis
n|die Feuerwehr|itfaiye
n|der Zoo|hayvanat bahçesi
n|die Ecke|köşe
n|die Kreuzung|kavşak
n|die Ampel|trafik ışığı
n|der Gehweg|kaldırım
n|der Weg|yol / patika
n|die Richtung|yön
w|rechts|sağ
w|links|sol
w|geradeaus|dümdüz
w|oben|yukarıda
w|unten|aşağıda
w|vorne|önde
w|hinten|arkada
n|die Mitte|orta
n|die Seite|taraf / sayfa
w|nah|yakın
n|die Umgebung|çevre
n|der Ort|yer / mekân
n|die Gegend|bölge
n|die Grenze|sınır
n|die Hauptstadt|başkent
n|der Einwohner|sakin / oturan
n|die Sehenswürdigkeit|turistik yer
n|das Denkmal|anıt
n|der Turm|kule
n|die Aussicht|manzara
n|der Verkehr|trafik
n|das Auto|araba
n|die Bahn|tren / demiryolu
n|der Zug|tren
n|die S-Bahn|banliyö treni
n|die U-Bahn|metro
n|die Straßenbahn|tramvay
n|das Fahrrad|bisiklet
n|das Motorrad|motosiklet
n|das Taxi|taksi
n|das Flugzeug|uçak
n|das Schiff|gemi
n|der Führerschein|ehliyet
n|die Fahrkarte|bilet
n|das Ticket|bilet
n|der Fahrplan|tarife
n|das Gleis|peron / ray
n|der Ausgang|çıkış
n|der Eingang|giriş
n|die Abfahrt|kalkış
n|die Ankunft|varış
n|der Aufenthalt|konaklama / mola
n|die Verbindung|bağlantı
v|umsteigen|aktarma yapmak
v|einsteigen|binmek
v|aussteigen|inmek
v|fliegen|uçmak
v|laufen|yürümek / koşmak
p|zu Fuß|yaya olarak
n|die Autobahn|otoyol
n|die Geschwindigkeit|hız
n|das Benzin|benzin
n|der Motor|motor
n|das Rad|tekerlek
n|der Reifen|lastik
n|die Panne|arıza
n|die Strecke|güzergâh / mesafe
n|die Entfernung|mesafe
n|der Koffer|bavul
n|das Gepäck|bagaj
n|der Pass|pasaport
n|das Visum|vize
n|der Ausweis|kimlik
n|der Zoll|gümrük
n|die Buchung|rezervasyon
n|die Unterkunft|konaklama
n|die Jugendherberge|gençlik yurdu
n|das Zelt|çadır
n|die Ferien|tatil (okul)
n|der Ausflug|gezi
n|die Tour|tur
n|der Tourist|turist
n|die Karte|harita / kart
n|das Navi|navigasyon
n|der Stau|trafik sıkışıklığı
n|die Baustelle|şantiye / yol çalışması
v|besichtigen|gezmek / ziyaret etmek
v|reservieren|rezervasyon yapmak
v|packen|valiz hazırlamak
v|ankommen|varmak
v|abfahren|hareket etmek
v|verpassen|kaçırmak
n|die Sicherheit|güvenlik
n|der Euro|avro
n|der Cent|sent
n|die Kasse|kasa
n|die Quittung|fiş
n|der Kunde|müşteri
n|der Verkäufer|satıcı
n|der Einkauf|alışveriş
n|die Einkaufsliste|alışveriş listesi
n|der Einkaufswagen|alışveriş arabası
n|die Tüte|poşet
n|das Angebot|kampanya / teklif
n|der Rabatt|indirim
n|der Ausverkauf|büyük indirim
w|kostenlos|ücretsiz
w|günstig|uygun fiyatlı
n|das Bargeld|nakit
n|die Kreditkarte|kredi kartı
n|die EC-Karte|banka kartı
n|das Konto|hesap
n|die Überweisung|havale
n|die Bankleitzahl|banka kodu
n|die IBAN|IBAN
n|der Geldautomat|ATM
n|das Wechselgeld|para üstü
n|die Steuer|vergi
n|die Mehrwertsteuer|KDV
n|die Gebühr|ücret / harç
n|die Kosten|maliyet
n|das Einkommen|gelir
v|sparen|biriktirmek / tasarruf etmek
v|ausgeben|harcamak
v|verkaufen|satmak
v|umtauschen|değiştirmek (ürün)
v|zurückgeben|iade etmek
n|die Garantie|garanti
n|die Lieferung|teslimat
n|die Ware|ürün / mal
n|das Produkt|ürün
n|die Qualität|kalite
n|die Menge|miktar
n|die Auswahl|seçenek / çeşit
n|die Reklamation|şikâyet / iade talebi
n|die Rate|taksit
n|die Schulden|borç
v|werden|olmak; -ecek (gelecek zaman)
v|können|-ebilmek
v|müssen|zorunda olmak
v|wollen|istemek
w|sollen|-meli
v|dürfen|izni olmak
v|mögen|hoşlanmak
v|tun|yapmak / etmek
v|sagen|söylemek
v|reden|konuşmak / sohbet etmek
v|fragen|sormak
v|antworten|cevap vermek
v|sehen|görmek
v|schauen|bakmak
v|hören|duymak / dinlemek
v|zuhören|dinlemek
v|kennen|tanımak
v|glauben|inanmak / sanmak
v|meinen|demek istemek / düşünmek
v|hoffen|ummak
v|wünschen|dilemek
v|geben|vermek
v|bringen|getirmek
v|holen|alıp getirmek
v|halten|tutmak
v|legen|yatırmak / koymak
v|stellen|dikey koymak
v|setzen|oturtmak / koymak
v|sitzen|oturmak
v|liegen|yatmak / bulunmak
v|aufwachen|uyanmak
v|einschlafen|uykuya dalmak
v|gehören|ait olmak
v|beginnen|başlamak
v|enden|bitmek
v|beenden|bitirmek
v|weitermachen|devam etmek
v|schaffen|başarmak / oluşturmak
v|gelingen|başarılı olmak
v|scheitern|başarısız olmak
v|danken|teşekkür etmek
v|bitten|rica etmek
v|erlauben|izin vermek
v|verbieten|yasaklamak
v|wählen|seçmek
v|planen|planlamak
v|ändern|değiştirmek
v|wachsen|büyümek
v|passieren|olmak / meydana gelmek
v|geschehen|gerçekleşmek
v|stattfinden|gerçekleşmek (etkinlik)
v|dauern|sürmek
v|besuchen|ziyaret etmek
v|einladen|davet etmek
v|mitkommen|birlikte gelmek
v|begleiten|eşlik etmek
v|verlassen|terk etmek
v|verabschieden|vedalaşmak
v|erkennen|tanımak / fark etmek
v|merken|fark etmek / aklında tutmak
v|leben|yaşamak
v|reisen|seyahat etmek
v|funktionieren|çalışmak (makine)
v|existieren|var olmak
v|genießen|keyfini çıkarmak
v|fürchten|korkmak
v|vertrauen|güvenmek
v|riskieren|risk almak
v|fehlen|eksik olmak
v|ärgern|kızdırmak
v|beruhigen|sakinleştirmek
v|überraschen|şaşırtmak
v|entschuldigen|affetmek, mazur görmek
""",
"A2.2": """
n|die Erfahrung|deneyim, tecrübe
n|die Bewerbung|iş başvurusu
n|der Lebenslauf|özgeçmiş (CV)
n|die Stelle|pozisyon, iş yeri
n|das Gehalt|maaş
n|der Vertrag|sözleşme
n|die Prüfung|sınav
n|die Ausbildung|meslek eğitimi
n|der Unterschied|fark
n|die Meinung|fikir, görüş
n|das Problem|sorun
n|die Lösung|çözüm
n|das Gefühl|his, duygu
n|die Umwelt|çevre
n|der Müll|çöp
v|sich freuen|sevinmek|er freut sich · hat sich gefreut
v|sich beeilen|acele etmek|er beeilt sich · hat sich beeilt
v|erklären|açıklamak|er erklärt · hat erklärt
v|verstehen|anlamak|er versteht · hat verstanden
v|versuchen|denemek, çalışmak|er versucht · hat versucht
v|entscheiden|karar vermek|er entscheidet · hat entschieden
v|erzählen|anlatmak|er erzählt · hat erzählt
v|bekommen|almak, elde etmek|er bekommt · hat bekommen
v|verlieren|kaybetmek|er verliert · hat verloren
v|gewinnen|kazanmak|er gewinnt · hat gewonnen
v|vorbereiten|hazırlamak|er bereitet vor · hat vorbereitet
v|umziehen|taşınmak|er zieht um · ist umgezogen
v|mitbringen|yanında getirmek|er bringt mit · hat mitgebracht
w|wichtig|önemli
w|zufrieden|memnun
w|pünktlich|dakik, zamanında
w|ziemlich|oldukça
n|der Beruf|meslek
n|der Job|iş
n|die Firma|firma
n|das Unternehmen|şirket
n|das Büro|ofis
n|der Chef|patron
n|der Mitarbeiter|çalışan
n|das Team|ekip
n|die Abteilung|departman
n|die Besprechung|toplantı
n|die Sitzung|oturum / toplantı
n|der Auftrag|görev / sipariş
n|die Aufgabe|görev
n|das Projekt|proje
n|das Praktikum|staj
n|das Vorstellungsgespräch|iş görüşmesi
n|die Kündigung|fesih / istifa
n|die Arbeitszeit|çalışma saati
n|die Überstunde|fazla mesai
n|die Pause|mola
n|die Schicht|vardiya
n|der Feierabend|paydos
n|die Vollzeit|tam zamanlı
n|die Teilzeit|yarı zamanlı
n|der Minijob|mini iş (az ücretli iş)
n|der Werkstudent|öğrenci çalışan
w|arbeitslos|işsiz
n|der Lehrer|öğretmen
n|der Ingenieur|mühendis
n|der Anwalt|avukat
n|der Koch|aşçı
n|der Bäcker|fırıncı
n|der Fahrer|şoför
n|der Polizist|polis memuru
n|der Krankenpfleger|hemşire (erkek)
n|die Krankenschwester|hemşire
n|der Handwerker|zanaatkâr / usta
n|der Elektriker|elektrikçi
n|der Mechaniker|tamirci
n|der Programmierer|yazılımcı
n|der Informatiker|bilgisayar bilimci
n|der Architekt|mimar
n|der Künstler|sanatçı
n|der Journalist|gazeteci
n|der Beamte|memur
n|der Student|öğrenci (üniversite)
n|der Praktikant|stajyer
n|der Rentner|emekli
v|verdienen|kazanmak
v|leiten|yönetmek
v|bewerben|başvurmak
v|einstellen|işe almak
n|die Karriere|kariyer
n|die Beförderung|terfi
n|der Kindergarten|anaokulu
n|die Grundschule|ilkokul
n|das Gymnasium|lise
n|die Hochschule|yüksekokul
n|der Unterricht|ders (saat)
n|das Fach|ders (branş)
n|die Klasse|sınıf
n|der Kurs|kurs
n|die Vorlesung|ders (üniversite)
n|das Seminar|seminer
n|der Schüler|öğrenci (okul)
n|der Professor|profesör
n|die Hausaufgabe|ödev
n|der Test|test
n|die Note|not
n|das Zeugnis|karne / belge
n|das Abitur|lise bitirme sınavı
n|das Studium|üniversite eğitimi
n|der Abschluss|mezuniyet / derece
n|der Bachelor|lisans
n|der Master|yüksek lisans
n|das Semester|dönem
n|das Buch|kitap
n|das Heft|defter
n|das Blatt|yaprak / sayfa
n|das Papier|kâğıt
n|der Stift|kalem
n|der Bleistift|kurşun kalem
n|der Kugelschreiber|tükenmez kalem
n|der Radiergummi|silgi
n|das Lineal|cetvel
n|die Schere|makas
n|die Tafel|tahta
n|der Schreibtisch|çalışma masası
n|das Wörterbuch|sözlük
n|die Grammatik|dilbilgisi
n|das Wort|kelime
n|der Satz|cümle
n|der Text|metin
n|die Übung|alıştırma
n|der Fehler|hata
n|die Antwort|cevap
n|das Beispiel|örnek
n|das Thema|konu
n|das Wissen|bilgi
v|studieren|üniversitede okumak
v|lehren|öğretmek
v|üben|alıştırma yapmak
v|wiederholen|tekrar etmek
v|rechnen|hesaplamak
v|durchfallen|sınavda kalmak
n|die Mathematik|matematik
n|die Physik|fizik
n|die Chemie|kimya
n|die Biologie|biyoloji
n|die Geschichte|tarih / hikâye
n|die Erdkunde|coğrafya
n|die Kunst|sanat
n|die Musik|müzik
n|die Natur|doğa
n|die Sonne|güneş
n|der Mond|ay (gökyüzü)
n|der Stern|yıldız
n|der Himmel|gökyüzü
n|die Wolke|bulut
n|der Schnee|kar
n|der Wind|rüzgâr
n|der Sturm|fırtına
n|der Nebel|sis
n|die Temperatur|sıcaklık
n|der Grad|derece
w|warm|ılık / sıcak
w|heiß|çok sıcak
w|kalt|soğuk
w|kühl|serin
w|sonnig|güneşli
w|bewölkt|bulutlu
w|regnerisch|yağmurlu
w|windig|rüzgârlı
w|neblig|sisli
w|trocken|kuru
w|nass|ıslak
w|feucht|nemli
n|der Berg|dağ
n|das Tal|vadi
n|der Wald|orman
n|der Baum|ağaç
n|die Blume|çiçek
n|das Gras|çimen
n|der See|göl
n|das Meer|deniz
n|der Strand|plaj
n|die Insel|ada
n|die Küste|kıyı
n|der Stein|taş
n|die Erde|toprak / dünya
n|die Welt|dünya
n|die Luft|hava
n|das Feuer|ateş
n|der Klimawandel|iklim değişikliği
n|die Energie|enerji
n|das Tier|hayvan
n|das Haustier|evcil hayvan
n|der Hund|köpek
n|die Katze|kedi
n|das Pferd|at
n|die Kuh|inek
n|das Schaf|koyun
n|die Ziege|keçi
n|das Schwein|domuz
n|das Huhn|tavuk
n|der Hahn|horoz
n|die Ente|ördek
n|der Vogel|kuş
n|die Maus|fare
n|das Kaninchen|tavşan
n|der Bär|ayı
n|der Löwe|aslan
n|der Elefant|fil
n|die Schlange|yılan
n|die Biene|arı
n|die Fliege|sinek
n|das Insekt|böcek
n|der Schwanz|kuyruk
n|der Flügel|kanat
n|das Fell|kürk / tüy
v|bellen|havlamak
v|fressen|yem yemek (hayvan)
v|füttern|beslemek
w|wild|vahşi
n|der Computer|bilgisayar
n|der Laptop|dizüstü bilgisayar
n|das Handy|cep telefonu
n|das Smartphone|akıllı telefon
n|das Telefon|telefon
n|der Bildschirm|ekran
n|die Tastatur|klavye
n|die Datei|dosya
n|das Programm|program
n|die Software|yazılım
n|die App|uygulama
n|das Internet|internet
n|die Webseite|web sitesi
n|die E-Mail|e-posta
n|die Nachricht|mesaj / haber
n|das Passwort|şifre
n|der Benutzer|kullanıcı
n|die Daten|veri
n|der Speicher|bellek / depolama
n|das WLAN|kablosuz internet
n|der Anschluss|bağlantı / hat
n|der Akku|batarya
n|das Ladegerät|şarj aleti
n|der Anruf|arama
v|telefonieren|telefonla konuşmak
v|schicken|göndermek
v|senden|yollamak
v|herunterladen|indirmek
v|hochladen|yüklemek
v|speichern|kaydetmek
v|löschen|silmek
v|klicken|tıklamak
v|suchen|aramak
v|finden|bulmak
v|installieren|kurmak
v|ausschalten|kapatmak
v|einschalten|açmak
n|der Fernseher|televizyon
n|das Foto|fotoğraf
n|das Video|video
n|die Technik|teknik / teknoloji
v|duschen|duş almak
v|baden|banyo yapmak
v|kämmen|taramak (saç)
v|rasieren|tıraş etmek
v|notieren|not almak
v|organisieren|organize etmek
v|malen|resim yapmak, boyamak
v|zeichnen|çizmek
v|basteln|el işi yapmak
v|erwarten|beklemek (ummak)
v|schwimmen|yüzmek
v|springen|zıplamak, atlamak
v|klettern|tırmanmak
v|rauchen|sigara içmek
v|surfen|internette gezinmek; sörf yapmak
v|chatten|sohbet etmek (internette)
v|posten|paylaşım yapmak
v|liken|beğenmek (sosyal medya)
v|kommentieren|yorum yapmak
v|drucken|yazdırmak
v|scannen|taramak
v|zahlen|ödemek
v|grillen|ızgara yapmak
v|spülen|bulaşık yıkamak; durulamak
v|bügeln|ütü yapmak
v|nähen|dikiş dikmek
v|kleben|yapıştırmak
v|auflegen|telefonu kapatmak
v|ausladen|yük boşaltmak; daveti iptal etmek
v|parken|park etmek
v|tanken|benzin almak
v|sortieren|ayırmak, sıralamak
v|betrachten|incelemek, bakmak
v|prüfen|kontrol etmek, sınamak
v|eintragen|kaydetmek, yazmak
v|anwenden|uygulamak
v|raten|tavsiye etmek; tahmin etmek
v|warnen|uyarmak
v|drohen|tehdit etmek
v|zurückkehren|geri dönmek
v|verschwinden|kaybolmak
v|erscheinen|görünmek, çıkmak (yayın)
v|entstehen|ortaya çıkmak, oluşmak
v|sich entwickeln|gelişmek
v|sich verändern|değişmek
v|verschlimmern|kötüleştirmek
v|sichern|güvence altına almak; yedeklemek
v|halbieren|ikiye bölmek
v|verdoppeln|iki katına çıkarmak
v|multiplizieren|çarpmak
v|addieren|toplamak
v|subtrahieren|çıkarmak (matematik)
v|dividieren|bölmek (matematik)
v|unterscheiden|ayırt etmek
v|ordnen|düzenlemek
""",
"B1.1": """
n|die Voraussetzung|ön koşul
n|die Möglichkeit|imkân, olasılık
n|die Entwicklung|gelişme
n|die Gesellschaft|toplum; şirket
n|der Zusammenhang|bağlam, ilişki
n|die Verantwortung|sorumluluk
n|die Behörde|resmi daire
n|der Antrag|başvuru (dilekçe)
n|die Anmeldung|kayıt (adres vb.)
n|die Versicherung|sigorta
n|die Gesundheit|sağlık
n|der Vorteil|avantaj
n|der Nachteil|dezavantaj
n|die Ursache|sebep
n|die Folge|sonuç
v|sich bewerben|başvurmak (um + Akk.)|er bewirbt sich · hat sich beworben
v|sich kümmern|ilgilenmek (um + Akk.)|er kümmert sich · hat sich gekümmert
v|sich gewöhnen|alışmak (an + Akk.)|er gewöhnt sich · hat sich gewöhnt
v|sich beschweren|şikâyet etmek (über + Akk.)|er beschwert sich · hat sich beschwert
v|teilnehmen|katılmak (an + Dat.)|er nimmt teil · hat teilgenommen
v|empfehlen|tavsiye etmek|er empfiehlt · hat empfohlen
v|vergleichen|karşılaştırmak|er vergleicht · hat verglichen
v|beschreiben|tarif etmek, betimlemek|er beschreibt · hat beschrieben
v|ausfüllen|(form) doldurmak|er füllt aus · hat ausgefüllt
v|unterschreiben|imzalamak|er unterschreibt · hat unterschrieben
v|kündigen|feshetmek, istifa etmek|er kündigt · hat gekündigt
v|erreichen|ulaşmak|er erreicht · hat erreicht
v|sich erinnern|hatırlamak (an + Akk.)|er erinnert sich · hat sich erinnert
w|deshalb|bu yüzden
w|trotzdem|yine de
w|ehrlich|dürüst
w|selbstständig|bağımsız; serbest çalışan
w|Deutschland|Almanya
n|die Türkei|Türkiye
w|Österreich|Avusturya
n|die Schweiz|İsviçre
w|Frankreich|Fransa
w|Russland|Rusya
w|Europa|Avrupa
w|Deutsch|Almanca
w|Türkisch|Türkçe
w|Englisch|İngilizce
n|die Muttersprache|ana dil
n|der Ausländer|yabancı
n|die Nationalität|uyruk
n|die Staatsangehörigkeit|vatandaşlık
n|die Kultur|kültür
n|die Tradition|gelenek
n|die Religion|din
n|die Regierung|hükümet
n|der Staat|devlet
n|die Politik|siyaset
n|das Gesetz|kanun
n|das Recht|hak / hukuk
n|die Freiheit|özgürlük
n|die Zeitung|gazete
n|die Nachrichten|haberler
n|der Sport|spor
n|das Spiel|oyun / maç
n|der Fußball|futbol
n|das Schwimmen|yüzme
n|das Laufen|koşu
n|das Fitness|fitness
n|das Training|antrenman
n|die Mannschaft|takım
n|der Spieler|oyuncu
n|der Trainer|antrenör
n|das Tor|gol / kapı
n|der Sieg|zafer
n|der Ball|top
n|die Freizeit|boş zaman
n|das Hobby|hobi
n|das Lied|şarkı
n|der Film|film
n|die Serie|dizi
n|das Konzert|konser
n|die Party|parti
n|das Fest|kutlama / festival
n|das Geschenk|hediye
n|die Feier|kutlama
n|das Lesen|okuma
n|das Kochen|yemek yapma
n|der Spaziergang|yürüyüş
v|trainieren|antrenman yapmak
v|sich entspannen|rahatlamak
v|feiern|kutlamak
v|tanzen|dans etmek
v|singen|şarkı söylemek
n|das Amt|resmî daire
n|das Bürgeramt|nüfus dairesi
n|die Ausländerbehörde|yabancılar dairesi
n|das Finanzamt|vergi dairesi
n|das Jobcenter|iş kurumu
n|die Agentur für Arbeit|iş ajansı
n|die Abmeldung|kayıt sildirme
n|die Bescheinigung|belge / yazı
n|das Formular|form
n|der Bescheid|karar yazısı
n|die Unterschrift|imza
n|der Stempel|mühür
n|die Kopie|kopya
n|das Original|asıl / orijinal
n|die Frist|süre / son tarih
n|der Nachweis|kanıt / belge
n|die Meldebescheinigung|ikamet belgesi
n|die Aufenthaltserlaubnis|oturma izni
n|die Arbeitserlaubnis|çalışma izni
n|die Steuer-ID|vergi numarası
n|die Sozialversicherung|sosyal sigorta
n|die Rentenversicherung|emeklilik sigortası
n|die Haftpflichtversicherung|sorumluluk sigortası
n|der Rundfunkbeitrag|yayın katkı payı
n|der Sachbearbeiter|dosya sorumlusu
n|der Schalter|gişe
n|die Wartenummer|sıra numarası
n|die Öffnungszeiten|açılış saatleri
v|beantragen|başvurmak
v|einreichen|teslim etmek
v|verlängern|uzatmak
v|abholen|teslim almak
v|anmelden|kaydolmak
w|erlaubt|izinli
w|verboten|yasak
w|nötig|gerekli
w|gültig|geçerli
v|erinnern|hatırlamak
v|berichten|rapor etmek
v|zeigen|göstermek
v|bedeuten|anlamına gelmek
v|übersetzen|çevirmek
v|aussprechen|telaffuz etmek
v|öffnen|açmak
v|schließen|kapatmak
v|zumachen|kapatmak
v|aufmachen|açmak
v|drücken|basmak / itmek
v|ziehen|çekmek
v|werfen|atmak
v|fangen|yakalamak
v|fallen|düşmek
v|heben|kaldırmak
v|bauen|inşa etmek
v|reparieren|tamir etmek
v|kaputt machen|bozmak
v|benutzen|kullanmak
v|verwenden|kullanmak
v|sammeln|toplamak / biriktirmek
v|teilen|paylaşmak / bölmek
v|verteilen|dağıtmak
v|wechseln|değiştirmek
v|tauschen|takas etmek
v|leihen|ödünç vermek / almak
v|besitzen|sahip olmak
v|entdecken|keşfetmek
v|mitteilen|bildirmek
v|streiten|tartışmak / kavga etmek
v|diskutieren|tartışmak
v|versprechen|söz vermek
v|lügen|yalan söylemek
v|stören|rahatsız etmek
v|beeilen|acele etmek
v|beobachten|gözlemlemek
v|aufpassen|dikkat etmek
v|kümmern|ilgilenmek
v|sorgen|endişelenmek / ilgilenmek
v|schützen|korumak
v|retten|kurtarmak
v|kämpfen|savaşmak / mücadele etmek
v|bemerken|fark etmek
v|interessieren|ilgisini çekmek
v|gefallen|hoşuna gitmek
v|lieben|sevmek
v|hassen|nefret etmek
v|lachen|gülmek
v|weinen|ağlamak
v|lächeln|gülümsemek
v|küssen|öpmek
v|rufen|seslenmek / çağırmak
v|schreien|bağırmak
v|riechen|koklamak / kokmak
v|schmecken|tadı olmak
v|fühlen|hissetmek
v|berühren|dokunmak
v|wiegen|tartmak
v|messen|ölçmek
v|zählen|saymak
v|vermieten|kiraya vermek
v|liefern|teslim etmek
v|führen|yönlendirmek / götürmek
v|folgen|takip etmek
v|vorschlagen|önermek
v|anbieten|sunmak
v|annehmen|kabul etmek / varsaymak
v|akzeptieren|kabul etmek
v|rennen|koşmak
v|träumen|rüya görmek / hayal etmek
w|schlecht|kötü
w|lang|uzun
w|kurz|kısa
w|hoch|yüksek
w|niedrig|alçak
w|breit|geniş
w|schmal|dar
w|dick|kalın / şişman
w|dünn|ince
w|schwer|ağır / zor
w|leicht|hafif / kolay
w|neu|yeni
w|alt|eski / yaşlı
w|jung|genç
w|modern|modern
w|langsam|yavaş
w|laut|gürültülü
w|leise|sessiz
w|voll|dolu
w|leer|boş
w|offen|açık
w|geschlossen|kapalı
w|richtig|doğru
w|falsch|yanlış
w|wahr|gerçek
w|möglich|mümkün
w|unmöglich|imkânsız
w|einfach|basit / kolay
w|schwierig|zor
w|kompliziert|karmaşık
w|interessant|ilginç
w|langweilig|sıkıcı
w|schön|güzel
w|nett|kibar / hoş
w|freundlich|dostane
w|höflich|nazik
w|ruhig|sakin
w|nervös|gergin
w|fleißig|çalışkan
w|faul|tembel / çürük
w|klug|akıllı
w|dumm|aptal
w|gefährlich|tehlikeli
w|sicher|güvenli / emin
w|frei|özgür / boş
w|besetzt|dolu / meşgul
w|beschäftigt|meşgul
w|bereit|hazır
w|fertig|bitmiş / hazır
w|nützlich|faydalı
w|beliebt|sevilen / popüler
w|bekannt|tanınmış
w|fremd|yabancı
w|ähnlich|benzer
w|verschieden|farklı
w|besonders|özel / özellikle
w|normal|normal
w|echt|gerçek / hakiki
w|privat|özel / kişisel
w|öffentlich|kamuya açık
w|arm|fakir
w|reich|zengin
w|glücklich|mutlu
w|traurig|üzgün
w|lustig|komik
w|ernst|ciddi
w|stolz|gururlu
w|mutig|cesur
w|geduldig|sabırlı
w|zuverlässig|güvenilir
w|erfolgreich|başarılı
w|hilfsbereit|yardımsever
w|kreativ|yaratıcı
w|praktisch|pratik
w|perfekt|mükemmel
w|wunderbar|harika
w|toll|süper
v|lösen|çözmek
v|befestigen|sabitlemek
v|befehlen|emretmek
v|gehorchen|itaat etmek
v|schenken|hediye etmek
v|ausleihen|ödünç almak
v|investieren|yatırım yapmak
v|zurückkommen|geri gelmek
v|zurückgehen|geri gitmek
v|losfahren|yola çıkmak
v|abreisen|ayrılmak (yolculuğa çıkmak)
v|mitnehmen|yanında götürmek
v|wegwerfen|çöpe atmak
v|auspacken|paketi açmak
v|markieren|işaretlemek
v|kopieren|kopyalamak
v|übertragen|aktarmak; yayınlamak
v|verbinden|bağlamak
v|trennen|ayırmak
v|begegnen|karşılaşmak (+ Dativ)
v|empfangen|karşılamak; almak (sinyal)
v|bewundern|hayran olmak
v|ergänzen|tamamlamak
v|informieren|bilgilendirmek
v|beweisen|kanıtlamak
v|verschlechtern|kötüleştirmek
v|verändern|değiştirmek
v|erweitern|genişletmek
v|reduzieren|azaltmak
v|erhöhen|artırmak
v|nutzen|yararlanmak, kullanmak
v|experimentieren|deney yapmak
v|starten|başlatmak
v|stoppen|durdurmak
v|pausieren|ara vermek
v|fortsetzen|devam ettirmek
v|unterbrechen|kesmek, bölmek
v|vorbeikommen|uğramak
v|vorbeifahren|yanından geçip gitmek
v|umdrehen|çevirmek, döndürmek
v|zurückbleiben|geride kalmak
v|behandeln|tedavi etmek; davranmak
v|bedauern|üzülmek, pişman olmak
v|beklagen|yakınmak
v|beweinen|ağıt yakmak, yasını tutmak
v|vermissen|özlemek
v|schätzen|değer vermek; tahmin etmek
v|respektieren|saygı duymak
v|tolerieren|hoş görmek
v|ignorieren|görmezden gelmek
v|analysieren|analiz etmek
v|recherchieren|araştırmak
v|erläutern|izah etmek
v|bewerten|değerlendirmek, not vermek
v|definieren|tanımlamak
v|entwickeln|geliştirmek
v|konstruieren|tasarlayıp inşa etmek
v|produzieren|üretmek
v|konsumieren|tüketmek
v|exportieren|ihraç etmek
v|importieren|ithal etmek
v|verschwenden|israf etmek
v|erhalten|almak, teslim almak; korumak
v|testen|test etmek
v|versagen|başarısız olmak
v|misslingen|başarısız olmak (iş)
v|vorhersehen|önceden görmek
v|gedeihen|gelişmek, serpilmek
v|vergehen|geçmek (zaman)
""",
"B1.2": """
n|die Erwartung|beklenti
n|die Herausforderung|zorluk, meydan okuma
n|die Fähigkeit|yetenek
n|die Kenntnisse|bilgiler (Pl.)
n|das Ziel|hedef
n|der Erfolg|başarı
n|die Absicht|niyet
n|das Verhalten|davranış
n|die Beziehung|ilişki
n|der Streit|kavga, tartışma
n|die Ausnahme|istisna
n|der Zweck|amaç
n|die Werbung|reklam
n|der Verbraucher|tüketici
n|die Gelegenheit|fırsat
v|sich verlassen|güvenmek (auf + Akk.)|er verlässt sich · hat sich verlassen
v|sich entschuldigen|özür dilemek|er entschuldigt sich · hat sich entschuldigt
v|vermeiden|kaçınmak|er vermeidet · hat vermieden
v|verbessern|geliştirmek, düzeltmek|er verbessert · hat verbessert
v|überzeugen|ikna etmek|er überzeugt · hat überzeugt
v|behaupten|iddia etmek|er behauptet · hat behauptet
v|zweifeln|şüphe etmek (an + Dat.)|er zweifelt · hat gezweifelt
v|abhängen|bağlı olmak (von + Dat.)|es hängt ab · hat abgehangen
v|erledigen|halletmek|er erledigt · hat erledigt
v|verschieben|ertelemek|er verschiebt · hat verschoben
v|zunehmen|artmak; kilo almak|er nimmt zu · hat zugenommen
v|abnehmen|azalmak; kilo vermek|er nimmt ab · hat abgenommen
v|sich vorstellen|kendini tanıtmak; hayal etmek|er stellt sich vor · hat sich vorgestellt
w|eigentlich|aslında
w|allerdings|ancak, gerçi
w|vorsichtig|dikkatli
w|neugierig|meraklı
n|die Freude|sevinç
n|das Glück|mutluluk / şans
n|die Trauer|keder
n|die Angst|korku
n|die Sorge|endişe
n|der Stress|stres
n|die Wut|öfke
n|der Ärger|kızgınlık / dert
n|die Überraschung|sürpriz
n|die Hoffnung|umut
n|der Wunsch|dilek
n|das Vertrauen|güven
n|der Mut|cesaret
n|die Geduld|sabır
n|die Ruhe|huzur / sessizlik
n|die Langeweile|can sıkıntısı
n|die Einsamkeit|yalnızlık
n|der Charakter|karakter
n|die Laune|keyif / ruh hâli
n|die Stimmung|atmosfer / ruh hâli
n|das Lachen|gülüş
n|die Träne|gözyaşı
v|sich ärgern|sinirlenmek
v|sich schämen|utanmak
v|sich langweilen|sıkılmak
v|sich verlieben|âşık olmak
v|sich wundern|şaşırmak
v|sich beruhigen|sakinleşmek
w|aufgeregt|heyecanlı
w|enttäuscht|hayal kırıklığına uğramış
w|überrascht|şaşırmış
w|verliebt|âşık
w|wütend|öfkeli
w|eifersüchtig|kıskanç
w|schüchtern|utangaç
w|gespannt|merakla bekleyen
w|erschöpft|tükenmiş
w|sehr|çok
w|ganz|tamamen / oldukça
w|fast|neredeyse
w|nur|sadece
w|auch|de / da
w|noch|hâlâ / daha
w|schon|zaten / çoktan
w|erst|ancak / ilk olarak
w|wieder|yine
w|nochmal|tekrar
p|vor allem|her şeyden önce
p|zum Beispiel|örneğin
w|übrigens|bu arada
w|wirklich|gerçekten
w|bestimmt|mutlaka
w|wahrscheinlich|muhtemelen
w|hoffentlich|umarım
p|zum Glück|neyse ki
w|plötzlich|aniden
w|endlich|sonunda
w|zuerst|önce
w|dann|sonra
w|danach|ondan sonra
w|zuletzt|en son
w|schließlich|nihayet
w|zusammen|birlikte
w|allein|yalnız
w|gemeinsam|ortaklaşa
w|überall|her yerde
w|dort|orada
w|hier|burada
w|da|orada / işte
w|draußen|dışarıda
w|drinnen|içeride
w|weg|uzakta / gitmiş
w|zurück|geri
w|weiter|daha ileri
w|sonst|yoksa / başka
w|kaum|neredeyse hiç
w|nicht|değil
w|doch|ama / yine de
w|gern|memnuniyetle
w|lieber|tercihen
p|am liebsten|en çok
w|mindestens|en az
w|höchstens|en fazla
w|ungefähr|yaklaşık
w|etwa|yaklaşık
w|normalerweise|normalde
w|insgesamt|toplamda
w|außerdem|ayrıca
w|jedoch|ancak
w|sogar|hatta
w|bereits|hâlihazırda
w|damals|o zamanlar
v|melden|bildirmek
v|empfinden|hissetmek
v|festlegen|belirlemek
v|vorstellen|tanıtmak
v|sich vorbereiten|hazırlanmak
v|sich treffen|buluşmak
v|sich setzen|oturmak
v|sich waschen|yıkanmak
v|sich anziehen|giyinmek
v|sich ausziehen|soyunmak
v|sich verlieben in|-e âşık olmak
v|sich bedanken|teşekkür etmek
v|sich verabschieden|vedalaşmak
v|sich entscheiden|karar vermek
v|sich konzentrieren|odaklanmak
v|sich wünschen|dilemek, istemek
v|sich lohnen|değmek
v|sich auszahlen|karşılığını vermek
v|sich überlegen|düşünüp taşınmak
v|sich irren|yanılmak
v|sich ändern|değişmek
v|sich verbessern|gelişmek, iyileşmek
v|sich informieren|bilgi almak
v|sich beklagen|şikâyet etmek
v|sich unterhalten|sohbet etmek
v|sich verlaufen|yolunu kaybetmek
v|sich anstrengen|çaba göstermek
v|sich auskennen|bir konuyu iyi bilmek
v|sich trauen|cesaret etmek
v|sich verschlechtern|kötüleşmek
v|sich sorgen|endişelenmek
v|sich freuen auf|dört gözle beklemek
v|sich umsehen|etrafa bakmak
v|sich verstehen|anlaşmak
v|sich streiten|tartışmak, kavga etmek
v|sich vertragen|iyi geçinmek
v|sich anpassen|uyum sağlamak
w|dabei|bu sırada; bu konuda
w|dazu|buna ek olarak; bunun için
w|sowie|ve ayrıca
w|dafür|bunun için; buna karşılık
w|davon|bundan
w|darauf|bunun üzerine
w|zwar … aber|gerçi … ama
w|jemand|biri
w|darüber|bunun hakkında
w|eben|az önce; işte
w|beide|her ikisi
w|daran|buna
w|direkt|doğrudan
w|anders|farklı
w|ebenfalls|aynı şekilde, de
w|eher|daha çok; daha erken
w|nachdem|-dikten sonra
w|egal|fark etmez
w|bisher|şimdiye kadar
w|mehrere|birkaç
w|niemand|hiç kimse
w|zunächst|ilk önce
w|darum|bu yüzden
w|bevor|-meden önce
w|wert|değerinde
w|innerhalb|içinde (+ Gen.)
w|völlig|tamamen
w|zudem|üstelik
w|irgendwie|bir şekilde
w|vorbei|geçmiş, bitmiş
w|dagegen|buna karşı
w|wobei|ki bu sırada
n|der Einsatz|kullanım; görev; çaba
w|falls|eğer, -diği takdirde
w|hinaus|dışarı
w|vorher|önceden
w|häufig|sık
w|manche|bazı
w|unbedingt|mutlaka
w|unterwegs|yolda
w|wenigstens|en azından
w|zuvor|daha önce
w|indem|-erek
w|entfernt|uzak
w|durchaus|kesinlikle, tamamen
w|inzwischen|bu arada, artık
w|komplett|tamamen
w|niemals|asla
w|erneut|yeniden
w|total|tamamen
w|früh|erken
w|nahe|yakın
v|nennen|adlandırmak
v|erfahren|öğrenmek (haber); deneyimlemek
w|aktiv|aktif
w|hart|sert
w|offenbar|anlaşılan
w|absolut|kesinlikle
w|immerhin|yine de, hiç değilse
w|solange|-dığı sürece
w|ständig|sürekli
w|persönlich|kişisel
v|bieten|sunmak
w|spät|geç
v|sterben|ölmek
w|stets|daima
n|die Version|sürüm
w|irgendwo|bir yerde
w|froh|memnun
v|leisten|başarmak; karşılamak
v|aussehen|görünmek
w|miteinander|birbiriyle
w|schade|yazık
w|schlimm|kötü, vahim
w|verantwortlich|sorumlu
w|weltweit|dünya çapında
w|vorhanden|mevcut
n|die Halle|salon
w|wiederum|öte yandan; yine
w|zugleich|aynı zamanda
w|extrem|aşırı
w|längst|çoktan
w|positiv|olumlu
w|böse|kötü; kızgın
w|diesmal|bu kez
v|handeln|davranmak; ticaret yapmak
w|notwendig|gerekli
w|näher|daha yakın
v|reichen|yetmek; uzatmak
n|die Industrie|sanayi
w|innen|içeride
w|unglaublich|inanılmaz
v|sich befinden|bulunmak
n|das Finale|final
w|herum|etrafında
n|der Landkreis|ilçe
v|treten|basmak; tekmelemek
w|entgegen|-e karşı, aksine
w|hauptsächlich|başlıca
v|ansehen|bakmak, seyretmek
w|international|uluslararası
w|sicherlich|kesinlikle
w|vollkommen|mükemmel; tamamen
w|mitten|ortasında
w|seitdem|o zamandan beri
w|sowieso|zaten
n|die Stiftung|vakıf
w|vollständig|eksiksiz
w|unabhängig|bağımsız
v|erleben|yaşamak, tecrübe etmek
v|schlagen|vurmak; yenmek
w|entlang|boyunca
v|kriegen|almak (günlük dil)
w|teils|kısmen
v|bewegen|hareket ettirmek
v|dienen|hizmet etmek
w|ursprünglich|aslında, başlangıçta
n|der Wille|irade
w|abgesehen von|-den başka
w|komisch|tuhaf; komik
w|mehrfach|defalarca
v|steuern|yönlendirmek
v|aussagen|ifade vermek
w|geschickt|becerikli
w|politisch|siyasi
w|real|gerçek
w|daneben|yanında; ayrıca
w|dringend|acil
v|hängen|asılı olmak; asmak
w|morgens|sabahları
w|nachts|geceleri
n|der Nutzer|kullanıcı
n|die Nutzung|kullanım
w|tätig|faal, çalışan
w|automatisch|otomatik
w|gelassen|sakin
w|momentan|şu an
w|nahezu|neredeyse
w|demnach|buna göre
n|der Hersteller|üretici
w|jemals|hiç, şimdiye dek
w|kaputt|bozuk
w|mittels|aracılığıyla
w|unmittelbar|doğrudan, hemen
v|fordern|talep etmek
v|gestalten|biçimlendirmek, tasarlamak
w|anscheinend|görünüşe göre
n|die Kommunikation|iletişim
v|scheinen|görünmek; parlamak
w|spätestens|en geç
""",
"B2.1": """
n|die Auswirkung|etki, sonuç
n|die Maßnahme|önlem
n|der Aufwand|emek, zahmet
n|die Bedingung|koşul
n|die Einstellung|tutum; ayar; işe alım
n|die Forderung|talep
n|der Vorwurf|suçlama, sitem
n|die Ansicht|görüş
n|das Vorurteil|önyargı
n|die Zuverlässigkeit|güvenilirlik
n|der Wettbewerb|rekabet
n|die Nachhaltigkeit|sürdürülebilirlik
n|die Begründung|gerekçe
n|der Umgang|(bir şeyle) başa çıkma, ilişki
n|der Anspruch|hak, talep
v|beitragen|katkıda bulunmak (zu + Dat.)|er trägt bei · hat beigetragen
v|berücksichtigen|dikkate almak|er berücksichtigt · hat berücksichtigt
v|bewältigen|üstesinden gelmek|er bewältigt · hat bewältigt
v|ermöglichen|mümkün kılmak|er ermöglicht · hat ermöglicht
v|beeinflussen|etkilemek|er beeinflusst · hat beeinflusst
v|darstellen|temsil etmek, sunmak|er stellt dar · hat dargestellt
v|sich auseinandersetzen|ele almak, uğraşmak (mit)|er setzt sich auseinander · hat sich auseinandergesetzt
v|feststellen|tespit etmek|er stellt fest · hat festgestellt
v|verzichten|vazgeçmek (auf + Akk.)|er verzichtet · hat verzichtet
v|bestehen|(sınavı) geçmek; ısrar etmek (auf)|er besteht · hat bestanden
v|nachweisen|kanıtlamak|er weist nach · hat nachgewiesen
v|gewährleisten|güvence altına almak|er gewährleistet · hat gewährleistet
w|offensichtlich|apaçık
w|ausreichend|yeterli
w|umfangreich|kapsamlı
w|dennoch|buna rağmen
w|nachvollziehbar|anlaşılır, makul
n|die Anforderung|gereklilik, talep
n|der Bedarf|ihtiyaç
n|die Beschwerde|şikâyet
n|die Erkenntnis|bulgu, idrak
n|das Ereignis|olay
n|die Fortbildung|mesleki gelişim eğitimi
n|die Gewohnheit|alışkanlık
n|der Hinweis|ipucu, uyarı
n|die Leistung|performans; hizmet
n|das Merkmal|özellik
n|die Mehrheit|çoğunluk
n|die Minderheit|azınlık
n|der Standpunkt|bakış açısı
n|die Überzeugung|inanç, kanaat
n|der Umstand|durum, koşul
n|die Verpflichtung|yükümlülük
n|der Verlauf|seyir, süreç
n|die Wirkung|etki
n|der Zweifel|şüphe
n|die Zusammenarbeit|iş birliği
n|der Zugang|erişim
v|ausüben|icra etmek, uygulamak
v|beantworten|cevaplamak
v|bedenken|göz önünde bulundurmak
v|befürchten|endişe etmek
v|begründen|gerekçelendirmek
v|beurteilen|değerlendirmek, yargılamak
v|durchführen|yürütmek, gerçekleştirmek
v|eingehen auf|ele almak, değinmek
v|einhalten|uymak (kurala, süreye)
v|ermitteln|tespit etmek; soruşturmak
v|fördern|desteklemek, teşvik etmek
v|hinweisen auf|dikkat çekmek
v|nachdenken über|üzerine düşünmek
v|überwiegen|ağır basmak
v|verlangen|talep etmek
v|voraussetzen|şart koşmak, varsaymak
v|zurückführen auf|-e bağlamak
w|angemessen|uygun, makul
w|bedeutend|önemli
w|eindeutig|açık, kesin
w|gegenseitig|karşılıklı
w|grundsätzlich|temelde, prensipte
w|jedenfalls|her halükârda
w|überwiegend|ağırlıklı olarak
w|vermutlich|muhtemelen
w|zumindest|en azından
w|zunehmend|giderek
v|angehen, ansprechen|ele almak, çözüme kavuşturmak
v|unterstützen; sichern|desteklemek, yedeklemek
v|beschuldigen, die Schuld geben|suçlamak
v|herausfordern, infrage stellen|meydan okumak, sorgulamak
v|bestimmen, festlegen|belirlemek, saptamak
v|sicherstellen, gewährleisten|sağlamak, garantiye almak
v|steigen, erhöhen|artmak, artırmak
v|aufrechterhalten; behaupten|sürdürmek, savunmak
v|verhindern|önlemek
n|der Reiz; der Einspruch|çekicilik, itiraz
n|die Kapazität|kapasite, yetenek
w|wesentlich, unerlässlich|temel, şart
w|relevant|konuyla ilgili
p|einen Rückzieher machen|geri adım atmak
p|sich einfallen lassen|bulmak, ortaya atmak
p|über die Runden kommen|idare etmek, geçinmek
p|gut auskommen mit; weitermachen|iyi geçinmek, devam etmek
p|nachgeben|pes etmek, boyun eğmek
p|durchgehen, überprüfen|gözden geçirmek
p|Schritt halten mit|ayak uydurmak
p|untersuchen|araştırmak, incelemek
p|wiedergutmachen|telafi etmek
p|sich abfinden mit|katlanmak
p|aufbrechen; darlegen|yola koyulmak, ortaya koymak
p|einrichten, gründen|kurmak
p|wie dem auch sei|öyle olsa bile
p|im Einklang mit|-ile uyumlu olarak
w|andernfalls|aksi takdirde
p|davon abgesehen|bununla birlikte
w|somit|böylece
v|stecken|sokmak; bulunmak
w|voraus|önde, önceden
v|achten auf|dikkat etmek
w|ausgezeichnet|mükemmel
w|einst|bir zamanlar
n|die Integration|entegrasyon, uyum
w|womit|neyle
n|der Code|kod
w|definitiv|kesinlikle
v|drehen|döndürmek; çekmek (film)
w|gratis|bedava
w|witzig|esprili
w|zumal|özellikle de
w|anstatt|yerine
w|aufmerksam|dikkatli
w|ausgeschlossen|imkânsız
w|begeistert|heyecanlı, hayran
w|daraufhin|bunun üzerine
w|erforderlich|gerekli
w|ewig|sonsuz
v|aufnehmen|kaydetmek; kabul etmek
w|speziell|özel
n|der Tipp|ipucu
w|betroffen|etkilenmiş
v|erfolgen|gerçekleşmek
w|ernsthaft|ciddi
n|der Hass|nefret
w|sinnvoll|anlamlı, mantıklı
w|sofern|-dığı sürece
n|das Umfeld|çevre, ortam
v|vergeben|affetmek; vermek
w|einerseits … andererseits|bir yandan … öte yandan
w|eventuell|belki
w|generell|genel olarak
v|gucken|bakmak (günlük)
w|quasi|adeta
w|scheinbar|görünüşte
n|die Variante|varyant
w|genügend|yeterli
w|lieb|sevimli
w|maximal|en fazla
w|bezüglich|ile ilgili (+ Gen.)
w|blöd|aptalca
w|ordentlich|düzenli
w|wach|uyanık
v|greifen|tutmak, kavramak
n|die Hölle|cehennem
w|locker|gevşek, rahat
w|sichtbar|görünür
w|dankbar|minnettar
w|dicht|sık; sızdırmaz
w|doppelt|çift
w|einzig|tek
w|gezwungen|zorunda kalmış
w|inklusive|dahil
v|stammen aus|-den gelmek
w|still|sessiz
v|vorgehen|davranmak; ilerlemek
w|zuständig|yetkili, sorumlu
n|der Anbieter|sağlayıcı
w|herzlich|içten
w|spannend|heyecanlı
v|treiben|sürmek; yapmak (spor)
v|töten|öldürmek
w|unterschiedlich|farklı
w|beinahe|neredeyse
v|fassen|tutmak; kavramak
w|gebildet|eğitimli
v|geraten in|-e düşmek
w|jederzeit|her zaman
n|das Netzwerk|ağ
v|reagieren|tepki vermek
n|der Schuss|atış
v|spenden|bağış yapmak
v|verbringen|geçirmek (zaman)
v|beziehen|almak; taşınmak
w|ferner|ayrıca
v|gelangen|ulaşmak
w|hinterher|sonradan
n|der Rassismus|ırkçılık
n|die Fraktion|meclis grubu
w|freiwillig|gönüllü
w|gewohnt|alışık
n|die Kooperation|iş birliği
w|lächerlich|gülünç
w|nachher|sonra
w|negativ|olumsuz
v|richten|yöneltmek
w|zufolge|-e göre
w|endgültig|kesin, nihai
w|fair|adil
n|die Finanzierung|finansman
w|gering|az
v|umgehen mit|başa çıkmak
w|wiederholt|tekrar tekrar
w|angebracht|uygun
w|mehrmals|birkaç kez
v|spüren|hissetmek
n|die Verbesserung|iyileştirme
w|gerecht|adil
w|heutzutage|günümüzde
n|die Hinsicht|bakımdan
w|insofern|bu bakımdan
w|künftig|gelecekte
n|die Option|seçenek
w|rechtzeitig|zamanında
w|verrückt|deli
v|entfernen|kaldırmak
w|gelegentlich|ara sıra
w|typisch|tipik
v|sich wenden an|başvurmak
v|abgeben|teslim etmek
n|die Erweiterung|genişleme
w|nackt|çıplak
w|peinlich|utanç verici
v|verteidigen|savunmak
n|das Überleben|hayatta kalma
w|demnächst|yakında
w|fein|ince; güzel
w|heftig|şiddetli
n|die Kampagne|kampanya
w|korrekt|doğru
w|oftmals|çoğu zaman
v|präsentieren|sunmak
v|siegen|galip gelmek
w|sozial|sosyal
w|technisch|teknik
w|ausgerechnet|tam da
v|landen|inmek
v|profitieren|yararlanmak
w|umsonst|boşuna; bedava
w|einander|birbirini
w|erstaunlich|şaşırtıcı
n|die Motivation|motivasyon
n|der Profi|profesyonel
n|der Beschluss|karar
v|brechen|kırmak
v|ehren|onurlandırmak
v|erlangen|elde etmek
w|gefangen|esir
w|kürzlich|geçenlerde
w|massiv|büyük; masif
w|rasch|hızlı
w|spontan|kendiliğinden
v|verraten|ele vermek
w|verständlich|anlaşılır
w|angewiesen auf|-e muhtaç
w|bedingt|şartlı; kısmen
w|beschränkt|sınırlı
w|hübsch|güzel, hoş
w|jenseits|ötesinde
v|räumen|boşaltmak, toplamak
w|seltsam|garip
w|versteckt|gizli
n|der Kumpel|kanka
n|der Tourismus|turizm
w|unbekannt|bilinmeyen
n|die Vielfalt|çeşitlilik
v|zerstören|yok etmek
w|angenehm|hoş
v|beachten|dikkate almak
v|belegen|kanıtlamak; almak (kurs)
w|daheim|evde
w|digital|dijital
w|einig|hemfikir
v|hinterlassen|geride bırakmak
v|kontrollieren|kontrol etmek
w|quer|çapraz
w|samt|ile birlikte
w|vertraut|tanıdık
v|wetten|bahse girmek
w|derart|öyle, o derece
w|einverstanden|razı
v|erzielen|elde etmek
w|fern|uzak
v|klagen|şikâyet etmek; dava açmak
w|konkret|somut
w|nebenbei|bu arada; yan iş olarak
w|wunderschön|çok güzel
w|blind|kör
w|dauerhaft|kalıcı
w|durchschnittlich|ortalama
v|heiraten|evlenmek
w|historisch|tarihî
w|langfristig|uzun vadeli
v|mitmachen|katılmak
w|passend|uygun
w|schief|eğri
n|die Überwachung|gözetim
n|die Altstadt|eski şehir
w|besorgt|endişeli
n|die Erhöhung|artış
w|hilfreich|yararlı
w|höchst|son derece
w|soeben|az önce
n|die Staatsanwaltschaft|savcılık
v|weichen|çekilmek, yol vermek
n|die Betreuung|bakım, danışmanlık
w|glatt|düz, kaygan
w|jahrelang|yıllarca
n|der Modus|mod
w|schlicht|sade
n|die Vielzahl|çokluk
w|vorerst|şimdilik
w|zustande kommen|gerçekleşmek
n|der Betreiber|işletmeci
n|das Detail|ayrıntı
n|das Fazit|sonuç
v|kennenlernen|tanışmak
w|schuldig|suçlu; borçlu
w|sozusagen|tabiri caizse
v|verstecken|saklamak
w|vorhin|az önce
w|zugunsten|lehine
n|die Dokumentation|belgeleme; belgesel
n|die Einschätzung|değerlendirme
w|exakt|tam
w|finanziell|mali
w|infolge|sonucunda (+ Gen.)
n|der Jahrgang|yaş grubu; dönem
w|schrecklich|korkunç
w|seither|o zamandan beri
w|unklar|belirsiz
w|unterhalb|altında
w|wirtschaftlich|ekonomik
v|aufbauen|kurmak
v|bedienen|hizmet etmek; kullanmak
w|dazwischen|arasında
n|die Erfüllung|yerine getirme
v|erwähnen|bahsetmek
v|klingen|kulağa gelmek
w|neulich|geçenlerde
v|opfern|feda etmek
v|umgeben|çevrelemek
w|ungewöhnlich|olağandışı
n|die Zerstörung|yıkım
w|abseits|uzağında
v|befreien|kurtarmak
v|betreten|girmek (mekâna)
w|dauernd|sürekli
n|der Entwickler|geliştirici
w|erstens|birincisi
w|konsequent|tutarlı
w|kräftig|güçlü
w|lokal|yerel
v|wandern|yürüyüş yapmak
w|einzeln|tek tek
w|enorm|muazzam
w|etliche|epeyce
w|kurzfristig|kısa vadeli
w|mitunter|zaman zaman
w|mächtig|güçlü
w|woanders|başka yerde
n|der Zugriff|erişim
w|zweitens|ikincisi
n|die Bearbeitung|işleme
v|gebrauchen|kullanmak
w|stabil|sağlam
w|vorwiegend|ağırlıklı olarak
w|wahnsinnig|çılgınca
n|die Weiterbildung|ileri eğitim
v|bekämpfen|mücadele etmek
n|die Berichterstattung|haber yapma
v|blicken|bakmak
v|erheben|yükseltmek; toplamak (vergi)
w|erreichbar|ulaşılabilir
w|unendlich|sonsuz
w|unnötig|gereksiz
v|vorliegen|mevcut olmak
n|die Aufstellung|liste; diziliş
v|ausprobieren|denemek
v|benötigen|ihtiyaç duymak
w|binnen|içinde (süre)
w|entschlossen|kararlı
n|die Erhebung|anket; tahsil
w|gewöhnt|alışık
w|herrlich|harika
w|pleite|beş parasız
w|unsicher|emin olmayan
n|das Vorfeld|ön aşama
n|die Allianz|ittifak
w|gemein|kaba, adi
w|genial|dâhice
n|der Konzern|şirketler grubu
n|das Medium|araç; medya
n|die Route|güzergâh
w|schlau|zeki
w|traditionell|geleneksel
w|treu|sadık
v|abwarten|beklemek
n|der Einzelfall|münferit vaka
n|die Episode|bölüm
w|erfreut|memnun
n|der Genuss|zevk
w|heimlich|gizlice
n|die Präsentation|sunum
n|der Rechner|bilgisayar
v|streichen|boyamak; silmek
w|untereinander|kendi aralarında
v|sich wehren|kendini savunmak
w|wissenschaftlich|bilimsel
v|anlegen|yatırım yapmak; kurmak
w|denkbar|düşünülebilir
w|furchtbar|korkunç
w|geradezu|adeta
w|gesetzlich|yasal
w|gewöhnlich|olağan
w|hervorragend|mükemmel
w|illegal|yasa dışı
w|komplex|karmaşık
w|nirgends|hiçbir yerde
v|schieben|itmek
w|südlich|güneyde
w|zeitweise|zaman zaman
n|die Berücksichtigung|dikkate alma
n|der Erhalt|alım; koruma
v|eröffnen|açmak (resmî)
n|die Fotografie|fotoğrafçılık
w|friedlich|barışçıl
w|lebendig|canlı
w|nördlich|kuzeyde
n|die Orientierung|yönelim
w|rechtlich|hukuki
w|vernünftig|makul
v|aufhalten|durdurmak
n|die Datenbank|veritabanı
n|der Datenschutz|veri koruma
n|der Einstieg|giriş, başlangıç
w|erwachsen|yetişkin
w|konstant|sabit
""",
"B2.2": """
n|der Einfluss|etki, nüfuz
n|die Grundlage|temel
n|der Zustand|durum, hal
n|die Abhängigkeit|bağımlılık
n|der Beitrag|katkı; aidat; yazı
n|die Wahrnehmung|algı
n|der Vorgang|süreç, işlem
n|die Einschränkung|kısıtlama
n|die Vereinbarung|anlaşma
n|die Umsetzung|uygulama, hayata geçirme
n|der Schwerpunkt|odak noktası
n|die Haltung|tutum, duruş
n|die Bereitschaft|istekli olma, hazır olma
n|der Rückgang|düşüş, azalma
v|umsetzen|hayata geçirmek|er setzt um · hat umgesetzt
v|hervorheben|vurgulamak|er hebt hervor · hat hervorgehoben
v|einschätzen|değerlendirmek, tahmin etmek|er schätzt ein · hat eingeschätzt
v|ablehnen|reddetmek|er lehnt ab · hat abgelehnt
v|zustimmen|onaylamak, katılmak (+ Dat.)|er stimmt zu · hat zugestimmt
v|widersprechen|itiraz etmek (+ Dat.)|er widerspricht · hat widersprochen
v|sich durchsetzen|sözünü geçirmek; kabul görmek|er setzt sich durch · hat sich durchgesetzt
v|ausgehen|varsaymak (von + Dat.)|er geht aus · ist ausgegangen
v|übernehmen|üstlenmek|er übernimmt · hat übernommen
v|verfügen|sahip olmak (über + Akk.)|er verfügt · hat verfügt
v|bewirken|yol açmak, sağlamak|er bewirkt · hat bewirkt
v|vorkommen|yaşanmak; görünmek|es kommt vor · ist vorgekommen
w|zwangsläufig|kaçınılmaz olarak
w|erheblich|önemli ölçüde
w|weitgehend|büyük ölçüde
w|beziehungsweise|ya da; sırasıyla (bzw.)
w|gegebenenfalls|gerekirse (ggf.)
n|die Absprache|mutabakat, anlaşma
n|der Ausgleich|denge, telafi
n|die Auseinandersetzung|tartışma, çatışma
n|die Behauptung|iddia
n|der Bestandteil|bileşen
n|die Entlastung|yükü hafifletme
n|der Ertrag|getiri, verim
n|die Folgerung|çıkarım
n|der Konsens|uzlaşı
n|die Rahmenbedingung|çerçeve koşul
n|die Rechtfertigung|haklı çıkarma, gerekçe
n|die Tendenz|eğilim
n|der Überblick|genel bakış
n|die Überlegung|düşünce, değerlendirme
n|das Verhältnis|oran; ilişki
n|die Vorhersage|tahmin
n|der Zusammenhalt|dayanışma
v|anerkennen|tanımak, takdir etmek
v|ansprechen|hitap etmek; değinmek
v|aufweisen|göstermek, sergilemek
v|ausgleichen|dengelemek
v|aushandeln|pazarlıkla belirlemek
v|sich bemühen|çaba göstermek
v|benachteiligen|dezavantajlı duruma düşürmek
v|bevorzugen|tercih etmek
v|einbeziehen|dahil etmek
v|einsetzen|kullanmak, görevlendirmek
v|erfordern|gerektirmek
v|gelten als|… olarak kabul edilmek
v|hinnehmen|kabullenmek
v|sich auswirken auf|etkilemek
v|überschätzen|fazla değer vermek
v|unterschätzen|hafife almak
v|vernachlässigen|ihmal etmek
v|vertreten|temsil etmek; savunmak
v|zusammenfassen|özetlemek
w|absehbar|öngörülebilir
w|ausdrücklich|açıkça
w|befristet|süreli
w|folglich|sonuç olarak
w|hinsichtlich|bakımından (+ Gen.)
w|keineswegs|asla, hiç de
w|mittlerweile|artık, bu arada
w|sachlich|nesnel
w|umstritten|tartışmalı
w|vielmehr|daha ziyade
v|zugeben, eingestehen|itiraf etmek, kabul etmek
v|befürworten, sich einsetzen für|savunmak, desteklemek
v|sich leisten können|(maddi olarak) gücü yetmek
v|argumentieren, streiten|iddia etmek, tartışmak
v|steigern, ankurbeln|artırmak, yükseltmek
v|sich verpflichten; begehen|taahhüt etmek, adamak
v|bestätigen|doğrulamak, teyit etmek
v|sich befassen mit, erledigen|ilgilenmek, halletmek
v|leugnen, verweigern|inkâr etmek, reddetmek
v|beseitigen|ortadan kaldırmak, elemek
v|beschäftigen; sich beteiligen|meşgul etmek, katılmak
v|gründen, festlegen|kurmak, tesis etmek
v|erzeugen|üretmek, oluşturmak
v|identifizieren, erkennen|tespit etmek, tanımlamak
v|beinhalten, einbeziehen|içermek, dahil etmek
v|rechtfertigen|gerekçelendirmek
v|überwachen|izlemek, takip etmek
v|überwinden|üstesinden gelmek
v|bewahren, erhalten|korumak, muhafaza etmek
v|fortfahren|devam etmek, ilerlemek
v|verfolgen|peşinden gitmek, sürdürmek
v|sich qualifizieren; einschränken|hak kazanmak, nitelendirmek
v|widerspiegeln; nachdenken|yansıtmak, düşünüp taşınmak
v|betrachten als|saymak, addetmek
v|sich verlassen auf|güvenmek, dayanmak
v|wiederherstellen|eski hâline getirmek
v|behalten, bewahren|elde tutmak, korumak
v|enthüllen, offenbaren|ortaya çıkarmak, açığa vurmak
v|umkehren|tersine çevirmek
v|sich niederlassen; beilegen|yerleşmek, çözüme kavuşturmak
v|ersetzen|yerine koymak
v|leiden|acı çekmek, maruz kalmak
v|neigen, tendieren|eğiliminde olmak
v|eindringlich auffordern|ısrarla teşvik etmek
v|variieren|değişkenlik göstermek
v|bezeugen, miterleben|tanık olmak
v|ergeben, liefern; nachgeben|vermek (sonuç), boyun eğmek
n|die Genauigkeit|doğruluk, isabet
n|der Aspekt|yön, boyut
n|das Bewusstsein|farkındalık
n|die Barriere, das Hindernis|engel
n|die Voreingenommenheit|önyargı, yanlılık
n|die Last, die Belastung|yük, külfet
n|das Engagement, die Verpflichtung|bağlılık, taahhüt
n|die Kontroverse|tartışma, ihtilaf
n|die Effizienz|verimlilik
n|die Betonung|vurgu
n|die Exposition, die Sichtbarkeit|maruz kalma, görünürlük
n|der Rahmen|çerçeve
n|die Initiative|girişim, inisiyatif
n|die Einsicht, der Einblick|içgörü
n|die Integrität|bütünlük, dürüstlük
n|die Haftung|sorumluluk, yükümlülük
n|das Ergebnis|sonuç
n|das Tempo|hız, tempo
n|das Muster|örüntü, kalıp
n|die Perspektive|bakış açısı
n|die Vorliebe, die Präferenz|tercih
n|die Priorität|öncelik
n|der Anteil, das Verhältnis|oran
n|die Ressource|kaynak
n|der Umfang, der Rahmen|kapsam
n|die Bedeutung|önem
n|die Belastung, die Anspannung|gerilim, zorlanma
n|der Übergang|geçiş
n|der Trend|eğilim, trend
w|zugänglich|erişilebilir
w|umfassend|kapsamlı
w|konsistent, folgerichtig|tutarlı
w|entscheidend|çok önemli, kritik
w|anspruchsvoll|zorlayıcı, çok şey isteyen
w|vielfältig|çeşitli, farklı
w|berechtigt, infrage kommend|hak sahibi, uygun
w|übermäßig|aşırı
w|grundlegend|temel
w|innovativ|yenilikçi
w|legitim, rechtmäßig|meşru
w|verpflichtend|zorunlu
w|fortlaufend, laufend|süregelen
w|präzise|kesin, hassas
w|prominent, herausragend|öne çıkan
w|nachfolgend|sonraki
w|verwundbar|savunmasız, kırılgan
w|letztendlich|nihayetinde
p|zur Sprache bringen; großziehen|gündeme getirmek, yetiştirmek
p|absagen|iptal etmek
p|stoßen auf; wirken|rastlamak, izlenim vermek
p|einsparen bei|kısmak, azaltmak
p|abschneiden, trennen|kesmek, bağlantıyı koparmak
p|nachverfolgen, nachhaken|takip etmek, peşini bırakmamak
p|zurückhalten|geri tutmak, çekinmek
p|im Großen und Ganzen|genel olarak
p|angesichts der Tatsache, dass|-diği göz önüne alınırsa
w|daher|dolayısıyla
p|auf lange Sicht|uzun vadede
p|mit dem Ziel|-mek amacıyla
w|oberhalb|üstünde
n|die Pressemitteilung|basın bülteni
v|reiten|ata binmek
v|sinken|düşmek, batmak
w|unangenehm|nahoş
v|verschaffen|sağlamak
w|verzweifelt|umutsuz
w|vorwärts|ileri
n|der Asylbewerber|sığınmacı
n|die Ausrichtung|yönelim
w|betrunken|sarhoş
n|die Bezahlung|ödeme
n|die Digitalisierung|dijitalleşme
v|finanzieren|finanse etmek
w|flach|düz
w|gewiss|kesin
w|grob|kaba
v|senken|düşürmek
v|zulassen|izin vermek
v|antreten|başlamak (göreve); yarışmak
n|der Arbeitsmarkt|iş piyasası
v|brennen|yanmak
w|circa|yaklaşık
n|die Elite|seçkinler
v|erwerben|edinmek
w|fröhlich|neşeli
w|logisch|mantıklı
n|die Migration|göç
n|die Partnerschaft|ortaklık
w|vorübergehend|geçici
w|weitaus|çok daha
v|zielen auf|hedeflemek
v|besorgen|temin etmek
v|fliehen|kaçmak
w|merkwürdig|tuhaf
n|der Notfall|acil durum
w|schriftlich|yazılı
v|verdanken|borçlu olmak (minnet)
w|zeitlich|zamansal
v|anhören|dinlemek
w|annähernd|yaklaşık
w|anwesend|mevcut, hazır
v|aufstellen|dikmek; kurmak
n|die Auswertung|değerlendirme
v|begreifen|kavramak
w|beruflich|mesleki
v|buchen|rezervasyon yapmak
v|erben|miras almak
w|geistig|zihinsel
n|der Mindestlohn|asgari ücret
v|versorgen|bakmak, sağlamak
v|verursachen|sebep olmak
v|ausdrücken|ifade etmek
v|errichten|inşa etmek
w|fähig|yetenekli
w|gänzlich|tamamen
w|primär|öncelikle
n|die Sanierung|yenileme
w|stetig|sürekli
v|stürzen|düşmek
w|unwahrscheinlich|olası değil
n|das Vorjahr|önceki yıl
v|ausmachen|kapatmak; oluşturmak
w|effektiv|etkili
w|individuell|bireysel
w|legal|yasal
w|mobil|mobil
w|unglücklich|mutsuz
w|verlegen|mahcup
w|weich|yumuşak
w|zulässig|izin verilen
w|zwingend|zorunlu
w|zwischendurch|arada bir
w|allmählich|yavaş yavaş
w|berühmt|ünlü
v|bremsen|fren yapmak
v|demonstrieren|gösteri yapmak
w|identisch|aynı
w|riesig|devasa
w|sinnlos|anlamsız
w|sorgfältig|özenli
v|strafen|cezalandırmak
v|werben|reklam yapmak
n|die Zulassung|ruhsat; kabul
n|die Aktivität|faaliyet
w|aufrecht|dik
v|sich begeben|gitmek
v|beherrschen|hâkim olmak
w|durcheinander|karmakarışık
w|indirekt|dolaylı
w|körperlich|bedensel
v|locken|cezbetmek
w|prinzipiell|prensipte
n|der Riss|çatlak
w|umgehend|derhal
v|verletzen|yaralamak
n|die Zielgruppe|hedef kitle
w|zugrunde liegen|temelinde yatmak
n|der Abstieg|iniş, düşüş
n|der Anleger|yatırımcı
n|die Bekämpfung|mücadele
v|besprechen|görüşmek
w|brav|uslu
n|die Formulierung|ifade
w|hässlich|çirkin
v|jagen|avlamak
n|die Kreativität|yaratıcılık
v|lauten|olmak (metin)
w|sportlich|sportif
w|tödlich|ölümcül
w|unheimlich|ürkütücü; aşırı
w|verkehrt|ters
n|die Diskriminierung|ayrımcılık
v|einnehmen|almak (ilaç); kazanmak
w|männlich|erkek
w|sanft|yumuşak
n|die Ankündigung|duyuru
n|der Auftakt|başlangıç
v|ausfallen|iptal olmak
v|beten|dua etmek
w|brutal|vahşi
v|sich eignen|uygun olmak
w|frühzeitig|erkenden
n|die Kriminalität|suç oranı
n|das Potenzial|potansiyel
w|problematisch|sorunlu
n|die Recherche|araştırma
w|voraussichtlich|muhtemelen
v|vornehmen|yapmak; niyet etmek
w|zukünftig|gelecekteki
w|anonym|anonim
v|ausführen|yürütmek
n|das Bedürfnis|ihtiyaç
v|entgehen|kaçmak, gözden kaçmak
n|die Innovation|yenilik
w|nebenan|yan tarafta
v|spazieren gehen|gezinti yapmak
w|tagsüber|gündüz
v|benehmen (sich)|davranmak
v|entnehmen|çıkarmak, anlamak
w|glücklicherweise|neyse ki
n|die Mobilität|hareketlilik
n|die Präsenz|varlık
v|tauchen|dalmak
v|verbrennen|yakmak
v|verleihen|ödünç vermek; ödül vermek
n|der Verlierer|kaybeden
v|verweisen auf|işaret etmek
v|wecken|uyandırmak
v|aussuchen|seçmek
w|einsam|yalnız
v|eintreten|girmek; meydana gelmek
w|gewaltig|muazzam
n|die Investition|yatırım
v|sich orientieren|yönelmek
v|sperren|kapatmak, bloke etmek
w|staatlich|devlete ait
n|die Uhrzeit|saat
n|die Umstellung|geçiş, değişiklik
v|zusehen|seyretmek
v|bearbeiten|işlemek, düzenlemek
v|gefährden|tehlikeye atmak
w|gepflegt|bakımlı
w|hintereinander|arka arkaya
n|der Klimaschutz|iklim koruma
n|die Privatsphäre|mahremiyet
w|realistisch|gerçekçi
n|die Schaffung|oluşturma
w|skeptisch|şüpheci
w|vergeblich|boşuna
w|weiblich|kadın
w|wertvoll|değerli
w|westlich|batıda
w|wirksam|etkili
v|überfallen|saldırmak, soymak
w|absurd|saçma
n|die Akzeptanz|kabul
v|besetzen|işgal etmek; doldurmak
v|drängen|sıkıştırmak, zorlamak
v|sich engagieren|kendini adamak
w|fraglich|şüpheli
w|rückwärts|geriye
n|die Tragödie|trajedi
v|abstimmen|oylamak
n|der Ausschluss|dışlama
w|drüben|karşıda
w|durchgehend|kesintisiz
v|entkommen|kaçmak
v|erlassen|çıkarmak (yasa); bağışlamak
v|ernähren|beslemek
v|erschaffen|yaratmak
w|menschlich|insani
w|psychisch|ruhsal
v|realisieren|gerçekleştirmek
w|vergangen|geçmiş
w|fällig|vadesi gelmiş
w|gegenwärtig|şimdiki
w|heilig|kutsal
w|klassisch|klasik
v|korrigieren|düzeltmek
v|lenken|yönlendirmek
w|sympathisch|sempatik
w|unerwartet|beklenmedik
w|ausnahmsweise|bir defalık
n|die Ermittlung|soruşturma
v|gönnen|layık görmek
w|intern|iç
w|künstlich|yapay
v|leuchten|parlamak
w|lose|gevşek
w|naiv|saf
n|der Rechtsstaat|hukuk devleti
v|ruhen|dinlenmek
w|stundenlang|saatlerce
w|ungern|isteksizce
w|unschuldig|masum
v|unterliegen|tabi olmak; yenilmek
w|vereinzelt|tek tük
v|ahnen|sezmek
v|angreifen|saldırmak
v|erobern|fethetmek
w|geheim|gizli
w|harmlos|zararsız
w|intelligent|zeki
n|die Lebensqualität|yaşam kalitesi
v|loswerden|kurtulmak
w|nebeneinander|yan yana
n|das Selbstbewusstsein|özgüven
v|unterrichten|ders vermek
v|vernichten|yok etmek
w|verschlossen|kapalı; içine kapanık
n|das Weltbild|dünya görüşü
w|wörtlich|kelimesi kelimesine
w|östlich|doğuda
n|die Abgrenzung|ayrım
v|sich aufregen|sinirlenmek
v|beleidigen|hakaret etmek
v|bestreiten|inkâr etmek; karşılamak
v|blockieren|engellemek
v|ergreifen|yakalamak; almak (önlem)
v|hinzufügen|eklemek
w|liebevoll|sevgi dolu
w|mies|berbat
v|mischen|karıştırmak
w|nüchtern|ayık; nesnel
w|optisch|görsel
v|strahlen|ışıldamak
n|die Thematik|konu
n|die Unterscheidung|ayrım
n|der Unterstützer|destekçi
v|abhalten|düzenlemek; engellemek
w|anderswo|başka yerde
v|austauschen|değiş tokuş etmek
w|ausverkauft|tükenmiş
w|beiseite|bir kenara
w|dramatisch|dramatik
w|erwünscht|istenen
w|gesamt|toplam
w|neutral|tarafsız
w|platt|düz; şaşkın
v|stützen|desteklemek
w|widerlich|iğrenç
n|die Attacke|saldırı
n|der Austritt|çıkış, ayrılma
n|die Befragung|sorgu, anket
w|beliebig|herhangi
w|eigen|kendi
n|das Feuerwerk|havai fişek
v|garantieren|garanti etmek
w|gemischt|karışık
n|die Publikation|yayın
w|schräg|eğik
n|der Terrorismus|terörizm
w|unzufrieden|memnuniyetsiz
v|verarbeiten|işlemek
v|abschalten|kapatmak
n|die Auszeit|mola
w|diesbezüglich|bununla ilgili
n|die Erstellung|oluşturma
n|die Fertigstellung|tamamlama
v|herrschen|hüküm sürmek
w|neuerdings|son zamanlarda
w|radikal|radikal
n|die Relevanz|önem
w|vorzeitig|erken
v|absetzen|indirmek; görevden almak
w|allerlei|türlü türlü
v|angehören|ait olmak
v|anhalten|durmak
n|die Auslegung|yorum
v|ausrichten|iletmek; düzenlemek
v|belasten|yük olmak
v|einsehen|kabul etmek, anlamak
v|flüchten|kaçmak
n|der Lebensraum|yaşam alanı
w|verwickelt|karışık; bulaşmış
v|verzeichnen|kaydetmek
n|die Zugehörigkeit|aidiyet
v|entfallen|düşmek, iptal olmak
w|gleichfalls|aynı şekilde
n|die Inspiration|ilham
n|die Leistungsfähigkeit|verimlilik
v|ablegen|çıkarmak; vermek (sınav)
v|absolvieren|bitirmek
n|der Anwohner|bölge sakini
v|erfinden|icat etmek
w|frech|arsız
n|die Immobilie|gayrimenkul
n|die Rendite|getiri
w|schlank|ince
w|steil|dik
n|der Stellenwert|önem
v|veranstalten|düzenlemek
w|allenfalls|olsa olsa
v|ausbauen|genişletmek
v|beibehalten|korumak
w|bescheiden|mütevazı
w|demokratisch|demokratik
w|erfolglos|başarısız
n|die Lebensweise|yaşam tarzı
w|nacheinander|birbiri ardına
v|reinigen|temizlemek
v|stehlen|çalmak
w|transparent|şeffaf
v|verwirklichen|gerçekleştirmek
w|zweifellos|şüphesiz
n|der Ansprechpartner|irtibat kişisi
v|benennen|adlandırmak
v|bestrafen|cezalandırmak
n|der Entschluss|karar
v|erteilen|vermek (izin, ders)
w|grausam|zalim
w|mühsam|zahmetli
n|die Registrierung|kayıt
w|unverzüglich|gecikmeksizin
n|die Vorgehensweise|yöntem
v|abschaffen|kaldırmak
n|das Darlehen|kredi, borç
n|die Insolvenz|iflas
v|nachfragen|sormak
v|sich nähern|yaklaşmak
w|selbständig|bağımsız
w|unerträglich|dayanılmaz
n|der Zusammenschluss|birleşme
v|ausreichen|yetmek
v|ausscheiden|elenmek; ayrılmak
n|die Ausschreibung|ihale; ilan
n|der Ausstieg|çıkış
w|auswendig|ezbere
n|die Gleichberechtigung|eşit haklar
w|moralisch|ahlaki
w|schmerzhaft|acı verici
w|ungerecht|haksız
w|verdächtig|şüpheli
v|vereinbaren|kararlaştırmak
w|versehentlich|yanlışlıkla
v|zittern|titremek
w|abwechselnd|dönüşümlü
n|der Auftraggeber|işveren, müşteri
v|beschleunigen|hızlandırmak
v|besiegen|yenmek
v|sich erholen|dinlenmek, iyileşmek
n|die Festplatte|sabit disk
v|genügen|yetmek
n|die Intensität|yoğunluk
w|nutzlos|işe yaramaz
w|optimistisch|iyimser
w|romantisch|romantik
""",
"C1.1": """
n|die Annahme|varsayım; kabul
n|der Ansatz|yaklaşım
n|die Tragweite|önem, kapsam
n|der Sachverhalt|olay, durum (resmî)
n|die Befugnis|yetki
n|die Beeinträchtigung|olumsuz etki, engel
n|der Verdacht|şüphe
n|die Rücksicht|saygı, göz önüne alma
n|die Anerkennung|tanınma; takdir
n|der Missbrauch|kötüye kullanım
n|die Schwachstelle|zayıf nokta, açık
n|die Bedrohung|tehdit
n|der Aufschwung|yükseliş, canlanma
v|beanspruchen|talep etmek; yormak|er beansprucht · hat beansprucht
v|erörtern|tartışmak, ele almak|er erörtert · hat erörtert
v|veranlassen|sebep olmak; yaptırmak|er veranlasst · hat veranlasst
v|beheben|gidermek (arıza)|er behebt · hat behoben
v|beimessen|(önem) atfetmek|er misst bei · hat beigemessen
v|unterstellen|isnat etmek, ima etmek|er unterstellt · hat unterstellt
v|sich erweisen|ortaya çıkmak (als)|er erweist sich · hat sich erwiesen
v|abwägen|ölçüp biçmek|er wägt ab · hat abgewogen
v|einräumen|kabul etmek (hata)|er räumt ein · hat eingeräumt
v|anstreben|hedeflemek|er strebt an · hat angestrebt
v|beruhen|dayanmak (auf + Dat.)|es beruht · hat beruht
v|bewerkstelligen|becermek, başarmak|er bewerkstelligt · hat bewerkstelligt
w|maßgeblich|belirleyici
w|nachhaltig|sürdürülebilir; kalıcı
w|ausschlaggebend|belirleyici, kesin
w|vorläufig|geçici
w|stichhaltig|sağlam (argüman)
n|die Abwägung|tartma, değerlendirme
n|der Anreiz|teşvik
n|die Ausprägung|biçim, derece
n|die Bewältigung|üstesinden gelme
n|die Darlegung|açıklama, sunuş
n|der Eingriff|müdahale
n|die Errungenschaft|kazanım
n|das Gefälle|eşitsizlik, fark
n|der Grundsatz|ilke
n|die Instanz|merci
n|die Rechenschaft|hesap verme
n|die Teilhabe|(toplumsal) katılım
n|der Vorbehalt|çekince
n|die Zumutung|kabul edilemez talep
n|der Zwiespalt|ikilem
v|abgrenzen|sınırlarını belirlemek
v|anfechten|itiraz etmek (hukuki)
v|anregen|teşvik etmek, önermek
v|ausschöpfen|sonuna kadar kullanmak
v|bekräftigen|teyit etmek
v|beleuchten|ele almak, aydınlatmak
v|einleiten|başlatmak
v|entkräften|çürütmek
v|erschließen|açmak, keşfetmek
v|gewähren|tanımak, vermek (hak)
v|herleiten|türetmek
v|relativieren|göreceli hale getirmek
v|sich niederschlagen in|-e yansımak
v|veranschaulichen|somutlaştırmak
v|verdeutlichen|netleştirmek
v|wahrnehmen|algılamak; (hakkı) kullanmak
w|abwegig|yersiz, saçma
w|angesichts|karşısında (+ Gen.)
w|beträchtlich|kayda değer
w|eingehend|ayrıntılı
w|gleichwohl|buna rağmen
w|hinfällig|geçersiz
w|infolgedessen|bunun sonucunda
w|mithin|dolayısıyla
w|nachweislich|kanıtlanabilir şekilde
w|schlüssig|tutarlı
w|unabdingbar|vazgeçilmez
w|zwecks|amacıyla (+ Gen.)
v|aufgeben, verlassen|terk etmek, vazgeçmek
v|vollbringen, erreichen|başarmak, tamamlamak
v|genehmigen, billigen|onaylamak
v|versichern, zusichern|temin etmek, güvence vermek
v|zuschreiben|atfetmek, bağlamak
v|klären, verdeutlichen|netleştirmek
v|umfassen, bestehen aus|kapsamak, oluşmak
v|konfrontieren, sich stellen|yüzleşmek, karşı karşıya gelmek
v|bestehen aus|-den oluşmak
v|konsultieren, sich beraten|danışmak
v|vermitteln, übermitteln|iletmek, aktarmak
v|eindämmen, zügeln|dizginlemek, sınırlamak
v|delegieren|yetki devretmek
v|offenlegen|ifşa etmek, açıklamak
v|entlassen; abtun|reddetmek, işten çıkarmak
v|näher ausführen|ayrıntılandırmak
v|ertragen, aushalten|dayanmak, katlanmak
v|überschreiten|aşmak, geçmek
v|ausschließen|dışlamak, hariç tutmak
v|ausbeuten, ausnutzen|sömürmek, istismar etmek
v|aussetzen; aufdecken|maruz bırakmak, ifşa etmek
v|erleichtern|kolaylaştırmak
v|herausfinden, verstehen|çözmek, anlamak
v|regieren, bestimmen|yönetmek, belirlemek
v|zögern|tereddüt etmek
v|andeuten, implizieren|ima etmek
v|auferlegen, aufzwingen|dayatmak, yüklemek
v|bestehen auf|ısrar etmek
v|inspirieren|ilham vermek
v|integrieren|entegre etmek, bütünleştirmek
v|sich einmischen, stören|müdahale etmek, karışmak
v|interpretieren, deuten|yorumlamak
v|eingreifen|araya girmek, müdahale etmek
v|manipulieren|manipüle etmek, yönlendirmek
v|modifizieren, ändern|değiştirmek, uyarlamak
v|verhandeln|müzakere etmek, pazarlık yapmak
v|skizzieren, umreißen|ana hatlarıyla belirtmek
v|überreden|ikna etmek
v|anwerben, einstellen|işe almak
v|unterlassen, sich enthalten|kaçınmak, geri durmak
v|verstärken|pekiştirmek, güçlendirmek
v|entlasten, lindern|rahatlatmak, hafifletmek
v|machen zu; erbringen|hâle getirmek, sunmak
v|ähneln|benzemek
v|beschränken|kısıtlamak
v|abrufen, zurückholen|geri almak, geri getirmek
v|stärken|güçlendirmek
v|streben|çabalamak, gayret etmek
v|unterdrücken|bastırmak
v|maßschneidern, anpassen|özel olarak uyarlamak
v|verwandeln|dönüştürmek
v|durchlaufen, sich unterziehen|geçirmek, maruz kalmak
v|untergraben|zayıflatmak, baltalamak
v|überprüfen|doğrulamak
v|zurückziehen, abheben|geri çekmek, çekilmek
v|standhalten|dayanmak, karşı koymak
n|die Rechenschaftspflicht|hesap verebilirlik
n|die Nachwirkungen (Pl.)|sonrasında yaşananlar
n|die Gegenreaktion|sert tepki
n|der Maßstab, der Richtwert|kıyas ölçütü
n|der Durchbruch|çığır açan gelişme
n|die Glaubwürdigkeit|güvenilirlik
n|das Dilemma|ikilem
n|die Störung, der Umbruch|kesinti, altüst oluş
n|das Fachwissen, die Expertise|uzmanlık
n|die Einmischung|müdahale, karışma
n|der Hebel, der Einfluss|kaldıraç gücü, nüfuz
n|die Wahrscheinlichkeit|olasılık
n|der Meilenstein|dönüm noktası
n|die Dynamik, der Schwung|ivme
n|das Motiv|güdü, saik
n|die Aufsicht; das Versehen|gözetim, gözden kaçırma
n|der Präzedenzfall|emsal
n|die Prämisse|öncül, dayanak
n|die Verbreitung, die Häufigkeit|yaygınlık
n|die Argumentation|akıl yürütme
n|der Rest|geri kalan
n|die genaue Prüfung|yakın inceleme
n|der Überschuss|fazlalık, artı değer
n|die Schwelle|eşik
n|die Transparenz|şeffaflık
n|der Umsatz; die Fluktuation|devir hızı, ciro
n|die Unsicherheit|belirsizlik
n|die Gültigkeit|geçerlilik
w|reichlich|bol, bereketli
w|nachteilig, ungünstig|olumsuz, ters
w|willkürlich|keyfi
w|vorteilhaft|faydalı
w|voreingenommen|önyargılı, taraflı
w|kohärent, schlüssig|tutarlı, bağdaşık
w|überzeugend|ikna edici, sürükleyici
w|kompetent|yetkin
w|absichtlich, bewusst|kasıtlı, bilinçli
w|ausführlich, aufwendig|ayrıntılı, özenli
w|offenkundig|besbelli
w|machbar|yapılabilir
w|fehlerhaft|kusurlu
w|unmittelbar bevorstehend|çok yakın, an meselesi
w|unzureichend|yetersiz
w|inklusiv|kapsayıcı
w|widersprüchlich|tutarsız
w|unvermeidlich|kaçınılmaz
w|einflussreich|etkili, nüfuzlu
w|faszinierend|merak uyandıran
w|irrelevant|konu dışı, ilgisiz
w|geringfügig, marginal|marjinal, sınırda
w|irreführend|yanıltıcı
w|bemerkenswert|dikkate değer
w|spürbar, merklich|fark edilir
w|veraltet|modası geçmiş, kullanımdan kalkmış
w|überholt|güncelliğini yitirmiş
w|überwältigend|ezici, bunaltıcı
w|hartnäckig, anhaltend|inatçı, kalıcı
w|plausibel|makul, inandırıcı
w|weit verbreitet|yaygın
w|verhältnismäßig|orantılı
w|fragwürdig|kuşkulu
w|widerwillig|isteksiz
w|streng, gründlich|titiz, sıkı
w|robust|sağlam, güçlü
w|knapp|kıt
w|unkompliziert|dolaysız, anlaşılır
w|anfällig|duyarlı, açık (etkiye)
w|gründlich|etraflı, derinlemesine
w|einstimmig|oybirliğiyle
w|beispiellos|eşi görülmemiş
w|vielseitig|çok yönlü
w|tragfähig, realisierbar|uygulanabilir
w|wohl, möglicherweise|tartışmalı olarak, muhtemelen
w|insbesondere|özellikle, dikkat çekici biçimde
w|dadurch|böylece
p|abbrechen, aussteigen|bırakmak, ayrılmak
p|in Rückstand geraten|geri kalmak
p|weitergeben|aktarmak, devretmek
p|mitbekommen, aufgreifen|fark etmek, yakalamak
p|regeln, klären|çözmek, düzene sokmak
p|herausragen|göze çarpmak
p|zurücktreten|görevden çekilmek
w|wenn auch|her ne kadar öyle olsa da
p|alles in allem|her şey göz önüne alındığında
p|tatsächlich, eigentlich|aslına bakılırsa
p|es versteht sich von selbst|söylemeye gerek yok ki
p|geschweige denn|bırakın -i, şöyle dursun
p|vorausgesetzt, dass|şu şartla ki
p|vorbehaltlich|-e tabi olarak
p|einfach ausgedrückt|basitçe söylemek gerekirse
""",
"C1.2": """
n|die Gepflogenheit|alışkanlık, teamül
n|der Einwand|itiraz
n|die Zuständigkeit|yetki alanı
n|die Wechselwirkung|etkileşim
n|der Spielraum|hareket alanı, esneklik
n|das Anliegen|istek, mesele
n|der Werdegang|kariyer geçmişi
n|die Gratwanderung|ince çizgide yürümek
n|die Nachfrage|talep (piyasa)
n|das Ausmaß|boyut, ölçek
n|der Nachdruck|vurgu, ısrar
n|die Hürde|engel
n|der Kompromiss|uzlaşma
v|bemängeln|kusur bulmak|er bemängelt · hat bemängelt
v|sich herausstellen|ortaya çıkmak|es stellt sich heraus · hat sich herausgestellt
v|nachgehen|peşine düşmek, takip etmek|er geht nach · ist nachgegangen
v|zurückgreifen|başvurmak (auf + Akk.)|er greift zurück · hat zurückgegriffen
v|entgegenwirken|karşı koymak (+ Dat.)|er wirkt entgegen · hat entgegengewirkt
v|vorbeugen|önlemek (+ Dat.)|er beugt vor · hat vorgebeugt
v|in Kauf nehmen|göze almak|er nimmt in Kauf · hat in Kauf genommen
v|sich bewähren|kendini kanıtlamak|es bewährt sich · hat sich bewährt
v|beeinträchtigen|olumsuz etkilemek|er beeinträchtigt · hat beeinträchtigt
v|hinterfragen|sorgulamak|er hinterfragt · hat hinterfragt
v|aufgreifen|ele almak (konu)|er greift auf · hat aufgegriffen
w|unumgänglich|kaçınılmaz
w|zweckmäßig|amaca uygun
w|einschlägig|(alanla) ilgili
w|zeitnah|kısa süre içinde
w|ohnehin|zaten
n|die Abhilfe|çare
n|der Anlass|vesile, sebep
n|die Befürchtung|endişe
n|die Einbuße|kayıp
n|das Gutachten|bilirkişi raporu
n|der Handlungsbedarf|harekete geçme gereği
n|die Kehrseite|olumsuz taraf
n|das Missverhältnis|orantısızlık
n|die Nachsicht|hoşgörü
n|das Versäumnis|ihmal
n|die Weichenstellung|yön belirleme
n|die Zurückhaltung|çekingenlik, ölçülülük
v|anknüpfen an|üzerine inşa etmek
v|beanstanden|kusur bulmak, itiraz etmek
v|beherzigen|(öğüdü) dikkate almak
v|bekunden|ifade etmek
v|dulden|göz yummak
v|einbüßen|kaybetmek
v|entgegenkommen|uzlaşmak, yardımcı olmak
v|erachten|saymak, addetmek
v|ergründen|derinlemesine araştırmak
v|sich erübrigen|gereksiz hale gelmek
v|gutheißen|onaylamak
v|hervorrufen|neden olmak
v|sich vergewissern|emin olmak
v|verankern|yerleştirmek, güvenceye almak
v|vorenthalten|esirgemek
v|sich zuspitzen|kızışmak
w|bisweilen|zaman zaman
w|dergestalt|öyle ki
w|eigens|özellikle, sırf
w|fortan|bundan böyle
w|geflissentlich|kasten
w|nichtsdestotrotz|yine de
w|sinngemäß|anlam olarak
w|tendenziell|eğilim olarak
w|unstrittig|tartışmasız
w|vorrangig|öncelikli olarak
w|zuweilen|bazen
v|ansammeln, anhäufen|birikmek, biriktirmek
v|lindern|hafifletmek, azaltmak
v|zuweisen, bereitstellen|tahsis etmek, ayırmak
v|zusammenarbeiten|iş birliği yapmak
v|zwingen|zorlamak, mecbur bırakmak
v|zusammenstellen|derlemek
v|verbergen|gizlemek, saklamak
v|entsprechen; korrespondieren|karşılık gelmek, yazışmak
v|kritisieren|eleştirmek
v|pflegen, kultivieren|geliştirmek, yetiştirmek
v|widmen|adamak, tahsis etmek
v|aufschieben|ertelemek
v|bezeichnen, bedeuten|belirtmek, işaret etmek
v|ableiten, gewinnen|türetmek, elde etmek
v|abschrecken|caydırmak
v|ersinnen, entwerfen|tasarlamak, kurgulamak
v|verringern, abnehmen|azalmak, küçültmek
v|entmutigen, abraten|caydırmak, cesaretini kırmak
v|verdrängen, vertreiben|yerinden etmek
v|entsorgen|elden çıkarmak, bertaraf etmek
v|auseinandergehen, abweichen|ayrılmak, sapmak
v|betonen|vurgulamak
v|mit sich bringen|gerektirmek, beraberinde getirmek
v|übertreiben|abartmak
v|erfüllen|yerine getirmek, karşılamak
v|behindern|engellemek
v|neigen zu|eğilim göstermek
v|herbeiführen, auslösen|yol açmak, teşvik etmek
v|hemmen|engellemek, ketlemek
v|mildern, abschwächen|hafifletmek, azaltmak
v|beaufsichtigen|denetlemek, gözetmek
v|übersehen|gözden kaçırmak, göz yummak
v|fortbestehen, beharren|ısrar etmek, sürüp gitmek
v|genau bestimmen|tam olarak belirlemek
v|priorisieren|önceliklendirmek
v|quantifizieren|nicelleştirmek, sayısallaştırmak
v|verfeinern|inceltmek, iyileştirmek
v|überarbeiten|gözden geçirmek, revize etmek
v|vereinfachen|basitleştirmek
v|herrühren von|-den kaynaklanmak
v|validieren, bestätigen|doğrulamak, geçerli kılmak
v|schwächen|zayıflatmak
n|die Widrigkeit|zorluk, sıkıntı
n|die Mehrdeutigkeit|belirsizlik, muğlaklık
n|der Widerspruch|çelişki
n|das Kriterium|ölçüt
n|die Diskrepanz|tutarsızlık, uyuşmazlık
n|die Ungleichheit|eşitsizlik, fark
n|das Bestreben|çaba, girişim
n|die Machbarkeit|yapılabilirlik
n|das Hindernis|engel
n|die Implikation, die Folge|çıkarım, doğuracağı sonuç
n|die Inkonsistenz|tutarsızlık
n|das Missverständnis, der Irrglaube|yanlış kanı
n|die Nuance|nüans, ince ayrım
n|die Beharrlichkeit|azim, süreklilik
n|die Falle, der Fallstrick|tuzak, olası hata
n|die Plausibilität|inandırıcılık
n|die Kompetenz, die Fertigkeit|yetkinlik
n|das Widerstreben|isteksizlik
n|die Resilienz, die Widerstandskraft|dayanıklılık, direnç
n|der Rückschlag|aksilik, geri adım
n|der Mangel, das Defizit|eksiklik
n|die Dringlichkeit|aciliyet
n|die Tragfähigkeit|yaşayabilirlik, uygulanabilirlik
w|mehrdeutig|belirsiz, çift anlamlı
w|auffällig|göze çarpan
w|umständlich, schwerfällig|hantal, kullanışsız
w|schädlich|zararlı
w|zweifelhaft|şüpheli
w|herausragend, bedeutend|seçkin, önde gelen
w|erschöpfend, lückenlos|çok kapsamlı, eksiksiz
w|schwankend|dalgalanan
w|vernachlässigbar|ihmal edilebilir
w|allgegenwärtig|her yere yayılmış
w|vorherrschend|baskın
w|überflüssig|gereksiz, fazlalık
w|widerstandsfähig|dirençli
w|unvoreingenommen|tarafsız
p|nachholen|açığını kapatmak
p|zurückgreifen auf|-den yararlanmak
p|eingrenzen|daraltmak, elemek
p|sich entscheiden für|-i tercih etmek
p|schrittweise abschaffen|kademeli olarak kaldırmak
p|sich halten an|bağlı kalmak
p|was mich betrifft|bana kalırsa
p|auf Kosten von|-in pahasına
p|im Gegensatz zu|-in aksine
p|um … willen|-in hatırına, uğruna
p|im Zuge von, nach|-in ardından
p|insofern als|-diği ölçüde
p|mit der Begründung, dass|-gerekçesiyle
p|unabhängig von|-e bakılmaksızın
p|bis zu einem gewissen Grad|bir dereceye kadar
p|in Bezug auf|-e ilişkin
""",
"C2.1": """
n|die Befangenheit|taraflılık; çekingenlik
n|der Duktus|üslup
n|die Zwickmühle|ikilem, çıkmaz
n|der Hintergedanke|art niyet
n|die Gemengelage|karmaşık durum
n|der Schachzug|(taktik) hamle
n|die Stellungnahme|görüş bildirimi
n|der Sinneswandel|fikir değişikliği
n|die Fahrlässigkeit|ihmal, dikkatsizlik
n|das Unterfangen|(riskli) girişim
v|anprangern|kınamak, teşhir etmek|er prangert an · hat angeprangert
v|beschönigen|olduğundan iyi göstermek|er beschönigt · hat beschönigt
v|verharmlosen|önemsizmiş gibi göstermek|er verharmlost · hat verharmlost
v|ausloten|derinlemesine yoklamak|er lotet aus · hat ausgelotet
v|untermauern|(kanıtla) desteklemek|er untermauert · hat untermauert
v|sich anbahnen|belirmek, yaklaşmak|es bahnt sich an · hat sich angebahnt
v|beipflichten|hak vermek (+ Dat.)|er pflichtet bei · hat beigepflichtet
v|vereiteln|boşa çıkarmak|er vereitelt · hat vereitelt
v|erwägen|göz önüne almak|er erwägt · hat erwogen
v|ins Gewicht fallen|önem taşımak|es fällt ins Gewicht · ist ins Gewicht gefallen
v|auf der Hand liegen|apaçık olmak|es liegt auf der Hand · hat auf der Hand gelegen
w|unverblümt|açık sözlü, lafı dolandırmadan
w|eklatant|bariz, göze batan
w|ungeachtet|-e rağmen (+ Gen.)
w|tunlichst|mümkün olduğunca
w|mitnichten|hiç de değil
w|gewissermaßen|bir bakıma
n|die Ambivalenz|ikircikli duygu
n|der Anachronismus|anakronizm
n|die Arglist|hile, kurnazlık
n|die Besonnenheit|soğukkanlılık
n|der Einschnitt|dönüm noktası, kesinti
n|die Geringschätzung|küçümseme
n|das Hirngespinst|hayal ürünü
n|die Kurzsichtigkeit|dar görüşlülük; miyopi
n|die Nachlässigkeit|özensizlik
n|die Redlichkeit|dürüstlük
n|der Rückschluss|çıkarım
n|die Selbstgefälligkeit|kendini beğenmişlik
n|die Spitzfindigkeit|kılı kırk yarma
n|der Trugschluss|yanılgı
n|die Verklärung|idealize etme
v|abwiegeln|geçiştirmek
v|anzweifeln|şüpheyle karşılamak
v|aufoktroyieren|dayatmak
v|ausufern|kontrolden çıkmak
v|beschwichtigen|yatıştırmak
v|brandmarken|damgalamak
v|sich entziehen|kaçınmak (+ Dat.)
v|erodieren|aşınmak
v|frönen|düşkün olmak (+ Dat.)
v|hadern mit|kabullenememek
v|kaschieren|gizlemek
v|monieren|eleştirmek
v|unterminieren|baltalamak
v|vereinnahmen|kendine mal etmek
v|zermürben|yıpratmak
w|akribisch|titiz
w|beiläufig|laf arasında
w|dezidiert|kesin, kararlı
w|fadenscheinig|inandırıcı olmayan
w|hanebüchen|akıl almaz
w|inhärent|doğasında olan
w|latent|gizli, örtük
w|perfide|sinsi
w|subtil|ince, zarif
w|unumstößlich|değiştirilemez
w|verbrämt|örtülü, süslenmiş
w|zögerlich|tereddütlü
n|die Abgeklärtheit|olgunluk, soğukkanlılık
n|der Anflug|hafif iz, belirti
n|die Beflissenheit|aşırı gayretkeşlik
n|die Behäbigkeit|ağırkanlılık
n|die Gepflogenheiten|teamüller, adetler
n|das Gebot|buyruk; teklif
n|die Häme|kötü niyetli alay
n|der Kniefall|boyun eğme
n|die Nonchalance|umursamazlık
n|die Preisgabe|ifşa; teslim etme
n|der Schlendrian|üstünkörülük, gevşeklik
n|die Unbill|haksızlık, sıkıntı
n|die Vehemenz|şiddet, ateşlilik
n|der Zwist|anlaşmazlık
v|ahnden|cezalandırmak
v|bezichtigen|suçlamak (+ Gen.)
v|darben|yoksulluk çekmek
v|erheischen|gerektirmek
v|feilschen|pazarlık etmek
v|hintertreiben|gizlice engellemek
v|kokettieren mit|-le flört etmek, oynamak
v|lancieren|piyasaya sürmek, yaymak
v|obliegen|görevi olmak (+ Dat.)
v|nachkommen|yerine getirmek (+ Dat.)
v|sich anschicken|-meye hazırlanmak
v|verbürgen|kefil olmak, garanti etmek
v|verquicken|birbirine karıştırmak
w|ambitioniert|hırslı
w|apodiktisch|kesin, tartışmasız
w|behände|çevik
w|blauäugig|saf, safdil
w|explizit|açıkça
w|famos|harika
w|halbherzig|gönülsüz
w|kryptisch|anlaşılması güç
w|landläufig|yaygın kabul gören
w|unbotmäßig|itaatsiz
w|zuvorderst|her şeyden önce
""",
"C2.2": """
n|die Augenwischerei|göz boyama
n|der Spagat|iki şeyi dengeleme çabası
n|die Haarspalterei|kılı kırk yarma
n|der Kuhhandel|kirli pazarlık
n|die Fallstricke|tuzaklar (Pl.)
n|das Kalkül|hesap, strateji
n|der Wermutstropfen|tek kusur, acı nokta
n|die Gesinnung|zihniyet
n|der Tunnelblick|dar bakış açısı
n|die Bredouille|zor durum, sıkıntı
v|sich ins Zeug legen|var gücüyle çalışmak|er legt sich ins Zeug · hat sich ins Zeug gelegt
v|den Kürzeren ziehen|kaybeden taraf olmak|er zieht den Kürzeren · hat den Kürzeren gezogen
v|unter den Teppich kehren|halının altına süpürmek|er kehrt · hat gekehrt
v|auf den Busch klopfen|ağız aramak|er klopft · hat geklopft
v|ins Fettnäpfchen treten|pot kırmak|er tritt · ist getreten
v|kolportieren|(söylenti) yaymak|er kolportiert · hat kolportiert
v|lavieren|manevra yaparak idare etmek|er laviert · hat laviert
v|brüskieren|gücendirmek, kabaca reddetmek|er brüskiert · hat brüskiert
v|konterkarieren|boşa çıkarmak|er konterkariert · hat konterkariert
v|sich etwas verbitten|bir şeye izin vermemek|er verbittet sich · hat sich verbeten
v|sich etwas anmaßen|haddini aşmak|er maßt sich an · hat sich angemaßt
w|lapidar|kısa ve öz
w|despektierlich|saygısız
w|obsolet|geçerliliğini yitirmiş
w|sukzessive|adım adım
w|ostentativ|gösterişli, kasıtlı
w|vehement|şiddetle
n|der Augenschein|ilk görünüş
n|die Binsenweisheit|herkesin bildiği gerçek
n|der Etikettenschwindel|ambalaj aldatmacası
n|das Gebaren|tavır, davranış
n|der Hemmschuh|engel
n|die Kehrtwende|U dönüşü
n|der Lackmustest|turnusol testi
n|die Lappalie|önemsiz şey
n|das Sammelsurium|karmakarışık yığın
n|der Seitenhieb|iğneleme
n|die Schadenfreude|başkasının zararına sevinme
n|der Vorwand|bahane
p|aus dem Ruder laufen|kontrolden çıkmak
p|das Handtuch werfen|pes etmek
p|die Katze im Sack kaufen|görmeden almak
p|einen Bärendienst erweisen|iyilik yaparken zarar vermek
p|etwas auf die lange Bank schieben|sürüncemede bırakmak
p|jemandem reinen Wein einschenken|açık açık gerçeği söylemek
p|kein Blatt vor den Mund nehmen|lafını esirgememek
p|mit offenen Karten spielen|açık oynamak
p|sich aus der Affäre ziehen|işin içinden sıyrılmak
p|Tacheles reden|açık konuşmak
p|über den Tellerrand schauen|ufkunu genişletmek
p|zwischen den Zeilen lesen|satır arasını okumak
p|den Teufel an die Wand malen|felaket tellallığı yapmak
p|Öl ins Feuer gießen|yangına körükle gitmek
w|blasiert|kendini beğenmiş
w|dubios|şüpheli
w|ephemer|geçici
w|lakonisch|kısa ve öz
w|obskur|karanlık, şüpheli
w|prätentiös|iddialı, gösterişçi
w|salopp|laubali, rahat
w|verschroben|tuhaf, eksantrik
n|die Chuzpe|yüzsüzlük, cüret
n|das Fiasko|fiyasko
n|die Gemütlichkeit|rahatlık, sıcaklık
n|der Heißsporn|aceleci, ateşli kişi
n|die Kakophonie|ses kargaşası
n|das Kauderwelsch|anlaşılmaz konuşma
n|der Kleingeist|dar kafalı kişi
n|die Querele|sürtüşme
n|die Torschlusspanik|son fırsatı kaçırma korkusu
n|das Wolkenkuckucksheim|hayal âlemi
n|der Zeitgeist|çağın ruhu
n|der Weltschmerz|dünya acısı, derin hüzün
p|auf dem Holzweg sein|yanılıyor olmak
p|aus allen Wolken fallen|şaşkına dönmek
p|das Kind mit dem Bade ausschütten|pireye kızıp yorgan yakmak
p|den Nagel auf den Kopf treffen|tam üstüne basmak
p|die Flinte ins Korn werfen|pes etmek
p|eine Extrawurst verlangen|ayrıcalık istemek
p|ins Blaue hinein|rastgele, plansız
p|jemandem den Wind aus den Segeln nehmen|birinin elini zayıflatmak
p|Krokodilstränen weinen|timsah gözyaşı dökmek
p|mit Kanonen auf Spatzen schießen|serçeye top atmak
p|sich ins eigene Fleisch schneiden|kendi ayağına sıkmak
p|unter einer Decke stecken|gizlice iş birliği yapmak
p|von Tuten und Blasen keine Ahnung haben|hiçbir şeyden anlamamak
p|wie die Katze um den heißen Brei schleichen|lafı dolandırmak
v|desavouieren|açıkça reddetmek, yüzüstü bırakmak
v|echauffieren (sich)|öfkelenmek
v|perhorreszieren|şiddetle reddetmek
v|prätendieren|iddia etmek
w|abstrus|anlaşılmaz
w|antiquiert|demode
w|frugal|sade, mütevazı
w|larmoyant|ağlamaklı, duygusal
w|obsequiös|dalkavuk
w|sakrosankt|dokunulmaz
w|süffisant|kendini beğenmiş
""",
}

GERMAN_ACADEMIC = {
"B1.1": """
n|die Forschung|araştırma
n|die Daten (Pl.)|veri
n|die Methode|yöntem
n|die Quelle|kaynak
n|der Nachweis, die Belege (Pl.)|kanıt
n|die Analyse|analiz
n|der Faktor|etken
n|der Prozess|süreç
n|die Struktur|yapı
v|definieren|tanımlamak
v|identifizieren, ermitteln|belirlemek, tespit etmek
v|hindeuten auf, zeigen|göstermek, işaret etmek
v|auftreten|meydana gelmek
v|erfordern|gerektirmek
v|bewerten, beurteilen|değerlendirmek
v|feststellen; etablieren|kurmak; ortaya koymak
w|signifikant, bedeutend|anlamlı, önemli
w|ähnlich|benzer
w|spezifisch|belirli, özgül
w|darüber hinaus|ayrıca
w|beispielsweise|örneğin
n|der Ansatz|yaklaşım
n|das Ziel|amaç
n|das Kapitel|bölüm
n|die Schlussfolgerung|sonuç
n|die Abbildung; die Zahl|şekil; rakam
n|die Einleitung|giriş
n|die Frage, das Problem|mesele
n|das Niveau|düzey
n|der Zeitraum|dönem
n|der Verweis, die Quelle|kaynak, atıf
n|die Zusammenfassung|özet
n|die Tabelle|tablo
n|das Thema|konu
v|beeinflussen|etkilemek
v|erörtern, diskutieren|tartışmak
v|erklären|açıklamak
v|einschließen|içermek
v|messen|ölçmek
v|bereitstellen, liefern|sağlamak
v|vorschlagen; nahelegen|önermek; ileri sürmek
v|unterstützen|desteklemek
w|verbreitet, üblich|yaygın
w|aktuell|mevcut, güncel
w|vorherig|önceki
w|jedoch|ancak
w|daher|bu nedenle
w|abschließend|sonuç olarak
w|wie zum Beispiel|gibi
v|angeben, feststellen|belirtmek, ifade etmek
v|hinterfragen|sorgulamak
n|die Reihe, die Serie|seri
v|berichten|raporlamak, bildirmek
v|auflisten|sıralamak
v|prognostizieren|öngörmek, yansıtmak
v|aufzeichnen, erfassen|kaydetmek
v|testen|sınamak
n|das Ergebnis|sonuç
v|modellieren|modellemek
v|überprüfen; rezensieren|gözden geçirmek, derlemek
n|der Bereich, die Spannweite|aralık, erim
n|die Phase, das Stadium|aşama
v|festhalten, anmerken|kaydetmek, belirtmek
n|die Konferenz, die Tagung|konferans
n|die Grundgesamtheit, die Population|evren, popülasyon
n|der Fokus|odak
n|der Abschnitt|bölüm
w|insbesondere|özellikle
n|die Anwendung; die Bewerbung|uygulama, başvuru
n|die Bedingung|koşul
n|die Skala|ölçek
w|kritisch|eleştirel, kritik
n|die Autorität|otorite, yetkili kaynak
n|die Grundlage|temel
n|die Funktion|işlev
v|beweisen|kanıtlamak
n|die Fachzeitschrift|akademik dergi
n|der Band; das Volumen|cilt, hacim
v|reduzieren|indirgemek, azaltmak
n|die Alternative|seçenek
w|relativ|görece
w|zahlreich|çok sayıda
""",
"B1.2": """
n|der Begriff, das Konzept|kavram
n|der Kontext|bağlam
n|der Rahmen|çerçeve
n|die Hypothese|hipotez
n|der Teilnehmer, die Teilnehmerin|katılımcı
n|die Stichprobe|örneklem
n|die Umfrage|anket
n|die Variable|değişken
v|interpretieren|yorumlamak
v|nachweisen, zeigen|göstermek, kanıtlamak
v|ableiten|türetmek, elde etmek
v|erhalten, gewinnen|elde etmek
v|untersuchen|araştırmak, incelemek
w|relevant|ilgili, alakalı
w|übereinstimmend, konsistent|tutarlı
w|angemessen, geeignet|uygun
w|folglich|sonuç olarak
w|zusätzlich|ek olarak
w|während, wohingegen|-iken, oysa
n|der Aspekt|yön, boyut
n|der Nutzen|fayda
n|die Kategorie|kategori
n|die Komponente|bileşen
n|das Merkmal|özellik
n|die Auswirkung|etki
n|das Interview|görüşme
n|der Prozentsatz|yüzde
n|der Fragebogen|anket formu
n|die Antwort, die Reaktion|yanıt
n|die Rolle|rol
v|erreichen|ulaşmak
v|analysieren|analiz etmek
v|anwenden|uygulamak
v|vergleichen|karşılaştırmak
v|schlussfolgern|sonuca varmak
v|gegenüberstellen|karşıtlık kurmak
v|vorhersagen|tahmin etmek
v|sich beziehen auf|atıfta bulunmak
v|auswählen|seçmek
w|genau|doğru, kesin
w|verfügbar|mevcut
w|bedeutend|büyük, önemli
w|außerdem|üstelik
w|ebenso|benzer şekilde
w|insgesamt|genel olarak
w|andererseits|öte yandan
w|typischerweise|tipik olarak
v|entwerfen|taslak hazırlamak
n|die Statistik|istatistik
n|der Fall, das Beispiel|örnek, durum
n|die Definition|tanım
w|zufällig|rastgele
n|der Index|dizin, endeks
w|repräsentativ|temsil edici
n|der Anteil|kısım, pay
v|pilotieren, erproben|pilot uygulama yapmak
v|zitieren|alıntı yapmak
n|der Vergleich|karşılaştırma
v|dokumentieren|belgelemek
n|die Konvention|teamül, uzlaşım
w|gleichwertig, äquivalent|eşdeğer
w|zeitgenössisch|çağdaş
w|anfangs|başlangıçta
n|die Technik|teknik
n|die Bewertung|değerlendirme
n|das Element|öge
n|die Formel|formül
n|die Veröffentlichung|yayın
v|einstufen, ranken|sıralamak, derecelendirmek
n|die Erklärung|açıklama
n|das Verfahren|prosedür, işlem
v|kennzeichnen|etiketlemek
n|der Output, die Ausgabe|çıktı
w|im Wesentlichen|esasen
n|die Institution|kurum
n|das Experiment|deney
v|einführen, vorstellen|tanıtmak, sunmak
n|das Verhältnis|oran
w|lediglich|sadece
n|die Häufigkeit|sıklık
n|die Ausnahme|istisna
n|der Input, die Eingabe|girdi
n|der Datensatz|veri kümesi
v|abhängen von|-e bağlı olmak
v|kartieren, planen|haritalamak, planlamak
v|in Beziehung setzen|ilişkilendirmek
v|betreffen|-ile ilgili olmak
n|die Fallstudie|vaka çalışması
v|beschränken auf|-ile sınırlamak
n|die Stichprobengröße|örneklem büyüklüğü
p|im Hinblick auf|-açısından
p|im Gegensatz dazu|buna karşılık
v|sich identifizieren mit|özdeşleştirmek
n|die Forschungslücke|bilgi boşluğu
n|die Rücklaufquote|yanıt oranı
""",
"B2.1": """
n|die Annahme|varsayım
n|das Kriterium|ölçüt
n|die Implikation, die Folgerung|sonuç, çıkarım
n|die Einschränkung, die Limitation|sınırlılık
n|die Perspektive|bakış açısı
n|das Phänomen|olgu
n|die Korrelation|korelasyon, ilişki
n|der Trend, die Tendenz|eğilim
v|argumentieren|savunmak, ileri sürmek
v|veranschaulichen|örneklemek
v|betonen|vurgulamak
v|evaluieren, auswerten|değerlendirmek
v|klären|açıklığa kavuşturmak
v|skizzieren|ana hatlarıyla anlatmak
w|entscheidend|kritik, çok önemli
w|empirisch|deneysel, ampirik
w|nachfolgend|sonraki
w|somit|böylece
w|dennoch|yine de
n|das Argument|argüman
n|die Behauptung|iddia
n|die Folge|sonuç
n|die Dimension|boyut
n|die Betonung|vurgu
n|der Indikator|gösterge
n|die Zielsetzung|hedef
n|die Strategie|strateji
n|die Theorie|kuram
v|anerkennen|kabul etmek
v|übernehmen|benimsemek
v|vorwegnehmen, erwarten|öngörmek
v|annehmen|varsaymak
v|kategorisieren|sınıflandırmak
v|infrage stellen|sorgulamak
v|bestimmen|belirlemek
v|steigern, verbessern|geliştirmek
v|hervorheben|vurgulamak
v|aufrechterhalten; behaupten|sürdürmek; savunmak
w|beträchtlich|kayda değer
w|explizit|açık, belirgin
w|potenziell|olası
w|dementsprechend|buna uygun olarak
w|in erster Linie|öncelikle
w|in gewissem Maße|bir ölçüde
w|hinsichtlich|ile ilgili olarak
n|die Abfolge, die Sequenz|dizi, sıra
n|der Beitrag|katkı
n|das Prinzip|ilke
n|die Zusammensetzung|bileşim, kompozisyon
w|einheitlich|tekdüze, aynı
n|das Feedback, die Rückmeldung|geri bildirim
w|ausreichend|yeterli
w|dynamisch|değişken, dinamik
w|kollektiv, gemeinsam|toplu, ortak
n|die Schätzung|tahmin
n|die Wechselwirkung|etkileşim
w|eindeutig, verschieden|belirgin, ayrı
w|parallel|koşut
n|das Instrument|araç (ölçüm)
n|die Intervention|müdahale
n|die Anforderung|gereklilik
n|die Untersuchung|araştırma, soruşturma
n|die Disziplin, das Fachgebiet|bilim dalı
w|dominant|baskın
w|kurz|kısaca
w|ausschließlich|yalnızca
v|nachverfolgen|izini sürmek
n|die Ethik|etik
n|das Szenario|senaryo
w|jeweilig|ilgili, sırasıyla
w|teilweise|kısmen
v|auflösen, lösen|çözümlemek
n|die Vorstellung, der Begriff|kavram, fikir
w|zugrunde liegend|altta yatan
n|die Beobachtung|gözlem
w|anwendbar|uygulanabilir
w|linear|doğrusal
n|die Kontrollgruppe|kontrol grubu
v|ausgleichen|telafi etmek
p|zusammengenommen|bir bütün olarak ele alındığında
n|die Fehlertoleranz, die Fehlermarge|hata payı
n|das Forschungsdesign|araştırma tasarımı
p|in Bezug auf|-e ilişkin olarak
p|auf der Grundlage von|-e dayanarak
p|daraus folgt, dass|buradan şu çıkar ki
n|qualitative Daten (Pl.)|nitel veri
p|in diesem Sinne|aynı doğrultuda
p|das konzeptionelle Modell|kavramsal model
n|das Ethikvotum|etik kurul onayı
p|die informierte Einwilligung|bilgilendirilmiş onam
n|die Literaturübersicht|literatür taraması
n|quantitative Daten (Pl.)|nicel veri
""",
"B2.2": """
n|die Methodik|yöntembilim
n|die Validität, die Gültigkeit|geçerlilik
n|die Reliabilität, die Zuverlässigkeit|güvenilirlik
n|die Verzerrung|yanlılık
n|die Fachliteratur|literatür
n|der Befund, das Ergebnis|bulgu
n|die Verteilung|dağılım
v|zuschreiben|atfetmek
v|darstellen, bilden|oluşturmak
v|erleichtern|kolaylaştırmak
v|erzeugen|üretmek
v|durchführen|üstlenmek, yürütmek
v|begründen|gerekçelendirmek
w|umfassend|kapsamlı
w|vorläufig|ön, ilk
w|qualitativ|nitel
w|quantitativ|nicel
w|beziehungsweise, jeweils|sırasıyla
w|in hohem Maße|büyük ölçüde
n|das Abstract|özet (makale)
n|der Anhang|ek
n|das Zitat|alıntı, atıf
n|die Kohärenz|tutarlılık
n|die Gleichung|denklem
n|die Interpretation|yorum
n|der Mechanismus|mekanizma
n|der Ausreißer|aykırı değer
n|das Peer-Review|hakem değerlendirmesi
n|die Signifikanz|anlamlılık
n|der Betreuer|tez danışmanı
v|zuweisen|tahsis etmek
v|zusammenstellen|derlemek
v|bestätigen|doğrulamak
v|unterscheiden|ayırt etmek
v|ausschließen|dışlamak
v|umsetzen|uygulamak
v|folgern|çıkarsamak
v|modifizieren|değiştirmek
v|validieren|doğrulamak
w|zugänglich|erişilebilir
w|statistisch|istatistiksel
w|gültig, valide|geçerli
w|theoretisch|kuramsal
w|ungefähr|yaklaşık
w|anschließend|ardından
w|entsprechend|buna karşılık olarak
v|umwandeln|dönüştürmek
w|generisch, allgemein|genel, jenerik
v|veröffentlichen|yayımlamak
n|die Dynamik|dinamikler
w|vergleichbar|karşılaştırılabilir
v|beobachten|gözlemlemek
v|erkennen, nachweisen|saptamak, tespit etmek
n|der Graph, die Grafik|grafik
n|der Median|ortanca
n|die These; die Abschlussarbeit|tez, sav
n|der Schwellenwert|eşik
v|unterbringen, berücksichtigen|barındırmak, uyum sağlatmak
v|extrahieren|çıkarmak, ayıklamak
n|die Achse|eksen
w|nämlich|yani, şöyle ki
n|die Anpassung|uyarlama
v|abwägen|tartmak, değerlendirmek
n|die Konfiguration|yapılandırma
n|die Tendenz|eğilim
w|integral, wesentlich|ayrılmaz, bütünleyici
w|ausdrücklich|açıkça
v|aggregieren, zusammenfassen|toplamak, bir araya getirmek
v|lokalisieren|konumlandırmak, bulmak
w|optimal|en uygun
v|übersetzen|çevirmek
n|die Norm|norm
n|die Illustration|görsel örnek
n|das Manuskript|müsvedde, makale metni
v|hervorgehen, auftauchen|ortaya çıkmak
n|das Modul|modül
v|verifizieren|doğrulamak
n|die Glaubwürdigkeit|güvenilirlik
w|begutachtet (peer-reviewed)|hakemli
v|berechnen|hesaplamak
v|regulieren|düzenlemek
w|systematisch|sistematik
n|die Forschungsfrage|araştırma sorusu
n|der Forschungsstand|literatür bütünü
n|die empirische Evidenz|ampirik kanıt
n|das Signifikanzniveau|anlamlılık düzeyi
n|die Standardabweichung|standart sapma
p|in Übereinstimmung mit|-e uygun olarak
p|wie in Tabelle 2 ersichtlich|Tablo 2'de görüldüğü üzere
p|inwieweit|-in ne ölçüde olduğu
n|die Nullhypothese|sıfır hipotezi
p|in der vorliegenden Studie|bu çalışmada
p|wir haben die Hypothese aufgestellt, dass|şu hipotezi kurduk
n|die Störvariable|karıştırıcı değişken
p|der theoretische Rahmen|kuramsal çerçeve
p|in dieser Arbeit wird argumentiert, dass|bu çalışma şunu savunmaktadır
n|die Daten zeigen, dass|veriler şunu göstermektedir
""",
"C1.1": """
n|das Paradigma|paradigma
n|die Begründung|gerekçe
n|der Diskurs|söylem
n|die Diskrepanz|tutarsızlık
n|die Machbarkeit|uygulanabilirlik
n|die Prämisse|öncül
v|synthetisieren|sentezlemek
v|postulieren|ileri sürmek, varsaymak
v|erläutern|aydınlatmak, açıklamak
v|abgrenzen, umreißen|sınırlarını çizmek
v|mindern, abschwächen|hafifletmek, azaltmak
w|inhärent|doğasında olan
w|robust|sağlam
w|hervorstechend|göze çarpan, belirgin
w|mehrdeutig|belirsiz, çok anlamlı
w|umgekehrt|tersine
n|die Anomalie|anomali
n|die Kausalität|nedensellik
n|die Verallgemeinerbarkeit|genellenebilirlik
n|die Umsetzung|uygulama
n|der Parameter|parametre
n|die Strenge|titizlik
n|die Taxonomie|sınıflandırma
v|befürworten|savunmak
v|kalibrieren|kalibre etmek
v|umfassen|kapsamak
v|formulieren|formüle etmek
w|kohärent|tutarlı
w|intrinsisch|içsel
w|marginal|marjinal
w|plausibel|akla yatkın
w|dadurch|böylece
w|wodurch|ki bununla
w|nichtsdestotrotz|yine de
n|das Diagramm|şema
w|willkürlich|keyfi
n|die Synthese|sentez
v|kritisch bewerten|eleştirel değerlendirme yapmak
n|der Prototyp|prototip
w|diagnostisch|tanısal
n|das Literaturverzeichnis|kaynakça
w|im Großen und Ganzen|genel hatlarıyla
w|alternativ|alternatif olarak
w|subjektiv|öznel
n|die Hierarchie|hiyerarşi
n|das Intervall|aralık
v|zusammenführen|birleştirmek
w|endlich|sonlu
n|die Zuweisung|tahsis
w|vorhergehend|önceki
w|analytisch|çözümleyici
v|wahrnehmen|algılamak
n|die Probe|numune
n|die Analogie|benzeşim
n|die Dissertation|tez (doktora)
v|sich manifestieren|açığa vurmak, tezahür etmek
n|die Terminologie|terminoloji
v|übertragen|iletmek
v|annähern, näherungsweise berechnen|yaklaşık olarak hesaplamak
v|prüfen, inspizieren|denetlemek, incelemek
v|überdenken|yeniden değerlendirmek
v|reproduzieren|yeniden üretmek
n|der Praktiker|uygulayıcı
v|behaupten, geltend machen|savunmak, öne sürmek
v|vermuten|varsaymak
w|konzeptionell|kavramsal
w|hypothetisch|varsayımsal
p|in Anlehnung an die Arbeit von|-in çalışmasından yararlanarak
p|frühere Forschung legt nahe|önceki araştırmalar şunu göstermektedir
p|es ist darauf hinzuweisen, dass|belirtmek gerekir ki
p|dies steht im Einklang mit|bu, -ile uyumludur
n|der Rahmen dieser Arbeit|bu makalenin kapsamı
p|entgegen den Erwartungen|beklentilerin aksine
p|soweit die Daten es zulassen|verilerin izin verdiği ölçüde
p|statistisch signifikant|istatistiksel olarak anlamlı
p|es ist allgemein anerkannt, dass|genel kabul görmektedir ki
p|weitere Forschung ist erforderlich|daha fazla araştırmaya ihtiyaç var
p|wie in Abbildung 1 dargestellt|Şekil 1'de gösterildiği gibi
p|angesichts dieser Befunde|bu bulgular ışığında
p|künftige Arbeiten sollten … behandeln|ilerideki çalışmalar -i ele almalıdır
p|Ziel dieser Studie ist es, …|bu çalışmanın amacı
p|diese Befunde legen nahe, dass|bu bulgular şunu düşündürmektedir
""",
"C1.2": """
n|der Vorbehalt|çekince, uyarı
n|die Nuance|nüans, ince fark
n|der Verlauf|seyir, gidişat
n|die Dichotomie|ikilik, ayrım
n|der Konsens|uzlaşı
n|die Heuristik|sezgisel yöntem
v|untermauern|temelini oluşturmak
v|in Einklang bringen|bağdaştırmak
v|extrapolieren|genellemek, ileriye tahmin etmek
v|operationalisieren|ölçülebilir hale getirmek
v|genau prüfen|titizlikle incelemek
v|widerlegen|çürütmek
v|rechtfertigen|gerektirmek, haklı kılmak
w|einschlägig, sachdienlich|yerinde, ilgili
w|dürftig, schwach|zayıf (bağlantı)
w|zentral, ausschlaggebend|kilit, merkezi
w|streng, rigoros|titiz
w|angeblich, vordergründig|görünüşte
w|unter anderem|diğerlerinin yanı sıra
w|wenn auch|-se de
n|der Vorläufer|öncül
n|die Vermutung|varsayım
n|das Korpus|derlem
n|das Gegenargument|karşı argüman
n|die Darlegung|açıklama
n|das Paradoxon|paradoks
n|der Präzedenzfall|emsal
n|die Proxy-Variable|vekil gösterge
v|sich halten an|bağlı kalmak
v|anspielen auf|ima etmek
v|artikulieren|açıkça ifade etmek
v|festigen|pekiştirmek
v|gipfeln|doruğa ulaşmak
v|verbreiten|yaymak
v|voraussetzen|önceden varsaymak
v|festlegen|şart koşmak
w|abhängig|koşullu, bağlı
w|diskret|ayrık
w|implizit|örtük
w|bahnbrechend|çığır açan
w|beispiellos|eşi görülmemiş
w|insofern als|-dığı ölçüde
w|ungeachtet|-e rağmen
w|in dieser Hinsicht|bu bağlamda
w|im weiteren Sinne|buna bağlı olarak
v|isolieren|yalıtmak, ayrıştırmak
n|das Gleichgewicht|denge
v|beginnen|başlamak
w|naturgemäß|doğası gereği
w|indikativ, hinweisend|gösterge niteliğinde
w|ergänzend, komplementär|tamamlayıcı
v|fragmentieren|parçalamak
v|replizieren|yinelemek (deneyi), kopyalamak
w|kumulativ|birikimli
w|deskriptiv|betimleyici
v|entsprechen, sich anpassen|uygun olmak, uymak
n|die Abhängigkeit|bağımlılık
n|der Auszug|alıntı parçası
w|vergleichsweise|görece olarak
v|organisieren|düzenlemek
v|provozieren, auslösen|kışkırtmak, tetiklemek
w|korreliert|ilişkili, bağıntılı
v|zusammenfallen|çakışmak, aynı anda olmak
w|gleichzeitig|eşzamanlı
v|spekulieren|spekülasyon yapmak
n|die Deduktion|tümdengelim
n|die Varianz|varyans
v|simulieren|benzetim yapmak
n|das Kontinuum|süreklilik
n|die Replikation|yineleme çalışması
n|die Kohorte|kohort, grup
n|die Abweichung|sapma
v|klassifizieren|sınıflandırmak
n|der Koeffizient|katsayı
w|interdisziplinär|disiplinlerarası
v|entstammen|kaynaklanmak, doğmak
w|longitudinal|boylamsal (uzun süreli)
w|prädiktiv|öngörücü
w|einseitig|tek taraflı
w|kausal|nedensel
n|die Danksagung; die Anerkennung|teşekkür bölümü, kabul
p|dies wirft die Frage auf|bu, şu soruyu doğurmaktadır
p|ein erheblicher Anteil von|-in hatırı sayılır bir kısmı
p|die vorliegenden Befunde erweitern|mevcut bulgular -i genişletmektedir
p|nach unserem besten Wissen|bildiğimiz kadarıyla
p|die zugrunde liegende Annahme ist|altta yatan varsayım şudur
p|eine mögliche Erklärung ist, dass|olası bir açıklama şudur ki
p|über den Rahmen dieser Studie hinaus|bu çalışmanın kapsamı dışında
p|für die Zwecke dieser Studie|bu çalışmanın amaçları doğrultusunda
p|mehrere Studien haben gezeigt|bir dizi çalışma göstermiştir ki
p|eine Limitation dieser Studie ist|bu çalışmanın bir sınırlılığı
n|die Ergebnisse stimmen überein mit|sonuçlar -ile tutarlıdır
p|im Gegensatz zu früheren Befunden|önceki bulguların aksine
p|… wurde bisher wenig beachtet|-e çok az dikkat gösterilmiştir
p|es gibt zunehmend Belege|giderek artan bir kanıt bütünü var
""",
"C2.1": """
n|die Erkenntnistheorie|epistemoloji, bilgi kuramı
n|die Ontologie|ontoloji
n|die Hegemonie|hegemonya
n|die Tautologie|totoloji, gereksiz tekrar
n|die logische Folge|doğal sonuç
v|problematisieren|sorunsallaştırmak
v|kontextualisieren|bağlama oturtmak
v|hervorrufen|doğurmak, yol açmak
v|verschleiern|bulanıklaştırmak
w|eigentümlich, idiosynkratisch|kendine özgü
w|reduktionistisch|indirgemeci
w|allgegenwärtig|her yerde bulunan
w|selbstverständlich, axiomatisch|apaçık, aksiyomatik
w|stillschweigend|örtük, söylenmeden kabul edilen
w|erst recht|haydi haydi, evleviyetle
w|eo ipso, eben dadurch|bizzat bu nedenle
w|sinngemäß|gerekli değişiklikler yapılarak
n|die Aporie|(felsefi) çıkmaz
n|die Dialektik|diyalektik
n|die Exegese|yorum, tefsir
n|die Geschichtsschreibung|tarih yazımı
n|die Ideologie|ideoloji
n|der Positivismus|pozitivizm
n|der Relativismus|görecilik
n|die Subjektivität|öznellik
n|der Syllogismus|kıyas
v|urteilen|hüküm vermek
v|eingrenzen|sınırlamak
v|dekonstruieren|yapıbozuma uğratmak
v|verkörpern|simgelemek
v|explizieren|açıklamak
v|marginalisieren|ötekileştirmek
v|bevorzugen|ayrıcalık tanımak
v|theoretisieren|kuramlaştırmak
w|kanonisch|kanonik
w|dialektisch|diyalektik
w|normativ|normatif
w|paradigmatisch|paradigmatik
w|nachträglich|sonradan
w|im engeren Sinne|dar anlamda
w|gegenüber|-e karşı, ile ilgili olarak
n|die Annäherung|yaklaşıklık
v|beleuchten|aydınlatmak (konuyu)
w|schlüssig|kesin
w|erschöpfend|tüketici, eksiksiz
w|sequenziell|ardışık
w|deutlich|belirgin biçimde
w|hierarchisch|hiyerarşik
n|die Richtlinie|yönerge
n|der Unterabschnitt|alt bölüm
v|anprangern|kınamak
v|konvergieren, zusammenlaufen|yakınsamak, birleşmek
n|das Plagiat|intihal
v|korrelieren|ilişkilendirmek, bağıntı kurmak
v|gleichsetzen|eşitlemek, denk saymak
v|erweitern, ergänzen|artırmak, takviye etmek
w|explorativ|keşfedici
n|die Fußnote|dipnot
v|verstärken|güçlendirmek, büyütmek
n|der Befürworter|savunucu
w|bislang|şimdiye kadar
v|behindern|engellemek
w|kontextuell|bağlamsal
v|vermitteln|aracılık etmek
v|wiederholen, bekräftigen|yinelemek
n|das Schema|şema, çerçeve
w|nicht schlüssig|sonuçsuz, belirsiz
n|der Prädiktor|yordayıcı değişken
v|hervorlocken, ermitteln|ortaya çıkarmak, elde etmek (yanıt)
n|der Befragte|katılımcı, yanıtlayan
v|automatisieren|otomatikleştirmek
v|verzerren|çarpıtmak
v|auslassen|çıkarmak, atlamak
v|paraphrasieren|başka sözcüklerle ifade etmek
v|vereinheitlichen|birleştirmek
v|abweichen|sapmak
v|erbitten, einholen|talep etmek, istemek
n|die Herleitung|türetme
w|methodisch|yöntemsel
v|entkräften, ungültig machen|geçersiz kılmak
""",
"C2.2": """
n|die Heterogenität|heterojenlik
n|die Verdinglichung|şeyleştirme
n|die Teleologie|teleoloji, ereksellik
n|die Hermeneutik|yorumbilim
n|die Wahrscheinlichkeit, die Glaubwürdigkeit|gerçeğe benzerlik
n|die Praxis|pratik, uygulama
v|instanziieren, konkretisieren|somutlaştırmak, örneklemek
v|aufwerten|değer atfetmek, yüceltmek
v|kritisch hinterfragen|(eleştirel) sorgulamak
v|in den Vordergrund stellen|ön plana çıkarmak
v|vermengen|birbirine karıştırmak
w|abstrus, schwer verständlich|anlaşılması güç
w|entstehend, aufkommend|yeni filizlenen
w|polemisch|polemik, tartışmacı
w|auf den ersten Blick|ilk bakışta
w|unter sonst gleichen Bedingungen|diğer koşullar sabitken
n|die Alterität|ötekilik
n|die Episteme|bilgi düzeni
n|der Habitus|habitus
n|die Intertextualität|metinlerarasılık
n|die Liminalität|eşiksellik
n|die Performativität|performatiflik
n|die Positionalität|konumsallık
n|die Reflexivität|düşünümsellik
v|aufheben|yürürlükten kaldırmak
v|dulden, gutheißen|hoş görmek
v|essentialisieren|özcüleştirmek
v|verdecken|örtmek, gizlemek
v|verdinglichen|şeyleştirmek
v|subsumieren|kapsamına almak
w|aporetisch|çıkmaza dair
w|apodiktisch|kesin
w|hegemonial|hegemonik
w|liminal|eşiksel
w|rekursiv|özyinelemeli
w|synkretistisch|bağdaştırmacı
w|bei allem Respekt vor|(-e) saygıyla katılmayarak
w|sic|aynen böyle (alıntıda)
v|unterstreichen|altını çizmek, vurgulamak
v|beschränken|sınırlamak, kısıtlamak
v|fälschen; herstellen|uydurmak, imal etmek
n|die Anmerkung|dipnot, açıklama
v|annullieren|hükümsüz kılmak
v|erzählen|anlatmak
v|authentifizieren, beglaubigen|gerçekliğini doğrulamak
v|transkribieren|deşifre etmek, yazıya dökmek
v|ablösen, ersetzen|yerini almak, geçersiz kılmak
v|wiederkehren|yinelemek, tekrar etmek
v|anhängen|eklemek (sona)
v|charakterisieren|nitelendirmek
v|vorgeben, angeblich sein|iddia etmek, öyle görünmek
v|optimieren|en iyi duruma getirmek
v|ausführlich darlegen|ayrıntılı açıklamak
v|neu formulieren|yeniden ifade etmek
n|die Verallgemeinerung|genelleme
v|zusammentragen, abgleichen|karşılaştırıp derlemek
v|verorten|konumlandırmak
v|aufzählen|tek tek saymak
v|rationalisieren|akla uydurmak, gerekçelendirmek
v|auslegen, deuten|yorumlamak, anlam vermek
v|normalisieren|normalleştirmek
v|annotieren, kommentieren|notlandırmak, açıklama düşmek
v|verallgemeinern|genellemek
v|tabellarisch darstellen|tablolaştırmak
v|rekapitulieren|özetleyerek tekrarlamak
v|konzeptualisieren|kavramsallaştırmak
v|Hypothesen aufstellen|hipotez kurmak
v|randomisieren|rastgeleleştirmek
""",
}

GERMAN_CYBER = {
"B1.1": """
n|der Vermögenswert, das Asset|varlık (korunacak değer)
n|die Bedrohung|tehdit
n|der Bedrohungsakteur|tehdit aktörü
n|die Schwachstelle|zafiyet, açık
n|der Exploit; ausnutzen|istismar kodu / istismar etmek
n|das Risiko|risk
n|die Eintrittswahrscheinlichkeit|olasılık
n|die Auswirkung|etki, sonuç
n|die Angriffsfläche|saldırı yüzeyi
n|der Angriffsvektor|saldırı vektörü
n|der Schadensradius|etki alanı, yayılma çapı
n|die Vertraulichkeit|gizlilik
n|die Integrität|bütünlük
n|die Verfügbarkeit|erişilebilirlik
n|die Nichtabstreitbarkeit|inkâr edilemezlik
n|die Authentifizierung|kimlik doğrulama
n|die Autorisierung|yetkilendirme
n|die Protokollierung (Accounting)|kayıt tutma, hesap verme
n|das Prinzip der geringsten Rechte|en az yetki ilkesi
n|die gestaffelte Verteidigung (Defense in Depth)|katmanlı savunma
n|Zero Trust|sıfır güven
n|die Sicherheitslage|güvenlik duruşu
n|die Baseline, die Referenzkonfiguration|temel referans yapılandırma
n|die Härtung|sıkılaştırma
n|der Patch|yama
n|das Patch-Management|yama yönetimi
n|die Gegenmaßnahme|karşı önlem
n|die Schutzmaßnahme|koruyucu tedbir
n|die Kontrolle, die Sicherheitsmaßnahme|kontrol, denetim mekanizması
n|die kompensierende Kontrolle|telafi edici kontrol
n|die Risikominderung|azaltma, hafifletme
n|die Behebung|giderme, düzeltme
n|das Restrisiko|artık risk
n|das False Positive, der Fehlalarm|yanlış pozitif
n|das False Negative|yanlış negatif
n|das True Positive|doğru pozitif
n|die Erkennung|tespit
n|die Prävention|önleme
n|die Reaktion|müdahale
n|die Wiederherstellung|kurtarma
n|die Resilienz|dayanıklılık
n|die Redundanz|yedeklilik
n|das Failover|yedeğe geçiş
n|die Geschäftskontinuität|iş sürekliliği
n|die Notfallwiederherstellung (Disaster Recovery)|felaket kurtarma
n|der Single Point of Failure|tek hata noktası
n|Security by Design|tasarımdan gelen güvenlik
n|ausfallsicher (fail secure)|hata durumunda güvenli kalma
n|die Vertrauensgrenze|güven sınırı
n|die Bedrohungslage|tehdit ortamı
n|das Risiko bewerten|riski değerlendirmek
n|das Risiko mindern|riski azaltmak
p|den Vorfall eskalieren|olayı üst seviyeye taşımak
n|die Bedrohung eindämmen|tehdidi kontrol altına almak
p|den Befund beheben|bulguyu gidermek
n|das System härten|sistemi sıkılaştırmak
n|die Schwachstelle patchen|zafiyeti yamalamak
n|die Richtlinie durchsetzen|politikayı uygulatmak
n|die Korrektur verifizieren|düzeltmeyi doğrulamak
n|das Problem reproduzieren|sorunu yeniden oluşturmak
n|die Schritte dokumentieren|adımları belgelemek
p|ein Ticket erstellen|kayıt/talep açmak
p|ein Bedenken melden|bir endişeyi işaretlemek
p|den Bericht durchgehen|raporu adım adım anlatmak
p|nachfassen bei|takibini yapmak
n|das Team einbeziehen|ekibi sürece dâhil etmek
p|sich mit den Stakeholdern abstimmen|paydaşlarla mutabık kalmak
p|Befunde priorisieren|bulguları önceliklendirmek
p|den Auftragsumfang festlegen|projenin kapsamını belirlemek
p|freigeben, abzeichnen|onay vermek
""",
"B1.2": """
p|ausrollen|yaygınlaştırmak, devreye almak
p|zurückrollen|geri almak (değişikliği)
w|außer Betrieb nehmen|hizmetten çıkarmak
p|eine IP auf die Allowlist setzen|bir IP'yi izin listesine eklemek
p|den Zugriff entziehen|erişimi iptal etmek
p|Zugriff gewähren|erişim vermek
p|Zugangsdaten rotieren|kimlik bilgilerini yenilemek
n|die Protokollierung aktivieren|günlük kaydını açmak
p|auf Anomalien überwachen|anormallikleri izlemek
p|Ereignisse korrelieren|olayları ilişkilendirmek
p|den Alarm verifizieren|uyarıyı doğrulamak
p|als Fehlalarm schließen|yanlış pozitif olarak kapatmak
p|eine Überprüfung durchführen|inceleme yürütmek
n|die Befunde präsentieren|bulguları sunmak
n|das Budget begründen|bütçeyi gerekçelendirmek
p|gemäß unserer Richtlinie|politikamız gereği
p|im Einklang mit Best Practices|iyi uygulamalarla uyumlu olarak
p|vorbehaltlich der Genehmigung|onaya tabi olarak
p|bis zur weiteren Untersuchung|inceleme sürerken, sonuç beklenirken
p|mit sofortiger Wirkung|derhal geçerli olmak üzere
n|das Paket|paket
n|die Nutzlast, der Payload|yük, veri kısmı
n|der Header|başlık
n|der Frame|çerçeve
n|das Protokoll|protokol
n|der Port|port
n|der Socket|soket
n|der Handshake|el sıkışma
n|der Drei-Wege-Handshake|üçlü el sıkışma
n|das Subnetz|alt ağ
n|das Gateway|ağ geçidi
n|der Router|yönlendirici
n|der Switch|anahtar
n|die Firewall|güvenlik duvarı
n|die Next-Generation-Firewall|yeni nesil güvenlik duvarı
n|die Stateful Inspection|durum bilgili denetim
n|die Zugriffskontrollliste (ACL)|erişim kontrol listesi
n|NAT (Netzwerkadressübersetzung)|ağ adresi çevirisi
n|das VLAN|sanal yerel ağ
n|die Netzwerksegmentierung|ağ segmentasyonu
n|die Mikrosegmentierung|mikro segmentasyon
n|die DMZ|silahtan arındırılmış bölge
n|der Proxy|vekil sunucu
n|der Reverse Proxy|ters vekil sunucu
n|der Load Balancer, der Lastverteiler|yük dengeleyici
n|das VPN|sanal özel ağ
n|das Tunneling|tünelleme
n|die Portweiterleitung|port yönlendirme
n|das Pivoting|başka ağa sıçrama
n|der Paketmitschnitt|paket yakalama
n|das Sniffing|trafik dinleme
n|die Verkehrsanalyse|trafik analizi
n|die Bandbreite|bant genişliği
n|die Latenz|gecikme
n|der Durchsatz|iş hacmi, veri geçiş oranı
n|der Broadcast|yayın (tüm ağa)
n|die Routingtabelle|yönlendirme tablosu
n|die DNS-Auflösung|DNS çözümleme
n|die DHCP-Lease|DHCP kirası
n|TLS|taşıma katmanı güvenliği
n|mutual TLS (mTLS)|karşılıklı TLS
n|das Certificate Pinning|sertifika sabitleme
n|der WLAN-Zugangspunkt|kablosuz erişim noktası
n|der Rogue Access Point|sahte erişim noktası
n|der Evil Twin|ikiz sahte ağ
n|der Deauthentication-Angriff|bağlantı kesme saldırısı
n|WPA2 / WPA3|kablosuz güvenlik standardı
n|die Egress-Filterung|çıkış trafiği filtreleme
n|die Ingress-Filterung|giriş trafiği filtreleme
n|der Netzwerk-TAP|ağ dinleme noktası
""",
"B2.1": """
n|der Kernel|çekirdek
n|der Prozess|süreç, işlem
n|der Daemon, der Dienst|arka plan servisi
n|der Dienst|servis
n|die Shell|kabuk
n|das Recht, die Berechtigung|yetki
n|root|en yetkili kullanıcı
n|sudo|yetkili komut çalıştırma
n|die Dateiberechtigung|dosya izni
n|das Setuid-Binary|setuid çalıştırılabilir
n|der Cronjob|zamanlanmış görev
n|die systemd-Unit|systemd servis birimi
n|die Logdatei|günlük dosyası
n|Syslog|sistem günlük protokolü
n|der Prüfpfad, der Audit-Trail|denetim izi
n|die Registry|kayıt defteri (Windows)
n|Active Directory|Active Directory dizin hizmeti
n|der Domänencontroller|etki alanı denetleyicisi
n|die Gruppenrichtlinie|grup ilkesi
n|das Dienstkonto|servis hesabı
n|das Golden Ticket|sahte Kerberos bileti (altın bilet)
n|der Hash|özet değeri
n|Pass-the-Hash|hash ile kimlik doğrulama saldırısı
n|der LSASS-Dump|LSASS bellek dökümü
n|der Speicherabzug|bellek dökümü
n|der Snapshot|anlık görüntü
n|die virtuelle Maschine|sanal makine
n|der Hypervisor|hipervizör
n|der Container|konteyner
n|das Image|imaj
n|die Sandbox|yalıtılmış test ortamı
n|der Ausbruch (Sandbox/Container)|yalıtımdan kaçış
n|der Endpunkt|uç nokta
n|der Agent|ajan yazılımı
n|das Inventar|envanter
n|das Asset-Management|varlık yönetimi
n|die Konfigurationsabweichung|yapılandırma sapması
n|das Golden Image|standart kurulum imajı
n|die Schadsoftware, die Malware|zararlı yazılım
n|die Ransomware, die Erpressersoftware|fidye yazılımı
n|die Spyware|casus yazılım
n|die Adware|reklam yazılımı
n|das Rootkit|rootkit, kök seti
n|das Bootkit|önyükleme zararlısı
n|der Trojaner|truva atı
n|der Wurm|solucan
n|der Virus|virüs
n|der Dropper|yükleyici zararlı
n|der Loader|yükleyici bileşen
n|der Wiper|veri silici zararlı
n|der Keylogger|tuş kaydedici
n|das Botnetz|bot ağı
n|Command and Control (C2)|komuta kontrol sunucusu
n|der Beacon|periyodik geri bağlantı sinyali
n|die Hintertür|arka kapı
n|die logische Bombe|mantık bombası
n|das Phishing|oltalama
n|das Spear-Phishing|hedefli oltalama
n|das Whaling|üst yönetime yönelik oltalama
n|das Smishing|SMS ile oltalama
n|das Vishing|telefonla oltalama
n|das Pretexting|bahane uydurma (sosyal mühendislik)
n|das Baiting, der Köder|yem atma
n|das Tailgating|yetkisiz peşinden girme
n|das Social Engineering|sosyal mühendislik
n|der CEO-Betrug (Business Email Compromise)|kurumsal e-posta dolandırıcılığı
n|der Diebstahl von Zugangsdaten|kimlik bilgisi hırsızlığı
n|das Credential Stuffing|çalıntı kimlik denemesi
n|das Password Spraying|yaygın parola denemesi
n|der Brute-Force-Angriff|kaba kuvvet saldırısı
n|der Wörterbuchangriff|sözlük saldırısı
n|die Rainbow Table|gökkuşağı tablosu
""",
"B2.2": """
n|der Man-in-the-Middle-Angriff|araya girme saldırısı
n|der Replay-Angriff|tekrar saldırısı
n|das Session Hijacking|oturum ele geçirme
n|das Spoofing|kimlik/adres sahteciliği
n|das ARP-Spoofing|ARP zehirlemesi
n|das DNS-Poisoning|DNS zehirlemesi
n|das DNS-Tunneling|DNS üzerinden tünelleme
n|das Typosquatting|yazım hatası alan adı kapma
n|der Watering-Hole-Angriff|su kaynağı saldırısı
n|der Lieferkettenangriff|tedarik zinciri saldırısı
n|der Denial-of-Service-Angriff (DoS)|hizmet dışı bırakma
n|der DDoS-Angriff|dağıtık hizmet dışı bırakma
n|der Amplification-Angriff|yükseltme saldırısı
n|die Zero-Day-Lücke|sıfırıncı gün açığı
n|die Rechteausweitung|yetki yükseltme
n|die laterale Bewegung|yatay hareket
n|die Persistenz|kalıcılık sağlama
n|die Datenexfiltration|veri sızdırma
n|die Datenpanne|veri ihlali
n|der Innentäter|iç tehdit
n|die APT (fortgeschrittene, andauernde Bedrohung)|gelişmiş kalıcı tehdit
n|Living off the Land|sistemin kendi araçlarını kullanma
n|die dateilose Malware|dosyasız zararlı
n|die Verschleierung|gizleme, karmaşıklaştırma
n|das Packing|paketleme (zararlıyı gizleme)
w|polymorph|çok biçimli (zararlı)
n|die Umgehung|atlatma, kaçınma
n|Anti-Forensik|adli analizi engelleme
n|das Cryptojacking|izinsiz kripto madenciliği
n|die Scareware|korkutma yazılımı
n|die doppelte Erpressung|çifte şantaj
n|der Erstzugriff|ilk erişim
n|die Verweildauer|saldırganın sistemde kalış süresi
n|die Kill Chain|saldırı zinciri
n|die Injection|enjeksiyon
n|die SQL-Injection|SQL enjeksiyonu
n|die Command Injection|komut enjeksiyonu
n|Cross-Site-Scripting (XSS)|siteler arası betik çalıştırma
n|Stored XSS|kalıcı XSS
n|Reflected XSS|yansıyan XSS
n|Cross-Site Request Forgery (CSRF)|siteler arası istek sahteciliği
n|Server-Side Request Forgery (SSRF)|sunucu taraflı istek sahteciliği
n|die unsichere Deserialisierung|güvensiz seri hâlden çıkarma
n|die Path Traversal|dizin geçişi
n|die Local File Inclusion|yerel dosya dahil etme
n|die Remote Code Execution (RCE)|uzaktan kod çalıştırma
n|die offene Weiterleitung|açık yönlendirme
n|das Clickjacking|tıklama hırsızlığı
n|die fehlerhafte Zugriffskontrolle|bozuk erişim kontrolü
n|IDOR (unsichere direkte Objektreferenz)|güvensiz doğrudan nesne referansı
n|der Logikfehler|iş mantığı açığı
n|die Race Condition|yarış durumu
n|der Pufferüberlauf|arabellek taşması
n|der Heap-Überlauf|yığın taşması
n|der Stack-Überlauf|yığıt taşması
n|Use-after-free|serbest bırakılan belleği kullanma
n|die Eingabevalidierung|girdi doğrulama
n|die Ausgabekodierung|çıktı kodlama
""",
"C1.1": """
n|die Bereinigung|temizleme, arındırma
n|die parametrisierte Abfrage|parametreli sorgu
n|das Prepared Statement|hazırlanmış ifade
n|die Content Security Policy (CSP)|içerik güvenlik politikası
n|die Same-Origin-Policy|aynı köken politikası
n|CORS|kökenler arası kaynak paylaşımı
n|der Sicherheitsheader|güvenlik başlığı
n|die Ratenbegrenzung|istek sınırlama
n|die Web Application Firewall (WAF)|web uygulama güvenlik duvarı
n|das API-Gateway|API ağ geçidi
n|das Token|jeton
n|das Session-Cookie|oturum çerezi
n|das Secure-Flag|güvenli çerez bayrağı
n|HttpOnly|betikten erişilemez çerez
n|das CAPTCHA|bot doğrulama testi
n|die Abhängigkeit|bağımlılık
n|die Software-Stückliste (SBOM)|yazılım bileşen listesi
n|sicheres Programmieren|güvenli kod yazımı
n|das Code-Review|kod incelemesi
n|die statische Codeanalyse (SAST)|statik kod analizi
n|die dynamische Analyse (DAST)|dinamik uygulama testi
n|das Fuzzing|rastgele girdi testi
n|das Secrets-Management|gizli bilgi yönetimi
n|fest codierte Zugangsdaten|koda gömülü kimlik bilgisi
n|die Verschlüsselung|şifreleme
n|die Entschlüsselung|şifre çözme
n|der Klartext|düz metin
n|der Geheimtext, der Chiffretext|şifreli metin
n|die Chiffre|şifre algoritması
n|die symmetrische Verschlüsselung|simetrik şifreleme
n|die asymmetrische Verschlüsselung|asimetrik şifreleme
n|der öffentliche Schlüssel|açık anahtar
n|der private Schlüssel|özel anahtar
n|der Schlüsselaustausch|anahtar değişimi
n|die Schlüsselrotation|anahtar döndürme
n|das Schlüsselmanagement|anahtar yönetimi
n|das Hashing|özetleme
n|der Salt|tuz (hash'e eklenen rastgele değer)
n|der Pepper|gizli ek değer
n|die digitale Signatur|dijital imza
n|das Zertifikat|sertifika
n|die Zertifizierungsstelle (CA)|sertifika otoritesi
n|die Public-Key-Infrastruktur (PKI)|açık anahtar altyapısı
n|das selbstsignierte Zertifikat|kendinden imzalı sertifika
n|der Widerruf|iptal (sertifika)
n|die Entropie|entropi, rastgelelik
n|die Nonce|tek kullanımlık değer
n|der Initialisierungsvektor|başlatma vektörü
n|die Ende-zu-Ende-Verschlüsselung|uçtan uca şifreleme
n|die Verschlüsselung ruhender Daten|durağan veri şifreleme
n|die Transportverschlüsselung|aktarımda şifreleme
n|das Hardware-Sicherheitsmodul (HSM)|donanım güvenlik modülü
n|der Identitätsanbieter (IdP)|kimlik sağlayıcı
n|Single Sign-on (SSO)|tek oturum açma
n|die Föderation|kimlik federasyonu
n|SAML|SAML kimlik doğrulama standardı
n|OAuth|OAuth yetkilendirme protokolü
n|OpenID Connect|OIDC kimlik katmanı
n|die Multi-Faktor-Authentifizierung (MFA)|çok faktörlü kimlik doğrulama
n|das Einmalpasswort (OTP)|tek kullanımlık parola
n|der Passkey|geçiş anahtarı, şifresiz kimlik
w|biometrisch|biyometrik
n|die rollenbasierte Zugriffskontrolle (RBAC)|rol tabanlı erişim kontrolü
n|die attributbasierte Zugriffskontrolle|nitelik tabanlı erişim kontrolü
n|das Privileged Access Management (PAM)|ayrıcalıklı erişim yönetimi
n|der Just-in-Time-Zugriff|anlık/geçici yetki verme
n|der Identitätslebenszyklus|kimlik yaşam döngüsü
n|die Bereitstellung (Provisioning)|hesap oluşturma/atama
n|die Deprovisionierung|hesap kapatma
n|die Zugriffsprüfung|erişim gözden geçirmesi
n|die Funktionstrennung|görevler ayrılığı
""",
"C1.2": """
n|der Penetrationstest|sızma testi
n|das Red Team|kırmızı takım
n|das Blue Team|mavi takım
n|das Purple Team|mor takım
n|der Auftrag, das Projekt|proje, görev süreci
n|die Rules of Engagement|görev kuralları
n|der Umfang, der Scope|kapsam
n|im Scope / außerhalb des Scopes|kapsam içi / kapsam dışı
n|das Autorisierungsschreiben|yetki mektubu
n|die Freistellungserklärung|yasal muafiyet yazısı
n|der Blackbox-Test|kara kutu testi
n|der Whitebox-Test|beyaz kutu testi
n|der Greybox-Test|gri kutu testi
n|die Aufklärung|keşif
n|OSINT|açık kaynak istihbaratı
n|das Footprinting|iz sürme, hedef haritalama
n|die Enumeration|numaralandırma, listeleme
n|das Scannen|tarama
n|der Portscan|port taraması
n|die Diensterkennung|servis tespiti
n|das Banner Grabbing|servis afişi toplama
n|der Schwachstellenscan|zafiyet taraması
n|der Proof of Concept (PoC)|kavram kanıtı
n|die Payload-Auslieferung|zararlı yük iletimi
n|der Shellcode|kabuk kodu
n|die Reverse Shell|ters kabuk bağlantısı
n|die Bind Shell|dinleyen kabuk
n|der Brückenkopf, der Foothold|ilk tutunma noktası
n|pivotieren|sıçrama noktası olarak kullanmak
n|die Post-Exploitation|istismar sonrası aşama
n|das Sammeln von Zugangsdaten|kimlik bilgisi toplama
n|das Knacken von Passwörtern|parola kırma
n|die Rechte-Enumeration|yetki listeleme
n|der Persistenzmechanismus|kalıcılık yöntemi
n|die Nachbesprechung|değerlendirme toplantısı
n|der Befund|bulgu
n|der Schweregrad|önem derecesi
n|der CVSS-Wert|CVSS puanı
n|die Ausnutzbarkeit|istismar edilebilirlik
n|die Behebungsempfehlung|düzeltme önerisi
n|der Retest|yeniden test
n|die Management-Zusammenfassung|yönetici özeti
n|der technische Bericht|teknik rapor
n|das Bug-Bounty-Programm|hata ödül programı
n|die verantwortungsvolle Offenlegung|sorumlu açıklama
n|die koordinierte Offenlegung|eşgüdümlü açıklama
n|die Angreiferemulation|saldırgan taklidi
n|TTPs (Taktiken, Techniken, Prozeduren)|taktikler, teknikler ve prosedürler
n|MITRE ATT&CK|ATT&CK saldırı tekniği çerçevesi
n|das Bedrohungsmodell|tehdit modeli
n|der Angriffsbaum|saldırı ağacı
""",
"C2.1": """
n|das Security Operations Center (SOC)|güvenlik operasyon merkezi
n|der Analyst|analist
n|Level 1 / Level 2|birinci / ikinci seviye destek
n|der Alarm, die Warnung|uyarı
n|die Alarmmüdigkeit|uyarı yorgunluğu
n|die Triage|önceliklendirme, ilk eleme
n|die Eskalation|üst seviyeye taşıma
n|der Sicherheitsvorfall|olay
n|die Vorfallsreaktion (Incident Response)|olay müdahalesi
n|das Playbook|müdahale kılavuzu
n|das Runbook|işletim adımları kılavuzu
n|die Rufbereitschaft|nöbetçi olma
n|die Eindämmung|sınırlandırma, kontrol altına alma
n|die Beseitigung|tehdidi tamamen temizleme
n|die Lessons Learned|çıkarılan dersler
n|die Nachanalyse (Post-Mortem)|olay sonrası inceleme
n|die Ursachenanalyse|kök neden analizi
n|SIEM|güvenlik bilgi ve olay yönetimi
n|die Log-Aggregation|günlük toplama
n|die Korrelationsregel|korelasyon kuralı
n|der Use Case|kullanım senaryosu (tespit kuralı)
n|das Detection Engineering|tespit mühendisliği
n|die Signatur|imza tabanlı tespit
w|heuristisch|sezgisel tespit
n|die Anomalieerkennung|anomali tespiti
n|die Verhaltensanalyse|davranışsal analiz
n|die Abweichung von der Baseline|normalden sapma
n|EDR|uç nokta tespit ve müdahale
n|XDR|genişletilmiş tespit ve müdahale
n|IDS (Angriffserkennungssystem)|saldırı tespit sistemi
n|IPS (Angriffsverhinderungssystem)|saldırı önleme sistemi
n|der Honeypot|bal küpü tuzak sistemi
n|die Deception-Technologie|aldatma teknolojisi
n|die Bedrohungsaufklärung (Threat Intelligence)|tehdit istihbaratı
n|der Kompromittierungsindikator (IoC)|ihlal göstergesi
n|der Angriffsindikator (IoA)|saldırı göstergesi
n|das Threat Hunting|tehdit avcılığı
n|die hypothesengetriebene Jagd|hipotez temelli avlanma
n|die digitale Forensik|dijital adli bilişim
n|die Beweismittelkette|delil zinciri
n|die forensische Abbilderstellung|birebir disk kopyası alma
n|der Schreibblocker|yazma engelleyici
n|flüchtige Daten (Pl.)|uçucu veri
n|die Zeitlinienanalyse|zaman çizelgesi analizi
n|das Artefakt|iz, kalıntı (adli)
n|die Malware-Analyse|zararlı yazılım analizi
n|die statische Analyse|statik analiz
n|das Reverse Engineering|tersine mühendislik
n|die Sandbox-Detonation|zararlıyı yalıtılmış ortamda çalıştırma
n|die YARA-Regel|YARA tespit kuralı
n|SOAR|güvenlik orkestrasyonu ve otomasyonu
n|die mittlere Erkennungszeit (MTTD)|ortalama tespit süresi
n|die mittlere Reaktionszeit (MTTR)|ortalama müdahale süresi
n|der Fehlalarm|yanlış alarm
n|das Tuning, die Feinabstimmung|kural ince ayarı
n|das Whitelisting|beyaz listeye alma
n|das Blocklisting|engelleme listesi
n|die Quarantäne|karantinaya alma
n|die Isolierung|makineyi ağdan yalıtma
n|der Notausschalter (Kill Switch)|acil durdurma anahtarı
""",
"C2.2": """
n|die Governance|yönetişim
n|die Compliance, die Einhaltung|uyum, mevzuata uygunluk
n|die Regulierung|düzenleme, mevzuat
n|der Standard|standart
n|das Rahmenwerk|çerçeve
n|die Richtlinie|politika
n|das Verfahren|prosedür
n|die Leitlinie|kılavuz ilke
n|das Audit, die Prüfung|denetim
n|der Auditor, der Prüfer|denetçi
n|die Audit-Feststellung|denetim bulgusu
n|der Nachweis, das Beweismittel|kanıt, delil
n|die Bestätigung, die Attestierung|beyan, onaylama
n|die Zertifizierung|sertifikasyon
n|die Akkreditierung|akreditasyon
n|die Gap-Analyse|boşluk analizi
n|das Reifegradmodell|olgunluk modeli
n|die Risikobewertung|risk değerlendirmesi
n|das Risikoregister|risk kaydı
n|die Risikobereitschaft|risk iştahı
n|die Risikotoleranz|risk toleransı
n|die Risikoakzeptanz|riski kabul etme
n|der Risikotransfer|riski devretme (sigorta vb.)
n|die Risikovermeidung|riskten kaçınma
n|das inhärente Risiko|doğal risk
n|die Business-Impact-Analyse|iş etki analizi
n|das Wiederherstellungszeitziel (RTO)|kurtarma süresi hedefi
n|das Wiederherstellungspunktziel (RPO)|kurtarma noktası hedefi
n|die Datenklassifizierung|veri sınıflandırma
n|die Datenaufbewahrung|veri saklama süresi
n|die Datenminimierung|veri minimizasyonu
n|personenbezogene Daten (Pl.)|kişisel veri
n|die betroffene Person|veri sahibi
n|der Verantwortliche (Datenschutz)|veri sorumlusu
n|der Auftragsverarbeiter|veri işleyen
n|die DSGVO|Avrupa Genel Veri Koruma Tüzüğü
n|die Meldung einer Datenpanne|ihlal bildirimi
n|Privacy by Design|tasarımdan gelen mahremiyet
n|das Drittanbieterrisiko|üçüncü taraf riski
n|die Lieferantenbewertung|tedarikçi değerlendirmesi
n|die Sorgfaltsprüfung (Due Diligence)|gerekli özen incelemesi
n|das Service-Level-Agreement (SLA)|hizmet seviyesi anlaşması
n|die Geheimhaltungsvereinbarung (NDA)|gizlilik sözleşmesi
n|die Sicherheitsschulung|güvenlik farkındalık eğitimi
n|die Nutzungsrichtlinie|kabul edilebilir kullanım politikası
n|das Änderungsmanagement|değişiklik yönetimi
n|der Genehmigungsworkflow|onay akışı
n|der Ausnahmeantrag|istisna talebi
""",
}

DE_EN = {'der Mann': 'man',
 'die Frau': 'woman',
 'das Kind': 'child',
 'der Name': 'name',
 'das Haus': 'house',
 'die Wohnung': 'flat, apartment',
 'das Wasser': 'water',
 'das Brot': 'bread',
 'der Kaffee': 'coffee',
 'der Tag': 'day',
 'die Woche': 'week',
 'die Stadt': 'city, town',
 'das Land': 'country',
 'die Sprache': 'language',
 'der Freund': 'friend (male); boyfriend',
 'die Familie': 'family',
 'die Mutter': 'mother',
 'der Vater': 'father',
 'sein': 'to be',
 'haben': 'to have',
 'heißen': 'to be called',
 'kommen': 'to come',
 'wohnen': 'to live (reside)',
 'sprechen': 'to speak',
 'trinken': 'to drink',
 'essen': 'to eat',
 'lernen': 'to learn, to study',
 'machen': 'to do, to make',
 'gut': 'good',
 'groß': 'big, tall',
 'klein': 'small',
 'heute': 'today',
 'der Bahnhof': 'train station',
 'der Bus': 'bus',
 'die Straße': 'street, road',
 'das Zimmer': 'room',
 'die Küche': 'kitchen',
 'der Tisch': 'table',
 'der Stuhl': 'chair',
 'das Bett': 'bed',
 'die Uhr': 'clock, watch',
 'das Geld': 'money',
 'der Preis': 'price',
 'der Supermarkt': 'supermarket',
 'das Obst': 'fruit',
 'das Gemüse': 'vegetables',
 'die Milch': 'milk',
 'der Arzt': 'doctor',
 'gehen': 'to go, to walk',
 'fahren': 'to drive, to go (by vehicle)',
 'kaufen': 'to buy',
 'kosten': 'to cost',
 'brauchen': 'to need',
 'möchten': 'would like',
 'nehmen': 'to take',
 'schlafen': 'to sleep',
 'arbeiten': 'to work',
 'spielen': 'to play',
 'lesen': 'to read',
 'schreiben': 'to write',
 'teuer': 'expensive',
 'billig': 'cheap',
 'morgen': 'tomorrow',
 'immer': 'always',
 'der Termin': 'appointment',
 'die Rechnung': 'bill, invoice',
 'der Urlaub': 'holiday, vacation',
 'die Reise': 'trip, journey',
 'das Wetter': 'weather',
 'der Regen': 'rain',
 'die Erkältung': 'cold (illness)',
 'der Kopf': 'head',
 'der Bauch': 'belly, stomach',
 'die Apotheke': 'pharmacy',
 'der Schlüssel': 'key',
 'die Miete': 'rent',
 'der Nachbar': 'neighbour',
 'die Arbeit': 'work, job',
 'der Kollege': 'colleague',
 'anrufen': 'to call (phone)',
 'aufstehen': 'to get up',
 'einkaufen': 'to go shopping',
 'anfangen': 'to begin, to start',
 'aufhören': 'to stop, to quit',
 'helfen': 'to help',
 'warten': 'to wait',
 'bezahlen': 'to pay',
 'vergessen': 'to forget',
 'treffen': 'to meet',
 'bleiben': 'to stay',
 'wissen': 'to know (a fact)',
 'denken': 'to think',
 'müde': 'tired',
 'krank': 'sick, ill',
 'schnell': 'fast, quick',
 'leider': 'unfortunately',
 'die Erfahrung': 'experience',
 'die Bewerbung': 'job application',
 'der Lebenslauf': 'CV, résumé',
 'die Stelle': 'position, job',
 'das Gehalt': 'salary',
 'der Vertrag': 'contract',
 'die Prüfung': 'exam',
 'die Ausbildung': 'vocational training',
 'der Unterschied': 'difference',
 'die Meinung': 'opinion',
 'das Problem': 'problem',
 'die Lösung': 'solution',
 'das Gefühl': 'feeling',
 'die Umwelt': 'environment',
 'der Müll': 'rubbish, trash',
 'sich freuen': 'to be glad, to look forward to',
 'sich beeilen': 'to hurry',
 'erklären': 'to explain',
 'verstehen': 'to understand',
 'versuchen': 'to try',
 'entscheiden': 'to decide',
 'erzählen': 'to tell (a story)',
 'bekommen': 'to get, to receive',
 'verlieren': 'to lose',
 'gewinnen': 'to win',
 'vorbereiten': 'to prepare',
 'umziehen': 'to move (house)',
 'mitbringen': 'to bring along',
 'wichtig': 'important',
 'zufrieden': 'satisfied',
 'pünktlich': 'punctual, on time',
 'ziemlich': 'quite, fairly',
 'die Voraussetzung': 'prerequisite',
 'die Möglichkeit': 'possibility, opportunity',
 'die Entwicklung': 'development',
 'die Gesellschaft': 'society; company',
 'der Zusammenhang': 'context, connection',
 'die Verantwortung': 'responsibility',
 'die Behörde': 'authority, public office',
 'der Antrag': 'application (form)',
 'die Anmeldung': 'registration',
 'die Versicherung': 'insurance',
 'die Gesundheit': 'health',
 'der Vorteil': 'advantage',
 'der Nachteil': 'disadvantage',
 'die Ursache': 'cause',
 'die Folge': 'consequence',
 'sich bewerben': 'to apply (for a job)',
 'sich kümmern': 'to take care of',
 'sich gewöhnen': 'to get used to',
 'sich beschweren': 'to complain',
 'teilnehmen': 'to take part',
 'empfehlen': 'to recommend',
 'vergleichen': 'to compare',
 'beschreiben': 'to describe',
 'ausfüllen': 'to fill in (a form)',
 'unterschreiben': 'to sign',
 'kündigen': 'to cancel; to resign',
 'erreichen': 'to reach, to achieve',
 'sich erinnern': 'to remember',
 'deshalb': "therefore, that's why",
 'trotzdem': 'nevertheless, anyway',
 'ehrlich': 'honest',
 'selbstständig': 'independent; self-employed',
 'die Erwartung': 'expectation',
 'die Herausforderung': 'challenge',
 'die Fähigkeit': 'ability',
 'die Kenntnisse': 'knowledge, skills (pl.)',
 'das Ziel': 'goal, aim',
 'der Erfolg': 'success',
 'die Absicht': 'intention',
 'das Verhalten': 'behaviour',
 'die Beziehung': 'relationship',
 'der Streit': 'argument, quarrel',
 'die Ausnahme': 'exception',
 'der Zweck': 'purpose',
 'die Werbung': 'advertising',
 'der Verbraucher': 'consumer',
 'die Gelegenheit': 'opportunity, occasion',
 'sich verlassen': 'to rely on',
 'sich entschuldigen': 'to apologise',
 'vermeiden': 'to avoid',
 'verbessern': 'to improve; to correct',
 'überzeugen': 'to convince',
 'behaupten': 'to claim',
 'zweifeln': 'to doubt',
 'abhängen': 'to depend on',
 'erledigen': 'to take care of, to get done',
 'verschieben': 'to postpone',
 'zunehmen': 'to increase; to gain weight',
 'abnehmen': 'to decrease; to lose weight',
 'sich vorstellen': 'to introduce oneself; to imagine',
 'eigentlich': 'actually',
 'allerdings': 'however, though',
 'vorsichtig': 'careful',
 'neugierig': 'curious',
 'die Auswirkung': 'effect, impact',
 'die Maßnahme': 'measure (action)',
 'der Aufwand': 'effort, expense',
 'die Bedingung': 'condition',
 'die Einstellung': 'attitude; setting; hiring',
 'die Forderung': 'demand',
 'der Vorwurf': 'reproach, accusation',
 'die Ansicht': 'view, opinion',
 'das Vorurteil': 'prejudice',
 'die Zuverlässigkeit': 'reliability',
 'der Wettbewerb': 'competition',
 'die Nachhaltigkeit': 'sustainability',
 'die Begründung': 'justification, reasoning',
 'der Umgang': 'handling, dealing with',
 'der Anspruch': 'claim, entitlement',
 'beitragen': 'to contribute',
 'berücksichtigen': 'to take into account',
 'bewältigen': 'to cope with, to master',
 'ermöglichen': 'to enable',
 'beeinflussen': 'to influence',
 'darstellen': 'to represent, to present',
 'sich auseinandersetzen': 'to deal with, to engage with',
 'feststellen': 'to find, to establish',
 'verzichten': 'to do without, to waive',
 'bestehen': 'to pass (exam); to insist; to consist',
 'nachweisen': 'to prove',
 'gewährleisten': 'to guarantee, to ensure',
 'offensichtlich': 'obvious(ly)',
 'ausreichend': 'sufficient',
 'umfangreich': 'extensive',
 'dennoch': 'nevertheless',
 'nachvollziehbar': 'comprehensible, understandable',
 'der Einfluss': 'influence',
 'die Grundlage': 'basis, foundation',
 'der Zustand': 'state, condition',
 'die Abhängigkeit': 'dependence; addiction',
 'der Beitrag': 'contribution; fee; article',
 'die Wahrnehmung': 'perception',
 'der Vorgang': 'process, procedure',
 'die Einschränkung': 'restriction',
 'die Vereinbarung': 'agreement',
 'die Umsetzung': 'implementation',
 'der Schwerpunkt': 'focus, main emphasis',
 'die Haltung': 'attitude, stance',
 'die Bereitschaft': 'willingness, readiness',
 'der Rückgang': 'decline',
 'umsetzen': 'to implement',
 'hervorheben': 'to emphasise',
 'einschätzen': 'to assess, to estimate',
 'ablehnen': 'to reject, to decline',
 'zustimmen': 'to agree',
 'widersprechen': 'to contradict',
 'sich durchsetzen': 'to prevail, to assert oneself',
 'ausgehen': 'to assume; to go out',
 'übernehmen': 'to take over',
 'verfügen': "to have at one's disposal",
 'bewirken': 'to bring about',
 'vorkommen': 'to occur, to happen',
 'zwangsläufig': 'inevitably',
 'erheblich': 'considerable',
 'weitgehend': 'largely',
 'beziehungsweise': 'or; respectively',
 'gegebenenfalls': 'if necessary',
 'die Annahme': 'assumption; acceptance',
 'der Ansatz': 'approach',
 'die Tragweite': 'scope, significance',
 'der Sachverhalt': 'facts of the case',
 'die Befugnis': 'authority, power',
 'die Beeinträchtigung': 'impairment',
 'der Verdacht': 'suspicion',
 'die Rücksicht': 'consideration',
 'die Anerkennung': 'recognition',
 'der Missbrauch': 'abuse, misuse',
 'die Schwachstelle': 'weak point, vulnerability',
 'die Bedrohung': 'threat',
 'der Aufschwung': 'upswing, boom',
 'beanspruchen': 'to claim; to strain',
 'erörtern': 'to discuss',
 'veranlassen': 'to arrange; to prompt',
 'beheben': 'to fix, to remedy',
 'beimessen': 'to attach (importance)',
 'unterstellen': 'to insinuate, to impute',
 'sich erweisen': 'to prove (to be)',
 'abwägen': 'to weigh up',
 'einräumen': 'to concede, to admit',
 'anstreben': 'to aim for',
 'beruhen': 'to be based on',
 'bewerkstelligen': 'to accomplish',
 'maßgeblich': 'decisive',
 'nachhaltig': 'sustainable; lasting',
 'ausschlaggebend': 'decisive',
 'vorläufig': 'provisional',
 'stichhaltig': 'sound, valid (argument)',
 'die Gepflogenheit': 'custom, practice',
 'der Einwand': 'objection',
 'die Zuständigkeit': 'responsibility, jurisdiction',
 'die Wechselwirkung': 'interaction',
 'der Spielraum': 'leeway, scope',
 'das Anliegen': 'concern, request',
 'der Werdegang': 'career path, background',
 'die Gratwanderung': 'balancing act, tightrope walk',
 'die Nachfrage': 'demand',
 'das Ausmaß': 'extent, scale',
 'der Nachdruck': 'emphasis',
 'die Hürde': 'hurdle',
 'der Kompromiss': 'compromise',
 'bemängeln': 'to criticise, to find fault',
 'sich herausstellen': 'to turn out',
 'nachgehen': 'to pursue, to look into',
 'zurückgreifen': 'to fall back on',
 'entgegenwirken': 'to counteract',
 'vorbeugen': 'to prevent',
 'in Kauf nehmen': 'to accept (a downside)',
 'sich bewähren': 'to prove oneself',
 'beeinträchtigen': 'to impair, to affect',
 'hinterfragen': 'to question',
 'aufgreifen': 'to take up (a topic)',
 'unumgänglich': 'unavoidable',
 'zweckmäßig': 'expedient, practical',
 'einschlägig': 'relevant (to the field)',
 'zeitnah': 'promptly',
 'ohnehin': 'anyway',
 'die Befangenheit': 'bias; self-consciousness',
 'der Duktus': 'style, manner',
 'die Zwickmühle': 'dilemma',
 'der Hintergedanke': 'ulterior motive',
 'die Gemengelage': 'complex mix, tangled situation',
 'der Schachzug': 'move, gambit',
 'die Stellungnahme': 'statement, position paper',
 'der Sinneswandel': 'change of heart',
 'die Fahrlässigkeit': 'negligence',
 'das Unterfangen': 'venture, undertaking',
 'anprangern': 'to denounce',
 'beschönigen': 'to gloss over',
 'verharmlosen': 'to play down',
 'ausloten': 'to sound out, to explore',
 'untermauern': 'to substantiate',
 'sich anbahnen': 'to be in the offing',
 'beipflichten': 'to agree with',
 'vereiteln': 'to thwart',
 'erwägen': 'to consider',
 'ins Gewicht fallen': 'to carry weight',
 'auf der Hand liegen': 'to be obvious',
 'unverblümt': 'blunt(ly)',
 'eklatant': 'glaring, flagrant',
 'ungeachtet': 'notwithstanding',
 'tunlichst': 'if at all possible',
 'mitnichten': 'by no means',
 'gewissermaßen': 'so to speak, to some extent',
 'die Augenwischerei': 'eyewash, window dressing',
 'der Spagat': 'balancing act',
 'die Haarspalterei': 'hair-splitting',
 'der Kuhhandel': 'horse-trading',
 'die Fallstricke': 'pitfalls',
 'das Kalkül': 'calculation, strategy',
 'der Wermutstropfen': 'fly in the ointment',
 'die Gesinnung': 'mindset, convictions',
 'der Tunnelblick': 'tunnel vision',
 'die Bredouille': 'predicament, fix',
 'sich ins Zeug legen': 'to go all out',
 'den Kürzeren ziehen': 'to get the short end of the stick',
 'unter den Teppich kehren': 'to sweep under the rug',
 'auf den Busch klopfen': 'to sound someone out',
 'ins Fettnäpfchen treten': "to put one's foot in it",
 'kolportieren': 'to spread (rumours)',
 'lavieren': 'to manoeuvre, to equivocate',
 'brüskieren': 'to snub',
 'konterkarieren': 'to thwart, to counteract',
 'sich etwas verbitten': 'to not tolerate something',
 'sich etwas anmaßen': 'to presume, to arrogate',
 'lapidar': 'terse, succinct',
 'despektierlich': 'disrespectful',
 'obsolet': 'obsolete',
 'sukzessive': 'gradually',
 'ostentativ': 'ostentatious(ly)',
 'vehement': 'vehement(ly)',
 'hallo': 'hello',
 'guten Morgen': 'good morning',
 'guten Tag': 'good afternoon',
 'guten Abend': 'good evening',
 'gute Nacht': 'good night',
 'tschüss': 'bye',
 'auf Wiedersehen': 'goodbye',
 'bis später': 'see you later',
 'bis morgen': 'see you tomorrow',
 'bis bald': 'see you soon',
 'ja': 'yes',
 'nein': 'no',
 'vielleicht': 'maybe',
 'bitte': 'please',
 'danke': 'thanks',
 'danke schön': 'thank you very much',
 'gern geschehen': "you're welcome",
 'entschuldigung': 'excuse me',
 'es tut mir leid': "I'm sorry",
 'kein Problem': 'no problem',
 "wie geht's?": 'how are you?',
 'mir geht es gut': "I'm fine",
 'und dir?': 'and you?',
 'willkommen': 'welcome',
 'herzlich willkommen': 'a warm welcome',
 'mein Name ist ...': 'my name is …',
 'ich heiße ...': "I'm called …",
 'freut mich': 'nice to meet you',
 'wie bitte?': 'pardon?',
 'ich verstehe nicht': "I don't understand",
 'langsam bitte': 'slowly, please',
 'noch einmal': 'once more',
 'natürlich': 'of course',
 'genau': 'exactly',
 'stimmt': 'right',
 'okay': 'okay',
 'in Ordnung': 'all right',
 'viel Glück': 'good luck',
 'viel Spaß': 'have fun',
 'gute Reise': 'have a good trip',
 'guten Appetit': 'enjoy your meal',
 'prost': 'cheers',
 'herzlichen Glückwunsch': 'congratulations',
 'alles Gute': 'all the best',
 'gute Besserung': 'get well soon',
 'schönes Wochenende': 'have a nice weekend',
 'bitte schön': 'here you are',
 'Verzeihung': 'pardon me',
 'Achtung': 'attention',
 'Hilfe!': 'help!',
 'null': 'zero',
 'eins': 'one',
 'zwei': 'two',
 'drei': 'three',
 'vier': 'four',
 'fünf': 'five',
 'sechs': 'six',
 'sieben': 'seven',
 'acht': 'eight',
 'neun': 'nine',
 'zehn': 'ten',
 'elf': 'eleven',
 'zwölf': 'twelve',
 'dreizehn': 'thirteen',
 'vierzehn': 'fourteen',
 'fünfzehn': 'fifteen',
 'sechzehn': 'sixteen',
 'siebzehn': 'seventeen',
 'achtzehn': 'eighteen',
 'neunzehn': 'nineteen',
 'zwanzig': 'twenty',
 'dreißig': 'thirty',
 'vierzig': 'forty',
 'fünfzig': 'fifty',
 'sechzig': 'sixty',
 'siebzig': 'seventy',
 'achtzig': 'eighty',
 'neunzig': 'ninety',
 'hundert': 'hundred',
 'tausend': 'thousand',
 'die Million': 'million',
 'erste': 'first',
 'zweite': 'second',
 'dritte': 'third',
 'letzte': 'last',
 'halb': 'half',
 'die Hälfte': 'half (noun)',
 'das Viertel': 'quarter',
 'das Paar': 'pair',
 'das Dutzend': 'dozen',
 'viel': 'much, a lot',
 'wenig': 'little, few',
 'mehr': 'more',
 'weniger': 'less',
 'genug': 'enough',
 'alle': 'all',
 'nichts': 'nothing',
 'etwas': 'something, some',
 'die Zahl': 'number',
 'die Nummer': 'number (phone, house)',
 'das Prozent': 'percent',
 'das Stück': 'piece',
 'das Kilo': 'kilo',
 'das Gramm': 'gram',
 'der Liter': 'litre',
 'die Farbe': 'colour',
 'rot': 'red',
 'blau': 'blue',
 'gelb': 'yellow',
 'grün': 'green',
 'schwarz': 'black',
 'weiß': 'white',
 'grau': 'grey',
 'braun': 'brown',
 'orange': 'orange',
 'rosa': 'pink',
 'lila': 'purple',
 'bunt': 'colourful',
 'hell': 'light, bright',
 'dunkel': 'dark',
 'der Kreis': 'circle',
 'das Quadrat': 'square',
 'die Linie': 'line',
 'rund': 'round',
 'ich': 'I',
 'du': 'you',
 'er': 'he',
 'sie': 'she, they',
 'es': 'it',
 'wir': 'we',
 'ihr': 'you (plural)',
 'mein': 'my',
 'dein': 'your',
 'unser': 'our',
 'euer': 'your (plural)',
 'mich': 'me',
 'dich': 'you (object)',
 'mir': '(to) me',
 'dir': '(to) you',
 'man': 'one (people in general)',
 'der': 'the (masculine)',
 'die': 'the (feminine)',
 'das': 'the (neuter)',
 'ein': 'a, an (masc./neut.)',
 'eine': 'a, an (feminine)',
 'kein': 'no, not a',
 'dieser': 'this',
 'jener': 'that',
 'jeder': 'every, each',
 'einige': 'some',
 'andere': 'others',
 'selbst': 'oneself, -self',
 'und': 'and',
 'oder': 'or',
 'aber': 'but',
 'denn': 'because',
 'weil': 'because',
 'dass': 'that',
 'wenn': 'if, when',
 'als': 'when, than',
 'ob': 'whether',
 'obwohl': 'although',
 'damit': 'so that',
 'also': 'so, therefore',
 'sondern': 'but rather',
 'sowohl ... als auch': 'both … and',
 'entweder ... oder': 'either … or',
 'weder ... noch': 'neither … nor',
 'in': 'in',
 'an': 'at, on',
 'auf': 'on, onto',
 'unter': 'under',
 'über': 'over, about',
 'vor': 'in front of, before',
 'hinter': 'behind',
 'neben': 'next to',
 'zwischen': 'between',
 'bei': 'at, with (someone)',
 'mit': 'with',
 'ohne': 'without',
 'für': 'for',
 'gegen': 'against',
 'von': 'from, of',
 'zu': 'to',
 'nach': 'after, to',
 'aus': 'out of, from',
 'seit': 'since',
 'bis': 'until',
 'durch': 'through',
 'um': 'around, at (time)',
 'während': 'during',
 'wegen': 'because of',
 'statt': 'instead of',
 'außer': 'except',
 'gegenüber': 'opposite',
 'wer': 'who',
 'was': 'what',
 'wo': 'where',
 'wohin': 'where to',
 'woher': 'where from',
 'wann': 'when',
 'wie': 'how',
 'warum': 'why',
 'wieso': 'how come',
 'weshalb': 'why',
 'welcher': 'which',
 'wie viel': 'how much',
 'wie viele': 'how many',
 'wie lange': 'how long',
 'wie oft': 'how often',
 'wie weit': 'how far',
 'wem': '(to) whom',
 'wen': 'whom',
 'wessen': 'whose',
 'die Frage': 'question',
 'die Zeit': 'time',
 'die Stunde': 'hour',
 'die Minute': 'minute',
 'die Sekunde': 'second',
 'der Monat': 'month',
 'das Jahr': 'year',
 'der Morgen': 'morning',
 'der Vormittag': 'late morning',
 'der Mittag': 'noon',
 'der Nachmittag': 'afternoon',
 'der Abend': 'evening',
 'die Nacht': 'night',
 'gestern': 'yesterday',
 'übermorgen': 'the day after tomorrow',
 'vorgestern': 'the day before yesterday',
 'jetzt': 'now',
 'gleich': 'right away, in a moment',
 'sofort': 'immediately',
 'später': 'later',
 'früher': 'earlier',
 'bald': 'soon',
 'gerade': 'just now',
 'nie': 'never',
 'manchmal': 'sometimes',
 'oft': 'often',
 'selten': 'rarely',
 'meistens': 'mostly',
 'täglich': 'daily',
 'wöchentlich': 'weekly',
 'monatlich': 'monthly',
 'jährlich': 'yearly',
 'der Montag': 'Monday',
 'der Dienstag': 'Tuesday',
 'der Mittwoch': 'Wednesday',
 'der Donnerstag': 'Thursday',
 'der Freitag': 'Friday',
 'der Samstag': 'Saturday',
 'der Sonntag': 'Sunday',
 'das Wochenende': 'weekend',
 'der Werktag': 'working day',
 'der Feiertag': 'public holiday',
 'der Januar': 'January',
 'der Februar': 'February',
 'der März': 'March',
 'der April': 'April',
 'der Mai': 'May',
 'der Juni': 'June',
 'der Juli': 'July',
 'der August': 'August',
 'der September': 'September',
 'der Oktober': 'October',
 'der November': 'November',
 'der Dezember': 'December',
 'der Frühling': 'spring',
 'der Sommer': 'summer',
 'der Herbst': 'autumn',
 'der Winter': 'winter',
 'die Jahreszeit': 'season',
 'das Datum': 'date',
 'der Kalender': 'calendar',
 'die Vergangenheit': 'past',
 'die Gegenwart': 'present',
 'die Zukunft': 'future',
 'der Geburtstag': 'birthday',
 'die Verspätung': 'delay',
 'der Mensch': 'human being',
 'die Leute': 'people',
 'die Person': 'person',
 'der Junge': 'boy',
 'das Mädchen': 'girl',
 'das Baby': 'baby',
 'die Eltern': 'parents',
 'der Sohn': 'son',
 'die Tochter': 'daughter',
 'der Bruder': 'brother',
 'die Schwester': 'sister',
 'die Geschwister': 'siblings',
 'die Großeltern': 'grandparents',
 'der Großvater': 'grandfather',
 'die Großmutter': 'grandmother',
 'der Opa': 'grandpa',
 'die Oma': 'grandma',
 'der Enkel': 'grandson',
 'der Onkel': 'uncle',
 'die Tante': 'aunt',
 'der Cousin': 'cousin (male)',
 'die Cousine': 'cousin (female)',
 'der Neffe': 'nephew',
 'die Nichte': 'niece',
 'der Schwiegervater': 'father-in-law',
 'die Schwiegermutter': 'mother-in-law',
 'der Ehemann': 'husband',
 'die Ehefrau': 'wife',
 'der Partner': 'partner',
 'die Freundin': 'girlfriend, friend',
 'der Gast': 'guest',
 'der Erwachsene': 'adult',
 'der Jugendliche': 'teenager',
 'der Vorname': 'first name',
 'der Nachname': 'surname',
 'das Alter': 'age',
 'die Hochzeit': 'wedding',
 'die Ehe': 'marriage',
 'die Liebe': 'love',
 'die Freundschaft': 'friendship',
 'ledig': 'single',
 'verheiratet': 'married',
 'geschieden': 'divorced',
 'schwanger': 'pregnant',
 'verwandt': 'related',
 'der Körper': 'body',
 'das Haar': 'hair',
 'das Gesicht': 'face',
 'das Auge': 'eye',
 'die Nase': 'nose',
 'der Mund': 'mouth',
 'das Ohr': 'ear',
 'der Zahn': 'tooth',
 'der Hals': 'neck, throat',
 'der Arm': 'arm',
 'die Hand': 'hand',
 'der Finger': 'finger',
 'der Rücken': 'back',
 'das Bein': 'leg',
 'das Knie': 'knee',
 'der Fuß': 'foot',
 'die Haut': 'skin',
 'das Herz': 'heart',
 'das Blut': 'blood',
 'die Krankheit': 'illness',
 'gesund': 'healthy',
 'die Schmerzen': 'pain',
 'die Kopfschmerzen': 'headache',
 'das Fieber': 'fever',
 'der Husten': 'cough',
 'die Grippe': 'flu',
 'die Allergie': 'allergy',
 'die Wunde': 'wound',
 'der Unfall': 'accident',
 'die Ärztin': 'doctor (female)',
 'der Zahnarzt': 'dentist',
 'das Krankenhaus': 'hospital',
 'die Praxis': "doctor's office",
 'das Medikament': 'medicine',
 'die Tablette': 'pill',
 'das Rezept': 'prescription',
 'die Untersuchung': 'examination',
 'die Krankenkasse': 'health insurance',
 'die Versichertenkarte': 'insurance card',
 'die Notaufnahme': 'emergency room',
 'der Krankenwagen': 'ambulance',
 'die Behandlung': 'treatment',
 'schwach': 'weak',
 'stark': 'strong',
 'die Brille': 'glasses',
 'sich ausruhen': 'to rest',
 'weh tun': 'to hurt',
 'sich fühlen': 'to feel',
 'atmen': 'to breathe',
 'heilen': 'to heal',
 'das Wohnzimmer': 'living room',
 'das Schlafzimmer': 'bedroom',
 'das Badezimmer': 'bathroom',
 'die Toilette': 'toilet',
 'der Flur': 'hallway',
 'der Balkon': 'balcony',
 'der Garten': 'garden',
 'der Keller': 'basement',
 'die Tür': 'door',
 'das Fenster': 'window',
 'die Wand': 'wall',
 'der Boden': 'floor',
 'die Decke': 'ceiling, blanket',
 'das Dach': 'roof',
 'die Treppe': 'stairs',
 'der Aufzug': 'lift, elevator',
 'das Schloss': 'lock, castle',
 'die Möbel': 'furniture',
 'der Sessel': 'armchair',
 'das Sofa': 'sofa',
 'der Schrank': 'cupboard, wardrobe',
 'das Regal': 'shelf',
 'die Lampe': 'lamp',
 'das Licht': 'light',
 'der Teppich': 'carpet',
 'der Spiegel': 'mirror',
 'das Bild': 'picture',
 'das Handtuch': 'towel',
 'die Seife': 'soap',
 'die Zahnbürste': 'toothbrush',
 'die Zahnpasta': 'toothpaste',
 'das Shampoo': 'shampoo',
 'die Dusche': 'shower',
 'das Waschbecken': 'washbasin',
 'die Waschmaschine': 'washing machine',
 'der Kühlschrank': 'fridge',
 'der Herd': 'stove, cooker',
 'der Backofen': 'oven',
 'die Spülmaschine': 'dishwasher',
 'die Heizung': 'heating',
 'die Klimaanlage': 'air conditioning',
 'der Mülleimer': 'bin',
 'die Steckdose': 'socket',
 'der Stecker': 'plug',
 'der Mieter': 'tenant',
 'der Vermieter': 'landlord',
 'die Nebenkosten': 'additional costs',
 'die Kaution': 'deposit',
 'der Mietvertrag': 'rental agreement',
 'der Hausmeister': 'caretaker',
 'die Adresse': 'address',
 'die Hausnummer': 'house number',
 'die Postleitzahl': 'postcode',
 'das Stockwerk': 'floor, storey',
 'das Erdgeschoss': 'ground floor',
 'der Umzug': 'move (house)',
 'die Hausarbeit': 'housework',
 'putzen': 'to clean',
 'aufräumen': 'to tidy up',
 'waschen': 'to wash',
 'kochen': 'to cook',
 'mieten': 'to rent',
 'gemütlich': 'cosy',
 'sauber': 'clean',
 'schmutzig': 'dirty',
 'das Essen': 'food, meal',
 'das Getränk': 'drink',
 'das Frühstück': 'breakfast',
 'das Mittagessen': 'lunch',
 'das Abendessen': 'dinner',
 'der Hunger': 'hunger',
 'der Durst': 'thirst',
 'hungrig': 'hungry',
 'durstig': 'thirsty',
 'das Brötchen': 'bread roll',
 'die Butter': 'butter',
 'der Käse': 'cheese',
 'das Ei': 'egg',
 'der Joghurt': 'yoghurt',
 'die Sahne': 'cream',
 'das Fleisch': 'meat',
 'das Rindfleisch': 'beef',
 'das Hähnchen': 'chicken',
 'das Schweinefleisch': 'pork',
 'die Wurst': 'sausage',
 'der Schinken': 'ham',
 'der Fisch': 'fish',
 'die Suppe': 'soup',
 'der Salat': 'salad',
 'die Kartoffel': 'potato',
 'die Tomate': 'tomato',
 'die Gurke': 'cucumber',
 'die Zwiebel': 'onion',
 'der Knoblauch': 'garlic',
 'die Karotte': 'carrot',
 'der Pfeffer': 'pepper (spice)',
 'die Paprika': 'pepper (vegetable)',
 'der Reis': 'rice',
 'die Nudeln': 'pasta, noodles',
 'das Mehl': 'flour',
 'der Zucker': 'sugar',
 'das Salz': 'salt',
 'das Öl': 'oil',
 'der Apfel': 'apple',
 'die Banane': 'banana',
 'die Orange': 'orange',
 'die Zitrone': 'lemon',
 'die Erdbeere': 'strawberry',
 'der Kuchen': 'cake',
 'die Schokolade': 'chocolate',
 'das Eis': 'ice cream, ice',
 'der Honig': 'honey',
 'die Marmelade': 'jam',
 'der Tee': 'tea',
 'der Saft': 'juice',
 'das Bier': 'beer',
 'der Wein': 'wine',
 'die Limonade': 'lemonade',
 'die Flasche': 'bottle',
 'das Glas': 'glass',
 'die Tasse': 'cup',
 'der Teller': 'plate',
 'die Gabel': 'fork',
 'das Messer': 'knife',
 'der Löffel': 'spoon',
 'der Topf': 'pot',
 'die Pfanne': 'pan',
 'das Restaurant': 'restaurant',
 'das Café': 'café',
 'die Speisekarte': 'menu',
 'das Trinkgeld': 'tip',
 'der Kellner': 'waiter',
 'die Bestellung': 'order',
 'die Vorspeise': 'starter',
 'das Hauptgericht': 'main course',
 'die Nachspeise': 'dessert',
 'die Zutat': 'ingredient',
 'lecker': 'delicious',
 'süß': 'sweet',
 'salzig': 'salty',
 'sauer': 'sour',
 'scharf': 'spicy, sharp',
 'frisch': 'fresh',
 'gekocht': 'cooked, boiled',
 'backen': 'to bake',
 'braten': 'to fry',
 'schneiden': 'to cut',
 'probieren': 'to try, to taste',
 'bestellen': 'to order',
 'satt': 'full (after eating)',
 'vegetarisch': 'vegetarian',
 'die Kleidung': 'clothes',
 'das Hemd': 'shirt',
 'das T-Shirt': 'T-shirt',
 'der Pullover': 'jumper, sweater',
 'die Jacke': 'jacket',
 'der Mantel': 'coat',
 'die Hose': 'trousers',
 'die Jeans': 'jeans',
 'der Rock': 'skirt',
 'das Kleid': 'dress',
 'die Socke': 'sock',
 'die Unterwäsche': 'underwear',
 'der Schuh': 'shoe',
 'der Hut': 'hat',
 'die Mütze': 'cap, beanie',
 'der Schal': 'scarf',
 'der Gürtel': 'belt',
 'die Tasche': 'bag',
 'der Rucksack': 'backpack',
 'der Regenschirm': 'umbrella',
 'der Schmuck': 'jewellery',
 'die Größe': 'size',
 'anziehen': 'to put on',
 'ausziehen': 'to take off',
 'tragen': 'to wear, to carry',
 'anprobieren': 'to try on',
 'passen': 'to fit',
 'stehen': 'to suit, to stand',
 'eng': 'tight, narrow',
 'weit': 'wide, far',
 'modisch': 'fashionable',
 'bequem': 'comfortable',
 'die Umkleidekabine': 'changing room',
 'die Wäsche': 'laundry',
 'die Marke': 'brand',
 'die Mode': 'fashion',
 'die Sonnenbrille': 'sunglasses',
 'das Dorf': 'village',
 'das Zentrum': 'centre',
 'die Innenstadt': 'city centre',
 'der Platz': 'square, place',
 'der Park': 'park',
 'die Brücke': 'bridge',
 'der Fluss': 'river',
 'das Gebäude': 'building',
 'die Kirche': 'church',
 'die Moschee': 'mosque',
 'das Museum': 'museum',
 'das Theater': 'theatre',
 'das Kino': 'cinema',
 'die Bibliothek': 'library',
 'die Schule': 'school',
 'die Universität': 'university',
 'das Rathaus': 'town hall',
 'die Post': 'post office',
 'die Bank': 'bank',
 'das Hotel': 'hotel',
 'das Geschäft': 'shop',
 'der Laden': 'store',
 'die Bäckerei': 'bakery',
 'die Metzgerei': "butcher's",
 'der Markt': 'market',
 'das Einkaufszentrum': 'shopping centre',
 'die Tankstelle': 'petrol station',
 'der Parkplatz': 'car park',
 'die Haltestelle': 'stop (bus, tram)',
 'der Flughafen': 'airport',
 'der Hafen': 'harbour, port',
 'das Stadion': 'stadium',
 'das Schwimmbad': 'swimming pool',
 'das Fitnessstudio': 'gym',
 'der Friseur': 'hairdresser',
 'die Polizei': 'police',
 'die Feuerwehr': 'fire brigade',
 'der Zoo': 'zoo',
 'die Ecke': 'corner',
 'die Kreuzung': 'crossroads',
 'die Ampel': 'traffic light',
 'der Gehweg': 'pavement',
 'der Weg': 'way, path',
 'die Richtung': 'direction',
 'rechts': 'right',
 'links': 'left',
 'geradeaus': 'straight ahead',
 'oben': 'above, upstairs',
 'unten': 'below, downstairs',
 'vorne': 'at the front',
 'hinten': 'at the back',
 'die Mitte': 'middle',
 'die Seite': 'side, page',
 'nah': 'near',
 'die Umgebung': 'surroundings',
 'der Ort': 'place, location',
 'die Gegend': 'area, region',
 'die Grenze': 'border',
 'die Hauptstadt': 'capital city',
 'der Einwohner': 'inhabitant',
 'die Sehenswürdigkeit': 'sight (tourist attraction)',
 'das Denkmal': 'monument',
 'der Turm': 'tower',
 'die Aussicht': 'view',
 'der Verkehr': 'traffic',
 'das Auto': 'car',
 'die Bahn': 'train, railway',
 'der Zug': 'train',
 'die S-Bahn': 'suburban train',
 'die U-Bahn': 'underground, subway',
 'die Straßenbahn': 'tram',
 'das Fahrrad': 'bicycle',
 'das Motorrad': 'motorbike',
 'das Taxi': 'taxi',
 'das Flugzeug': 'plane',
 'das Schiff': 'ship',
 'der Führerschein': 'driving licence',
 'die Fahrkarte': 'ticket',
 'das Ticket': 'ticket',
 'der Fahrplan': 'timetable',
 'das Gleis': 'platform, track',
 'der Ausgang': 'exit',
 'der Eingang': 'entrance',
 'die Abfahrt': 'departure',
 'die Ankunft': 'arrival',
 'der Aufenthalt': 'stay, stopover',
 'die Verbindung': 'connection',
 'umsteigen': 'to change (trains)',
 'einsteigen': 'to get on',
 'aussteigen': 'to get off',
 'fliegen': 'to fly',
 'laufen': 'to walk, to run',
 'zu Fuß': 'on foot',
 'die Autobahn': 'motorway',
 'die Geschwindigkeit': 'speed',
 'das Benzin': 'petrol',
 'der Motor': 'engine',
 'das Rad': 'wheel',
 'der Reifen': 'tyre',
 'die Panne': 'breakdown',
 'die Strecke': 'route, distance',
 'die Entfernung': 'distance',
 'der Koffer': 'suitcase',
 'das Gepäck': 'luggage',
 'der Pass': 'passport',
 'das Visum': 'visa',
 'der Ausweis': 'ID card',
 'der Zoll': 'customs',
 'die Buchung': 'booking',
 'die Unterkunft': 'accommodation',
 'die Jugendherberge': 'youth hostel',
 'das Zelt': 'tent',
 'die Ferien': 'school holidays',
 'der Ausflug': 'excursion, trip',
 'die Tour': 'tour',
 'der Tourist': 'tourist',
 'die Karte': 'map, card',
 'das Navi': 'satnav',
 'der Stau': 'traffic jam',
 'die Baustelle': 'construction site, roadworks',
 'besichtigen': 'to visit, to sightsee',
 'reservieren': 'to reserve, to book',
 'packen': 'to pack',
 'ankommen': 'to arrive',
 'abfahren': 'to depart, to leave',
 'verpassen': 'to miss',
 'die Sicherheit': 'safety, security',
 'der Euro': 'euro',
 'der Cent': 'cent',
 'die Kasse': 'checkout, till',
 'die Quittung': 'receipt',
 'der Kunde': 'customer',
 'der Verkäufer': 'salesperson',
 'der Einkauf': 'shopping, purchase',
 'die Einkaufsliste': 'shopping list',
 'der Einkaufswagen': 'shopping trolley',
 'die Tüte': 'plastic bag',
 'das Angebot': 'offer, deal',
 'der Rabatt': 'discount',
 'der Ausverkauf': 'clearance sale',
 'kostenlos': 'free of charge',
 'günstig': 'good value',
 'das Bargeld': 'cash',
 'die Kreditkarte': 'credit card',
 'die EC-Karte': 'debit card',
 'das Konto': 'account',
 'die Überweisung': 'bank transfer',
 'die Bankleitzahl': 'bank sort code',
 'die IBAN': 'IBAN',
 'der Geldautomat': 'cash machine, ATM',
 'das Wechselgeld': 'change (money)',
 'die Steuer': 'tax',
 'die Mehrwertsteuer': 'VAT',
 'die Gebühr': 'fee',
 'die Kosten': 'costs',
 'das Einkommen': 'income',
 'sparen': 'to save',
 'ausgeben': 'to spend',
 'verkaufen': 'to sell',
 'umtauschen': 'to exchange',
 'zurückgeben': 'to give back, to return',
 'die Garantie': 'guarantee',
 'die Lieferung': 'delivery',
 'die Ware': 'goods',
 'das Produkt': 'product',
 'die Qualität': 'quality',
 'die Menge': 'amount, quantity',
 'die Auswahl': 'choice, selection',
 'die Reklamation': 'complaint (return)',
 'die Rate': 'instalment',
 'die Schulden': 'debts',
 'der Beruf': 'profession',
 'der Job': 'job',
 'die Firma': 'firm, company',
 'das Unternehmen': 'company, business',
 'das Büro': 'office',
 'der Chef': 'boss',
 'der Mitarbeiter': 'employee',
 'das Team': 'team',
 'die Abteilung': 'department',
 'die Besprechung': 'meeting',
 'die Sitzung': 'meeting, session',
 'der Auftrag': 'order, assignment',
 'die Aufgabe': 'task',
 'das Projekt': 'project',
 'das Praktikum': 'internship',
 'das Vorstellungsgespräch': 'job interview',
 'die Kündigung': 'notice, resignation',
 'die Arbeitszeit': 'working hours',
 'die Überstunde': 'overtime',
 'die Pause': 'break',
 'die Schicht': 'shift',
 'der Feierabend': 'end of the working day',
 'die Vollzeit': 'full-time',
 'die Teilzeit': 'part-time',
 'der Minijob': 'mini-job',
 'der Werkstudent': 'working student',
 'arbeitslos': 'unemployed',
 'der Lehrer': 'teacher',
 'der Ingenieur': 'engineer',
 'der Anwalt': 'lawyer',
 'der Koch': 'cook, chef',
 'der Bäcker': 'baker',
 'der Fahrer': 'driver',
 'der Polizist': 'police officer',
 'der Krankenpfleger': 'nurse (male)',
 'die Krankenschwester': 'nurse',
 'der Handwerker': 'craftsman, tradesman',
 'der Elektriker': 'electrician',
 'der Mechaniker': 'mechanic',
 'der Programmierer': 'programmer',
 'der Informatiker': 'computer scientist',
 'der Architekt': 'architect',
 'der Künstler': 'artist',
 'der Journalist': 'journalist',
 'der Beamte': 'civil servant',
 'der Student': 'student (university)',
 'der Praktikant': 'intern',
 'der Rentner': 'pensioner',
 'verdienen': 'to earn',
 'leiten': 'to lead, to manage',
 'bewerben': 'to apply',
 'einstellen': 'to hire',
 'die Karriere': 'career',
 'die Beförderung': 'promotion',
 'der Kindergarten': 'kindergarten',
 'die Grundschule': 'primary school',
 'das Gymnasium': 'grammar school, high school',
 'die Hochschule': 'university, college',
 'der Unterricht': 'lessons, class',
 'das Fach': 'subject',
 'die Klasse': 'class, grade',
 'der Kurs': 'course',
 'die Vorlesung': 'lecture',
 'das Seminar': 'seminar',
 'der Schüler': 'pupil',
 'der Professor': 'professor',
 'die Hausaufgabe': 'homework',
 'der Test': 'test',
 'die Note': 'grade, mark',
 'das Zeugnis': 'school report, certificate',
 'das Abitur': 'school-leaving exam (A levels)',
 'das Studium': 'university studies',
 'der Abschluss': 'degree, qualification',
 'der Bachelor': "bachelor's degree",
 'der Master': "master's degree",
 'das Semester': 'semester',
 'das Buch': 'book',
 'das Heft': 'notebook',
 'das Blatt': 'sheet, leaf',
 'das Papier': 'paper',
 'der Stift': 'pen',
 'der Bleistift': 'pencil',
 'der Kugelschreiber': 'ballpoint pen',
 'der Radiergummi': 'eraser',
 'das Lineal': 'ruler',
 'die Schere': 'scissors',
 'die Tafel': 'board',
 'der Schreibtisch': 'desk',
 'das Wörterbuch': 'dictionary',
 'die Grammatik': 'grammar',
 'das Wort': 'word',
 'der Satz': 'sentence',
 'der Text': 'text',
 'die Übung': 'exercise',
 'der Fehler': 'mistake',
 'die Antwort': 'answer',
 'das Beispiel': 'example',
 'das Thema': 'topic',
 'das Wissen': 'knowledge',
 'studieren': 'to study (at university)',
 'lehren': 'to teach',
 'üben': 'to practise',
 'wiederholen': 'to repeat',
 'rechnen': 'to calculate',
 'durchfallen': 'to fail (an exam)',
 'die Mathematik': 'maths',
 'die Physik': 'physics',
 'die Chemie': 'chemistry',
 'die Biologie': 'biology',
 'die Geschichte': 'history, story',
 'die Erdkunde': 'geography',
 'die Kunst': 'art',
 'die Musik': 'music',
 'die Natur': 'nature',
 'die Sonne': 'sun',
 'der Mond': 'moon',
 'der Stern': 'star',
 'der Himmel': 'sky',
 'die Wolke': 'cloud',
 'der Schnee': 'snow',
 'der Wind': 'wind',
 'der Sturm': 'storm',
 'der Nebel': 'fog',
 'die Temperatur': 'temperature',
 'der Grad': 'degree',
 'warm': 'warm',
 'heiß': 'hot',
 'kalt': 'cold',
 'kühl': 'cool',
 'sonnig': 'sunny',
 'bewölkt': 'cloudy',
 'regnerisch': 'rainy',
 'windig': 'windy',
 'neblig': 'foggy',
 'trocken': 'dry',
 'nass': 'wet',
 'feucht': 'humid',
 'der Berg': 'mountain',
 'das Tal': 'valley',
 'der Wald': 'forest',
 'der Baum': 'tree',
 'die Blume': 'flower',
 'das Gras': 'grass',
 'der See': 'lake',
 'das Meer': 'sea',
 'der Strand': 'beach',
 'die Insel': 'island',
 'die Küste': 'coast',
 'der Stein': 'stone',
 'die Erde': 'earth, soil',
 'die Welt': 'world',
 'die Luft': 'air',
 'das Feuer': 'fire',
 'der Klimawandel': 'climate change',
 'die Energie': 'energy',
 'das Tier': 'animal',
 'das Haustier': 'pet',
 'der Hund': 'dog',
 'die Katze': 'cat',
 'das Pferd': 'horse',
 'die Kuh': 'cow',
 'das Schaf': 'sheep',
 'die Ziege': 'goat',
 'das Schwein': 'pig',
 'das Huhn': 'hen, chicken',
 'der Hahn': 'rooster',
 'die Ente': 'duck',
 'der Vogel': 'bird',
 'die Maus': 'mouse',
 'das Kaninchen': 'rabbit',
 'der Bär': 'bear',
 'der Löwe': 'lion',
 'der Elefant': 'elephant',
 'die Schlange': 'snake',
 'die Biene': 'bee',
 'die Fliege': 'fly',
 'das Insekt': 'insect',
 'der Schwanz': 'tail',
 'der Flügel': 'wing',
 'das Fell': 'fur',
 'bellen': 'to bark',
 'fressen': 'to eat (animals)',
 'füttern': 'to feed',
 'wild': 'wild',
 'der Computer': 'computer',
 'der Laptop': 'laptop',
 'das Handy': 'mobile phone',
 'das Smartphone': 'smartphone',
 'das Telefon': 'telephone',
 'der Bildschirm': 'screen',
 'die Tastatur': 'keyboard',
 'die Datei': 'file',
 'das Programm': 'program',
 'die Software': 'software',
 'die App': 'app',
 'das Internet': 'internet',
 'die Webseite': 'website',
 'die E-Mail': 'email',
 'die Nachricht': 'message, news',
 'das Passwort': 'password',
 'der Benutzer': 'user',
 'die Daten': 'data',
 'der Speicher': 'memory, storage',
 'das WLAN': 'Wi-Fi',
 'der Anschluss': 'connection, line',
 'der Akku': 'battery',
 'das Ladegerät': 'charger',
 'der Anruf': 'phone call',
 'telefonieren': 'to talk on the phone',
 'schicken': 'to send',
 'senden': 'to send',
 'herunterladen': 'to download',
 'hochladen': 'to upload',
 'speichern': 'to save',
 'löschen': 'to delete',
 'klicken': 'to click',
 'suchen': 'to search, to look for',
 'finden': 'to find',
 'installieren': 'to install',
 'ausschalten': 'to switch off',
 'einschalten': 'to switch on',
 'der Fernseher': 'television',
 'das Foto': 'photo',
 'das Video': 'video',
 'die Technik': 'technology',
 'Deutschland': 'Germany',
 'die Türkei': 'Turkey',
 'Österreich': 'Austria',
 'die Schweiz': 'Switzerland',
 'Frankreich': 'France',
 'Russland': 'Russia',
 'Europa': 'Europe',
 'Deutsch': 'German',
 'Türkisch': 'Turkish',
 'Englisch': 'English',
 'die Muttersprache': 'mother tongue',
 'der Ausländer': 'foreigner',
 'die Nationalität': 'nationality',
 'die Staatsangehörigkeit': 'citizenship',
 'die Kultur': 'culture',
 'die Tradition': 'tradition',
 'die Religion': 'religion',
 'die Regierung': 'government',
 'der Staat': 'state',
 'die Politik': 'politics',
 'das Gesetz': 'law',
 'das Recht': 'right, law',
 'die Freiheit': 'freedom',
 'die Zeitung': 'newspaper',
 'die Nachrichten': 'news',
 'der Sport': 'sport',
 'das Spiel': 'game, match',
 'der Fußball': 'football',
 'das Schwimmen': 'swimming',
 'das Laufen': 'running',
 'das Fitness': 'fitness',
 'das Training': 'training',
 'die Mannschaft': 'team',
 'der Spieler': 'player',
 'der Trainer': 'coach',
 'das Tor': 'goal, gate',
 'der Sieg': 'victory',
 'der Ball': 'ball',
 'die Freizeit': 'free time',
 'das Hobby': 'hobby',
 'das Lied': 'song',
 'der Film': 'film, movie',
 'die Serie': 'series',
 'das Konzert': 'concert',
 'die Party': 'party',
 'das Fest': 'festival, celebration',
 'das Geschenk': 'present, gift',
 'die Feier': 'celebration',
 'das Lesen': 'reading',
 'das Kochen': 'cooking',
 'der Spaziergang': 'walk',
 'trainieren': 'to train',
 'sich entspannen': 'to relax',
 'feiern': 'to celebrate',
 'tanzen': 'to dance',
 'singen': 'to sing',
 'das Amt': 'public office, authority',
 'das Bürgeramt': "citizens' office",
 'die Ausländerbehörde': 'immigration office',
 'das Finanzamt': 'tax office',
 'das Jobcenter': 'job centre',
 'die Agentur für Arbeit': 'Federal Employment Agency',
 'die Abmeldung': 'deregistration',
 'die Bescheinigung': 'certificate',
 'das Formular': 'form',
 'der Bescheid': 'official notice, decision',
 'die Unterschrift': 'signature',
 'der Stempel': 'stamp',
 'die Kopie': 'copy',
 'das Original': 'original',
 'die Frist': 'deadline',
 'der Nachweis': 'proof',
 'die Meldebescheinigung': 'registration certificate',
 'die Aufenthaltserlaubnis': 'residence permit',
 'die Arbeitserlaubnis': 'work permit',
 'die Steuer-ID': 'tax ID',
 'die Sozialversicherung': 'social security',
 'die Rentenversicherung': 'pension insurance',
 'die Haftpflichtversicherung': 'liability insurance',
 'der Rundfunkbeitrag': 'broadcasting fee (TV licence)',
 'der Sachbearbeiter': 'case worker',
 'der Schalter': 'counter',
 'die Wartenummer': 'queue number',
 'die Öffnungszeiten': 'opening hours',
 'beantragen': 'to apply for',
 'einreichen': 'to submit',
 'verlängern': 'to extend',
 'abholen': 'to pick up, to collect',
 'anmelden': 'to register',
 'erlaubt': 'allowed',
 'verboten': 'forbidden',
 'nötig': 'necessary',
 'gültig': 'valid',
 'werden': 'to become; will',
 'können': 'can, to be able to',
 'müssen': 'must, to have to',
 'wollen': 'to want',
 'sollen': 'should, to be supposed to',
 'dürfen': 'may, to be allowed to',
 'mögen': 'to like',
 'tun': 'to do',
 'sagen': 'to say',
 'reden': 'to talk, to chat',
 'fragen': 'to ask',
 'antworten': 'to answer',
 'sehen': 'to see',
 'schauen': 'to look',
 'hören': 'to hear, to listen',
 'zuhören': 'to listen',
 'kennen': 'to know (a person)',
 'glauben': 'to believe',
 'meinen': 'to mean, to think',
 'hoffen': 'to hope',
 'wünschen': 'to wish',
 'geben': 'to give',
 'bringen': 'to bring',
 'holen': 'to fetch',
 'halten': 'to hold',
 'legen': 'to lay, to put (flat)',
 'stellen': 'to put (upright)',
 'setzen': 'to set, to put',
 'sitzen': 'to sit',
 'liegen': 'to lie, to be located',
 'aufwachen': 'to wake up',
 'einschlafen': 'to fall asleep',
 'gehören': 'to belong',
 'beginnen': 'to begin',
 'enden': 'to end',
 'beenden': 'to finish',
 'weitermachen': 'to carry on',
 'schaffen': 'to manage, to create',
 'gelingen': 'to succeed',
 'scheitern': 'to fail',
 'danken': 'to thank',
 'bitten': 'to ask (for), to request',
 'erlauben': 'to allow',
 'verbieten': 'to forbid',
 'wählen': 'to choose, to vote',
 'planen': 'to plan',
 'ändern': 'to change',
 'wachsen': 'to grow',
 'passieren': 'to happen',
 'geschehen': 'to happen, to occur',
 'stattfinden': 'to take place',
 'dauern': 'to last',
 'besuchen': 'to visit',
 'einladen': 'to invite',
 'mitkommen': 'to come along',
 'begleiten': 'to accompany',
 'verlassen': 'to leave',
 'verabschieden': 'to say goodbye',
 'erkennen': 'to recognise',
 'merken': 'to notice, to remember',
 'erinnern': 'to remember, to remind',
 'berichten': 'to report',
 'zeigen': 'to show',
 'bedeuten': 'to mean',
 'übersetzen': 'to translate',
 'aussprechen': 'to pronounce',
 'öffnen': 'to open',
 'schließen': 'to close',
 'zumachen': 'to close, to shut',
 'aufmachen': 'to open',
 'drücken': 'to press, to push',
 'ziehen': 'to pull',
 'werfen': 'to throw',
 'fangen': 'to catch',
 'fallen': 'to fall',
 'heben': 'to lift',
 'bauen': 'to build',
 'reparieren': 'to repair',
 'kaputt machen': 'to break (something)',
 'benutzen': 'to use',
 'verwenden': 'to use',
 'sammeln': 'to collect',
 'teilen': 'to share, to divide',
 'verteilen': 'to distribute',
 'wechseln': 'to change, to exchange',
 'tauschen': 'to swap',
 'leihen': 'to lend, to borrow',
 'besitzen': 'to own',
 'entdecken': 'to discover',
 'mitteilen': 'to inform',
 'streiten': 'to argue, to fight',
 'diskutieren': 'to discuss',
 'versprechen': 'to promise',
 'lügen': 'to lie (tell lies)',
 'stören': 'to disturb',
 'beeilen': 'to hurry',
 'beobachten': 'to observe',
 'aufpassen': 'to pay attention, to look after',
 'kümmern': 'to take care of',
 'sorgen': 'to worry, to provide for',
 'schützen': 'to protect',
 'retten': 'to save, to rescue',
 'kämpfen': 'to fight, to struggle',
 'bemerken': 'to notice',
 'interessieren': 'to interest',
 'gefallen': 'to please (be liked)',
 'lieben': 'to love',
 'hassen': 'to hate',
 'lachen': 'to laugh',
 'weinen': 'to cry',
 'lächeln': 'to smile',
 'küssen': 'to kiss',
 'rufen': 'to call, to shout',
 'schreien': 'to scream',
 'riechen': 'to smell',
 'schmecken': 'to taste',
 'fühlen': 'to feel',
 'berühren': 'to touch',
 'wiegen': 'to weigh',
 'messen': 'to measure',
 'zählen': 'to count',
 'vermieten': 'to rent out',
 'liefern': 'to deliver',
 'führen': 'to lead, to guide',
 'folgen': 'to follow',
 'vorschlagen': 'to suggest',
 'anbieten': 'to offer',
 'annehmen': 'to accept, to assume',
 'akzeptieren': 'to accept',
 'rennen': 'to run',
 'träumen': 'to dream',
 'schlecht': 'bad',
 'lang': 'long',
 'kurz': 'short',
 'hoch': 'high',
 'niedrig': 'low',
 'breit': 'wide',
 'schmal': 'narrow',
 'dick': 'thick, fat',
 'dünn': 'thin',
 'schwer': 'heavy, difficult',
 'leicht': 'light, easy',
 'neu': 'new',
 'alt': 'old',
 'jung': 'young',
 'modern': 'modern',
 'langsam': 'slow',
 'laut': 'loud',
 'leise': 'quiet',
 'voll': 'full',
 'leer': 'empty',
 'offen': 'open',
 'geschlossen': 'closed',
 'richtig': 'right, correct',
 'falsch': 'wrong',
 'wahr': 'true',
 'möglich': 'possible',
 'unmöglich': 'impossible',
 'einfach': 'simple, easy',
 'schwierig': 'difficult',
 'kompliziert': 'complicated',
 'interessant': 'interesting',
 'langweilig': 'boring',
 'schön': 'beautiful',
 'nett': 'nice',
 'freundlich': 'friendly',
 'höflich': 'polite',
 'ruhig': 'calm',
 'nervös': 'nervous',
 'fleißig': 'hard-working',
 'faul': 'lazy, rotten',
 'klug': 'clever',
 'dumm': 'stupid',
 'gefährlich': 'dangerous',
 'sicher': 'safe, sure',
 'frei': 'free, vacant',
 'besetzt': 'occupied, taken',
 'beschäftigt': 'busy',
 'bereit': 'ready',
 'fertig': 'finished, ready',
 'nützlich': 'useful',
 'beliebt': 'popular',
 'bekannt': 'well-known',
 'fremd': 'foreign, strange',
 'ähnlich': 'similar',
 'verschieden': 'different',
 'besonders': 'special, especially',
 'normal': 'normal',
 'echt': 'real, genuine',
 'privat': 'private',
 'öffentlich': 'public',
 'arm': 'poor',
 'reich': 'rich',
 'glücklich': 'happy',
 'traurig': 'sad',
 'lustig': 'funny',
 'ernst': 'serious',
 'stolz': 'proud',
 'mutig': 'brave',
 'geduldig': 'patient',
 'zuverlässig': 'reliable',
 'erfolgreich': 'successful',
 'hilfsbereit': 'helpful',
 'kreativ': 'creative',
 'praktisch': 'practical',
 'perfekt': 'perfect',
 'wunderbar': 'wonderful',
 'toll': 'great',
 'die Freude': 'joy',
 'das Glück': 'happiness, luck',
 'die Trauer': 'grief',
 'die Angst': 'fear',
 'die Sorge': 'worry',
 'der Stress': 'stress',
 'die Wut': 'rage',
 'der Ärger': 'anger, trouble',
 'die Überraschung': 'surprise',
 'die Hoffnung': 'hope',
 'der Wunsch': 'wish',
 'das Vertrauen': 'trust',
 'der Mut': 'courage',
 'die Geduld': 'patience',
 'die Ruhe': 'calm, quiet',
 'die Langeweile': 'boredom',
 'die Einsamkeit': 'loneliness',
 'der Charakter': 'character',
 'die Laune': 'mood',
 'die Stimmung': 'mood, atmosphere',
 'das Lachen': 'laughter',
 'die Träne': 'tear',
 'sich ärgern': 'to get angry',
 'sich schämen': 'to be ashamed',
 'sich langweilen': 'to be bored',
 'sich verlieben': 'to fall in love',
 'sich wundern': 'to be surprised',
 'sich beruhigen': 'to calm down',
 'aufgeregt': 'excited',
 'enttäuscht': 'disappointed',
 'überrascht': 'surprised',
 'verliebt': 'in love',
 'wütend': 'furious',
 'eifersüchtig': 'jealous',
 'schüchtern': 'shy',
 'gespannt': 'eager, in suspense',
 'erschöpft': 'exhausted',
 'sehr': 'very',
 'ganz': 'quite, completely',
 'fast': 'almost',
 'nur': 'only',
 'auch': 'also, too',
 'noch': 'still, yet',
 'schon': 'already',
 'erst': 'only (not until), first',
 'wieder': 'again',
 'nochmal': 'once more',
 'vor allem': 'above all',
 'zum Beispiel': 'for example',
 'übrigens': 'by the way',
 'wirklich': 'really',
 'bestimmt': 'certainly',
 'wahrscheinlich': 'probably',
 'hoffentlich': 'hopefully',
 'zum Glück': 'luckily',
 'plötzlich': 'suddenly',
 'endlich': 'finally, at last',
 'zuerst': 'first',
 'dann': 'then',
 'danach': 'afterwards',
 'zuletzt': 'last',
 'schließlich': 'finally, eventually',
 'zusammen': 'together',
 'allein': 'alone',
 'gemeinsam': 'jointly',
 'überall': 'everywhere',
 'dort': 'there',
 'hier': 'here',
 'da': 'there',
 'draußen': 'outside',
 'drinnen': 'inside',
 'weg': 'away, gone',
 'zurück': 'back',
 'weiter': 'further',
 'sonst': 'otherwise, else',
 'kaum': 'hardly',
 'nicht': 'not',
 'doch': 'but, yet',
 'gern': 'gladly',
 'lieber': 'rather, preferably',
 'am liebsten': 'most of all',
 'mindestens': 'at least',
 'höchstens': 'at most',
 'ungefähr': 'approximately',
 'etwa': 'about, roughly',
 'normalerweise': 'normally',
 'insgesamt': 'in total',
 'außerdem': 'besides, moreover',
 'jedoch': 'however',
 'sogar': 'even',
 'bereits': 'already',
 'damals': 'back then',
 'leben': 'to live',
 'reisen': 'to travel',
 'funktionieren': 'to work, to function',
 'existieren': 'to exist',
 'genießen': 'to enjoy',
 'fürchten': 'to fear',
 'vertrauen': 'to trust',
 'riskieren': 'to risk',
 'fehlen': 'to be missing',
 'ärgern': 'to annoy',
 'beruhigen': 'to calm (sb) down',
 'überraschen': 'to surprise',
 'entschuldigen': 'to excuse',
 'duschen': 'to shower',
 'baden': 'to bathe',
 'kämmen': 'to comb',
 'rasieren': 'to shave',
 'notieren': 'to note down',
 'organisieren': 'to organise',
 'malen': 'to paint',
 'zeichnen': 'to draw',
 'basteln': 'to do crafts, to tinker',
 'erwarten': 'to expect',
 'schwimmen': 'to swim',
 'springen': 'to jump',
 'klettern': 'to climb',
 'rauchen': 'to smoke',
 'surfen': 'to surf',
 'chatten': 'to chat',
 'posten': 'to post',
 'liken': 'to like (a post)',
 'kommentieren': 'to comment',
 'drucken': 'to print',
 'scannen': 'to scan',
 'zahlen': 'to pay',
 'grillen': 'to grill, to barbecue',
 'spülen': 'to wash up, to rinse',
 'bügeln': 'to iron',
 'nähen': 'to sew',
 'kleben': 'to glue, to stick',
 'auflegen': 'to hang up',
 'ausladen': 'to unload; to uninvite',
 'parken': 'to park',
 'tanken': 'to refuel',
 'sortieren': 'to sort',
 'betrachten': 'to look at, to regard',
 'prüfen': 'to check, to test',
 'eintragen': 'to enter, to register',
 'anwenden': 'to apply, to use',
 'raten': 'to advise; to guess',
 'warnen': 'to warn',
 'drohen': 'to threaten',
 'zurückkehren': 'to return',
 'verschwinden': 'to disappear',
 'erscheinen': 'to appear',
 'entstehen': 'to arise, to emerge',
 'sich entwickeln': 'to develop',
 'sich verändern': 'to change',
 'verschlimmern': 'to make worse',
 'sichern': 'to secure; to back up',
 'halbieren': 'to halve',
 'verdoppeln': 'to double',
 'multiplizieren': 'to multiply',
 'addieren': 'to add',
 'subtrahieren': 'to subtract',
 'dividieren': 'to divide',
 'unterscheiden': 'to distinguish',
 'ordnen': 'to arrange, to put in order',
 'lösen': 'to solve',
 'befestigen': 'to fasten, to fix',
 'befehlen': 'to order, to command',
 'gehorchen': 'to obey',
 'schenken': 'to give (as a present)',
 'ausleihen': 'to borrow',
 'investieren': 'to invest',
 'zurückkommen': 'to come back',
 'zurückgehen': 'to go back',
 'losfahren': 'to set off',
 'abreisen': 'to depart, to leave',
 'mitnehmen': 'to take along',
 'wegwerfen': 'to throw away',
 'auspacken': 'to unpack',
 'markieren': 'to mark',
 'kopieren': 'to copy',
 'übertragen': 'to transfer; to broadcast',
 'verbinden': 'to connect',
 'trennen': 'to separate',
 'begegnen': 'to come across, to meet',
 'empfangen': 'to receive, to welcome',
 'bewundern': 'to admire',
 'ergänzen': 'to complete, to add',
 'informieren': 'to inform',
 'beweisen': 'to prove',
 'verschlechtern': 'to worsen',
 'verändern': 'to change, to alter',
 'erweitern': 'to expand',
 'reduzieren': 'to reduce',
 'erhöhen': 'to raise, to increase',
 'nutzen': 'to use, to make use of',
 'experimentieren': 'to experiment',
 'starten': 'to start, to launch',
 'stoppen': 'to stop',
 'pausieren': 'to pause',
 'fortsetzen': 'to continue',
 'unterbrechen': 'to interrupt',
 'vorbeikommen': 'to drop by',
 'vorbeifahren': 'to drive past',
 'umdrehen': 'to turn round',
 'zurückbleiben': 'to stay behind',
 'behandeln': 'to treat',
 'bedauern': 'to regret',
 'beklagen': 'to lament',
 'beweinen': 'to mourn',
 'vermissen': 'to miss (sb)',
 'schätzen': 'to value; to estimate',
 'respektieren': 'to respect',
 'tolerieren': 'to tolerate',
 'ignorieren': 'to ignore',
 'analysieren': 'to analyse',
 'recherchieren': 'to research',
 'erläutern': 'to explain in detail',
 'bewerten': 'to evaluate, to rate',
 'definieren': 'to define',
 'entwickeln': 'to develop',
 'konstruieren': 'to construct',
 'produzieren': 'to produce',
 'konsumieren': 'to consume',
 'exportieren': 'to export',
 'importieren': 'to import',
 'verschwenden': 'to waste',
 'erhalten': 'to receive; to preserve',
 'testen': 'to test',
 'versagen': 'to fail',
 'misslingen': 'to go wrong, to fail',
 'vorhersehen': 'to foresee',
 'gedeihen': 'to thrive',
 'vergehen': 'to pass (time)',
 'melden': 'to report, to notify',
 'empfinden': 'to feel, to perceive',
 'festlegen': 'to determine, to fix',
 'vorstellen': 'to introduce',
 'sich vorbereiten': 'to prepare oneself',
 'sich treffen': 'to meet (up)',
 'sich setzen': 'to sit down',
 'sich waschen': 'to wash (oneself)',
 'sich anziehen': 'to get dressed',
 'sich ausziehen': 'to get undressed',
 'sich verlieben in': 'to fall in love with',
 'sich bedanken': 'to say thank you',
 'sich verabschieden': 'to say goodbye',
 'sich entscheiden': 'to decide',
 'sich konzentrieren': 'to concentrate',
 'sich wünschen': 'to wish for',
 'sich lohnen': 'to be worth it',
 'sich auszahlen': 'to pay off',
 'sich überlegen': 'to think over',
 'sich irren': 'to be wrong',
 'sich ändern': 'to change',
 'sich verbessern': 'to improve',
 'sich informieren': 'to inform oneself',
 'sich beklagen': 'to complain',
 'sich unterhalten': 'to talk, to chat',
 'sich verlaufen': 'to get lost',
 'sich anstrengen': 'to make an effort',
 'sich auskennen': "to know one's way around",
 'sich trauen': 'to dare',
 'sich verschlechtern': 'to get worse',
 'sich sorgen': 'to worry',
 'sich freuen auf': 'to look forward to',
 'sich umsehen': 'to look around',
 'sich verstehen': 'to get on (well)',
 'sich streiten': 'to argue, to quarrel',
 'sich vertragen': 'to get along',
 'sich anpassen': 'to adapt',
 'die Anforderung': 'requirement',
 'der Bedarf': 'need, demand',
 'die Beschwerde': 'complaint',
 'die Erkenntnis': 'insight, finding',
 'das Ereignis': 'event',
 'die Fortbildung': 'further training',
 'die Gewohnheit': 'habit',
 'der Hinweis': 'hint, notice',
 'die Leistung': 'performance; service',
 'das Merkmal': 'feature, characteristic',
 'die Mehrheit': 'majority',
 'die Minderheit': 'minority',
 'der Standpunkt': 'standpoint',
 'die Überzeugung': 'conviction',
 'der Umstand': 'circumstance',
 'die Verpflichtung': 'obligation',
 'der Verlauf': 'course, progress',
 'die Wirkung': 'effect',
 'der Zweifel': 'doubt',
 'die Zusammenarbeit': 'cooperation',
 'der Zugang': 'access',
 'ausüben': 'to exercise, to practise',
 'beantworten': 'to answer (sth)',
 'bedenken': 'to bear in mind',
 'befürchten': 'to fear (that)',
 'begründen': 'to justify',
 'beurteilen': 'to judge, to assess',
 'durchführen': 'to carry out',
 'eingehen auf': 'to go into, to address',
 'einhalten': 'to comply with, to keep',
 'ermitteln': 'to determine; to investigate',
 'fördern': 'to promote, to support',
 'hinweisen auf': 'to point out',
 'nachdenken über': 'to think about',
 'überwiegen': 'to predominate',
 'verlangen': 'to demand',
 'voraussetzen': 'to presuppose',
 'zurückführen auf': 'to attribute to',
 'angemessen': 'appropriate',
 'bedeutend': 'significant',
 'eindeutig': 'clear, unambiguous',
 'gegenseitig': 'mutual',
 'grundsätzlich': 'basically, in principle',
 'jedenfalls': 'in any case',
 'überwiegend': 'predominantly',
 'vermutlich': 'presumably',
 'zumindest': 'at least',
 'zunehmend': 'increasingly',
 'die Absprache': 'arrangement',
 'der Ausgleich': 'balance, compensation',
 'die Auseinandersetzung': 'dispute, debate',
 'die Behauptung': 'claim, assertion',
 'der Bestandteil': 'component',
 'die Entlastung': 'relief',
 'der Ertrag': 'yield, return',
 'die Folgerung': 'conclusion',
 'der Konsens': 'consensus',
 'die Rahmenbedingung': 'framework condition',
 'die Rechtfertigung': 'justification',
 'die Tendenz': 'tendency',
 'der Überblick': 'overview',
 'die Überlegung': 'consideration',
 'das Verhältnis': 'ratio; relationship',
 'die Vorhersage': 'prediction',
 'der Zusammenhalt': 'cohesion',
 'anerkennen': 'to recognise, to acknowledge',
 'ansprechen': 'to address, to approach',
 'aufweisen': 'to show, to exhibit',
 'ausgleichen': 'to balance out',
 'aushandeln': 'to negotiate',
 'sich bemühen': 'to make an effort',
 'benachteiligen': 'to disadvantage',
 'bevorzugen': 'to prefer',
 'einbeziehen': 'to include, to involve',
 'einsetzen': 'to use, to deploy',
 'erfordern': 'to require',
 'gelten als': 'to be regarded as',
 'hinnehmen': 'to put up with',
 'sich auswirken auf': 'to have an effect on',
 'überschätzen': 'to overestimate',
 'unterschätzen': 'to underestimate',
 'vernachlässigen': 'to neglect',
 'vertreten': 'to represent; to advocate',
 'zusammenfassen': 'to summarise',
 'absehbar': 'foreseeable',
 'ausdrücklich': 'explicitly',
 'befristet': 'fixed-term',
 'folglich': 'consequently',
 'hinsichtlich': 'with regard to',
 'keineswegs': 'by no means',
 'mittlerweile': 'meanwhile, by now',
 'sachlich': 'objective, factual',
 'umstritten': 'controversial',
 'vielmehr': 'rather',
 'die Abwägung': 'weighing up',
 'der Anreiz': 'incentive',
 'die Ausprägung': 'manifestation, form',
 'die Bewältigung': 'coping, mastering',
 'die Darlegung': 'exposition',
 'der Eingriff': 'intervention',
 'die Errungenschaft': 'achievement',
 'das Gefälle': 'gap, disparity',
 'der Grundsatz': 'principle',
 'die Instanz': 'authority, instance',
 'die Rechenschaft': 'accountability',
 'die Teilhabe': 'participation',
 'der Vorbehalt': 'reservation',
 'die Zumutung': 'imposition',
 'der Zwiespalt': 'conflict, dilemma',
 'abgrenzen': 'to delimit',
 'anfechten': 'to contest',
 'anregen': 'to stimulate, to suggest',
 'ausschöpfen': 'to exhaust (options)',
 'bekräftigen': 'to reaffirm',
 'beleuchten': 'to shed light on',
 'einleiten': 'to initiate',
 'entkräften': 'to refute',
 'erschließen': 'to open up',
 'gewähren': 'to grant',
 'herleiten': 'to derive',
 'relativieren': 'to put into perspective',
 'sich niederschlagen in': 'to be reflected in',
 'veranschaulichen': 'to illustrate',
 'verdeutlichen': 'to clarify',
 'wahrnehmen': 'to perceive; to exercise',
 'abwegig': 'far-fetched',
 'angesichts': 'in view of',
 'beträchtlich': 'considerable',
 'eingehend': 'thorough(ly)',
 'gleichwohl': 'nonetheless',
 'hinfällig': 'invalid, void',
 'infolgedessen': 'as a result',
 'mithin': 'consequently',
 'nachweislich': 'demonstrably',
 'schlüssig': 'conclusive, coherent',
 'unabdingbar': 'indispensable',
 'zwecks': 'for the purpose of',
 'die Abhilfe': 'remedy',
 'der Anlass': 'occasion, cause',
 'die Befürchtung': 'fear, apprehension',
 'die Einbuße': 'loss',
 'das Gutachten': 'expert report',
 'der Handlungsbedarf': 'need for action',
 'die Kehrseite': 'downside',
 'das Missverhältnis': 'imbalance',
 'die Nachsicht': 'leniency',
 'das Versäumnis': 'omission, failure',
 'die Weichenstellung': 'setting the course',
 'die Zurückhaltung': 'restraint',
 'anknüpfen an': 'to build on',
 'beanstanden': 'to object to',
 'beherzigen': 'to heed',
 'bekunden': 'to express, to declare',
 'dulden': 'to tolerate',
 'einbüßen': 'to lose, to forfeit',
 'entgegenkommen': 'to accommodate',
 'erachten': 'to consider, to deem',
 'ergründen': 'to fathom',
 'sich erübrigen': 'to become unnecessary',
 'gutheißen': 'to approve of',
 'hervorrufen': 'to cause, to evoke',
 'sich vergewissern': 'to make sure',
 'verankern': 'to anchor, to enshrine',
 'vorenthalten': 'to withhold',
 'sich zuspitzen': 'to come to a head',
 'bisweilen': 'at times',
 'dergestalt': 'in such a way',
 'eigens': 'specially',
 'fortan': 'henceforth',
 'geflissentlich': 'deliberately',
 'nichtsdestotrotz': 'nevertheless',
 'sinngemäß': 'in essence',
 'tendenziell': 'tendentially',
 'unstrittig': 'undisputed',
 'vorrangig': 'primarily',
 'zuweilen': 'occasionally',
 'die Ambivalenz': 'ambivalence',
 'der Anachronismus': 'anachronism',
 'die Arglist': 'malice, deceit',
 'die Besonnenheit': 'level-headedness',
 'der Einschnitt': 'turning point, cut',
 'die Geringschätzung': 'disdain',
 'das Hirngespinst': 'fantasy, pipe dream',
 'die Kurzsichtigkeit': 'short-sightedness',
 'die Nachlässigkeit': 'carelessness',
 'die Redlichkeit': 'integrity',
 'der Rückschluss': 'inference',
 'die Selbstgefälligkeit': 'complacency',
 'die Spitzfindigkeit': 'hair-splitting',
 'der Trugschluss': 'fallacy',
 'die Verklärung': 'glorification',
 'abwiegeln': 'to play down',
 'anzweifeln': 'to question, to doubt',
 'aufoktroyieren': 'to impose',
 'ausufern': 'to get out of hand',
 'beschwichtigen': 'to appease',
 'brandmarken': 'to brand, to stigmatise',
 'sich entziehen': 'to evade',
 'erodieren': 'to erode',
 'frönen': 'to indulge in',
 'hadern mit': 'to be at odds with',
 'kaschieren': 'to conceal',
 'monieren': 'to criticise',
 'unterminieren': 'to undermine',
 'vereinnahmen': 'to co-opt',
 'zermürben': 'to wear down',
 'akribisch': 'meticulous',
 'beiläufig': 'casually',
 'dezidiert': 'decided, firm',
 'fadenscheinig': 'flimsy',
 'hanebüchen': 'outrageous',
 'inhärent': 'inherent',
 'latent': 'latent',
 'perfide': 'perfidious',
 'subtil': 'subtle',
 'unumstößlich': 'irrefutable',
 'verbrämt': 'veiled',
 'zögerlich': 'hesitant',
 'der Augenschein': 'appearance',
 'die Binsenweisheit': 'truism',
 'der Etikettenschwindel': 'false labelling',
 'das Gebaren': 'conduct',
 'der Hemmschuh': 'obstacle, drag',
 'die Kehrtwende': 'U-turn',
 'der Lackmustest': 'litmus test',
 'die Lappalie': 'trifle',
 'das Sammelsurium': 'hotchpotch',
 'der Seitenhieb': 'dig, jibe',
 'die Schadenfreude': 'schadenfreude',
 'der Vorwand': 'pretext',
 'aus dem Ruder laufen': 'to get out of hand',
 'das Handtuch werfen': 'to throw in the towel',
 'die Katze im Sack kaufen': 'to buy a pig in a poke',
 'einen Bärendienst erweisen': 'to do sb a disservice',
 'etwas auf die lange Bank schieben': 'to put sth on the back burner',
 'jemandem reinen Wein einschenken': 'to tell sb the plain truth',
 'kein Blatt vor den Mund nehmen': "not to mince one's words",
 'mit offenen Karten spielen': "to put one's cards on the table",
 'sich aus der Affäre ziehen': 'to wriggle out of it',
 'Tacheles reden': 'to talk straight',
 'über den Tellerrand schauen': 'to think outside the box',
 'zwischen den Zeilen lesen': 'to read between the lines',
 'den Teufel an die Wand malen': 'to tempt fate, to fear the worst',
 'Öl ins Feuer gießen': 'to add fuel to the fire',
 'blasiert': 'blasé, arrogant',
 'dubios': 'dubious',
 'ephemer': 'ephemeral',
 'lakonisch': 'laconic',
 'obskur': 'obscure',
 'prätentiös': 'pretentious',
 'salopp': 'casual, sloppy',
 'verschroben': 'odd, eccentric',
 'aufgeben, verlassen': 'abandon',
 'vollbringen, erreichen': 'accomplish',
 'ansammeln, anhäufen': 'accumulate',
 'angehen, ansprechen': 'address',
 'zugeben, eingestehen': 'admit',
 'befürworten, sich einsetzen für': 'advocate',
 'sich leisten können': 'afford',
 'lindern': 'alleviate',
 'zuweisen, bereitstellen': 'allocate',
 'genehmigen, billigen': 'approve',
 'argumentieren, streiten': 'argue',
 'versichern, zusichern': 'assure',
 'zuschreiben': 'attribute',
 'unterstützen; sichern': 'back up',
 'beschuldigen, die Schuld geben': 'blame',
 'steigern, ankurbeln': 'boost',
 'herausfordern, infrage stellen': 'challenge',
 'klären, verdeutlichen': 'clarify',
 'zusammenarbeiten': 'collaborate',
 'sich verpflichten; begehen': 'commit',
 'zwingen': 'compel',
 'zusammenstellen': 'compile',
 'umfassen, bestehen aus': 'comprise',
 'verbergen': 'conceal',
 'bestätigen': 'confirm',
 'konfrontieren, sich stellen': 'confront',
 'bestehen aus': 'consist',
 'konsultieren, sich beraten': 'consult',
 'vermitteln, übermitteln': 'convey',
 'entsprechen; korrespondieren': 'correspond',
 'kritisieren': 'criticise',
 'pflegen, kultivieren': 'cultivate',
 'eindämmen, zügeln': 'curb',
 'sich befassen mit, erledigen': 'deal with',
 'widmen': 'dedicate',
 'aufschieben': 'defer',
 'delegieren': 'delegate',
 'bezeichnen, bedeuten': 'denote',
 'leugnen, verweigern': 'deny',
 'ableiten, gewinnen': 'derive',
 'bestimmen, festlegen': 'determine',
 'abschrecken': 'deter',
 'ersinnen, entwerfen': 'devise',
 'verringern, abnehmen': 'diminish',
 'offenlegen': 'disclose',
 'entmutigen, abraten': 'discourage',
 'entlassen; abtun': 'dismiss',
 'verdrängen, vertreiben': 'displace',
 'entsorgen': 'dispose',
 'auseinandergehen, abweichen': 'diverge',
 'näher ausführen': 'elaborate',
 'beseitigen': 'eliminate',
 'betonen': 'emphasise',
 'ertragen, aushalten': 'endure',
 'beschäftigen; sich beteiligen': 'engage',
 'sicherstellen, gewährleisten': 'ensure',
 'mit sich bringen': 'entail',
 'gründen, festlegen': 'establish',
 'übertreiben': 'exaggerate',
 'überschreiten': 'exceed',
 'ausschließen': 'exclude',
 'ausbeuten, ausnutzen': 'exploit',
 'aussetzen; aufdecken': 'expose',
 'erleichtern': 'facilitate',
 'herausfinden, verstehen': 'figure out',
 'erfüllen': 'fulfil',
 'erzeugen': 'generate',
 'regieren, bestimmen': 'govern',
 'zögern': 'hesitate',
 'behindern': 'hinder',
 'identifizieren, erkennen': 'identify',
 'andeuten, implizieren': 'imply',
 'auferlegen, aufzwingen': 'impose',
 'neigen zu': 'incline',
 'steigen, erhöhen': 'increase',
 'herbeiführen, auslösen': 'induce',
 'hemmen': 'inhibit',
 'bestehen auf': 'insist',
 'inspirieren': 'inspire',
 'integrieren': 'integrate',
 'sich einmischen, stören': 'interfere',
 'interpretieren, deuten': 'interpret',
 'eingreifen': 'intervene',
 'beinhalten, einbeziehen': 'involve',
 'rechtfertigen': 'justify',
 'aufrechterhalten; behaupten': 'maintain',
 'manipulieren': 'manipulate',
 'mildern, abschwächen': 'mitigate',
 'modifizieren, ändern': 'modify',
 'überwachen': 'monitor',
 'verhandeln': 'negotiate',
 'skizzieren, umreißen': 'outline',
 'überwinden': 'overcome',
 'beaufsichtigen': 'oversee',
 'übersehen': 'overlook',
 'fortbestehen, beharren': 'persist',
 'überreden': 'persuade',
 'genau bestimmen': 'pinpoint',
 'bewahren, erhalten': 'preserve',
 'verhindern': 'prevent',
 'priorisieren': 'prioritise',
 'fortfahren': 'proceed',
 'verfolgen': 'pursue',
 'sich qualifizieren; einschränken': 'qualify',
 'quantifizieren': 'quantify',
 'anwerben, einstellen': 'recruit',
 'verfeinern': 'refine',
 'widerspiegeln; nachdenken': 'reflect',
 'unterlassen, sich enthalten': 'refrain',
 'betrachten als': 'regard',
 'verstärken': 'reinforce',
 'entlasten, lindern': 'relieve',
 'sich verlassen auf': 'rely',
 'machen zu; erbringen': 'render',
 'ähneln': 'resemble',
 'wiederherstellen': 'restore',
 'beschränken': 'restrict',
 'behalten, bewahren': 'retain',
 'abrufen, zurückholen': 'retrieve',
 'enthüllen, offenbaren': 'reveal',
 'umkehren': 'reverse',
 'überarbeiten': 'revise',
 'sich niederlassen; beilegen': 'settle',
 'vereinfachen': 'simplify',
 'herrühren von': 'stem from',
 'stärken': 'strengthen',
 'streben': 'strive',
 'ersetzen': 'substitute',
 'leiden': 'suffer',
 'unterdrücken': 'suppress',
 'maßschneidern, anpassen': 'tailor',
 'neigen, tendieren': 'tend',
 'verwandeln': 'transform',
 'durchlaufen, sich unterziehen': 'undergo',
 'untergraben': 'undermine',
 'eindringlich auffordern': 'urge',
 'validieren, bestätigen': 'validate',
 'variieren': 'vary',
 'überprüfen': 'verify',
 'schwächen': 'weaken',
 'zurückziehen, abheben': 'withdraw',
 'standhalten': 'withstand',
 'bezeugen, miterleben': 'witness',
 'ergeben, liefern; nachgeben': 'yield',
 'die Rechenschaftspflicht': 'accountability',
 'die Genauigkeit': 'accuracy',
 'die Widrigkeit': 'adversity',
 'die Nachwirkungen (Pl.)': 'aftermath',
 'die Mehrdeutigkeit': 'ambiguity',
 'der Reiz; der Einspruch': 'appeal',
 'der Aspekt': 'aspect',
 'das Bewusstsein': 'awareness',
 'die Gegenreaktion': 'backlash',
 'die Barriere, das Hindernis': 'barrier',
 'der Maßstab, der Richtwert': 'benchmark',
 'die Voreingenommenheit': 'bias',
 'der Durchbruch': 'breakthrough',
 'die Last, die Belastung': 'burden',
 'die Kapazität': 'capacity',
 'das Engagement, die Verpflichtung': 'commitment',
 'der Widerspruch': 'contradiction',
 'die Kontroverse': 'controversy',
 'die Glaubwürdigkeit': 'credibility',
 'das Kriterium': 'criterion',
 'das Dilemma': 'dilemma',
 'die Diskrepanz': 'discrepancy',
 'die Ungleichheit': 'disparity',
 'die Störung, der Umbruch': 'disruption',
 'die Effizienz': 'efficiency',
 'die Betonung': 'emphasis',
 'das Bestreben': 'endeavour',
 'das Fachwissen, die Expertise': 'expertise',
 'die Exposition, die Sichtbarkeit': 'exposure',
 'die Machbarkeit': 'feasibility',
 'der Rahmen': 'framework',
 'das Hindernis': 'hindrance',
 'die Implikation, die Folge': 'implication',
 'die Inkonsistenz': 'inconsistency',
 'die Initiative': 'initiative',
 'die Einsicht, der Einblick': 'insight',
 'die Integrität': 'integrity',
 'die Einmischung': 'interference',
 'der Hebel, der Einfluss': 'leverage',
 'die Haftung': 'liability',
 'die Wahrscheinlichkeit': 'likelihood',
 'der Meilenstein': 'milestone',
 'das Missverständnis, der Irrglaube': 'misconception',
 'die Dynamik, der Schwung': 'momentum',
 'das Motiv': 'motive',
 'die Nuance': 'nuance',
 'das Ergebnis': 'outcome',
 'die Aufsicht; das Versehen': 'oversight',
 'das Tempo': 'pace',
 'das Muster': 'pattern',
 'die Beharrlichkeit': 'persistence',
 'die Perspektive': 'perspective',
 'die Falle, der Fallstrick': 'pitfall',
 'die Plausibilität': 'plausibility',
 'der Präzedenzfall': 'precedent',
 'die Vorliebe, die Präferenz': 'preference',
 'die Prämisse': 'premise',
 'die Verbreitung, die Häufigkeit': 'prevalence',
 'die Priorität': 'priority',
 'die Kompetenz, die Fertigkeit': 'proficiency',
 'der Anteil, das Verhältnis': 'proportion',
 'die Argumentation': 'reasoning',
 'das Widerstreben': 'reluctance',
 'der Rest': 'remainder',
 'die Resilienz, die Widerstandskraft': 'resilience',
 'die Ressource': 'resource',
 'der Umfang, der Rahmen': 'scope',
 'die genaue Prüfung': 'scrutiny',
 'der Rückschlag': 'setback',
 'der Mangel, das Defizit': 'shortcoming',
 'die Bedeutung': 'significance',
 'die Belastung, die Anspannung': 'strain',
 'der Überschuss': 'surplus',
 'die Schwelle': 'threshold',
 'der Übergang': 'transition',
 'die Transparenz': 'transparency',
 'der Trend': 'trend',
 'der Umsatz; die Fluktuation': 'turnover',
 'die Unsicherheit': 'uncertainty',
 'die Dringlichkeit': 'urgency',
 'die Gültigkeit': 'validity',
 'die Tragfähigkeit': 'viability',
 'reichlich': 'abundant',
 'zugänglich': 'accessible',
 'nachteilig, ungünstig': 'adverse',
 'mehrdeutig': 'ambiguous',
 'willkürlich': 'arbitrary',
 'vorteilhaft': 'beneficial',
 'voreingenommen': 'biased',
 'kohärent, schlüssig': 'coherent',
 'überzeugend': 'compelling',
 'kompetent': 'competent',
 'umfassend': 'comprehensive',
 'konsistent, folgerichtig': 'consistent',
 'auffällig': 'conspicuous',
 'entscheidend': 'crucial',
 'umständlich, schwerfällig': 'cumbersome',
 'absichtlich, bewusst': 'deliberate',
 'anspruchsvoll': 'demanding',
 'schädlich': 'detrimental',
 'vielfältig': 'diverse',
 'zweifelhaft': 'dubious',
 'ausführlich, aufwendig': 'elaborate',
 'berechtigt, infrage kommend': 'eligible',
 'herausragend, bedeutend': 'eminent',
 'wesentlich, unerlässlich': 'essential',
 'offenkundig': 'evident',
 'übermäßig': 'excessive',
 'erschöpfend, lückenlos': 'exhaustive',
 'machbar': 'feasible',
 'fehlerhaft': 'flawed',
 'schwankend': 'fluctuating',
 'grundlegend': 'fundamental',
 'unmittelbar bevorstehend': 'imminent',
 'unzureichend': 'inadequate',
 'inklusiv': 'inclusive',
 'widersprüchlich': 'inconsistent',
 'unvermeidlich': 'inevitable',
 'einflussreich': 'influential',
 'innovativ': 'innovative',
 'faszinierend': 'intriguing',
 'irrelevant': 'irrelevant',
 'legitim, rechtmäßig': 'legitimate',
 'verpflichtend': 'mandatory',
 'geringfügig, marginal': 'marginal',
 'irreführend': 'misleading',
 'vernachlässigbar': 'negligible',
 'bemerkenswert': 'notable',
 'spürbar, merklich': 'noticeable',
 'veraltet': 'obsolete',
 'fortlaufend, laufend': 'ongoing',
 'überholt': 'outdated',
 'überwältigend': 'overwhelming',
 'hartnäckig, anhaltend': 'persistent',
 'allgegenwärtig': 'pervasive',
 'plausibel': 'plausible',
 'präzise': 'precise',
 'vorherrschend': 'predominant',
 'weit verbreitet': 'prevalent',
 'prominent, herausragend': 'prominent',
 'verhältnismäßig': 'proportional',
 'fragwürdig': 'questionable',
 'überflüssig': 'redundant',
 'relevant': 'relevant',
 'widerwillig': 'reluctant',
 'widerstandsfähig': 'resilient',
 'streng, gründlich': 'rigorous',
 'robust': 'robust',
 'knapp': 'scarce',
 'unkompliziert': 'straightforward',
 'nachfolgend': 'subsequent',
 'anfällig': 'susceptible',
 'gründlich': 'thorough',
 'einstimmig': 'unanimous',
 'unvoreingenommen': 'unbiased',
 'beispiellos': 'unprecedented',
 'vielseitig': 'versatile',
 'tragfähig, realisierbar': 'viable',
 'verwundbar': 'vulnerable',
 'wohl, möglicherweise': 'arguably',
 'insbesondere': 'notably',
 'dadurch': 'thereby',
 'letztendlich': 'ultimately',
 'einen Rückzieher machen': 'back down',
 'zur Sprache bringen; großziehen': 'bring up',
 'absagen': 'call off',
 'nachholen': 'catch up on',
 'stoßen auf; wirken': 'come across',
 'sich einfallen lassen': 'come up with',
 'einsparen bei': 'cut back on',
 'abschneiden, trennen': 'cut off',
 'zurückgreifen auf': 'draw on',
 'abbrechen, aussteigen': 'drop out',
 'in Rückstand geraten': 'fall behind',
 'nachverfolgen, nachhaken': 'follow up',
 'über die Runden kommen': 'get by',
 'gut auskommen mit; weitermachen': 'get on with',
 'nachgeben': 'give in',
 'durchgehen, überprüfen': 'go over',
 'zurückhalten': 'hold back',
 'Schritt halten mit': 'keep up with',
 'untersuchen': 'look into',
 'wiedergutmachen': 'make up for',
 'eingrenzen': 'narrow down',
 'sich entscheiden für': 'opt for',
 'weitergeben': 'pass on',
 'schrittweise abschaffen': 'phase out',
 'mitbekommen, aufgreifen': 'pick up on',
 'sich abfinden mit': 'put up with',
 'aufbrechen; darlegen': 'set out',
 'einrichten, gründen': 'set up',
 'regeln, klären': 'sort out',
 'herausragen': 'stand out',
 'zurücktreten': 'step down',
 'sich halten an': 'stick to',
 'wenn auch': 'albeit',
 'alles in allem': 'all things considered',
 'tatsächlich, eigentlich': 'as a matter of fact',
 'was mich betrifft': "as far as I'm concerned",
 'auf Kosten von': 'at the expense of',
 'wie dem auch sei': 'be that as it may',
 'im Großen und Ganzen': 'by and large',
 'im Gegensatz zu': 'contrary to',
 'um … willen': 'for the sake of',
 'angesichts der Tatsache, dass': 'given that',
 'daher': 'hence',
 'im Einklang mit': 'in line with',
 'auf lange Sicht': 'in the long run',
 'im Zuge von, nach': 'in the wake of',
 'insofern als': 'insofar as',
 'es versteht sich von selbst': 'it goes without saying',
 'geschweige denn': 'let alone',
 'mit der Begründung, dass': 'on the grounds that',
 'andernfalls': 'otherwise',
 'vorausgesetzt, dass': 'provided that',
 'unabhängig von': 'regardless of',
 'vorbehaltlich': 'subject to',
 'davon abgesehen': 'that being said',
 'somit': 'thus',
 'bis zu einem gewissen Grad': 'to a certain extent',
 'einfach ausgedrückt': 'to put it simply',
 'mit dem Ziel': 'with a view to',
 'in Bezug auf': 'with regard to',
 'die Abgeklärtheit': 'serenity, maturity',
 'der Anflug': 'touch, hint',
 'die Beflissenheit': 'eagerness, zeal',
 'die Behäbigkeit': 'sluggishness, complacency',
 'die Gepflogenheiten': 'customs, practices',
 'das Gebot': 'commandment; bid',
 'die Häme': 'malice, gloating',
 'der Kniefall': 'genuflection, capitulation',
 'die Nonchalance': 'nonchalance',
 'die Preisgabe': 'disclosure; surrender',
 'der Schlendrian': 'sloppiness, slackness',
 'die Unbill': 'hardship, injustice',
 'die Vehemenz': 'vehemence',
 'der Zwist': 'feud, discord',
 'ahnden': 'to punish, to prosecute',
 'bezichtigen': 'to accuse of',
 'darben': 'to suffer want',
 'erheischen': 'to require, to demand',
 'feilschen': 'to haggle',
 'hintertreiben': 'to thwart secretly',
 'kokettieren mit': 'to flirt with (an idea)',
 'lancieren': 'to launch, to plant',
 'obliegen': 'to be incumbent on',
 'nachkommen': 'to comply with',
 'sich anschicken': 'to be about to',
 'verbürgen': 'to vouch for',
 'verquicken': 'to mix up, to intertwine',
 'ambitioniert': 'ambitious',
 'apodiktisch': 'apodictic',
 'behände': 'nimble',
 'blauäugig': 'naive',
 'explizit': 'explicit(ly)',
 'famos': 'splendid',
 'halbherzig': 'half-hearted',
 'kryptisch': 'cryptic',
 'landläufig': 'commonly held',
 'unbotmäßig': 'insubordinate',
 'zuvorderst': 'first and foremost',
 'die Chuzpe': 'chutzpah, nerve',
 'das Fiasko': 'fiasco',
 'die Gemütlichkeit': 'cosiness',
 'der Heißsporn': 'hothead',
 'die Kakophonie': 'cacophony',
 'das Kauderwelsch': 'gibberish',
 'der Kleingeist': 'petty-minded person',
 'die Querele': 'squabble',
 'die Torschlusspanik': 'fear of missing the boat',
 'das Wolkenkuckucksheim': 'cloud-cuckoo-land',
 'der Zeitgeist': 'zeitgeist',
 'der Weltschmerz': 'world-weariness',
 'auf dem Holzweg sein': 'to be barking up the wrong tree',
 'aus allen Wolken fallen': 'to be flabbergasted',
 'das Kind mit dem Bade ausschütten': 'to throw the baby out with the bathwater',
 'den Nagel auf den Kopf treffen': 'to hit the nail on the head',
 'die Flinte ins Korn werfen': 'to throw in the towel',
 'eine Extrawurst verlangen': 'to want special treatment',
 'ins Blaue hinein': 'at random, aimlessly',
 'jemandem den Wind aus den Segeln nehmen': "to take the wind out of sb's sails",
 'Krokodilstränen weinen': 'to shed crocodile tears',
 'mit Kanonen auf Spatzen schießen': 'to use a sledgehammer to crack a nut',
 'sich ins eigene Fleisch schneiden': 'to shoot oneself in the foot',
 'unter einer Decke stecken': 'to be in cahoots',
 'von Tuten und Blasen keine Ahnung haben': 'not to have a clue',
 'wie die Katze um den heißen Brei schleichen': 'to beat around the bush',
 'desavouieren': 'to disavow',
 'echauffieren (sich)': 'to get worked up',
 'perhorreszieren': 'to abhor',
 'prätendieren': 'to claim, to pretend',
 'abstrus': 'abstruse',
 'antiquiert': 'antiquated',
 'frugal': 'frugal',
 'larmoyant': 'maudlin',
 'obsequiös': 'obsequious',
 'sakrosankt': 'sacrosanct',
 'süffisant': 'smug',
 'dabei': 'in doing so, at the same time',
 'dazu': 'in addition, for it',
 'sowie': 'as well as',
 'dafür': 'for it, in return',
 'davon': 'of it, from it',
 'darauf': 'on it, thereupon',
 'zwar … aber': 'admittedly … but',
 'jemand': 'someone',
 'darüber': 'about it, above it',
 'eben': 'just; simply',
 'beide': 'both',
 'daran': 'on it, about it',
 'direkt': 'direct(ly)',
 'anders': 'different(ly)',
 'ebenfalls': 'likewise, also',
 'eher': 'rather; sooner',
 'nachdem': 'after (conjunction)',
 'egal': "no matter, doesn't matter",
 'bisher': 'so far',
 'mehrere': 'several',
 'niemand': 'nobody',
 'zunächst': 'first of all',
 'darum': "that's why",
 'bevor': 'before (conjunction)',
 'wert': 'worth',
 'innerhalb': 'within',
 'völlig': 'completely',
 'zudem': 'moreover',
 'irgendwie': 'somehow',
 'vorbei': 'over, past',
 'dagegen': 'against it; on the other hand',
 'wobei': 'whereby, while',
 'der Einsatz': 'use; deployment; effort',
 'falls': 'in case, if',
 'hinaus': 'out',
 'vorher': 'before, beforehand',
 'häufig': 'frequent(ly)',
 'manche': 'some',
 'unbedingt': 'absolutely, by all means',
 'unterwegs': 'on the way',
 'wenigstens': 'at least',
 'zuvor': 'previously',
 'indem': 'by (doing)',
 'entfernt': 'distant, away',
 'durchaus': 'absolutely, quite',
 'inzwischen': 'meanwhile, by now',
 'komplett': 'complete(ly)',
 'niemals': 'never',
 'erneut': 'again, anew',
 'total': 'totally',
 'früh': 'early',
 'nahe': 'near',
 'nennen': 'to name, to call',
 'erfahren': 'to learn of; to experience',
 'aktiv': 'active',
 'hart': 'hard',
 'offenbar': 'apparently',
 'absolut': 'absolutely',
 'immerhin': 'after all, at least',
 'solange': 'as long as',
 'ständig': 'constantly',
 'persönlich': 'personal(ly)',
 'bieten': 'to offer',
 'spät': 'late',
 'sterben': 'to die',
 'stets': 'always',
 'die Version': 'version',
 'irgendwo': 'somewhere',
 'froh': 'glad',
 'leisten': 'to achieve; to afford',
 'aussehen': 'to look (appearance)',
 'miteinander': 'with each other',
 'schade': 'a pity',
 'schlimm': 'bad',
 'verantwortlich': 'responsible',
 'weltweit': 'worldwide',
 'vorhanden': 'available, existing',
 'die Halle': 'hall',
 'wiederum': 'in turn; again',
 'zugleich': 'at the same time',
 'extrem': 'extreme(ly)',
 'längst': 'long since',
 'positiv': 'positive',
 'böse': 'evil; angry',
 'diesmal': 'this time',
 'handeln': 'to act; to trade',
 'notwendig': 'necessary',
 'näher': 'closer',
 'reichen': 'to be enough; to pass',
 'die Industrie': 'industry',
 'innen': 'inside',
 'unglaublich': 'unbelievable',
 'sich befinden': 'to be located',
 'das Finale': 'final',
 'herum': 'around',
 'der Landkreis': 'district',
 'treten': 'to step; to kick',
 'entgegen': 'contrary to, towards',
 'hauptsächlich': 'mainly',
 'ansehen': 'to look at, to watch',
 'international': 'international',
 'sicherlich': 'certainly',
 'vollkommen': 'perfect; completely',
 'mitten': 'in the middle',
 'seitdem': 'since then',
 'sowieso': 'anyway',
 'die Stiftung': 'foundation',
 'vollständig': 'complete',
 'unabhängig': 'independent',
 'erleben': 'to experience',
 'schlagen': 'to hit; to beat',
 'entlang': 'along',
 'kriegen': 'to get (colloquial)',
 'teils': 'partly',
 'bewegen': 'to move',
 'dienen': 'to serve',
 'ursprünglich': 'originally',
 'der Wille': 'will',
 'abgesehen von': 'apart from',
 'komisch': 'strange; funny',
 'mehrfach': 'several times',
 'steuern': 'to steer, to control',
 'aussagen': 'to testify, to state',
 'geschickt': 'skilful',
 'politisch': 'political',
 'real': 'real',
 'daneben': 'next to it; besides',
 'dringend': 'urgent(ly)',
 'hängen': 'to hang',
 'morgens': 'in the morning',
 'nachts': 'at night',
 'der Nutzer': 'user',
 'die Nutzung': 'use',
 'tätig': 'active, working',
 'automatisch': 'automatic',
 'gelassen': 'calm, relaxed',
 'momentan': 'at the moment',
 'nahezu': 'almost',
 'demnach': 'accordingly',
 'der Hersteller': 'manufacturer',
 'jemals': 'ever',
 'kaputt': 'broken',
 'mittels': 'by means of',
 'unmittelbar': 'immediate(ly)',
 'fordern': 'to demand',
 'gestalten': 'to shape, to design',
 'anscheinend': 'apparently',
 'die Kommunikation': 'communication',
 'scheinen': 'to seem; to shine',
 'spätestens': 'at the latest',
 'stecken': 'to put in; to be stuck',
 'voraus': 'ahead',
 'achten auf': 'to pay attention to',
 'ausgezeichnet': 'excellent',
 'einst': 'once',
 'die Integration': 'integration',
 'womit': 'with what',
 'der Code': 'code',
 'definitiv': 'definitely',
 'drehen': 'to turn; to shoot (film)',
 'gratis': 'free of charge',
 'witzig': 'funny',
 'zumal': 'especially since',
 'anstatt': 'instead of',
 'aufmerksam': 'attentive',
 'ausgeschlossen': 'out of the question',
 'begeistert': 'enthusiastic',
 'daraufhin': 'thereupon',
 'erforderlich': 'required',
 'ewig': 'eternal',
 'aufnehmen': 'to record; to take in',
 'speziell': 'special',
 'der Tipp': 'tip',
 'betroffen': 'affected',
 'erfolgen': 'to take place',
 'ernsthaft': 'serious(ly)',
 'der Hass': 'hatred',
 'sinnvoll': 'sensible',
 'sofern': 'provided that',
 'das Umfeld': 'environment, surroundings',
 'vergeben': 'to forgive; to award',
 'einerseits … andererseits': 'on the one hand … on the other',
 'eventuell': 'possibly',
 'generell': 'generally',
 'gucken': 'to look (colloquial)',
 'quasi': 'virtually, so to speak',
 'scheinbar': 'seemingly',
 'die Variante': 'variant',
 'genügend': 'sufficient',
 'lieb': 'dear, kind',
 'maximal': 'maximum',
 'bezüglich': 'regarding',
 'blöd': 'stupid',
 'ordentlich': 'tidy, proper',
 'wach': 'awake',
 'greifen': 'to grab',
 'die Hölle': 'hell',
 'locker': 'loose, relaxed',
 'sichtbar': 'visible',
 'dankbar': 'grateful',
 'dicht': 'dense; tight',
 'doppelt': 'double',
 'einzig': 'only, sole',
 'gezwungen': 'forced',
 'inklusive': 'including',
 'stammen aus': 'to come from',
 'still': 'quiet',
 'vorgehen': 'to proceed',
 'zuständig': 'responsible, in charge',
 'der Anbieter': 'provider',
 'herzlich': 'warm(ly)',
 'spannend': 'exciting',
 'treiben': 'to drive; to do (sport)',
 'töten': 'to kill',
 'unterschiedlich': 'different',
 'beinahe': 'almost',
 'fassen': 'to grasp',
 'gebildet': 'educated',
 'geraten in': 'to get into',
 'jederzeit': 'at any time',
 'das Netzwerk': 'network',
 'reagieren': 'to react',
 'der Schuss': 'shot',
 'spenden': 'to donate',
 'verbringen': 'to spend (time)',
 'beziehen': 'to obtain; to move into',
 'ferner': 'furthermore',
 'gelangen': 'to reach',
 'hinterher': 'afterwards',
 'der Rassismus': 'racism',
 'die Fraktion': 'parliamentary group',
 'freiwillig': 'voluntary',
 'gewohnt': 'used to',
 'die Kooperation': 'cooperation',
 'lächerlich': 'ridiculous',
 'nachher': 'afterwards',
 'negativ': 'negative',
 'richten': 'to direct',
 'zufolge': 'according to',
 'endgültig': 'final(ly)',
 'fair': 'fair',
 'die Finanzierung': 'financing',
 'gering': 'low, small',
 'umgehen mit': 'to deal with',
 'wiederholt': 'repeatedly',
 'angebracht': 'appropriate',
 'mehrmals': 'several times',
 'spüren': 'to feel, to sense',
 'die Verbesserung': 'improvement',
 'gerecht': 'just, fair',
 'heutzutage': 'nowadays',
 'die Hinsicht': 'respect, regard',
 'insofern': 'in this respect',
 'künftig': 'in future',
 'die Option': 'option',
 'rechtzeitig': 'in time',
 'verrückt': 'crazy',
 'entfernen': 'to remove',
 'gelegentlich': 'occasionally',
 'typisch': 'typical',
 'sich wenden an': 'to turn to',
 'abgeben': 'to hand in',
 'die Erweiterung': 'extension',
 'nackt': 'naked',
 'peinlich': 'embarrassing',
 'verteidigen': 'to defend',
 'das Überleben': 'survival',
 'demnächst': 'soon',
 'fein': 'fine',
 'heftig': 'violent, heavy',
 'die Kampagne': 'campaign',
 'korrekt': 'correct',
 'oftmals': 'often',
 'präsentieren': 'to present',
 'siegen': 'to win',
 'sozial': 'social',
 'technisch': 'technical',
 'ausgerechnet': 'of all things',
 'landen': 'to land',
 'profitieren': 'to benefit',
 'umsonst': 'in vain; free',
 'einander': 'each other',
 'erstaunlich': 'astonishing',
 'die Motivation': 'motivation',
 'der Profi': 'professional',
 'der Beschluss': 'resolution, decision',
 'brechen': 'to break',
 'ehren': 'to honour',
 'erlangen': 'to attain',
 'gefangen': 'captured',
 'kürzlich': 'recently',
 'massiv': 'massive',
 'rasch': 'quick',
 'spontan': 'spontaneous',
 'verraten': 'to betray, to reveal',
 'verständlich': 'understandable',
 'angewiesen auf': 'dependent on',
 'bedingt': 'conditional; partly',
 'beschränkt': 'limited',
 'hübsch': 'pretty',
 'jenseits': 'beyond',
 'räumen': 'to clear',
 'seltsam': 'strange',
 'versteckt': 'hidden',
 'der Kumpel': 'mate, buddy',
 'der Tourismus': 'tourism',
 'unbekannt': 'unknown',
 'die Vielfalt': 'diversity',
 'zerstören': 'to destroy',
 'angenehm': 'pleasant',
 'beachten': 'to observe, to heed',
 'belegen': 'to prove; to take (course)',
 'daheim': 'at home',
 'digital': 'digital',
 'einig': 'in agreement',
 'hinterlassen': 'to leave behind',
 'kontrollieren': 'to check',
 'quer': 'across',
 'samt': 'together with',
 'vertraut': 'familiar',
 'wetten': 'to bet',
 'derart': 'so, such',
 'einverstanden': 'agreed',
 'erzielen': 'to achieve',
 'fern': 'far',
 'klagen': 'to complain; to sue',
 'konkret': 'concrete',
 'nebenbei': 'incidentally; on the side',
 'wunderschön': 'beautiful',
 'blind': 'blind',
 'dauerhaft': 'permanent',
 'durchschnittlich': 'average',
 'heiraten': 'to marry',
 'historisch': 'historical',
 'langfristig': 'long-term',
 'mitmachen': 'to join in',
 'passend': 'suitable',
 'schief': 'crooked',
 'die Überwachung': 'surveillance',
 'die Altstadt': 'old town',
 'besorgt': 'worried',
 'die Erhöhung': 'increase',
 'hilfreich': 'helpful',
 'höchst': 'highly',
 'soeben': 'just now',
 'die Staatsanwaltschaft': "public prosecutor's office",
 'weichen': 'to give way',
 'die Betreuung': 'care, supervision',
 'glatt': 'smooth',
 'jahrelang': 'for years',
 'der Modus': 'mode',
 'schlicht': 'plain, simple',
 'die Vielzahl': 'multitude',
 'vorerst': 'for the time being',
 'zustande kommen': 'to come about',
 'der Betreiber': 'operator',
 'das Detail': 'detail',
 'das Fazit': 'conclusion',
 'kennenlernen': 'to get to know',
 'schuldig': 'guilty; owing',
 'sozusagen': 'so to speak',
 'verstecken': 'to hide',
 'vorhin': 'a moment ago',
 'zugunsten': 'in favour of',
 'die Dokumentation': 'documentation',
 'die Einschätzung': 'assessment',
 'exakt': 'exact',
 'finanziell': 'financial',
 'infolge': 'as a result of',
 'der Jahrgang': 'year, vintage',
 'schrecklich': 'terrible',
 'seither': 'since then',
 'unklar': 'unclear',
 'unterhalb': 'below',
 'wirtschaftlich': 'economic',
 'aufbauen': 'to build up',
 'bedienen': 'to serve; to operate',
 'dazwischen': 'in between',
 'die Erfüllung': 'fulfilment',
 'erwähnen': 'to mention',
 'klingen': 'to sound',
 'neulich': 'recently',
 'opfern': 'to sacrifice',
 'umgeben': 'to surround',
 'ungewöhnlich': 'unusual',
 'die Zerstörung': 'destruction',
 'abseits': 'away from',
 'befreien': 'to free',
 'betreten': 'to enter',
 'dauernd': 'constantly',
 'der Entwickler': 'developer',
 'erstens': 'firstly',
 'konsequent': 'consistent',
 'kräftig': 'strong',
 'lokal': 'local',
 'wandern': 'to hike',
 'einzeln': 'individual(ly)',
 'enorm': 'enormous',
 'etliche': 'quite a few',
 'kurzfristig': 'short-term',
 'mitunter': 'at times',
 'mächtig': 'powerful',
 'woanders': 'elsewhere',
 'der Zugriff': 'access',
 'zweitens': 'secondly',
 'die Bearbeitung': 'processing',
 'gebrauchen': 'to use',
 'stabil': 'stable',
 'vorwiegend': 'predominantly',
 'wahnsinnig': 'insane(ly)',
 'die Weiterbildung': 'further education',
 'bekämpfen': 'to fight',
 'die Berichterstattung': 'reporting',
 'blicken': 'to look, to glance',
 'erheben': 'to raise; to levy',
 'erreichbar': 'reachable',
 'unendlich': 'infinite',
 'unnötig': 'unnecessary',
 'vorliegen': 'to be available',
 'die Aufstellung': 'list; line-up',
 'ausprobieren': 'to try out',
 'benötigen': 'to need',
 'binnen': 'within',
 'entschlossen': 'determined',
 'die Erhebung': 'survey; levy',
 'gewöhnt': 'accustomed',
 'herrlich': 'wonderful',
 'pleite': 'broke',
 'unsicher': 'unsure, unsafe',
 'das Vorfeld': 'run-up',
 'die Allianz': 'alliance',
 'gemein': 'mean',
 'genial': 'brilliant',
 'der Konzern': 'group, corporation',
 'das Medium': 'medium',
 'die Route': 'route',
 'schlau': 'clever',
 'traditionell': 'traditional',
 'treu': 'loyal',
 'abwarten': 'to wait and see',
 'der Einzelfall': 'individual case',
 'die Episode': 'episode',
 'erfreut': 'pleased',
 'der Genuss': 'pleasure',
 'heimlich': 'secret(ly)',
 'die Präsentation': 'presentation',
 'der Rechner': 'computer',
 'streichen': 'to paint; to cancel',
 'untereinander': 'among themselves',
 'sich wehren': 'to defend oneself',
 'wissenschaftlich': 'scientific',
 'anlegen': 'to invest; to set up',
 'denkbar': 'conceivable',
 'furchtbar': 'awful',
 'geradezu': 'downright',
 'gesetzlich': 'legal',
 'gewöhnlich': 'usual',
 'hervorragend': 'excellent',
 'illegal': 'illegal',
 'komplex': 'complex',
 'nirgends': 'nowhere',
 'schieben': 'to push',
 'südlich': 'southern',
 'zeitweise': 'at times',
 'die Berücksichtigung': 'consideration',
 'der Erhalt': 'receipt; preservation',
 'eröffnen': 'to open',
 'die Fotografie': 'photography',
 'friedlich': 'peaceful',
 'lebendig': 'lively',
 'nördlich': 'northern',
 'die Orientierung': 'orientation',
 'rechtlich': 'legal',
 'vernünftig': 'sensible',
 'aufhalten': 'to stop, to hold up',
 'die Datenbank': 'database',
 'der Datenschutz': 'data protection',
 'der Einstieg': 'entry',
 'erwachsen': 'adult',
 'konstant': 'constant',
 'oberhalb': 'above',
 'die Pressemitteilung': 'press release',
 'reiten': 'to ride',
 'sinken': 'to sink, to fall',
 'unangenehm': 'unpleasant',
 'verschaffen': 'to procure',
 'verzweifelt': 'desperate',
 'vorwärts': 'forward',
 'der Asylbewerber': 'asylum seeker',
 'die Ausrichtung': 'alignment, focus',
 'betrunken': 'drunk',
 'die Bezahlung': 'payment',
 'die Digitalisierung': 'digitalisation',
 'finanzieren': 'to finance',
 'flach': 'flat',
 'gewiss': 'certain',
 'grob': 'rough',
 'senken': 'to lower',
 'zulassen': 'to allow',
 'antreten': 'to take up; to compete',
 'der Arbeitsmarkt': 'labour market',
 'brennen': 'to burn',
 'circa': 'about',
 'die Elite': 'elite',
 'erwerben': 'to acquire',
 'fröhlich': 'cheerful',
 'logisch': 'logical',
 'die Migration': 'migration',
 'die Partnerschaft': 'partnership',
 'vorübergehend': 'temporary',
 'weitaus': 'by far',
 'zielen auf': 'to aim at',
 'besorgen': 'to get, to obtain',
 'fliehen': 'to flee',
 'merkwürdig': 'odd',
 'der Notfall': 'emergency',
 'schriftlich': 'in writing',
 'verdanken': 'to owe',
 'zeitlich': 'in terms of time',
 'anhören': 'to listen to',
 'annähernd': 'approximately',
 'anwesend': 'present',
 'aufstellen': 'to set up',
 'die Auswertung': 'evaluation',
 'begreifen': 'to comprehend',
 'beruflich': 'professional',
 'buchen': 'to book',
 'erben': 'to inherit',
 'geistig': 'mental',
 'der Mindestlohn': 'minimum wage',
 'versorgen': 'to supply, to look after',
 'verursachen': 'to cause',
 'ausdrücken': 'to express',
 'errichten': 'to erect',
 'fähig': 'capable',
 'gänzlich': 'entirely',
 'primär': 'primarily',
 'die Sanierung': 'renovation',
 'stetig': 'steady',
 'stürzen': 'to fall',
 'unwahrscheinlich': 'unlikely',
 'das Vorjahr': 'previous year',
 'ausmachen': 'to switch off; to make up',
 'effektiv': 'effective',
 'individuell': 'individual',
 'legal': 'legal',
 'mobil': 'mobile',
 'unglücklich': 'unhappy',
 'verlegen': 'embarrassed',
 'weich': 'soft',
 'zulässig': 'permissible',
 'zwingend': 'compulsory',
 'zwischendurch': 'in between',
 'allmählich': 'gradually',
 'berühmt': 'famous',
 'bremsen': 'to brake',
 'demonstrieren': 'to demonstrate',
 'identisch': 'identical',
 'riesig': 'huge',
 'sinnlos': 'pointless',
 'sorgfältig': 'careful',
 'strafen': 'to punish',
 'werben': 'to advertise',
 'die Zulassung': 'approval; admission',
 'die Aktivität': 'activity',
 'aufrecht': 'upright',
 'sich begeben': 'to proceed',
 'beherrschen': 'to master',
 'durcheinander': 'in a muddle',
 'indirekt': 'indirect',
 'körperlich': 'physical',
 'locken': 'to lure',
 'prinzipiell': 'in principle',
 'der Riss': 'crack',
 'umgehend': 'immediately',
 'verletzen': 'to injure',
 'die Zielgruppe': 'target group',
 'zugrunde liegen': 'to underlie',
 'der Abstieg': 'descent, relegation',
 'der Anleger': 'investor',
 'die Bekämpfung': 'fight against',
 'besprechen': 'to discuss',
 'brav': 'well-behaved',
 'die Formulierung': 'wording',
 'hässlich': 'ugly',
 'jagen': 'to hunt',
 'die Kreativität': 'creativity',
 'lauten': 'to read, to go (text)',
 'sportlich': 'sporty',
 'tödlich': 'deadly',
 'unheimlich': 'scary; incredibly',
 'verkehrt': 'wrong, the wrong way',
 'die Diskriminierung': 'discrimination',
 'einnehmen': 'to take; to earn',
 'männlich': 'male',
 'sanft': 'gentle',
 'die Ankündigung': 'announcement',
 'der Auftakt': 'start, prelude',
 'ausfallen': 'to be cancelled',
 'beten': 'to pray',
 'brutal': 'brutal',
 'sich eignen': 'to be suitable',
 'frühzeitig': 'early',
 'die Kriminalität': 'crime',
 'das Potenzial': 'potential',
 'problematisch': 'problematic',
 'die Recherche': 'research',
 'voraussichtlich': 'expected(ly)',
 'vornehmen': 'to carry out; to resolve',
 'zukünftig': 'future',
 'anonym': 'anonymous',
 'ausführen': 'to carry out',
 'das Bedürfnis': 'need',
 'entgehen': 'to escape, to miss',
 'die Innovation': 'innovation',
 'nebenan': 'next door',
 'spazieren gehen': 'to go for a walk',
 'tagsüber': 'during the day',
 'benehmen (sich)': 'to behave',
 'entnehmen': 'to take from, to gather',
 'glücklicherweise': 'fortunately',
 'die Mobilität': 'mobility',
 'die Präsenz': 'presence',
 'tauchen': 'to dive',
 'verbrennen': 'to burn',
 'verleihen': 'to lend; to award',
 'der Verlierer': 'loser',
 'verweisen auf': 'to refer to',
 'wecken': 'to wake',
 'aussuchen': 'to pick',
 'einsam': 'lonely',
 'eintreten': 'to enter; to occur',
 'gewaltig': 'enormous',
 'die Investition': 'investment',
 'sich orientieren': 'to orient oneself',
 'sperren': 'to block',
 'staatlich': 'state, public',
 'die Uhrzeit': 'time (of day)',
 'die Umstellung': 'changeover',
 'zusehen': 'to watch',
 'bearbeiten': 'to edit, to process',
 'gefährden': 'to endanger',
 'gepflegt': 'well-kept',
 'hintereinander': 'in a row',
 'der Klimaschutz': 'climate protection',
 'die Privatsphäre': 'privacy',
 'realistisch': 'realistic',
 'die Schaffung': 'creation',
 'skeptisch': 'sceptical',
 'vergeblich': 'in vain',
 'weiblich': 'female',
 'wertvoll': 'valuable',
 'westlich': 'western',
 'wirksam': 'effective',
 'überfallen': 'to attack, to rob',
 'absurd': 'absurd',
 'die Akzeptanz': 'acceptance',
 'besetzen': 'to occupy; to fill',
 'drängen': 'to push, to urge',
 'sich engagieren': 'to get involved',
 'fraglich': 'questionable',
 'rückwärts': 'backwards',
 'die Tragödie': 'tragedy',
 'abstimmen': 'to vote',
 'der Ausschluss': 'exclusion',
 'drüben': 'over there',
 'durchgehend': 'continuous(ly)',
 'entkommen': 'to escape',
 'erlassen': 'to issue; to waive',
 'ernähren': 'to feed',
 'erschaffen': 'to create',
 'menschlich': 'human',
 'psychisch': 'psychological',
 'realisieren': 'to realise',
 'vergangen': 'past',
 'fällig': 'due',
 'gegenwärtig': 'current',
 'heilig': 'holy',
 'klassisch': 'classic(al)',
 'korrigieren': 'to correct',
 'lenken': 'to steer',
 'sympathisch': 'likeable',
 'unerwartet': 'unexpected',
 'ausnahmsweise': 'for once',
 'die Ermittlung': 'investigation',
 'gönnen': 'not to begrudge',
 'intern': 'internal',
 'künstlich': 'artificial',
 'leuchten': 'to shine',
 'lose': 'loose',
 'naiv': 'naive',
 'der Rechtsstaat': 'constitutional state',
 'ruhen': 'to rest',
 'stundenlang': 'for hours',
 'ungern': 'reluctantly',
 'unschuldig': 'innocent',
 'unterliegen': 'to be subject to; to lose',
 'vereinzelt': 'isolated',
 'ahnen': 'to suspect, to sense',
 'angreifen': 'to attack',
 'erobern': 'to conquer',
 'geheim': 'secret',
 'harmlos': 'harmless',
 'intelligent': 'intelligent',
 'die Lebensqualität': 'quality of life',
 'loswerden': 'to get rid of',
 'nebeneinander': 'side by side',
 'das Selbstbewusstsein': 'self-confidence',
 'unterrichten': 'to teach',
 'vernichten': 'to destroy',
 'verschlossen': 'locked; reserved',
 'das Weltbild': 'world view',
 'wörtlich': 'literal(ly)',
 'östlich': 'eastern',
 'die Abgrenzung': 'demarcation',
 'sich aufregen': 'to get upset',
 'beleidigen': 'to insult',
 'bestreiten': 'to deny; to cover',
 'blockieren': 'to block',
 'ergreifen': 'to seize; to take',
 'hinzufügen': 'to add',
 'liebevoll': 'loving',
 'mies': 'lousy',
 'mischen': 'to mix',
 'nüchtern': 'sober',
 'optisch': 'visual',
 'strahlen': 'to beam',
 'die Thematik': 'subject matter',
 'die Unterscheidung': 'distinction',
 'der Unterstützer': 'supporter',
 'abhalten': 'to hold; to keep from',
 'anderswo': 'elsewhere',
 'austauschen': 'to exchange',
 'ausverkauft': 'sold out',
 'beiseite': 'aside',
 'dramatisch': 'dramatic',
 'erwünscht': 'desired',
 'gesamt': 'total',
 'neutral': 'neutral',
 'platt': 'flat; flabbergasted',
 'stützen': 'to support',
 'widerlich': 'disgusting',
 'die Attacke': 'attack',
 'der Austritt': 'exit',
 'die Befragung': 'survey, questioning',
 'beliebig': 'any',
 'eigen': 'own',
 'das Feuerwerk': 'fireworks',
 'garantieren': 'to guarantee',
 'gemischt': 'mixed',
 'die Publikation': 'publication',
 'schräg': 'slanted',
 'der Terrorismus': 'terrorism',
 'unzufrieden': 'dissatisfied',
 'verarbeiten': 'to process',
 'abschalten': 'to switch off',
 'die Auszeit': 'time out',
 'diesbezüglich': 'in this regard',
 'die Erstellung': 'creation',
 'die Fertigstellung': 'completion',
 'herrschen': 'to rule, to prevail',
 'neuerdings': 'recently',
 'radikal': 'radical',
 'die Relevanz': 'relevance',
 'vorzeitig': 'premature(ly)',
 'absetzen': 'to put down; to depose',
 'allerlei': 'all sorts of',
 'angehören': 'to belong to',
 'anhalten': 'to stop',
 'die Auslegung': 'interpretation',
 'ausrichten': 'to pass on; to organise',
 'belasten': 'to burden',
 'einsehen': 'to realise',
 'flüchten': 'to flee',
 'der Lebensraum': 'habitat',
 'verwickelt': 'complicated; involved',
 'verzeichnen': 'to record',
 'die Zugehörigkeit': 'affiliation, belonging',
 'entfallen': 'to be dropped',
 'gleichfalls': 'likewise',
 'die Inspiration': 'inspiration',
 'die Leistungsfähigkeit': 'efficiency',
 'ablegen': 'to take off; to take (exam)',
 'absolvieren': 'to complete',
 'der Anwohner': 'resident',
 'erfinden': 'to invent',
 'frech': 'cheeky',
 'die Immobilie': 'property',
 'die Rendite': 'return, yield',
 'schlank': 'slim',
 'steil': 'steep',
 'der Stellenwert': 'importance',
 'veranstalten': 'to organise',
 'allenfalls': 'at most',
 'ausbauen': 'to expand',
 'beibehalten': 'to retain',
 'bescheiden': 'modest',
 'demokratisch': 'democratic',
 'erfolglos': 'unsuccessful',
 'die Lebensweise': 'way of life',
 'nacheinander': 'one after another',
 'reinigen': 'to clean',
 'stehlen': 'to steal',
 'transparent': 'transparent',
 'verwirklichen': 'to realise',
 'zweifellos': 'undoubtedly',
 'der Ansprechpartner': 'contact person',
 'benennen': 'to name',
 'bestrafen': 'to punish',
 'der Entschluss': 'decision',
 'erteilen': 'to grant, to give',
 'grausam': 'cruel',
 'mühsam': 'laborious',
 'die Registrierung': 'registration',
 'unverzüglich': 'without delay',
 'die Vorgehensweise': 'approach',
 'abschaffen': 'to abolish',
 'das Darlehen': 'loan',
 'die Insolvenz': 'insolvency',
 'nachfragen': 'to ask, to enquire',
 'sich nähern': 'to approach',
 'selbständig': 'independent',
 'unerträglich': 'unbearable',
 'der Zusammenschluss': 'merger',
 'ausreichen': 'to suffice',
 'ausscheiden': 'to be eliminated; to leave',
 'die Ausschreibung': 'tender; advertisement',
 'der Ausstieg': 'exit',
 'auswendig': 'by heart',
 'die Gleichberechtigung': 'equality',
 'moralisch': 'moral',
 'schmerzhaft': 'painful',
 'ungerecht': 'unfair',
 'verdächtig': 'suspicious',
 'vereinbaren': 'to agree on',
 'versehentlich': 'by mistake',
 'zittern': 'to tremble',
 'abwechselnd': 'alternately',
 'der Auftraggeber': 'client',
 'beschleunigen': 'to accelerate',
 'besiegen': 'to defeat',
 'sich erholen': 'to recover',
 'die Festplatte': 'hard drive',
 'genügen': 'to suffice',
 'die Intensität': 'intensity',
 'nutzlos': 'useless',
 'optimistisch': 'optimistic',
 'romantisch': 'romantic'}

DE_EN_ACADEMIC = {'die Forschung': 'research',
 'die Daten (Pl.)': 'data',
 'die Methode': 'method',
 'die Quelle': 'source',
 'der Nachweis, die Belege (Pl.)': 'evidence',
 'die Analyse': 'analysis',
 'der Faktor': 'factor',
 'der Prozess': 'process',
 'die Struktur': 'structure',
 'definieren': 'define',
 'identifizieren, ermitteln': 'identify',
 'hindeuten auf, zeigen': 'indicate',
 'auftreten': 'occur',
 'erfordern': 'require',
 'bewerten, beurteilen': 'assess',
 'feststellen; etablieren': 'establish',
 'signifikant, bedeutend': 'significant',
 'ähnlich': 'similar',
 'spezifisch': 'specific',
 'darüber hinaus': 'furthermore',
 'beispielsweise': 'for instance',
 'der Ansatz': 'approach',
 'das Ziel': 'aim',
 'das Kapitel': 'chapter',
 'die Schlussfolgerung': 'conclusion',
 'die Abbildung; die Zahl': 'figure',
 'die Einleitung': 'introduction',
 'die Frage, das Problem': 'issue',
 'das Niveau': 'level',
 'der Zeitraum': 'period',
 'der Verweis, die Quelle': 'reference',
 'die Zusammenfassung': 'summary',
 'die Tabelle': 'table',
 'das Thema': 'topic',
 'beeinflussen': 'affect',
 'erörtern, diskutieren': 'discuss',
 'erklären': 'explain',
 'einschließen': 'include',
 'messen': 'measure',
 'bereitstellen, liefern': 'provide',
 'vorschlagen; nahelegen': 'suggest',
 'unterstützen': 'support',
 'verbreitet, üblich': 'common',
 'aktuell': 'current',
 'vorherig': 'previous',
 'jedoch': 'however',
 'daher': 'therefore',
 'abschließend': 'in conclusion',
 'wie zum Beispiel': 'such as',
 'angeben, feststellen': 'state',
 'hinterfragen': 'question',
 'die Reihe, die Serie': 'series',
 'berichten': 'report',
 'auflisten': 'list',
 'prognostizieren': 'project',
 'aufzeichnen, erfassen': 'record',
 'testen': 'test',
 'das Ergebnis': 'result',
 'modellieren': 'model',
 'überprüfen; rezensieren': 'review',
 'der Bereich, die Spannweite': 'range',
 'die Phase, das Stadium': 'stage',
 'festhalten, anmerken': 'note',
 'die Konferenz, die Tagung': 'conference',
 'die Grundgesamtheit, die Population': 'population',
 'der Fokus': 'focus',
 'der Abschnitt': 'section',
 'insbesondere': 'particularly',
 'die Anwendung; die Bewerbung': 'application',
 'die Bedingung': 'condition',
 'die Skala': 'scale',
 'kritisch': 'critical',
 'die Autorität': 'authority',
 'die Grundlage': 'foundation',
 'die Funktion': 'function',
 'beweisen': 'prove',
 'die Fachzeitschrift': 'journal',
 'der Band; das Volumen': 'volume',
 'reduzieren': 'reduce',
 'die Alternative': 'alternative',
 'relativ': 'relatively',
 'zahlreich': 'numerous',
 'der Begriff, das Konzept': 'concept',
 'der Kontext': 'context',
 'der Rahmen': 'framework',
 'die Hypothese': 'hypothesis',
 'der Teilnehmer, die Teilnehmerin': 'participant',
 'die Stichprobe': 'sample',
 'die Umfrage': 'survey',
 'die Variable': 'variable',
 'interpretieren': 'interpret',
 'nachweisen, zeigen': 'demonstrate',
 'ableiten': 'derive',
 'erhalten, gewinnen': 'obtain',
 'untersuchen': 'investigate',
 'relevant': 'relevant',
 'übereinstimmend, konsistent': 'consistent',
 'angemessen, geeignet': 'appropriate',
 'folglich': 'consequently',
 'zusätzlich': 'in addition',
 'während, wohingegen': 'whereas',
 'der Aspekt': 'aspect',
 'der Nutzen': 'benefit',
 'die Kategorie': 'category',
 'die Komponente': 'component',
 'das Merkmal': 'feature',
 'die Auswirkung': 'impact',
 'das Interview': 'interview',
 'der Prozentsatz': 'percentage',
 'der Fragebogen': 'questionnaire',
 'die Antwort, die Reaktion': 'response',
 'die Rolle': 'role',
 'erreichen': 'achieve',
 'analysieren': 'analyse',
 'anwenden': 'apply',
 'vergleichen': 'compare',
 'schlussfolgern': 'conclude',
 'gegenüberstellen': 'contrast',
 'vorhersagen': 'predict',
 'sich beziehen auf': 'refer to',
 'auswählen': 'select',
 'genau': 'accurate',
 'verfügbar': 'available',
 'bedeutend': 'major',
 'außerdem': 'moreover',
 'ebenso': 'similarly',
 'insgesamt': 'overall',
 'andererseits': 'on the other hand',
 'typischerweise': 'typically',
 'entwerfen': 'draft',
 'die Statistik': 'statistics',
 'der Fall, das Beispiel': 'instance',
 'die Definition': 'definition',
 'zufällig': 'random',
 'der Index': 'index',
 'repräsentativ': 'representative',
 'der Anteil': 'portion',
 'pilotieren, erproben': 'pilot',
 'zitieren': 'quote',
 'der Vergleich': 'comparison',
 'dokumentieren': 'document',
 'die Konvention': 'convention',
 'gleichwertig, äquivalent': 'equivalent',
 'zeitgenössisch': 'contemporary',
 'anfangs': 'initially',
 'die Technik': 'technique',
 'die Bewertung': 'assessment',
 'das Element': 'element',
 'die Formel': 'formula',
 'die Veröffentlichung': 'publication',
 'einstufen, ranken': 'rank',
 'die Erklärung': 'explanation',
 'das Verfahren': 'procedure',
 'kennzeichnen': 'label',
 'der Output, die Ausgabe': 'output',
 'im Wesentlichen': 'essentially',
 'die Institution': 'institution',
 'das Experiment': 'experiment',
 'einführen, vorstellen': 'introduce',
 'das Verhältnis': 'ratio',
 'lediglich': 'merely',
 'die Häufigkeit': 'frequency',
 'die Ausnahme': 'exception',
 'der Input, die Eingabe': 'input',
 'der Datensatz': 'data set',
 'abhängen von': 'depend on',
 'kartieren, planen': 'map (out)',
 'in Beziehung setzen': 'relate to',
 'betreffen': 'pertain to',
 'die Fallstudie': 'case study',
 'beschränken auf': 'restrict to',
 'die Stichprobengröße': 'sample size',
 'im Hinblick auf': 'in terms of',
 'im Gegensatz dazu': 'by contrast',
 'sich identifizieren mit': 'identify with',
 'die Forschungslücke': 'knowledge gap',
 'die Rücklaufquote': 'response rate',
 'die Annahme': 'assumption',
 'das Kriterium': 'criterion',
 'die Implikation, die Folgerung': 'implication',
 'die Einschränkung, die Limitation': 'limitation',
 'die Perspektive': 'perspective',
 'das Phänomen': 'phenomenon',
 'die Korrelation': 'correlation',
 'der Trend, die Tendenz': 'trend',
 'argumentieren': 'argue',
 'veranschaulichen': 'illustrate',
 'betonen': 'emphasise',
 'evaluieren, auswerten': 'evaluate',
 'klären': 'clarify',
 'skizzieren': 'outline',
 'entscheidend': 'crucial',
 'empirisch': 'empirical',
 'nachfolgend': 'subsequent',
 'somit': 'thus',
 'dennoch': 'nevertheless',
 'das Argument': 'argument',
 'die Behauptung': 'claim',
 'die Folge': 'consequence',
 'die Dimension': 'dimension',
 'die Betonung': 'emphasis',
 'der Indikator': 'indicator',
 'die Zielsetzung': 'objective',
 'die Strategie': 'strategy',
 'die Theorie': 'theory',
 'anerkennen': 'acknowledge',
 'übernehmen': 'adopt',
 'vorwegnehmen, erwarten': 'anticipate',
 'annehmen': 'assume',
 'kategorisieren': 'categorise',
 'infrage stellen': 'challenge',
 'bestimmen': 'determine',
 'steigern, verbessern': 'enhance',
 'hervorheben': 'highlight',
 'aufrechterhalten; behaupten': 'maintain',
 'beträchtlich': 'considerable',
 'explizit': 'explicit',
 'potenziell': 'potential',
 'dementsprechend': 'accordingly',
 'in erster Linie': 'primarily',
 'in gewissem Maße': 'to some extent',
 'hinsichtlich': 'with regard to',
 'die Abfolge, die Sequenz': 'sequence',
 'der Beitrag': 'contribution',
 'das Prinzip': 'principle',
 'die Zusammensetzung': 'composition',
 'einheitlich': 'uniform',
 'das Feedback, die Rückmeldung': 'feedback',
 'ausreichend': 'sufficient',
 'dynamisch': 'dynamic',
 'kollektiv, gemeinsam': 'collective',
 'die Schätzung': 'estimate',
 'die Wechselwirkung': 'interaction',
 'eindeutig, verschieden': 'distinct',
 'parallel': 'parallel',
 'das Instrument': 'instrument',
 'die Intervention': 'intervention',
 'die Anforderung': 'requirement',
 'die Untersuchung': 'inquiry',
 'die Disziplin, das Fachgebiet': 'discipline',
 'dominant': 'dominant',
 'kurz': 'briefly',
 'ausschließlich': 'solely',
 'nachverfolgen': 'trace',
 'die Ethik': 'ethics',
 'das Szenario': 'scenario',
 'jeweilig': 'respective',
 'teilweise': 'partially',
 'auflösen, lösen': 'resolve',
 'die Vorstellung, der Begriff': 'notion',
 'zugrunde liegend': 'underlying',
 'die Beobachtung': 'observation',
 'anwendbar': 'applicable',
 'linear': 'linear',
 'die Kontrollgruppe': 'control group',
 'ausgleichen': 'compensate for',
 'zusammengenommen': 'taken together',
 'die Fehlertoleranz, die Fehlermarge': 'margin of error',
 'das Forschungsdesign': 'research design',
 'in Bezug auf': 'with respect to',
 'auf der Grundlage von': 'on the basis of',
 'daraus folgt, dass': 'it follows that',
 'qualitative Daten (Pl.)': 'qualitative data',
 'in diesem Sinne': 'in the same vein',
 'das konzeptionelle Modell': 'conceptual model',
 'das Ethikvotum': 'ethical approval',
 'die informierte Einwilligung': 'informed consent',
 'die Literaturübersicht': 'literature review',
 'quantitative Daten (Pl.)': 'quantitative data',
 'die Methodik': 'methodology',
 'die Validität, die Gültigkeit': 'validity',
 'die Reliabilität, die Zuverlässigkeit': 'reliability',
 'die Verzerrung': 'bias',
 'die Fachliteratur': 'literature',
 'der Befund, das Ergebnis': 'finding',
 'die Verteilung': 'distribution',
 'zuschreiben': 'attribute',
 'darstellen, bilden': 'constitute',
 'erleichtern': 'facilitate',
 'erzeugen': 'generate',
 'durchführen': 'undertake',
 'begründen': 'justify',
 'umfassend': 'comprehensive',
 'vorläufig': 'preliminary',
 'qualitativ': 'qualitative',
 'quantitativ': 'quantitative',
 'beziehungsweise, jeweils': 'respectively',
 'in hohem Maße': 'to a large extent',
 'das Abstract': 'abstract',
 'der Anhang': 'appendix',
 'das Zitat': 'citation',
 'die Kohärenz': 'coherence',
 'die Gleichung': 'equation',
 'die Interpretation': 'interpretation',
 'der Mechanismus': 'mechanism',
 'der Ausreißer': 'outlier',
 'das Peer-Review': 'peer review',
 'die Signifikanz': 'significance',
 'der Betreuer': 'supervisor',
 'zuweisen': 'allocate',
 'zusammenstellen': 'compile',
 'bestätigen': 'confirm',
 'unterscheiden': 'differentiate',
 'ausschließen': 'exclude',
 'umsetzen': 'implement',
 'folgern': 'infer',
 'modifizieren': 'modify',
 'validieren': 'validate',
 'zugänglich': 'accessible',
 'statistisch': 'statistical',
 'gültig, valide': 'valid',
 'theoretisch': 'theoretical',
 'ungefähr': 'approximately',
 'anschließend': 'subsequently',
 'entsprechend': 'correspondingly',
 'umwandeln': 'convert',
 'generisch, allgemein': 'generic',
 'veröffentlichen': 'publish',
 'die Dynamik': 'dynamics',
 'vergleichbar': 'comparable',
 'beobachten': 'observe',
 'erkennen, nachweisen': 'detect',
 'der Graph, die Grafik': 'graph',
 'der Median': 'median',
 'die These; die Abschlussarbeit': 'thesis',
 'der Schwellenwert': 'threshold',
 'unterbringen, berücksichtigen': 'accommodate',
 'extrahieren': 'extract',
 'die Achse': 'axis',
 'nämlich': 'namely',
 'die Anpassung': 'adaptation',
 'abwägen': 'weigh',
 'die Konfiguration': 'configuration',
 'die Tendenz': 'tendency',
 'integral, wesentlich': 'integral',
 'ausdrücklich': 'explicitly',
 'aggregieren, zusammenfassen': 'aggregate',
 'lokalisieren': 'locate',
 'optimal': 'optimal',
 'übersetzen': 'translate',
 'die Norm': 'norm',
 'die Illustration': 'illustration',
 'das Manuskript': 'manuscript',
 'hervorgehen, auftauchen': 'emerge',
 'das Modul': 'module',
 'verifizieren': 'verify',
 'die Glaubwürdigkeit': 'credibility',
 'begutachtet (peer-reviewed)': 'peer-reviewed',
 'berechnen': 'calculate',
 'regulieren': 'regulate',
 'systematisch': 'systematic',
 'die Forschungsfrage': 'research question',
 'der Forschungsstand': 'body of literature',
 'die empirische Evidenz': 'empirical evidence',
 'das Signifikanzniveau': 'significance level',
 'die Standardabweichung': 'standard deviation',
 'in Übereinstimmung mit': 'in accordance with',
 'wie in Tabelle 2 ersichtlich': 'as shown in Table 2',
 'inwieweit': 'the extent to which',
 'die Nullhypothese': 'the null hypothesis',
 'in der vorliegenden Studie': 'in the present study',
 'wir haben die Hypothese aufgestellt, dass': 'we hypothesised that',
 'die Störvariable': 'confounding variable',
 'der theoretische Rahmen': 'theoretical framework',
 'in dieser Arbeit wird argumentiert, dass': 'this paper argues that',
 'die Daten zeigen, dass': 'the data indicate that',
 'das Paradigma': 'paradigm',
 'die Begründung': 'rationale',
 'der Diskurs': 'discourse',
 'die Diskrepanz': 'discrepancy',
 'die Machbarkeit': 'feasibility',
 'die Prämisse': 'premise',
 'synthetisieren': 'synthesise',
 'postulieren': 'postulate',
 'erläutern': 'elucidate',
 'abgrenzen, umreißen': 'delineate',
 'mindern, abschwächen': 'mitigate',
 'inhärent': 'inherent',
 'robust': 'robust',
 'hervorstechend': 'salient',
 'mehrdeutig': 'ambiguous',
 'umgekehrt': 'conversely',
 'die Anomalie': 'anomaly',
 'die Kausalität': 'causality',
 'die Verallgemeinerbarkeit': 'generalisability',
 'die Umsetzung': 'implementation',
 'der Parameter': 'parameter',
 'die Strenge': 'rigour',
 'die Taxonomie': 'taxonomy',
 'befürworten': 'advocate',
 'kalibrieren': 'calibrate',
 'umfassen': 'encompass',
 'formulieren': 'formulate',
 'kohärent': 'coherent',
 'intrinsisch': 'intrinsic',
 'marginal': 'marginal',
 'plausibel': 'plausible',
 'dadurch': 'thereby',
 'wodurch': 'whereby',
 'nichtsdestotrotz': 'nonetheless',
 'das Diagramm': 'diagram',
 'willkürlich': 'arbitrary',
 'die Synthese': 'synthesis',
 'kritisch bewerten': 'critique',
 'der Prototyp': 'prototype',
 'diagnostisch': 'diagnostic',
 'das Literaturverzeichnis': 'bibliography',
 'im Großen und Ganzen': 'broadly',
 'alternativ': 'alternatively',
 'subjektiv': 'subjective',
 'die Hierarchie': 'hierarchy',
 'das Intervall': 'interval',
 'zusammenführen': 'merge',
 'endlich': 'finite',
 'die Zuweisung': 'allocation',
 'vorhergehend': 'preceding',
 'analytisch': 'analytical',
 'wahrnehmen': 'perceive',
 'die Probe': 'specimen',
 'die Analogie': 'analogy',
 'die Dissertation': 'dissertation',
 'sich manifestieren': 'manifest',
 'die Terminologie': 'terminology',
 'übertragen': 'transmit',
 'annähern, näherungsweise berechnen': 'approximate',
 'prüfen, inspizieren': 'inspect',
 'überdenken': 'reconsider',
 'reproduzieren': 'reproduce',
 'der Praktiker': 'practitioner',
 'behaupten, geltend machen': 'assert',
 'vermuten': 'presume',
 'konzeptionell': 'conceptual',
 'hypothetisch': 'hypothetical',
 'in Anlehnung an die Arbeit von': 'drawing on the work of',
 'frühere Forschung legt nahe': 'prior research suggests',
 'es ist darauf hinzuweisen, dass': 'it should be noted that',
 'dies steht im Einklang mit': 'this is consistent with',
 'der Rahmen dieser Arbeit': 'the scope of this paper',
 'entgegen den Erwartungen': 'contrary to expectations',
 'soweit die Daten es zulassen': 'insofar as the data allow',
 'statistisch signifikant': 'statistically significant',
 'es ist allgemein anerkannt, dass': 'it is widely accepted that',
 'weitere Forschung ist erforderlich': 'further research is needed',
 'wie in Abbildung 1 dargestellt': 'as illustrated in Figure 1',
 'angesichts dieser Befunde': 'in light of these findings',
 'künftige Arbeiten sollten … behandeln': 'future work should address',
 'Ziel dieser Studie ist es, …': 'the aim of this study is to',
 'diese Befunde legen nahe, dass': 'these findings suggest that',
 'der Vorbehalt': 'caveat',
 'die Nuance': 'nuance',
 'der Verlauf': 'trajectory',
 'die Dichotomie': 'dichotomy',
 'der Konsens': 'consensus',
 'die Heuristik': 'heuristic',
 'untermauern': 'underpin',
 'in Einklang bringen': 'reconcile',
 'extrapolieren': 'extrapolate',
 'operationalisieren': 'operationalise',
 'genau prüfen': 'scrutinise',
 'widerlegen': 'refute',
 'rechtfertigen': 'warrant',
 'einschlägig, sachdienlich': 'pertinent',
 'dürftig, schwach': 'tenuous',
 'zentral, ausschlaggebend': 'pivotal',
 'streng, rigoros': 'rigorous',
 'angeblich, vordergründig': 'ostensibly',
 'unter anderem': 'inter alia',
 'wenn auch': 'albeit',
 'der Vorläufer': 'antecedent',
 'die Vermutung': 'conjecture',
 'das Korpus': 'corpus',
 'das Gegenargument': 'counterargument',
 'die Darlegung': 'exposition',
 'das Paradoxon': 'paradox',
 'der Präzedenzfall': 'precedent',
 'die Proxy-Variable': 'proxy',
 'sich halten an': 'adhere to',
 'anspielen auf': 'allude to',
 'artikulieren': 'articulate',
 'festigen': 'consolidate',
 'gipfeln': 'culminate',
 'verbreiten': 'disseminate',
 'voraussetzen': 'presuppose',
 'festlegen': 'stipulate',
 'abhängig': 'contingent',
 'diskret': 'discrete',
 'implizit': 'implicit',
 'bahnbrechend': 'seminal',
 'beispiellos': 'unprecedented',
 'insofern als': 'insofar as',
 'ungeachtet': 'notwithstanding',
 'in dieser Hinsicht': 'in this regard',
 'im weiteren Sinne': 'by extension',
 'isolieren': 'isolate',
 'das Gleichgewicht': 'equilibrium',
 'beginnen': 'commence',
 'naturgemäß': 'inherently',
 'indikativ, hinweisend': 'indicative',
 'ergänzend, komplementär': 'complementary',
 'fragmentieren': 'fragment',
 'replizieren': 'replicate',
 'kumulativ': 'cumulative',
 'deskriptiv': 'descriptive',
 'entsprechen, sich anpassen': 'conform',
 'die Abhängigkeit': 'dependency',
 'der Auszug': 'excerpt',
 'vergleichsweise': 'comparatively',
 'organisieren': 'organise',
 'provozieren, auslösen': 'provoke',
 'korreliert': 'correlated',
 'zusammenfallen': 'coincide',
 'gleichzeitig': 'concurrent',
 'spekulieren': 'speculate',
 'die Deduktion': 'deduction',
 'die Varianz': 'variance',
 'simulieren': 'simulate',
 'das Kontinuum': 'continuum',
 'die Replikation': 'replication',
 'die Kohorte': 'cohort',
 'die Abweichung': 'deviation',
 'klassifizieren': 'classify',
 'der Koeffizient': 'coefficient',
 'interdisziplinär': 'interdisciplinary',
 'entstammen': 'originate',
 'longitudinal': 'longitudinal',
 'prädiktiv': 'predictive',
 'einseitig': 'unilateral',
 'kausal': 'causal',
 'die Danksagung; die Anerkennung': 'acknowledgement',
 'dies wirft die Frage auf': 'this raises the question of',
 'ein erheblicher Anteil von': 'a substantial proportion of',
 'die vorliegenden Befunde erweitern': 'the present findings extend',
 'nach unserem besten Wissen': 'to the best of our knowledge',
 'die zugrunde liegende Annahme ist': 'the underlying assumption is',
 'eine mögliche Erklärung ist, dass': 'a possible explanation is that',
 'über den Rahmen dieser Studie hinaus': 'beyond the scope of this study',
 'für die Zwecke dieser Studie': 'for the purposes of this study',
 'mehrere Studien haben gezeigt': 'a number of studies have shown',
 'eine Limitation dieser Studie ist': 'one limitation of this study is',
 'die Ergebnisse stimmen überein mit': 'the results are consistent with',
 'im Gegensatz zu früheren Befunden': 'in contrast to previous findings',
 '… wurde bisher wenig beachtet': 'little attention has been paid to',
 'es gibt zunehmend Belege': 'there is a growing body of evidence',
 'die Erkenntnistheorie': 'epistemology',
 'die Ontologie': 'ontology',
 'die Hegemonie': 'hegemony',
 'die Tautologie': 'tautology',
 'die logische Folge': 'corollary',
 'problematisieren': 'problematise',
 'kontextualisieren': 'contextualise',
 'hervorrufen': 'engender',
 'verschleiern': 'obfuscate',
 'eigentümlich, idiosynkratisch': 'idiosyncratic',
 'reduktionistisch': 'reductive',
 'allgegenwärtig': 'ubiquitous',
 'selbstverständlich, axiomatisch': 'axiomatic',
 'stillschweigend': 'tacit',
 'erst recht': 'a fortiori',
 'eo ipso, eben dadurch': 'ipso facto',
 'sinngemäß': 'mutatis mutandis',
 'die Aporie': 'aporia',
 'die Dialektik': 'dialectic',
 'die Exegese': 'exegesis',
 'die Geschichtsschreibung': 'historiography',
 'die Ideologie': 'ideology',
 'der Positivismus': 'positivism',
 'der Relativismus': 'relativism',
 'die Subjektivität': 'subjectivity',
 'der Syllogismus': 'syllogism',
 'urteilen': 'adjudicate',
 'eingrenzen': 'circumscribe',
 'dekonstruieren': 'deconstruct',
 'verkörpern': 'epitomise',
 'explizieren': 'explicate',
 'marginalisieren': 'marginalise',
 'bevorzugen': 'privilege',
 'theoretisieren': 'theorise',
 'kanonisch': 'canonical',
 'dialektisch': 'dialectical',
 'normativ': 'normative',
 'paradigmatisch': 'paradigmatic',
 'nachträglich': 'post hoc',
 'im engeren Sinne': 'sensu stricto',
 'gegenüber': 'vis-à-vis',
 'die Annäherung': 'approximation',
 'beleuchten': 'illuminate',
 'schlüssig': 'conclusive',
 'erschöpfend': 'exhaustive',
 'sequenziell': 'sequential',
 'deutlich': 'markedly',
 'hierarchisch': 'hierarchical',
 'die Richtlinie': 'guideline',
 'der Unterabschnitt': 'subsection',
 'anprangern': 'denounce',
 'konvergieren, zusammenlaufen': 'converge',
 'das Plagiat': 'plagiarism',
 'korrelieren': 'correlate',
 'gleichsetzen': 'equate',
 'erweitern, ergänzen': 'augment',
 'explorativ': 'exploratory',
 'die Fußnote': 'footnote',
 'verstärken': 'amplify',
 'der Befürworter': 'proponent',
 'bislang': 'hitherto',
 'behindern': 'impede',
 'kontextuell': 'contextual',
 'vermitteln': 'mediate',
 'wiederholen, bekräftigen': 'reiterate',
 'das Schema': 'schema',
 'nicht schlüssig': 'inconclusive',
 'der Prädiktor': 'predictor',
 'hervorlocken, ermitteln': 'elicit',
 'der Befragte': 'respondent',
 'automatisieren': 'automate',
 'verzerren': 'distort',
 'auslassen': 'omit',
 'paraphrasieren': 'paraphrase',
 'vereinheitlichen': 'unify',
 'abweichen': 'deviate',
 'erbitten, einholen': 'solicit',
 'die Herleitung': 'derivation',
 'methodisch': 'methodological',
 'entkräften, ungültig machen': 'invalidate',
 'die Heterogenität': 'heterogeneity',
 'die Verdinglichung': 'reification',
 'die Teleologie': 'teleology',
 'die Hermeneutik': 'hermeneutics',
 'die Wahrscheinlichkeit, die Glaubwürdigkeit': 'verisimilitude',
 'die Praxis': 'praxis',
 'instanziieren, konkretisieren': 'instantiate',
 'aufwerten': 'valorise',
 'kritisch hinterfragen': 'interrogate',
 'in den Vordergrund stellen': 'foreground',
 'vermengen': 'conflate',
 'abstrus, schwer verständlich': 'recondite',
 'entstehend, aufkommend': 'nascent',
 'polemisch': 'polemical',
 'auf den ersten Blick': 'prima facie',
 'unter sonst gleichen Bedingungen': 'ceteris paribus',
 'die Alterität': 'alterity',
 'die Episteme': 'episteme',
 'der Habitus': 'habitus',
 'die Intertextualität': 'intertextuality',
 'die Liminalität': 'liminality',
 'die Performativität': 'performativity',
 'die Positionalität': 'positionality',
 'die Reflexivität': 'reflexivity',
 'aufheben': 'abrogate',
 'dulden, gutheißen': 'countenance',
 'essentialisieren': 'essentialise',
 'verdecken': 'occlude',
 'verdinglichen': 'reify',
 'subsumieren': 'subsume',
 'aporetisch': 'aporetic',
 'apodiktisch': 'apodictic',
 'hegemonial': 'hegemonic',
 'liminal': 'liminal',
 'rekursiv': 'recursive',
 'synkretistisch': 'syncretic',
 'bei allem Respekt vor': 'pace',
 'sic': 'sic',
 'unterstreichen': 'underscore',
 'beschränken': 'confine',
 'fälschen; herstellen': 'fabricate',
 'die Anmerkung': 'annotation',
 'annullieren': 'nullify',
 'erzählen': 'narrate',
 'authentifizieren, beglaubigen': 'authenticate',
 'transkribieren': 'transcribe',
 'ablösen, ersetzen': 'supersede',
 'wiederkehren': 'recur',
 'anhängen': 'append',
 'charakterisieren': 'characterise',
 'vorgeben, angeblich sein': 'purport',
 'optimieren': 'optimise',
 'ausführlich darlegen': 'expound',
 'neu formulieren': 'restate',
 'die Verallgemeinerung': 'generalisation',
 'zusammentragen, abgleichen': 'collate',
 'verorten': 'situate',
 'aufzählen': 'enumerate',
 'rationalisieren': 'rationalise',
 'auslegen, deuten': 'construe',
 'normalisieren': 'normalise',
 'annotieren, kommentieren': 'annotate',
 'verallgemeinern': 'generalise',
 'tabellarisch darstellen': 'tabulate',
 'rekapitulieren': 'recapitulate',
 'konzeptualisieren': 'conceptualise',
 'Hypothesen aufstellen': 'hypothesise',
 'randomisieren': 'randomise'}

DE_EN_CYBER = {'der Vermögenswert, das Asset': 'asset',
 'die Bedrohung': 'threat',
 'der Bedrohungsakteur': 'threat actor',
 'die Schwachstelle': 'vulnerability',
 'der Exploit; ausnutzen': 'exploit',
 'das Risiko': 'risk',
 'die Eintrittswahrscheinlichkeit': 'likelihood',
 'die Auswirkung': 'impact',
 'die Angriffsfläche': 'attack surface',
 'der Angriffsvektor': 'attack vector',
 'der Schadensradius': 'blast radius',
 'die Vertraulichkeit': 'confidentiality',
 'die Integrität': 'integrity',
 'die Verfügbarkeit': 'availability',
 'die Nichtabstreitbarkeit': 'non-repudiation',
 'die Authentifizierung': 'authentication',
 'die Autorisierung': 'authorisation',
 'die Protokollierung (Accounting)': 'accounting',
 'das Prinzip der geringsten Rechte': 'least privilege',
 'die gestaffelte Verteidigung (Defense in Depth)': 'defence in depth',
 'Zero Trust': 'zero trust',
 'die Sicherheitslage': 'security posture',
 'die Baseline, die Referenzkonfiguration': 'baseline',
 'die Härtung': 'hardening',
 'der Patch': 'patch',
 'das Patch-Management': 'patch management',
 'die Gegenmaßnahme': 'countermeasure',
 'die Schutzmaßnahme': 'safeguard',
 'die Kontrolle, die Sicherheitsmaßnahme': 'control',
 'die kompensierende Kontrolle': 'compensating control',
 'die Risikominderung': 'mitigation',
 'die Behebung': 'remediation',
 'das Restrisiko': 'residual risk',
 'das False Positive, der Fehlalarm': 'false positive',
 'das False Negative': 'false negative',
 'das True Positive': 'true positive',
 'die Erkennung': 'detection',
 'die Prävention': 'prevention',
 'die Reaktion': 'response',
 'die Wiederherstellung': 'recovery',
 'die Resilienz': 'resilience',
 'die Redundanz': 'redundancy',
 'das Failover': 'failover',
 'die Geschäftskontinuität': 'business continuity',
 'die Notfallwiederherstellung (Disaster Recovery)': 'disaster recovery',
 'der Single Point of Failure': 'single point of failure',
 'Security by Design': 'security by design',
 'ausfallsicher (fail secure)': 'fail secure',
 'die Vertrauensgrenze': 'trust boundary',
 'die Bedrohungslage': 'threat landscape',
 'das Risiko bewerten': 'assess the risk',
 'das Risiko mindern': 'mitigate the risk',
 'den Vorfall eskalieren': 'escalate the incident',
 'die Bedrohung eindämmen': 'contain the threat',
 'den Befund beheben': 'remediate the finding',
 'das System härten': 'harden the system',
 'die Schwachstelle patchen': 'patch the vulnerability',
 'die Richtlinie durchsetzen': 'enforce the policy',
 'die Korrektur verifizieren': 'validate the fix',
 'das Problem reproduzieren': 'reproduce the issue',
 'die Schritte dokumentieren': 'document the steps',
 'ein Ticket erstellen': 'raise a ticket',
 'ein Bedenken melden': 'flag a concern',
 'den Bericht durchgehen': 'walk through the report',
 'nachfassen bei': 'follow up on',
 'das Team einbeziehen': 'loop in the team',
 'sich mit den Stakeholdern abstimmen': 'align with stakeholders',
 'Befunde priorisieren': 'prioritise findings',
 'den Auftragsumfang festlegen': 'scope the engagement',
 'freigeben, abzeichnen': 'sign off on',
 'ausrollen': 'roll out',
 'zurückrollen': 'roll back',
 'außer Betrieb nehmen': 'decommission',
 'eine IP auf die Allowlist setzen': 'whitelist an IP',
 'den Zugriff entziehen': 'revoke access',
 'Zugriff gewähren': 'grant access',
 'Zugangsdaten rotieren': 'rotate credentials',
 'die Protokollierung aktivieren': 'enable logging',
 'auf Anomalien überwachen': 'monitor for anomalies',
 'Ereignisse korrelieren': 'correlate events',
 'den Alarm verifizieren': 'verify the alert',
 'als Fehlalarm schließen': 'dismiss as false positive',
 'eine Überprüfung durchführen': 'conduct a review',
 'die Befunde präsentieren': 'present the findings',
 'das Budget begründen': 'justify the budget',
 'gemäß unserer Richtlinie': 'as per our policy',
 'im Einklang mit Best Practices': 'in line with best practice',
 'vorbehaltlich der Genehmigung': 'subject to approval',
 'bis zur weiteren Untersuchung': 'pending further investigation',
 'mit sofortiger Wirkung': 'with immediate effect',
 'das Paket': 'packet',
 'die Nutzlast, der Payload': 'payload',
 'der Header': 'header',
 'der Frame': 'frame',
 'das Protokoll': 'protocol',
 'der Port': 'port',
 'der Socket': 'socket',
 'der Handshake': 'handshake',
 'der Drei-Wege-Handshake': 'three-way handshake',
 'das Subnetz': 'subnet',
 'das Gateway': 'gateway',
 'der Router': 'router',
 'der Switch': 'switch',
 'die Firewall': 'firewall',
 'die Next-Generation-Firewall': 'next-generation firewall',
 'die Stateful Inspection': 'stateful inspection',
 'die Zugriffskontrollliste (ACL)': 'access control list (ACL)',
 'NAT (Netzwerkadressübersetzung)': 'NAT',
 'das VLAN': 'VLAN',
 'die Netzwerksegmentierung': 'network segmentation',
 'die Mikrosegmentierung': 'micro-segmentation',
 'die DMZ': 'DMZ',
 'der Proxy': 'proxy',
 'der Reverse Proxy': 'reverse proxy',
 'der Load Balancer, der Lastverteiler': 'load balancer',
 'das VPN': 'VPN',
 'das Tunneling': 'tunnelling',
 'die Portweiterleitung': 'port forwarding',
 'das Pivoting': 'pivoting',
 'der Paketmitschnitt': 'packet capture',
 'das Sniffing': 'sniffing',
 'die Verkehrsanalyse': 'traffic analysis',
 'die Bandbreite': 'bandwidth',
 'die Latenz': 'latency',
 'der Durchsatz': 'throughput',
 'der Broadcast': 'broadcast',
 'die Routingtabelle': 'routing table',
 'die DNS-Auflösung': 'DNS resolution',
 'die DHCP-Lease': 'DHCP lease',
 'TLS': 'TLS',
 'mutual TLS (mTLS)': 'mutual TLS',
 'das Certificate Pinning': 'certificate pinning',
 'der WLAN-Zugangspunkt': 'wireless access point',
 'der Rogue Access Point': 'rogue access point',
 'der Evil Twin': 'evil twin',
 'der Deauthentication-Angriff': 'deauthentication attack',
 'WPA2 / WPA3': 'WPA2 / WPA3',
 'die Egress-Filterung': 'egress filtering',
 'die Ingress-Filterung': 'ingress filtering',
 'der Netzwerk-TAP': 'network tap',
 'der Kernel': 'kernel',
 'der Prozess': 'process',
 'der Daemon, der Dienst': 'daemon',
 'der Dienst': 'service',
 'die Shell': 'shell',
 'das Recht, die Berechtigung': 'privilege',
 'root': 'root',
 'sudo': 'sudo',
 'die Dateiberechtigung': 'file permission',
 'das Setuid-Binary': 'setuid binary',
 'der Cronjob': 'cron job',
 'die systemd-Unit': 'systemd unit',
 'die Logdatei': 'log file',
 'Syslog': 'syslog',
 'der Prüfpfad, der Audit-Trail': 'audit trail',
 'die Registry': 'registry',
 'Active Directory': 'Active Directory',
 'der Domänencontroller': 'domain controller',
 'die Gruppenrichtlinie': 'group policy',
 'das Dienstkonto': 'service account',
 'das Golden Ticket': 'golden ticket',
 'der Hash': 'hash',
 'Pass-the-Hash': 'pass-the-hash',
 'der LSASS-Dump': 'LSASS dump',
 'der Speicherabzug': 'memory dump',
 'der Snapshot': 'snapshot',
 'die virtuelle Maschine': 'virtual machine',
 'der Hypervisor': 'hypervisor',
 'der Container': 'container',
 'das Image': 'image',
 'die Sandbox': 'sandbox',
 'der Ausbruch (Sandbox/Container)': 'escape (sandbox/container)',
 'der Endpunkt': 'endpoint',
 'der Agent': 'agent',
 'das Inventar': 'inventory',
 'das Asset-Management': 'asset management',
 'die Konfigurationsabweichung': 'configuration drift',
 'das Golden Image': 'golden image',
 'die Schadsoftware, die Malware': 'malware',
 'die Ransomware, die Erpressersoftware': 'ransomware',
 'die Spyware': 'spyware',
 'die Adware': 'adware',
 'das Rootkit': 'rootkit',
 'das Bootkit': 'bootkit',
 'der Trojaner': 'trojan',
 'der Wurm': 'worm',
 'der Virus': 'virus',
 'der Dropper': 'dropper',
 'der Loader': 'loader',
 'der Wiper': 'wiper',
 'der Keylogger': 'keylogger',
 'das Botnetz': 'botnet',
 'Command and Control (C2)': 'command and control (C2)',
 'der Beacon': 'beacon',
 'die Hintertür': 'backdoor',
 'die logische Bombe': 'logic bomb',
 'das Phishing': 'phishing',
 'das Spear-Phishing': 'spear phishing',
 'das Whaling': 'whaling',
 'das Smishing': 'smishing',
 'das Vishing': 'vishing',
 'das Pretexting': 'pretexting',
 'das Baiting, der Köder': 'baiting',
 'das Tailgating': 'tailgating',
 'das Social Engineering': 'social engineering',
 'der CEO-Betrug (Business Email Compromise)': 'business email compromise',
 'der Diebstahl von Zugangsdaten': 'credential theft',
 'das Credential Stuffing': 'credential stuffing',
 'das Password Spraying': 'password spraying',
 'der Brute-Force-Angriff': 'brute force',
 'der Wörterbuchangriff': 'dictionary attack',
 'die Rainbow Table': 'rainbow table',
 'der Man-in-the-Middle-Angriff': 'man-in-the-middle (MitM)',
 'der Replay-Angriff': 'replay attack',
 'das Session Hijacking': 'session hijacking',
 'das Spoofing': 'spoofing',
 'das ARP-Spoofing': 'ARP poisoning',
 'das DNS-Poisoning': 'DNS poisoning',
 'das DNS-Tunneling': 'DNS tunnelling',
 'das Typosquatting': 'typosquatting',
 'der Watering-Hole-Angriff': 'watering hole attack',
 'der Lieferkettenangriff': 'supply chain attack',
 'der Denial-of-Service-Angriff (DoS)': 'denial of service (DoS)',
 'der DDoS-Angriff': 'DDoS',
 'der Amplification-Angriff': 'amplification attack',
 'die Zero-Day-Lücke': 'zero-day',
 'die Rechteausweitung': 'privilege escalation',
 'die laterale Bewegung': 'lateral movement',
 'die Persistenz': 'persistence',
 'die Datenexfiltration': 'data exfiltration',
 'die Datenpanne': 'data breach',
 'der Innentäter': 'insider threat',
 'die APT (fortgeschrittene, andauernde Bedrohung)': 'advanced persistent threat (APT)',
 'Living off the Land': 'living off the land',
 'die dateilose Malware': 'fileless malware',
 'die Verschleierung': 'obfuscation',
 'das Packing': 'packing',
 'polymorph': 'polymorphic',
 'die Umgehung': 'evasion',
 'Anti-Forensik': 'anti-forensics',
 'das Cryptojacking': 'cryptojacking',
 'die Scareware': 'scareware',
 'die doppelte Erpressung': 'double extortion',
 'der Erstzugriff': 'initial access',
 'die Verweildauer': 'dwell time',
 'die Kill Chain': 'kill chain',
 'die Injection': 'injection',
 'die SQL-Injection': 'SQL injection',
 'die Command Injection': 'command injection',
 'Cross-Site-Scripting (XSS)': 'cross-site scripting (XSS)',
 'Stored XSS': 'stored XSS',
 'Reflected XSS': 'reflected XSS',
 'Cross-Site Request Forgery (CSRF)': 'cross-site request forgery (CSRF)',
 'Server-Side Request Forgery (SSRF)': 'server-side request forgery (SSRF)',
 'die unsichere Deserialisierung': 'insecure deserialisation',
 'die Path Traversal': 'path traversal',
 'die Local File Inclusion': 'local file inclusion',
 'die Remote Code Execution (RCE)': 'remote code execution (RCE)',
 'die offene Weiterleitung': 'open redirect',
 'das Clickjacking': 'clickjacking',
 'die fehlerhafte Zugriffskontrolle': 'broken access control',
 'IDOR (unsichere direkte Objektreferenz)': 'insecure direct object reference (IDOR)',
 'der Logikfehler': 'business logic flaw',
 'die Race Condition': 'race condition',
 'der Pufferüberlauf': 'buffer overflow',
 'der Heap-Überlauf': 'heap overflow',
 'der Stack-Überlauf': 'stack overflow',
 'Use-after-free': 'use-after-free',
 'die Eingabevalidierung': 'input validation',
 'die Ausgabekodierung': 'output encoding',
 'die Bereinigung': 'sanitisation',
 'die parametrisierte Abfrage': 'parameterised query',
 'das Prepared Statement': 'prepared statement',
 'die Content Security Policy (CSP)': 'content security policy (CSP)',
 'die Same-Origin-Policy': 'same-origin policy',
 'CORS': 'CORS',
 'der Sicherheitsheader': 'security header',
 'die Ratenbegrenzung': 'rate limiting',
 'die Web Application Firewall (WAF)': 'web application firewall (WAF)',
 'das API-Gateway': 'API gateway',
 'das Token': 'token',
 'das Session-Cookie': 'session cookie',
 'das Secure-Flag': 'secure flag',
 'HttpOnly': 'HttpOnly',
 'das CAPTCHA': 'CAPTCHA',
 'die Abhängigkeit': 'dependency',
 'die Software-Stückliste (SBOM)': 'software bill of materials (SBOM)',
 'sicheres Programmieren': 'secure coding',
 'das Code-Review': 'code review',
 'die statische Codeanalyse (SAST)': 'static analysis (SAST)',
 'die dynamische Analyse (DAST)': 'dynamic analysis (DAST)',
 'das Fuzzing': 'fuzzing',
 'das Secrets-Management': 'secrets management',
 'fest codierte Zugangsdaten': 'hardcoded credentials',
 'die Verschlüsselung': 'encryption',
 'die Entschlüsselung': 'decryption',
 'der Klartext': 'plaintext',
 'der Geheimtext, der Chiffretext': 'ciphertext',
 'die Chiffre': 'cipher',
 'die symmetrische Verschlüsselung': 'symmetric encryption',
 'die asymmetrische Verschlüsselung': 'asymmetric encryption',
 'der öffentliche Schlüssel': 'public key',
 'der private Schlüssel': 'private key',
 'der Schlüsselaustausch': 'key exchange',
 'die Schlüsselrotation': 'key rotation',
 'das Schlüsselmanagement': 'key management',
 'das Hashing': 'hashing',
 'der Salt': 'salt',
 'der Pepper': 'pepper',
 'die digitale Signatur': 'digital signature',
 'das Zertifikat': 'certificate',
 'die Zertifizierungsstelle (CA)': 'certificate authority (CA)',
 'die Public-Key-Infrastruktur (PKI)': 'public key infrastructure (PKI)',
 'das selbstsignierte Zertifikat': 'self-signed certificate',
 'der Widerruf': 'revocation',
 'die Entropie': 'entropy',
 'die Nonce': 'nonce',
 'der Initialisierungsvektor': 'initialisation vector',
 'die Ende-zu-Ende-Verschlüsselung': 'end-to-end encryption',
 'die Verschlüsselung ruhender Daten': 'encryption at rest',
 'die Transportverschlüsselung': 'encryption in transit',
 'das Hardware-Sicherheitsmodul (HSM)': 'hardware security module (HSM)',
 'der Identitätsanbieter (IdP)': 'identity provider (IdP)',
 'Single Sign-on (SSO)': 'single sign-on (SSO)',
 'die Föderation': 'federation',
 'SAML': 'SAML',
 'OAuth': 'OAuth',
 'OpenID Connect': 'OpenID Connect',
 'die Multi-Faktor-Authentifizierung (MFA)': 'multi-factor authentication (MFA)',
 'das Einmalpasswort (OTP)': 'one-time password (OTP)',
 'der Passkey': 'passkey',
 'biometrisch': 'biometric',
 'die rollenbasierte Zugriffskontrolle (RBAC)': 'role-based access control (RBAC)',
 'die attributbasierte Zugriffskontrolle': 'attribute-based access control',
 'das Privileged Access Management (PAM)': 'privileged access management (PAM)',
 'der Just-in-Time-Zugriff': 'just-in-time access',
 'der Identitätslebenszyklus': 'identity lifecycle',
 'die Bereitstellung (Provisioning)': 'provisioning',
 'die Deprovisionierung': 'deprovisioning',
 'die Zugriffsprüfung': 'access review',
 'die Funktionstrennung': 'segregation of duties',
 'der Penetrationstest': 'penetration test',
 'das Red Team': 'red team',
 'das Blue Team': 'blue team',
 'das Purple Team': 'purple team',
 'der Auftrag, das Projekt': 'engagement',
 'die Rules of Engagement': 'rules of engagement',
 'der Umfang, der Scope': 'scope',
 'im Scope / außerhalb des Scopes': 'in scope / out of scope',
 'das Autorisierungsschreiben': 'authorisation letter',
 'die Freistellungserklärung': 'get-out-of-jail letter',
 'der Blackbox-Test': 'black box',
 'der Whitebox-Test': 'white box',
 'der Greybox-Test': 'grey box',
 'die Aufklärung': 'reconnaissance',
 'OSINT': 'OSINT',
 'das Footprinting': 'footprinting',
 'die Enumeration': 'enumeration',
 'das Scannen': 'scanning',
 'der Portscan': 'port scan',
 'die Diensterkennung': 'service detection',
 'das Banner Grabbing': 'banner grabbing',
 'der Schwachstellenscan': 'vulnerability scanning',
 'der Proof of Concept (PoC)': 'proof of concept (PoC)',
 'die Payload-Auslieferung': 'payload delivery',
 'der Shellcode': 'shellcode',
 'die Reverse Shell': 'reverse shell',
 'die Bind Shell': 'bind shell',
 'der Brückenkopf, der Foothold': 'foothold',
 'pivotieren': 'pivot',
 'die Post-Exploitation': 'post-exploitation',
 'das Sammeln von Zugangsdaten': 'credential harvesting',
 'das Knacken von Passwörtern': 'password cracking',
 'die Rechte-Enumeration': 'privilege enumeration',
 'der Persistenzmechanismus': 'persistence mechanism',
 'die Nachbesprechung': 'debrief',
 'der Befund': 'finding',
 'der Schweregrad': 'severity',
 'der CVSS-Wert': 'CVSS score',
 'die Ausnutzbarkeit': 'exploitability',
 'die Behebungsempfehlung': 'remediation advice',
 'der Retest': 'retest',
 'die Management-Zusammenfassung': 'executive summary',
 'der technische Bericht': 'technical report',
 'das Bug-Bounty-Programm': 'bug bounty',
 'die verantwortungsvolle Offenlegung': 'responsible disclosure',
 'die koordinierte Offenlegung': 'coordinated disclosure',
 'die Angreiferemulation': 'adversary emulation',
 'TTPs (Taktiken, Techniken, Prozeduren)': 'TTPs',
 'MITRE ATT&CK': 'MITRE ATT&CK',
 'das Bedrohungsmodell': 'threat model',
 'der Angriffsbaum': 'attack tree',
 'das Security Operations Center (SOC)': 'security operations centre (SOC)',
 'der Analyst': 'analyst',
 'Level 1 / Level 2': 'tier 1 / tier 2',
 'der Alarm, die Warnung': 'alert',
 'die Alarmmüdigkeit': 'alert fatigue',
 'die Triage': 'triage',
 'die Eskalation': 'escalation',
 'der Sicherheitsvorfall': 'incident',
 'die Vorfallsreaktion (Incident Response)': 'incident response',
 'das Playbook': 'playbook',
 'das Runbook': 'runbook',
 'die Rufbereitschaft': 'on-call',
 'die Eindämmung': 'containment',
 'die Beseitigung': 'eradication',
 'die Lessons Learned': 'lessons learned',
 'die Nachanalyse (Post-Mortem)': 'post-mortem',
 'die Ursachenanalyse': 'root cause analysis',
 'SIEM': 'SIEM',
 'die Log-Aggregation': 'log aggregation',
 'die Korrelationsregel': 'correlation rule',
 'der Use Case': 'use case',
 'das Detection Engineering': 'detection engineering',
 'die Signatur': 'signature',
 'heuristisch': 'heuristic',
 'die Anomalieerkennung': 'anomaly detection',
 'die Verhaltensanalyse': 'behavioural analysis',
 'die Abweichung von der Baseline': 'baseline deviation',
 'EDR': 'EDR',
 'XDR': 'XDR',
 'IDS (Angriffserkennungssystem)': 'IDS',
 'IPS (Angriffsverhinderungssystem)': 'IPS',
 'der Honeypot': 'honeypot',
 'die Deception-Technologie': 'deception technology',
 'die Bedrohungsaufklärung (Threat Intelligence)': 'threat intelligence',
 'der Kompromittierungsindikator (IoC)': 'indicator of compromise (IoC)',
 'der Angriffsindikator (IoA)': 'indicator of attack (IoA)',
 'das Threat Hunting': 'threat hunting',
 'die hypothesengetriebene Jagd': 'hypothesis-driven hunt',
 'die digitale Forensik': 'digital forensics',
 'die Beweismittelkette': 'chain of custody',
 'die forensische Abbilderstellung': 'imaging',
 'der Schreibblocker': 'write blocker',
 'flüchtige Daten (Pl.)': 'volatile data',
 'die Zeitlinienanalyse': 'timeline analysis',
 'das Artefakt': 'artefact',
 'die Malware-Analyse': 'malware analysis',
 'die statische Analyse': 'static analysis',
 'das Reverse Engineering': 'reverse engineering',
 'die Sandbox-Detonation': 'sandbox detonation',
 'die YARA-Regel': 'YARA rule',
 'SOAR': 'SOAR',
 'die mittlere Erkennungszeit (MTTD)': 'mean time to detect (MTTD)',
 'die mittlere Reaktionszeit (MTTR)': 'mean time to respond (MTTR)',
 'der Fehlalarm': 'false alarm',
 'das Tuning, die Feinabstimmung': 'tuning',
 'das Whitelisting': 'whitelisting',
 'das Blocklisting': 'blocklisting',
 'die Quarantäne': 'quarantine',
 'die Isolierung': 'isolation',
 'der Notausschalter (Kill Switch)': 'kill switch',
 'die Governance': 'governance',
 'die Compliance, die Einhaltung': 'compliance',
 'die Regulierung': 'regulation',
 'der Standard': 'standard',
 'das Rahmenwerk': 'framework',
 'die Richtlinie': 'policy',
 'das Verfahren': 'procedure',
 'die Leitlinie': 'guideline',
 'das Audit, die Prüfung': 'audit',
 'der Auditor, der Prüfer': 'auditor',
 'die Audit-Feststellung': 'audit finding',
 'der Nachweis, das Beweismittel': 'evidence',
 'die Bestätigung, die Attestierung': 'attestation',
 'die Zertifizierung': 'certification',
 'die Akkreditierung': 'accreditation',
 'die Gap-Analyse': 'gap analysis',
 'das Reifegradmodell': 'maturity model',
 'die Risikobewertung': 'risk assessment',
 'das Risikoregister': 'risk register',
 'die Risikobereitschaft': 'risk appetite',
 'die Risikotoleranz': 'risk tolerance',
 'die Risikoakzeptanz': 'risk acceptance',
 'der Risikotransfer': 'risk transfer',
 'die Risikovermeidung': 'risk avoidance',
 'das inhärente Risiko': 'inherent risk',
 'die Business-Impact-Analyse': 'business impact analysis',
 'das Wiederherstellungszeitziel (RTO)': 'recovery time objective (RTO)',
 'das Wiederherstellungspunktziel (RPO)': 'recovery point objective (RPO)',
 'die Datenklassifizierung': 'data classification',
 'die Datenaufbewahrung': 'data retention',
 'die Datenminimierung': 'data minimisation',
 'personenbezogene Daten (Pl.)': 'personal data',
 'die betroffene Person': 'data subject',
 'der Verantwortliche (Datenschutz)': 'data controller',
 'der Auftragsverarbeiter': 'data processor',
 'die DSGVO': 'GDPR',
 'die Meldung einer Datenpanne': 'breach notification',
 'Privacy by Design': 'privacy by design',
 'das Drittanbieterrisiko': 'third-party risk',
 'die Lieferantenbewertung': 'vendor assessment',
 'die Sorgfaltsprüfung (Due Diligence)': 'due diligence',
 'das Service-Level-Agreement (SLA)': 'service level agreement (SLA)',
 'die Geheimhaltungsvereinbarung (NDA)': 'NDA',
 'die Sicherheitsschulung': 'security awareness training',
 'die Nutzungsrichtlinie': 'acceptable use policy',
 'das Änderungsmanagement': 'change management',
 'der Genehmigungsworkflow': 'approval workflow',
 'der Ausnahmeantrag': 'exception request'}
