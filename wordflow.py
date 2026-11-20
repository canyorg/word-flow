#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Word Flow — a tiny always-on-top vocabulary widget.

A new word / verb / phrase every 20 seconds, with its meaning right below it,
so you learn it whenever your eye catches it.

On first start it asks which language you speak (Turkish, English, German or
Russian) and which of the other three you want to learn; you can change this
any time from the right-click menu.

Language pairs (word → meaning):
    de-tr / en-tr   German / English → Turkish   (Turkish speakers)
    de-en / tr-en   German / Turkish → English   (English speakers)
    en-de / tr-de   English / Turkish → German   (German speakers)
    en-ru / de-ru / tr-ru   English / German / Turkish → Russian (Russian speakers)
    ru-tr / ru-en / ru-de   Russian → Turkish / English / German (learn Russian)

Usage:
    python3 wordflow.py           # remembers your languages, asks on first start
    python3 wordflow.py en-de     # open one pair directly
"""
import os
import re
import sys
import json
import random
import datetime
import argparse
from html import escape

# GNOME/KDE on Wayland ignore "always on top" for normal clients -> use XWayland.
if sys.platform.startswith("linux") and os.environ.get("WAYLAND_DISPLAY") \
        and "QT_QPA_PLATFORM" not in os.environ:
    os.environ["QT_QPA_PLATFORM"] = "xcb"

from PyQt6.QtCore import Qt, QTimer, QRectF, QPoint
from PyQt6.QtGui import (QPainter, QColor, QLinearGradient, QRadialGradient,
                         QPainterPath, QPixmap, QFont, QFontMetrics,
                         QActionGroup)
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                             QVBoxLayout, QHBoxLayout, QGridLayout,
                             QStackedWidget, QMenu, QFileDialog, QSizePolicy)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wordlists import german, english, russian  # noqa: E402

APP_W, APP_H = 340, 196
CONFIG_ROOT = os.path.join(os.path.expanduser("~"), ".config")

# --------------------------------------------------------------------------- UI text
UI = {
    "tr": {
        "know": "✓ Biliyorum", "dont": "✗ Bilmiyordum",
        "tip_know": "Öğrendim — daha az göster", "tip_dont": "Daha sık göster",
        "next": "Sonraki", "tip_level": "Mod / seviye değiştir",
        "pin_on": "Konum kilitli — aç", "pin_off": "Konumu kilitle",
        "choose": "Seviyeni seç",
        "modes": {"general": "Genel", "daily": "Günlük", "academic": "Akademik",
                  "cyber": "Siber"},
        "hints": {"general": "Temel 1500 kelimeden C2 deyimlerine — seviyeni seç",
                  "daily": "Günlük kelimeler, phrasal verb'ler, deyimler — seviyeni seç",
                  "academic": "Makale, tez ve sunum dili — seviyeni seç",
                  "cyber": "Siber güvenlik: ağ → saldırı → pentest → SOC → GRC"},
        "m_mode": "Mod", "m_level": "Seviye", "m_interval": "Değişme süresi",
        "sec": "{} saniye", "m_lock": "Konumu kilitle", "m_top": "Her zaman üstte", "m_auto": "Windows ile başlat",
        "m_bg": "Arka plan resmi seç…", "m_bg_reset": "Varsayılan arka plan",
        "m_reset": "İlerlemeyi sıfırla", "m_close": "Kapat", "images": "Resimler",
        "m_lang": "Dili değiştir…", "learn_q": "Hangi dili öğrenmek istiyorsunuz?",
        "learn_hint": "Kelimeler bu dilde gelir, anlamı Türkçe yazar",
        "langs": {"tr": "Türkçe", "en": "İngilizce", "de": "Almanca", "ru": "Rusça"}, "back": "‹ Geri",
        "types": {"n": "İSİM", "v": "FİİL", "a": "SIFAT", "d": "ZARF",
                  "p": "KALIP", "w": "KELİME"},
    },
    "en": {
        "know": "✓ I know it", "dont": "✗ Didn't know",
        "tip_know": "Learned — show less often", "tip_dont": "Show more often",
        "next": "Next", "tip_level": "Change mode / level",
        "pin_on": "Position locked — unlock", "pin_off": "Lock position",
        "choose": "Choose your level",
        "modes": {"general": "General", "daily": "Everyday", "academic": "Academic",
                  "cyber": "Cyber"},
        "hints": {"general": "From 1,500 core words to C2 idioms — choose your level",
                  "daily": "Everyday words, phrasal verbs, idioms — choose your level",
                  "academic": "Language of papers, theses and talks — choose your level",
                  "cyber": "Cybersecurity: network → attacks → pentest → SOC → GRC"},
        "m_mode": "Mode", "m_level": "Level", "m_interval": "Change every",
        "sec": "{} seconds", "m_lock": "Lock position", "m_top": "Always on top", "m_auto": "Start with Windows",
        "m_bg": "Choose background image…", "m_bg_reset": "Default background",
        "m_reset": "Reset progress", "m_close": "Close", "images": "Images",
        "m_lang": "Change language…", "learn_q": "Which language do you want to learn?",
        "learn_hint": "Words appear in that language, with the meaning in English",
        "langs": {"tr": "Turkish", "en": "English", "de": "German", "ru": "Russian"}, "back": "‹ Back",
        "types": {"n": "NOUN", "v": "VERB", "a": "ADJECTIVE", "d": "ADVERB",
                  "p": "PHRASE", "w": "WORD"},
    },
    "de": {
        "know": "✓ Kann ich", "dont": "✗ Wusste ich nicht",
        "tip_know": "Gelernt — seltener zeigen", "tip_dont": "Öfter zeigen",
        "next": "Weiter", "tip_level": "Modus / Niveau ändern",
        "pin_on": "Position gesperrt — entsperren", "pin_off": "Position sperren",
        "choose": "Wähle dein Niveau",
        "modes": {"general": "Allgemein", "daily": "Alltag", "academic": "Akademisch",
                  "cyber": "Cyber"},
        "hints": {"general": "Von 1.500 Grundwörtern bis zu C2-Redewendungen",
                  "daily": "Alltagswörter, Phrasal Verbs, Redewendungen",
                  "academic": "Sprache für Paper, Abschlussarbeit und Vortrag",
                  "cyber": "Cybersecurity: Netzwerk → Angriffe → Pentest → SOC → GRC"},
        "m_mode": "Modus", "m_level": "Niveau", "m_interval": "Wechsel alle",
        "sec": "{} Sekunden", "m_lock": "Position sperren", "m_top": "Immer im Vordergrund", "m_auto": "Mit Windows starten",
        "m_bg": "Hintergrundbild wählen…", "m_bg_reset": "Standard-Hintergrund",
        "m_reset": "Fortschritt zurücksetzen", "m_close": "Schließen", "images": "Bilder",
        "m_lang": "Sprache ändern…", "learn_q": "Welche Sprache möchten Sie lernen?",
        "learn_hint": "Die Wörter erscheinen in dieser Sprache, die Bedeutung auf Deutsch",
        "langs": {"tr": "Türkisch", "en": "Englisch", "de": "Deutsch", "ru": "Russisch"}, "back": "‹ Zurück",
        "types": {"n": "NOMEN", "v": "VERB", "a": "ADJEKTIV", "d": "ADVERB",
                  "p": "WENDUNG", "w": "WORT"},
    },
    "ru": {
        "know": "✓ Знаю", "dont": "✗ Не знал(а)",
        "tip_know": "Выучил(а) — показывать реже", "tip_dont": "Показывать чаще",
        "next": "Дальше", "tip_level": "Сменить режим / уровень",
        "pin_on": "Позиция закреплена — открепить", "pin_off": "Закрепить позицию",
        "choose": "Выберите уровень",
        "modes": {"general": "Общий", "daily": "Повседневный", "academic": "Академический",
                  "cyber": "Кибер"},
        "hints": {"general": "От 1500 базовых слов до идиом уровня C2",
                  "daily": "Повседневные слова, фразовые глаголы, идиомы",
                  "academic": "Язык статей, диссертаций и докладов",
                  "cyber": "Кибербезопасность: сеть → атаки → пентест → SOC → GRC"},
        "m_mode": "Режим", "m_level": "Уровень", "m_interval": "Смена каждые",
        "sec": "{} секунд", "m_lock": "Закрепить позицию", "m_top": "Поверх всех окон", "m_auto": "Запускать вместе с Windows",
        "m_bg": "Выбрать фон…", "m_bg_reset": "Стандартный фон",
        "m_reset": "Сбросить прогресс", "m_close": "Закрыть", "images": "Изображения",
        "m_lang": "Сменить язык…", "learn_q": "Какой язык вы хотите учить?",
        "learn_hint": "Слова показываются на этом языке, значение — по-русски",
        "langs": {"tr": "Турецкий", "en": "Английский", "de": "Немецкий", "ru": "Русский"},
        "back": "‹ Назад",
        "types": {"n": "СУЩ.", "v": "ГЛАГОЛ", "a": "ПРИЛ.", "d": "НАРЕЧИЕ",
                  "p": "ВЫРАЖЕНИЕ", "w": "СЛОВО"},
    },
}


# --------------------------------------------------------------------------- word lists
def parse_block(raw, mode, meaning):
    """raw: level -> 'type|word|turkish|hint' lines. meaning(word, turkish) -> text"""
    out = {}
    for lv, block in raw.items():
        items = []
        for line in block.strip().splitlines():
            p = [x.strip() for x in line.split("|")]
            if len(p) < 3:
                continue
            items.append({"t": p[0], "w": p[1], "m": meaning(p[1], p[2]),
                          "x": p[3] if len(p) > 3 else "", "lv": lv,
                          "mode": mode, "key": f"{mode}:{p[1]}"})
        out[lv] = items
    return out


def parse_reverse(raw, mode, source):
    """Turkish → X: the Turkish meaning becomes the word, source(word) the meaning."""
    out = {}
    for lv, block in raw.items():
        items, seen = [], set()
        for line in block.strip().splitlines():
            p = [x.strip() for x in line.split("|")]
            if len(p) < 3 or p[2] in seen:
                continue
            seen.add(p[2])
            items.append({"t": p[0], "w": p[2], "m": source(p[1]), "x": "", "lv": lv,
                          "mode": mode, "key": f"{mode}:{p[2]}"})
        out[lv] = items
    return out


def en_de(mode):
    table = {"academic": english.EN_DE_ACADEMIC, "cyber": english.EN_DE_CYBER}.get(
        mode, english.EN_DE)
    return lambda w, tr: table.get(w) or english.EN_DE.get(w, tr)


def de_en(table):
    return lambda w, tr: table.get(w, tr)


def to_ru(table):
    return lambda w, tr: table.get(w, tr)


def parse_ru(raw, mode, table, meaning):
    """Russian → X: the Russian translation of each entry becomes the word."""
    out = {}
    for lv, block in raw.items():
        items, seen = [], set()
        for line in block.strip().splitlines():
            p = [x.strip() for x in line.split("|")]
            if len(p) < 3 or p[1] not in table:
                continue
            ru = table[p[1]]
            if ru in seen or ru.startswith("("):
                continue
            seen.add(ru)
            items.append({"t": p[0], "w": ru, "m": meaning(p[1], p[2]), "x": "", "lv": lv,
                          "mode": mode, "key": f"{mode}:{ru}"})
        out[lv] = items
    return out


# (spoken language, language to learn) -> pair
PAIR_FOR = {("tr", "en"): "en-tr", ("tr", "de"): "de-tr",
            ("en", "de"): "de-en", ("en", "tr"): "tr-en",
            ("de", "en"): "en-de", ("de", "tr"): "tr-de",
            ("ru", "en"): "en-ru", ("ru", "de"): "de-ru", ("ru", "tr"): "tr-ru",
            ("tr", "ru"): "ru-tr", ("en", "ru"): "ru-en", ("de", "ru"): "ru-de"}

PAIRS = {
    "de-tr": {"title": "Kelime Akışı · DE → TR", "ui": "tr", "src": "de", "dst": "tr",
              "state": "kelime-akisi",
              "modes": {"general": parse_block(german.GERMAN, "general", lambda w, tr: tr),
                        "academic": parse_block(german.GERMAN_ACADEMIC, "academic",
                                                lambda w, tr: tr),
                        "cyber": parse_block(german.GERMAN_CYBER, "cyber", lambda w, tr: tr)}},
    "en-tr": {"title": "Word Flow · EN → TR", "ui": "tr", "src": "en", "dst": "tr",
              "state": "kelime-akisi-en",
              "modes": {"daily": parse_block(english.DAILY, "daily", lambda w, tr: tr),
                        "academic": parse_block(english.ACADEMIC, "academic",
                                                lambda w, tr: tr),
                        "cyber": parse_block(english.CYBER, "cyber", lambda w, tr: tr)}},
    "en-de": {"title": "Word Flow · EN → DE", "ui": "de", "src": "en", "dst": "de",
              "state": "word-flow-en-de",
              "modes": {"daily": parse_block(english.DAILY, "daily", en_de("daily")),
                        "academic": parse_block(english.ACADEMIC, "academic",
                                                en_de("academic")),
                        "cyber": parse_block(english.CYBER, "cyber", en_de("cyber"))}},
    "de-en": {"title": "Word Flow · DE → EN", "ui": "en", "src": "de", "dst": "en",
              "state": "word-flow-de-en",
              "modes": {"general": parse_block(german.GERMAN, "general", de_en(german.DE_EN)),
                        "academic": parse_block(german.GERMAN_ACADEMIC, "academic",
                                                de_en(german.DE_EN_ACADEMIC)),
                        "cyber": parse_block(german.GERMAN_CYBER, "cyber",
                                             de_en(german.DE_EN_CYBER))}},
    "tr-en": {"title": "Word Flow · TR → EN", "ui": "en", "src": "tr", "dst": "en",
              "state": "word-flow-tr-en",
              "modes": {"daily": parse_reverse(english.DAILY, "daily", lambda w: w),
                        "academic": parse_reverse(english.ACADEMIC, "academic", lambda w: w),
                        "cyber": parse_reverse(english.CYBER, "cyber", lambda w: w)}},
    "tr-de": {"title": "Word Flow · TR → DE", "ui": "de", "src": "tr", "dst": "de",
              "state": "word-flow-tr-de",
              "modes": {"general": parse_reverse(german.GERMAN, "general", lambda w: w),
                        "academic": parse_reverse(german.GERMAN_ACADEMIC, "academic", lambda w: w),
                        "cyber": parse_reverse(german.GERMAN_CYBER, "cyber", lambda w: w)}},
    "en-ru": {"title": "Word Flow · EN → RU", "ui": "ru", "src": "en", "dst": "ru",
              "state": "word-flow-en-ru",
              "modes": {m: parse_block(r, m, to_ru(russian.EN_RU)) for m, r in
                        (("daily", english.DAILY), ("academic", english.ACADEMIC),
                         ("cyber", english.CYBER))}},
    "de-ru": {"title": "Word Flow · DE → RU", "ui": "ru", "src": "de", "dst": "ru",
              "state": "word-flow-de-ru",
              "modes": {m: parse_block(r, m, to_ru(russian.DE_RU)) for m, r in
                        (("general", german.GERMAN), ("academic", german.GERMAN_ACADEMIC),
                         ("cyber", german.GERMAN_CYBER))}},
    "tr-ru": {"title": "Word Flow · TR → RU", "ui": "ru", "src": "tr", "dst": "ru",
              "state": "word-flow-tr-ru",
              "modes": {m: parse_reverse(r, m, lambda w: russian.EN_RU.get(w, w)) for m, r in
                        (("daily", english.DAILY), ("academic", english.ACADEMIC),
                         ("cyber", english.CYBER))}},
    "ru-tr": {"title": "Word Flow · RU → TR", "ui": "tr", "src": "ru", "dst": "tr",
              "state": "word-flow-ru-tr",
              "modes": {m: parse_ru(r, m, russian.EN_RU, lambda w, tr: tr) for m, r in
                        (("daily", english.DAILY), ("academic", english.ACADEMIC),
                         ("cyber", english.CYBER))}},
    "ru-en": {"title": "Word Flow · RU → EN", "ui": "en", "src": "ru", "dst": "en",
              "state": "word-flow-ru-en",
              "modes": {m: parse_ru(r, m, russian.EN_RU, lambda w, tr: w) for m, r in
                        (("daily", english.DAILY), ("academic", english.ACADEMIC),
                         ("cyber", english.CYBER))}},
    "ru-de": {"title": "Word Flow · RU → DE", "ui": "de", "src": "ru", "dst": "de",
              "state": "word-flow-ru-de",
              "modes": {m: parse_ru(r, m, russian.DE_RU, lambda w, tr: w) for m, r in
                        (("general", german.GERMAN), ("academic", german.GERMAN_ACADEMIC),
                         ("cyber", german.GERMAN_CYBER))}},
}

ARTICLE_COLORS = {"der": "#7fb2ff", "die": "#ff8fa3", "das": "#7fe0a8"}
ARTICLE_RE = re.compile(r"(?<![\wäöüßÄÖÜ])(der|die|das)(?= [A-ZÄÖÜ])")


def colorize_german(text, base):
    """Colour der/die/das (blue / pink / green) in a German string."""
    esc = escape(text, quote=False)
    html = ARTICLE_RE.sub(
        lambda m: f"<span style='color:{ARTICLE_COLORS[m.group(1)]}'>{m.group(1)}</span>",
        esc)
    return f"<span style='color:{base}'>{html}</span>"


def paint_card(w, bg_pix):
    """Rounded dark card background (or the user's picture). Returns (painter, path)."""
    p = QPainter(w)
    p.setRenderHint(QPainter.RenderHint.Antialiasing)
    path = QPainterPath()
    path.addRoundedRect(QRectF(w.rect()).adjusted(0.5, 0.5, -0.5, -0.5), 20, 20)
    p.setClipPath(path)
    if bg_pix and not bg_pix.isNull():
        pm = bg_pix.scaled(w.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                           Qt.TransformationMode.SmoothTransformation)
        p.drawPixmap(int((w.width() - pm.width()) / 2), int((w.height() - pm.height()) / 2), pm)
        ov = QLinearGradient(0, 0, 0, w.height())
        ov.setColorAt(0, QColor(10, 10, 25, 110))
        ov.setColorAt(1, QColor(10, 10, 25, 185))
        p.fillRect(w.rect(), ov)
    else:
        g = QLinearGradient(0, 0, w.width(), w.height())
        g.setColorAt(0, QColor("#141a3a"))
        g.setColorAt(0.55, QColor("#2a1d4f"))
        g.setColorAt(1, QColor("#0d1226"))
        p.fillRect(w.rect(), g)
        glow = QRadialGradient(w.width() * 0.85, w.height() * 0.1, w.width() * 0.6)
        glow.setColorAt(0, QColor(255, 140, 120, 70))
        glow.setColorAt(1, QColor(255, 140, 120, 0))
        p.fillRect(w.rect(), glow)
        glow2 = QRadialGradient(w.width() * 0.1, w.height() * 1.0, w.width() * 0.55)
        glow2.setColorAt(0, QColor(90, 160, 255, 60))
        glow2.setColorAt(1, QColor(90, 160, 255, 0))
        p.fillRect(w.rect(), glow2)
    return p, path


CHIP_CSS = ("QPushButton{color:#e8e6ff;background:rgba(255,255,255,0.13);"
            "border:none;border-radius:9px;padding:2px 9px;font-size:11px;"
            "font-weight:600;}"
            "QPushButton:hover{background:rgba(255,255,255,0.24);}")


def btn_css(bg, hover):
    return ("QPushButton{color:white;background:%s;border:none;"
            "border-radius:11px;padding:5px 10px;font-size:12px;"
            "font-weight:600;}QPushButton:hover{background:%s;}" % (bg, hover))


# --------------------------------------------------------------------------- widget
class WordWidget(QWidget):
    def __init__(self, pair_id, controller=None, pos=None):
        super().__init__()
        self.controller = controller
        self.pair_id = pair_id
        self.pair = PAIRS[pair_id]
        self.T = UI[self.pair["ui"]]
        self.words = self.pair["modes"]
        self.levels = {m: list(v.keys()) for m, v in self.words.items()}
        self.config_dir = os.path.join(CONFIG_ROOT, self.pair["state"])
        self.state_file = os.path.join(self.config_dir, "state.json")

        self.st = self.load_state()
        self.bg_pix = None
        self.load_bg()

        self.cur = None
        self.counter = 0
        self.recent = []
        self.soon = []          # [(card_no, key)] — "didn't know" words come back soon
        self.elapsed = 0.0
        self.hovering = False
        self._drag = None
        self.picker_mode = self.mode()

        flags = Qt.WindowType.FramelessWindowHint | Qt.WindowType.Tool
        if self.st["on_top"]:
            flags |= Qt.WindowType.WindowStaysOnTopHint
        self.setWindowFlags(flags)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setFixedSize(APP_W, APP_H)
        self.setWindowTitle(self.pair["title"])

        self.stack = QStackedWidget(self)
        self.stack.setGeometry(0, 0, APP_W, APP_H)
        self.stack.addWidget(self.build_card())
        self.stack.addWidget(self.build_picker())

        self.tick = QTimer(self)
        self.tick.timeout.connect(self.on_tick)
        self.tick.start(100)
        self.save_timer = QTimer(self)
        self.save_timer.setSingleShot(True)
        self.save_timer.timeout.connect(self.save_state)

        if pos is not None:
            self.move(pos)
        elif self.st.get("pos"):
            self.move(QPoint(*self.st["pos"]))
        else:
            self.move(default_pos())

        if self.level() in self.levels.get(self.mode(), []):
            self.show_card()
        else:
            self.show_picker()

    # ------------------------------------------------------------ state
    def mode(self):
        m = self.st.get("mode")
        return m if m in self.words else next(iter(self.words))

    def level(self):
        return self.st["levels"].get(self.mode())

    def load_state(self):
        d = {"mode": None, "levels": {}, "interval": 20, "pinned": False,
             "on_top": True, "bg": None, "pos": None, "words": {},
             "today": {"date": "", "k": 0, "u": 0}}
        try:
            with open(self.state_file, encoding="utf-8") as f:
                d.update(json.load(f))
        except Exception:
            pass
        # migrate the first single-file version (one level, plain word keys)
        if isinstance(d.get("level"), str) and not d["levels"]:
            d["levels"] = {"general": d.pop("level")}
            d["mode"] = "general"
        d.pop("level", None)
        if any(":" not in k for k in d["words"]):
            d["words"] = {(k if ":" in k else f"general:{k}"): v
                          for k, v in d["words"].items()}
        return d

    def save_state(self):
        try:
            os.makedirs(self.config_dir, exist_ok=True)
            self.st["pos"] = [self.x(), self.y()]
            tmp = self.state_file + ".tmp"
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(self.st, f, ensure_ascii=False, indent=1)
            os.replace(tmp, self.state_file)
        except Exception as e:
            print("Could not save state:", e, file=sys.stderr)

    def ws(self, e):
        return self.st["words"].setdefault(e["key"], {"w": 1.0, "k": 0, "u": 0})

    def today(self):
        t = self.st["today"]
        d = datetime.date.today().isoformat()
        if t.get("date") != d:
            t.update({"date": d, "k": 0, "u": 0})
        return t

    # ------------------------------------------------------------ UI
    def build_card(self):
        page = QWidget()
        v = QVBoxLayout(page)
        v.setContentsMargins(16, 11, 16, 14)
        v.setSpacing(0)

        top = QHBoxLayout()
        top.setSpacing(6)
        self.level_btn = QPushButton()
        self.level_btn.setStyleSheet(CHIP_CSS)
        self.level_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.level_btn.setToolTip(self.T["tip_level"])
        self.level_btn.clicked.connect(self.show_picker)
        self.type_lbl = QLabel()
        self.type_lbl.setStyleSheet("color:rgba(255,255,255,0.55);"
                                    "font-size:9px;font-weight:700;letter-spacing:1px;")
        self.stats_lbl = QLabel()
        self.stats_lbl.setStyleSheet("color:rgba(255,255,255,0.6);font-size:11px;")
        self.pin_btn = QPushButton()
        self.pin_btn.setFixedSize(26, 22)
        self.pin_btn.setStyleSheet(CHIP_CSS)
        self.pin_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.pin_btn.clicked.connect(self.toggle_pin)
        top.addWidget(self.level_btn)
        top.addWidget(self.type_lbl)
        top.addStretch(1)
        top.addWidget(self.stats_lbl)
        if self.controller:
            self.lang_btn = QPushButton("🌐")
            self.lang_btn.setFixedSize(26, 22)
            self.lang_btn.setStyleSheet(CHIP_CSS)
            self.lang_btn.setCursor(Qt.CursorShape.PointingHandCursor)
            self.lang_btn.setToolTip(self.T["m_lang"])
            self.lang_btn.clicked.connect(lambda: self.controller.change_language(self))
            top.addWidget(self.lang_btn)
        top.addWidget(self.pin_btn)
        v.addLayout(top)
        v.addStretch(1)

        self.w_lbl = QLabel()
        self.w_lbl.setTextFormat(Qt.TextFormat.RichText)
        self.w_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.x_lbl = QLabel()
        self.x_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.x_lbl.setStyleSheet("color:rgba(255,255,255,0.5);font-size:10px;")
        self.m_lbl = QLabel()
        self.m_lbl.setTextFormat(Qt.TextFormat.RichText)
        self.m_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.m_lbl.setWordWrap(True)
        for w in (self.w_lbl, self.x_lbl, self.m_lbl):
            w.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        v.addWidget(self.w_lbl)
        v.addWidget(self.x_lbl)
        v.addSpacing(3)
        v.addWidget(self.m_lbl)
        v.addStretch(1)

        row = QHBoxLayout()
        row.setSpacing(6)
        self.know_btn = QPushButton(self.T["know"])
        self.know_btn.setStyleSheet(btn_css("rgba(46,170,110,0.55)", "rgba(46,170,110,0.85)"))
        self.know_btn.setToolTip(self.T["tip_know"])
        self.know_btn.clicked.connect(lambda: self.mark(True))
        self.dont_btn = QPushButton(self.T["dont"])
        self.dont_btn.setStyleSheet(btn_css("rgba(220,80,100,0.55)", "rgba(220,80,100,0.85)"))
        self.dont_btn.setToolTip(self.T["tip_dont"])
        self.dont_btn.clicked.connect(lambda: self.mark(False))
        self.skip_btn = QPushButton("›")
        self.skip_btn.setFixedWidth(34)
        self.skip_btn.setStyleSheet(btn_css("rgba(255,255,255,0.14)", "rgba(255,255,255,0.28)"))
        self.skip_btn.setToolTip(self.T["next"])
        self.skip_btn.clicked.connect(self.next_word)
        for b in (self.know_btn, self.dont_btn, self.skip_btn):
            b.setCursor(Qt.CursorShape.PointingHandCursor)
        row.addWidget(self.know_btn, 1)
        row.addWidget(self.dont_btn, 1)
        row.addWidget(self.skip_btn)
        v.addLayout(row)
        return page

    def build_picker(self):
        page = QWidget()
        v = QVBoxLayout(page)
        v.setContentsMargins(16, 11, 16, 12)
        v.setSpacing(7)

        self.mode_btns = {}
        if len(self.words) > 1:
            seg = QHBoxLayout()
            seg.setSpacing(0)
            for m in self.words:
                b = QPushButton(self.T["modes"][m])
                b.setCursor(Qt.CursorShape.PointingHandCursor)
                b.clicked.connect(lambda _=False, x=m: self.pick_mode(x))
                self.mode_btns[m] = b
                seg.addWidget(b)
            v.addLayout(seg)
        else:
            t = QLabel(self.T["choose"])
            t.setAlignment(Qt.AlignmentFlag.AlignCenter)
            t.setStyleSheet("color:white;font-size:15px;font-weight:700;")
            v.addWidget(t)

        self.pick_hint = QLabel()
        self.pick_hint.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pick_hint.setWordWrap(True)
        self.pick_hint.setStyleSheet("color:rgba(255,255,255,0.6);font-size:10px;")
        v.addWidget(self.pick_hint)

        host = QWidget()
        self.grid = QGridLayout(host)
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.grid.setSpacing(6)
        v.addWidget(host)
        v.addStretch(1)
        return page

    def seg_css(self, on, pos):
        r = {"first": "border-top-left-radius:11px;border-bottom-left-radius:11px;",
             "last": "border-top-right-radius:11px;border-bottom-right-radius:11px;"
             }.get(pos, "border-radius:0px;")
        bg = "rgba(140,120,255,0.8)" if on else "rgba(255,255,255,0.12)"
        return ("QPushButton{color:white;background:%s;border:none;%s"
                "padding:5px;font-size:12px;font-weight:700;}"
                "QPushButton:hover{background:rgba(140,120,255,0.6);}" % (bg, r))

    def pick_mode(self, m):
        self.picker_mode = m
        n = len(self.mode_btns)
        for i, (k, b) in enumerate(self.mode_btns.items()):
            b.setStyleSheet(self.seg_css(k == m, "first" if i == 0 else
                                         "last" if i == n - 1 else "mid"))
        self.pick_hint.setText(self.T["hints"][m])
        while self.grid.count():
            wd = self.grid.takeAt(0).widget()
            if wd is not None:
                wd.hide()
                wd.setParent(None)
                wd.deleteLater()
        cur = self.st["levels"].get(m) if m == self.mode() else None
        for i, lv in enumerate(self.levels[m]):
            b = QPushButton(lv)
            b.setCursor(Qt.CursorShape.PointingHandCursor)
            b.setStyleSheet(btn_css("rgba(140,120,255,0.75)" if lv == cur
                                    else "rgba(255,255,255,0.13)", "rgba(140,120,255,0.9)"))
            b.clicked.connect(lambda _=False, x=lv: self.set_level(m, x))
            self.grid.addWidget(b, i // 4, i % 4)

    def show_picker(self):
        self.pick_mode(self.mode())
        self.stack.setCurrentIndex(1)
        self.update()

    def show_card(self):
        self.stack.setCurrentIndex(0)
        self.refresh_chrome()
        if self.cur is None:
            self.next_word()
        self.update()

    def set_level(self, mode, lv):
        changed = mode != self.mode() or lv != self.level()
        self.st["mode"] = mode
        self.st["levels"][mode] = lv
        self.save_state()
        if changed:
            self.cur = None
            self.soon.clear()
            self.recent.clear()
        self.show_card()

    def refresh_chrome(self):
        lvl = self.level()
        if len(self.words) > 1:
            self.level_btn.setText(f"{self.T['modes'][self.mode()]} · {lvl} ▾")
        else:
            self.level_btn.setText(f"{lvl} ▾")
        self.pin_btn.setText("📌" if self.st["pinned"] else "📍")
        self.pin_btn.setToolTip(self.T["pin_on"] if self.st["pinned"] else self.T["pin_off"])
        t = self.today()
        self.stats_lbl.setText(f"✓{t['k']}  ✗{t['u']}")

    # ------------------------------------------------------------ choosing words
    def pool(self):
        m = self.mode()
        lvls = self.levels[m]
        idx = lvls.index(self.level())
        items, weights = [], []
        for i, lv in enumerate(lvls[:idx + 1]):
            base = 1.0 if i == idx else (0.35 if i == idx - 1 else 0.12)
            for e in self.words[m][lv]:
                items.append(e)
                weights.append(base * self.ws(e)["w"])
        return items, weights

    def find(self, key):
        for m in self.words.values():
            for items in m.values():
                for e in items:
                    if e["key"] == key:
                        return e
        return None

    def next_word(self):
        self.counter += 1
        e = None
        if self.soon and self.soon[0][0] <= self.counter:
            e = self.find(self.soon.pop(0)[1])
        if e is None:
            items, weights = self.pool()
            cand = [(it, w) for it, w in zip(items, weights) if it["key"] not in self.recent]
            if not cand:
                cand = list(zip(items, weights))
            e = random.choices([c[0] for c in cand], weights=[c[1] for c in cand])[0]
        self.cur = e
        self.recent = (self.recent + [e["key"]])[-8:]
        self.elapsed = 0.0
        self.render_word()
        self.update()

    def mark(self, known):
        if not self.cur:
            return
        s = self.ws(self.cur)
        t = self.today()
        if known:
            s["k"] += 1
            s["w"] = max(0.04, s["w"] * 0.3)
            t["k"] += 1
        else:
            s["u"] += 1
            s["w"] = min(8.0, s["w"] * 2 + 0.5)
            t["u"] += 1
            self.soon = sorted([x for x in self.soon if x[1] != self.cur["key"]]
                               + [(self.counter + 4, self.cur["key"])])
        self.save_state()
        self.refresh_chrome()
        self.next_word()

    # ------------------------------------------------------------ drawing
    def fit_font(self, text, max_pt, min_pt, width):
        f = QFont(self.font())
        f.setBold(True)
        pt = max_pt
        while pt > min_pt:
            f.setPointSizeF(pt)
            if QFontMetrics(f).horizontalAdvance(text) <= width:
                break
            pt -= 0.5
        f.setPointSizeF(pt)
        return f

    def render_word(self):
        e = self.cur
        avail = APP_W - 36
        self.w_lbl.setFont(self.fit_font(e["w"], 22, 12, avail))
        if self.pair["src"] == "de":
            self.w_lbl.setText(colorize_german(e["w"], "white"))
        else:
            self.w_lbl.setText(f"<span style='color:white'>{escape(e['w'])}</span>")
        self.x_lbl.setText(e["x"])
        self.x_lbl.setVisible(bool(e["x"]))
        self.m_lbl.setFont(self.fit_font(e["m"], 15, 11, avail))
        gold = "#ffd98a"
        if self.pair["dst"] == "de":
            self.m_lbl.setText(colorize_german(e["m"], gold))
        else:
            self.m_lbl.setText(f"<span style='color:{gold}'>{escape(e['m'])}</span>")
        self.type_lbl.setText(self.T["types"].get(e["t"], ""))
        s = self.ws(e)
        self.know_btn.setText(self.T["know"] + (f" ·{s['k']}" if s["k"] else ""))
        self.dont_btn.setText(self.T["dont"] + (f" ·{s['u']}" if s["u"] else ""))

    def paintEvent(self, ev):
        p, path = paint_card(self, self.bg_pix)
        if self.stack.currentIndex() == 0:   # countdown line
            frac = min(1.0, self.elapsed / max(1, self.st["interval"]))
            p.fillRect(QRectF(0, self.height() - 3, self.width(), 3), QColor(255, 255, 255, 25))
            p.fillRect(QRectF(0, self.height() - 3, self.width() * frac, 3),
                       QColor(255, 217, 138, 90 if self.hovering else 200))
        p.setClipping(False)
        p.setPen(QColor(255, 255, 255, 40))
        p.drawPath(path)

    # ------------------------------------------------------------ timer
    def on_tick(self):
        if self.stack.currentIndex() != 0 or self.hovering:
            return
        self.elapsed += 0.1
        if self.elapsed >= self.st["interval"]:
            self.next_word()
        else:
            self.update(0, self.height() - 4, self.width(), 4)

    def enterEvent(self, e):
        self.hovering = True     # pause while the mouse is over the card
        self.update()

    def leaveEvent(self, e):
        self.hovering = False
        self.update()

    # ------------------------------------------------------------ dragging
    def mousePressEvent(self, e):
        if e.button() != Qt.MouseButton.LeftButton or self.st["pinned"]:
            return
        h = self.windowHandle()
        if h is not None and h.startSystemMove():
            return
        self._drag = e.globalPosition().toPoint() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, e):
        if self._drag is not None and not self.st["pinned"]:
            self.move(e.globalPosition().toPoint() - self._drag)

    def mouseReleaseEvent(self, e):
        self._drag = None

    def moveEvent(self, e):
        self.save_timer.start(800)

    def toggle_pin(self):
        self.st["pinned"] = not self.st["pinned"]
        self.refresh_chrome()
        self.save_state()

    # ------------------------------------------------------------ right-click menu
    def contextMenuEvent(self, e):
        T = self.T
        m = QMenu(self)
        if len(self.words) > 1:
            mm = m.addMenu(T["m_mode"])
            for k in self.words:
                a = mm.addAction(T["modes"][k])
                a.setCheckable(True)
                a.setChecked(k == self.mode())
                a.triggered.connect(lambda _=False, x=k: self.switch_mode(x))
        lv = m.addMenu(T["m_level"])
        for l in self.levels[self.mode()]:
            a = lv.addAction(l)
            a.setCheckable(True)
            a.setChecked(l == self.level())
            a.triggered.connect(lambda _=False, x=l: self.set_level(self.mode(), x))
        sm = m.addMenu(T["m_interval"])
        grp = QActionGroup(sm)
        for s in (10, 15, 20, 30, 45, 60):
            a = sm.addAction(T["sec"].format(s))
            a.setCheckable(True)
            a.setChecked(self.st["interval"] == s)
            grp.addAction(a)
            a.triggered.connect(lambda _=False, x=s: self.set_interval(x))
        m.addSeparator()
        a = m.addAction(T["m_lock"])
        a.setCheckable(True)
        a.setChecked(self.st["pinned"])
        a.triggered.connect(self.toggle_pin)
        a = m.addAction(T["m_top"])
        a.setCheckable(True)
        a.setChecked(self.st["on_top"])
        a.triggered.connect(self.toggle_on_top)
        if sys.platform == "win32":
            a = m.addAction(T["m_auto"])
            a.setCheckable(True)
            a.setChecked(win_autostart())
            a.triggered.connect(win_autostart)
        m.addSeparator()
        m.addAction(T["m_bg"], self.choose_bg)
        if self.st.get("bg"):
            m.addAction(T["m_bg_reset"], self.reset_bg)
        m.addAction(T["m_reset"], self.reset_progress)
        m.addSeparator()
        if self.controller:
            m.addAction("🌐 " + T["m_lang"], lambda: self.controller.change_language(self))
        m.addAction(T["m_close"], self.quit_app)
        m.exec(e.globalPos())

    def switch_mode(self, k):
        lv = self.st["levels"].get(k)
        if lv in self.levels[k]:
            self.set_level(k, lv)
        else:
            self.pick_mode(k)
            self.stack.setCurrentIndex(1)
            self.update()

    def set_interval(self, s):
        self.st["interval"] = s
        self.elapsed = min(self.elapsed, s - 0.5)
        self.save_state()

    def toggle_on_top(self):
        self.st["on_top"] = not self.st["on_top"]
        pos = self.pos()
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, self.st["on_top"])
        self.show()
        self.move(pos)
        self.save_state()

    def load_bg(self):
        path = self.st.get("bg")
        self.bg_pix = QPixmap(path) if path and os.path.exists(path) else None

    def choose_bg(self):
        path, _ = QFileDialog.getOpenFileName(
            self, self.T["m_bg"], os.path.expanduser("~"),
            f"{self.T['images']} (*.png *.jpg *.jpeg *.webp *.bmp)")
        if path:
            self.st["bg"] = path
            self.load_bg()
            self.save_state()
            self.update()

    def reset_bg(self):
        self.st["bg"] = None
        self.bg_pix = None
        self.save_state()
        self.update()

    def reset_progress(self):
        self.st["words"] = {}
        self.st["today"] = {"date": "", "k": 0, "u": 0}
        self.soon.clear()
        self.save_state()
        self.refresh_chrome()
        if self.cur:
            self.render_word()

    def quit_app(self):
        self.save_state()
        QApplication.instance().quit()

    def closeEvent(self, e):
        self.save_state()
        if not (self.controller and self.controller.switching):
            QApplication.instance().quit()
        super().closeEvent(e)


# --------------------------------------------------------------------------- Windows
WIN_RUN_KEY = r"Software\Microsoft\Windows\CurrentVersion\Run"


def win_autostart(enable=None):
    """Read (enable=None) or set the 'start with Windows' entry for the current user."""
    import winreg
    if getattr(sys, "frozen", False):
        cmd = f'"{sys.executable}"'
    else:
        pyw = os.path.join(os.path.dirname(sys.executable), "pythonw.exe")
        cmd = f'"{pyw if os.path.exists(pyw) else sys.executable}" "{os.path.abspath(__file__)}"'
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, WIN_RUN_KEY, 0,
                        winreg.KEY_READ | winreg.KEY_SET_VALUE) as k:
        if enable is None:
            try:
                winreg.QueryValueEx(k, "WordFlow")
                return True
            except FileNotFoundError:
                return False
        if enable:
            winreg.SetValueEx(k, "WordFlow", 0, winreg.REG_SZ, cmd)
        else:
            try:
                winreg.DeleteValue(k, "WordFlow")
            except FileNotFoundError:
                pass
        return enable


def resource(name):
    """Path of a bundled file, also inside a PyInstaller one-file exe."""
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, name)


# --------------------------------------------------------------------------- first start
APP_CONFIG = os.path.join(CONFIG_ROOT, "word-flow", "app.json")
QUESTION_ALL = [("Hangi dili konuşuyorsunuz?", 14), ("Which language do you speak?", 11),
                ("Welche Sprache sprechen Sie?", 11), ("На каком языке вы говорите?", 11)]
NATIVE_NAMES = [("tr", "Türkçe"), ("en", "English"), ("de", "Deutsch"), ("ru", "Русский")]


def default_pos():
    scr = QApplication.primaryScreen().availableGeometry()
    return QPoint(scr.right() - APP_W - 30, scr.top() + 60)


class Onboarding(QWidget):
    """Step 1: which language do you speak (asked in all four languages).
    Step 2: which of the other three do you want to learn (asked in your language)."""

    def __init__(self, controller, pos):
        super().__init__()
        self.controller = controller
        self.native = None
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Tool
                            | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setFixedSize(APP_W, APP_H)
        self.setWindowTitle("Word Flow")
        self.stack = QStackedWidget(self)
        self.stack.setGeometry(0, 0, APP_W, APP_H)
        self.stack.addWidget(self.build_step1())
        self.step2 = QWidget()
        self.stack.addWidget(self.step2)
        self.move(pos)

    def build_step1(self):
        page = QWidget()
        v = QVBoxLayout(page)
        v.setContentsMargins(16, 16, 16, 16)
        v.setSpacing(2)
        v.addStretch(1)
        for text, size in QUESTION_ALL:
            l = QLabel(text)
            l.setAlignment(Qt.AlignmentFlag.AlignCenter)
            l.setStyleSheet(f"color:{'white' if size > 12 else 'rgba(255,255,255,0.7)'};"
                            f"font-size:{size}px;font-weight:{700 if size > 12 else 500};")
            v.addWidget(l)
        v.addSpacing(12)
        row = QHBoxLayout()
        row.setSpacing(6)
        for code, name in NATIVE_NAMES:
            b = QPushButton(name)
            b.setCursor(Qt.CursorShape.PointingHandCursor)
            b.setMinimumHeight(34)
            b.setStyleSheet(btn_css("rgba(140,120,255,0.55)", "rgba(140,120,255,0.9)"))
            b.clicked.connect(lambda _=False, c=code: self.pick_native(c))
            row.addWidget(b)
        v.addLayout(row)
        v.addStretch(1)
        return page

    def pick_native(self, code):
        self.native = code
        T = UI[code]
        old = self.step2
        page = QWidget()
        v = QVBoxLayout(page)
        v.setContentsMargins(16, 11, 16, 16)
        v.setSpacing(4)
        top = QHBoxLayout()
        back = QPushButton(T["back"])
        back.setStyleSheet(CHIP_CSS)
        back.setCursor(Qt.CursorShape.PointingHandCursor)
        back.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        top.addWidget(back)
        top.addStretch(1)
        v.addLayout(top)
        v.addStretch(1)
        q = QLabel(T["learn_q"])
        q.setAlignment(Qt.AlignmentFlag.AlignCenter)
        q.setWordWrap(True)
        q.setStyleSheet("color:white;font-size:15px;font-weight:700;")
        v.addWidget(q)
        h = QLabel(T["learn_hint"])
        h.setAlignment(Qt.AlignmentFlag.AlignCenter)
        h.setWordWrap(True)
        h.setStyleSheet("color:rgba(255,255,255,0.6);font-size:10px;")
        v.addWidget(h)
        v.addSpacing(8)
        row = QHBoxLayout()
        row.setSpacing(8)
        for target in [c for c, _ in NATIVE_NAMES if c != code]:
            b = QPushButton(T["langs"][target])
            b.setCursor(Qt.CursorShape.PointingHandCursor)
            b.setMinimumHeight(36)
            b.setStyleSheet(btn_css("rgba(140,120,255,0.55)", "rgba(140,120,255,0.9)"))
            b.clicked.connect(lambda _=False, t=target: self.controller.chosen(self, code, t))
            row.addWidget(b)
        v.addLayout(row)
        v.addStretch(1)
        self.stack.removeWidget(old)
        old.deleteLater()
        self.step2 = page
        self.stack.addWidget(page)
        self.stack.setCurrentWidget(page)

    def paintEvent(self, ev):
        p, path = paint_card(self, None)
        p.setClipping(False)
        p.setPen(QColor(255, 255, 255, 40))
        p.drawPath(path)

    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            h = self.windowHandle()
            if h is not None:
                h.startSystemMove()

    def closeEvent(self, e):
        if not self.controller.switching:
            QApplication.instance().quit()
        super().closeEvent(e)


class Controller:
    """Keeps exactly one card on screen and switches between pairs."""

    def __init__(self):
        self.win = None
        self.switching = False

    def load(self):
        try:
            with open(APP_CONFIG, encoding="utf-8") as f:
                c = json.load(f)
            return PAIR_FOR.get((c.get("native"), c.get("target")))
        except Exception:
            return None

    def save(self, native, target):
        os.makedirs(os.path.dirname(APP_CONFIG), exist_ok=True)
        with open(APP_CONFIG, "w", encoding="utf-8") as f:
            json.dump({"native": native, "target": target}, f)

    def start(self, pair=None):
        pair = pair or self.load()
        if pair:
            self.open_pair(pair)
        else:
            self.show(Onboarding(self, default_pos()))

    def show(self, w):
        old, self.win = self.win, w
        w.show()
        if old is not None:
            self.switching = True
            old.close()
            old.deleteLater()
            self.switching = False

    def open_pair(self, pair, pos=None):
        self.show(WordWidget(pair, self, pos))

    def chosen(self, onboarding, native, target):
        self.save(native, target)
        self.open_pair(PAIR_FOR[(native, target)], onboarding.pos())

    def change_language(self, widget):
        widget.save_state()
        self.show(Onboarding(self, widget.pos()))


def main():
    ap = argparse.ArgumentParser(description="Word Flow — tiny vocabulary widget")
    ap.add_argument("pair", nargs="?", choices=list(PAIRS),
                    help="open one language pair directly (word → meaning); "
                         "without it Word Flow asks for your languages on first start")
    args = ap.parse_args()
    app = QApplication(sys.argv[:1])
    app.setApplicationName("Word Flow")
    if os.path.exists(resource("icon.png")):
        from PyQt6.QtGui import QIcon
        app.setWindowIcon(QIcon(resource("icon.png")))
    if sys.platform == "win32":
        try:  # own taskbar identity instead of python.exe
            import ctypes
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("canyorg.WordFlow")
        except Exception:
            pass
    app.setQuitOnLastWindowClosed(False)
    ctl = Controller()
    ctl.start(args.pair)
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
