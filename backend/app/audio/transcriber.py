from faster_whisper import WhisperModel

model = WhisperModel("base")

def transcribe(audio_path):

    segments, info = model.transcribe(audio_path)

    full_text = ""

    for segment in segments:
        full_text += segment.text + " "

    return full_text