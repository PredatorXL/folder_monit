import time
from os import walk
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from win10toast import ToastNotifier

list1 = []
list2 = []
file = []
path = "C:/Users/Darek/Desktop/test"
notification = ToastNotifier()

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for (dirpath, dirnames, filenames) in walk(path):

            # definiujemy list2
            list2.extend(filenames)

            # wprowadzamy zmienną file, która jest różnicą list1 i list2
            file = list(set(list2) - set(list1))

            for new_element in file:
                # Dla każdego nowego elementu listy, dodajemy ten element do list1
                list1.append(new_element)
                # oraz printujemy ten element
                print(new_element)
                # pokazujemy powiadomienie
                notification.show_toast(f'W folderze pojawił się nowy plik: {new_element}',
                                        'Zajebiście, że działa',
                                        icon_path="custom.ico",
                                        duration=8)





for (dirpath, dirnames, filenames) in walk(path):

    # Definiujemy zawartość początkową list1
    list1.extend(filenames)

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


