    REALISTIC MG-1 CONCERTMATE
    --------------------------

This is a pimpy little synth. It was sold through the Realistic electronics 
chain, also known as Radio Shack (and as Tandy, in the UK at least). It was
relatively cheap but had a design from Moog Music (from after Robert Moog
had left?) including the patented ladder filter. It consisted of a monophonic
synth, dual oscillator, lfo, noise, filter, env, and a ring modulator. On top
of that there was an organ circuit to give 'polyphony'. It was not really
polyphonic although different descriptions will tell you it had 10 voices. 
These write-ups are by people who probably only had 10 fingers, the truth is
that the organ circuit was as per any other - it had a master oscillator at
about 2MHz and this was divided using binary counters to deliver a frequency
for every note. The output of the 'poly' section was lamentable at best, it is
a fairly pure square wave passed through the filter and contour. This is fully
emulated although in addition to the contour bristol implements a per note
envelope just to groom the note - this prevents ticks when new keys are pressed
with the mono envelope fully open. There is no access to this env, it just has
fast attack and decay times to smooth the signal and is preconfigured by the
user interface on startup.

The mono section is reasonably fun, the oscillators can be synchronised and
there is a ring modulator so the range of sounds is quite wide. The emulator
uses a chaimberlain filter so is not as warm as the Moog ladder filters.

The list of people who used this is really quite amazing. The promotion for
the product had Elton John holding one up in the air, although seeing as he
probably already had every other synth known to man, holding it up in the
air is likely to be all he ever did with it. Who knows how much they had to
pay him to do it - the photo was nice though, from the days when Elton was
still bald and wearing ridiculously oversized specs.

Tuning:

    One control each for the poly oscillator and mono oscillators

Glide:

    Only affects the monophonic oscillators.

Modulation:

    One LFO with rate and waveshape selection
        produces tri, square and S/H signals.
        can trigger the envelope
    One noise source.
    The modulation can be directed to:
        Oscillators for vibrato
        Filter for wah-wah effects

Oscillator-1:

    Tri or square wave
    Octave from -2 to 0 transposition
    Sync selector (synchronises Osc-2 to Osc-1)

Oscillator-2:

    Tri or pulse wave
    Detune. This interoperates with the sync setting to alter harmonics
    Octave from -1 to +1 transposition

Contour: This is not an ADSR, rather an AR envelope

    Sustain: AR or ASR envelope selector.
    Tracking: controls mono oscillators
        Envelope control
        Key tracking (gate, no env)
        Continuous (always on)
    Rise (attack time)
    Fall (release time)

Filter:

    Cutoff frequency
    Emphasis
    Contour depth
    Keyboard tracking off, 1/2, full.

Mixer: Levels for
    Mono Osc-1
    Mono Osc-2
    Noise
    RingMod of the mono oscillators (called 'bell').
    Poly Osc level.

Master Volume control.

One extra button was added to save the current settings. For the rest the 
controls reflect the simplicity of the original. The implementation is a single
synth, however due to the engine architecture having a pre-operational routine,
a post-operational routine and an operate(polyphonic emulator) the emulation
executes the mono synth in the pre- and post- ops to be mono, these are called
just once per cycle. The poly synth is executed in the operate() code so is 
polyphonic. This leads to one minor deviation from the original routing in
that if you select continuous tone controls then you will also hear one note
from the poly section. This is a minor issue as the poly oscillator can be
zeroed out in the mixer.

It is noted here that this emulation is just a freebie, the interface is kept
simple with no midi channel selection (start it with the -channel option and
it stays there) and no real memories (start it with the -load option and it
will stay on that memory location). There is an extra button on the front
panel (a mod?) and pressing it will save the current settings for next time
it is started. I could have done more, and will if people are interested, but
I built it since the current developments were a granular synth and it was
hard work getting my head around the grain/wave manipulations, so to give 
myself a rest I put this together one weekend. The Rhodesbass and ARP AXXE
were done for similar reasons. I considered adding another mod button, to make
the mono section also truly polyphonic but that kind of detracts from the
original. Perhaps I should put together a Polymoog sometime that did kind of
work like that anyway.

This was perhaps a strange choice, however I like the way it highlights the
difference between monophonic, polyphonic and 'neopolyphonic' synthesised
organs (such as the polymoog). Its a fun synth as well, few people are likely
to every bother buying one as they cost more now than when they were produced
due to being collectable: for the few hundred dollars they would set you back
on eBay you can get a respectable polyphonic unit.
So here is an emulator, for free, for those who want to see how they worked.
