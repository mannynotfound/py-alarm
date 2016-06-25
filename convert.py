import sys
from pydub import AudioSegment

inp = sys.argv[1]
out = sys.argv[2]

sound = AudioSegment.from_mp3(inp)
sound.export(out, format="wav")
