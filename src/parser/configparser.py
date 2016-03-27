import sys
from antlr4 import *
from antlr4.InputStream import InputStream

from HotkeyLexer import HotkeyLexer
from HotkeyParser import HotkeyParser
from HotkeyListener import HotkeyListener

#The data classes that the parser is populating!
from data.configuration import Configuration
from data.projectinfo import ProjectInfo
from data.osconfig import OsConfig


class HotkeyEmitter(HotkeyListener):
    def __init__(self):
        self.configuration  = configuration.Configuration()
        self.dictionaries   = {}
        self.values         = {}
        self.current_os     = None
        
    def exitString(self, ctx:HotkeyParser.StringContext):
        """
        Denotes the entry of a value context of type string.
        """
        self.values[ctx] = ctx.getText()

    def exitAtom(self, ctx:HotkeyParser.AtomContext):
        """
        Denotes the entry of a value context of any type other than the string type.
        """
        self.values[ctx] = ctx.getText().strip('"')
        
    def enterAnObject(self, ctx:HotkeyParser.AnObjectContext):
        """
        Denotes the entry of a non-empty dictionary context.
        """
        dict = {}
        for pair_ctx in ctx.pair():
             
            
    def enterOs_config(self, ctx:HotkeyParser.Os_configContext):
        
    
    def enterEmptyObject(self, ctx:HotkeyParser.EmptyObjectContext):
        """
        Denotes the entry of an empty dictionary context.
        """
        self.dictionaries[ctx] = {}
        
    def exitProject(self, ctx : HotkeyParser.ProjectContext):
        #First we need to populate the ProjectInfo class with the header information of the project.
        project_info        = ProjectInfo(proj_name)
        
        #Hotkey.g4 forces exactly 1 project_info for each config file!
        proj_info_ctx       = ctx.project_info()[0]:
        
        proj_name           = proj_info_ctx.NAME().getText()
        project_info.name   = proj_name
        
        info_ctx            = proj_info_ctx.dictionary()
        project_info.info   = self.dictionaries[info_ctx]
        
        self.configuration.project_info = project_info
        
        
        #Then we need to loop through all of the os_config contexts and create all of those objects.
        
        
            
        
        
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