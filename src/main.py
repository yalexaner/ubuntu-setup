from argparse import ArgumentParser
from os import system as execute, listdir, rmdir, mkdir
from shutil import copy as copy_file


def setup_bash():
    # creating aliases
    copy_file('../res/.bash_aliases', '/home/yalexaner/')

    # changing promt
    with open('/home/yalexaner/.bashrc', 'a') as bashrc:
        with open('../res/promt') as promt:
            bashrc.write(promt.read())


def configure_dirs():
    dirs = listdir('/home/yalexaner')

    for dir in dirs:
        rmdir(f'/home/yalexaner/{dir}')

    mkdir('/home/yalexaner/downloads')


def install_and_configure_yandex_disk():
    # installing yandex-disk
    execute('echo "deb http://repo.yandex.ru/yandex-disk/deb/ stable main" '
            '| sudo tee -a /etc/apt/sources.list.d/yandex-disk.list > /dev/null '
            '&& wget http://repo.yandex.ru/yandex-disk/YANDEX-DISK-KEY.GPG -O- '
            '| sudo apt-key add - && sudo apt update '
            '&& sudo apt install -y yandex-disk')

    # setting up yandex-disk
    execute('yandex-disk setup')


def install_and_configure_git():
    execute('sudo apt install git')

    username = input('username (leave empty for default value): ') or 'yalexaner'
    email = input('email (leave empty for default value): ') or 'mail.yalexaner@gmail.com'

    execute(f'git config --global user.name {username}')
    execute(f'git config --global user.email {email}')
    execute('git config --global user.editor vim')


def install_applications():
    # Vivaldi
    execute('wget "https://downloads.vivaldi.com/stable/vivaldi-stable_3.3.2022.45-1_amd64.deb" -O /tmp/vivaldi.deb '
            '&& sudo dpkg -i /tmp/vivaldi.deb')

    # Stremio
    execute('wget "https://dl.strem.io/shell-linux/v4.4.116/stremio_4.4.116-1_amd64.deb" -O /tmp/stremio.deb '
            '&& sudo dpkg -i /tmp/stremio.deb')
    
    # VK Messenger
    execute('wget "https://desktop.userapi.com/get_last?platform=linux64&branch=master&packet=deb" -O /tmp/vk.deb '
            '&& sudo dpkg -i /tmp/vk.deb')

    # apts: Spotify, Telegram, Zeal, mpv, GParted, Vim, Vim GTK (for external clipboard)
    execute('sudo apt install spotify-client telegram-desktop zeal mpv gparted vim vim-gtk')


if __name__ == '__main__':
    parser = ArgumentParser(description='Setup the system.')

    parser.add_argument('object', default='everything', nargs='?',
                        choices=['everything', 'bash', 'git'],
                        metavar='{everything, bash, git}',
                        help='Object on which to perform the setup.')

    arg = parser.parse_args().object

    if arg == 'bash':
        setup_bash()
    elif arg == 'git':
        install_and_configure_git()
    else:
        setup_bash()
        configure_dirs()
        install_and_configure_yandex_disk()
        install_and_configure_git()
        install_applications()
