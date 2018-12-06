import subprocess

proc1 = subprocess.Popen(['mpg321', '-q', "tds.mp3"])
#play_mp3("/home/rohstoff/pythonexercises/ff7.mp3")
#play_mp3("/home/rohstoff/pythonexercises/tds.mp3")
g = input("Waiting: ")
proc1.kill()