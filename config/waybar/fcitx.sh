#!/usr/bin/env sh


if [ $(fcitx5-remote -n) = "keyboard-us" ];
then
   echo "us"
else
    echo "kr"
fi
