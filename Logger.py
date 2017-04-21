import time
import os

class Logger:
    def __init__(self):
        self.name = 'Logger'
        self.init_time = time.strftime('%m-%d-%y (%H;%M;%S)')
        self.cwd = os.getcwd()
        self.filename = self.cwd + '/logs/ExplodingKittens Log ' + self.init_time + '.html'

    # initialize the html file to hold the events
    def initialize(self):
        if not os.path.exists('%s/logs/' % self.cwd):
            os.makedirs('%s/logs/' % self.cwd)
        self.file = open(self.filename, 'w')
        css = '''<style>
        h1 {
            font-size: 40px;
        }
        h2 {
            font-size: 30px;
        }
        p {
            font-size: 12px;
        }
        </style>'''
        self.file.write(css)
        self.file.write('<h1>Exploding Kittens Log</h1>\n')
        self.file.write('<h2>%s</2>\n' % self.init_time)
        self.log('Initialized log..')

    # adds a new event to the log
    def log(self, event):
        self.file.write('<p>' + event + '</p>')

    # closes the log file, to be used when the program is closed
    def close(self):
        self.log('Closing..')
        self.file.close()


