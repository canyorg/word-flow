#!/usr/bin/env bash
# Word Flow installer for Linux (GNOME, KDE, …)
#   ./install.sh                      -> app-menu entries for all 4 pairs
#   ./install.sh --autostart de-tr en-tr  -> also start these pairs at login
set -euo pipefail

PAIRS=(de-tr en-tr en-de de-en)
declare -A NAMES=(
  [de-tr]="Word Flow · Deutsch → Türkçe"
  [en-tr]="Word Flow · English → Türkçe"
  [en-de]="Word Flow · English → Deutsch"
  [de-en]="Word Flow · Deutsch → English"
)

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
cp -r "$SRC/wordflow.py" "$SRC/wordlists" "$DEST/"

write_entry() {   # $1 = pair, $2 = target file
  cat > "$2" <<DESK
[Desktop Entry]
Type=Application
Name=${NAMES[$1]}
Comment=Tiny always-on-top vocabulary widget
Exec=python3 $DEST/wordflow.py $1
Icon=accessories-dictionary
Terminal=false
Categories=Education;Languages;
X-GNOME-Autostart-Delay=10
DESK
}

for p in "${PAIRS[@]}"; do
  write_entry "$p" "$APPS/word-flow-$p.desktop"
done
echo "✓ Installed to $DEST — find 'Word Flow' in your app menu."

if [[ "${1:-}" == "--autostart" ]]; then
  shift
  mkdir -p "$AUTO"
  for p in "$@"; do
    [[ -n "${NAMES[$p]:-}" ]] || { echo "unknown pair: $p"; exit 1; }
    write_entry "$p" "$AUTO/word-flow-$p.desktop"
    echo "✓ $p will start at login"
  done
fi
