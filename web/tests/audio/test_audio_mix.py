from pydub import AudioSegment


def test_audio_mix():
    sound1 = AudioSegment.from_wav("../../alarm/alarm-1002.wav")
    sound2 = AudioSegment.from_wav("../../alarm/alarm-1004.wav")
    sound3 = AudioSegment.from_wav("../../alarm/the-morning-2462.wav")

    output = sound1.overlay(sound2, position=10)
    output = output.overlay(sound3, position=10)

    output.export("../../alarm/mixed_alarm.wav", format="wav")
