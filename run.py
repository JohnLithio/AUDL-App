import webbrowser
from threading import Timer
from app.app import app

server = app.server


def open_browser():
    """Open the default broswer to the app's web address."""
    webbrowser.open_new("http://127.0.0.1:2000/")


# TODO: Make checking S3 optional
# TODO: Set up script to makes sure all s3 files are up to date and schedule to run weekly
# TODO: Dan's suggestions:
#       Have a clear purpose as to why I'm doing this, clear takeaways.
#           Tool for coaches to analyze teams, etc.
#       Have a predictive model. The clustering would be good too.
#           Perhaps a game score type metric (like EDGE)
#           Predict next pass or possession outcome based on more than just position
#               # of throws before, distances of throws, time left, players on field, prior game completion %, etc.
#               Could then perhaps create player metrics
if __name__ == "__main__":
    # Timer(1, open_browser).start()
    app.run_server(debug=False)
    # app.run_server(debug=False, port=2000)
