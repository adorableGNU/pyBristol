    KORG MONOPOLY
    -------------

A synth suite would not be complete without some example of a Korg instrument,
the company was also pivotal in the early synthesiser developments. This is
an implementation of their early attempts at polyphonic synthesis, it was
either this one or the Poly-6 (which may be implemented later). Other choices
would have been the MS series, MS-20, but there are other synth packages that
do a better job of emulating the patching flexibility of that synth - Bristol
is more for fixed configurations.

As with many of the Korg synths (the 800 worked similarly) this is not really
true polyphony, and it is the quirks that make it interesting. The synth had
four audio oscillators, each independently configurable but which are bussed
into a common filter and envelope pair - these are not per voice but rather
per instrument. The unit had different operating modes such that the four
oscillators can be driven together for a phat synth, independently for a form
of polyphony where each is allocated to a different keypress, and a shared
mode where they are assigned in groups depending on the number of keys pressed.
For example, if only 2 notes are held then each key is sounded on two different
oscillators, one key is sounded on all 4 oscillators, and 3 or more have one
each. In addition there are two LFOs for modulation and a basic effects option
for beefing up the sounds. To be honest to the original synth, this emulation
will only request 1 voice from the engine. Korg is one of the few original
manufacturers to have survived the transition to digital synthesis and are
still popular.

One thing that is immediately visible with this synth is that there are a lot
of controllers since each oscillator is configured independently. This is in
contrast to the true polyphonic synths where one set of controls are given to
configure all the oscillators/filters/envelopes. The synth stages do follow the
typical synth design, there are modulation controllers and an FX section
feeding into the oscillators and filter. The effects section is a set of
controllers that can be configured and then enabled/disabled with a button
press. The overall layout is rather kludgy, with some controllers that are
typically grouped being dispersed over the control panel.

Control:

    Volume

    Arpeg:
        Whether arpegiator steps up, down, or down then up. This works in
        conjunction with the 'Hold' mode described later.

    Glide: glissando note to note. Does not operate in all modes

    Octave: Up/Normal/Down one octave transpose of keyboard

    Tune: Global tuning of all oscillators +/- 50 cents (*)
    Detune: Overall detuning of all oscillators +/- 50 cents (*)

    * There is an abundance of 'Tune' controllers. Global Tuning affects all
    the oscillators together, then oscillators 2, 3 and 4 have an independent
    tune controller, and finally there is 'Detune'. The target was to tune all
    the oscillators to Osc-1 using the independent Tune for each, and then use
    the global Tune here to have the synth tuned to other instruments. The
    Detune control can then be applied to introduce some beating between the
    oscillators to fatten the sound without necessarily losing overall tune of
    the instrument.

Modulation wheels:

    Bend:
        Intensity: Depth of modulation
        Destination:
            VCF - Filter cutoff
            Pitch - Frequency of all oscillators
            VCO - Frequency of selected oscillators (FX selection below).

    MG1: Mod Group 1 (LFO)
        Intensity: Depth of modulation
        Destination:
            VCF - Filter cutoff
            Pitch - Frequency of all oscillators
            VCO - Frequency of selected oscillators (FX selection below).

LFO:

    MG-1:
        Frequency
        Waveform - Tri, +ve ramp, -ve ramp, square.

    MG-2:
        Frequency (Triangle wave only).

Pulse Width Control:

    Pulse Width Modulation:
        Source - Env/MG-1/MG-2
        Depth
    
    Pule Width
        Width control
    
    These controllers affect Osc-1 though 4 with they are selected for either
    square of pulse waveforms.

Mode:

    The Mono/Poly had 3 operating modes, plus a 'Hold' option that affects 
    each mode:

        Mono: All oscillators sound same key in unison
        Poly: Each oscillator is assigned independent key - 4 note poly.
        Share: Dynamic assignment:
            1 key - 4 oscillators = Mono mode
            2 key - 2 oscillators per key
            3/4   - 1 oscillator per key = Poly mode

    The Hold function operates in 3 different modes:

        Mono: First 4 keypresses are memorised, further notes are then chorded
            together monophonically.
        Poly:
            Notes are argeggiated in sequence, new note presses are appended
            to the chain. Arpeggiation is up, down or up/down.
        Share:
            First 4 notes are memorised and are then argeggiated in sequence,
            new note presses will transpose the arpeggiation. Stepping is up,
            down or up/down.

    There are several controllers that affect arpeggation:

        Arpeg - direction of stepping
        MG-2 - Frequency of steps from about 10 seconds down to 50 bps.
        Trigger - Multiple will trigger envelopes on each step.

Effects:

    There are three main effects, or perhaps rather modulations, that are
    controlled in this section. These are vibrato, crossmodulated frequency
    and oscillator synchronisation. The application of each mod is configured
    with the controllers and then all of them can be enabled/disabled with
    the 'Effects' button. This allows for big differences in sound to be 
    applied quickly and simply as a typical effect would be. Since these mods
    apply between oscillators it was envisaged they would be applied in Mono
    mode to further fatten the sound, and the Mono mode is actually enabled when
    the Effects key is selected (as per the original instrument). The Mode can
    be changed afterwards for Effects/Poly for example, and they work with the
    arpeggiation function.

    X-Mod: frequency crossmodulation between oscillators
    Freq: frequency modulation by MG-1 (vibrato) or Envlope (sweep)

    Mode:
        Syn: Oscillators are synchronised
        X-M: Oscillators are crossmodulated
        S-X: Oscillators are crossmodulated and synchronised

    SNG:
        Single mode: synth had a master oscillator (1) and three slaves (2/3/4)
    DBL:
        Double mode: synth had two master (1/3) and two slaves (2/4)

    The overall FX routing depends on the SNG/DBL mode and the selection of
    Effects enabled or not according to the table below. This table affects 
    the FX routing and the modulation wheels discussed in the LFO section above:

                     --------------------------------------------------
                     |    FX OFF    |              FX ON              |
                     |              |----------------------------------
                     |              |    Single       |     Double    |
      ---------------+--------------+-----------------+---------------|
      | VCO-1/Slave  |    VCO-1     |    VCO 2/3/4    |     VCO 2/4   |
      |              |              |                 |               |
      | Pitch        |    VCO 1-4   |    VCO 1-4      |     VCO 1-4   |
      |              |              |                 |               |
      | VCF          |    VCF       |    VCF          |     VCF       |
      -----------------------------------------------------------------

    So, glad that is clear. Application of the modulation wheels to Pitch and
    VCF is invariable when they are selected. In contrast, VCO/Slave will have
    different destinations depending on the Effects, ie, when effects are on
    the modwheels will affect different 'slave' oscillators.


Oscillators:

    Each oscillator had the following controllers:

        Tune (*)
        Waveform: Triangle, ramp, pulse, square (**)
        Octave: Transpose 16' to 2'
        Level: output gain/mix of oscillators.

        * Osc-1 tuning is global
        ** width of pulse and square wave is governed by PW controller. The
        modulation of the pulse waveform is then also controlled by PWM.

Noise:

    Level: white noise output gain, mixed with oscillators into filter.

VCF:

    Freq:
        Cutoff frequency

    Res:
        Resonance/emphasis.
    
    Env:
        Amount of contour applied to cutoff
    
    KBD:
        Amount of key tracking applied.

ADSR: Two: filter/PWM/FX, amplifier

    Attack
    Decay
    Sustain
    Release

    Trigger:
        Single: Trigger once until last key release
        Multi: Trigger for each key or arpeggiator step.

    Damp:
        Off: Notes are held in Poly/Share mode until last key is released.
        On: Oscillators are released as keys are released.

This is more a synth to play with than describe. It never managed to be a true
blue synth perhaps largely due to its unusual design: the quasi-poly mode was
never widely accepted, and the effects routing is very strange. This does make
it a synth to be tweaked though.

Some of the mod routings do not conform to the original specification for the
different Slave modes. This is the first and probably the only bristol synth that
will have an inbuilt arpeggiator. The feature was possible here due to the mono
synth specification, and whilst it could be built into the MIDI library for
general use it is left up to the MIDI sequencers (that largely came along to 
replace the 1980s arpeggiators anyway) that are generally availlable on Linux.
[Other instruments emulated by bristol that also included arpeggiation but do
not have in the emulation were the Juno-6, Prophet-10, Oberheim OB-Xa, Poly6].

As of May 06 this synth was in its final stages of development. There are a few
issues with Tune and Detune that need to be fixed, and some of the poly key
assignment may be wrong.
