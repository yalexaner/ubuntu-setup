# update apts
alias upd='aptu && aptar && aptac'

# apts
alias aptu='sudo apt update && sudo apt upgrade'
alias apti='sudo apt install'
alias aptr='sudo apt remove'
alias aptar='sudo apt autoremove'
alias aptac='sudo apt autoclean'

# debs
alias debi='sudo dpkg -i'
alias debr='sudo dpkg -r'

alias rm='rm -i'
alias rmf='rm -rf'

# check for files' sizes
alias v='du -sh'
alias vb='du -bs' # size in bytes
alias vkb='du -s' # size in Kbytes

# yandex-disk sync
alias yad='yandex-disk'
alias yads='yandex-disk status'
alias yadp='yandex-disk publish'

# git
alias gits='git status'
alias gita='git add'
alias gitc='git commit -m'
alias gitl='git log'

# clipboard
alias cl='xclip'
alias cg='xclip -selection clipboard'
alias vl='xclip -o'
alias vg='xclip -o -selection clipboard'

# update .bashrc
alias bashu='source ~/.bashrc'
