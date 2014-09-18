#!/usr/bin/env python3
'''
pyBristol - a python and tkinter based GUI for bristol - anything else but mono

author: adorableGNU
mail: adorablegnu@hushmail.com
Copyright (C) 2014

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import sys, subprocess, configparser, shutil, os.path, shlex
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
settingsConf = os.path.expanduser("~") + "/.config/pyBristol/settings.conf"

def getSettings():
    for var in bSettings:
        globals()[var].set(bSettings.get(var))
    return

def setDefaultConf():
    if not os.path.exists(os.path.dirname(settingsConf)):
         os.makedirs(os.path.dirname(settingsConf))
    shutil.copyfile("default.conf", settingsConf)

def setCvars(*args):
    bMod = bModel.get()
    if bMod != "b3":
        Model = " -" + bMod
    else:
        Model = ""
    bDri = bDriver.get()
    Driver = " -" + bDri
    bJa = bJackA.get()
    autoconn = ""
    if bDri == "jack" or bDri == "jko":
        bJackAbutton.config(state="normal")
        jackName = " -audiodev bristol_" + bMod
        if bJa == "1":
            autoconn = " -autoconn"
    else:
        bJackAbutton.config(state="disabled")
        jackName = ""
    bRa = bRate.get()
    if bRa != "44100":
        SampleRate = " -rate " + bRa
    else:
        SampleRate = ""
    bPrio = bPriority.get()
    if bPrio != "75":
        Priority = " -priority " + bPrio
    else:
        Priority = ""
    bVelo = bVelocity.get()
    if bVelo != "520":
        Velocity = " -velocity " + bVelo
    else:
        Velocity = ""
    bIg = bIgain.get()
    if bIg != "4":
        InputGain = " -ingain " + bIg
    else:
        InputGain = ""
    bOg = bOgain.get()
    if bOg != "4":
        OutputGain = " -outgain " + bOg
    else:
        OutputGain = ""
    bMo = bMono.get()
    if bMo == "1":
        voices = " -mono"
        bVoices.config(state="disabled")
    else:
        bVoi = bVoices.get()
        if bVoi != "32":
            voices = " -voices " + bVoi
        else:
            voices = ""
        bVoices.config(state="normal")
    bCh = bChannel.get()
    if bCh != "1":
        MidiChannel = " -channel " + bCh
    else:
        MidiChannel = ""
    bMem = bMemory.get()
    if bMem != "0":
        MemoryBank = " -load " + bMem
    else:
        MemoryBank = ""
    ExtraArgs = " " + bArgs.get()
    cVars.set("startBristol" + Model
                             + Driver
                             + jackName
                             + autoconn
                             + SampleRate
                             + Priority
                             + Velocity
                             + InputGain
                             + OutputGain
                             + voices
                             + MidiChannel
                             + MemoryBank
                             + ExtraArgs)
    imgPath = "./gif/" + bMod + ".gif"
    bImg.configure(file = imgPath)
    return


def bSave():
    with open(settingsConf, "w") as confFile:
        confFile.write("[SETTINGS]\n")
        for var in bSettings:
            confFile.write(var + " = " + globals()[var].get() + "\n")
    messagebox.showinfo(title = "Your config was saved...", message = "The actual settings will be loaded automatically next time.")
    return


def bRestore():
    bReset = messagebox.askyesno(title = "Restoring Default-Settings...", message = "Warning: If you proceed, all your settings will get lost. Do you wish to continue?")
    if bReset > 0:
        setDefaultConf()
        config.read(settingsConf)
        getSettings()
        setCvars()
    return


def exitAll():
    mExit = messagebox.askokcancel(title = "Exit", message = "pyBristol will exit now...")
    if mExit > 0:
        stopBristol()
        bGui.destroy()
        sys.exit()
    return


def bGuiHelp():
    bGuiHelp = Toplevel(bGui)
    bGuiHelp.geometry("730x400+100+100")
    bGuiHelp.resizable(0, 0)
    bGuiHelp.title("pyBristol Gui-Helppage")
    guiScrollBar = ttk.Scrollbar(bGuiHelp)
    guiScrollBar.pack(side = RIGHT, fill = Y)
    bGuiWrapper = Text(bGuiHelp, bg = "white", fg = "black")
    with open("./doc/guihelp", "r") as bGuiFile:
        bGuiText = bGuiFile.read()
    bGuiWrapper.insert(END, bGuiText)
    bGuiWrapper.config(state = DISABLED, yscrollcommand = guiScrollBar.set)
    guiScrollBar.config(command = bGuiWrapper.yview)
    bGuiWrapper.pack(expand = 1, fill = BOTH)
    bGuiHelp.bind("<Escape>", lambda e: bGuiHelp.destroy())
    return


def bMan():
    bShowMan = Toplevel(bGui)
    bShowMan.geometry("730x400+100+100")
    bShowMan.title("Bristol Manpage")
    manScrollBar = ttk.Scrollbar(bShowMan)
    manScrollBar.pack(side = RIGHT, fill = Y)
    bManWrapper = Text(bShowMan, bg = "white", fg = "black")
    with open("./doc/bristolMan", "r") as bManFile:
        bManText = bManFile.read()
    bManWrapper.insert(END, bManText)
    bManWrapper.config(state = DISABLED, yscrollcommand = manScrollBar.set)
    manScrollBar.config(command = bManWrapper.yview)
    bManWrapper.pack(expand = 1, fill = BOTH)
    bShowMan.bind("<Escape>", lambda e: bShowMan.destroy())
    return


def bReadme():
    bMod = bModel.get()
    bShowRM = Toplevel(bGui)
    bShowRM.geometry("600x400+100+100")
    bShowRM.title(bMod)
    rmScrollBar = ttk.Scrollbar(bShowRM)
    rmScrollBar.pack(side = RIGHT, fill = Y)
    bRMwrapper = Text(bShowRM, bg = "white", fg = "black")
    rmFile = "./doc/" + bMod
    with open(rmFile, "r") as bRMfile:
        bRMtext = bRMfile.read()
    bRMwrapper.insert(END, bRMtext)
    bRMwrapper.config(state = DISABLED, yscrollcommand = rmScrollBar.set)
    rmScrollBar.config(command = bRMwrapper.yview)
    bRMwrapper.pack(expand = 1, fill = BOTH)
    bShowRM.bind("<Escape>", lambda e: bShowRM.destroy())
    return


def bAbout():
    messagebox.showinfo(title = "About", message="pyBristol -- Version 1.0.25 --\nanything else but mono\n\nCopyright (C) 2014, adorableGNU\n\nThis program comes with ABSOLUTELY NO WARRANTY.\nThis is free software, and you\nare welcome to redistribute it\nunder certain conditions.")
    return


def runBristol():
    cLine = cVars.get()
    cArgs = shlex.split(cLine)
    subprocess.Popen(cArgs)
    return


def stopBristol():
    subprocess.Popen(["/usr/bin/startBristol", "-exit"])
    return


#configFile
if not os.path.isfile(settingsConf):
    setDefaultConf()
config = configparser.ConfigParser()
config.optionxform = str
config.read(settingsConf)
bSettings = config["SETTINGS"]


#root
bGui = Tk()
bGui.geometry("850x500+150+100")
bGui.resizable(0, 0)
bGui.title("Python based GUI for Bristol")
icon = Image("photo", file = "icon/pyBristol.gif")
bGui.call("wm", "iconphoto", bGui._w, icon)


#frames
frameA = Frame(bGui)
frameA.pack(expand = 1, fill = BOTH)
frameB = Frame(bGui)
frameB.pack(expand = 1, fill = BOTH)
frameB0 = Frame(frameB)
frameB0.grid(row = 0, column = 0, padx = 20)
frameB1 = Frame(frameB)
frameB1.grid(row = 0, column = 1, padx = 20)
frameB2 = Frame(frameB)
frameB2.grid(row = 0, column = 2, padx = 2, pady = 5, sticky = E)
frameC = Frame(bGui)
frameC.pack(expand = 1, fill = BOTH)
frameD = Frame(bGui)
frameD.pack(expand = 1, fill = BOTH)
#columnconfiguration
frameA.columnconfigure(0, weight = 1)
frameA.columnconfigure(1, weight = 1)
frameA.columnconfigure(2, weight = 1)
frameB.columnconfigure(0, weight = 1)
frameB.columnconfigure(1, weight = 1)
frameB.columnconfigure(2, weight = 1)
frameC.columnconfigure(0, weight = 1)
frameD.columnconfigure(0, weight = 1)
frameD.columnconfigure(1, weight = 1)
frameD.columnconfigure(2, weight = 1)


#menu
bMenu = Menu(bGui, fg = "black")
#menu > file
bMfile = Menu(bMenu, tearoff = 0, fg = "black")
bMfile.add_command(label = "Save Config", command = bSave, underline = 0, accelerator = "Crtl+S")
bMfile.add_command(label = "Restore Defaults", command = bRestore, underline = 8, accelerator = "Crtl+D")
bMfile.add_command(label = "Exit", command = exitAll, underline = 1, accelerator = "Crtl+Q/X")
bMenu.add_cascade(label = "File", menu = bMfile, underline= 0 )
#menu > run
bMrun = Menu(bMenu, tearoff = 0, fg = "black")
bMrun.add_command(label = "Run Bristol", command = runBristol, underline = 0, accelerator = "F5")
bMrun.add_command(label = "Stop Bristol", command = stopBristol, underline = 2, accelerator = "F6")
bMenu.add_cascade(label = "Run", menu = bMrun, underline = 0)
#menu > help
bMhelp = Menu(bMenu, tearoff = 0, fg = "black")
bMhelp.add_command(label = "GUI-Help", command = bGuiHelp, underline = 0, accelerator = "F1")
bMhelp.add_command(label = "Bristol Manpage", command = bMan, underline = 8, accelerator = "Crtl+M")
bMhelp.add_command(label = "Current Synth", underline = 0, command = bReadme, accelerator = "Crtl+H")
bMhelp.add_command(label = "About", command = bAbout, underline = 1)
bMenu.add_cascade(label = "Help", menu = bMhelp, underline = 0)
#adding menu
bGui.config(menu = bMenu)


#keyboard-shortcuts
bGui.bind("<Control-s>", lambda e: bSave())
bGui.bind("<Control-d>", lambda e: bRestore())
bGui.bind_all("<Control-q>", lambda e: exitAll())
bGui.bind_all("<Control-x>", lambda e: exitAll())
bGui.bind("<F1>", lambda e: bGuiHelp())
bGui.bind("<Control-m>", lambda e: bMan())
bGui.bind("<Control-h>", lambda e: bReadme())
bGui.bind("<F5>", lambda e: runBristol())
bGui.bind("<F6>", lambda e: stopBristol())


#variables
cVars = StringVar()
bModel = StringVar()
bDriver = StringVar()
bRate = StringVar()
bPriority = StringVar()
bVelocity = StringVar()
bJackA = StringVar()
bIgainDef = StringVar()
bOgainDef = StringVar()
bVoicesDef = StringVar()
bMono = StringVar()
bChannelDef = StringVar()
bMemory = StringVar()
bArgs = StringVar()
r = 0
c = 0
getSettings()


#list: sythesizer-models 
bModelList = [
    ("mini", "moog mini"),
    ("explorer", "moog voyager"),
    ("voyager", "moog voyager electric blue"),
    ("memory", "moog memory"),
    ("sonic6", "moog sonic 6"),
    ("mg1", "moog/realistic mg-1 concertmate"),
    ("b3", "hammond B3"),
    ("prophet", "sequential circuits prophet-5"),
    ("pro52", "sequential circuits prophet-5/fx"),
    ("pro10", "sequential circuits prophet-10"),
    ("pro1", "sequential circuits pro-one"),
    ("rhodes", "fender rhodes mark-I stage 73"),
    ("rhodesbass", "fender rhodes bass piano"),
    ("roadrunner", "crumar roadrunner electric piano"),
    ("bitone", "crumar bit 01"),
    ("bit99", "crumar bit 99"),
    ("bit100", "crumar bit + mods"),
    ("stratus", "crumar stratus synth/organ combo"),
    ("trilogy", "crumar trilogy synth/organ/string combo"),
    ("obx", "oberheim OB-X"),
    ("obxa", "oberheim OB-Xa"),
    ("axxe", "arp axxe"),
    ("odyssey", "arp odyssey"),
    ("arp2600", "arp 2600"),
    ("solina", "arp/solina string ensemble"),
    ("polysix", "korg polysix"),
    ("poly800", "korg poly-800"),
    ("monopoly", "korg mono/poly"),
    ("vox", "vox continental"),
    ("voxM2", "vox continental super/300/II"),
    ("juno", "roland juno-60"),
    ("jupiter", "roland jupiter-8"),
    ("bme700", "baumann bme-700"),
    ("bm", "bristol bassmaker sequencer (broken)"),
    ("dx", "yamaha dx-7"),
    ("sidney", "commodore-64 SID chip synth")]
for bMod, bModH in bModelList:
    bModelButton = Radiobutton(frameA,
                               text = bModH,
                               variable = bModel,
                               value = bMod,
                               indicatoron = 0,
                               width = 100,
                               padx = 20,
                               fg = "black",
                               command = setCvars)
    bModelButton.grid(row = r, column = c)
    r += 1
    if r == 12:
        c += 1
        r = 0


#Driver
bLabelDriver = Label(frameB0, text = " driver:", fg = "black")
bLabelDriver.grid(row = 0, column = 0, padx = 3, sticky = W)
bDriverList = [ "alsa", "oss", "jack", "jko" ]
for bDri in bDriverList:
    r += 1
    if bDri == "jko":
        driText = "jack(channel split)"
    else:
        driText = bDri
    bDriverButton = Radiobutton(frameB0,
                                text = driText,
                                variable = bDriver,
                                value = bDri,
                                fg = "black",
                                command = setCvars)
    bDriverButton.grid(row = r, column = 0, sticky = W)


#jack-autoconnect
bJackAbutton = Checkbutton(frameB0,
                           text="autoconnect",
                           variable = bJackA,
                           fg = "black",
                           command = setCvars)
bJackAbutton.grid(row = 5, column = 0, padx = 2, sticky = W)


#SampleRate
bRateLabel = Label(frameB0, text="sample rate:", fg = "black")
bRateLabel.grid(row = 0, column = 1, sticky = W)
bRateLine = Entry(frameB0, textvariable = bRate, width = 9, fg = "black", bg = "white")
bRateLine.grid(row = 1, column = 1, sticky = W)
bRate.trace("w", setCvars)


#Prority
bPriorityLabel = Label(frameB0, text="priority:", fg = "black")
bPriorityLabel.grid(row = 2, column = 1, sticky = W)
bPriorityLine = Entry(frameB0, textvariable = bPriority, width = 9, fg = "black", bg = "white")
bPriorityLine.grid(row = 3, column = 1, sticky = W)
bPriority.trace("w", setCvars)


#Velocity
bVelocityLabel = Label(frameB0, text="velocity:", fg = "black")
bVelocityLabel.grid(row = 4, column = 1, sticky = W)
bVelocityLine = Entry(frameB0, textvariable = bVelocity, width = 9, fg = "black", bg = "white")
bVelocityLine.grid(row = 5, column = 1, sticky = W)
bVelocity.trace("w", setCvars)


#InputGain
bIgainLabel = Label(frameB1, text="input gain:", fg = "black")
bIgainLabel.grid(row = 0, column = 0, sticky = W)
bIgain = Spinbox(frameB1,
                 from_ = 0,
                 to = 20,
                 textvariable = bIgainDef,
                 width = 3,
                 fg = "black",
                 bg = "white",
                 command = setCvars)
bIgain.grid(row = 1, column = 0, sticky = W)


#OutputGain
bOgainLabel = Label(frameB1, text="output gain:", fg = "black")
bOgainLabel.grid(row = 2, column = 0, sticky = W)
bOgain = Spinbox(frameB1,
                 from_ = 0,
                 to = 20,
                 textvariable = bOgainDef,
                 width = 3,
                 fg = "black",
                 bg = "white",
                 command = setCvars)
bOgain.grid(row = 3, column = 0, sticky = W)


#Voices
bVoicesLabel = Label(frameB1, text="voices:", fg = "black")
bVoicesLabel.grid(row = 4, column = 0, sticky = W)
bVoices = Spinbox(frameB1,
                  from_ = 1,
                  to = 128,
                  textvariable = bVoicesDef,
                  width = 3,
                  fg = "black",
                  bg = "white",
                  command = setCvars)
bVoices.grid(row = 5, column = 0, sticky = W)
#mono
bMonoButton = Checkbutton(frameB1,
                          text="mono",
                          fg = "black",
                          variable = bMono,
                          command = setCvars)
bMonoButton.grid(row = 5, column = 0, padx = 40, sticky = W)


#MidiChannel
bChannelLabel = Label(frameB1, text="midi channel:", fg = "black")
bChannelLabel.grid(row = 0, column = 1, sticky = W)
bChannel = Spinbox(frameB1,
                   from_ = 1,
                   to = 16,
                   textvariable = bChannelDef,
                   width = 3,
                   fg = "black",
                   bg = "white",
                   command = setCvars)
bChannel.grid(row = 1, column = 1, sticky = W)


#LoadMemory
bMemoryLabel = Label(frameB1, text = "load memory:", fg = "black")
bMemoryLabel.grid(row = 2, column = 1, sticky = W)
bMemoryLine = Entry(frameB1, textvariable = bMemory, width = 4, fg = "black", bg = "white")
bMemoryLine.grid(row = 3, column = 1, sticky = W)
bMemory.trace("w", setCvars)


#AdditionalArguments
bArgsLabel = Label(frameB1, text="extra arguments:", fg = "black")
bArgsLabel.grid(row = 4, column = 1, sticky = W)
bArgsLine = Entry(frameB1, textvariable = bArgs, width = 12, fg = "black", bg = "white")
bArgsLine.grid(row = 5, column = 1, sticky = W)
bArgs.trace("w", setCvars)


#Thumbnail
bMod = bModel.get()
imgPath = "./gif/" + bMod + ".gif"
bImg = PhotoImage(file = imgPath)
bCanvas = Canvas(frameB2, height = 147, width = 277)
bCanvas.create_image(0, 0, image = bImg, anchor = NW)
bCanvas.pack()


#Commandline
bLabelCL = Label(frameC, text=" commandline:", fg = "black")
bLabelCL.grid(row = 0, column = 0, sticky = W)
bCommand = Entry(frameC, textvariable = cVars, width = 300, fg = "black", bg = "white")
bCommand.grid(row = 1, column = 0)


#Start>Button
startButton = ttk.Button(frameD, text = "start", command = runBristol)
startButton.grid(row = 0, column = 0)


#StopButton
panicButton = ttk.Button(frameD, text = "stop", command = stopBristol)
panicButton.grid(row = 0, column = 1)


#ExitButton
exitButton = ttk.Button(frameD, text = "exit", command = exitAll)
exitButton.grid(row = 0, column = 2)


setCvars()
bGui.mainloop()
