#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
pyBristol - a python and tkinter based GUI for bristol - anything else but mono

author: adorableGNU
mail: adorablegnu@hushmail.com
Copyright (C) 2014, 2015

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

import sys, subprocess, configparser, shutil, os.path
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

__version__ = "1.0.33"
SETTINGS_CONF = os.path.join(os.path.expanduser("~"), ".config", "pyBristol", "settings.conf")

class pyBristol:
    '''
    Main-Class for pyBristol.
    '''
    def __init__(self):
        self.configFile()
        self.tkRoot()
        self.cVars = StringVar()
        self.bModel = StringVar()
        self.bDriver = StringVar()
        self.bRate = StringVar()
        self.bPriority = StringVar()
        self.bVelocity = StringVar()
        self.bJackA = StringVar()
        self.bIgainDef = StringVar()
        self.bOgainDef = StringVar()
        self.bVoicesDef = StringVar()
        self.bMono = StringVar()
        self.bChannelDef = StringVar()
        self.bMemory = StringVar()
        self.bArgs = StringVar()
        self.getSettings()
        self.tkFrames()
        self.r = 0
        self.c = 0
        self.tkMenu()
        self.keyboardShortcuts()
        self.generateModels()
        self.driver()
        self.jackAutoconnect()
        self.sampleRate()
        self.priority()
        self.velocity()
        self.inputGain()
        self.outputGain()
        self.voices()
        self.midiChannel()
        self.loadMemory()
        self.additionalArguments()
        self.thumbnail()
        self.commandline()
        self.startButton()
        self.stopButton()
        self.exitButton()
        self.setCvars()

    def getSettings(self):
        for var in self.bSettings:
            self.__dict__[var].set(self.bSettings.get(var))
        return

    def setDefaultConf(self):
        if not os.path.exists(os.path.dirname(SETTINGS_CONF)):
             os.makedirs(os.path.dirname(SETTINGS_CONF))
        shutil.copyfile("default.conf", SETTINGS_CONF)

    def setCvars(self, *args):
        bMod = self.bModel.get()
        if bMod != "b3":
            Model = " -" + bMod
        else:
            Model = ""
        bDri = self.bDriver.get()
        Driver = " -" + bDri
        bJa = self.bJackA.get()
        autoconn = ""
        if bDri == "jack" or bDri == "jko":
            self.bJackAbutton.config(state="normal")
            jackName = " -audiodev bristol_" + bMod
            if bJa == "1":
                autoconn = " -autoconn"
        else:
            self.bJackAbutton.config(state="disabled")
            jackName = ""
        bRa = self.bRate.get()
        if bRa != "44100":
            SampleRate = " -rate " + bRa
        else:
            SampleRate = ""
        bPrio = self.bPriority.get()
        if bPrio != "75":
            Priority = " -priority " + bPrio
        else:
            Priority = ""
        bVelo = self.bVelocity.get()
        if bVelo != "520":
            Velocity = " -velocity " + bVelo
        else:
            Velocity = ""
        bIg = self.bIgain.get()
        if bIg != "4":
            InputGain = " -ingain " + bIg
        else:
            InputGain = ""
        bOg = self.bOgain.get()
        if bOg != "4":
            OutputGain = " -outgain " + bOg
        else:
            OutputGain = ""
        bMo = self.bMono.get()
        if bMo == "1":
            voices = " -mono"
            self.bVoices.config(state="disabled")
        else:
            bVoi = self.bVoices.get()
            if bVoi != "32":
                voices = " -voices " + bVoi
            else:
                voices = ""
            self.bVoices.config(state="normal")
        bCh = self.bChannel.get()
        if bCh != "1":
            MidiChannel = " -channel " + bCh
        else:
            MidiChannel = ""
        bMem = self.bMemory.get()
        if bMem != "0":
            MemoryBank = " -load " + bMem
        else:
            MemoryBank = ""
        ExtraArgs = " " + self.bArgs.get()
        self.cVars.set("startBristol" + Model
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
        img = bMod + ".gif"
        imgPath = os.path.join(os.path.curdir, "gif", img)
        self.bImg.configure(file=imgPath)
        return

    def bSave(self):
        with open(SETTINGS_CONF, "w") as confFile:
            confFile.write("[SETTINGS]\n")
            for var in self.bSettings:
                confFile.write(var + " = " + self.__dict__[var].get() + "\n")
        messagebox.showinfo(title="Your config was saved...", message="The current settings will get loaded automatically next time.")
        return

    def bRestore(self):
        bReset = messagebox.askyesno(title="Restoring default-settings...", message="Warning: If you proceed, all your settings will get lost. Do you wish to continue?")
        if bReset > 0:
            self.setDefaultConf()
            self.configFile()
            self.getSettings()
            self.setCvars()
        return

    def exitAll(self):
        mExit = messagebox.askokcancel(title="Exit", message="pyBristol will exit now...")
        if mExit > 0:
            self.stopBristol()
            self.bGui.destroy()
            sys.exit()
        return

    def bGuiHelp(self):
        bGuiHelp = Toplevel(self.bGui)
        bGuiHelp.geometry("730x400+100+100")
        bGuiHelp.resizable(0, 0)
        bGuiHelp.title("pyBristol Gui-Helppage")
        guiScrollBar = ttk.Scrollbar(bGuiHelp)
        guiScrollBar.pack(side=RIGHT, fill=Y)
        bGuiWrapper = Text(bGuiHelp, bg="white", fg="black")
        guihelp = os.path.join(os.path.curdir, "doc", "guihelp")
        with open(guihelp, "r") as bGuiFile:
            bGuiText = bGuiFile.read()
        bGuiWrapper.insert(END, bGuiText)
        bGuiWrapper.config(state=DISABLED, yscrollcommand=guiScrollBar.set)
        guiScrollBar.config(command=bGuiWrapper.yview)
        bGuiWrapper.pack(expand=1, fill=BOTH)
        bGuiHelp.bind("<Escape>", lambda e: bGuiHelp.destroy())
        return

    def bMan(self):
        bShowMan = Toplevel(self.bGui)
        bShowMan.geometry("730x400+100+100")
        bShowMan.title("Bristol Manpage")
        manScrollBar = ttk.Scrollbar(bShowMan)
        manScrollBar.pack(side=RIGHT, fill=Y)
        bManWrapper = Text(bShowMan, bg="white", fg="black")
        docPath = os.path.join(os.path.curdir, "doc", "bristolMan")
        with open(docPath, "r") as bManFile:
            bManText = bManFile.read()
        bManWrapper.insert(END, bManText)
        bManWrapper.config(state=DISABLED, yscrollcommand=manScrollBar.set)
        manScrollBar.config(command=bManWrapper.yview)
        bManWrapper.pack(expand=1, fill=BOTH)
        bShowMan.bind("<Escape>", lambda e: bShowMan.destroy())
        return

    def bReadme(self):
        bMod = self.bModel.get()
        bShowRM = Toplevel(self.bGui)
        bShowRM.geometry("600x400+100+100")
        bShowRM.title(bMod)
        rmScrollBar = ttk.Scrollbar(bShowRM)
        rmScrollBar.pack(side=RIGHT, fill=Y)
        bRMwrapper = Text(bShowRM, bg="white", fg="black")
        rmFile = os.path.join(os.path.curdir, "doc", bMod)
        with open(rmFile, "r") as bRMfile:
            bRMtext = bRMfile.read()
        bRMwrapper.insert(END, bRMtext)
        bRMwrapper.config(state=DISABLED, yscrollcommand=rmScrollBar.set)
        rmScrollBar.config(command=bRMwrapper.yview)
        bRMwrapper.pack(expand=1, fill=BOTH)
        bShowRM.bind("<Escape>", lambda e: bShowRM.destroy())
        return

    def bAbout(self):
        messagebox.showinfo(title="About", message="pyBristol -- Version %s --\nanything else but mono\n\nThis program comes with ABSOLUTELY NO WARRANTY.\nThis is free software, and you\nare welcome to redistribute it\nunder certain conditions." % (__version__))
        return

    def runBristol(self):
        cLine = self.cVars.get()
        cArgs = cLine.split()
        subprocess.Popen(cArgs)
        return

    def stopBristol(self):
        subprocess.Popen(["startBristol", "-exit"])
        return

    def configFile(self):
        if not os.path.isfile(SETTINGS_CONF):
            self.setDefaultConf()
        config = configparser.ConfigParser()
        config.optionxform = str
        config.read(SETTINGS_CONF)
        self.bSettings = config["SETTINGS"]

    def tkRoot(self):
        self.bGui = Tk()
        self.bGui.geometry("850x500+150+100")
        self.bGui.resizable(0, 0)
        self.bGui.title("Python based GUI for Bristol")
        iconfile = os.path.join(os.path.curdir, "icon", "pyBristol.gif")
        icon = Image("photo", file=iconfile)
        self.bGui.call("wm", "iconphoto", self.bGui._w, icon)

    def tkFrames(self):
        self.frameA = Frame(self.bGui)
        self.frameA.pack(expand=1, fill=BOTH)
        self.frameB = Frame(self.bGui)
        self.frameB.pack(expand=1, fill=BOTH)
        self.frameB0 = Frame(self.frameB)
        self.frameB0.grid(row=0, column=0, padx=20)
        self.frameB1 = Frame(self.frameB)
        self.frameB1.grid(row=0, column=1, padx=20)
        self.frameB2 = Frame(self.frameB)
        self.frameB2.grid(row=0, column=2, padx=2, pady=5, sticky=E)
        self.frameC = Frame(self.bGui)
        self.frameC.pack(expand=1, fill=BOTH)
        self.frameD = Frame(self.bGui)
        self.frameD.pack(expand=1, fill=BOTH)
        #columnconfiguration
        self.frameA.columnconfigure(0, weight=1)
        self.frameA.columnconfigure(1, weight=1)
        self.frameA.columnconfigure(2, weight=1)
        self.frameB.columnconfigure(0, weight=1)
        self.frameB.columnconfigure(1, weight=1)
        self.frameB.columnconfigure(2, weight=1)
        self.frameC.columnconfigure(0, weight=1)
        self.frameD.columnconfigure(0, weight=1)
        self.frameD.columnconfigure(1, weight=1)
        self.frameD.columnconfigure(2, weight=1)

    def tkMenu(self):
        bMenu = Menu(self.bGui, fg="black")
        #menu > file
        bMfile = Menu(bMenu, tearoff=0, fg="black")
        bMfile.add_command(label="Save Config", command=self.bSave, underline=0, accelerator="Crtl+S")
        bMfile.add_command(label="Restore Defaults", command=self.bRestore, underline=8, accelerator="Crtl+D")
        bMfile.add_command(label="Exit", command=self.exitAll, underline=1, accelerator="Crtl+Q/X")
        bMenu.add_cascade(label="File", menu=bMfile, underline= 0 )
        #menu > run
        bMrun = Menu(bMenu, tearoff=0, fg="black")
        bMrun.add_command(label="Run Bristol", command=self.runBristol, underline=0, accelerator="F5")
        bMrun.add_command(label="Stop Bristol", command=self.stopBristol, underline=2, accelerator="F6")
        bMenu.add_cascade(label="Run", menu=bMrun, underline=0)
        #menu > help
        bMhelp = Menu(bMenu, tearoff=0, fg="black")
        bMhelp.add_command(label="GUI-Help", command=self.bGuiHelp, underline=0, accelerator="F1")
        bMhelp.add_command(label="Bristol Manpage", command=self.bMan, underline=8, accelerator="Crtl+M")
        bMhelp.add_command(label="Current Synth", underline=0, command=self.bReadme, accelerator="Crtl+H")
        bMhelp.add_command(label="About", command=self.bAbout, underline=1)
        bMenu.add_cascade(label="Help", menu=bMhelp, underline=0)
        #adding menu
        self.bGui.config(menu=bMenu)

    def keyboardShortcuts(self):
        self.bGui.bind("<Control-s>", lambda e: self.bSave())
        self.bGui.bind("<Control-d>", lambda e: self.bRestore())
        self.bGui.bind_all("<Control-q>", lambda e: self.exitAll())
        self.bGui.bind_all("<Control-x>", lambda e: self.exitAll())
        self.bGui.bind("<F1>", lambda e: self.bGuiHelp())
        self.bGui.bind("<Control-m>", lambda e: self.bMan())
        self.bGui.bind("<Control-h>", lambda e: self.bReadme())
        self.bGui.bind("<F5>", lambda e: self.runBristol())
        self.bGui.bind("<F6>", lambda e: self.stopBristol())

    def generateModels(self): 
        bModelList = [("mini", "moog mini"),
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
            bModelButton = Radiobutton(self.frameA,
                                       text=bModH,
                                       variable=self.bModel,
                                       value=bMod,
                                       indicatoron=0,
                                       width=100,
                                       padx=20,
                                       fg="black",
                                       command=self.setCvars)
            bModelButton.grid(row=self.r, column=self.c)
            self.r += 1
            if self.r == 12:
                self.c += 1
                self.r = 0

    def driver(self):
        bLabelDriver = Label(self.frameB0, text=" driver:", fg="black")
        bLabelDriver.grid(row=0, column=0, padx=3, sticky=W)
        bDriverList = ["alsa", "oss", "jack", "jko"]
        for bDri in bDriverList:
            self.r += 1
            if bDri == "jko":
                driText = "jack(channel split)"
            else:
                driText = bDri
            bDriverButton = Radiobutton(self.frameB0,
                                        text=driText,
                                        variable=self.bDriver,
                                        value=bDri,
                                        fg="black",
                                        command=self.setCvars)
            bDriverButton.grid(row=self.r, column=0, sticky=W)

    def jackAutoconnect(self):
        self.bJackAbutton = Checkbutton(self.frameB0,
                                        text="autoconnect",
                                        variable=self.bJackA,
                                        fg="black",
                                        command=self.setCvars)
        self.bJackAbutton.grid(row=5, column=0, padx=2, sticky=W)

    def sampleRate(self):
        bRateLabel = Label(self.frameB0, text="sample rate:", fg="black")
        bRateLabel.grid(row=0, column=1, sticky=W)
        bRateLine = Entry(self.frameB0, textvariable=self.bRate, width=9, fg="black", bg="white")
        bRateLine.grid(row=1, column=1, sticky=W)
        self.bRate.trace("w", self.setCvars)

    def priority(self):
        bPriorityLabel = Label(self.frameB0, text="priority:", fg="black")
        bPriorityLabel.grid(row=2, column=1, sticky=W)
        bPriorityLine = Entry(self.frameB0, textvariable=self.bPriority, width=9, fg="black", bg="white")
        bPriorityLine.grid(row=3, column=1, sticky=W)
        self.bPriority.trace("w", self.setCvars)

    def velocity(self):
        bVelocityLabel = Label(self.frameB0, text="velocity:", fg="black")
        bVelocityLabel.grid(row=4, column=1, sticky=W)
        bVelocityLine = Entry(self.frameB0, textvariable=self.bVelocity, width=9, fg="black", bg="white")
        bVelocityLine.grid(row=5, column=1, sticky=W)
        self.bVelocity.trace("w", self.setCvars)

    def inputGain(self):
        bIgainLabel = Label(self.frameB1, text="input gain:", fg="black")
        bIgainLabel.grid(row=0, column=0, sticky=W)
        self.bIgain = Spinbox(self.frameB1,
                      from_=0,
                      to=20,
                      textvariable=self.bIgainDef,
                      width=3,
                      fg="black",
                      bg="white",
                      command=self.setCvars)
        self.bIgain.grid(row=1, column=0, sticky=W)

    def outputGain(self):
        bOgainLabel = Label(self.frameB1, text="output gain:", fg="black")
        bOgainLabel.grid(row=2, column=0, sticky=W)
        self.bOgain = Spinbox(self.frameB1,
                      from_=0,
                      to=20,
                      textvariable=self.bOgainDef,
                      width=3,
                      fg="black",
                      bg="white",
                      command=self.setCvars)
        self.bOgain.grid(row=3, column=0, sticky=W)

    def voices(self):
        bVoicesLabel = Label(self.frameB1, text="voices:", fg="black")
        bVoicesLabel.grid(row=4, column=0, sticky=W)
        self.bVoices = Spinbox(self.frameB1,
                       from_=1,
                       to=128,
                       textvariable=self.bVoicesDef,
                       width=3,
                       fg="black",
                       bg="white",
                       command=self.setCvars)
        self.bVoices.grid(row=5, column=0, sticky=W)
        #mono
        bMonoButton = Checkbutton(self.frameB1,
                                  text="mono",
                                  fg="black",
                                  variable=self.bMono,
                                  command=self.setCvars)
        bMonoButton.grid(row=5, column=0, padx=40, sticky=W)

    def midiChannel(self):
        bChannelLabel = Label(self.frameB1, text="midi channel:", fg="black")
        bChannelLabel.grid(row=0, column=1, sticky=W)
        self.bChannel = Spinbox(self.frameB1,
                        from_=1,
                        to=16,
                        textvariable=self.bChannelDef,
                        width=3,
                        fg="black",
                        bg="white",
                        command=self.setCvars)
        self.bChannel.grid(row=1, column=1, sticky=W)

    def loadMemory(self):
        bMemoryLabel = Label(self.frameB1, text="load memory:", fg="black")
        bMemoryLabel.grid(row=2, column=1, sticky=W)
        bMemoryLine = Entry(self.frameB1, textvariable=self.bMemory, width=4, fg="black", bg="white")
        bMemoryLine.grid(row=3, column=1, sticky=W)
        self.bMemory.trace("w", self.setCvars)

    def additionalArguments(self):
        bArgsLabel = Label(self.frameB1, text="extra arguments:", fg="black")
        bArgsLabel.grid(row=4, column=1, sticky=W)
        bArgsLine = Entry(self.frameB1, textvariable=self.bArgs, width=12, fg="black", bg="white")
        bArgsLine.grid(row=5, column=1, sticky=W)
        self.bArgs.trace("w", self.setCvars)

    def thumbnail(self):
        bMod = self.bModel.get()
        imgPath = os.path.join(os.path.curdir, "gif", bMod + ".gif")
        self.bImg = PhotoImage(file=imgPath)
        bCanvas = Canvas(self.frameB2, height=147, width=277)
        bCanvas.create_image(0, 0, image=self.bImg, anchor=NW)
        bCanvas.pack()

    def commandline(self):
        bLabelCL = Label(self.frameC, text=" commandline:", fg="black")
        bLabelCL.grid(row=0, column=0, sticky=W)
        bCommand = Entry(self.frameC, textvariable=self.cVars, width=300, fg="black", bg="white")
        bCommand.grid(row=1, column=0)

    def startButton(self):
        staButton = ttk.Button(self.frameD, text="start", command=self.runBristol)
        staButton.grid(row=0, column=0)

    def stopButton(self):
        stoButton = ttk.Button(self.frameD, text="stop", command=self.stopBristol)
        stoButton.grid(row=0, column=1)

    def exitButton(self):
        eButton = ttk.Button(self.frameD, text="exit", command=self.exitAll)
        eButton.grid(row=0, column=2)

if __name__ == "__main__":
    PYBRISTOL = pyBristol()
    PYBRISTOL.bGui.mainloop()
