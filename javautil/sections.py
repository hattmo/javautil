from .interfaces import Linkable
import struct

class Attribute_Info(Linkable):
    def __init__(self, attribute_name_index: int, info: bytes):
        super().__init__()
        self.attribute_name_index = attribute_name_index
        self.info = info

    def __str__():
        return ""

    def to_bytes(self):
        return struct.pack(f">HL{len(self.info)}s", self.attribute_name_index,
                           len(self.info), self.info)


class Field_Info(Linkable):
    def __init__(self, access_flags: int, name_index: int,
                 descriptor_index: int):
        super().__init__()
        self.access_flags = access_flags
        self.name_index = name_index
        self.descriptor_index = descriptor_index
        self.attributes = list()

    def link(self, const_pool):
        super().link(const_pool)
        for i in self.attributes:
            i.link(const_pool)

    def add_attribute_raw(self, attribute_info):
        if self.const_pool != None:
            attribute_info.link(self.const_pool)
        self.attributes.append(attribute_info)

    def __str__(self):
        out = f"access flags: {self.access_flags}\n"
        out += f"name: {self.const_pool[self.name_index-1].resolve()}\n"
        out += f"descriptor: {self.const_pool[self.descriptor_index-1].resolve()}\n"
        out += f"attributes: {len(self.attributes)}"
        return out

    def to_bytes(self):
        out = struct.pack(">HHHH", self.access_flags, self.name_index,
                          self.descriptor_index, len(self.attributes))
        for attr in self.attributes:
            out += attr.to_bytes()
        return out


class Method_Info(Linkable):
    def __init__(self, access_flags: int, name_index: int,
                 descriptor_index: int):
        super().__init__()
        self.access_flags = access_flags
        self.name_index = name_index
        self.descriptor_index = descriptor_index
        self.attributes = list()

    def link(self, const_pool):
        super().link(const_pool)
        for i in self.attributes:
            i.link(const_pool)

    def add_attribute_raw(self, attribute_info):
        if self.const_pool != None:
            attribute_info.link(self.const_pool)
        self.attributes.append(attribute_info)

    def __str__(self):
        out = f"access flags: {self.access_flags}\n"
        out += f"name: {self.const_pool[self.name_index-1].resolve()}\n"
        out += f"descriptor: {self.const_pool[self.descriptor_index-1].resolve()}\n"
        out += f"attributes: {len(self.attributes)}"
        return out

    def to_bytes(self):
        out = struct.pack(">HHHH", self.access_flags, self.name_index,
                          self.descriptor_index, len(self.attributes))
        for attr in self.attributes:
            out += attr.to_bytes()
        return out