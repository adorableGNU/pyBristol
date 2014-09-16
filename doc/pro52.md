    Sequential Circuits Prophet-5
    Sequential Circuits Prophet-52 (the '5' with chorus)
    ----------------------------------------------------

Sequential circuits released amongst the first truly polyphonic synthesisers
where a group of voice circuits (5 in this case) were linked to an onboard
computer that gave the same parameters to each voice and drove the notes to
each voice from the keyboard. The device had some limited memories to allow 
for real live stage work. The synth was amazingly flexible regaring the
oscillator options and modulation routing, producing some of the fattest 
sounds around. They also had some of the fattest pricing as well, putting it
out of reach of all but the select few, something that maintained its mythical
status. David Sylvian of Duran Duran used the synth to wide acclaim in the
early 80's as did many of the new wave of bands.

The -52 is the same as the -5 with the addition of a chorus as it was easy, it
turns the synth stereo for more width to the sound, and others have done it on
the Win platform.

The design of the Prophet synthesisers follows that of the Mini Moog. It has
three oscillators one of them as a dedicated LFO. The second audio oscillator
can also function as a second LFO, and can cross modulate oscillator A for FM 
type effects. The audible oscillators have fixed waveforms with pulse width
modulation of the square wave. These are then mixed and sent to the filter with
two envelopes, for the filter and amplifier.

Modulation bussing is quite rich. There is the wheel modulation which is global,
taking the LFO and Noise as a mixed source, and send it under wheel control to
any of the oscillator frequency and pulse width, plus the filter cutoff. Poly
mods take two sources, the filter envelope and Osc-B output (which are fully
polyphonic, or rather, independent per voice), and can route them through to
Osc-A frequency and Pulse Width, or through to the filter. To get the filter
envelope to actually affect the filter it needs to go through the PolyMod
section. Directing the filter envelope to the PW of Osc-A can make wide, breathy
scanning effects, and when applied to the frequency can give portamento effects.

LFO:

    Frequency: 0.1 to 50 Hz
    Shape: Ramp/Triangle/Square. All can be selected, none selected should
    give a sine wave (*)

    (*) Not yet implemented.

Wheel Mod:

    Mix: LFO/Noise
    Dest: Osc-A Freq/Osc-B Freq/Osc-A PW/Osc-B PW/Filter Cutoff

Poly Mod: These are affected by key velocity.

    Filter Env: Amount of filter envelope applied
    Osc-B: Amount of Osc-B applied:
    Dest: Osc-A Freq/Osc-A PW/Filter Cutoff

Osc-A:

    Freq: 32' to 1' in octave steps
    Shape: Ramp or Square
    Pulse Width: only when Square is active.
    Sync: synchronise to Osc-B

Osc-B:

    Freq: 32' to 1' in octave steps
    Fine: +/- 7 semitones
    Shape: Ramp/Triangle/Square
    Pulse Width: only when Square is active.
    LFO: Lowers frequency by 'several' octaves.
    KBD: enable/disable keyboard tracking.

Mixer:

    Gain for Osc-A, Osc-B, Noise

Filter:

    Cutoff: cuttof frequency
    Res: Resonance/Q/Emphasis
    Env: amount of PolyMod affecting to cutoff.

Envelopes: One each for PolyMod (filter) and amplifier.

    Attack
    Decay
    Sustain
    Release

Global:

    Master Volume
    A440 - stable sine wave at A440 Hz for tuning.
    Midi: channel up/down
    Release: release all notes
    Tune: autotune oscillators.
    Glide: amount of portamento

    Unison: gang all voices to a single 'fat' monophonic synthesiser.

This is one of the fatter of the Bristol synths and the design of the mods
is impressive (not my design, this is as per sequential circuits spec). Some
of the cross modulations are noisy, notably 'Osc-B->Freq Osc-A' for square
waves as dest and worse as source.

The chorus used by the Prophet-52 is a stereo 'Dimension-D' type effect. The
signal is panned from left to right at one rate, and the phasing and depth at
a separate rate to generate subtle chorus through to helicopter flanging.

Memories are loaded by selecting the 'Bank' button and typing in a two digit
bank number followed by load. Once the bank has been selected then 8 memories
from the bank can be loaded by pressing another memory select and pressing
load. The display will show free memories (FRE) or programmed (PRG).
