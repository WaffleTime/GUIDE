# Generated from ../../src/parser/Hotkey.g4 by ANTLR 4.5.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .HotkeyParser import HotkeyParser
else:
    from HotkeyParser import HotkeyParser

# This class defines a complete listener for a parse tree produced by HotkeyParser.
class HotkeyListener(ParseTreeListener):

    # Enter a parse tree produced by HotkeyParser#project.
    def enterProject(self, ctx:HotkeyParser.ProjectContext):
        pass

    # Exit a parse tree produced by HotkeyParser#project.
    def exitProject(self, ctx:HotkeyParser.ProjectContext):
        pass


    # Enter a parse tree produced by HotkeyParser#project_info.
    def enterProject_info(self, ctx:HotkeyParser.Project_infoContext):
        pass

    # Exit a parse tree produced by HotkeyParser#project_info.
    def exitProject_info(self, ctx:HotkeyParser.Project_infoContext):
        pass


    # Enter a parse tree produced by HotkeyParser#AnObject.
    def enterAnObject(self, ctx:HotkeyParser.AnObjectContext):
        pass

    # Exit a parse tree produced by HotkeyParser#AnObject.
    def exitAnObject(self, ctx:HotkeyParser.AnObjectContext):
        pass


    # Enter a parse tree produced by HotkeyParser#EmptyObject.
    def enterEmptyObject(self, ctx:HotkeyParser.EmptyObjectContext):
        pass

    # Exit a parse tree produced by HotkeyParser#EmptyObject.
    def exitEmptyObject(self, ctx:HotkeyParser.EmptyObjectContext):
        pass


    # Enter a parse tree produced by HotkeyParser#pair.
    def enterPair(self, ctx:HotkeyParser.PairContext):
        pass

    # Exit a parse tree produced by HotkeyParser#pair.
    def exitPair(self, ctx:HotkeyParser.PairContext):
        pass


    # Enter a parse tree produced by HotkeyParser#String.
    def enterString(self, ctx:HotkeyParser.StringContext):
        pass

    # Exit a parse tree produced by HotkeyParser#String.
    def exitString(self, ctx:HotkeyParser.StringContext):
        pass


    # Enter a parse tree produced by HotkeyParser#Atom.
    def enterAtom(self, ctx:HotkeyParser.AtomContext):
        pass

    # Exit a parse tree produced by HotkeyParser#Atom.
    def exitAtom(self, ctx:HotkeyParser.AtomContext):
        pass


    # Enter a parse tree produced by HotkeyParser#os_config.
    def enterOs_config(self, ctx:HotkeyParser.Os_configContext):
        pass

    # Exit a parse tree produced by HotkeyParser#os_config.
    def exitOs_config(self, ctx:HotkeyParser.Os_configContext):
        pass


    # Enter a parse tree produced by HotkeyParser#namespace.
    def enterNamespace(self, ctx:HotkeyParser.NamespaceContext):
        pass

    # Exit a parse tree produced by HotkeyParser#namespace.
    def exitNamespace(self, ctx:HotkeyParser.NamespaceContext):
        pass


    # Enter a parse tree produced by HotkeyParser#hotkey.
    def enterHotkey(self, ctx:HotkeyParser.HotkeyContext):
        pass

    # Exit a parse tree produced by HotkeyParser#hotkey.
    def exitHotkey(self, ctx:HotkeyParser.HotkeyContext):
        pass


    # Enter a parse tree produced by HotkeyParser#sequence_condition.
    def enterSequence_condition(self, ctx:HotkeyParser.Sequence_conditionContext):
        pass

    # Exit a parse tree produced by HotkeyParser#sequence_condition.
    def exitSequence_condition(self, ctx:HotkeyParser.Sequence_conditionContext):
        pass


    # Enter a parse tree produced by HotkeyParser#simultaneous_condition.
    def enterSimultaneous_condition(self, ctx:HotkeyParser.Simultaneous_conditionContext):
        pass

    # Exit a parse tree produced by HotkeyParser#simultaneous_condition.
    def exitSimultaneous_condition(self, ctx:HotkeyParser.Simultaneous_conditionContext):
        pass


