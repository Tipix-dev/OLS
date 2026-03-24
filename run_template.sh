#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

# -----------------------------
# OLS GUI Installer
# -----------------------------

command -v zenity >/dev/null 2>&1 || {
    echo "[OLS] Zenity not found. Installing..."
    if command -v pacman >/dev/null 2>&1; then
        sudo pacman -S --noconfirm zenity
    elif command -v apt-get >/dev/null 2>&1; then
        sudo apt-get update
        sudo apt-get install -y zenity
    elif command -v yum >/dev/null 2>&1; then
        sudo yum install -y zenity
    elif command -v dnf >/dev/null 2>&1; then
        sudo dnf install -y zenity
    else
        zenity --error --text="Cannot install Zenity automatically. Please install it manually."
        exit 1
    fi
}

TMP_LICENSE=$(mktemp)
cat LICENSE > "$TMP_LICENSE"

zenity --text-info \
       --title="GNU GPL Public License 3.0" \
       --filename="$TMP_LICENSE" \
       --width=700 --height=500

rm -f "$TMP_LICENSE"

if ! zenity --question --text="Do you accept the GPL 3.0 license?"; then
    zenity --error --text="Installation canceled."
    exit 0
fi

if ! zenity --question --text="This installer may modify your shell config and install OLS. Continue?"; then
    zenity --error --text="Installation canceled."
    exit 0
fi


TMP_DIR=$(mktemp -d)
ARCHIVE_LINE=$(awk '/^__ARCHIVE_BELOW__/ {print NR + 1; exit 0; }' "$0")
tail -n+$ARCHIVE_LINE "$0" | tar -xz -C "$TMP_DIR"

cd "$TMP_DIR"/*/
bash install.sh

rm -rf "$TMP_DIR"

# -----------------------------
# 4. Успешное завершение
# -----------------------------
zenity --info --text="OLS installed successfully!"

exit 0

__ARCHIVE_BELOW__