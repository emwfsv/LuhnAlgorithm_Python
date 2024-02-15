class LogHandler():
    def __init__(self, filepath):
        self.filepath = filepath

    def readFromFile(self):
        try:            
            file = open(self.filepath, "r")
            fileText =  file.read()
            return fileText
        except:
            pass

    def writeToFile(self, logText):
        try:            
            file = open(self.filepath, "a")
            file.writelines(logText + "\n")
            file.close()
        except:
            pass