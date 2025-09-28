class Solution:
    def interpret(self, command: str) -> str:
        final = ''
        i = 0
        while i<len(command):
            if command[i] == 'G':
                final += 'G'
                i += 1
            elif command[i] == '(' and command[i+1] == ')':
                final += 'o'
                i+=2
            elif command[i] == '(' and command[i+1] == 'a':
                final += 'al'
                i+=4
        return final