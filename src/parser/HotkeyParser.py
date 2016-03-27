# Generated from ../../src/parser/Hotkey.g4 by ANTLR 4.5.2
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\24")
        buf.write("\\\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\7\2\31\n\2\f\2")
        buf.write("\16\2\34\13\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\7\4%\n\4\f\4")
        buf.write("\16\4(\13\4\3\4\3\4\3\4\5\4-\n\4\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\5\68\n\6\3\7\3\7\3\7\7\7=\n\7\f\7\16\7")
        buf.write("@\13\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\5\tL\n")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\2\2\f\2\4\6\b\n\f\16\20\22\24\2\2[\2\26")
        buf.write("\3\2\2\2\4\35\3\2\2\2\6,\3\2\2\2\b.\3\2\2\2\n\67\3\2\2")
        buf.write("\2\f9\3\2\2\2\16C\3\2\2\2\20G\3\2\2\2\22O\3\2\2\2\24U")
        buf.write("\3\2\2\2\26\32\5\4\3\2\27\31\5\f\7\2\30\27\3\2\2\2\31")
        buf.write("\34\3\2\2\2\32\30\3\2\2\2\32\33\3\2\2\2\33\3\3\2\2\2\34")
        buf.write("\32\3\2\2\2\35\36\7\3\2\2\36\37\7\21\2\2\37 \5\6\4\2 ")
        buf.write("\5\3\2\2\2!&\5\b\5\2\"#\7\4\2\2#%\5\b\5\2$\"\3\2\2\2%")
        buf.write("(\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\')\3\2\2\2(&\3\2\2\2)*")
        buf.write("\7\5\2\2*-\3\2\2\2+-\7\5\2\2,!\3\2\2\2,+\3\2\2\2-\7\3")
        buf.write("\2\2\2./\7\22\2\2/\60\7\17\2\2\60\61\5\n\6\2\61\t\3\2")
        buf.write("\2\2\628\7\22\2\2\638\7\23\2\2\648\7\6\2\2\658\7\7\2\2")
        buf.write("\668\7\b\2\2\67\62\3\2\2\2\67\63\3\2\2\2\67\64\3\2\2\2")
        buf.write("\67\65\3\2\2\2\67\66\3\2\2\28\13\3\2\2\29>\7\20\2\2:=")
        buf.write("\5\16\b\2;=\5\20\t\2<:\3\2\2\2<;\3\2\2\2=@\3\2\2\2><\3")
        buf.write("\2\2\2>?\3\2\2\2?A\3\2\2\2@>\3\2\2\2AB\7\5\2\2B\r\3\2")
        buf.write("\2\2CD\7\t\2\2DE\7\21\2\2EF\5\6\4\2F\17\3\2\2\2GH\7\n")
        buf.write("\2\2HK\7\21\2\2IL\5\22\n\2JL\5\24\13\2KI\3\2\2\2KJ\3\2")
        buf.write("\2\2LM\3\2\2\2MN\7\5\2\2N\21\3\2\2\2OP\7\13\2\2PQ\7\f")
        buf.write("\2\2QR\7\21\2\2RS\7\r\2\2ST\7\21\2\2T\23\3\2\2\2UV\7\13")
        buf.write("\2\2VW\7\f\2\2WX\7\21\2\2XY\7\16\2\2YZ\7\21\2\2Z\25\3")
        buf.write("\2\2\2\t\32&,\67<>K")
        return buf.getvalue()


class HotkeyParser ( Parser ):

    grammarFileName = "Hotkey.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'project'", "','", "';'", "'true'", "'false'", 
                     "'null'", "'namespace'", "'hotkey'", "'condition'", 
                     "'is'", "'->'", "'&'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "EQUAL", "OPERATING_SYSTEM", "NAME", 
                      "STRING", "NUMBER", "WS" ]

    RULE_project = 0
    RULE_project_info = 1
    RULE_dictionary = 2
    RULE_pair = 3
    RULE_value = 4
    RULE_os_config = 5
    RULE_namespace = 6
    RULE_hotkey = 7
    RULE_sequence_condition = 8
    RULE_simultaneous_condition = 9

    ruleNames =  [ "project", "project_info", "dictionary", "pair", "value", 
                   "os_config", "namespace", "hotkey", "sequence_condition", 
                   "simultaneous_condition" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    EQUAL=13
    OPERATING_SYSTEM=14
    NAME=15
    STRING=16
    NUMBER=17
    WS=18

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProjectContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def project_info(self):
            return self.getTypedRuleContext(HotkeyParser.Project_infoContext,0)


        def os_config(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HotkeyParser.Os_configContext)
            else:
                return self.getTypedRuleContext(HotkeyParser.Os_configContext,i)


        def getRuleIndex(self):
            return HotkeyParser.RULE_project

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProject" ):
                listener.enterProject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProject" ):
                listener.exitProject(self)




    def project(self):

        localctx = HotkeyParser.ProjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_project)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.project_info()
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HotkeyParser.OPERATING_SYSTEM:
                self.state = 21
                self.os_config()
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Project_infoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(HotkeyParser.NAME, 0)

        def dictionary(self):
            return self.getTypedRuleContext(HotkeyParser.DictionaryContext,0)


        def getRuleIndex(self):
            return HotkeyParser.RULE_project_info

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProject_info" ):
                listener.enterProject_info(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProject_info" ):
                listener.exitProject_info(self)




    def project_info(self):

        localctx = HotkeyParser.Project_infoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_project_info)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(HotkeyParser.T__0)
            self.state = 28
            self.match(HotkeyParser.NAME)
            self.state = 29
            self.dictionary()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DictionaryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HotkeyParser.RULE_dictionary

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AnObjectContext(DictionaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HotkeyParser.DictionaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HotkeyParser.PairContext)
            else:
                return self.getTypedRuleContext(HotkeyParser.PairContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnObject" ):
                listener.enterAnObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnObject" ):
                listener.exitAnObject(self)


    class EmptyObjectContext(DictionaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HotkeyParser.DictionaryContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyObject" ):
                listener.enterEmptyObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyObject" ):
                listener.exitEmptyObject(self)



    def dictionary(self):

        localctx = HotkeyParser.DictionaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_dictionary)
        self._la = 0 # Token type
        try:
            self.state = 42
            token = self._input.LA(1)
            if token in [HotkeyParser.STRING]:
                localctx = HotkeyParser.AnObjectContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.pair()
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==HotkeyParser.T__1:
                    self.state = 32
                    self.match(HotkeyParser.T__1)
                    self.state = 33
                    self.pair()
                    self.state = 38
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 39
                self.match(HotkeyParser.T__2)

            elif token in [HotkeyParser.T__2]:
                localctx = HotkeyParser.EmptyObjectContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.match(HotkeyParser.T__2)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PairContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(HotkeyParser.STRING, 0)

        def EQUAL(self):
            return self.getToken(HotkeyParser.EQUAL, 0)

        def value(self):
            return self.getTypedRuleContext(HotkeyParser.ValueContext,0)


        def getRuleIndex(self):
            return HotkeyParser.RULE_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPair" ):
                listener.enterPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPair" ):
                listener.exitPair(self)




    def pair(self):

        localctx = HotkeyParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(HotkeyParser.STRING)
            self.state = 45
            self.match(HotkeyParser.EQUAL)
            self.state = 46
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HotkeyParser.RULE_value

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StringContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HotkeyParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(HotkeyParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)


    class AtomContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HotkeyParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(HotkeyParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)



    def value(self):

        localctx = HotkeyParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_value)
        try:
            self.state = 53
            token = self._input.LA(1)
            if token in [HotkeyParser.STRING]:
                localctx = HotkeyParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.match(HotkeyParser.STRING)

            elif token in [HotkeyParser.NUMBER]:
                localctx = HotkeyParser.AtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.match(HotkeyParser.NUMBER)

            elif token in [HotkeyParser.T__3]:
                localctx = HotkeyParser.AtomContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.match(HotkeyParser.T__3)

            elif token in [HotkeyParser.T__4]:
                localctx = HotkeyParser.AtomContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 51
                self.match(HotkeyParser.T__4)

            elif token in [HotkeyParser.T__5]:
                localctx = HotkeyParser.AtomContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 52
                self.match(HotkeyParser.T__5)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Os_configContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPERATING_SYSTEM(self):
            return self.getToken(HotkeyParser.OPERATING_SYSTEM, 0)

        def namespace(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HotkeyParser.NamespaceContext)
            else:
                return self.getTypedRuleContext(HotkeyParser.NamespaceContext,i)


        def hotkey(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HotkeyParser.HotkeyContext)
            else:
                return self.getTypedRuleContext(HotkeyParser.HotkeyContext,i)


        def getRuleIndex(self):
            return HotkeyParser.RULE_os_config

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOs_config" ):
                listener.enterOs_config(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOs_config" ):
                listener.exitOs_config(self)




    def os_config(self):

        localctx = HotkeyParser.Os_configContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_os_config)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(HotkeyParser.OPERATING_SYSTEM)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HotkeyParser.T__6 or _la==HotkeyParser.T__7:
                self.state = 58
                token = self._input.LA(1)
                if token in [HotkeyParser.T__6]:
                    self.state = 56
                    self.namespace()

                elif token in [HotkeyParser.T__7]:
                    self.state = 57
                    self.hotkey()

                else:
                    raise NoViableAltException(self)

                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 63
            self.match(HotkeyParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NamespaceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(HotkeyParser.NAME, 0)

        def dictionary(self):
            return self.getTypedRuleContext(HotkeyParser.DictionaryContext,0)


        def getRuleIndex(self):
            return HotkeyParser.RULE_namespace

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamespace" ):
                listener.enterNamespace(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamespace" ):
                listener.exitNamespace(self)




    def namespace(self):

        localctx = HotkeyParser.NamespaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_namespace)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(HotkeyParser.T__6)
            self.state = 66
            self.match(HotkeyParser.NAME)
            self.state = 67
            self.dictionary()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class HotkeyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(HotkeyParser.NAME, 0)

        def sequence_condition(self):
            return self.getTypedRuleContext(HotkeyParser.Sequence_conditionContext,0)


        def simultaneous_condition(self):
            return self.getTypedRuleContext(HotkeyParser.Simultaneous_conditionContext,0)


        def getRuleIndex(self):
            return HotkeyParser.RULE_hotkey

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHotkey" ):
                listener.enterHotkey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHotkey" ):
                listener.exitHotkey(self)




    def hotkey(self):

        localctx = HotkeyParser.HotkeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_hotkey)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(HotkeyParser.T__7)
            self.state = 70
            self.match(HotkeyParser.NAME)
            self.state = 73
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 71
                self.sequence_condition()
                pass

            elif la_ == 2:
                self.state = 72
                self.simultaneous_condition()
                pass


            self.state = 75
            self.match(HotkeyParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Sequence_conditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(HotkeyParser.NAME)
            else:
                return self.getToken(HotkeyParser.NAME, i)

        def getRuleIndex(self):
            return HotkeyParser.RULE_sequence_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSequence_condition" ):
                listener.enterSequence_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSequence_condition" ):
                listener.exitSequence_condition(self)




    def sequence_condition(self):

        localctx = HotkeyParser.Sequence_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_sequence_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(HotkeyParser.T__8)
            self.state = 78
            self.match(HotkeyParser.T__9)
            self.state = 79
            self.match(HotkeyParser.NAME)
            self.state = 80
            self.match(HotkeyParser.T__10)
            self.state = 81
            self.match(HotkeyParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Simultaneous_conditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(HotkeyParser.NAME)
            else:
                return self.getToken(HotkeyParser.NAME, i)

        def getRuleIndex(self):
            return HotkeyParser.RULE_simultaneous_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimultaneous_condition" ):
                listener.enterSimultaneous_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimultaneous_condition" ):
                listener.exitSimultaneous_condition(self)




    def simultaneous_condition(self):

        localctx = HotkeyParser.Simultaneous_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_simultaneous_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(HotkeyParser.T__8)
            self.state = 84
            self.match(HotkeyParser.T__9)
            self.state = 85
            self.match(HotkeyParser.NAME)
            self.state = 86
            self.match(HotkeyParser.T__11)
            self.state = 87
            self.match(HotkeyParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





