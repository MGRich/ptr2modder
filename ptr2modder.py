import ast
import ctypes
import linecache
import os
import subprocess
import time
import urllib
import webbrowser
import sys
import math
from difflib import get_close_matches as match
from decimal import Decimal as decimal
from msvcrt import getch
import colorama
from termcolor import colored as color

#colors
black = "\033[1;30m"
red =  "\033[1;31m"
green =  "\033[1;32m"
yellow =  "\033[1;33m"
blue =  "\033[1;34m"
magenta =  "\033[1;35m"
cyan =  "\033[1;36m"
white =  "\033[1;37m"

bblack =  "\033[1;30;1m"
bred =  "\033[1;31;1m"
bgreen =  "\033[1;32;1m"
byellow =  "\033[1;33;1m"
bblue =  "\033[1;34;1m"
bmagenta =  "\033[1;35;1m"
bcyan =  "\033[1;36;1m"
bwhite =  "\033[1;37;1m"

reset =  "\033[1;0m"
bold = "\033[1;1m"
#endcolors

colorama.init()
colorf = sys.stdout.write

if os.path.isfile("devmode"):
    d = True
else:
    d = False
if not os.path.isdir("temp"):
    os.mkdir("temp")
title = ctypes.windll.kernel32.SetConsoleTitleA
title("PTR2Modder")
if d:
    title("PTR2Modder DEV")
if not d:
    urllib.urlretrieve("https://mgrich.github.io/storage/ptr2modder/versionb.txt", "temp/version.txt")
else:
    urllib.urlretrieve("https://mgrich.github.io/storage/ptr2modder/versiond.txt", "temp/version.txt")
v = open("temp/version.txt").read()
v = float(v[:-1])
if not os.path.isdir("config"):
    print("Welcome to PTR2Modder.\nThis is a program specifically made for making and using PTR2 mods.\nSpecial thanks to the PTR2 Modding Discord for motivating me to do this.")
    print("")
    print("We will start by creating basic configuration files.")
    os.mkdir("mods")
    os.mkdir("config")
    os.chdir("config")
    os.mkdir("mds")
    con1 = open("basic.conf", 'w+')
    os.mkdir("ibrn")
    while not os.path.isfile("ibrn/imgburn.exe"):
        print("Please put your IMGBurn exe (all lowercase) in ibrn (in config).")
        os.system("pause >nul")
    os.chdir("..")
    os.mkdir("ogiso")
    while not os.path.isfile("ogiso/SYSTEM.CNF"):
        print("Please place your unedited ISO in ogiso (at root of ptr2modder).")
        os.system("pause >nul")
    sys = linecache.getline("ogiso/SYSTEM.CNF", 3)
    sys = sys[-4:-1]
    if sys == "TSC":
        sys = "NTSC"
    con1.write(sys + "\n")
    os.mkdir("miso")
    print("Copying into miso..")
    os.system("xcopy /s /q ogiso miso")
    h = str(raw_input("Do you plan using this in (b)asic mode or (c)reation mode? (B OR C)> "))
    h = str(h) + "\n"
    con1.write(h)
    if h == h.lower():
        print("Downloading tools..")
        urllib.urlretrieve("https://mgrich.github.io/storage/tools.zip", "temp/tools.zip")
        os.chdir("temp")
        print("Extracting..")
        from zipfile import ZipFile as zipfile
        zipfile('tools.zip').extractall()
        os.remove('tools.zip')
        os.chdir("..")
        print("Moving..")
        os.mkdir("tools")
        os.system("xcopy /s /q temp tools")
        os.system("rmdir /Q /S temp")
        os.chdir("config")
        con2 = open("create.conf", 'w+')
        print("Done with tools.\nChanging to basic mode will not get rid of the tools.")
        print("")
        os.chdir("..")
        while True:
            h = str(raw_input("What do you want your WIP folder where WIP mods are stored to be called? (cannot be called mods)> "))
            while h == "mods":
                print("Nice try.")
                h = input("Pick an actual name> ")
            try:
                os.mkdir(h)
            except WindowsError:
                print("That didn't work, try again.")
    con2.write(h)
    print("Congratulations, you're now all set!")
    print("The program will now shut down to load the config correctly.")
    time.sleep(5)
    exit()
else:
    conf = os.getcwd() + "\\config\\basic.conf"
    ibrn = os.getcwd() + "\\config\\ibrn\\imgburn.exe"
    cre = linecache.getline(conf, 2)
    if cre == "c\n":
        cre = True
    else:
        cre = False
    print("Refreshing mods..")
    hahayes = os.listdir("mods")
    yeshaha = open("config/mods.conf", "w")
    yeshaha.truncate()
    for x in hahayes:
        yeshaha.write(x + "\n")
    yeshaha.close()

print("Downloading news..")
urllib.urlretrieve("https://mgrich.github.io/storage/ptr2modder/news.txt", "temp/news.txt")
while True:
    os.system("cls")
    print("")
    colorf(red)
    if not d:
        print("PTR2Modder")
    else:
        print("PTR2Modder (Dev)")
    print("Tool by RMGRich")
    print("Icon by Charx")
    print("")
    if v > 1.5:
        opt = ["1", "2", "3", "4", "5", "6", "7", "8"]
    else:
        opt = ["1", "2", "3", "4", "5", "6", "7"]
    if d and cre:
        opt.append("c")
    while True:
        colorf(reset)
        print("1. Convert ISO mod to usable mod")
        print("2. Apply mod")
        print("3. Unapply mod")
        print("4. Check news")
        print("5. Refresh mods")
        print("6. Options")
        print("7. Exit properly")
        if v > 1.5:
            print("8. Install new version")
        if d and cre:
            print("C. Creation Menu")
        ch = getch()
        if not ch in opt:
            print("Invalid answer")
            time.sleep(3)
            os.system("cls")
            print("")
            colorf(red)
            if not d:
                print("PTR2Modder")
            else:
                print("PTR2Modder (Dev)")
            print("Tool by RMGRich")
            print("Icon by Charx")
            print("")
        else:
            break
    if ch == "1":
        os.chdir("mods")
        hg = str(raw_input("What do you want your mod's folder to be called?> "))
        os.mkdir(hg)
        os.chdir(hg)
        print("Now to setup configuration:")
        m = open("mod.inf", "w+")
        h1 = str(raw_input("Name of mod> "))
        h2 = str(raw_input("Author> "))
        h3 = str(raw_input("Version> "))
        h4 = str(raw_input("Description> "))
        m.write(h1 + "\n" + h2 + "\n" + h3 + "\n" + h4 + "\n")
        print("Please place your modified ISO contents (only the modified files) WITH THEIR CORRECT FOLDERS in the new 'iso' folder.\nMake sure you do it correctly, as if you mess it up, the mod wont work unless you start over.")
        os.mkdir("iso")
        os.system("pause")
        os.chdir("iso")
        mm = []
        for root, directories, filenames in os.walk('.'):
            for filename in filenames: 
                    h = os.path.join(root,filename)
                    h = h[2:]
                    mm.append(h)
        lmfao = []
        dect = str(mm).lower()
        for x in range(1,9):
            x = str(x)
            o = "st0" + x
            f = "vs0" + x
            if o in dect:
                lmfao.append(x)
            if f in dect:
                lmfao.append("VS" + x)
        if 'stbn' in dect:
            lmfao.append("Bonus")
        if 'stmenu' in dect:
            lmfao.append("Stage Menu")
        if 'title.int' in dect:
            lmfao.append("Title")
        charx = []
        #conditional checks
        if 'wp2' in dect:
            charx.append('Music Modding')
            if 'gm0n' in dect:
                charx.append("Bad/Awful Editing")
        if 'int' in dect:
            charx.append('INT Mod')
        if 'olm' in dect:
            charx.append('OLM Editing')
        if 'xtr' in dect:
            charx.append('Cutscene Editing')
        if 'hk0' in dect:
            charx.append('Boxy Editing')
        if 'ext' in dect:
            charx.append('Music Box Editing')
        if 'scus' in dect:
            charx.append('ELF Model Editing')
        m.write(str(mm))
        m.write("\n" + str(linecache.getline(conf, 1)) + str(lmfao) + "\n" + str(charx))
        m.close()
        os.chdir("../../..")
        print("Refreshing mods..")
        hahayes = os.listdir("mods")
        yeshaha = open("config/mods.conf", "w")
        yeshaha.truncate()
        for x in hahayes:
            yeshaha.write(x + "\n")
        yeshaha.close()
        print("Done.")
        os.system('pause')
    elif ch == "2": 
        os.chdir("config")
        m = open("mods.conf", "r")
        mds = m.readlines()
        os.chdir("mds")
        ooo = open("on.conf")
        con = ooo.readlines()
        con = map(lambda s: s.strip(), con)
        os.chdir("../../mods")
        mds = map(lambda s: s.strip(), mds)
        mdl = []
        omdl = []
        onli = []
        for x in mds:
            md = linecache.getline(x + "/mod.inf", 1)
            omdl.append(md)
            if x in con:
                md = md[:-1]
                onli.append(md)
                md = color(md, 'red')
            else:
                md = color(md[:-1], 'green')
            mdl.append(md)
        mdl = map(lambda s: s.strip(), mdl)
        omdl = map(lambda s: s.strip(), omdl)
        onli = map(lambda s: s.strip(), onli)
        p = 1
        mp = int(str(math.ceil((len(mdl) + .0) / 5))[:-2])
        mdlf = mdl
        omdlf = omdl
        ex = False
        while True:
            while True:
                if ex:
                    break
                os.system("cls")
                mdp = mdlf[p * 5 - 5:p * 5]
                print("")
                print("Page " + str(p) + " of " + str(mp) + " (" + str(len(omdlf)) + " mods)")
                print("--pu to move up a page, --pd to move down a page.\n--p (page number) to skip to a page\n--s (query/nothing (to unfilter)) to search.\n--e to exit.\n")
                print("Mods installed:")
                print('\n'.join(mdp))
                print("")
                m = raw_input("Which mod?> ")
                if m == "--e":
                    ex = True
                elif m == "--pu":
                    p = p + 1
                    if p > mp:
                        p = p - 1
                elif m == "--pd":
                    p = p - 1
                    print("mmm")
                    if p <= 0:
                        p = p + 1
                elif m[:3] == "--p":
                    p = int(m[4:])
                elif m[:3] == "--s":
                    qu = m[4:]
                    mdlf = [x for x in mdl if qu in x.lower()]
                    omdlf = [x for x in omdl if qu in x.lower()]
                    p = 1
                    mp = int(str(math.ceil((len(mdlf) + .0) / 5))[:-2])
                    if mp == 0:
                        print("None found.")
                        os.system("pause")
                        mdlf = mdl
                        omdlf = omdl
                        mp = int(str(math.ceil((len(mdlf) + .0) / 5))[:-2])
                    else:
                        continue
                else:
                    m = match(m, omdlf, len(omdlf), 0)
                    try:
                        m = m[0]
                    except:
                        m = None
                    print(m)
                    if m in onli:
                        print("Mod is already active.")
                        os.system("pause")
                    elif not m in omdlf:
                        print("Mod doesnt exist or is not in query.")
                        os.system("pause")
                    else:
                        blo = omdlf.index(m)
                        ate = mds[int(blo)]
                        os.chdir(ate)
                        print("Is this the mod you want? (N if no, anything else if yes)")
                        da = open("mod.inf")
                        dat = da.readlines()
                        dat = map(lambda s: s.strip(), dat)
                        print("Name: " + dat[0])
                        print("Author: " + dat[1])
                        print("Version: " + dat[2])
                        print("Description: " + dat[3])
                        try:
                            mmtastyyy = dat[6]
                        except IndexError:
                            mmtastyyy = "None listed"
                        else:
                            if mmtastyyy == "[]":
                                mmtastyyy = "None listed"
                            else:
                                mmtastyyy = ast.literal_eval(mmtastyyy)
                                mmtastyyy = ", ".join(mmtastyyy)                    
                        print("Stages: " + mmtastyyy)
                        try:
                            mmtastyyy = dat[7]
                        except IndexError:
                            mmtastyyy = "None listed"
                        else:
                            if mmtastyyy == "[]":
                                mmtastyyy = "None listed"
                            else:
                                mmtastyyy = ast.literal_eval(mmtastyyy)
                                mmtastyyy = ", ".join(mmtastyyy)
                        print("Mod types: " + mmtastyyy)
                        da.close()
                        while True:
                            fishy = getch()
                            if fishy == "n":
                                mrl = "n"
                                break
                            else:
                                mrl = "h"
                                break
                        if mrl == "n":
                            print("Returning to list..")
                            os.chdir("..")
                        else:
                            break
            pips = linecache.getline("mod.inf", 6)
            if ex:
                break
            if not pips == str(linecache.getline(conf, 1)):
                print("This mod is not meant for your region.")
            else:
                os.chdir("iso")
                dc = os.getcwd()
                os.chdir("../../..")
                print("Applying mod..")
                no = open("config/mds/on.conf", "a+")
                exprz = no.readlines()
                if not str(ate + "\n") in exprz:
                    no.write(ate + "\n")
                no.close()
                os.system("xcopy /s /q /y " + dc + " miso") 
                print("Would you like to add more? (Y if yes)")
                mmm = getch()
                if mmm == "y":
                    os.chdir("mods")
                    print("Going to list..")
                else:
                    z = open("config/basic.conf")
                    y = z.readlines()
                    if not len(y) >= 3:
                        a = open("config/basic.temp", "w+")
                        b = raw_input("What do you want your ISO's name to be called?> ")
                        y.append(b + "\n")
                        a.writelines(y)
                        z.close()
                        a.close()
                        os.remove("basic.conf")
                        os.rename("basic.temp", "basic.conf")
                    z.close()
                    c = map(lambda s: s.strip(), y)
                    print("Done with general modding. Starting with IMGBurn..")
                    os.system("move " + ibrn + ".")
                    os.system("imgburn.exe /MODE BUILD /SRC miso /DEST " + c[2] + ".iso /FILESYSTEM \"ISO9660 + UDF \" /UDFREVISION \"1.02\" /NOIMAGEDETAILS /ROOTFOLDER YES /VOLUMELABEL \"MISO\" /OVERWRITE YES /START /CLOSE")
                    os.system("move imgburn.exe config/ibrn")
                    print("Done! Exported to " + c[2] + ".iso.")
                    break
        if not ex:
            os.system("pause")
    elif ch == "3":
        #tbh, very near same to ch 2
        os.chdir("config/mds")
        frink = open("on.conf", "r")
        mds = frink.readlines()
        if len(mds) == 0:
            print("No mods are active.")
            os.system("pause")
        else:
            os.chdir("../../mods")
            mds = map(lambda s: s.strip(), mds)
            wadl = mds
            mdl = []
            for x in mds:
                md = linecache.getline(x + "/mod.inf", 1)
                mdl.append(md)
            mdl = map(lambda s: s.strip(), mdl)
            while True:
                print("")
                print("Active mods:")
                print('\n'.join(mdl))
                print("")
                m = raw_input("Which mod?> ")
                if not m in mdl:
                    print("Mod doesnt exist.")
                    os.system("pause")
                else:
                    break
            blo = mdl.index(m)
            ate = mds[int(blo)]
            os.chdir(ate)
            pips = linecache.getline("mod.inf", 5)
            pips = ast.literal_eval(pips)
            os.chdir("../..")
            os.chdir("config/mds")
            with open('on.temp', 'w+') as hh:
                for x in wadl:
                    if not x == ate:
                        hh.write(x + "\n")
            frink.close()
            os.remove("on.conf")
            os.rename("on.temp", "on.conf")
            os.chdir("../..")
            for x in pips:
                if '.' in x:
                    if os.path.isfile("miso\\" + x):
                        os.remove("miso\\" + x)
                    os.system("copy /y ogiso\\" + x + " miso\\" + x)
            print("Un-applying mod..")
            print("Would you like to add more? (Y if yes)")
            mmm = getch()
            if mmm == "y":
                os.chdir("mods")
                print("Going to list..")
            else:
                z = open("config/basic.conf")
                y = z.readlines()
                if not len(y) >= 3:
                    a = open("config/basic.temp", "w+")
                    b = raw_input("What do you want your ISO's name to be called?> ")
                    y.append(b + "\n")
                    a.writelines(y)
                    z.close()
                    a.close()
                    os.remove("basic.conf")
                    os.rename("basic.temp", "basic.conf")
                c = map(lambda s: s.strip(), y)
                print("Done with general modding. Starting with IMGBurn..")
                os.system("move " + ibrn + ".")
                os.system("imgburn.exe /MODE BUILD /SRC miso /DEST " + c[2] + ".iso /FILESYSTEM \"ISO9660 + UDF \" /UDFREVISION \"1.02\" /NOIMAGEDETAILS /ROOTFOLDER YES /VOLUMELABEL \"MISO\" /OVERWRITE YES /START /CLOSE")
                os.system("move imgburn.exe config/ibrn")
                print("Done! Exported to " + c[2] + ".iso.")
                os.system("pause")
                break
    elif ch == "4":
        print("")
        print(open("temp/news.txt").read())
        print("")
        os.system("pause")
    elif ch == "5":
        print("Refreshing mods..")
        hahayes = os.listdir("mods")
        yeshaha = open("config/mods.conf", "w")
        yeshaha.truncate()
        for x in hahayes:
            yeshaha.write(x + "\n")
        yeshaha.close()
    elif ch == "6":
        os.chdir("config")
        x = "1"
        ob = ""
        n = ""
        z = open("basic.conf")
        a = open("basic.temp", "w+")
        while True:
            if n == "true":
                z.close()
                a.close()
                os.remove("basic.temp")
                os.chdir("..")
                break
            os.system("cls")
            z = open("basic.conf")
            y = z.readlines()
            b = map(lambda s: s.strip(), y)
            a = open("basic.temp", "w+")
            print("There isn't much here yet, but as I make create, there should be more popping up.")
            print("Options (up, down, or enter (esc to exit)):")
            o1 = " Region:    "
            o2 = " Mode:      "
            o3 = " ISO name:  "
            while True:
                exec("ob = o" + x)
                ob = list(ob)
                ob[0] = ">"
                ob = "".join(ob)
                exec("o" + x + " = ob")
                print(o1 + b[0])
                print(o2 + b[1])
                try: 
                    iso = b[2]
                except IndexError:
                    iso = "[NONE SPECIFIED]"
                print(o3 + iso)
                opc = ord(getch())
                if opc == 224:
                    x = int(x)
                    opd = ord(getch())
                    if opd == 80:    
                        x = x + 1
                        if x > 3:
                            x = 3
                    if opd == 72:
                        x = x - 1
                        if x < 1:
                            x = 1
                elif opc == 13:
                    x = int(x)
                    w = x - 1
                    if x == 1:
                        print("Pleae put either PAL or NTSC matching with your iso or else it will not work.")
                    elif x == 2:
                        print("Please put c for create more or b for basic mode.")
                    opm = raw_input("New value?> ")
                    if x == 2 and opm == "c":
                        cre = True
                    else:
                        cre = False
                    if x == 3 and iso == "[NONE SPECIFIED]":
                        y.append(opm + "\n")
                    else:
                        y[w] = opm + "\n"
                    a.writelines(y)
                    z.close()
                    a.close()
                    os.remove("basic.conf")
                    os.rename("basic.temp", "basic.conf")
                elif opc == 27:
                    n = "true"
                x = str(x)
                break
    elif ch == "7":
        exit()
    elif ch == "8":
        print("Due to auto updating being removed, you must now update it manually.")
        os.system("pause")
        webbrowser.open("https://github.com/MGRich/PTR2Modder/releases")
        exit()
    elif ch == "c":
        ba = False
        while True:
            if ba:
                print("Going to basic..")
                break
            else:
                os.system("cls")
                print("")
                colorf(bcyan)
                print("PTR2Modder - CREATE")
                print("")
                opt = ["1", "2", "3", "b"]
                if d and cre:
                    opt.append("c")
                while True:
                    colorf(reset)
                    print("1. Create mod")
                    print("2. Manage mods (WIP)")
                    print("3. Options")
                    print("B. Basic")
                    ch = getch()
                    if not ch in opt:
                        print("Invalid answer")
                        time.sleep(3)
                        os.system("cls")
                        print("")
                        colorf(bcyan)
                        print("PTR2Modder - CREATE")
                        print("")
                    else:
                        break
            if ch == "b":
                ba = True
            elif ch == "1":
                with open("config/create.conf") as x:
                    crtc = x.readlines()
                os.chdir(crtc[0][:-1])
                a = raw_input("What do you want the mods' folder to be called?> ")
                os.mkdir(a)
                os.chdir(a)
                print("Now to setup the BASIC configuration:")
                m = open("mod.inf", "w+")
                h1 = str(raw_input("Name of mod> "))
                h2 = str(raw_input("Author> "))
                h3 = str(raw_input("Version> "))
                h4 = str(raw_input("Description> "))
                m.write(h1 + "\n" + h2 + "\n" + h3 + "\n" + h4 + "\n[]\n" + str(linecache.getline(conf, 1)) + "\n[]\n[]")
                m.close()
                print("Mod is now ready for editing. Launching the mod editor.")
                os.system("pause")
                mod1 = a
                os.chdir("../..")
                if os.path.isfile("ptr2modder.py"):
                    subprocess.Popen('modman.py' + a + crtc[0][:-1], shell=True)
                else:
                    subprocess.Popen('modman.exe' + a + crtc[0][:-1], shell=True)
            elif ch == "3":
                os.chdir("config")
                x = "1"
                ob = ""
                n = ""
                while True:
                    if n == "true":
                        if os.path.isfile("create.temp"):
                            os.remove("create.temp")
                        os.chdir("..")
                        break
                    os.system("cls")
                    with open("create.conf") as z:
                        y = z.readlines()
                        b = map(lambda s: s.strip(), y)
                    print("Options (up, down, or enter (esc to exit)):")
                    o1 = " Workspace:  "
                    while True:
                        exec("ob = o" + x)
                        ob = list(ob)
                        ob[0] = ">"
                        ob = "".join(ob)
                        exec("o" + x + " = ob")
                        for v in range(0,1):
                            try: 
                                b[v] = b[v]
                            except IndexError:
                                b.append("[NONE SPECIFIED]")
                        print(o1 + b[0])
                        opc = ord(getch())
                        if opc == 224:
                            x = int(x)
                            opd = ord(getch())
                            #if opd == 80:    
                            #    x = x + 1
                            #    if x > 1:
                            #        x = 1
                            #if opd == 72:
                            #    x = x - 1
                            #    if x < 1:
                            #        x = 1
                        elif opc == 13:
                            x = int(x)
                            w = x - 1
                            opm = raw_input("New value?> ")
                            if b[w] == "[NONE SPECIFIED]":
                                y.append(opm + "\n")
                            else:
                                y[w] = opm + "\n"
                            with open("create.temp", "w+") as a:
                                a.writelines(y)
                            os.remove("create.conf")
                            os.rename("create.temp", "create.conf")
                        elif opc == 27:
                            n = "true"
                        x = str(x)
                        break
