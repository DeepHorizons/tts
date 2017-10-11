#!/usr/bin/env python3
"""
This is a helper to use the Microsoft SAPI

Needs to run on a Windows system
Requires comtypes
"""

import os # Allows checking if using Windows
try:
    assert(os.name == 'nt') # Checks for Windows
except:
    raise RuntimeError("Windows is required.")

import comtypes.client  # Importing comtypes.client will make the gen subpackage
try:
    from comtypes.gen import SpeechLib  # comtypes
except ImportError:
    # Generate the SpeechLib lib and any associated files
    engine = comtypes.client.CreateObject("SAPI.SpVoice")
    stream = comtypes.client.CreateObject("SAPI.SpFileStream")
    from comtypes.gen import SpeechLib


class Sapi(object):
    """A speech API using the Microsoft SAPI through COM"""

    def __init__(self):
        super().__init__()
        self.voice = comtypes.client.CreateObject('Sapi.SpVoice')

    def get_voices(self, name=''):
        """Get a list of voices, search by name optional"""
        voice_list = []
        voices = self.voice.GetVoices()

        if name is not '':
            for voice in voices:
                if name in voice.GetDescription():
                    voice_list.append(voice)
                    break
            else:
                print('Voice not found')
        else:
            for voice in voices:
                voice_list.append(voice)

        return voice_list

    def get_voice_names(self):
        """Get the names of all the voices"""
        return [voice.GetDescription() for voice in self.get_voices()]

    def set_voice(self, voice):
        """Set the voice to the given voice"""
        if type(voice) is str:
            self.voice.Voice = self.get_voices(voice)[0]
        else:
            self.voice.Voice = voice
        return

    def get_audio_outputs(self, name=''):
        """Get the audio outputs, search for the one with the name if given"""
        output_list = []
        outputs = self.voice.GetAudioOutputs()

        if name is not '':
            for output in outputs:
                if name in output.GetDescription():
                    output_list.append(output)
                    break
            else:
                print('Audio output not found')
        else:
            for output in outputs:
                output_list.append(output)

        return output_list

    def get_audio_output_names(self):
        """Get the names of all the audio outpus"""
        return [output.GetDescription() for output in self.get_audio_outputs()]

    def set_audio_output(self, output):
        if type(output) is str:
            self.voice.AudioOutput = self.get_audio_outputs(output)[0]
        else:
            self.voice.AudioOutput = output
        return

    def say(self, message):
        self.voice.Speak(message)
        return
    
    def set_rate(self, rate):
        """Set the speed of the speaker
        -10 is slowest, 10 is fastest"""
        self.voice.Rate = rate

    def _create_stream(self, filename):
        """Create a file stream handler"""
        stream = comtypes.client.CreateObject('Sapi.SpFileStream')
        stream.Open(filename, SpeechLib.SSFMCreateForWrite)
        return stream

    def create_recording(self, filename, message):
        """Make a recording of the given message to the file
        The file should be a .wav as the output is
        PCM 22050 Hz 16 bit, Little endianness, Signed"""
        stream = self._create_stream(filename)
        temp_stream = self.voice.AudioOutputStream
        self.voice.AudioOutputStream = stream
        self.say(message)
        self.voice.AudioOutputStream = temp_stream


if __name__ == '__main__':
    v = Sapi()
    v.set_voice('Anna')
    v.get_voice_names()
