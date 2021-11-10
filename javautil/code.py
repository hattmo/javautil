from .interfaces import Const_Type
from .op_defs import op_code_lookup

class Code:
    def __init__(self):
        self.ops = list()

    def __add__(self, other):
        out = Code()
        out.ops = self.ops + other.ops
        return out

    def append(self, item):
        self.ops.append(item)

    def __getitem__(self,index):
        return self.ops[index]


class Op():
    def __init__(self, bytecode, args):
        self.args = args
        self.bytecode = bytecode
        self.offset = 0

    def set_offset(self,offset):
        self.offset = offset

    def __len__(self):
        

class Op_Code_Builder():
    def __init__(self, bytecode: bytes):
        self.bytecode = bytecode

    def __call__(self, *args):
        if not op_code_lookup[self.bytecode].check(args):
            raise ValueError("Invalid arguments for opcode")
        new_op = Op(self.bytecode,args)
        out = Code()
        out.ops.append(new_op)
        return out


class Op_Codes:
    @staticmethod
    def __dir__():
        out = super().__dir__()
        return out + ['aaload']

    @staticmethod
    def __getattr__(name):
        return Op_Code_Builer(op_code_lookup[name])
