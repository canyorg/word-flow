"""Write the word lists as Markdown tables into docs/wordlists/.

Run from the repository root:  python3 tools/make_wordlists.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
import wordflow as w  # noqa: E402
from wordlists import english, german  # noqa: E402

OUT = "docs/wordlists"
MAX = 380_000          # bytes per file; bigger lists are split by CEFR band

TYPES = {"n": "noun", "v": "verb", "a": "adj.", "d": "adv.", "p": "phrase", "w": "word"}

LISTS = [
    # file, title, raw data, mode, source column, columns: (header, lookup)
    ("english-everyday", "English · Everyday (A1.1 – C2.2)", english.DAILY, "daily", "English",
     lambda m: [("Türkçe", lambda wd, tr: tr),
                ("Deutsch", w.en_de(m)),
                ("Русский", w.to_ru(w.en_ru(m)))]),
    ("english-academic", "English · Academic (B1.1 – C2.2)", english.ACADEMIC, "academic",
     "English", None),
    ("english-cyber", "English · Cybersecurity (B1.1 – C2.2)", english.CYBER, "cyber",
     "English", None),
    ("german-general", "Deutsch · Allgemein (A1.1 – C2.2)", german.GERMAN, "general", "Deutsch",
     lambda m: [("Türkçe", lambda wd, tr: tr),
                ("English", w.de_en(german.DE_EN)),
                ("Русский", w.to_ru(w.de_ru(m)))]),
    ("german-academic", "Deutsch · Akademisch (B1.1 – C2.2)", german.GERMAN_ACADEMIC, "academic",
     "Deutsch", lambda m: [("Türkçe", lambda wd, tr: tr),
                           ("English", w.de_en(german.DE_EN_ACADEMIC)),
                           ("Русский", w.to_ru(w.de_ru(m)))]),
    ("german-cyber", "Deutsch · Cybersicherheit (B1.1 – C2.2)", german.GERMAN_CYBER, "cyber",
     "Deutsch", lambda m: [("Türkçe", lambda wd, tr: tr),
                           ("English", w.de_en(german.DE_EN_CYBER)),
                           ("Русский", w.to_ru(w.de_ru(m)))]),
]


def cell(s):
    return (s or "").replace("|", "\\|").strip()


def rows(raw, cols):
    out = {}
    for lv, block in raw.items():
        r = []
        for line in block.strip().splitlines():
            p = [x.strip() for x in line.split("|")]
            if len(p) < 3:
                continue
            r.append([p[1], TYPES.get(p[0], "")] + [f(p[1], p[2]) for _, f in cols])
        out[lv] = r
    return out


def table(src, cols, lv, items):
    head = ["#", src, "Type", *[h for h, _ in cols]]
    s = [f"### {lv}", "", f"{len(items)} words", "",
         "| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    s += [f"| {i} | " + " | ".join(cell(x) for x in r) + " |" for i, r in enumerate(items, 1)]
    return "\n".join(s) + "\n"


def main():
    os.makedirs(OUT, exist_ok=True)
    for f in os.listdir(OUT):
        os.remove(os.path.join(OUT, f))
    index = []
    for name, title, raw, mode, src, colf in LISTS:
        colf = colf or LISTS[0][5]
        cols = colf(mode)
        data = rows(raw, cols)
        total = sum(len(v) for v in data.values())
        parts = {"": list(data)}
        body = "".join(table(src, cols, lv, data[lv]) for lv in data)
        if len(body.encode()) > MAX:                      # split by CEFR band
            parts = {}
            for lv in data:
                parts.setdefault(lv[:2], []).append(lv)
        files = []
        for band, lvs in parts.items():
            fn = f"{name}-{band.lower()}.md" if band else f"{name}.md"
            n = sum(len(data[lv]) for lv in lvs)
            head = f"# {title}{' · ' + band if band else ''}\n\n{n} words · [all lists](README.md)\n\n"
            toc = " · ".join(f"[{lv}](#{lv.replace('.', '').lower()})" for lv in lvs)
            with open(os.path.join(OUT, fn), "w", encoding="utf-8") as fh:
                fh.write(head + toc + "\n\n" + "\n".join(table(src, cols, lv, data[lv]) for lv in lvs))
            files.append((band or "all", fn, n))
        index.append((title, total, files))
    with open(os.path.join(OUT, "README.md"), "w", encoding="utf-8") as fh:
        fh.write("# Word lists\n\nGenerated from `wordlists/*.py` by `tools/make_wordlists.py`. "
                 "Every row shows the word with its Turkish, German/English and Russian meaning.\n\n"
                 "| List | Words | Files |\n|---|---|---|\n")
        for title, total, files in index:
            links = " · ".join(f"[{b}]({fn})" for b, fn, _ in files)
            fh.write(f"| {title} | {total:,} | {links} |\n")
    for title, total, files in index:
        print(title, total, [(b, n) for b, _, n in files])


if __name__ == "__main__":
    main()
