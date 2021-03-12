# Qlink - https://leetcode.com/problems/robot-bounded-in-circle/

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = {
            'N':('W','E'),
            'W':('S','N'),
            'S':('E','W'),
            'E':('N','S')            
        }
        
        positions = {
            'N':(0,1),
            'W':(-1,0),
            'S':(0,-1),
            'E':(1,0)            
        }
        #initial conditions
        x=0
        y=0
        direct='N'
        
        for cmd in instructions:
            if cmd == 'G':
                x += positions[direct][0]
                y += positions[direct][1]
            
            elif cmd == 'L':
                direct = directions[direct][0]
            
            elif cmd == 'R':
                direct = directions[direct][1]
        
        return (x==0 and y==0) or direct!='N'
