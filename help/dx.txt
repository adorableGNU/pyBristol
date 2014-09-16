    Yamaha DX-7
    -----------

Released in the '80s this synth quickly became the most popular of all time.
It was the first fully digital synth, employed a revolutionary frequency 
modulated algorithm and was priced much lower than the analogue monsters
that preceded it. Philip Glass used it to wide effect for Miami Vice, Prince
had it on many of his albums, Howard Jones produced albums filled with its
library sounds. The whole of the 80's were loaded with this synth, almost to
the point of saturation. There was generally wide use of its library sounds
due to the fact that it was nigh on impossible to programme, only having entry
buttons and the algorithm itself was not exactly intuitive, but also because
the library was exceptional and the voices very playable. The emulation is a
6 operator per voice, and all the parameters are directly accessible to ease
programming.

The original DX had six operators although cheaper models were release with
just 4 operators and a consequently thinner sound. Each operator is a sine
wave oscillator with its own envelope generator for amplification and a few 
parameters that adjusted its modulators. It used a number of different 
algorithms where operators were mixed together and then used to adjust the
frequency of the next set of operators. The sequence of the operators affected
the net harmonics of the overall sound. Each operator has a seven stage 
envelope - 'ramp' to 'level 1', 'ramp' to 'level 2', 'decay' to 'sustain',
and finally 'release' when a key is released. The input gain to the frequency
modulation is controllable, the output gain is also adjustable, and the final
stage operators can be panned left and right.

Each operator has:

    Envelope:

        Attack: Ramp rate to L1
        L1: First target gain level
        Attack: Ramp rate from L2 to L2
        L2: Second target gain level
        Decay: Ramp rate to sustain level
        Sustain: Continuous gain level
        Release: Key release ramp rate

    Tuning:

        Tune: +/- 7 semitones
        Transpose: 32' to 1' in octave increments

        LFO: Low frequency oscillation with no keyboard control

    Gain controls:

        Touch: Velocity sensitivity of operator.

        In gain: Amount of frequency modulation from input
        Out gain: Output signal level

        IGC: Input gain under Mod control
        OGC: Output gain under Mod control

        Pan: L/R pan of final stage operators.

Global and Algorithms:

    24 different operator staging algorithms
    Pitchwheel: Depth of pitch modifier
    Glide: Polyphonic portamento
    Volume
    Tune: Autotune all operators

Memories can be selected with either submitting a 3 digit number on the keypad,
or selecting the orange up/down buttons.

An improvement could be more preset memories with different sounds that can
then be modified, ie, more library sounds. There are some improvements that
could be made to polyphonic mods from key velocity and channel/poly pressure
that would not be difficult to implement.

The addition of triangle of other complex waveforms could be a fun development
effort (if anyone were to want to do it).

The DX still has a prependancy to seg fault, especially when large gains are
applied to input signals. This is due to loose bounds checking that will be
extended in a present release.
