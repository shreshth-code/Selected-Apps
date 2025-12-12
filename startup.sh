#!/bin/bash

sleep 5

echo "Opening apps..."

while IFS= read -r app; do
    if command -v "$app" >/dev/null 2>&1; then
        $app &
    else
        echo "Not found: $app"
    fi
done < ~/project_apps/apps.txt
