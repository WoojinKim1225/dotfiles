#!/bin/bash

# Check if hyprpicker is installed
if ! command -v hyprpicker &> /dev/null; then
    notify-send "Error: hyprpicker is not installed"
    exit 1
fi

# Run hyprpicker and get the hex color
hex_color=$(hyprpicker)

# Send a notification with the picked color
notify-send "Hyprpicker Color" "$hex_color"
