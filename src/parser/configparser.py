import sys
from antlr4 import *
from antlr4.InputStream import InputStream

from HotkeyLexer import HotkeyLexer
from HotkeyParser import HotkeyParser
from HotkeyListener import HotkeyListener


class HotkeyEmitter(HotkeyListener):
    def __init__(self):
        pass
        
    def exitProject(self):
        print("exit project")
    
    def exitProject_Info(self):
        print("exit project_info")
        
    def exitMap(self):
        print("map")
        
    def exitPair(self):
        print("pair")
        
    def exitNamespace(self):
        print("namespace")
        
    def exitValue(self):
        print("value")
        
    def exitOs_Config(self):
        print("os_config")
        
    def exitHotkey(self):
        print("hotkey")

def parse(file_path):
    input   = FileStream(argv[1])
    lexer   = HotkeyLexer(input)
    stream  = CommonTokenStream(lexer)
    parser  = HotkeyParser(stream)
    tree    = parser.StartRule()
    
    
    listener = HotkeyEmitter()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
        
        
if __name__ == '__main__':
    if (len(sys.argv) > 1):
        parse(sys.argv[1])
    else:
        print("Usage:\npython configparser.py <onfig_path>")