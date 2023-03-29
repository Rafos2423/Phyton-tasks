class SuperStr(str):
    def __init__(self, str):
        self = str

    def is_repeatance(self, string):
        if not isinstance(string, str):
            return False

        repeatTimes = len(self) / len(string)

        if repeatTimes != round(repeatTimes):
            return False

        if string * int(repeatTimes) != self:
            return False

        return True

    def is_palindrom(self):
        return self == self[::-1]