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

import shutil
import subprocess
from PyQt6.QtCore import Qt, QTimer, QRectF, QPoint, QLocale
from PyQt6.QtGui import (QPainter, QColor, QLinearGradient, QRadialGradient,
                         QPainterPath, QPixmap, QFont, QFontMetrics,
                         QActionGroup, QIcon, QPen)
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                             QVBoxLayout, QHBoxLayout, QGridLayout,
                             QStackedWidget, QMenu, QFileDialog, QSizePolicy,
                             QDialog, QTabWidget, QTableWidget, QTableWidgetItem,
                             QHeaderView, QAbstractItemView, QMessageBox,
                             QProgressBar)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wordlists import german, english, russian  # noqa: E402

APP_W, APP_H = 340, 196
CONFIG_ROOT = os.path.join(os.path.expanduser("~"), ".config")

# --------------------------------------------------------------------------- UI text
UI = {
    "tr": {
        "rate_tip": "Ne kadar biliyorsun? 1 = hiç, 9 = neredeyse. 10 = tam biliyorum, bir daha gösterme",
        "rate_10": "10 = tam biliyorum — bir daha gösterme (Rapor → Öğrendiklerim'den geri getirilebilir)",
        "stats_tip": "Bugün puanlanan · öğrenilen (bu modda)",
        "all_learned": "Bu seviyedeki tüm kelimeleri öğrendin 🎉",
        "all_learned2": "Seviyeyi yükselt ya da Rapor → Öğrendiklerim'den kelime geri getir",
        "m_report": "📊 Rapor ve öğrendiklerim…",
        "r_title": "Word Flow — Rapor",
        "r_summary": "Özet",
        "r_words": "Puanladıklarım",
        "r_learned": "Öğrendiklerim",
        "r_level": "Seviye",
        "r_total": "Kelime",
        "r_seen": "Puanlanan",
        "r_learned_n": "Öğrenilen",
        "r_avg": "Ort. puan",
        "r_progress": "İlerleme",
        "r_all": "Toplam",
        "r_ratings": "Toplam puanlama",
        "r_dist": "Puan dağılımı (son puanlar)",
        "r_week": "Son 7 gün",
        "r_word": "Kelime",
        "r_meaning": "Anlam",
        "r_count": "Kaç kez",
        "r_last": "Son",
        "r_hist": "Geçmiş",
        "r_date": "Tarih",
        "r_restore": "Seçilenleri geri getir",
        "r_restore_tip": "Kelime tekrar gösterilmeye başlar",
        "r_none": "Henüz yok",
        "r_mode": "Mod",
        "r_close": "Kapat",
        "reset_q": "Bu dil yönündeki tüm puanlar ve öğrenilen kelimeler silinsin mi?",
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
        "m_hide": "Anlamı gizle",
        "hide_off": "Kapalı (anlam hep açık)",
        "hide_after": "{} saniye sonra göster",
        "hide_hover": "Sadece üzerine gelince / tıklayınca",
        "hidden_tip": "Önce kendin hatırla — üzerine gel ya da tıkla",
        "m_speak": "🔊 Sesli oku",
        "m_autospeak": "Yeni kelimeyi otomatik oku",
        "tip_speak": "Sesli oku",
        "tip_eye_show": "Anlamı göster",
        "tip_eye_hide": "Anlamı gizle",
        "no_voice": "Bu dil için sistemde ses bulunamadı.\nLinux: sudo dnf install espeak-ng  (Debian/Ubuntu: sudo apt install espeak-ng)\nWindows: Ayarlar → Saat ve dil → Konuşma → Ses ekle",
        "m_bg": "Arka plan resmi seç…", "m_bg_reset": "Varsayılan arka plan",
        "m_reset": "İlerlemeyi sıfırla", "m_close": "Kapat", "images": "Resimler",
        "m_lang": "Dili değiştir…", "learn_q": "Hangi dili öğrenmek istiyorsunuz?",
        "learn_hint": "Kelimeler bu dilde gelir, anlamı Türkçe yazar",
        "langs": {"tr": "Türkçe", "en": "İngilizce", "de": "Almanca", "ru": "Rusça"}, "back": "‹ Geri",
        "types": {"n": "İSİM", "v": "FİİL", "a": "SIFAT", "d": "ZARF",
                  "p": "KALIP", "w": "KELİME"},
    },
    "en": {
        "rate_tip": "How well do you know it? 1 = not at all, 9 = almost. 10 = I know it, don't show again",
        "rate_10": "10 = I know it — don't show again (bring it back from Report → Learned)",
        "stats_tip": "Rated today · learned (this mode)",
        "all_learned": "You've learned every word at this level 🎉",
        "all_learned2": "Pick a higher level or bring words back from Report → Learned",
        "m_report": "📊 Report and learned words…",
        "r_title": "Word Flow — Report",
        "r_summary": "Summary",
        "r_words": "Rated words",
        "r_learned": "Learned",
        "r_level": "Level",
        "r_total": "Words",
        "r_seen": "Rated",
        "r_learned_n": "Learned",
        "r_avg": "Avg. score",
        "r_progress": "Progress",
        "r_all": "Total",
        "r_ratings": "Ratings in total",
        "r_dist": "Score distribution (latest scores)",
        "r_week": "Last 7 days",
        "r_word": "Word",
        "r_meaning": "Meaning",
        "r_count": "Times",
        "r_last": "Last",
        "r_hist": "History",
        "r_date": "Date",
        "r_restore": "Bring selected back",
        "r_restore_tip": "The word will be shown again",
        "r_none": "Nothing yet",
        "r_mode": "Mode",
        "r_close": "Close",
        "reset_q": "Delete all scores and learned words for this language pair?",
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
        "m_hide": "Hide the meaning",
        "hide_off": "Off (meaning always shown)",
        "hide_after": "Show after {} seconds",
        "hide_hover": "Only on hover / click",
        "hidden_tip": "Try to recall it first — hover or click to reveal",
        "m_speak": "🔊 Read aloud",
        "m_autospeak": "Read new words aloud automatically",
        "tip_speak": "Read aloud",
        "tip_eye_show": "Show the meaning",
        "tip_eye_hide": "Hide the meaning",
        "no_voice": "No voice for this language was found on your system.\nLinux: sudo dnf install espeak-ng  (Debian/Ubuntu: sudo apt install espeak-ng)\nWindows: Settings → Time & language → Speech → Add voices",
        "m_bg": "Choose background image…", "m_bg_reset": "Default background",
        "m_reset": "Reset progress", "m_close": "Close", "images": "Images",
        "m_lang": "Change language…", "learn_q": "Which language do you want to learn?",
        "learn_hint": "Words appear in that language, with the meaning in English",
        "langs": {"tr": "Turkish", "en": "English", "de": "German", "ru": "Russian"}, "back": "‹ Back",
        "types": {"n": "NOUN", "v": "VERB", "a": "ADJECTIVE", "d": "ADVERB",
                  "p": "PHRASE", "w": "WORD"},
    },
    "de": {
        "rate_tip": "Wie gut kennst du es? 1 = gar nicht, 9 = fast. 10 = kann ich, nicht mehr zeigen",
        "rate_10": "10 = kann ich — nicht mehr zeigen (zurückholen unter Bericht → Gelernt)",
        "stats_tip": "Heute bewertet · gelernt (in diesem Modus)",
        "all_learned": "Du hast alle Wörter dieses Niveaus gelernt 🎉",
        "all_learned2": "Wähle ein höheres Niveau oder hol Wörter unter Bericht → Gelernt zurück",
        "m_report": "📊 Bericht und gelernte Wörter…",
        "r_title": "Word Flow — Bericht",
        "r_summary": "Übersicht",
        "r_words": "Bewertete Wörter",
        "r_learned": "Gelernt",
        "r_level": "Niveau",
        "r_total": "Wörter",
        "r_seen": "Bewertet",
        "r_learned_n": "Gelernt",
        "r_avg": "Ø Note",
        "r_progress": "Fortschritt",
        "r_all": "Gesamt",
        "r_ratings": "Bewertungen insgesamt",
        "r_dist": "Verteilung (letzte Bewertung)",
        "r_week": "Letzte 7 Tage",
        "r_word": "Wort",
        "r_meaning": "Bedeutung",
        "r_count": "Mal",
        "r_last": "Zuletzt",
        "r_hist": "Verlauf",
        "r_date": "Datum",
        "r_restore": "Ausgewählte zurückholen",
        "r_restore_tip": "Das Wort wird wieder angezeigt",
        "r_none": "Noch nichts",
        "r_mode": "Modus",
        "r_close": "Schließen",
        "reset_q": "Alle Bewertungen und gelernten Wörter dieses Sprachpaars löschen?",
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
        "m_hide": "Bedeutung verbergen",
        "hide_off": "Aus (Bedeutung immer sichtbar)",
        "hide_after": "Nach {} Sekunden zeigen",
        "hide_hover": "Nur beim Überfahren / Klicken",
        "hidden_tip": "Erst selbst erinnern — überfahren oder klicken",
        "m_speak": "🔊 Vorlesen",
        "m_autospeak": "Neue Wörter automatisch vorlesen",
        "tip_speak": "Vorlesen",
        "tip_eye_show": "Bedeutung zeigen",
        "tip_eye_hide": "Bedeutung verbergen",
        "no_voice": "Für diese Sprache wurde keine Stimme gefunden.\nLinux: sudo dnf install espeak-ng  (Debian/Ubuntu: sudo apt install espeak-ng)\nWindows: Einstellungen → Zeit und Sprache → Sprache → Stimmen hinzufügen",
        "m_bg": "Hintergrundbild wählen…", "m_bg_reset": "Standard-Hintergrund",
        "m_reset": "Fortschritt zurücksetzen", "m_close": "Schließen", "images": "Bilder",
        "m_lang": "Sprache ändern…", "learn_q": "Welche Sprache möchten Sie lernen?",
        "learn_hint": "Die Wörter erscheinen in dieser Sprache, die Bedeutung auf Deutsch",
        "langs": {"tr": "Türkisch", "en": "Englisch", "de": "Deutsch", "ru": "Russisch"}, "back": "‹ Zurück",
        "types": {"n": "NOMEN", "v": "VERB", "a": "ADJEKTIV", "d": "ADVERB",
                  "p": "WENDUNG", "w": "WORT"},
    },
    "ru": {
        "rate_tip": "Насколько хорошо вы знаете слово? 1 = совсем нет, 9 = почти. 10 = знаю, больше не показывать",
        "rate_10": "10 = знаю — больше не показывать (вернуть: Отчёт → Выученные)",
        "stats_tip": "Оценено сегодня · выучено (в этом режиме)",
        "all_learned": "Вы выучили все слова этого уровня 🎉",
        "all_learned2": "Выберите уровень выше или верните слова: Отчёт → Выученные",
        "m_report": "📊 Отчёт и выученные слова…",
        "r_title": "Word Flow — Отчёт",
        "r_summary": "Сводка",
        "r_words": "Оценённые слова",
        "r_learned": "Выученные",
        "r_level": "Уровень",
        "r_total": "Слов",
        "r_seen": "Оценено",
        "r_learned_n": "Выучено",
        "r_avg": "Ср. оценка",
        "r_progress": "Прогресс",
        "r_all": "Всего",
        "r_ratings": "Всего оценок",
        "r_dist": "Распределение (последние оценки)",
        "r_week": "Последние 7 дней",
        "r_word": "Слово",
        "r_meaning": "Значение",
        "r_count": "Раз",
        "r_last": "Последняя",
        "r_hist": "История",
        "r_date": "Дата",
        "r_restore": "Вернуть выбранные",
        "r_restore_tip": "Слово снова начнёт показываться",
        "r_none": "Пока ничего",
        "r_mode": "Режим",
        "r_close": "Закрыть",
        "reset_q": "Удалить все оценки и выученные слова для этой языковой пары?",
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
        "m_hide": "Скрывать значение",
        "hide_off": "Выкл. (значение видно всегда)",
        "hide_after": "Показать через {} секунд",
        "hide_hover": "Только при наведении / щелчке",
        "hidden_tip": "Сначала вспомните сами — наведите курсор или щёлкните",
        "m_speak": "🔊 Прочитать вслух",
        "m_autospeak": "Автоматически читать новые слова",
        "tip_speak": "Прочитать вслух",
        "tip_eye_show": "Показать значение",
        "tip_eye_hide": "Скрыть значение",
        "no_voice": "Голос для этого языка в системе не найден.\nLinux: sudo dnf install espeak-ng  (Debian/Ubuntu: sudo apt install espeak-ng)\nWindows: Параметры → Время и язык → Речь → Добавить голоса",
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


EN_RU_DAILY = {**russian.EN_RU, **getattr(russian, "EN_RU_DAILY", {})}
DE_RU_GENERAL = {**russian.DE_RU, **getattr(russian, "DE_RU_GENERAL", {})}


def en_ru(mode):
    """Russian meanings; everyday words can differ from the academic/cyber sense."""
    return EN_RU_DAILY if mode == "daily" else russian.EN_RU


def de_ru(mode):
    return DE_RU_GENERAL if mode == "general" else russian.DE_RU


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
    "de-tr": {"title": "Word Flow · DE → TR", "ui": "tr", "src": "de", "dst": "tr",
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
              "modes": {m: parse_block(r, m, to_ru(en_ru(m))) for m, r in
                        (("daily", english.DAILY), ("academic", english.ACADEMIC),
                         ("cyber", english.CYBER))}},
    "de-ru": {"title": "Word Flow · DE → RU", "ui": "ru", "src": "de", "dst": "ru",
              "state": "word-flow-de-ru",
              "modes": {m: parse_block(r, m, to_ru(de_ru(m))) for m, r in
                        (("general", german.GERMAN), ("academic", german.GERMAN_ACADEMIC),
                         ("cyber", german.GERMAN_CYBER))}},
    "tr-ru": {"title": "Word Flow · TR → RU", "ui": "ru", "src": "tr", "dst": "ru",
              "state": "word-flow-tr-ru",
              "modes": {m: parse_reverse(r, m, lambda w, t=en_ru(m): t.get(w, w)) for m, r in
                        (("daily", english.DAILY), ("academic", english.ACADEMIC),
                         ("cyber", english.CYBER))}},
    "ru-tr": {"title": "Word Flow · RU → TR", "ui": "tr", "src": "ru", "dst": "tr",
              "state": "word-flow-ru-tr",
              "modes": {m: parse_ru(r, m, en_ru(m), lambda w, tr: tr) for m, r in
                        (("daily", english.DAILY), ("academic", english.ACADEMIC),
                         ("cyber", english.CYBER))}},
    "ru-en": {"title": "Word Flow · RU → EN", "ui": "en", "src": "ru", "dst": "en",
              "state": "word-flow-ru-en",
              "modes": {m: parse_ru(r, m, en_ru(m), lambda w, tr: w) for m, r in
                        (("daily", english.DAILY), ("academic", english.ACADEMIC),
                         ("cyber", english.CYBER))}},
    "ru-de": {"title": "Word Flow · RU → DE", "ui": "de", "src": "ru", "dst": "de",
              "state": "word-flow-ru-de",
              "modes": {m: parse_ru(r, m, de_ru(m), lambda w, tr: w) for m, r in
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


class Speaker:
    """Offline text-to-speech. Uses Qt's speech engine (speech-dispatcher on Linux,
    the system voices on Windows); on Linux falls back to espeak-ng / spd-say."""
    LOCALES = {"de": QLocale.Language.German, "en": QLocale.Language.English,
               "tr": QLocale.Language.Turkish, "ru": QLocale.Language.Russian}
    MAIN = {"de": "Germany", "en": "UnitedKingdom", "tr": "Turkey", "ru": "Russia"}

    def __init__(self):
        self.tts = None
        try:
            from PyQt6.QtTextToSpeech import QTextToSpeech
            engines = [e for e in QTextToSpeech.availableEngines() if e != "mock"]
            pref = [e for e in ("winrt", "sapi", "speechd", "flite") if e in engines]
            for eng in pref or engines:
                t = QTextToSpeech(eng)
                if t.engine() and t.state() != QTextToSpeech.State.Error:
                    self.tts = t
                    break
        except Exception:
            self.tts = None

    @staticmethod
    def clean(text):
        text = re.sub(r"\(.*?\)|\[.*?\]", "", text)
        text = re.sub(r"\b(sth|sb|etw\.|jdn\.|jdm\.)(?=\W|$)|…", "", text)
        return text.split(";")[0].replace("/", ",").strip(" ,")

    def qt_say(self, text, lang):
        if self.tts is None:
            return False
        want = self.LOCALES[lang]
        voices = [v for v in self.tts.allVoices(QLocale(want))] \
            if hasattr(self.tts, "allVoices") else []
        locs = [l for l in self.tts.availableLocales() if l.language() == want]
        if not locs and not voices:
            return False
        if locs:
            locs.sort(key=lambda l: QLocale.territoryToString(l.territory()).replace(" ", "")
                      != self.MAIN[lang])
            self.tts.setLocale(locs[0])
        own = [v for v in self.tts.availableVoices() if v.locale().language() == want]
        if own:
            self.tts.setVoice(own[0])
        elif voices:
            self.tts.setVoice(voices[0])
        elif self.tts.engine() != "speechd":
            return False
        self.tts.stop()
        self.tts.say(text)
        return True

    @staticmethod
    def cmd_say(text, lang):
        if not sys.platform.startswith("linux"):
            return False
        for cmd in (["espeak-ng", "-v", lang, "--", text],
                    ["spd-say", "-l", lang, "--", text], ["espeak", "-v", lang, text]):
            if shutil.which(cmd[0]):
                try:
                    subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    return True
                except Exception:
                    pass
        return False

    def say(self, text, lang):
        text = self.clean(text)
        if not text:
            return True
        try:
            if self.qt_say(text, lang):
                return True
        except Exception:
            pass
        return self.cmd_say(text, lang)


SPEAKER = None


def speaker():
    global SPEAKER
    if SPEAKER is None:
        SPEAKER = Speaker()
    return SPEAKER


def score_color(n):
    """1 = red … 9 = green-ish, 10 = gold (learned)."""
    if n == 10:
        return (214, 170, 60)
    t = (n - 1) / 8
    return (int(220 - 150 * t), int(80 + 100 * t), int(100 - 10 * t))


def score_css(n, outlined):
    if n is None:
        bg, hv = "rgba(255,255,255,0.14)", "rgba(255,255,255,0.28)"
    else:
        r, g, b = score_color(n)
        bg, hv = f"rgba({r},{g},{b},0.45)", f"rgba({r},{g},{b},0.9)"
    border = "2px solid rgba(255,255,255,0.95)" if outlined else "none"
    return ("QPushButton{color:white;background:%s;border:%s;border-radius:7px;"
            "padding:0px;font-size:11px;font-weight:700;}"
            "QPushButton:hover{background:%s;}"
            "QPushButton:disabled{color:rgba(255,255,255,0.3);"
            "background:rgba(255,255,255,0.06);}" % (bg, border, hv))


DIALOG_CSS = """
QDialog, QTabWidget::pane, QTableWidget, QLabel {background:#1d1a2e; color:#ece9ff;}
QTabWidget::pane {border:1px solid #3a3558; border-radius:8px; top:-1px;}
QTabBar::tab {background:#2a2640; color:#cfc9f0; padding:7px 16px; margin-right:3px;
              border-top-left-radius:8px; border-top-right-radius:8px;}
QTabBar::tab:selected {background:#5b4fc4; color:white;}
QTableWidget {gridline-color:#3a3558; border:none; alternate-background-color:#242038;
              selection-background-color:#5b4fc4;}
QHeaderView::section {background:#2a2640; color:#cfc9f0; border:none; padding:5px;
                      font-weight:600;}
QPushButton {background:#5b4fc4; color:white; border:none; border-radius:8px;
             padding:7px 14px; font-weight:600;}
QPushButton:hover {background:#7466e0;}
QPushButton:disabled {background:#3a3558; color:#8c86ad;}
"""


class DistChart(QWidget):
    """Bar chart of the latest score of every rated word (1–10)."""
    def __init__(self):
        super().__init__()
        self.counts = [0] * 11
        self.setMinimumHeight(110)

    def set_counts(self, counts):
        self.counts = counts
        self.update()

    def paintEvent(self, ev):
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        w, h = self.width(), self.height()
        slot = w / 10
        bw = min(34.0, slot * 0.62)
        mx = max(self.counts[1:]) or 1
        top, bottom = 16, h - 18
        f = QFont(self.font())
        f.setPointSizeF(8.5)
        p.setFont(f)
        for n in range(1, 11):
            x = (n - 1) * slot + (slot - bw) / 2
            bh = (bottom - top) * self.counts[n] / mx
            p.setPen(Qt.PenStyle.NoPen)
            p.setBrush(QColor(255, 255, 255, 18))
            p.drawRoundedRect(QRectF(x, top, bw, bottom - top), 4, 4)
            p.setBrush(QColor(*score_color(n)))
            if bh > 0:
                p.drawRoundedRect(QRectF(x, bottom - bh, bw, bh), 4, 4)
            p.setPen(QColor("#cfc9f0"))
            p.drawText(QRectF(x - 10, bottom - bh - 15, bw + 20, 14),
                       Qt.AlignmentFlag.AlignCenter, str(self.counts[n]))
            p.setPen(QColor("white"))
            p.drawText(QRectF(x - 10, bottom + 2, bw + 20, 14),
                       Qt.AlignmentFlag.AlignCenter, str(n))
        p.end()


class SortItem(QTableWidgetItem):
    """Table cell that sorts by a hidden value (dates, scores) instead of its text."""
    def __lt__(self, other):
        a = self.data(Qt.ItemDataRole.UserRole + 1)
        b = other.data(Qt.ItemDataRole.UserRole + 1)
        if a is not None and b is not None:
            return a < b
        return super().__lt__(other)


class ReportDialog(QDialog):
    """Right-click → Report: progress per level, every rating, and the learned list
    (words scored 10) from which words can be brought back."""

    def __init__(self, ww):
        super().__init__(None)
        self.ww = ww
        T = ww.T
        self.setWindowTitle(f"{T['r_title']} · {ww.pair['title'].split('·')[-1].strip()}")
        self.resize(690, 560)
        self.setStyleSheet(DIALOG_CSS)
        v = QVBoxLayout(self)
        self.tabs = QTabWidget()
        v.addWidget(self.tabs)

        # summary
        page = QWidget()
        pv = QVBoxLayout(page)
        self.head = QLabel()
        self.head.setWordWrap(True)
        self.head.setTextFormat(Qt.TextFormat.RichText)
        pv.addWidget(self.head)
        self.lv_table = self.table([T["r_level"], T["r_total"], T["r_seen"],
                                    T["r_learned_n"], T["r_avg"], T["r_progress"]])
        pv.addWidget(self.lv_table, 1)
        self.dist_lbl = QLabel(T["r_dist"])
        self.dist_lbl.setStyleSheet("color:#cfc9f0;")
        pv.addWidget(self.dist_lbl)
        self.dist = DistChart()
        pv.addWidget(self.dist)
        self.tabs.addTab(page, T["r_summary"])

        # rated words
        self.w_table = self.table([T["r_word"], T["r_meaning"], T["r_level"], T["r_count"],
                                   T["r_last"], T["r_avg"], T["r_hist"], T["r_date"]])
        self.w_table.setSortingEnabled(True)
        self.w_table.horizontalHeader().setSortIndicator(7, Qt.SortOrder.DescendingOrder)
        self.tabs.addTab(self.w_table, T["r_words"])

        # learned
        page = QWidget()
        lv = QVBoxLayout(page)
        self.l_table = self.table([T["r_word"], T["r_meaning"], T["r_level"], T["r_date"]])
        self.l_table.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.l_table.setSortingEnabled(True)
        self.l_table.horizontalHeader().setSortIndicator(3, Qt.SortOrder.DescendingOrder)
        lv.addWidget(self.l_table, 1)
        self.restore_btn = QPushButton("↩ " + T["r_restore"])
        self.restore_btn.setToolTip(T["r_restore_tip"])
        self.restore_btn.clicked.connect(self.do_restore)
        self.l_table.itemSelectionChanged.connect(
            lambda: self.restore_btn.setEnabled(bool(self.l_table.selectionModel().selectedRows())))
        lv.addWidget(self.restore_btn, 0, Qt.AlignmentFlag.AlignRight)
        self.tabs.addTab(page, T["r_learned"])

        close = QPushButton(T["r_close"])
        close.clicked.connect(self.close)
        v.addWidget(close, 0, Qt.AlignmentFlag.AlignRight)

    def table(self, cols):
        t = QTableWidget(0, len(cols))
        t.setHorizontalHeaderLabels(cols)
        t.verticalHeader().setVisible(False)
        t.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        t.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        t.setAlternatingRowColors(True)
        hh = t.horizontalHeader()
        hh.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        hh.setStretchLastSection(True)
        return t

    @staticmethod
    def item(value, sort=None):
        it = SortItem()
        it.setData(Qt.ItemDataRole.DisplayRole, value)
        if sort is not None:
            it.setData(Qt.ItemDataRole.UserRole + 1, sort)
        return it

    def fill(self, table, rows):
        sorting = table.isSortingEnabled()
        table.setSortingEnabled(False)
        table.setRowCount(len(rows))
        for r, row in enumerate(rows):
            for c, val in enumerate(row["cells"]):
                it = QTableWidgetItem() if not isinstance(val, QTableWidgetItem) else val
                if not isinstance(val, QTableWidgetItem):
                    it.setData(Qt.ItemDataRole.DisplayRole, val)
                if c == 0:
                    it.setData(Qt.ItemDataRole.UserRole, row.get("key"))
                table.setItem(r, c, it)
        table.setSortingEnabled(sorting)

    def refresh(self):
        ww, T = self.ww, self.ww.T
        mode = ww.mode()
        recs = {k: v for k, v in ww.st["words"].items() if k.startswith(mode + ":") and v["h"]}
        fmt = lambda ts: datetime.datetime.fromtimestamp(ts).strftime("%d.%m.%Y")

        # per level
        rows, tot = [], [0, 0, 0, []]
        for lv in ww.levels[mode]:
            keys = [e["key"] for e in ww.words[mode][lv]]
            seen = [recs[k] for k in keys if k in recs]
            learned = sum(1 for r in seen if r.get("learned"))
            lasts = [r["h"][-1][1] for r in seen]
            avg = round(sum(lasts) / len(lasts), 1) if lasts else ""
            pct = round(100 * learned / len(keys)) if keys else 0
            rows.append({"cells": [lv, len(keys), len(seen), learned, avg, ""], "pct": pct})
            tot[0] += len(keys); tot[1] += len(seen); tot[2] += learned; tot[3] += lasts
        avg = round(sum(tot[3]) / len(tot[3]), 1) if tot[3] else ""
        pct = round(100 * tot[2] / tot[0]) if tot[0] else 0
        rows.append({"cells": [T["r_all"], tot[0], tot[1], tot[2], avg, ""], "pct": pct})
        self.fill(self.lv_table, rows)
        for r, row in enumerate(rows):
            bar = QProgressBar()
            bar.setRange(0, 100)
            bar.setValue(row["pct"])
            bar.setFormat("%p%")
            bar.setStyleSheet(
                "QProgressBar{background:#2a2640;border:none;border-radius:6px;color:white;"
                "text-align:center;font-size:11px;margin:5px 6px;}"
                "QProgressBar::chunk{border-radius:6px;background:qlineargradient("
                "x1:0,y1:0,x2:1,y2:0,stop:0 #6f5cf0,stop:1 #d6aa3c);}")
            self.lv_table.setCellWidget(r, 5, bar)

        n_ratings = sum(len(r["h"]) for r in recs.values())
        week = datetime.datetime.now().timestamp() - 7 * 86400
        n_week = sum(1 for r in recs.values() for ts, _ in r["h"] if ts >= week)
        self.head.setText(
            f"<b style='font-size:15px'>{escape(ww.pair['title'])}</b> &nbsp; "
            f"{T['r_mode']}: <b>{T['modes'][mode]}</b><br>"
            f"{T['r_ratings']}: <b>{n_ratings}</b> &nbsp;·&nbsp; {T['r_week']}: <b>{n_week}</b>"
            f" &nbsp;·&nbsp; {T['r_learned_n']}: <b>{tot[2]}</b>")
        counts = [0] * 11
        for r in recs.values():
            counts[r["h"][-1][1]] += 1
        self.dist.set_counts(counts)

        # rated words
        rows = []
        for k, r in recs.items():
            e = ww.index.get(k)
            if not e:
                continue
            sc = [x[1] for x in r["h"]]
            last = self.item(f"{sc[-1]}" + (" ★" if r.get("learned") else ""), sc[-1])
            rows.append({"key": k, "cells": [
                e["w"], e["m"], e["lv"], len(sc), last,
                round(sum(sc) / len(sc), 1), " ".join(map(str, sc[-12:])),
                self.item(fmt(r["h"][-1][0]), r["h"][-1][0])]})
        rows.sort(key=lambda x: -self._ts(x))
        self.fill(self.w_table, rows)

        # learned
        rows = []
        for k, r in recs.items():
            e = ww.index.get(k)
            if e and r.get("learned"):
                rows.append({"key": k, "cells": [e["w"], e["m"], e["lv"],
                                                 self.item(fmt(r["h"][-1][0]), r["h"][-1][0])]})
        self.fill(self.l_table, rows)
        self.tabs.setTabText(2, f"{T['r_learned']} ({len(rows)})")
        self.restore_btn.setEnabled(False)

    @staticmethod
    def _ts(row):
        it = row["cells"][-1]
        return it.data(Qt.ItemDataRole.UserRole + 1) or 0

    def do_restore(self):
        keys = [self.l_table.item(i.row(), 0).data(Qt.ItemDataRole.UserRole)
                for i in self.l_table.selectionModel().selectedRows()]
        self.ww.restore([k for k in keys if k])
        self.refresh()


def _icon(draw, size=18, color="white"):
    pm = QPixmap(size * 2, size * 2)
    pm.setDevicePixelRatio(2)
    pm.fill(Qt.GlobalColor.transparent)
    p = QPainter(pm)
    p.setRenderHint(QPainter.RenderHint.Antialiasing)
    pen = QPen(QColor(color))
    pen.setWidthF(1.6)
    pen.setCapStyle(Qt.PenCapStyle.RoundCap)
    pen.setJoinStyle(Qt.PenJoinStyle.RoundJoin)
    p.setPen(pen)
    draw(p, size)
    p.end()
    return QIcon(pm)


def eye_icon(crossed, color="white"):
    """Open eye = meaning visible, crossed-out eye = meaning hidden."""
    def draw(p, s):
        c = s / 2
        path = QPainterPath()
        path.moveTo(1.5, c)
        path.quadTo(c, c - 9, s - 1.5, c)
        path.quadTo(c, c + 9, 1.5, c)
        p.drawPath(path)
        p.drawEllipse(QRectF(c - 2.8, c - 2.8, 5.6, 5.6))
        if crossed:
            pen = p.pen()
            pen.setWidthF(1.8)
            p.setPen(pen)
            p.drawLine(QPoint(4, s - 3), QPoint(s - 4, 3))
    return _icon(draw, color=color)


def speaker_icon(color="white"):
    def draw(p, s):
        c = s / 2
        body = QPainterPath()
        body.moveTo(2, c - 2.5)
        body.lineTo(5, c - 2.5)
        body.lineTo(9, c - 6)
        body.lineTo(9, c + 6)
        body.lineTo(5, c + 2.5)
        body.lineTo(2, c + 2.5)
        body.closeSubpath()
        p.setBrush(QColor(color))
        p.drawPath(body)
        p.setBrush(Qt.BrushStyle.NoBrush)
        p.drawArc(QRectF(6, c - 3.5, 6, 7), -55 * 16, 110 * 16)
        p.drawArc(QRectF(6, c - 7, 10, 14), -55 * 16, 110 * 16)
    return _icon(draw, color=color)


SPEAK_W = 24
ICON_BTN_CSS = ("QPushButton{background:transparent;border:none;border-radius:11px;}"
                "QPushButton:hover{background:rgba(255,255,255,0.14);}"
                "QPushButton:pressed{background:rgba(255,255,255,0.24);}")


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
        self.index = {e["key"]: e for m in self.words.values()
                      for items in m.values() for e in items}
        self.report = None
        self.elapsed = 0.0
        self.hovering = False
        self.revealed = True
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
             "reveal": 0, "autospeak": False,
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
        # v2: 1–10 scale. Old ✓/✗ weights can't be mapped to a score, so they are dropped.
        d["words"] = {k: v for k, v in d["words"].items() if isinstance(v, dict) and "h" in v}
        if "n" not in d["today"]:
            d["today"] = {"date": "", "n": 0}
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

    def ws(self, key):
        """Per-word record: h = [[unix time, score 1–10], …], learned = scored 10."""
        return self.st["words"].get(key) or {"h": [], "learned": False}

    def is_learned(self, key):
        return self.st["words"].get(key, {}).get("learned", False)

    def today(self):
        t = self.st["today"]
        d = datetime.date.today().isoformat()
        if t.get("date") != d:
            t.update({"date": d, "n": 0})
        return t

    def learned_count(self):
        m = self.mode() + ":"
        return sum(1 for k, v in self.st["words"].items() if k.startswith(m) and v.get("learned"))

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
        self.level_btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.type_lbl = QLabel()
        self.type_lbl.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        self.type_lbl.setMinimumWidth(0)
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
        top.addWidget(self.type_lbl, 1)
        top.addWidget(self.stats_lbl)
        self.eye_btn = QPushButton()
        self.eye_btn.setFixedSize(26, 22)
        self.eye_btn.setStyleSheet(CHIP_CSS)
        self.eye_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.eye_btn.clicked.connect(self.toggle_hide)
        top.addWidget(self.eye_btn)
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
        for w in (self.x_lbl, self.m_lbl):
            w.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        self.speak_btn = QPushButton()
        self.speak_btn.setIcon(speaker_icon())
        self.speak_btn.setFixedSize(SPEAK_W, SPEAK_W)
        self.speak_btn.setStyleSheet(ICON_BTN_CSS)
        self.speak_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.speak_btn.setToolTip(self.T["tip_speak"])
        self.speak_btn.clicked.connect(self.speak)
        self.w_lbl.setWordWrap(True)
        self.w_lbl.setMaximumWidth(APP_W - 36 - 2 * (SPEAK_W + 4))
        wrow = QHBoxLayout()
        wrow.setSpacing(0)
        wrow.addStretch(1)
        wrow.addSpacing(SPEAK_W + 4)          # balances the button: word stays centred
        wrow.addWidget(self.w_lbl)
        wrow.addSpacing(4)
        wrow.addWidget(self.speak_btn, 0, Qt.AlignmentFlag.AlignVCenter)
        wrow.addStretch(1)
        v.addLayout(wrow)
        v.addWidget(self.x_lbl)
        v.addSpacing(3)
        v.addWidget(self.m_lbl)
        v.addStretch(1)

        row = QHBoxLayout()
        row.setSpacing(3)
        self.score_btns = []
        for n in range(1, 11):
            b = QPushButton(str(n))
            b.setFixedHeight(26)
            b.setMinimumWidth(10)
            b.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            b.setCursor(Qt.CursorShape.PointingHandCursor)
            b.setToolTip(self.T["rate_10"] if n == 10 else self.T["rate_tip"])
            b.clicked.connect(lambda _=False, x=n: self.rate(x))
            self.score_btns.append(b)
            row.addWidget(b, 1)
        self.skip_btn = QPushButton("›")
        self.skip_btn.setFixedSize(26, 26)
        self.skip_btn.setStyleSheet(score_css(None, False))
        self.skip_btn.setToolTip(self.T["next"])
        self.skip_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.skip_btn.clicked.connect(self.next_word)
        row.addWidget(self.skip_btn)
        v.addLayout(row)
        self.style_scores(None)
        return page

    def style_scores(self, last):
        for n, b in enumerate(self.score_btns, 1):
            b.setStyleSheet(score_css(n, n == last))

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
            self.recent.clear()
        self.show_card()

    def refresh_chrome(self):
        lvl = self.level()
        if len(self.words) > 1:
            self.level_btn.setText(f"{self.T['modes'][self.mode()]} · {lvl} ▾")
        else:
            self.level_btn.setText(f"{lvl} ▾")
        self.pin_btn.setText("📌" if self.st["pinned"] else "📍")
        self.update_eye()
        self.pin_btn.setToolTip(self.T["pin_on"] if self.st["pinned"] else self.T["pin_off"])
        t = self.today()
        self.stats_lbl.setText(f"✎{t['n']}  ★{self.learned_count()}")
        self.stats_lbl.setMinimumWidth(
            QFontMetrics(self.stats_lbl.font()).horizontalAdvance(self.stats_lbl.text()) + 8)
        self.stats_lbl.setToolTip(self.T["stats_tip"])

    # ------------------------------------------------------------ choosing words
    def pool(self):
        """Every word of the chosen level (and, less often, the levels below) that
        hasn't been scored 10. Scores 1–9 don't change how often a word comes up."""
        m = self.mode()
        lvls = self.levels[m]
        idx = lvls.index(self.level())
        items, weights = [], []
        for i, lv in enumerate(lvls[:idx + 1]):
            base = 1.0 if i == idx else (0.35 if i == idx - 1 else 0.12)
            for e in self.words[m][lv]:
                if not self.is_learned(e["key"]):
                    items.append(e)
                    weights.append(base)
        return items, weights

    def next_word(self):
        items, weights = self.pool()
        if not items:
            self.cur = None
            self.render_empty()
            return
        cand = [(it, w) for it, w in zip(items, weights) if it["key"] not in self.recent]
        if not cand:
            cand = list(zip(items, weights))
        e = random.choices([c[0] for c in cand], weights=[c[1] for c in cand])[0]
        self.cur = e
        self.recent = (self.recent + [e["key"]])[-min(8, len(items) - 1):] if len(items) > 1 else []
        self.elapsed = 0.0
        self.render_word()
        self.update()
        if self.st.get("autospeak") and self.isVisible():
            QTimer.singleShot(250, self.speak)

    def rate(self, score):
        if not self.cur:
            return
        key = self.cur["key"]
        rec = self.st["words"].setdefault(key, {"h": [], "learned": False})
        rec["h"].append([int(datetime.datetime.now().timestamp()), score])
        rec["h"] = rec["h"][-100:]
        rec["learned"] = score == 10
        self.today()["n"] += 1
        self.save_state()
        self.refresh_chrome()
        if self.report is not None:
            self.report.refresh()
        self.next_word()

    def restore(self, keys):
        for k in keys:
            if k in self.st["words"]:
                self.st["words"][k]["learned"] = False
        self.save_state()
        self.refresh_chrome()
        if self.cur is None and self.stack.currentIndex() == 0:
            self.next_word()

    def open_report(self):
        if self.report is None:
            self.report = ReportDialog(self)
        self.report.refresh()
        self.report.show()
        self.report.raise_()
        self.report.activateWindow()

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
        ww = avail - 2 * (SPEAK_W + 4)
        f = self.fit_font(e["w"], 22, 15, ww)
        if QFontMetrics(f).horizontalAdvance(e["w"]) > ww:     # long phrase: two lines
            f = self.fit_font(e["w"], 15, 10, ww * 1.6)
            self.w_lbl.setFixedWidth(ww)
        else:
            self.w_lbl.setMinimumWidth(0)
            self.w_lbl.setMaximumWidth(ww)
        self.w_lbl.setFont(f)
        if self.pair["src"] == "de":
            self.w_lbl.setText(colorize_german(e["w"], "white"))
        else:
            self.w_lbl.setText(f"<span style='color:white'>{escape(e['w'])}</span>")
        self.x_lbl.setText(e["x"])
        self.x_lbl.setVisible(bool(e["x"]))
        self.m_lbl.setFont(self.fit_font(e["m"], 15, 11, avail))
        self.revealed = not self.st.get("reveal")
        self.show_meaning()
        self.set_type(self.T["types"].get(e["t"], ""))
        h = self.ws(e["key"])["h"]
        self.style_scores(h[-1][1] if h else None)   # outline = your last score
        for b in self.score_btns:
            b.setEnabled(True)

    def show_meaning(self):
        e = self.cur
        if e is None:
            return
        gold = "#ffd98a"
        if not self.revealed:
            self.m_lbl.setText("<span style='color:rgba(255,217,138,0.45)'>• • •</span>")
            self.m_lbl.setToolTip(self.T["hidden_tip"])
        elif self.pair["dst"] == "de":
            self.m_lbl.setText(colorize_german(e["m"], gold))
            self.m_lbl.setToolTip("")
        else:
            self.m_lbl.setText(f"<span style='color:{gold}'>{escape(e['m'])}</span>")
            self.m_lbl.setToolTip("")

    def update_eye(self):
        hidden = bool(self.st.get("reveal"))
        self.eye_btn.setIcon(eye_icon(hidden))
        self.eye_btn.setToolTip(self.T["tip_eye_show"] if hidden else self.T["tip_eye_hide"])

    def toggle_hide(self):
        """Eye button: off ⇄ the last hide setting (default: until hover / click)."""
        r = self.st.get("reveal") or 0
        if r:
            self.st["reveal_last"] = r
            self.set_reveal(0)
        else:
            self.set_reveal(self.st.get("reveal_last") or -1)
            if self.cur is not None:      # hide the current meaning right away
                self.revealed = False
                self.show_meaning()

    def reveal(self):
        if not self.revealed and self.cur is not None:
            self.revealed = True
            self.show_meaning()

    def speak(self):
        if self.cur is None:
            return
        if not speaker().say(self.cur["w"], self.pair["src"]):
            self.st["autospeak"] = False
            self.save_state()
            QMessageBox.information(self, self.pair["title"], self.T["no_voice"])

    def set_type(self, text):
        """Word-type tag (NOUN, VERB …) — dropped when the top row has no room for it."""
        used = (self.level_btn.sizeHint().width() + self.stats_lbl.minimumWidth()
                + 26 * (3 if self.controller else 2) + 6 * 6)
        room = APP_W - 32 - used
        fits = QFontMetrics(self.type_lbl.font()).horizontalAdvance(text) + 12 <= room
        self.type_lbl.setText(text if fits else "")

    def render_empty(self):
        self.w_lbl.setFont(self.fit_font(self.T["all_learned"], 14, 9, APP_W - 36))
        self.w_lbl.setText(f"<span style='color:white'>{escape(self.T['all_learned'])}</span>")
        self.x_lbl.setVisible(False)
        f = QFont(self.font())
        f.setPointSizeF(9)
        self.m_lbl.setFont(f)
        self.m_lbl.setText(f"<span style='color:#ffd98a'>{escape(self.T['all_learned2'])}</span>")
        self.type_lbl.setText("")
        self.style_scores(None)
        for b in self.score_btns:
            b.setEnabled(False)
        self.update()

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
        r = self.st.get("reveal") or 0
        if not self.revealed and r > 0 and self.elapsed >= min(r, self.st["interval"] - 2):
            self.reveal()
        if self.elapsed >= self.st["interval"]:
            self.next_word()
        else:
            self.update(0, self.height() - 4, self.width(), 4)

    def enterEvent(self, e):
        self.hovering = True     # pause while the mouse is over the card
        self.reveal()
        self.update()

    def leaveEvent(self, e):
        self.hovering = False
        self.update()

    # ------------------------------------------------------------ dragging
    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.reveal()
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
        hm = m.addMenu(T["m_hide"])
        grp2 = QActionGroup(hm)
        for val, label in ((0, T["hide_off"]), (3, T["hide_after"].format(3)),
                           (5, T["hide_after"].format(5)), (8, T["hide_after"].format(8)),
                           (-1, T["hide_hover"])):
            a = hm.addAction(label)
            a.setCheckable(True)
            a.setChecked((self.st.get("reveal") or 0) == val)
            grp2.addAction(a)
            a.triggered.connect(lambda _=False, x=val: self.set_reveal(x))
        m.addSeparator()
        m.addAction(T["m_speak"], self.speak)
        a = m.addAction(T["m_autospeak"])
        a.setCheckable(True)
        a.setChecked(bool(self.st.get("autospeak")))
        a.triggered.connect(self.toggle_autospeak)
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
        m.addAction(T["m_report"], self.open_report)
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

    def set_reveal(self, v):
        self.st["reveal"] = v
        if v:
            self.st["reveal_last"] = v
        self.save_state()
        self.update_eye()
        if self.cur is not None:
            self.revealed = not v or (v > 0 and self.elapsed >= v)
            self.show_meaning()

    def toggle_autospeak(self):
        self.st["autospeak"] = not self.st.get("autospeak")
        self.save_state()
        if self.st["autospeak"]:
            self.speak()

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
        if QMessageBox.question(self, self.pair["title"], self.T["reset_q"]) \
                != QMessageBox.StandardButton.Yes:
            return
        self.st["words"] = {}
        self.st["today"] = {"date": "", "n": 0}
        self.save_state()
        self.refresh_chrome()
        if self.report is not None:
            self.report.refresh()
        self.next_word()

    def quit_app(self):
        self.save_state()
        if self.report is not None:
            self.report.close()
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
