
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

#api_key = "AIzaSyBVoJn-b_rSBUNjxjKk_mrGqufGE9LgzLs"



#data, sr = utl.read_wav("Enough!!.wav")
#utils.plot_sound("data",data.shape[1],data.shape[0]/sr,data)


# main.py
import sys
from PyQt5.QtWidgets import QApplication
from GUI import AudioPlayer

def main():
    app = QApplication(sys.argv)
    player = AudioPlayer()
    player.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
