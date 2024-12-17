#!/usr/bin/env python3
import argparse, random, os, sys

parser = argparse.ArgumentParser('fortune', description='Python-based customizable fortune', epilog='thanks! ; main Branch ; updated 2024-12-17 ; by Nacroni')
parser.add_argument('-v', '--verbose', help='not a good verbose mode', action='store_true')
args = parser.parse_args()
verbose_enable = args.verbose

if verbose_enable:print('Checking ./fortune/ directory...')
file_list = os.listdir('./fortune/')

chosen_file = random.choice(file_list)
if verbose_enable:print(f'Chosen File: {chosen_file}')

if chosen_file.startswith('.'):
    if verbose_enable: print('File is hidden, restarting...')
    os.execv(sys.argv[0], sys.argv)

file = open(f'./fortune/{chosen_file}', 'r')
text = file.read()

print(text)