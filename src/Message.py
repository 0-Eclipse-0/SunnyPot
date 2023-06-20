# Message handler
class Message:
    def log(content):
        print("[\033[38;5;136mSunnyPot\033[00m]", content)

    def error(content):
        exit("[\033[38;5;226mError\033[00m] " + str(content))

    def abort(content):
        exit("[\033[38;5;160mAbort\033[00m] " + str(content))

    def intrusion(content):
        print("[\033[38;5;88mIntrusion\033[00m] " + str(content))