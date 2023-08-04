"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #18 - Talking Clock (talkingclock.py)


Author: Andrew Scott White

Difficulty Level: 8/10

Prompt: I don’t want to be late for the BWSI Grand Prix, so I want
to program my phone to update me on the time. Can you help me make 
a Talking Clock? I need a script that takes an input 24-hour time 
(00:00 - 23:59) and translates it into words. Please format the input 
as ‘##:##’ and include am/pm in the output string. Thanks!

Test Cases:
Input: 12:00  Output: It's twelve pm

Input: 23:59  Output: It's eleven fifty nine pm

Input: 12:05  Output: It's twelve oh five pm
"""




    # This will convert military hours to regular hours, and determine AM vs PM
class Solution:    
    def ClockTalker(self, input_time):
            #type input_time: string
            #return type: string
            hour = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"one", 14:"two", 15:"three", 16:"four", 17:"five", 18:"six", 19:"seven", 20:"eight", 21:"nine", 22:"ten", 23:"eleven", 00:"twelve"}
            min = {10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen", 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty"}

            h = int(input_time[0:1])
            tm = int(input_time[3:4])
            m = int(input_time[4])

            if h >= 12:
                if input_time[3] == "0" and input_time[4] == "0":
                    return f"It's {hour[h]} pm"
                elif input_time[3] == "0" and input_time[4] != "0":
                    return f"It's {hour[h]} oh {hour[m]} pm"
                elif input_time[3] == "1":
                    return f"It's {hour[h]} {min[tm]} pm"
                elif input_time[3] == "2" or "3" or "4" or "5":
                    return f"It's {hour[h]} {min[tm]} {hour[m]} pm"
            else:
                if input_time[3] == "0" and input_time[4] == "0":
                    return f"It's {hour[h]} am"
                elif input_time[3] == "0" and input_time[4] != "0":
                    return f"It's {hour[h]} oh {hour[m]} am"
                elif input_time[3] == "1":
                    return f"It's {hour[h]} {min[tm]} am"
                elif input_time[3] == "2" or "3" or "4" or "5":
                    return f"It's {hour[h]} {min[tm]} {hour[m]} am"


def main():
     str1=input()
     tc1= Solution()
     ans=tc1.ClockTalker(str1)
     print(ans)
    
if __name__ == '__main__': 
    main()
        