    KORG POLY 6
    -----------

Korg in no way endorses this emulation of their classic synthesiser and have
their own emulation product that gives the features offered here. Korg,
Mono/Poly, Poly-6, MS-20, Vox and Continental are all registered names or
trademarks of Korg Inc of Japan.

Quite a few liberties were taken with this synth. There were extremely few  
differences between the original and the Roland Juno 6, they both had one osc  
with PWM and a suboscillator, one filter and envelope, a chorus effect, and  
inevitably both competed for the same market space for their given price. To  
differentiate this algorithm some alterations were made. There are two separate
envelopes rather than just one, but the option to have a gated amplifier is  
still there. In addition glide and noise were added, both of which were not in  
the original instrument. With respect to the original instrument this was  
perhaps not a wise move, but there seemed little point in making another Juno  
with a different layout. The net results is that the two synths do sound quite  
different. The emulation does not have an arpeggiator.  
 
    Volume: Master volume of the instrument  
 
    Glide: length of portamento  
 
    Tune: Master tuning of instrument  
 
    Bend: Amount of pitch wheel that is applied to the oscillators frequency.  
 
 
    VCO section:  

        Octave: What octave the instrument's keyboard is in.  
 
        Wave: Waveform selection: Triangle, Saw, Pulse and Pulsewidth  
 
        PW PWM: Amount of Pulsewidth (when Pulse is selected) and Pulsewidth
            Modulation (When Pulsewidth is selected).  
 
        Freq: Frequency of PW/PWM  
 
        OFF/SUB1/SUB2; Adds a square sub-oscillator either off, 1 or 2 octaves
            down from a note.  
 
    MG (Modulation Group):  
 
        Freq: Frequency of LFO  

        Delay: Amount of time before the LFO affects the destination when a key
            is pressed.  
        Level: How strongly the LFO affects the destination  
 
        VCO/VCF/VCA: Destinations that the LFO can go to:  
 
            VCO: The Voltage Controlled Oscillator:
                Affects oscillator pitch, producing vibrato  
 
            VCF: The Voltage Controlled Filter:
                Affects Filter, producing a wah effect  
 
            VCA: The Voltage Controlled Amplifier:
                Affects the Amplifier, producing tremolo  
 
    VCF section:  
 
        Freq: Cut off frequency of the filter  
 
        Res: Resonance of the filter  
 
        Env: By how much the filter is affected by the envelope.  
 
        Kbd: How much Keyboard tracking is applied to the envelope. note:

            A low setting doesn't allow the filter to open, making the notes
            seem darker the further you go up the keyboard.  
 
    Hold: prevent key off events  
 
    Mono Mode: Gang all voices to a single 'fat' monophonic synthesiser.  
 
    Poly: One voice per note.  
 
    Envelope Section:  
 
        Top:  
 
        Filter envelope: 
 
            Attack: Amount of time it takes the filter to fully open.
                A high value can produce a 'sweeping filter' effect. 
            Decay: Amount of time it takes for the filter to close to
                the sustain level 
            Sustain: Amount of filter that is sustained when a key is held 

            Release: Amount of time it takes for the filter envelope to stop
                affecting the filter. Combining a low filter release with a
                high amplitude release time can cause an interesting effect. 
 
        Bottom:  
 
        Amplitude envelope:  
 
        Attack: Amount of time it takes for the signal to reach its peak. 

        Decay: Amount of time it takes for the signal to drop to the
            sustain level 
        Sustain: How quickly the sound decays to silence. 

        Release: How long it takes the sound to decay to silence after
            releasing a key. 
 
    VCA:  

        Env: When on, this causes the Amplitude envelope to affect the sound.
            I.E, If you have a long attack time, you get a long attack time. 
        Gate: When on, this causes the Amplitude envelope only (not the filter
            envelope) to be be bypassed.  
        Gain: Gain of signal. 
 
    Effects Section:  

        0: No effects  
        1: Soft Chorus  
        2: Phaser  
        3: Ensemble  
 
        Intensity: How much the effects affect the output. 

There are some mildly anomolous effects possible from the MG section, especially
with the VCA. The MG and the env are summed into the VCA which means if the env
decays to zero then the LFO may end up pumping the volume, something that may
be unexpected. Similarly, if the LFO is pumping and the voice finally stops its
cycle then the closing gate may cause a pop on the MG signal. These can be 
resolved however the current behavious is probably close to the original.

Bristol thanks Andrew Coughlan for patches, bug reports, this manual page and
diverse suggestions to help improve the application.

Korg in no way endorses this emulation of their classic synthesiser and have  
their own emulation product that gives the features offered here. Korg,  
Mono/Poly, Poly-6, MS-20, Vox and Continental are all registered names or  
trademarks of Korg Inc of Japan.
