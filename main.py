import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QVBoxLayout,
                             QHBoxLayout, QLabel, QPushButton)
from PyQt5.QtCore import Qt, QTime, QTimer

class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.watch_label = QLabel("00:00:00.00",self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Pause", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.iniUI()

    def iniUI(self):
        self.setWindowTitle("Stop Watch")
        self.setGeometry(600, 400, 800, 300)

        vbox = QVBoxLayout()
        vbox.addWidget(self.watch_label)
        self.setLayout(vbox)
        self.watch_label.setAlignment(Qt.AlignCenter)
        self.watch_label.setGeometry(0, 0, 50, 100)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addLayout(hbox)

        self.setStyleSheet("""
                    QPushButton, QLabel{
                        font-weight: bold;
                        padding: 20px;
                        font-family: calibri;
                    }

                    QPushButton{
                        font-size: 50px;
                        background-color: #cad7d9;
                    }

                    QLabel{
                        font-size: 120px;
                        background-color: #00e1ff;
                    }
                """)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.watch_label.setText(self.format_time(self.time))

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}:{milliseconds:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.watch_label.setText(self.format_time(self.time))

def main():
    app = QApplication(sys.argv)
    watch = StopWatch()
    watch.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()