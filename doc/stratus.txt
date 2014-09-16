    CRUMAR STRATUS
    --------------

This unit is a hybrid synth/organ combo, an early polyphonic synth using an
organ divider circuit rather than independent VCO and having a set of filters
and envelope for the synth sounds, most manufacturers came out with similar
designs. The organ section was generally regarded as pretty bad here, there
were just five controls, four used for the volume of 16, 8, 4 and 2 foot 
harmonics and a fifth for overall organ volume. The synth section had 6 voices
and some quite neat little features for a glide circuitry and legato playing
modes.

The emulator consists of two totally separate layers, one emulating the organ
circuitry and another the synth. The organ has maximum available polyphony as
the algorithm is quite lightweight even though diverse liberties have been
taken to beef up the sound. The synth section is limited to 6 voices unless
otherwise specified at run time.

The legato playing modes affects three sections, the LFO modulation, VCO 
selection and glide:

LFO: this mod has a basic envelope to control the gain of the LFO using delay,
slope and gain. In 'multi' mode the envelope is triggered for every note that
is played and in the emulator this is actually a separate LFO per voice, a bit
fatter than the original. In 'Mono' mode there is only one LFO that all voices
will share and the envelope is triggered in Legato style, ie, only once for
a sequence of notes - all have to be released for the envelope to recover.

VCO: The original allowed for wavaeform selection to alternate between notes, 
something that is rather ugly to do with the bristol architecture. This is 
replaced with a VCO selector where each note will only take the output from
one of the two avalable oscillators and gives the ntoes a little more
separation. The legato mode works whereby the oscillator selection is only
made for the first note in a sequence to give a little more sound consistency.

Glide: This is probably the coolest feature of the synth. Since it used an
organ divider circuit it was not possible to actually glide from one note to
another - there are really only two oscillators in the synth section, not two
per voice. In contrast the glide section could glide up or down from a selected
amount to the real frequency. Selected from down with suitable values would
give a nice 'blue note' effect for example. In Legato mode this is done only
for the first keypress rather than all of the since the effect can be a bit
over the top if applied to each keystroke in a sequence. At the same time it
was possible to Sync the two oscillators, so having only one of them glide 
and be in sync then without legato this gave a big phasing entrance to each
note, a very interesting effect. The Glide has 4 modes:

    A. Both oscillators glide up to the target frequency
    B. Only oscillator-2 glides up to the target frequency
    C. Only oscillator-2 glides down to the target frequency
    D. Both oscillators glide down to the target frequency

These glide options with different sync and legato lead to some very unique
sounds and are emulated here with only minor differences.

The features, then notes on the differences to the original:

    A. Organ Section

        16, 8, 4 and 2 foot harmonic strengths.
        Volume.

    B. Synth Section

        LFO Modulation

            Rate - 0.1 to 50Hz approx
            Slope - up to 10 seconds
            Delay - up to 10 seconds
            Gain

            Routing selector: VCO, VCF, VCA
            Mono/Multi legato mode
            Shape - Tri/Ramp/Saw/Square

        Oscillator 1

            Tuning
            Sync 2 to 1
            Octave selector

        Oscillator 2

            Tuning
            Octave trill
            Octave selector

        Waveform Ramp and Square mix
        Alternate on/off
        Mono/Multi legato mode VCO selection

        Glide

            Amount up or down from true frequency
            Speed of glide
            Mono/Multi legato mode
            Direction A, B, C, D

        Filter

            Cutoff frequency
            Resonance
            Envelope tracking -ve to +ve
            Pedal tracking on/off

        Envelope

            Attack
            Decay
            Sustain
            Release

        Gain

Diverse liberties were taken with the reproduction, these are manageable from
the options panel by selecting the button next to the keyboard. This opens up
a graphic of a PCB, mostly done for humorous effect as it not in the least bit
representative of the actual hardware. Here there are a number of surface
mounted controllers. These are as below but may change by release:

   P1 Master volume

   P2  Organ pan
   P3  Organ waveform distorts
   P4  Organ spacialisation
   P5  Organ mod level
   J1  Organ key grooming 
   P6  Organ tuning (currently inactive *)

   P7  Synth pan
   P8  Synth tuning
   P9  Synth osc1 harmonics
   P10 Synth osc2 harmonics
   J2  Synth velocity sensitivity
   J3  Synth filter type
   P11 Synth filter tracking

*: To make the organ tunable the keymap file has to be removed.

Master (P1) volume affects both layers simultaneously and each layer can be
panned (P2/P7) and tuned (P8) separately to give phasing and spacialisation.
The synth layer has the default frequency map of equal temperament however the
organ section uses a 2MHz divider frequency map that is a few cents out for
each key. The Stratus actually has this map for both layers and that can easily
be done with the emulator, details on request.

It is currently not possible to retune the organ divider circuit, it has a
private microtonal mapping to emulate the few percent anomalies of the divider
circuit and the frequencies are predefined. The pot is still visible in P6 and
can be activated by removing the related microtonal mapping file, details from
the author on request.

Diverse liberties were taken with the Organ section since the original only 
produced 4 pure (infinite bandwidth) square waves that were mixed together, 
an overly weak result. The emulator adds a waveform distort (P3), an notched
control that produces a pure sine wave at centre point. Going down it will
generate gradually increasing 3rd and 5th harmonics to give it a squarey wave
with a distinct hammond tone. The distortion actually came from the B3 emulator
which models the distort on the shape of the hammond tonewheels themselves.
Going up from centre point will produce gradually sharper sawtooth waves using
a different phase distortion.

Organ spacialisation (P4) will separate out the 4 harmonics to give them 
slightly different left and right positions to fatten out the sound. This works
in conjunction with the mod level (P5) where one of the stereo components of
each wave is modified by the LFO to give phasing changes up to vibrato.

The organ key grooming (J1) will either give a groomed wave to remove any
audible clicks from the key on and off events or when selected will produce 
something akin to a percussive ping for the start of the note.

The result for the organ section is that it can produce some quite nice sounds
reminiscent of the farfisa range to not quite hammond, either way far more
useful than the flat, honking square waves. The original sound can be made by
waveform to a quarter turn or less, spacialisation and mod to zero, key
grooming off.

The synth has 5 modifications at the first release. The oscillator harmonics
can be fattened at the top or bottom using P9 and P10, one control for each
oscillator, low is more bass, high is more treble. Some of the additional
harmonics will be automatically detuned a little to fatten out the sound as a
function of the -detune parameter defaulting to 100.

The envelope can have its velocity sensitively to the filter enabled or disabled
(J2) and the filter type can be a light weight filter for a thinner sound but at
far lower CPU load (J3).

The filter keyboard tracking is configurable (P11), this was outside of the spec
of the Stratus however it was implemented here to correct the keyboard tracking
of the filter for all the emulations and the filter should now be playable.
The envelope touch will affect this depending on J2 since velocity affects the
cut off frequency and that is noticeable when playing the filter. This jumper
is there so that the envelope does not adversely affect tuning but can still be
used to have the filter open up with velocity if desired.

The mod application is different from the original. It had a three way selector
for routing the LFO to either VCO, VCA or VCF but only a single route. This
emulation uses a continuous notched control where full off is VCO only, notch
is VCF only and full on is VCA however the intermidiate positions will route
proportional amounts to two components.

The LFO has more options (Ramp and Saw) than the original (Tri and Square).

The extra options are saved with each memory however they are only loaded at
initialisation and when the 'Load' button is double-clicked. This allows you to
have them as global settings or per memory as desired. The MemUp and MemDown 
will not load the options, only the main settings.

VCO mod routing is a little bit arbitrary in this first release however I could
not find details of the actual implementation. The VCO mod routing only goes
to Osc-1 which also takes mod from the joystick downward motion. Mod routing
to Osc-2 only happens if 'trill' is selected. This seemed to give the most
flexibility, directing the LFO to VCF/VCA and controlling vibrato from the 
stick, then having Osc-2 separate so that it can be modified and sync'ed to
give some interesting phasing.

As of the first release there are possibly some issues with the oscillator 
Sync selector, it is perhaps a bit noisy with a high content of square wave.
Also, there are a couple of minor improvements that could be made to the 
legato features but they will be done in a future release. They regard how
the glide is applied to the first or all in a sequence of notes.

The joystick does not always pick up correctly however it is largely for 
presentation, doing actual work you would use a real joystick or just use the
modwheel (the stick generates and tracks continuous controller 1 - mod). The
modwheel tracking is also a bit odd but reflects the original architecture - 
at midpoint on the wheel there is no net modulation, going down affects VCO
in increasing amounts and going up from mid affect the VCF. The control feels
like it should be notched however generally that is not the case with mod
wheels.

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
arbitrary. For the Stratus this simplification of the sync waveform is done
automatically by the Sync switch, this means the synchronised output sounds
correct but the overall waveform may be simpler.
