    Vox Continental 300
    -------------------

There is an additional emulator for the later Mark-II, Super, 300 or whatever
model you want to call it. This is probably closest to the 300. It was a 
dual manual organ, the lower manual is a Continental and the upper manual had
a different drawbar configuration, using 8', 4' and 2', another two compound
drawbars that represented 5-1/3'+1-3/5', and 2-2/3'+2'+1' respectively. This
gave upper manual a wider tonic range, plus it had the ability to apply some
percussive controls to two of the drawbars. Now, depending on model, some of 
these values could be different and bristol does not emulate all the different
combinations, it uses the harmonics described above and applies percussive to
the 2' and 5-1/3' harmonics (which is arguably incorrect however it gives
a wider combination of percussive harmonics).

The percussive has 4 controls, these are selectors for the harmonics that will
be driven through the percussive decay (and then no longer respond to the 
drawbars), a decay rate called 'L' which acts as a Longer decay when selected,
and a volume selector called 'S' which stands for Soft. The variables are 
adjustable in the mods section. The mods panel is intended to be hidden as
they are just variable parameters. On the original units these were PCB mounted
pots that were not generally accessible either. The panel is visible when you
turn the power control off, not that I suppress the keyboard or anything when
the power is off, but it gave me something useful do to with this button. The
transparency layer is fixed here and is used to apply some drop shadow and a
few beer spills on the cover.

There is an additional Bass section for those who bought the optional Bass
pedals (my old one had them). The emulation allow the selection of Flute and
Reed strengths, and to select 8' or 8'/16' harmonics. The 'Sustain' control
does not currently operate (0.10.9) but that can be fixed if people request
the feature.

The lower manual responds to the MIDI channel on which the emulation was 
started. The upper manual responds to notes greater than MIDI key 48 on the
next channel up. The Bass section also responds to this second channel on keys
lower than #48. Once started you cannot change the midi channel - use the 
'-channel' option at startup to select the one you want. The actual available
max is 15 and that is enforced.

The emulation only contains 6 available presets and a 'Save' button that you 
need to double click to overwrite any preset. The emulation actually uses 
banks, so if you started it with '-load 23' it would start up by selecting
bank 20, and load memory #3 from that bank. Any saved memories are also then
written back to bank 20, still with just 6 memories accessible 20-25. You can
access more via MIDI bank select and program change operations if suitably
linked up.

Vox is a trade name owned by Korg Inc. of Japan, and Continental is one of 
their registered trademarks. Bristol does not intend to infringe upon these
registered names and Korg have their own remarkable range of vintage emulations
available. You are directed to their website for further information of true
Korg products.
