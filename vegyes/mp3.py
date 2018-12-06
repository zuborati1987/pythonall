import subprocess

def play_mp3(path):
    proc1 = subprocess.Popen(['mpg321', '-q', path]).wait()
#play_mp3("/home/rohstoff/pythonexercises/ff7.mp3")
play_mp3("/home/rohstoff/pythonexercises/tds.mp3")

    