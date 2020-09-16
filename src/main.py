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


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.parse_args()

    setup_bash()
    install_and_configure_yandex_disk()
