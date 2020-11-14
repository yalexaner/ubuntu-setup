# update apts
alias upd='aptuq && flatuq && aptarq && aptacq'

# apts
alias aptu='sudo apt update && sudo apt upgrade'
alias aptuq='sudo apt update -qq && sudo apt upgrade -qq'
alias aptar='sudo apt autoremove'
alias aptarq='sudo apt autoremove -qq'
alias aptac='sudo apt autoclean'
alias aptacq='sudo apt autoclean -qq'
alias apti='sudo apt install'
alias aptr='sudo apt remove'
alias apts='apt search'

# flatpak
alias flatu='sudo flatpak update'
alias flatuq='sudo flatpak update --noninteractive'
alias flati='sudo flatpak install'

# debs
alias debi='sudo dpkg -i'
alias debr='sudo dpkg -r'

alias rm='rm -i'
alias rmf='rm -rf'

# check for files' sizes
alias v='du -sh'
alias vb='du -bs' # size in bytes
alias vk='du -s' # size in Kilobytes

# yandex-disk sync
alias yad='yandex-disk'
alias yads='yandex-disk status'
alias yadp='yandex-disk publish'

# git
alias gits='git status'
alias gita='git add'
alias gitc='git commit -m'
alias gitl='git log'
alias gitd='git diff'

# clipboard
alias cl='xclip'
alias cg='xclip -selection clipboard'
alias vl='xclip -o'
alias vg='xclip -o -selection clipboard'

# update .bashrc
alias bashu='source ~/.bashrc'
