from internetarchive import get_item
from internetarchive import download
from internetarchive import search_items
from zipfile import ZipFile 
from clint.textui import colored, puts
from pyunpack import Archive
from pyfiglet import Figlet
f = Figlet()
print(puts(colored.yellow(f.renderText("NES ROM DOWNLOADER"))))



item = get_item('movieversionspiderman3unlicensedenglishfixed')

files = item.item_metadata['files']
names = []
for i in files:
    names.append(i["name"])
        
names = list(enumerate(names))

names = dict(names)
for i in range(96,100):
    del names[i]
    
for i in names:
        
    puts(colored.blue(f'{i}) {names[i]}'))

select = input("Select the game number to download: ")
try:
    select = select.strip(" ")
    select = select.split()
        
    for s in select:
        game = names[int(s)]
        print(game)


        download("movieversionspiderman3unlicensedenglishfixed",glob_pattern=game,no_directory=True,destdir='A:\Games',silent=True)
            
        Archive(f'A:\Games\{game}').extractall('A:\Games')
except:

    print("Error downloading.Please check your chosen game number")