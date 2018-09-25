#!/usr/bin/env python3

import os 
import argparse 
import json 
import webbrowser 
import random 
home = os.path.expanduser("~")
parser = argparse.ArgumentParser(description="SCC - Super Cheat Cheet") 
parser.add_argument('--export',choices=["html"],default=None)
group = parser.add_mutually_exclusive_group()

argument_list = ['-html','-css','-js','-python']

for i in argument_list:
	group.add_argument(i,nargs='?',default='scc_empty')

parser.add_argument('-rand',choices=["html","css","js"])
arg = parser.parse_args() 

def sep():
	print('\u001b[33;1m-\u001b[0m'*60)



if arg.rand != None:
	with open(f"{home}/.scc/ccs/en/{arg.rand}.json") as file :
		data = json.load(file)
		key = random.choice(list(data.keys()))
		sep()
		print(key)
		sep()
		for k in data[key]:
			if k == "Attribute(s)":
				break 
			print(f"\033[4;33m{k}\033[0m :",
					f'{data[key][k]}')



# html part 
if not arg.html:
	with open(f"{home}/.scc/ccs/en/html.json") as file:
		data = json.load(file)
		if arg.export=="html" :
			print('exporting to html ... ')
			html_output = '<html><head><title>SCC-HTML CHEAT CHEET</title></head><body><style>body{ max-width:100vw ; font-family:"roboto","open sans" , "ubuntu" ,"sans-serif";background-color:#fff;color:#666; }#tag{font-size:1.2em ; color:#006688 ; background-color:#ddd ;display:inline-block ;  border-radius:10px ; padding:0.7em ;  } .xmp_tags{ padding:10px ;border-radius:5px ;word-wrap: break-word;font-family:monospace } .xmp_tags:first-child()::before{ content: "Tag : " ;}#wrapper{background-color:#eee;padding:1em ;border-radius:10px ; margin:0.5em auto ; max-width:95vw ;word-wrap: break-word; overflow:auto ; }h1{text-align:center; }</style><h1>SCC - HTML Cheat Cheet</h1>'
			key_elem = ""
			for tag in data:
				key_elem += f"<div id='wrapper'><span id='tag'>{tag}</span>"
				for desc in data[tag]:
					if desc == list(data[tag])[0]:
						continue
					if desc == "Attribute(s)":
						key_elem+= "--- Attributes ---"
						attrs = data[tag][desc]
						for attr in attrs:
							key_elem+= f"<xmp class='xmp_tags'>{attr}:{data[tag][desc][attr]}</xmp>"
						continue
					key_elem += f"<xmp class='xmp_tags'>{data[tag][desc]}</xmp>"
				key_elem += "</div>"	
			html_output += key_elem 

			with open("exported-scc.html",'w') as file:
				file.write(f'{html_output}')
			webbrowser.open_new_tab("exported-scc.html")
			print('Done.')
			exit()
		for key in data:
			os.system(f'echo {key}')
elif arg.html != "scc_empty":
	try:
		with open(f"{home}/.scc/ccs/en/html.json") as file:
			data = json.load(file)
			for key in data[arg.html.rstrip()]:
				if key == "Attribute(s)":
					sep()
					print("--- Attributes ---".rjust(40))
					sep() 
					for elem in data[arg.html][key]:
						print(f'\033[4;33m• {elem}\u001b[0m : {data[arg.html][key][elem]}')
					sep()
					exit()	
				print(f'\033[4;33m{key}\u001b[0m : ',
						f'{data[arg.html][key]}')
	except KeyError:
		print("this tag doesnt exist")

# css part
if not arg.css:

	with open(f"{home}/scc./ccs/en/css.json") as file:
		data = json.load(file)
		for key in data:
			os.system(f'echo {key}')

elif arg.css != 'scc_empty':
	try:
		with open(f"{home}/.scc/ccs/en/css.json") as file:
			data = json.load(file)
			for key in data[arg.css.rstrip()]:
				print(f"\033[4;33m{key}\033[0m :",
					f'{data[arg.css][key]}')
	except KeyError:
		print("The CSS proprety that you requested doesn't exist/isnt't indexed ")


# js
if not arg.js:
	with open(f"{home}/.scc/ccs/en/js.json") as file:
		data = json.load(file)
		for key in data:
			os.system(f'echo {key}')
elif arg.js != 'scc_empty':
	try:
		with open(f"{home}/.scc/ccs/en/js.json") as file:
			data = json.load(file)
			for key in data[arg.js.rstrip()]:
				print(f"\033[4;33m{key}\033[0m :",
					f'{data[arg.js][key]}')
	except KeyError:
		print(f"{arg.js} Not found")
		try : 
			lkeys = []
			for key in data :
				if arg.js.split('.')[0] == key.split('.')[0]:
					lkeys.append(key)
			if lkeys[0]:
				print("possible values : ")
				for i in lkeys:
					print(i)
			# if lkeys :
			# 	print("do you mean this : ")
			# 	for i in lkeys :
			# 		print(key)
		except Exception :
			pass 
	