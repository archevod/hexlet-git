import os
from datetime import datetime, date, time


h = datetime.now().timetuple()

os.system('/usr/bin/aplay /home/archer/.local/share/sounds/clock/{}.wav'.format(h[3]))
