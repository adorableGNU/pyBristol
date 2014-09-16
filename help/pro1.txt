    Sequential Circuits Prophet Pro-One
    -----------------------------------

Sequential circuits released amongst the first truly polyphonic synthesisers
where a group of voice circuits (5 to 10 of them) were linked to an onboard
computer that gave the same parameters to each voice and drove the notes to
each voice from the keyboard. The costs were nothing short of exhorbitant and
this lead to Sequential releasing a model with just one voice board as a mono-
phonic equivalent. The sales ran up to 10,000 units, a measure of its success
and it continues to be recognised alongside the Mini Moog as a fat bass synth.

The design of the Prophet synthesisers follows that of the Mini Moog. It has
three oscillators one of them as a dedicated LFO. The second audio oscillator
can also function as a second LFO, and can cross modulate oscillator A for FM 
type effects. The audible oscillators have fixed waveforms with pulse width
modulation of the square wave. These are then mixed and sent to the filter with
two envelopes, for the filter and amplifier.

The Pro-1 had a nice bussing matrix where 3 different sources, LFO, Filter Env
and Oscillator-B could be mixed in varying amounts to two different modulation
busses and each bus could then be chosen as inputs to modulation destinations.
One bus was a direct bus from the mixed parameters, the second bus was under
the modwheel to give configurable expressive control.

LFO:

    Frequency: 0.1 to 50 Hz
    Shape: Ramp/Triangle/Square. All can be selected, none selected should
    give a sine wave

Modulations:

    Source:

        Filter Env amount to Direct or Wheel Mod busses
        Oscillator-B amount to Direct or Wheel Mod busses
        LFO to Direct amount or Wheel Mod busses

    Dest:

        Oscillator-A frequency from Direct or Wheel Mod busses
        Oscillator-A PWM from Direct or Wheel Mod busses
        Oscillator-B frequency from Direct or Wheel Mod busses
        Oscillator-B PWM from Direct or Wheel Mod busses
        Filter Cutoff from Direct or Wheel Mod busses

Osc-A:

    Tune: +/-7 semitones
    Freq: 16' to 2' in octave steps
    Shape: Ramp or Square
    Pulse Width: only when Square is active.
    Sync: synchronise to Osc-B

Osc-B:

    Tune: +/-7 semitones
    Freq: 16' to 2' in octave steps
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
    Env: amount of modulation affecting to cutoff.
    KBD: amount of keyboard trackingn to cutoff

Envelopes: One each for PolyMod (filter) and amplifier.

    Attack
    Decay
    Sustain
    Release

Sequencer:

    On/Off
    Record Play
    Rate configured from LFO

Arpeggiator:

    Up/Off/UpDown
    Rate configured from LFO

Glide:

    Amount of portamento
    Auto/Normal - first key will/not glide.

Global:

    Master Tune
    Master Volume


Memories are loaded by selecting the 'Bank' button and typing in a two digit
bank number followed by load. Once the bank has been selected then 8 memories
from the bank can be loaded by pressing another memory select and pressing
load. The display will show free memories (FRE) or programmed (PRG).
There is an additional Up/Down which scan for the next program and a 'Find'
key which will scan up to the next unused memory location.

The original supported two sequences, Seq1 and Seq2, but these have not been
implemented. Instead the emulator will save a sequence with each memory location
which is a bit more flexible if not totally in the spirit of the original.

The Envelope amount for the filter is actually 'Mod Amount'. To get the filter
envelope to drive the filter it must be routed to the filter via a mod bus. This
may differ from the original.
Arpeggiator range is two octaves.
The Mode options may not be correctly implemented due to the differences in
the original being monophonic and the emulator being polyphonic. The Retrig is
actually 'rezero' since we have separate voices. Drone is a Sustain key that
emulates a sustain pedal.
Osc-B cannot modulate itself in polyphonic mode (well, it could, it's just that
it has not been coded that way).
The filter envelope is configured to ignore velocity.

The default filters are quite expensive. The -lwf option will select the less
computationally expensive lightweight Chamberlain filters which have a colder
response but require zonks fewer CPU cycles.
