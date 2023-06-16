import sys 
import time 
import os
import random 
import shutil 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = " C:\Users\DELL\Desktop\delete 1 "
to_dir = " D:\Users\DELL "

class FileEventHandler(FileSystemEventHandler):
    
    def on_created(self, event):
        print(f"hey, {event.src_path} has been created!")
        
    def on_deleted(self, event):
        print(f"Oops! someone deleted {event.src_path}!")
        
    
    def on_modified(self, event):
        print(f"hii, someone modified {event.src_path}!")
    
    def on_moved(self, event):
        print(f"hello, {event.src_path} has been moved!")
    
    
event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()
    
        