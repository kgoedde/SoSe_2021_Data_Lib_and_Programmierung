# -*- coding: utf-8 -*-

"""
This script performs simple calculations.
Arguments are given during the call of this script.
"""
# Do simple calculation

import argparse

# Neues Objekt der Klasse ArgumentParser erzeugen.
parser = argparse.ArgumentParser()


parser.add_argument("number_1", type=int, help="An integer")
parser.add_argument("number_2", type=int, help="Another integer")
#parser.add_argument("-multi", default=False, action="store_true")
parser.add_argument("-operation", choices=["add", "sub", "multi", "div"])


args = parser.parse_args()

# Commented code - not active anymore
print(args)
# print(args.number_1, args.number_2)

#if args.multi is True
if args.operation == "multi":
    result = args.number_1 * args.number_2
elif args.operation == "add":
    result = args.number_1 + args.number_2
elif args.operation == "sub":
    result = args.number_1 - args.number_2
elif args.operation == "div":
    result = args.number_1 / args.number_2


print(result)