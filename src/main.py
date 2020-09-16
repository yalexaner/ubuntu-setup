import argparse
import shutil

parser = argparse.ArgumentParser()
parser.parse_args()

# creating aliases
shutil.copy('../res/.bash_aliases', '/home/yalexaner/')

# changing promt
with open('/home/yalexaner/.bashrc', 'a') as bashrc:
    with open('../res/promt') as promt:
        bashrc.write(promt.read())
