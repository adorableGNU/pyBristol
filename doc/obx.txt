    Oberheim OB-X
    -------------

Oberheim was the biggest competitor of Sequential Circuits, having their OB
range neck and neck with each SC Prophet. The sound is as fat, the OB-X 
similar to the Prophet-5 as the OB-Xa to the Prophet-10. The synths were widely
used in rock music in the late seventies and early 80s. Their early polyphonic
synthesisers had multiple independent voices linked to the keyboard and were
beast to program as each voice was configured independently, something that
prevented much live usage. The OB-X configured all of the voices with the same
parameters and had non-volatile memories for instant recall.

Priced at $6000 upwards, this beast was also sold in limited quantities and
as with its competition gained and maintained a massive reputation for rich,
fat sounds. Considering that it only had 21 continuous controllers they were
used wisely to build its distinctive and flexible sound.

The general design again follows that of the Mini Moog, three oscillators with
one dedicated as an LFO the other two audible. Here there is no mixer though,
the two audible oscillators feed directly into the filter and then the amplifier.

The richness of the sound came from the oscillator options and filter, the 
latter of which is not done justice in the emulator.

Manual:

    Volume
    Auto: autotune the oscillators
    Hold: disable note off events
    Reset: fast decay to zero for envelopes, disregards release parameter.
    Master Tune: up/down one semitone both oscillators.

Control:

    Glide: up to 30 seconds
    Oscillator 2 detune: Up/down one semitone

    Unison: gang all voices to a single 'fat' monophonic synthesiser.

Modulation:

    LFO: rate of oscillation
    Waveform: Sine/Square/Sample&Hold of noise src. Triangle if none selected.

    Depth: Amount of LFO going to:
        Freq Osc-1
        Freq Osc-2
        Filter Cutoff

    PWM: Amount of LFO going to:
        PWM Osc-1
        PWM Osc-2

Oscillators:

    Freq1: 32' to 1' in octave increments.
    PulseWidth: Width of pulse wave (*).
    Freq2: 16' to 1' in semitone increments.

    Saw: sawtooth waveform Osc-1 (**)
    Puls: Pulse waveform Osc-1

    XMod: Osc-1 FW to Osc-2 (***)
    Sync: Osc-2 sync to Osc-1

    Saw: sawtooth waveform Osc-2
    Puls: Pulse waveform Osc-2

    * Although this is a single controller it acts independently on each of the
    oscillators - the most recent to have its square wave selected will be
    affected by this parameter allowing each oscillator to have a different
    pulse width as per the original design.

    ** If no waveform is selected then a triangle is generated.

    *** The original synth had Osc-2 crossmodifying Osc-1, this is not totally
    feasible with the sync options as they are not mutually exclusive here.
    Cross modulation is noisy if the source or dest wave is pulse, something
    that may be fixed in a future release.

Filter:

    Freq: cutoff frequency
    Resonance: emphasis (*)
    Mod: Amount of modulation to filter cutoff (**)

    Osc-1: Osc-1 to cutoff at full swing.
    KDB: Keyboard tracking of cutoff.

    Half/Full: Oscillator 2 to Cutoff at defined levels (***)
    Half/Full: Noise to Cutoff at defined levels (***)

    * In contrast to the original, this filter can self oscillate.

    ** The original had this parameter for the envelope level only, not the
    other modifiers. Due to the filter implementation here it affects total
    depth of the sum of the mods.

    *** These are not mutually exclusive. The 'Half' button gives about 1/4,
    the 'Full' button full, and both on gives 1/2. They could be made mutually
    exclusive, but the same effect can be generated with a little more flexibility
    here.

Envelopes: One each for filter and amplifier.

    Attack
    Decay
    Sustain
    Release

The oscillators appear rather restricted at first sight, but the parametrics
allow for a very rich and cutting sound.

Improvements would be a fatter filter, but this can be argued of all the 
Bristol synthesisers as they all share the same design. It will be altered in
a future release.

The OB-X has its own mod panel (most of the rest share the same frequency and
mod controls). Narrow affects the depth of the two controllers, Osc-2 will 
make frequency only affect Osc-2 rather than both leading to beating, or phasing
effects if the oscillators are in sync. Transpose will raise the keyboard by
one octave.

Memories are quite simple, the first group of 8 buttons is a bank, the second
is for 8 memories in that bank. This is rather restricted for a digital synth
but is reasonably true to the original. If you want more than 64 memories let
me know.
