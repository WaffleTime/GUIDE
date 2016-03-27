import sys
from antlr4 import *
from antlr4.InputStream import InputStream

from HotkeyLexer import HotkeyLexer
from HotkeyParser import HotkeyParser
from HotkeyListener import HotkeyListener

#The data classes that the parser is populating!
import data.configuration
import data.projectinfo
import data.osconfig


class HotkeyEmitter(HotkeyListener):
    def __init__(self):
        self.configuration = configuration.Configuration()
        
    def exitProject(self, ctx : HotkeyParser.ProjectContext):
        #Hotkey.g4 forces exactly 1 project_info for each config file!
        ctx.project_info()[0]:
        
        for os_config in ctx.os_config():
            
        
        
    def exitOs_config(self, ctx : HotkeyParser.Os_configContext):
        print("os_config")
        
    def exitNamespace(self, ctx : HotkeyParser.NamespaceContext):
        print("namespace")
        
    def exitHotkey(self, ctx : HotkeyParser.HotkeyContext):
        print("hotkey")

def parse(file_path):
    input   = FileStream(file_path)
    lexer   = HotkeyLexer(input)
    stream  = CommonTokenStream(lexer)
    parser  = HotkeyParser(stream)
    tree    = parser.project()
    
    
    listener = HotkeyEmitter()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
        
        
if __name__ == '__main__':
    if (len(sys.argv) > 1):
        parse(sys.argv[1])
    else:
        print("Usage:\npython configparser.py <onfig_path>")