tts - A lightweight python TTS wrapper
======================================
tts is a python wrapper around Text To Speech api's

Currently only supports SAPI

Setup
-----
To install, simply use pip and point it at the repository

```
pip install git+https://github.com/DeepHorizons/tts
```

To Use
------
Import the tts package with the api you wish to use

### SAPI
```python
import tts.sapi
voice = tts.sapi.Sapi()
voice.say("Hello")
voice.set_voice("Anna")

voice.create_recording('output.wav', "This will be in a wav file")

voice.set_rate(-5)
voice.say("This will be said slower")

voice.set_volume(30)
voice.say("This will be said on a lower volume")
```

Aside from text, it also support [SSML](https://docs.microsoft.com/en-us/cortana/skills/speech-synthesis-markup-language). You'll need to pass the `SpeechVoiceSpeakFlags.IsXML` flag as a second parameter for the `say()` function
```python
import tts.sapi
import tts.flags

voice = tts.sapi.Sapi()

voice.say('<PRON SYM = "h eh l ow"/>', tts.flags.SpeechVoiceSpeakFlags.IsXML.value)
voice.say('<speak version="1.0" xmlns="https://www.w3.org/2001/10/synthesis" xml:lang="en-US"><phoneme alphabet="sapi" ph="w er 1 l d"></phoneme></speak>', tts.flags.SpeechVoiceSpeakFlags.IsXML.value)
```


The SpVoice COM object is available as the `voice` variable on the instance of the Sapi class.
You can access the raw SAPI interface from it.
The interface is available at:

https://msdn.microsoft.com/en-us/library/ee125640%28v=vs.85%29.aspx

Properties are assigned and read from, Methods are used like functions.
For example, to pause a voice and then to resume it:
```
voice.voice.Pause()
voice.voice.Resume()
```

Happy Hacking
