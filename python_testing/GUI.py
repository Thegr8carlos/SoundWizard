import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl

class Controler(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: purple;")
        
        # Crear botones
        self.load_button = QPushButton("Load Audio", self)
        self.play_button = QPushButton("Play Audio", self)
        self.stop_button = QPushButton("Stop Audio", self)

        # Crear layout y agregar botones
        layout = QVBoxLayout()
        layout.addWidget(self.load_button)
        layout.addWidget(self.play_button)
        layout.addWidget(self.stop_button)
        
        self.setLayout(layout)

class AudioPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Audio Player with PyQt5")
        self.setGeometry(100, 100, 1200, 900)
        
        # Crear reproductor de audio
        self.player = QMediaPlayer(self)
        
        # Crear instancia de Controler y establecerla como el widget central
        self.controler = Controler(self)
        self.setCentralWidget(self.controler)
        
        # Conectar señales de los botones a las funciones correspondientes
        self.controler.load_button.clicked.connect(self.load_audio)
        self.controler.play_button.clicked.connect(self.play_audio)
        self.controler.stop_button.clicked.connect(self.stop_audio)

    def load_audio(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Load Audio File", "", "Audio Files (*.wav);;All Files (*)", options=options)
        if file_path:
            audio_url = QUrl.fromLocalFile(file_path)
            self.player.setMedia(QMediaContent(audio_url))
            self.setWindowTitle(f"Audio Player - {file_path}")

    def play_audio(self):
        self.player.play()

    def stop_audio(self):
        self.player.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = AudioPlayer()
    player.show()
    sys.exit(app.exec_())
