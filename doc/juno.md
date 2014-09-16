    Roland Juno-60
    --------------

Roland was one of the main pacemakers in analogue synthesis, also competing
with the Sequential and Oberheim products. They did anticipate the moving
market and produced the Juno-6 relatively early. This was one of the first
accessible synths, having a reasonably fat analogue sound without the price
card of the monster predecessors. It brought synthesis to the mass market that
marked the decline of Sequential Circuits and Oberheim who continued to make
their products bigger and fatter. The reduced price tag meant it had a slightly
thinner sound, and a chorus was added to extend this, to be a little more
comparable.

The synth again follows the Mini Moog design of oscillators into filter into
amp. The single oscillator is fattened out with harmonics and pulse width
modulation. There is only one envelope generator that can apply to both the
filter and amplifier.

Control:

    DCO: Amount of pitch wheel that is applied to the oscillators frequency.
    VCF: Amount of pitch wheel that is applied to the filter frequency.

    Tune: Master tuning of instrument

    Glide: length of portamento

    LFO: Manual control for start of LFO operation.

Hold: (*)

    Transpose: Up/Down one octave
    Hold: prevent key off events

LFO:

    Rate: Frequency of LFO
    Delay: Period before LFO is activated
    Man/Auto: Manual or Automatic cut in of LFO

DCO:

    LFO: Amount of LFO affecting frequency. Affected by mod wheel.
    PWM: Amount of LFO affecting PWM. Affected by mod wheel.

    ENV/LFO/MANUAL: Modulator for PWM

    Waveform:
        Pulse or Ramp wave. Pulse has PWM capabily.
    
    Sub oscillator:
        On/Off first fundamental square wave.
    
    Sub:
        Mixer for fundamental

    Noise:
        Mixer of white noise source.

HPF: High Pass Filter

    Freq:
        Frequency of cutoff.

VCF:

    Freq:
        Cutoff frequency

    Res:
        Resonance/emphasis.
    
    Envelope:
        +ve/-ve application
    
    Env:
        Amount of contour applied to cutoff
    
    LFO:
        Depth of LFO modulation applied.
    
    KBD:
        Amount of key tracking applied.

VCA:

    Env/Gate:
        Contour is either gated or modulated by ADSR
    
    Level:
        Overall volume

ADSR:

    Attack
    Decay
    Sustain
    Release

Chorus:

    8 Selectable levels of Dimension-D type helicopter flanger.

* The original instrument had a basic sequencer on board for arpeggio effects
on each key. In fact, so did the Prophet-10 and Oberheims. This was only 
implemented in 0.10.11.

The LFO cut in and gain is adjusted by a timer and envelope that it triggers.

The Juno would improve from the use of the prophet DCO rather than its own one.
It would require a second oscillator for the sub frequency, but the prophet DCO
can do all the Juno does with better resampling and PWM generation.
