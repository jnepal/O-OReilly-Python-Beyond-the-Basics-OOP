import abc
from datetime import datetime

class WriteFile:
    __metaclass__ = abc.ABCMeta

    def __init__(self, filename):
        self.filename = filename

    @abc.abstractmethod
    def write(self):
        return

    def write_line(self, text):
        # with will automatically run cleanup routine i.e close the file
        with open(self.filename, 'a') as file:
            file.write(text + '\n')



class DelimFile(WriteFile):
    def __init__(self, filename, delimiter):
        super().__init__(filename)
        self.delimiter = delimiter

    def write(self, list):
        line = self.delimiter.join(list)
        self.write_line(line)

class LogFile(WriteFile):

    def write(self, line):
        date = datetime.now()
        date_string = date.strftime('%Y-%m0-%d %H:%M')
        self.write_line('{0}   {1}'.format(date_string, line))

logFile = LogFile('log.txt')
delimFile = DelimFile('text.csv', ',')

logFile.write('This is a log message')
logFile.write('This is another log message')

delimFile.write(['a', 'b', 'c', 'd'])
delimFile.write(['1', '2', '3', '4'])