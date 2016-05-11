from optparse import OptionParser
import subprocess

def autoPush(message):
    addCmd = 'git add .'
    process = subprocess.Popen(addCmd, shell = True)
    process.wait()
    commitCmd = 'git commit -m "%s"' %(message)
    process = subprocess.Popen(commitCmd, shell=True)
    process.wait()
    pushCmd = 'git push'
    process = subprocess.Popen(pushCmd, shell=True)
    process.wait()

def main():
    parser = OptionParser()
    parser.add_option("-m","--message", help="Commit Message",metavar="message")
    (options, args) = parser.parse_args()
    message = options.message
    autoPush(message)
if __name__ == '__main__':
	main()

