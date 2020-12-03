"""
so this got a little crazy

i wrote a micro language to handle the state updates,
so i can pass the code blocks around in the way i wanted

it works like this, theres a list of conditions to determine when
to change state, and some code to initialize the state

then theres also a code block for each state as an update function

conditionals are a lambda function

initstates = [ 
  [conditional, code block],
  [conditional, code block],
 ... ]

applystates = {
    "state name" : code block,
    "state name" : code block,
    ... }

the code blocks function in a stack based interpreter
code is split on whitespace and a stack is created

cmds = code.split(); s = []
while cmds: 
    cmd = code.pop()
    ... do stuff


words are evaluated right to left, if a token can be evaluated as 
an int or a float, then the number is put on the stack, otherwise
the string is put on the stack.

keywords and oporators pop arguments off the stack,
so if you mess up your syntax youll get indexErrors
--------- KEYWORDS
.  : prints next item on the stack

dup : duplicate top of the stack

example: + dup P:x
same as + P:x P:x

swap : swap the next two items on the stack

example: . . swap 2 1
will print 1 then 2

eat : gobbles the next item on the stack

example: . eat 2 1
will print 1 

--------- OPORATORS
oporations function in polish notation

example: + 1 1
will evaluate as 2

example: + 3 - 6 2
will evaluate as 7

example: - + 3 2 4
will evaluate as 1 
think of it as (- (+ 3 2) 4)

---------- PLAYER ATTRIBUTES
any word starting with P: will be evaluated as the players attribute

any word ending with = will be an assignment to the players attribute

example: "== P:state walk"
this will evaluate as true if the players state is "walk"

example: "state= walk"
this will set the players state to walk

example: "x= + P:x 1"
this is equivalent to "player.x += 1"

--------- IF 
if statements pass if the last item on the stack is true,
otherwise they eat code untill they reach the corrisponding fi

nested if's are a thing

example: fi x= + P:x 1 if P:MOV_RIGHT
equivalent to "if player.MOV_RIGHT: player.x += 1"

example: fi fi x- + P:x 1 if P:MOV_RIGHT if == P:state walk
equivalent to
if player.state == "walk":
    if player.MOV_RIGHT:
        player.x += 1

for an if else logic use dup and not

example: fi ___ if not fi ___ if dup == 1 1

---------- PYTHON OBJECTS

access attributes on the stack with the ":" character

:x P:nearest_player
player object gets put on the stack, then index the attribute "x"

use "call" to call the next item on the stack as a function
and put the return value on the stack (including NoneType)

"""

import operator as op
from random import randint

ops = {
    "+"  : op.add,
    "-"  : op.sub,
    "*"  : op.mul,
    "/"  : op.floordiv,
    "%"  : op.mod,
    "==" : op.eq,
    "!=" : op.ne,
    "<"  : op.lt,
    "<=" : op.le,
    ">"  : op.gt,
    ">=" : op.ge,

    "and": op.and_,
    "or" : op.or_,

    "RAND": randint,
}

class StateHandler(object):
    def __init__(self, player_object,
                 initstates=[], applystates={}):
        self.initstates = initstates
        self.applystates = applystates

        self.player = player_object

    def update_states(self):
        for cond, code in self.initstates:
            if cond(self.player):
                self.resolve(code)

    def apply_states(self):
        if self.player.state in self.applystates:
            self.resolve(self.applystates[self.player.state])

    def resolve(self, code):
        s = []
        cmds = code.split()
        while cmds:
            cmd = cmds.pop()
            # print(cmd, s)
            if cmd.endswith("=") and hasattr(self.player, cmd[:-1]):
                setattr(self.player, cmd[:-1], s.pop())

            elif cmd in ops:
                s.append(ops[cmd](s.pop(), s.pop()))

            elif cmd == "not": s.append(not s.pop())
            elif cmd == "abs": s.append(abs(s.pop()))
                
            elif cmd.startswith("P:") and hasattr(
                    self.player, cmd[2:]):
                s.append(getattr(self.player, cmd[2:]))

            elif cmd.startswith(":"):
                s.append(getattr(s.pop(), cmd[1:]))

            elif cmd == "call": s.append(s.pop()())
                
            elif cmd == "dup": s.append(s[-1])
            elif cmd == "swap": s.append(s.pop(-2))
            elif cmd == "eat": s.pop()
            elif cmd == ".": print(s.pop())

            elif cmd == "*/":
                token = None
                while cmds and token != "/*":
                    token = cmds.pop()
                
            
            elif cmd == "if":
                if not s.pop():
                    nest = 1
                    while cmds and nest > 0:
                        token = cmds.pop()
                        if token == "if": nest += 1
                        if token == "fi": nest -= 1
                    continue

            elif cmd in ["fi", "/*"]:
                continue
            
            else:
                try:
                    s.append( int(cmd) )
                    continue
                except ValueError:
                    try:
                        s.append( float(cmd) )
                        continue
                    except ValueError:
                        s.append( cmd )

if __name__ == """__main__""":
    sh = StateHandler(object(), [], {})
    while True:
        cmds = input("> ")
        if cmds == "quit": quit()
        sh.resolve(cmds)
