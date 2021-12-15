from pydub import AudioSegment
import time as t
import math
def time_sleep(file)
	sound = AudioSegment.from_file(file, "wav")

	time = sound.duration_seconds # 再生時間(秒)

	time = math.ceil(time) + 1
	t.sleep(time)