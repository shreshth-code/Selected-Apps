#!/bin/bash

SESSION_FILE="$HOME/project_apps/last_session.txt"
> "$SESSION_FILE"

for pid in $(pgrep -u "$USER"); do
    cmd=$(ps -p "$pid" -o comm=)
    case "$cmd" in
        brave*|firefox*|xfce4-terminal|gnome-terminal|code|chromium|thunar)
            echo "$cmd" >> "$SESSION_FILE"
            ;;
    esac
done
