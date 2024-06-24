if status is-interactive
    # Commands to run in interactive sessions can go here
    alias "emacsclient"="emacsclient -c -a 'emacs'"
    set -U fish_user_paths ~/swww/target/release/ $fish_user_paths

    alias config='/usr/bin/git --git-dir=/home/woojinkim/.cfg/ --work-tree=/home/woojinkim'
end
