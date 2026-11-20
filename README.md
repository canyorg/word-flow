# Word Flow

**A tiny, always-on-top vocabulary widget.** Every 20 seconds it shows a new word, verb or phrase with its meaning right below it, so you pick up vocabulary whenever your eye lands on it.

[English](#english) · [Türkçe](#türkçe) · [Deutsch](#deutsch)

![Word Flow screenshots](screenshots/preview.png)

| Pair | Word → meaning | Modes | Levels | Words | UI language |
|---|---|---|---|---|---|
| `de-tr` | German → Turkish | General | A1.1 – C2.2 | 368 | Türkçe |
| `en-tr` | English → Turkish | Everyday + Academic | A1.1 – C2.2 / B1.1 – C2.2 | 287 + 159 | Türkçe |
| `en-de` | English → German | Everyday + Academic | A1.1 – C2.2 / B1.1 – C2.2 | 287 + 159 | Deutsch |
| `de-en` | German → English | General | A1.1 – C2.2 | 368 | English |

---

## English

### Features
- **A new card every 20 s** (10–60 s, change it from the right-click menu). A thin line at the bottom shows the time left.
- **The timer pauses while your mouse is over the card**, so you can read in peace.
- **✓ I know it**: the word comes back much less often. **✗ Didn't know**: it comes back more often and shows up again 4 cards later.
- **Levels A1.1 – C2.2** (12 steps). Most cards come from your level, with occasional review from lower ones.
- English pairs come with two modes: **Everyday** (phrasal verbs, idioms) and **Academic** (vocabulary for papers and theses, with typical collocations such as *mitigate the risk*).
- German articles are colour-coded: **der** in blue, **die** in pink, **das** in green. Verbs show their forms (*er fährt · ist gefahren*).
- Drag the card anywhere, then 📍 lock its position. It stays always on top and you can set your own background image.
- Your progress is saved per pair in `~/.config/…`.

### Install (Linux)
```bash
sudo dnf install python3-pyqt6        # Fedora   (Debian/Ubuntu: sudo apt install python3-pyqt6)
git clone https://github.com/canyorg/word-flow.git
cd word-flow
./install.sh                          # adds 4 entries to the app menu
./install.sh --autostart de-tr en-tr  # optional: start these at login
```
Or run a pair directly: `python3 wordflow.py en-de`

**Windows:** `pip install PyQt6`, then `py wordflow.py de-en`

### Add your own words
The word lists live in `wordlists/german.py` and `wordlists/english.py`, one line per word:
```
type|word|Turkish meaning|hint
v|fahren|(araçla) gitmek|er fährt · ist gefahren
```
Then add the translation to `DE_EN` / `EN_DE`.

---

## Türkçe

Ekranın köşesinde duran küçük bir kelime kartı. Her 20 saniyede yeni bir kelime, fiil ya da kalıp gösteriyor ve anlamı hemen altında yazıyor. Gözün takıldığında öğreniyorsun.

- **✓ Biliyorum** dediğin kelime çok daha seyrek gelir. **✗ Bilmiyordum** dediğin daha sık gelir ve 4 kart sonra tekrar karşına çıkar.
- Fare kartın üstündeyken süre durur.
- Seviye: A1.1 – C2.2. İngilizcede **Günlük** ve **Akademik** olmak üzere iki mod var.
- Sağ tıkla süreyi, seviyeyi, arka plan resmini ve "her zaman üstte" ayarını değiştirebilirsin. 📍 kartın konumunu kilitler.

**Kurulum (Fedora):**
```bash
sudo dnf install python3-pyqt6
git clone https://github.com/canyorg/word-flow.git && cd word-flow
./install.sh --autostart de-tr en-tr
```

---

## Deutsch

Ein kleines Vokabel-Widget, das immer im Vordergrund bleibt. Alle 20 Sekunden erscheint ein neues Wort mit seiner Bedeutung direkt darunter.

- **✓ Kann ich**: Das Wort kommt seltener. **✗ Wusste ich nicht**: Es kommt öfter und erscheint nach 4 Karten erneut.
- Solange die Maus auf der Karte ist, hält der Timer an.
- Niveaus A1.1 – C2.2. Englisch gibt es in zwei Modi: **Alltag** und **Akademisch**.
- `en-de` (Englisch → Deutsch) hat eine deutsche Oberfläche, `de-en` eine englische.

```bash
sudo dnf install python3-pyqt6     # oder: pip install --user PyQt6
./install.sh --autostart en-de
```

---

Built with the help of Claude (vibe-coded). Word lists were hand-picked; if you spot a wrong translation, please open an issue or a PR.

License: MIT
