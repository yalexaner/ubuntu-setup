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
              '| sudo apt-key add - && sudo apt-get update '
              '&& sudo apt-get install -y yandex-disk')

    # setting up yandex-disk
    os.system('yandex-disk setup')


def install_applications():
    # Vivaldi
    os.system('wget "https://downloads.vivaldi.com/stable/vivaldi-stable_3.3.2022.45-1_amd64.deb" -O /tmp/vivaldi.deb '
              '&& debi /tmp/vivaldi.deb')

    # Stremio
    os.system('wget "https://dl.strem.io/shell-linux/v4.4.116/stremio_4.4.116-1_amd64.deb" -O /tmp/stremio.deb '
              '&& debi /tmp/stremio.deb')

    # apts: Spotify, Telegram, Zeal, mpv, GParted, Vim, Vim GTK (for external clipboard)
    os.system('apti spotify-client telegram-desktop zeal mpv gparted vim vim-gtk')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Setup the system.')

    parser.add_argument('object', default='basic', nargs='?', choices=['basic', 'bash', 'yandex-disk', 'apps'],
                        metavar='{basic, bash, yandex-disk, apps}',
                        help='Object on which to perform the setup. Basic includes bash, yandex-disk, and apps.')

    arg = parser.parse_args().object

    if arg == 'bash':
        setup_bash()
    elif arg == 'yandex-disk':
        install_and_configure_yandex_disk()
    elif arg == 'apps':
        install_applications()
    else:
        setup_bash()
        install_and_configure_yandex_disk()
        install_applications()
