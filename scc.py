#!/usr/bin/env python3

import argparse
import json
import os
import random
import webbrowser
import textwrap
import sys

# argument system
home = os.path.expanduser("~")
parser = argparse.ArgumentParser(description="SCC - Commandline Cheat Sheet")
parser.add_argument("--export", choices=["html"], default=None)
group = parser.add_mutually_exclusive_group()

argument_list = ["-html", "-css", "-js", "-python"]

for i in argument_list:
	group.add_argument(i, nargs="?", default=None)
parser.add_argument("-rand", choices=["html", "css", "js"])
arg = parser.parse_args()

line_separator = "━" * 72
# displays a banner , used primarly for dispaying titles
def banner(content):
	
	banner = ""
	banner += "┏"
	banner += line_separator
	banner += "┓\n┃\u001b[33;1m "
	banner += content.ljust(71) 
	banner += "\u001b[0m┃\n"
	banner += "┣" + line_separator + "┫"
	print(banner)
	
# handles the arg
def handler(arg_type,argument,error_message):
	with open(f"{home}/.scc/ccs/en/{arg_type}.json") as file:
		data = json.load(file)
	if argument == "all":
		for line in data:
			print(line)
		exit(1)
	try:
		if arg.rand:
			argument = random.choice(list(data))
		if argument == None:
			print("no arg!")
		
		dictionary_data = data[argument.rstrip()]
		banner(f"{argument}")
		for k, v in dictionary_data.items():
			
			title = f"┃ ● \033[4;33m{k}\033[0m".ljust(84) + "┃"
			print("┃"+ " "*72+ "┃")	
			print(title)
			print("┃"+ " "*72+ "┃")

			for chunk_of_text in textwrap.wrap(v):
				print("┃ " + chunk_of_text.ljust(71) + "┃")
			print("┃"+ " "*72+ "┃")
			print("┣" + line_separator + "┫")
			
		sys.stdout.write('\x1b[1A')
		sys.stdout.write('\x1b[2K') 
		print("┗" + line_separator + "┛")
	except Exception:
		print(error_message)
		if arg_type == "js":
			try:
				lkeys = []
				for key in data:
					if argument.split(".")[0] == key.split(".")[0]:
						lkeys.append(key)
				if lkeys:
					print("possible values :")
					print("\n".join(lkeys))
			except Exception:
				pass

# when using the random argument 

if arg.js:
	handler("js",arg.js,f"[\033[33;1mNOT FOUND\033[0m]: {arg.js} ")
	
if arg.css:
	handler("css",arg.css,"[\033[33;1mNOT FOUND\033[0m] The CSS property that you requested doesn't exist/isn't indexed")

if arg.html:
	handler("html",arg.html,f"[\033[33;1mNOT FOUND\033[0m] <{arg.html}> : not found")

if arg.rand:
	handler(arg.rand,arg.rand,"")