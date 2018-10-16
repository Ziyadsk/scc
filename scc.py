#!/usr/bin/env python3

import argparse
import json
import os
import random
import webbrowser


home = os.path.expanduser("~")
parser = argparse.ArgumentParser(description="SCC - Commandline Cheat Sheet")
parser.add_argument("--export", choices=["html"], default=None)
group = parser.add_mutually_exclusive_group()

argument_list = ["-html", "-css", "-js", "-python"]

for i in argument_list:
	group.add_argument(i, nargs="?", default="scc_empty")

parser.add_argument("-rand", choices=["html", "css", "js"])
arg = parser.parse_args()


def sep():
	print("\u001b[33;1m-\u001b[0m" * 60)


# random
if arg.rand:
	with open(f"{home}/.scc/ccs/en/{arg.rand}.json") as file:
		data = json.load(file)
	key = random.choice(list(data))
	sep()
	print(key)
	sep()
	for k, v in data[key].items():
		if k == "Attribute(s)":
			break
		print(f"\033[4;33m{k}\033[0m :{v}")


# html part
if not arg.html:
	with open(f"{home}/.scc/ccs/en/html.json") as file:
		data = json.load(file)
	if arg.export == "html":
		print("exporting to html ...")
		html_output = '<html><head><title>SCC-HTML CHEAT CHEET</title></head><body><style>body{ max-width:100vw ; font-family:"roboto","open sans" , "ubuntu" ,"sans-serif";background-color:#fff;color:#666; }#tag{font-size:1.2em ; color:#006688 ; background-color:#ddd ;display:inline-block ;  border-radius:10px ; padding:0.7em ;  } .xmp_tags{ padding:10px ;border-radius:5px ;word-wrap: break-word;font-family:monospace } .xmp_tags:first-child()::before{ content: "Tag : " ;}#wrapper{background-color:#eee;padding:1em ;border-radius:10px ; margin:0.5em auto ; max-width:95vw ;word-wrap: break-word; overflow:auto ; }h1{text-align:center; }</style><h1>SCC - HTML Cheat Cheet</h1>'
		key_elem = ""
		for tag, tag_val in data.items():
			key_elem += f"<div id='wrapper'><span id='tag'>{tag}</span>"
			for desc, desc_val in tag_val.items():
				if desc == list(tag_val)[0]:
					continue
				if desc == "Attribute(s)":
					key_elem += "--- Attributes ---"
					for attr, attr_val in desc_val.items():
						key_elem += f"<xmp class='xmp_tags'>{attr}:{attr_val}</xmp>"
					continue
				key_elem += f"<xmp class='xmp_tags'>{desc_val}</xmp>"
			key_elem += "</div>"
		html_output += key_elem

		with open("exported-scc.html", "w") as file:
			file.write(html_output)
		webbrowser.open_new_tab("exported-scc.html")
		print("Done.")
		exit()
	print("\n".join(data))
elif arg.html != "scc_empty":
	try:
		with open(f"{home}/.scc/ccs/en/html.json") as file:
			data = json.load(file)
		for key, val in data[arg.html.rstrip()].items():
			if key == "Attribute(s)":
				sep()
				print("--- Attributes ---".rjust(40))
				sep()
				for elem, info in val.items():
					print(f"\033[4;33m• {elem}\u001b[0m : {info}")
				sep()
				exit()
			print(f"\033[4;33m{key}\u001b[0m : {val}")
	except KeyError:
		print("This HTML tag doesn't exist")

# css part
if not arg.css:
	with open(f"{home}/.scc/ccs/en/css.json") as file:
		data = json.load(file)
	print("\n".join(data))
elif arg.css != "scc_empty":
	try:
		with open(f"{home}/.scc/ccs/en/css.json") as file:
			data = json.load(file)
		for key, val in data[arg.css.rstrip()].items():
			print(f"\033[4;33m{key}\033[0m :{val}")
	except KeyError:
		print("The CSS property that you requested doesn't exist/isn't indexed")


# js
if not arg.js:
	with open(f"{home}/.scc/ccs/en/js.json") as file:
		data = json.load(file)
	print("\n".join(data))
elif arg.js != "scc_empty":
	try:
		with open(f"{home}/.scc/ccs/en/js.json") as file:
			data = json.load(file)
		for key, val in data[arg.js.rstrip()].items():
			print(f"\033[4;33m{key}\033[0m : {val}")
	except KeyError:
		print(f"'{arg.js}' Not found")
		try:
			lkeys = []
			for key in data:
				if arg.js.split(".")[0] == key.split(".")[0]:
					lkeys.append(key)
			if lkeys:
				print("possible values :")
				print("\n".join(lkeys))
		except Exception:
			pass
