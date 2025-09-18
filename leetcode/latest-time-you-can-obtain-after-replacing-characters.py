class Solution:
    def findLatestTime(self, s: str) -> str:
        new = ''
        if '?' in s:
            x = s.split(':')
            if '?' in x[0]:
                a = x[0]
                if a.count('?') == 1:
                    if x[0][0] == '?':
                        if x[0][1] == '1' or x[0][1] == '0':
                            new = '1'
                        else:
                            new = '0'
                    else:
                        new = new + str(x[0][0])
                    if x[0][1] == '?':
                        if x[0][0] == '1':
                            new = new + '1'
                        else:
                            new = new + '9'
                    else:
                        new = new + str(x[0][1])
                if a.count('?') == 2:
                    new = new + '11'
            else:
                new = new + str(x[0])
            new = new + ":"
            if '?' in x[1]:
                b = x[1]
                if b.count('?') == 1:
                    if x[1][0] == '?':
                        new = new + '5'
                    else:
                        new = new + str(x[1][0])
                    if x[1][1] == '?':
                        new = new + '9'
                    else:
                        new = new + str(x[1][1])
                if b.count('?') == 2:
                    new = new + '59'
            else:
                new = new + str(x[1])
            return new
        else:
            return s