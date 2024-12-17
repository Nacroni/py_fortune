#!/usr/bin/env python3
import argparse, random, os, sys
import logging as log

# verbose (https://stackoverflow.com/questions/5980042/how-to-implement-the-verbose-or-v-option-into-a-script/15412863#15412863)

p = argparse.ArgumentParser()
p.add_argument('-v', '--verbose', help='enables verbose mode', action='count', default=0)
args = p.parse_args()
if args.verbose:
    log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
    log.info("Verbose output enabled!")
else:
    log.basicConfig(format="%(levelname)s: %(message)s")


# main script
file_list = os.listdir('./fortune/')
log.info('Checked ./fortune/ directory!')

chosen_file = random.choice(file_list)
log.info(f'Chosen File: {chosen_file}')

if chosen_file.startswith('.'):
    log.info('File is hidden, restarting...')
    os.execv(sys.argv[0], sys.argv)

fortune = open(f'./fortune/{chosen_file}', 'r')
log.info('Assigning & reading chosen file...')

print(fortune.read())