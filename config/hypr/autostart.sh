#!/usr/bin/bash

foot --server > ~/somelog
emacs --daemon >> ~/somelog
fcitx5 -d  >> ~/somelog
#killall waybar
#sleep 1
waybar >> ~/somelog
