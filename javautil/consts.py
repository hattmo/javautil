from .interfaces import Linkable, Const_Type
import struct

class Class_Info(Linkable, Const_Type):
    def __init__(self, name_index: int):
        super().__init__()
        self.name_index = name_index
        self.const_type = 7

    def __str__(self):
        leftside = f"{'#' + str(self.index):>4} - Class: #{self.name_index}"
        return f"{leftside:<40.40}// {self.resolve()}"

    def resolve(self):
        if self.const_pool == None:
            return "Unlinked"
        try:
            return self.const_pool[self.name_index - 1].resolve()
        except:
            return "Failed to resolve"

    def to_bytes(self):
        return struct.pack(">BH", 7, self.name_index)


class Fieldref_Info(Linkable, Const_Type):
    def __init__(self, class_index: int, name_and_type_index: int):
        super().__init__()
        self.class_index = class_index
        self.name_and_type_index = name_and_type_index
        self.const_type = 9

    def __str__(self):
        leftside = f"{'#' + str(self.index):>4} - Fieldref: #{self.class_index}, #{self.name_and_type_index}"
        return f"{leftside:<40.40}// {self.resolve()}"

    def resolve(self):
        if self.const_pool == None:
            return "Unlinked"
        try:
            return f'({self.const_pool[self.class_index-1].resolve()}) {self.const_pool[self.name_and_type_index-1].resolve()}'
        except:
            return "Failed to resolve"

    def to_bytes(self):
        return struct.pack(">BHH", 9, self.class_index,
                           self.name_and_type_index)


class Methodref_Info(Linkable, Const_Type):
    def __init__(self, class_index: int, name_and_type_index: int):
        super().__init__()
        self.class_index = class_index
        self.name_and_type_index = name_and_type_index
        self.const_type = 10

    def __str__(self):
        leftside = f"{'#' + str(self.index):>4} - Methodref: #{self.class_index}, #{self.name_and_type_index}"
        return f"{leftside:<40.40}// {self.resolve()}"

    def resolve(self):
        if self.const_pool == None:
            return "Unlinked"
        try:
            return f'({self.const_pool[self.class_index-1].resolve()}) {self.const_pool[self.name_and_type_index-1].resolve()}'
        except:
            return "Failed to resolve"

    def to_bytes(self):
        return struct.pack(">BHH", 10, self.class_index,
                           self.name_and_type_index)


class Interface_Methodref_Info(Linkable, Const_Type):
    def __init__(self, class_index: int, name_and_type_index: int):
        super().__init__()
        self.class_index = class_index
        self.name_and_type_index = name_and_type_index
        self.const_type = 11

    def __str__(self):
        leftside = f"{'#' + str(self.index):>4} - Interface Methodref: #{self.class_index}, #{self.name_and_type_index}"
        return f"{leftside:<40.40}// {self.resolve()}"

    def resolve(self):
        if self.const_pool == None:
            return "Unlinked"
        try:
            return f'({self.const_pool[self.class_index-1].resolve()}) {self.const_pool[self.name_and_type_index-1].resolve()}'
        except:
            return "Failed to resolve"

    def to_bytes(self):
        return struct.pack(">BHH", 11, self.class_index,
                           self.name_and_type_index)


class String_Info(Linkable, Const_Type):
    def __init__(self, string_index: int):
        super().__init__()
        self.string_index = string_index
        self.const_type = 8

    def __str__(self):
        leftside = f"{'#' + str(self.index):>4} - String: #{self.string_index}"
        return f"{leftside:<40.40}// {self.resolve()}"

    def resolve(self):
        if self.const_pool == None:
            return "Unlinked"
        try:
            return self.const_pool[self.string_index - 1].resolve()
        except:
            return "Failed to resolve"

    def to_bytes(self):
        return struct.pack(">BH", 8, self.string_index)


class Integer_Info(Linkable, Const_Type):
    def __init__(self, int_bytes: int):
        super().__init__()
        self.int_bytes = int_bytes
        self.const_type = 3

    def __str__(self):
        return f"{'#' + str(self.index):>4} - Integer: {self.int_bytes}"

    def to_bytes(self):
        return struct.pack(">BI", 3, self.int_bytes)


class Float_Info(Linkable, Const_Type):
    def __init__(self, float_bytes: float):
        super().__init__()
        self.float_bytes = float_bytes
        self.const_type = 4

    def __str__(self):
        return f"{'#' + str(self.index):>4} - Float: {self.float_bytes}"

    def to_bytes(self):
        return struct.pack(">Bf", 4, self.float_bytes)


class Long_Info(Linkable, Const_Type):
    def __init__(self, long_bytes: int):
        super().__init__()
        self.long_bytes = long_bytes
        self.const_type = 5

    def __str__(self):
        return f"{'#' + str(self.index):>4} - Long: {self.long_bytes}"

    def to_bytes(self):
        return struct.pack(">BQ", 5, self.long_bytes)


class Double_Info(Linkable, Const_Type):
    def __init__(self, double_bytes: float):
        super().__init__()
        self.double_bytes = double_bytes
        self.const_type = 6

    def __str__(self):
        return f"{'#' + str(self.index):>4} - Double: {self.double_bytes}"

    def to_bytes(self):
        return struct.pack(">Bd", 6, self.double_bytes)


class Name_And_Type_Info(Linkable, Const_Type):
    def __init__(self, name_index: int, descriptor_index: int):
        super().__init__()
        self.name_index = name_index
        self.descriptor_index = descriptor_index
        self.const_type = 12

    def __str__(self):
        leftside = f"{'#' + str(self.index):>4} - Name and Type: #{self.name_index}, #{self.descriptor_index}"
        return f"{leftside:<40.40}// {self.resolve()}"

    def resolve(self):
        if self.const_pool == None:
            return "Unlinked"
        try:
            return f"{self.const_pool[self.name_index-1].resolve()} {self.const_pool[self.descriptor_index-1].resolve()}"
        except:
            return "Failed to resolve"

    def to_bytes(self):
        return struct.pack(">BHH", 12, self.name_index, self.descriptor_index)


class Utf8(Linkable, Const_Type):
    def __init__(self, data: bytes):
        super().__init__()
        self.data = data
        self.const_type = 1

    def __str__(self):
        return f"{'#' + str(self.index):>4} - Utf8: {self.data.decode()}"

    def resolve(self):
        return self.data.decode()

    def to_bytes(self):
        return struct.pack(f">BH{len(self.data)}s", 1, len(self.data),
                           self.data)


class Method_Handle_Info(Linkable, Const_Type):
    def __init__(self, reference_kind: int, reference_index: int):
        super().__init__()
        self.reference_kind = reference_kind
        self.reference_index = reference_index
        self.const_type = 15

    def __str__(self):
        return f"{'#' + str(self.index):>4} - Method Handle: {self.reference_kind}, #{self.reference_index}"

    def to_bytes(self):
        return struct.pack(">BHH", 15, self.reference_kind,
                           self.reference_index)


class Method_Type_Info(Linkable, Const_Type):
    def __init__(self, descriptor_index: int):
        super().__init__()
        self.descriptor_index = descriptor_index
        self.const_type = 16

    def __str__(self):
        return f"{'#' + str(self.index):>4} - Method Type: #{self.descriptor_index}"

    def to_bytes(self):
        return struct.pack(">BH", 16, self.descriptor_index)


class Invoke_Dynamic_Info(Linkable, Const_Type):
    def __init__(self, bootstrap_method_attr_index: int,
                 name_and_type_index: int):
        super().__init__()
        self.bootstrap_method_attr_index = bootstrap_method_attr_index
        self.name_and_type_index = name_and_type_index
        self.const_type = 18

    def __str__(self):
        return f"{'#' + str(self.index):>4} - Invoke Dynamic: #{self.bootstrap_method_attr_index}, #{self.name_and_type_index}"

    def to_bytes(self):
        return struct.pack(">BHH", 18, self.bootstrap_method_attr_index,
                           self.name_and_type_index)