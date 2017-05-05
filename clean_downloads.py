from os import listdir, path, remove
import datetime
import shutil

def cleanup(folder,cutoffdays, removeFiles):
    filenames = listdir(folder)
    for file in filenames:
        filePath = folder + "\\" + file
        fileTime = datetime.datetime.fromtimestamp(path.getmtime(filePath))
        now = datetime.datetime.now() - datetime.timedelta(days=cutoffdays)
        if fileTime<now:
            print(filePath)
            if removeFiles:
                try:
                    remove(filePath)
                    print("file removed: " + filePath)
                except OSError:
                    shutil.rmtree(filePath)
                    print("folder removed: " + filePath)

if __name__ == "__main__":
    folder = r"C:\Users\ericl\Downloads"
    cleanup(folder, 60, True)