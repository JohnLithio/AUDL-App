import os
import boto3
import webbrowser
from threading import Timer
from app.app import app

server = app.server


def download_s3_folder(bucket_name, s3_folder, local_dir=None):
    """
    Download the contents of a folder directory
    Args:
        bucket_name: the name of the s3 bucket
        s3_folder: the folder path in the s3 bucket
        local_dir: a relative or absolute directory path in the local file system
    """
    s3 = boto3.resource("s3")
    bucket = s3.Bucket(bucket_name)
    for obj in bucket.objects.filter(Prefix=s3_folder):
        target = (
            obj.key
            if local_dir is None
            else os.path.join(local_dir, os.path.relpath(obj.key, s3_folder))
        )
        if not os.path.exists(os.path.dirname(target)):
            os.makedirs(os.path.dirname(target))
        if obj.key[-1] == "/":
            continue
        bucket.download_file(obj.key, target)


def open_browser():
    """Open the default broswer to the app's web address."""
    webbrowser.open_new("http://127.0.0.1:2000/")


if __name__ == "__main__":
    # Timer(1, open_browser).start()
    # download_s3_folder(
    #     "audl-heroku-data", "public/data/all_games/", "data/all_games",
    # )
    # download_s3_folder(
    #     "audl-heroku-data", "public/data/league_info/", "data/league_info",
    # )
    # s3 = boto3.client("s3")
    # s3.download_file(
    #     "audl-heroku-data", "public/data/audl.db", "data/audl.db",
    # )
    app.run_server(debug=False)
    # app.run_server(debug=False, port=2000)
