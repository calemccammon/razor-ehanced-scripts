from System.Collections.Generic import List
from System import Byte, Int32

class Direction:
    def __init__(self, gumpInt):
        self.gumpInt = gumpInt
    
    def go(self):
        Misc.Pause(500)
        Gumps.SendAction(10000, self.gumpInt)
        Misc.Pause(500)
        
    def isCorrect(self):
        return not Journal.Search("fail to disarm")
        
kit = 0x45FD0C42
up = Direction(1)
right = Direction(2)
down = Direction(3)
left = Direction(4)

solutionOne = [right, right, down, down]
solutionTwo = [right, down, right, down]
solutionThree = [right, down, down, right]
solutionFour = [right, down, left, down, right, right]
solutionFive = [right, right, down, left, down, right]
solutionSix = [right, right, down, left, left, down, right, right]

solutionSeven = [down, down, right, right]
solutionEight = [down, right, down, right]
solutionNine = [down, right, right, down]
solutionTen = [down, right, up, right, down, down]
solutionEleven = [down, down, right, up, right, down]
solutionTwelve = [down, down, right, up, up, right, down, down]

allSolutions = [solutionOne, solutionTwo, solutionThree, solutionFour, solutionFive,
    solutionSix, solutionSeven, solutionEight, solutionNine, solutionTen, solutionEleven, solutionTwelve]
    
def doSteps(solution):
    for direction in solution:
        direction.go()
        if not direction.isCorrect():
            Journal.Clear()
            openKit()
            break
    
def openKit():
    Misc.Pause(8000)
    Player.UseSkill("Remove Trap")
    Target.WaitForTarget(2000, False)
    Target.TargetExecute(0x45FD0C42)
    Gumps.WaitForGump(10000, 2000)

Journal.Clear()
for solution in allSolutions:
    index = allSolutions.index(solution)
    Misc.SendMessage("Starting solution " + str(index))
    openKit()
    doSteps(solution)
    if Journal.Search("successfully disarm"):
        break