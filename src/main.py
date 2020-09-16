import argparse
import shutil


def setup_bash():
    # creating aliases
    shutil.copy('../res/.bash_aliases', '/home/yalexaner/')

    # changing promt
    with open('/home/yalexaner/.bashrc', 'a') as bashrc:
        with open('../res/promt') as promt:
            bashrc.write(promt.read())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.parse_args()

    setup_bash()
