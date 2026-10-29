# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

class Record:
    def status(self, percent):
        return percent

r = Record()
print(r.status(95))
