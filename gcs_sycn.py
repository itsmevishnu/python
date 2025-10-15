# A simple Google Cloud Storage sync application similar to dropbox. When some modification
# (creation, deletion, updation) happens in a folder, the file will be sync with the google cloud storage
# tried to mimic the Dropbox sync feature

from watchdog.observers import  Observer
from watchdog.events import FileSystemEventHandler
from google.cloud import storage

import time

json_key = "./key.json"
sync_folder = "." # current folder

class Storage:
    def __init__(self):
        try:
            self.storage_client = storage.Client.from_service_account_json(json_key)
            self.bucket = self.storage_client.get_bucket("vj_test_report")
        except Exception as error:
            print(f"There is some error has occurred: {error}")
            raise error
    
    def upload_file(self, file_name, file_path, is_update=False):
        blob = self.bucket.blob(file_name)
        blob.upload_from_filename(file_path)
        if is_update:
            print(f"Updated the {file_name}")
        else:
            print(f"Uploaded the {file_name}")

    def delete_file(self, file_name):
        blob = self.bucket.blob(file_name)
        blob.delete()
        print(f"File removed {file_name}")

        

class MyCustomFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        file_path = event.src_path
        file_name = file_path.split("\\")[-1]
        print(f"A new file created: {file_name}")
        storage = Storage()
        storage.upload_file(file_name=file_name,
                            file_path=file_path)

    def on_deleted(self, event):
        file_path = event.src_path
        file_name = file_path.split("\\")[-1]
        print(f"A  file moved: {event.src_path}")
        storage = Storage()
        storage.delete_file(file_name)

    def on_modified(self, event):
        file_path = event.src_path
        file_name = file_path.split("\\")[-1]
        print(f"A File updated: {file_name}")
        storage = Storage()
        storage.upload_file(file_name=file_name,
                            file_path=file_path,
                            is_update=True
                            )

    def on_moved(self, event):
        self.on_deleted()




if __name__ == "__main__":
    event_handler = MyCustomFileHandler()
    observer = Observer()
    observer.schedule(event_handler, sync_folder, recursive=True)

    observer.start()

    try:
        while True:
            time.sleep(1)
    except Exception as error:
        observer.stop()
    observer.join()
