#!/usr/bin/env bash
# Word Flow installer for Linux (GNOME, KDE, …)
#   ./install.sh              -> adds "Word Flow" to the app menu
#   ./install.sh --autostart  -> also starts it when you log in
set -euo pipefail

DEST="$HOME/.local/share/word-flow"
APPS="$HOME/.local/share/applications"
AUTO="$HOME/.config/autostart"
SRC="$(cd "$(dirname "$0")" && pwd)"

if ! python3 -c "import PyQt6" 2>/dev/null; then
  echo "PyQt6 not found. Install it first:"
  echo "  Fedora:        sudo dnf install python3-pyqt6"
  echo "  Debian/Ubuntu: sudo apt install python3-pyqt6"
  echo "  any distro:    pip install --user PyQt6"
  exit 1
fi

mkdir -p "$DEST" "$APPS"
cp -r "$SRC/wordflow.py" "$SRC/wordlists" "$SRC/icon.png" "$DEST/"

# remove entries of older versions (one entry per language pair)
rm -f "$APPS"/word-flow-*.desktop "$AUTO"/word-flow-*.desktop "$AUTO"/kelime-akisi*.desktop

write_entry() {
  cat > "$1" <<DESK
[Desktop Entry]
Type=Application
Name=Word Flow
Comment=Tiny always-on-top vocabulary widget (English · Deutsch · Türkçe · Русский)
Exec=python3 $DEST/wordflow.py
Icon=$DEST/icon.png
Terminal=false
Categories=Education;Languages;
X-GNOME-Autostart-Delay=10
DESK
}

if ! command -v espeak-ng >/dev/null && ! command -v spd-say >/dev/null; then
  echo "ℹ For the 🔊 read-aloud button install a speech engine:"
  echo "    Fedora: sudo dnf install espeak-ng    Debian/Ubuntu: sudo apt install espeak-ng"
fi

write_entry "$APPS/word-flow.desktop"
echo "✓ Installed to $DEST — find 'Word Flow' in your app menu."

if [[ "${1:-}" == "--autostart" ]]; then
  mkdir -p "$AUTO"
  write_entry "$AUTO/word-flow.desktop"
  echo "✓ Word Flow will start when you log in"
fi
