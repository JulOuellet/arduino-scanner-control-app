import threading
import arduino


# Classe pour lire le port serial dans le background
class SerialReaderThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self._stop_event = threading.Event()

    # Get data from port
    def run(self):
        while not self.stopped():
            print(
                "Nouveau scan effectué! Valeurs numériques mesurées (plage 0 - 255) :\n"
                + str(arduino.getScannedValues())
            )

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()
