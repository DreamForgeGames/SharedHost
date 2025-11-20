from PyQt6.QtWidgets import QApplication
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
import sys
import threading
from server import app as flask_app

class Browser(QWebEngineView):
    def __init__(self, url, default_title="Mein Browser"):
        super().__init__()
        self.default_title = default_title
        self.setWindowTitle(self.default_title)  # Standardtitel setzen
        self.load(QUrl(url))
        # Signal, das feuert, wenn sich der Seitentitel ändert
        self.titleChanged.connect(self.update_title)

    def update_title(self, title):
        # Falls der Titel leer ist, Standardtitel verwenden
        if title:
            self.setWindowTitle(title)
        else:
            self.setWindowTitle(self.default_title)


def run():
    # Create Flask server thread
    def run_flask():
        flask_app.run(debug=False, port=1787, use_reloader=False, threaded=True)
    
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    
    # Create and run PyQt application in main thread
    app = QApplication(sys.argv)
    browser = Browser("http://localhost:1787", default_title="SharedHost - Easily Play Together!")
    browser.resize(800, 600)
    browser.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run()