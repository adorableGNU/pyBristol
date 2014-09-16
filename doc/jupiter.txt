    Roland Jupiter 8
    ----------------

This emulator is anticipated in 0.20.4.

The Jupiter synthesizers were the bigger brothers of the Juno series: their
capabilities, sounds and prices were all considerably larger. This is the
larger of the series, the others being the -4 and -6. The -6 and the rack
mounted MKS-80 both came out after the Jupiter-8 and had somewhat more flexible
features. Several of these have been incorporated into the emulation and that
is documented below.

A quick rundown of the synth and emulation:

The synth runs as two layers, each of which is an independent emulator running
the same algorithm, both layers are controlled from the single GUI. The layers
are started with a set of voices, effectively 4+4 per default however bristol
plays with those numbers to give the split/layer at 4 voices each and the 'All'
configuration with 8 voices - it juggles them around depending on the Poly 
mode you select. You can request a different number of voices and the emulator 
will effectively allocate half the number to each layer. If you request 32
voices you will end up with 4+4 though since 32 is interpreted as the default.

The Poly section is used to select between Dual layers, Split keyboard and the
8voice 'All' mode. You can redefine the split point with a double click on the
'Split' button and then pressing a key. If you have linked the GUI up to the
MIDI you should be able to press a key on your master keyboard rather than on
the GUI.

After that you can select the layer as upper or lower to review the parameter 
settings of each layer: they are as follows:

LFO:
    Frequency
    Delay
    Waveform (tri, saw, square, s&h)

VCO Mods:
    LFO and ENV-1
    Destination to modulate frequency of DCO1, DCO2 or both.

PWM:
    PW
    PWM
    Modified by Env-1 or LFO

DCO-1:
    Crossmod (FM) from DCO2 to DCO1
    Modified by Env-1

    Octave range 16' to 2' (all mixable)
    Waveform: Tri, saw, pulse, square (all mixable)

DCO-2:
    Sync (1->2 or 2->1 or off)
    Range: 32' to 2' (all mixable)
    Tuning
    Waveform: tri, saw, pulse, noise (all mixable)

Mix:
    Osc 1 and Osc 2

HPF:
    High pass filter of signal

Filter:
    Cutoff
    Emphasis
    LPF/BPF/HPF
    Env modulation
    Source from Env-1 or Env-2
    LFO mod amount
    Keyboard tracking amount

VCA:
    Env-2 modulation
    LFO modulation

ADSR-1:
    A/D/S/R
    Keyboard tracking amount
    Invert

ADSR-2:
    A/D/S/R
    Keyboard tracking amount

Pan:
    Stereo panning of layer

All of the above 40 or so parameters are part of the layer emulation and are
separately configurable.

The keyboard can operate in several different modes which are selectable from
the Poly and Keyboard mode sections. The first main one is Dual, Split and All.
Dual configure the two synth layers to be placed on top of each other. Split
configures them to be next to each other and by double clicking the split
button you can then enter a new split point by pressing a key. The All setting
gives you a single layer with all 8 voices active. These settings are for the
whole synth.

The Poly section provides different playing modes for each layer independently.
There are 3 settings: Solo give the layer access to a single voice for playing
lead solos. Unison give the layer however many voices it is allowed (8 if in 
the All mode, 4 otherwise) and stacks them all on top of each other. This is
similar to Solo but with multiple voices layered onto each other. Unison is 
good for fat lead sounds, Solo better for mono bass lines where Unison might
have produced unwanted low frequency signal phasing. The third option is Poly
mode 1 where the synth allocates a single voice to each key you press. The
original also had Poly mode 2 which was not available at the first bristol
release - this mode would apply as many notes as available to the keys you
pressed: 1 key = 8 voices as in Unison, with 2 keys pressed each would get 4
voices each, 4 keys pressed would get 2 voices and mixtures in there for other
key combinations. This may be implemented in a future release but it is a
rather left field option and would have to be put into the MIDI library that
controls the voice assignments.

The arpeggiator integrated into bristol is a general design and will differ
from the original. The default settings are 4 buttons controlling the range
of the arpeggiation, from 1 to 4 octaves, 4 buttons controlling the mode as
Up, Down, Up+Down or Random sequencing of the notes available, and 4 notes
that are preloaded into the sequence.

Finally there are two global controls that are outside of the memories - the
rate and clock source (however externally driven MTC has not been implemented
yet). It is noted that the Arpeggiator settings are separate from the sequence
information, ie, Up/Down/Rnd, the range and the arpeggiator clock are not the
same as the note memory, this is discussed further in the memory setting
section below.

It is possible to redefine the arpeggiator sequence: select the function 
button on the right hand side, then select any of the arpeggiator mode buttons,
this will initiate the recording. It does not matter which of the mode is
selected since they will all start the recording sequence. When you have
finished then select the mode button again (you may want to clear the function
key if still active). You can record up to 256 steps, either from the GUI
keyboard or from a master controller and the notes are saved into a midi
key memory.

There is no capability to edit the sequences once they have been entered, that
level of control is left up to separate MIDI sequencers for which there are
many available on Linux. Also, the note memory is actually volatile and will
be lost when the emulation exits. If you want to save the settings then you
have to enter them from the GUI keyboard or make sure that the GUI is linked
up to the master keyboard MIDI interface - you need to be able to see the
GUI keyboard following the notes pressed on the master keyboard since only
when the GUI sees the notes can it store them for later recall. If the GUI
did view the sequence entered here then it will be saved with the patch in
a separate file (so that it can be used with other bristol synths).

In addition to the Arpeggiator there is the 'Chord' control. The original
synth had two green panel buttons labelled 'Hold', they were actually similar
to the sustain pedal on a MIDI keyboard or piano, with one for each layer of
the synth. They have been redefined here as Chord memory. When activated the
layer will play a chord of notes for every key press. The notes are taken from
separate chord memory in the Arpeggiator sequencer. The result is very similar
to the Unison mode where every voice is activated for a single key, the
difference here is that every voice may be playing a different note to give
phat chords. To configure a chord you enable the function key and the target
Hold button to put the synth into chord learning mode, play a set of notes
(you don't have to hold them down), and click again to finalise the chord.
If there are more chord notes than voices available then all voices will
activate. If there are more voices than notes then you will be able to play
these chord polyphonically, for example, if you have 8 voices and entered
just 4 chorded notes then you will have 2 note polyphony left. You should
also be able to play arpeggiations of chords. The maximum number of notes
in a chord is 8.

The synth has a modifier panel which functions as performance options which 
can be applied selectively to different layers:

    Bender:
        This is the depth of the settings and is mapped by the engine to
        continuous controller 1 - the 'Mod' wheel. The emulation also tracks
        the pitch wheel separately.

    Bend to VCO
        This applies an amount of pitch bend from the Mod wheel selectively
        to either VCO-1 and/or VCO-2. These settings only affect the Mod
        layers selected from the main panel. Subtle modifications applied in
        different amounts to each oscillator can widen the sound considerable
        by introducing small amounts of oscillator phasing.
    
    Bend to VCF
        Affects the depth of cutoff to the filter with on/off available. Again
        only applies to layers activate with the Mod setting.

    LFO to VCO:
        The mod panel has a second global LFO producing a sine wave. This can
        be driven in selectable amounts to both VCO simultaneously. Layers are
        selected from the Mod buttons.

    LFO to VCF:
        The LFO can be driven in selectable amounts to both VCO or to the VCF.
        Layers are selected from the Mod buttons.

    Delay:
        This is the rise time of the LFO from the first note pressed. There is
        no apparent frequency control of the second LFO however bristol allows
        the frequency and gain of the LFO to track velocity using function B4
        (see below for function settings). Since there is only one LFO per
        emulation then the velocity tracking can be misleading as it only 
        tracks from a single voice and may not track the last note. For this
        reason it can be disabled. Using a tracking from something like channel
        pressure is for future study.

    Glide:
        Glissando between key frequencies, selectable to be either just to the
        upper layer, off, or to both layers.

    Transpose:
        There are two transpose switches for the lower and upper layers 
        respectively. The range is +/1 one octave.

Modifier panel settings are saved in the synth memories and are loaded with
the first memory (ie, with dual loaded memories discussed below). The ability
to save these settings in memory is an MKS-80 feature that was not available
in either the Jupiter-6 or -8.

There are several parts to the synth memories. Layer parameters govern sound
generation, synth parameters that govern operating modes such Dual/Split,
Solo/Unison etc, Function settings that modify internal operations, the
parameters for the mod panel and finally the Arpeggiator sequences. These
sequences are actually separate from the arpeggiator settings however that
was covered in the notes above.

When a patch is loaded then only the layer parameters are activated so that the
new sound can be played, and the settings are only for the selected layer. This
means any chord or arpeggiation can be tried with the new voice active.

When a memory is 'dual loaded' by a double click on the Load button then all
the memory settings will be read and activated: the current layer settings,
synth settings, operational parameters including the peer layer parameters
for dual/split configurations. Dual loading of the second layer will only 
happen if the memory was saved as a split/double with a peer layer active.

The emulation adds several recognised Jupiter-6 capabilities that were not a
part of the Jupiter-8 product. These are

    1.  PW setting as well as PWM
    2.  Cross modulation can be amplified with envelope-1 for FM type sounds
    3.  Sync can be set in either direction (DCO1 to 2 or DCO2 to 1)
    4.  The waveforms for DCO 1&2 are not exclusive but mixable
    5.  The LFO to VCA is a continuous controller rather than stepped
    6.  The envelope keyboard tracking is continuous rather than on/off
    7.  The filter option is multimode LP/BP/HP rather than 12/24dB
    8.  Layer detune is configurable
    9.  Layer transpose switches are available
    10. Arpeggiator is configurable on both layers

Beyond these recognised mods it is also possible to select any/all DCO
transpositions which further fattens up the sound as it allows for more
harmonics. There is some added detune between the waveforms with its depth
being a function of the -detune setting. Separate Pan and Balance controls
have been implemented, Pan is the stereo positioning and is configurable per
layer. Balance is the relative gain between each of the layers.

There are several options that can be configured from the 'f' button
in the MIDI section. When you push the f(n) button then the patch and bank
buttons will not select memory locations but display the on/off status of 16
algorithmic changes to the emulation. Values are saved in the synth memories.
These are bristol specific modifications and may change between releases unless
otherwise documented.

F(n):

    f(p1): Env-1 retriggers 
    f(p2): Env-1 conditionals
    f(p3): Env-1 attack sensitivity
    f(p4): Env-2 retriggers
    f(p5): Env-2 conditionals
    f(p6): Env-2 attack sensitivity
    f(p7): Noise per voice/layer
    f(p8): Noise white/pink

    f(b1): LFO-1 per voice/layer
    f(b2): LFO-1 Sync to Note ON
    f(b3): LFO-1 velocity tracking
    f(b4): Arpeggiator retrigger
    f(b5): LFO-2 velocity tracking
    f(b6): NRP enable
    f(b7): Debug MIDI
    f(b8): Debug GUI controllers

The same function key also enables the learning function of the arpeggiator 
and chord memory, as explained above. When using the arpeggiator you may want
to test with f(b4) enabled, it will give better control of the filter envelope.


Other differences to the original are the Hold keys on the front panel. These
acted as sustain pedals however for the emulation that does not function very
well. With the original the buttons were readily available whilst playing and
could be used manually, something that does not work well with a GUI and a
mouse. For this reason they were re-used for 'Unison Chording' discussed above.
Implementing them as sustain pedals would have been an easier if less flexible
option and users are advised that the bristol MIDI library does recognise the
sustain controller as the logical alternative here.

Another difference would be the quality of the sound. The emulation is a lot
cleaner and not as phat as the original. You might say it sounds more like
something that comes from Uranus rather than Jupiter and consideration was
indeed given to a tongue in cheek renaming of the emulation..... The author is
allowed this criticism as he wrote the application - as ever, if you want the
original sound then buy the original synth (or get Rolands own emulation?).

A few notes are required on oscillator sync since by default it will seem to 
be quite noisy. The original could only product a single waveform at a single
frequency at any one time. Several emulators, including this one, use a bitone
oscillator which generates complex waveforms. The Bristol Bitone can generate
up to 4 waveforms simultaneously at different levels for 5 different harmonics
and the consequent output is very rich, the waves can be slightly detuned, 
the pulse output can be PW modulated. As with all the bristol oscillators that
support sync, the sync pulse is extracted as a postive leading zero crossing.
Unfortunately if the complex bitone output is used as input to sync another
oscillator then the result is far too many zero crossings to extract a good
sync. For the time being you will have to simplify the sync source to get a
good synchronised output which itself may be complex wave. A future release
will add a sync signal from the bitone which will be a single harmonic at the
base frequency and allow both syncing and synchronised waveform outputs to be
arbitrary.
