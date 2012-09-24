from . import TestParent

class TestClass(TestParent):
    @property
    def exists(self):
        return True
    
def main():
    return True