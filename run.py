import webbrowser
from threading import Timer
from app.app import app

server = app.server


def open_browser():
    """Open the default broswer to the app's web address."""
    webbrowser.open_new("http://127.0.0.1:2000/")


# TODO: Pre-process as much data as possible and store on s3
#       Player names
#       Game info
#       Teams
# TODO: Put s3 download as 2nd highest priority, ahead of scrape, below local
# TODO: Set up script to makes sure all s3 files are up to date and schedule to run weekly
if __name__ == "__main__":
    # Timer(1, open_browser).start()
    app.run_server(debug=False)
    # app.run_server(debug=False, port=2000)
