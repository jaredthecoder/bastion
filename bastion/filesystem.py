import pickle
import os
from datetime import datetime


class FileSystem:
    CONST_FILE_SYSTEM_NAME = "file_system.p"
    open_files = []
    free_space = {}

    def __init__(self):
        self.exists = self.on_disk()
        self.total_size = 20971520  # 20 megabytes allocated for overhead
        self.fd = 0
        self.open_files = []
        self.root = Directory(None, "/")
        self.root.parent = self.root
        self.root.children = []
        self.root.add_child('..', self.root.parent)

    def initialize(self):
        """If the filesystem does not exist yet or we are
        overwriting the existing filesystem, run this function."""

        if self.on_disk():
            os.remove(self.CONST_FILE_SYSTEM_NAME)

        # Overwrite old values
        self.exists = False
        self.total_size = 20971520  # 20 megabytes allocated for overhead
        self.fd = 0
        self.open_files = []
        self.root = Directory(None, "/")
        self.root.parent = self.root
        self.root.children = []
        self.root.add_child('..', self.root.parent)

        # Dump the filesystem to disk.
        pickle.dump(self, open(self.CONST_FILE_SYSTEM_NAME, "wb"))

    def on_disk(self):
        if os.path.isfile(self.CONST_FILE_SYSTEM_NAME):
            return True
        else:
            return False

    def get_new_fd(self):
        current_fd = self.fd
        self.fd += 1
        return current_fd

    def get_open_file(self, fd):
        for file in self.open_files:
            if str(fd) == str(file[0]):
                return file[2]

    def get_free_space(size):
        """
            Return where space starts, return None otherwise
        """
        pass

    def write_to_disk(offset, content):
        """
            Write content (bytes) to offset, will always be enough room
        """
        pass

    def free_space(offset, size):
        """
            Go to offset and delete up to size
        """
        pass

class Directory:
    def __init__(self, parent, name):
        self.name = name
        self.parent = parent
        self.children = []
        self.add_child('..', parent)

    def add_child(self, name, child):
        self.children.append((name, child))

    def find_child(self, name):
        for child in self.children:
            if name == child[0]:
                return child[1]


class File:
    def __init__(self, parent, name, fd):
        self.name = name
        self.parent = parent
        self.fd = fd
        self.size = 4096
        self.content = ''
        self.offset = 0
        self.date = str(datetime.now())
