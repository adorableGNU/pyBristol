    Moog Voyager (Bristol "Explorer")
    ---------------------------------

This was Robert Moog's last synth, similar in build to the Mini but created
over a quarter of a century later and having far, far more flexibility. It 
was still monophonic, a flashback to a legendary synth but also a bit like
Bjorn Borg taking his wooden tennis racket back to Wimbledon long after having
retired and carbon fibre having come to pass. I have no idea who uses it and
Bjorn also crashed out in the first round. The modulation routing is exceptional
if not exactly clear.

The Voyager, or Bristol Explorer, is definitely a child of the Mini. It has
the same fold up control panel, three and half octave keyboard and very much
that same look and feel. It follows the same rough design of three oscillators
mixed with noise into a filter with envelopes for the filter and amplifier.
In contrast there is an extra 4th oscillator, a dedicated LFO bus also Osc-3
can still function as a second LFO here. The waveforms are continuously 
selected, changing gradually to each form: bristol uses a form of morphing
get get similar results. The envelopes are 4 stage rather than the 3 stage
Mini, and the effects routing bears no comparison at all, being far more
flexible here.

Just because its funny to know, Robert Moog once stated that the most difficult
part of building and releasing the Voyager was giving it the title 'Moog'. He
had sold his company in the seventies and had to buy back the right to use his
own name to release this synthesiser as a Moog, knowing that without that title
it probably would not sell quite as well as it didn't.

Control:

    LFO:
        Frequency
        Sync: LFO restarted with each keypress.

    Fine tune +/- one note
    Glide 0 to 30 seconds.

Modulation Busses:

    Two busses are implemented. Both have similar capabilities but one is
    controlled by the mod wheel and the other is constantly on. Each bus has
    a selection of sources, shaping, destination selection and amount.

    Wheel Modulation: Depth is controller by mod wheel.

        Source: Triwave/Ramp/Sample&Hold/Osc-3/External
        Shape: Off/Key control/Envelope/On
        Dest: All Osc Frequency/Osc-2/Osc-3/Filter/FilterSpace/Waveform (*)
        Amount: 0 to 1.

    Constant Modulation: Can use Osc-3 as second LFO to fatten sound.

        Source: Triwave/Ramp/Sample&Hold/Osc-3/External
        Shape: Off/Key control/Envelope/On
        Dest: All Osc Frequency/Osc-2/Osc-3/Filter/FilterSpace/Waveform (*)
        Amount: 0 to 1.

        * Destination of filter is the cutoff frequency. Filter space is the 
        difference in cutoff of the two layered filters. Waveform destination 
        affects the continuously variable oscillator waveforms and allows for 
        Pulse Width Modulation type effects with considerably more power since
        it can affect ramp to triangle for example, not just pulse width.

Oscillators:

    Oscillator 1:
        Octave: 32' to 1' in octave steps
        Waveform: Continuous between Triangle/Ramp/Square/Pulse

    Oscillator 2:
        Tune: Continuous up/down 7 semitones.
        Octave: 32' to 1' in octave steps
        Waveform: Continuous between Triangle/Ramp/Square/Pulse

    Oscillator 3:
        Tune: Continuous up/down 7 semitones.
        Octave: 32' to 1' in octave steps
        Waveform: Continuous between Triangle/Ramp/Square/Pulse

    Sync: Synchronise Osc-2 to Osc-1
    FM: Osc-3 frequency modulates Osc-1
    KBD: Keyboard tracking Osc-3
    Freq: Osc-3 as second LFO

Mixer:

    Gain levels for each source: Osc-1/2/3, noise and external input.

Filters:

    There are two filters with different configuration modes:

    1. Two parallel resonant lowpass filters.
    2. Serialised HPF and resonant LPF

    Cutoff: Frequency of cutoff
    Space: Distance between the cutoff of the two filters.
    Resonance: emphasis/Q.
    KBD tracking amount
    Mode: Select between the two operating modes.

Envelopes:

    Attack
    Decay
    Sustain
    Release

    Amount to filter (positive and negative control)

    Velocity sensitivity of amplifier envelope.

Master:

    Volume
    LFO: Single LFO or one per voice (polyphonic operation).
    Glide: On/Off portamento
    Release: On/Off envelope release.

The Explorer has a control wheel and a control pad. The central section has
the memory section plus a panel that can modify any of the synth parameters as
a real time control. Press the first mouse key here and move the mouse around
to adjust the controls. Default values are LFO frequency and filter cutoff 
but values can be changed with the 'panel' button. This is done by selecting
'panel' rather than 'midi', and then using the up/down keys to select parameter
that will be affected by the x and y motion of the mouse. At the moment the
mod routing from the pad controller is not saved to the memories, and it will
remain so since the pad controller is not exactly omnipresent on MIDI master
keyboards - the capabilities was put into the GIU to be 'exact' to the design.

This synth is amazingly flexible and difficult to advise on its best use. Try
starting by mixing just oscillator 1 through to the filter, working on mod 
and filter options to enrich the sound, playing with the oscillator switches
for different effects and then slowly mix in oscillator 2 and 3 as desired.

Memories are available via two grey up/down selector buttons, or a three digit
number can be entered. There are two rows of black buttons where the top row
is 0 to 4 and the second is 5 to 9. When a memory is selected the LCD display
will show whether it is is free (FRE) or programmed already (PRG).
