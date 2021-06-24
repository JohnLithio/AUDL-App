import webbrowser
from threading import Timer
from app.app import app


def open_browser():
    """Open the default broswer to the app's web address."""
    webbrowser.open_new("http://127.0.0.1:2000/")


if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run_server(debug=False, port=2000)
