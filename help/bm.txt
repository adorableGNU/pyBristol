    Bristol BassMaker
    -----------------

The BassMaker is not actually an emulator, it is a bespoke sequencer design but
based on the capabilities of some of the early analogue sequencers such as the
Korg SQ-10. Supplying this probably leaves bristol open to a lot of feature
requests for sequencer functionaliity and it is stated here that the BassMaker
is supposed to be simple so excess functionality will probably be declined as
there are plenty of other sequencing applications that can provide a richer
feature set.

The main page gives access to a screen of controls for 16 steps and a total of
4 pages are available for a total of 64 steps. The pages are named 'A' through
'D'. Each step has 5 options:

    Note: one octave of note selection
    Transpose: +/- one octave transposition of the note.
    Volume: MIDI note velocity
    Controller: MIDI modulation, discussed further below
    Triggers: Note On/Off enablers

The trigger button gives 4 options indicated by the LED:

    off: note on/off are sent
    red: only send note_on
    green: only send note_off
    yellow: do not send note on/off

The 'Controllers' setting has multiple functions which can be selected from
the menu as explained below. The options available are as follows:

    Send semitone tuning

    Send glide rate

    Send modwheel

    Send expression pedal (controller value)

    Send Note: the controller will be 12 discrete steps as per the 'Note' 
    setting and this note will be sent on the Secondary MIDI channel.

The semitone tuning and glide work for the majority of the emulations. Some do
not support fine tune controls (Vox, Hammond, others). If you are missing these
capabilities for specific emulators raise a change request on Sourceforge.net.

At the top of the window there is a panel to manage the sequencer. It has the
following functions:

    Speed: step rate through the notes
    DutyCycle: ratio of note-on to note-off

    Start/Pause
    Stop: stop and return to first step/page

    Direction:
        Up
        Down
        Up/Down
        Random

    Select: which of the pages to include in the sequence.
    Edit: which page is currently displayed to be edited.

    Memory:
        0..9 key entry buttons, 1000 memories available
        Load
        Save: doubleclick to save current sequence

    Menu Panel
        Up, Down menu
        Function (return to previous level)
        Enter: enter submenu or enter value if in submenu

The menu consists of several tables, these can be stepped through using the Up
and Down arrows to move through the menu and the 'Enter' arrow to select a sub
menu or activate any option. The 'Fn' button returns one level:

    Memory:

        Find next free memory upwards
        Find next memory upwards
        Find next memory downwards

    Copy:

        Copy current edit page to 'A', 'B', 'C' or 'D'.

    Control - Set the control value to send:

        semitone tuning
        glide rate
        modwheel
        expression pedal (controller value)
        note events

    First midi channel

        Primary midi channel for note events

    Second midi channel

        Secondary midi channel when 'Control' configured to 'Note' events.

    Global Transpose

        Transpose the whole sequence up or down 12 semitones

    Clear - configure default value for all of the:

        Notes to zero
        Transpose to zero (midpoint)
        Volume to 0.8
        Control to midpoint
        Triggers to on/off

As of the first release in 0.30.8 large parts of the Controllers functionality
was only lightly tested. If you do not get the results you anticipate you may
require a fix.
