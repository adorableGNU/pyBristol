    Moog Mini
    ---------

It is perhaps not possible to write up who used this synth, the list is endless.
Popular as it was about the first non-modular synthesiser, built as a fixed
configuration of the racked or modular predecessors.

Best known at the time on Pink Floyd 'Dark Side of the Moon' and other albums.
Rick Wakefield used it as did Jean Michel Jarre. Wakefield could actually
predict the sound it would make by just looking at the settings, nice to be
able to do if a little unproductive but it went to show how this was treated
as an instrument in its own right. It takes a bit of work to get the same sweet,
rich sounds out of the emulation, but it can be done with suitable tweaking.

The original was monophonic, although a polyphonic version was eventually made
after Moog sold the company - the MultiMoog. This emulation is more comparable
to that model as the sound is a bit thinner and can be polyphonic. The design
of this synth became the pole bearer for the following generations: it had 
three oscillators, one of which could become a low frequency modulator. They
were fed into a mixer with a noise source, and were then fed into a filter
with 2 envelope generators to contour the wave. Modulation capabilities were
not extensive, but interestingly enough it did have a frequency modulation (FM)
capability, eventually used by Yamaha to revolutionise the synthesiser market
starting the downfall of analogue synthesis twenty years later.

All the analogue synths were temperature sensitive. It was not unusual for the
synths to 'detune' between sound test and performance as the evening set in.
To overcome this they could optionally produce a stable A-440Hz signal for 
tuning the oscillators manually - eventually being an automated option in the
newer synths. Whilst this digital version has stable frequency generation the
A-440 is still employed here for the sake of it.

Modifiers and mod routing are relatively simple, Osc-3 and noise can be mixed,
and this signal routed to the oscillator 1 and 2 frequency or filter cutoff.

The synth had 5 main stages as follows:

Control:

    Master tuning: up/down one note.

    Glide: (glissando, portamento). The rate at which one key will change its
    frequency to the next played key, 0 to 30 seconds.

    Mod: source changes between Osc-3 and noise.

    Release: The envelope generators had only 3 parameters. This governed whether
    a key would release immediately or would use Decay to die out.

    Multi: Controls whether the envelope will retrigger for each new keypress.

Oscillators:

    There are three oscillators. One and two are keyboard tracking, the third
    can be decoupled and used as an LFO modulation source.

    Oscillator 1:
        Octave step from 32' to 1'.
        Waveform selection: sine/square/pulse/ramp/tri/splitramp
        Mod: controls whether Osc-3/noise modulates frequency

    Oscillator 2:
        Octave step from 32' to 1'.
        Fine tune up/down 7 half notes.
        Waveform selection: sine/square/pulse/ramp/tri/splitramp
        Mod: controls whether Osc-3/noise modulates frequency

    Oscillator 3:
        Octave step from 32' to 1'.
        Fine tune up/down 7 half notes.
        Waveform selection: sine/square/pulse/ramp/tri/splitramp
        LFO switch to decouple from keytracking.

Mixer:

    Gain levels for Oscillator 1/2/3
    Mixing of the external input source into filter
    Noise source with white/pink switch.

    Note: The level at which Osc-3 and noise modulates sound depends on its
    gain here, similarly the noise. The modulator mix also affects this, but
    allows Osc-3 to mod as well as sound. The modwheel also affect depth.

Filter:

    Cutoff frequency

    Emphasis (affects Q and resonance of filter).

    Contour: defines how much the filter envelope affects cutoff.

    Mod - Keyboard tracking of cutoff frequency.

    Mod - Osc-3/noise modulation of cutoff frequency.

Contour:

    The synth had two envelope generators, one for the filter and one for the
    amplifier. Release is affected by the release switch. If off the the sound
    will release at the rate of the decay control.

    Attack: initial ramp up of gain.

    Decay: fall off of maximum signal down to:

    Sustain: gain level for constant key-on level.

    Key: Touch sensitivity of amplifier envelope.

Improvements to the Mini would be some better oscillator waveforms, plus an
alternative filter as this is a relatively simple synthesiser and could do
with a warmer filter (this was fixed with integration of the houvillanen filters
although the do consume a lot of CPU to do it).

The Output selection has a Midi channel up/down selector and memory selector.
To read a memory either use the up/down arrows to go to the next available
memory, or type in a 3 digit number on the telephone keypad and press 'L' for
load or 'S' for save.

As of release 0.20.5 Vasiliy Basic contributed his Mini memory banks and they
are now a part of the distribution:

Programs for Bristol's "Mini" (from 50 to 86 PRG)

List of programs:

    -Melodic-
    50 - Trumpet
    51 - Cello
    52 - Guitar 1
    53 - Guitar 2
    54 - Fingered Bass
    55 - Picked Bass
    56 - Harmonica
    57 - Accordion
    58 - Tango Accordion
    59 - Super Accordion
    60 - Piano
    61 - Dark Organ
    62 - Flute
    63 - Music Box
    64 - Glass Xylo
    65 - Glass Pad
    66 - Acid Bass
    
    -Drums-
    67 - Bass Drum 1 
    68 - Bass Drum 2
    69 - Bass Drum 3
    70 - Bass Drum 4
    71 - Tom
    72 - Snare 1
    73 - Snare 2
    74 - Snare 3
    75 - Snare 4
    76 - Cl HH 1
    77 - Op HH 1
    78 - Crash Cym 1
    79 - Crash Cym 2
    80 - Cl HH 2
    81 - Op HH 2
    
    -FX-
    82 - Sea Shore
    83 - Helicopter 1
    84 - Helicopter 2
    85 - Bird Tweet
    86 - Birds Tweet
