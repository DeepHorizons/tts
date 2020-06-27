#!/usr/bin/env python3
from enum import Enum

class SpeechVoiceSpeakFlags(Enum):
    # SpVoice Flags
    Default = 0
    FlagsAsync = 1
    PurgeBeforeSpeak = 2
    IsFilename = 4
    IsXML = 8
    IsNotXML = 16
    PersistXML = 32

    # Normalizer Flags
    NLPSpeakPunc = 64

    # Masks
    NLPMask = 64
    VoiceMask = 127
    UnusedFlags = -128