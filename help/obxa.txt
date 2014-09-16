    Oberheim OB-Xa
    --------------

This is almost two OB-X in a single unit. With one keyboard they could provide
the same sounds but with added voicing for split/layers/poly options. The OB-Xa
did at least work with all 10 voices, had a single keyboard, and is renound for
the sounds of van Halen 'Jump' and Stranglers 'Strange Little Girl'. The sound
had the capability to cut through a mix to upstage even guitar solo's. Oberheim
went on to make the most over the top analogue synths before the cut price
alternatives and the age of the DX overcame them.

Parameters are much the same as the OB-X as the algorithm shares the same code,
with a few changes to the mod routing. The main changes will be in the use of
Poly/Split/Layer controllers for splitting the keyboard and layering the sounds
of the two integrated synthesisers and the choice of filter algorithm.

The voice controls apply to the layer being viewed, selected from the D/U
button.

Manual:

    Volume
    Balance
    Auto: autotune the oscillators
    Hold: disable note off
    Reset: fast decay to zero for envelopes, disregards release parameter.
    Master Tune: up/down one semitone both oscillators.

Control:

    Glide: up to 30 seconds
    Oscillator 2 detune: Up/down one semitone

    Unison: gang all voices to a single 'fat' monophonic synthesiser.

Modulation:

    LFO: rate of oscillation
    Waveform: Sine/Square/Sample&Hold of noise src. Triangle if none selected.

    Depth: Amount of LFO going to:
        Freq Osc-1
        Freq Osc-2
        Filter Cutoff

    PWM: Amount of LFO going to:
        PWM Osc-1
        PWM Osc-2
        Tremelo

Oscillators:

    Freq1: 32' to 1' in octave increments.
    PulseWidth: Width of pulse wave (*).
    Freq2: 16' to 1' in semitone increments.

    Saw: sawtooth waveform Osc-1 (**)
    Puls: Pulse waveform Osc-1

    Env: Application of Filter env to frequency
    Sync: Osc-2 sync to Osc-1

    Saw: sawtooth waveform Osc-2
    Puls: Pulse waveform Osc-2

    * Although this is a single controller it acts independently on each of the
    oscillators - the most recent to have its square wave selected will be
    affected by this parameter allowing each oscillator to have a different
    pulse width, as per the original design.

    ** If no waveform is selected then a triangle is generated.

Filter:

    Freq: cutoff frequency
    Resonance: emphasis (*)
    Mod: Amount of modulation to filter cutoff (**)

    Osc-1: Osc-1 to cutoff at full swing.
    KDB: Keyboard tracking of cutoff.

    Half/Full: Oscillator 2 to Cutoff at defined levels (***)

    Noise: to Cutoff at defined levels
    4 Pole: Select 2 pole or 4 pole filter

    * In contrast to the original, this filter will self oscillate.

    ** The original had this parameter for the envelope level only, not the
    other modifiers. Due to the filter implementation here it affects total
    depth of the sum of the mods.

    *** These are not mutually exclusive. The 'Half' button gives about 1/4,
     the 'Full' button full, and both on gives 1/2. They could be made mutually
    exclusive, but the same effect can be generated with a little more flexibility
    here.

Envelopes: One each for filter and amplifier.

    Attack
    Decay
    Sustain
    Release

Mode selection:

    Poly: play one key from each layer alternatively for 10 voices
    Split: Split the keyboard. The next keypress specifies split point
    Layer: Layer each voice on top each other.

    D/U: Select upper and lower layers for editing.

Modifier Panel:

    Rate: Second LFO frequency or Arpeggiator rate (*)
    Depth: Second LFO gain
    Low: Modifiers will affect the lower layer
    Up: Modifiers will affect the upper layer
    Multi: Each voice will implement its own LFO
    Copy: Copy lower layer to upper layer

    Mod 01: Modify Osc-1 in given layer
    Mod 02: Modify Osc-2 in given layer
    PW: Modify Pulse Width
    AMT: Amount (ie, depth) of mods and freq wheels

    Transpose: Up or Down one octave.

The Arpeggiator code integrated into release 0.20.4 has three main parts, the
arpeggiator itself, the arpeggiating sequencer and the chording. All are 
configured from the left of the main panel.

The arpeggiator is governed by the rate control that governs how the code
steps through the available keys, an octave selector for 1, 2 or 3 octaves
of arpeggiation, and finally the Up/Down/Up+Down keys - the last ones start
the arpeggiator. Arpeggiation will only affect the lower layer.

When it has been started you press keys on the keyboard (master controller
or GUI) and the code will step through each note and octaves of each note 
in the order they were pressed and according to the direction buttons. The
key settings are currently reset when you change the direction and you will
have to press the notes again.

The sequencer is a modification of the code. Select the Seq button and then 
a direction. The GUI will program the engine with a series of notes (that can
be redefined) and the GUI will sequence them, also only into the lower layer.
The sequence will only start when you press a key on the keyboard, this is 
the starting point for the sequence. You can press multiple notes to have 
them sequence in unison. Once started you can tweak parameters to control
the sound and memory 88 when loaded has the filter envelope closed down, a
bit of glide and some heavy mods to give you a starting point for some serious
fun.

To reprogram the sequence steps you should stop the sequencer, press the PRG
button, then the Sequence button: enter the notes you want to use one by one
on the keyboard. When finished press the sequence button again, it goes out.
Now enable it again - select Seq and a direction and press a note. Press two
notes.

When you save the memory the OBXa will also save the  sequence however there
is only one sequence memory - that can be changed if you want to have a sequence
memory per voice memory (implemented in 0.20.4).

The chord memory is similar to the Unison mode except that Unison plays all
voices with the same note. Chording will assign one voice to each notes in
the chord for a richer sound. To enable Chording press the 'Hold' button. This
is not the same as the original since it used the hold button as a sustain
option however that does not function well with a Gui and so it was reused.

To reprogram the Chord memory do the following: press the PRG button then the
Hold button. You can then press the keys, up to 8, that you want in the chord,
and finally hit the Hold button again. The default chord is just two notes, 
the one you press plus its octave higher. This results in multiple voices
per keypress (a total of 3 in Layered mode) and with suitable detune will 
give a very rich sound.

There is only one arpeggiator saved for all the memories, not one per memory
as with some of the other implementations. Mail me if you want that changed.



The oscillators appear rather restricted at first sight, but the parametrics
allow for a very rich and cutting sound.

The Copy function on the Mod Panel is to make Poly programming easier - generate the desired sound and then copy the complete parameter set for poly operation. 
It can also be used more subtly, as the copy operation does not affect balance
or detune, so sounds can be copied and immediately panned slightly out of tune to generate natural width in a patch. This is not per the original instrument
that had an arpeggiator on the mod panel.

The Arpeggiator was first integrated into the OBXa in release 0.20.4 but not
widely tested.
