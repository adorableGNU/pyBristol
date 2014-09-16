    Moog Sonic-6
    ------------

This original design was made by an engineer who had previously worked with 
Moog on the big modular systems, Gene Zumchek. He tried to get Moog Inc to 
develop a small standalone unit rather than the behemoths however he could 
not get heard. After leaving he built a synth eventually called a Sonic-5 that
did fit the bill but sales volumes were rather small. He had tied up with a
business manager who worked out that the volume was largely due to the name
not being known, muSonics.
This was quickly overcome by accident. Moog managed to run his company into
rather large debt and the company folded. Bill Waytena, working with Zumcheck,
gathered together the funding needed to buy the remains of the failed company
and hence Moog Inc was labled on the rebadged Sonic-6. Zumcheck was eventually
forced to leave this company (or agreed to) as he could not work with Moog.
After a few modifications Bob Moog actually used this unit quite widely for
lecturing on electronic music. For demonstrative purposes it is far more
flexible than any of Moog's own non-modular designs and it was housed in a
transport case rather than needing a shipping crate as the modular systems
required.

The emulation features are given below, but first a few of the differences to 
the original

    Added a mod wheel that can drive GenX/Y.
    PWM is implemented on the oscillator B
    Installed an ADSR rather than AR, selectable.
    No alternative scalings - use scala file support
    Not duo or dia phonic. Primarily poly with separated glide.

The original was duophonic, kind of. It had a keyboard with high note and low
note precedence and the two oscillators could be driven from different notes.
Its not really duophony and was reportedly not nice to play but it added some
flexibility to the instrument. This features was dropped largley because it
is ugly to emulate in a polyphonic environment but the code still has glide
only on Osc-B. It has the two LFO that can be mixed, or at full throw of the 
GenXY mixer they will link X->A and Y->B giving some interesting routing, two
osc each with their own LFO driving the LFO from the mod wheel or shaping it
with the ADSR. Playing around should give access to X driving Osc-A, then 
Osc-A and GenY driving Osc-B with Mod and shaping for some investigation of
FM synthesis. The gruesome direct output mixer is still there, having the osc
and ring-mod bypass the filter and amplifier completely (or can be mixed back
into the 'actuated' signal).

There is currently no likely use for an external signal even though the
graphics are there.

The original envelope was AR or ASR. The emulator has a single ADSR and a 
control switch to select AR (actually AD), ASR, ADSD (MiniMoog envelope) or
ADSR.

Generator-Y has a S/H function on the noise source for a random signal which 
replaced the square wave. Generator-X still has a square wave.

Modulators:

    Two LFO, X and Y:

        Gen X:
            Tri/Ramp/Saw/Square
            Tuning
            Shaping from Envelope or Modwheel

        Gen Y:
            Tri/Ramp/Saw/Rand
            Tuning
            Shaping from Envelope or Modwheel

        Master LFO frequency

        GenXY mixer
    
    Two Oscillators, A and B

        Gen A:
            Tri/Ramp/Pulse
            PulseWidth
            Tuning
            Transpose 16', 8', 4' (*)

            Mods:

                Envelope
                GenXY(or X)
                Low frequency, High Frequency (drone), KBD Tracking

        Gen B:
            Tri/Ramp/Pulse
            PulseWidth
            Tuning
            Transpose 16' 8', 4'

            Mods:
            
                Osc-B
                GenXY(or Y)
                PWM

        GenAB mix

        Ring Mod:

            Osc-B/Ext
            GenXY/Osc-A

        Noise

            Pink/White

        Mixer

            GenAB
            RingMod
            External
            Noise

        Filter (**)

            Cutoff
            Emphasis

            Mods:

                ADSR
                Keyboard tracking
                GenXY

        Envelope:

            AR/ASR/ADSD/ADSR
            Velociy on/off

            Trigger:

                GenX
                GenY
                Kbd (rezero only)

            Bypass (key gated audio)

        Direct Output Mixer

            Osc-A
            Osc-B
            RingMod


The keyboard has controls for

    Glide (Osc-B only)
    Master Volume
    PitchWheel
    ModWheel (gain modifier on LFO)

    Global Tuning

    MultiLFO X and Y

* The oscillator range was +/-2 octave switch and a +/-1 octave pot. This
emulator has +/-1 octave switch and +/-7 note pot. That may change in a future
release to be more like the original, probably having a multiway 5 stage octave
selector.

** The filter will self oscillate at full emphasis however this is less 
prominent at lower frequencies (much like the Moog ladder filter). The filter
is also 'not quite' in tune when played as an oscillator, this will also change
in a future release.

There may be a reverb on the emulator. Or there may not be, that depends on
release. The PitchWheel is not saved in the memories, the unit is tuned on
startup and this will maintain tuning to other instruments. The MultiLFO allow
you to configure single LFO per emulation or one per voice, independently.
Having polyphony means you can have the extra richness of independent LFO per
voice however that does not work well if they are used as triggers, for example,
you end up with a very noisy result. With single triggers for all voices the
result is a lot more predictable.

The Sonic-6 as often described as having bad tuning, that probably depends on 
model since different oscillators were used at times. Also, different units
had different filters (Zumchek used a ladder of diodes to overcome the Moog
ladder of transister patent). The original was often described as only being
useful for sound effects. Personally I don't think that was true however the
design is extremely flexible and the mods are applied with high gains so to
get subtle sounds they only have to be applied lightly. Also, this critique
was in comparison to the Mini which was not great for sound effects since it,
in contrast, had very little in the way of modifiers.

The actual mod routing here is very rich. The two LFO can be mixed to provide
for more complex waves and have independent signal gain from the ADSR. To go
a step further it is possible to take the two mixed LFO into Osc-A, configure
that as an LFO and feed it into Osc-B for some very complex mod signals. That
way you can get a frequency modulated LFO which is not possible from X or Y. As
stated, if these are applied heavily you will get ray guns and car alarms but
in small amounts it is possible to just shape sounds. Most of the mod controls
have been made into power functions to give more control at small values.

The memory panel gives access to 72 banks of 8 memories each. Press the Bank
button and two digits for the bank, then just select the memory and press Load.
You can get the single digit banks by selecting Bank->number->Bank. There is
a save button which should require a double click but does not yet (0.30.0),
a pair of buttons for searching up and down the available memories and a button
called 'Find' which will select the next available free memory.

Midi options include channel, channel down and, er, thats it.
