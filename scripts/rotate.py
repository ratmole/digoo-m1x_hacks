#!/usr/bin/env python3
import argparse
import requests
import time


h = { "Content-Type": "application/soap+xml" }
ip = "192.168.1.129"

x_offset = 0.0
y_offset = 0.0

parser = argparse.ArgumentParser()
parser.add_argument('--left', '-l', action='store_true')
parser.add_argument('--right', '-r', action='store_true')
parser.add_argument('--up', '-u', action='store_true')
parser.add_argument('--down', '-d', action='store_true')
parser.add_argument('--times', '-t', default=1)
parser.add_argument('--ip', default=ip)

args = parser.parse_args()
x_offset = 0.0
y_offset = 0.0
if args.left:
    x_offset = -1.0
elif args.right:
    x_offset = 1.0

if args.up:
    y_offset = 1.0
elif args.down:
    y_offset = -1.0

if x_offset == 0.0 and y_offset == 0.0:
    exit(0)
xml = open('ptz_request.xml').read().replace('_X_', str(x_offset)).replace('_Y_', str(y_offset))

for i in range(0, int(args.times)):
    try:
        r = requests.post("http://%s:5000" % args.ip, headers=h, data=xml, timeout=2)
    except requests.exceptions.ConnectTimeout:
        print("Timed out!")
        break
    if not r.ok:
        print(r.text)
        break
    time.sleep(0.35)
