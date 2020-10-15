import operator as op

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

            if cmd.endswith("=") and hasattr(self.player, cmd[:-1]):
                setattr(self.player, cmd[:-1], s.pop())

            elif cmd in ops:
                s.append(ops[cmd](s.pop(), s.pop()))

            elif cmd.startswith("P:") and hasattr(
                    self.player, cmd[2:]):
                s.append(getattr(self.player, cmd[2:]))

            elif cmd == "if":
                if not s.pop():
                    while cmds and cmds[-1] != "fi":
                        cmds.pop()
                    continue

            elif cmd == "fi":
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
