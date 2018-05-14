import time
from os import walk
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for (dirpath, dirnames, filenames) in walk("C:/Users/Darek/Desktop/test"):
            path2.extend(filenames)
        file = list(set(path2) - set(path1))
        print(file)


path1 = []
path2 = []
for (dirpath, dirnames, filenames) in walk("C:/Users/Darek/Desktop/test"):
    path1.extend(filenames)
    if __name__ == "__main__":
        event_handler = MyHandler()
        observer = Observer()
        observer.schedule(event_handler, path='C:/Users/Darek/Desktop/test', recursive=False)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
    path1 = path2

