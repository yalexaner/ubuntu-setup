import argparse
import os
import shutil


def setup_bash():
    # creating aliases
    shutil.copy('../res/.bash_aliases', '/home/yalexaner/')

    # changing promt
    with open('/home/yalexaner/.bashrc', 'a') as bashrc:
        with open('../res/promt') as promt:
            bashrc.write(promt.read())


def install_and_configure_yandex_disk():
    # installing yandex-disk
    os.system('echo "deb http://repo.yandex.ru/yandex-disk/deb/ stable main" '
              '| sudo tee -a /etc/apt/sources.list.d/yandex-disk.list > /dev/null '
              '&& wget http://repo.yandex.ru/yandex-disk/YANDEX-DISK-KEY.GPG -O- '
              '| sudo apt-key add - && sudo apt update '
              '&& sudo apt install -y yandex-disk')

    # setting up yandex-disk
    os.system('yandex-disk setup')


def install_and_configure_git():
    os.system('sudo apt install git')

    username = input('username (leave empty for default value): ') or 'yalexaner'
    email = input('email (leave empty for default value): ') or 'mail.yalexaner@gmail.com'

    os.system(f'git config --global user.name {username}')
    os.system(f'git config --global user.email {email}')
    os.system('git config --global user.editor vim')


def install_applications():
    # Vivaldi
    os.system('wget "https://downloads.vivaldi.com/stable/vivaldi-stable_3.3.2022.45-1_amd64.deb" -O /tmp/vivaldi.deb '
              '&& sudo dpkg -i /tmp/vivaldi.deb')

    # Stremio
    os.system('wget "https://dl.strem.io/shell-linux/v4.4.116/stremio_4.4.116-1_amd64.deb" -O /tmp/stremio.deb '
              '&& sudo dpkg -i /tmp/stremio.deb')

    # apts: Spotify, Telegram, Zeal, mpv, GParted, Vim, Vim GTK (for external clipboard)
    os.system('sudo apt install spotify-client telegram-desktop zeal mpv gparted vim vim-gtk')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Setup the system.')

    parser.add_argument('object', default='everything', nargs='?',
                        choices=['everything', 'bash', 'yandex-disk', 'git', 'apps'],
                        metavar='{basic, bash, yandex-disk, apps}',
                        help='Object on which to perform the setup.')

    arg = parser.parse_args().object

    if arg == 'bash':
        setup_bash()
    elif arg == 'yandex-disk':
        install_and_configure_yandex_disk()
    elif arg == 'git':
        install_and_configure_git()
    elif arg == 'apps':
        install_applications()
    else:
        setup_bash()
        install_and_configure_yandex_disk()
        install_and_configure_git()
        install_applications()
