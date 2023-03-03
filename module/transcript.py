import whisper
import os
from typing import Iterator, TextIO
from googletrans import Translator


class Transcript:

    def transcribe(self, file,language):
        model = whisper.load_model("large")
        result = model.transcribe(file, verbose=False)
        with open(f"{os.path.splitext(file)[0]}-en.text", "w", encoding="utf-8") as f:
            f.write(result["text"])
            f.close()
        with open(f"{os.path.splitext(file)[0]}-{language}.srt", "w", encoding="utf-8") as srt:
            self.write_srt(result["segments"], file=srt, language=language)

    def srt_format_timestamp(self, seconds: float):
        assert seconds >= 0, "non-negative timestamp expected"
        milliseconds = round(seconds * 1000.0)

        hours = milliseconds // 3_600_000
        milliseconds -= hours * 3_600_000

        minutes = milliseconds // 60_000
        milliseconds -= minutes * 60_000

        seconds = milliseconds // 1_000
        milliseconds -= seconds * 1_000

        return (f"{hours}:") + f"{minutes:02d}:{seconds:02d},{milliseconds:03d}"

    def write_srt(self, transcript: Iterator[dict], file: TextIO, language):
        count = 0
        for segment in transcript:
            count += 1
            tranlator = Translator()
            segment['text'] = tranlator.translate(
                segment['text'], dest=language).text
            print(
                f"{count}\n"
                f"{self.srt_format_timestamp(segment['start'])} --> {self.srt_format_timestamp(segment['end'])}\n"
                f"{segment['text'].replace('-->', '->').strip()}\n",
                file=file,
                flush=True,
            )
