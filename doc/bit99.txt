    CRUMAR BIT-1, BIT-99, BIT-100
    -----------------------------

I was considering the implementation of the Korg-800, a synth I used to borrow
without having due respect for it - it was a late low cost analogue having 
just one filter for all the notes and using the mildly annoying data entry
buttons and parameter selectors. Having only one filter meant that with key
tracking enabled the filter would open up as different keys were pressed,
wildly changing the sound of active notes. Anyway, whilst considering how to
implement the entry keys (and having features like the mouse tracking the
selectors of the parameter graphics) I was reminded of this synthesizer. It
was developed by Crumar but released under the name 'Bit' as the Crumar name
was associated with cheesy roadrunner electric pianos at the time (also
emulated by Bristol). This came out at the same time as the DX-7 but for
half the price, and having the split and layer facilities won it several awards
that would otherwise have gone to the incredibly innovative DX. However with
the different Crumar models being released as the digital era began they kind
of fell between the crack. It has some very nice mod features though, it was
fun to emulate and hopefully enjoyable to play with.

As a side note, the Korg Poly-800 is now also emulated by bristol

A quick rundown of the Bit features are below. The different emulated models
have slightly different default parameter values and/or no access to change
them:

    Two DCO with mixed waveforms.
    VCF with envelope
    VCA with envelope
    Two LFO able to mod all other components, controlled by the wheel and key
    velocity, single waveform, one had ramp and the other sawtooth options.

The envelopes were touch sensitive for gain but also for attack giving plenty 
of expressive capabilities. The bristol envelope, when configured for velocity
sensitive parameters (other than just gain) will also affect the attack rate.

The front panel had a graphic that displayed all the available parameters and
to change then you had to select the "Address" entry point then use the up/down
entry buttons to change its value. Bristol uses this with the addition that the
mouse can click on a parameter to start entering modifications to it.

The emulation includes the 'Compare' and 'Park' features although they are a
little annoying without a control surface. They work like this (not quite the
same as the original): When you select a parameter and change it's value then
the changes are not actually made to the active program, they just change the
current sounds. The Compare button can be used to flip between the last loaded
value and the current modified one to allow you to see if you prefer the sound
before or after the modification.

If you do prefer the changes then to keep them you must "Park" them into the
running program before saving the memory. At the time of writing the emulation
emulated the double click to park&write a memory, however it also has an actual
Save button since 'Save to Tape' is not a feature here. You can use park and
compare over dual loaded voices: unlike the original, which could only support
editing of sounds when not in split/double, this emulation allows you to edit
both layers by selecting the upper/lower entry buttons and then using the
sensitive panel controls to select the addressed parameters. This is not the
default behaviour, you first have to edit address 102 and increment it. Then,
each layer can be simultaneously edited and just needs to be parked and saved
separately. The Park/Compare cache can be disabled by editing parameter DE 101,
changes are then made to the synth memory and not the cache.

The memories are organised differently to the original. It had 99 memories, and
the ones from 75 and above were for Split and Layered memories. Bristol can 
have all memories as Split or Layer. When you save a memory it is written to
memory with a 'peer' program locator. When you load it with a single push on 
the Load button it returns to the active program, but if you double click then
its 'peer' program is loaded into the other layer: press Load once to get the
first program entered, then press it again - the Split/Layer will be set to
the value from the first program and the second layer will be loaded. This 
naturally requires that the first memory was saved with Split/Layer enabled.
It is advised (however not required) that this dual loading is done from the
lower layer. This sequence will allow the lower layer to configure certain
global options that the upper layer will not overwrite, for example the layer
volumes will be select from the lower layer when the upper layer is dual 
loaded.

For MIDI program change then since this quirky interface cannot be emulated
then the memories above 75 will be dual loaded, the rest will be single loaded.

Bristol will also emulate a bit-99 and a Bit-99m2 that includes some parameter
on the front panel that were not available on the original. The engine uses the
exact same algorithm for all emulations but the GUI presents different sets of
parameters on the front panel. Those that are not displayed can only be accessed
from the data entry buttons. The -99m2 put in a few extra features (ie, took a
few liberties) that were not in the original:

    DCO adds PWM from the LFO, not in the original
    DCO-2 adds Sync to DCO-1, also not in the original
    DCO-2 adds FM from DCO-1
    DCO add PWM from Envelope
    Glide has been added
    DCO harmonics are not necessarily exclusive
    Various envelope option for LFO
    S&H LFO modulation

The reason these were added was that bristol could already do them so were
quite easy to incorporate, and at least gave two slightly different emulations.

The oscillators can work slightly differently as well. Since this is a purely
digital emulations then the filters are a bit weak. This is slightly compensated
by the ability to configure more complex DCO. The transpose selectors (32', 16',
8' and 2') were exclusive in the original. That is true here also, however if
controllers 84 and 85 are set to zero then they can all work together to fatten
out the sound. Also, the controllers look like boolean however that is only the
case if the data entry buttons are used, if you change the value with the data
entry pot then they act more like continuous drawbars, a nice effect however 
the display will not show the actual value as the display remains boolean, you
have to use your ear. The square wave is exclusive and will typically only 
function on the most recently selected (ie, typically highest) harmonic.

The same continuous control is also available on the waveform selectors. You
can mix the waveform as per the original however the apparent boolean selectors
are again continuous from 0.0 to 1.0. The net result is that the oscillators 
are quite Voxy having the ability to mix various harmonic levels of different
mixable waveforms.

The stereo mode should be correctly implemented too. The synth was not really
stereo, it had two outputs - one for each layer. As bristol is stereo then each
layer is allocated to the left or right channel. In dual or split they came
out separate feeds if Stereo was selected. This has the rather strange side
effect of single mode with 6 voices. If stereo is not selected then you have
a mono synth. If stereo is selected then voices will exit from a totally 
arbitrary output depending on which voices is allocated to each note.
In contrast to the original the Stereo parameter is saved with the memory and
if you dual load a split/layer it is taken from the first loaded memory only.
The implementation actually uses two different stereo mixes selectable with the
Stereo button: Mono is a centre pan of the signal and Stereo pans hardleft and
hardright respectively. These mixes can be changed with parameters 110 to 117
using extended data entry documented below.

The default emulation takes 6 voices for unison and applies 3+3 for the split
and double modes. You can request more, for example if you used '-voices 16'
at startup then you would be given 8+8. As a slight anomaly you cant request 32
voices - this is currently interpreted as the default and gives you 3+3.

The bit-1 did not have the Stereo control - the controller presented is the
Unison button. You can configure stereo from the extended data entry ID 110 and
111 which give the LR channel panning for 'Mono' setting, it should default to
hard left and right panning. Similarly the -99 emulations do not have a Unison
button, the capability is available from DE 80.

The memories for the bit-1 and bit-99 should be interchangeable however the
code maintains separate directories.

There are three slightly different Bit GUI's. The first is the bit-1 with a 
limited parameter set as it only had 64 parameters. The second is the bit-99
that included midi and split options in the GUI and has the white design that
was an offered by Crumar. The third is a slightly homogenous design that is 
specific to bristol, similar to the black panelled bit99 but with a couple of
extra parameters. All the emulations have the same parameters, some require you
use the data entry controls to access them. This is the same as the original, 
there were diverse parameters that were not in memories that needed to be
entered manually every time you wanted the feature. The Bristol Bit-99m2 has
about all of the parameters selectable from the front panel however all of the
emulations use the same memories so it is not required to configure them at
startup (ie, they are saved). The emulation recognises the following parameters:

    Data Entry  1 LFO-1 triangle wave selector (exclusive switch)
    Data Entry  2 LFO-1 ramp wave selector (exclusive switch)
    Data Entry  3 LFO-1 square wave selector (exclusive switch)
    Data Entry  4 LFO-1 route to DCO-1
    Data Entry  5 LFO-1 route to DCO-2
    Data Entry  6 LFO-1 route to VCF
    Data Entry  7 LFO-1 route to VCA
    Data Entry  8 LFO-1 delay
    Data Entry  9 LFO-1 frequency
    Data Entry 10 LFO-1 velocity to frequency sensitivity
    Data Entry 11 LFO-1 gain
    Data Entry 12 LFO-1 wheel to gain sensitivity

    Data Entry 13 VCF envelope Attack
    Data Entry 14 VCF envelope Decay
    Data Entry 15 VCF envelope Sustain
    Data Entry 16 VCF envelope Release
    Data Entry 17 VCF velocity to attack sensitivity (and decay/release) 
    Data Entry 18 VCF keyboard tracking
    Data Entry 19 VCF cutoff
    Data Entry 20 VCF resonance
    Data Entry 21 VCF envelope amount
    Data Entry 22 VCF velocity to gain sensitivity
    Data Entry 23 VCF envelope invert

    Data Entry 24 DCO-1 32' harmonic
    Data Entry 25 DCO-1 16' harmonic
    Data Entry 26 DCO-1 8' harmonic
    Data Entry 27 DCO-1 4' harmonic
    Data Entry 28 DCO-1 Triangle wave
    Data Entry 29 DCO-1 Ramp wave
    Data Entry 30 DCO-1 Pulse wave
    Data Entry 31 DCO-1 Frequency 24 semitones
    Data Entry 32 DCO-1 Pulse width
    Data Entry 33 DCO-1 Velocity PWM
    Data Entry 34 DCO-1 Noise level

    Data Entry 35 DCO-2 32' harmonic
    Data Entry 36 DCO-2 16' harmonic
    Data Entry 37 DCO-2 8' harmonic
    Data Entry 38 DCO-2 4' harmonic
    Data Entry 39 DCO-2 Triangle wave
    Data Entry 40 DCO-2 Ramp wave
    Data Entry 41 DCO-2 Pulse wave
    Data Entry 42 DCO-2 Frequency 24 semitones
    Data Entry 43 DCO-2 Pulse width
    Data Entry 44 DCO-2 Env to pulse width
    Data Entry 45 DCO-2 Detune

    Data Entry 46 VCA velocity to attack sensitivity (and decay/release) 
    Data Entry 47 VCA velocity to gain sensitivity
    Data Entry 48 VCA overall gain ADSR
    Data Entry 49 VCA Attack
    Data Entry 50 VCA Decay
    Data Entry 51 VCA Sustain
    Data Entry 52 VCA Release

    Data Entry 53 LFO-2 triangle wave selector (exclusive switch)
    Data Entry 54 LFO-2 saw wave selector (exclusive switch)
    Data Entry 55 LFO-2 square wave selector (exclusive switch)
    Data Entry 56 LFO-2 route to DCO-1
    Data Entry 57 LFO-2 route to DCO-2
    Data Entry 58 LFO-2 route to VCF
    Data Entry 59 LFO-2 route to VCA
    Data Entry 60 LFO-2 delay
    Data Entry 61 LFO-2 frequency
    Data Entry 62 LFO-2 velocity to frequency sensitivity
    Data Entry 63 LFO-2 gain
    Data Entry 12 LFO-2 wheel to gain sensitivity

    Data Entry 64 Split
    Data Entry 65 Upper layer transpose
    Data Entry 66 Lower Layer gain
    Data Entry 67 Upper Layer gain

The following were visible in the Bit-99 graphics only:

    Data Entry 68 MIDI Mod wheel depth
    Data Entry 69 MIDI Velocity curve (0 = soft, 10=linear, 25 = hard)
    Data Entry 70 MIDI Enable Debug
    Data Entry 71 MIDI Enable Program Change
    Data Entry 72 MIDI Enable OMNI Mode
    Data Entry 73 MIDI Receive channel

    Data Entry 74 MIDI Mem Search Upwards
    Data Entry 75 MIDI Mem Search Downwards
    Data Entry 76 MIDI Panic (all notes off)

Most of the MIDI options are not as per the original. This is because they are
implemented in the bristol MIDI library and not the emulation.

The following were added which were not really part of the Bit specifications
so are only visible on the front panel of the bit100. For the other emulations
they are accessible from the address entry buttons.

    Data Entry 77 DCO-1->DCO-2 FM
    Data Entry 78 DCO-2 Sync to DCO-1
    Data Entry 79 Keyboard glide
    Data Entry 80 Unison

    Data Entry 81 LFO-1 SH
    Data Entry 82 LFO-1 PWM routing for DCO-1
    Data Entry 83 LFO-1 PWM routing for DCO-2
    Data Entry 84 LFO-1 wheel tracking frequency
    Data Entry 85 LFO-1 velocity tracking gain
    Data Entry 86 LFO-1 per layer or per voice

    Data Entry 87 LFO-2 SH
    Data Entry 88 LFO-2 PWM routing for DCO-1
    Data Entry 89 LFO-2 PWM routing for DCO-2
    Data Entry 90 LFO-2 wheel tracking frequency
    Data Entry 91 LFO-2 velocity tracking gain
    Data Entry 92 LFO-2 per layer or per voice

    Data Entry 93 ENV-1 PWM routing for DCO-1
    Data Entry 94 ENV-1 PWM routing for DCO-2

    Data Entry 95 DCO-1 restricted harmonics
    Data Entry 96 DCO-2 restricted harmonics

    Data Entry 97 VCF Filter type
    Data Entry 98 DCO-1 Mix

    Data Entry 99 Noise per layer

    Data Entry 00 Extended data entry (above 99)
    
Extended data entry is for all parameters above number 99. Since the displays
only have 2 digits it is not totally straightforward to enter these values and
they are only available in Single mode, not dual or split - strangely similar
to the original specification for editing memories. These are only activated for
the lower layer loaded memory, not for dual loaded secondaries or upper layer
loaded memories. You can edit the upper layer voices but they will be saved with
their original extended parameters. This may seem correct however it is possible
to edit an upper layer voice, save it, and have it sound different when next
loaded since the extended parameters were taken from a different lower layer.
This is kind of intentional but if in doubt then only ever dual load voices from
the lower layer and edit them in single mode (not split or layer). Per default
the emulation, as per the original, will not allow voice editing in Split or
Layer modes however it can be enabled with DE 102.

All the Bit emulations recognise extended parameters. They are somewhat in a
disorganised list as they were built in as things developed. For the most part
they should not be needed.
The Bit-100 includes some in its silkscreen, for the others you can access them
as follows:

1. deselect split or double
2. select addr entry
3. use 0..9 buttons to enter address 00
4. increment value to '1'. Last display should show EE (Extended Entry)

5. select last two digits of desired address with 0-9 buttons
6. change value (preferably with pot).

7. when finished, select address 00 again (this is now actually 100) to exit

    Data Entry 100 Exit extended data entry
    Data Entry 101 enable WriteThru scratchpad (disables park and compare)
    Data Entry 102 enable layer edits on Split/Double memories.
    Data Entry 103 LFO-1 Sync to note on
    Data Entry 104 LFO-2 Sync to note on
    Data Entry 105 ENV-1 zero retrigger
    Data Entry 106 ENV-2 zero retrigger
    Data Entry 107 LFO-1 zero retrigger
    Data Entry 108 LFO-2 zero retrigger
    Data Entry 109 Debug enable (0 == none, 5 == persistent)

    Data Entry 110 Left channel Mono gain, Lower
    Data Entry 111 Right channel Mono gain, Lower
    Data Entry 112 Left channel Stereo gain, Lower
    Data Entry 113 Right channel Stereo gain, Lower
    Data Entry 114 Left channel Mono gain, Upper
    Data Entry 115 Right channel Mono gain, Upper
    Data Entry 116 Left channel Stereo gain, Upper
    Data Entry 117 Right channel Stereo gain, Upper
    Data Entry 118 Bit-100 flag
    Data Entry 119 Temperature sensitivity

    Data Entry 120 MIDI Channel tracking layer-2 (same/different channel)
    Data Entry 121 MIDI Split point tracking layer-2 (same/different split)
    Data Entry 122 MIDI Transpose tracking (layer-2 or both layers) N/A
    Data Entry 123 MIDI NRP enable

    Data Entry 130 Free Memory Search Up
    Data Entry 131 Free Memory Search Down
    Data Entry 132 ENV-1 Conditional
    Data Entry 133 ENV-2 Conditional
    Data Entry 134 LFO-1 ENV Conditional
    Data Entry 135 LFO-2 ENV Conditional
    Data Entry 136 Noise white/pink
    Data Entry 137 Noise pink filter (enable DE 136 Pink)
    Data Entry 138 Glide duration 0 to 30 seconds
    Data Entry 139 Emulation gain level

    Data Entry 140 DCO-1 Square wave gain
    Data Entry 141 DCO-1 Subharmonic level
    Data Entry 142 DCO-2 Square wave gain
    Data Entry 143 DCO-2 Subharmonic level

The 150 range will be incorporated when the Arpeggiator code is more stable,
currently in development for the Jupiter. This is anticipated in 0.20.4:

    Data Entry 150 Arpeggiator Start/Stop
    Data Entry 151 Arpeggiator mode D, U/D, U or Random
    Data Entry 152 Arpeggiator range 1, 2, 3, 4 octaves
    Data Entry 153 Arpeggiator rate
    Data Entry 154 Arpeggiator external clock
    Data Entry 155 Arpeggiator retrigger envelopes
    Data Entry 156 Arpeggiator poly-2 mode
    Data Entry 157 Chord Enable
    Data Entry 158 Chord Relearn
    Data Entry 159 Sequencer Start/Stop
    Data Entry 160 Sequencer mode D, U/D, U or Random
    Data Entry 161 Sequencer range 1, 2, 3, 4 octaves
    Data Entry 162 Sequencer rate
    Data Entry 163 Sequencer external clock
    Data Entry 164 Sequencer retrigger envelopes
    Data Entry 165 Sequencer Relearn

The following can be manually configured but are really for internal uses only
and will be overwritten when memories are saved to disk. The Split/Join flag,
for example, is used by dual loading memories to configure the peer layer to
load the memory in DE-198, and the stereo placeholder for configuring the stereo
status of any single loaded memory.

    Data Entry 193 Reserved: save bit-1 formatted memory
    Data Entry 194 Reserved: save bit-99 formatted memory
    Data Entry 195 Reserved: save bit-100 formatted memory
    Data Entry 196 Reserved: Split/Join flag - internal use
    Data Entry 197 Reserved: Stereo placeholder - internal use
    Data Entry 198 Reserved: Peer memory pointer - internal use
    Data Entry 199 Reserved: DCO-2 Wheel mod (masks entry 12) - internal use

The tuning control in the emulation is on the front panel rather than on the
rear panel as in the original. It had a keyboard sensitivity pot however that
is achieved separately with bristol using velocity curves from the MIDI control
settings. The front panel rotary defaults to 0% tuning and is not saved in the
memory. The front panel gain controls are also not saved in the memory and
default to 0.8 at startup.

The net emulation is pretty intensive as it runs with over 150 operational
parameters.

A few notes are required on oscillator sync since by default it may seem to 
be quite noisy. The original could only produce a single waveform at a single
frequency at any one time. Several emulators, including this one, use a bitone
oscillator which generates complex waveforms. The Bristol Bitone can generate
up to 4 waveforms simultaneously at different levels for 5 different harmonics
and the consequent output is very rich, the waves can be slightly detuned, 
the pulse output can be PW modulated. As with all the bristol oscillators that
support sync, the sync pulse is extracted as a postive leading zero crossing.
Unfortunately if the complex bitone output is used as input to sync another
oscillator then the result is far too many zero crossings to extract a good
sync.
Code has been implemented to generate a second sync source using a side output
sync wave which is then fed to a sideband sync input on the oscillator, the
results are far better
