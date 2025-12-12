#!/bin/bash

SESSION_FILE="/home/neer/project_apps/last_session.txt"

# Load correct GUI environment
export DISPLAY=:0
export XAUTHORITY=/home/neer/.Xauthority
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus"

sleep 10  # Wait for GUI login

if [ -f "$SESSION_FILE" ]; then
    while read app; do
        if [ ! -z "$app" ]; then
            echo "Reopening $app"
            "$app" &
        fi
    done < "$SESSION_FILE"
fi

