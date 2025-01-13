#!/usr/bin/env python3
import argparse, random, os, sys
import logging as log

# verbose (https://stackoverflow.com/questions/5980042/how-to-implement-the-verbose-or-v-option-into-a-script/15412863#15412863)

p = argparse.ArgumentParser()
p.add_argument('-a', '--all', help='read all cookies, including offensive and hidden ones', action='count', default=False)
p.add_argument('-o', '--offensive', help='enable reading offensive cookies', action='count', default=False)
p.add_argument('-c', '--cookie', help='choose a specific cookie')
p.add_argument('-v', '--verbose', help='enables verbose mode', action='count', default=False)

args = p.parse_args()

if args.verbose:
    log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
    log.info("Verbose output enabled!")
else:
    log.basicConfig(format="%(levelname)s: %(message)s")

if args.cookie:
    log.info('Cookie override enabled.')
    chosen_cookie = args.cookie
    log.info(f'Chosen Cookie: {chosen_cookie}')
    cookie = open(f'./cookies/{chosen_cookie}', 'r')
    log.info('Assigned & reading chosen cookie...')
    print(cookie.read())
    exit()

# main script
cookie_list = os.listdir('./cookies/')
log.info('Checked ./cookies/ directory!')

chosen_cookie = random.choice(cookie_list)

if chosen_cookie.startswith('.'):
    if args.all:
        log.info('File is hidden, ignoring...')
    else:
        log.info('File is hidden, restarting...')
        os.execv(sys.argv[0], sys.argv)

if chosen_cookie.startswith('o.'):
    if args.all or args.offensive:
        log.info('File is offensive, ignoring...')
    else:
        log.info('File is offensive, restarting...')
        os.execv(sys.argv[0], sys.argv)
    

cookie = open(f'./cookies/{chosen_cookie}', 'r')
log.info('Assigned & reading chosen cookie...')

print(cookie.read())
