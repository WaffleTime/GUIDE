// Generated from ../../src/parser/Hotkey.g4 by ANTLR 4.5.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class HotkeyParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.5.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, EQUAL=13, OPERATING_SYSTEM=14, STRING=15, 
		NUMBER=16, WS=17;
	public static final int
		RULE_project = 0, RULE_project_info = 1, RULE_map = 2, RULE_pair = 3, 
		RULE_value = 4, RULE_os_config = 5, RULE_namespace = 6, RULE_hotkey = 7, 
		RULE_sequence_condition = 8, RULE_simultaneous_condition = 9;
	public static final String[] ruleNames = {
		"project", "project_info", "map", "pair", "value", "os_config", "namespace", 
		"hotkey", "sequence_condition", "simultaneous_condition"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'project'", "','", "';'", "'true'", "'false'", "'null'", "'namespace'", 
		"'hotkey'", "'condition'", "'is'", "'->'", "'&'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, "EQUAL", "OPERATING_SYSTEM", "STRING", "NUMBER", "WS"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Hotkey.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public HotkeyParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class ProjectContext extends ParserRuleContext {
		public Project_infoContext project_info() {
			return getRuleContext(Project_infoContext.class,0);
		}
		public List<Os_configContext> os_config() {
			return getRuleContexts(Os_configContext.class);
		}
		public Os_configContext os_config(int i) {
			return getRuleContext(Os_configContext.class,i);
		}
		public ProjectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_project; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HotkeyListener ) ((HotkeyListener)listener).enterProject(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HotkeyListener ) ((HotkeyListener)listener).exitProject(this);
		}
	}

	public final ProjectContext project() throws RecognitionException {
		ProjectContext _localctx = new ProjectContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_project);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(20);
			project_info();
			setState(24);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OPERATING_SYSTEM) {
				{
				{
				setState(21);
				os_config();
				}
				}
				setState(26);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Project_infoContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(HotkeyParser.STRING, 0); }
		public MapContext map() {
			return getRuleContext(MapContext.class,0);
		}
		public Project_infoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_project_info; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HotkeyListener ) ((HotkeyListener)listener).enterProject_info(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HotkeyListener ) ((HotkeyListener)listener).exitProject_info(this);
		}
	}

	public final Project_infoContext project_info() throws RecognitionException {
		Project_infoContext _localctx = new Project_infoContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_project_info);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(27);
			match(T__0);
			setState(28);
			match(STRING);
			setState(29);
			map();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MapContext extends ParserRuleContext {
		public MapContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_map; }
	 
		public MapContext() { }
		public void copyFrom(MapContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class AnObjectContext extends MapContext {
		public List<PairContext> pair() {
			return getRuleContexts(PairContext.class);
		}
		public PairContext pair(int i) {
			return getRuleContext(PairContext.class,i);
		}
		public AnObjectContext(MapContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HotkeyListener ) ((HotkeyListener)listener).enterAnObject(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HotkeyListener ) ((HotkeyListener)listener).exitAnObject(this);
		}
	}
	public static class EmptyObjectContext extends MapContext {
		public EmptyObjectContext(MapContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HotkeyListener ) ((HotkeyListener)listener).enterEmptyObject(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HotkeyListener ) ((HotkeyListener)listener).exitEmptyObject(this);
		}
	}

	public final MapContext map() throws RecognitionException {
		MapContext _localctx = new MapContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_map);
		int _la;
		try {
			setState(42);
			switch (_input.LA(1)) {
			case STRING:
				_localctx = new AnObjectContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(31);
				pair();
				setState(36);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__1) {
					{
					{
					setState(32);
					match(T__1);
					setState(33);
					pair();
					}
					}
					setState(38);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(39);
				match(T__2);
				}
				break;
			case T__2:
				_localctx = new EmptyObjectContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(41);
				match(T__2);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PairContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(HotkeyParser.STRING, 0); }
		public TerminalNode EQUAL() { return getToken(HotkeyParser.EQUAL, 0); }
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public PairContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pair; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HotkeyListener ) ((HotkeyListener)listener).enterPair(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HotkeyListener ) ((HotkeyListener)listener).exitPair(this);
		}
	}

	public final PairContext pair() throws RecognitionException {
		PairContext _localctx = new PairContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_pair);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(44);
			match(STRING);
			setState(45);
			match(EQUAL);
			setState(46);
			value();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ValueContext extends ParserRuleContext {
		public ValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value; }
	 
		public ValueContext() { }
		public void copyFrom(ValueContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class StringContext extends ValueContext {
		public TerminalNode STRING() { return getToken(HotkeyParser.STRING, 0); }
		public StringContext(ValueContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HotkeyListener ) ((HotkeyListener)listener).enterString(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HotkeyListener ) ((HotkeyListener)listener).exitString(this);
		}
	}
	public static class AtomContext extends ValueContext {
		public TerminalNode NUMBER() { return getToken(HotkeyParser.NUMBER, 0); }
		public AtomContext(ValueContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HotkeyListener ) ((HotkeyListener)listener).enterAtom(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HotkeyListener ) ((HotkeyListener)listener).exitAtom(this);
		}
	}

	public final ValueContext value() throws RecognitionException {
		ValueContext _localctx = new ValueContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_value);
		try {
			setState(53);
			switch (_input.LA(1)) {
			case STRING:
				_localctx = new StringContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(48);
				match(STRING);
				}
				break;
			case NUMBER:
				_localctx = new AtomContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(49);
				match(NUMBER);
				}
				break;
			case T__3:
				_localctx = new AtomContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(50);
				match(T__3);
				}
				break;
			case T__4:
				_localctx = new AtomContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(51);
				match(T__4);
				}
				break;
			case T__5:
				_localctx = new AtomContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(52);
				match(T__5);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Os_configContext extends ParserRuleContext {
		public TerminalNode OPERATING_SYSTEM() { return getToken(HotkeyParser.OPERATING_SYSTEM, 0); }
		public List<NamespaceContext> namespace() {
			return getRuleContexts(NamespaceContext.class);
		}
		public NamespaceContext namespace(int i) {
			return getRuleContext(NamespaceContext.class,i);
		}
		public List<HotkeyContext> hotkey() {
			return getRuleContexts(HotkeyContext.class);
		}
		public HotkeyContext hotkey(int i) {
			return getRuleContext(HotkeyContext.class,i);
		}
		public Os_configContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_os_config; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HotkeyListener ) ((HotkeyListener)listener).enterOs_config(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HotkeyListener ) ((HotkeyListener)listener).exitOs_config(this);
		}
	}

	public final Os_configContext os_config() throws RecognitionException {
		Os_configContext _localctx = new Os_configContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_os_config);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(55);
			match(OPERATING_SYSTEM);
			setState(60);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6 || _la==T__7) {
				{
				setState(58);
				switch (_input.LA(1)) {
				case T__6:
					{
					{
					setState(56);
					namespace();
					}
					}
					break;
				case T__7:
					{
					{
					setState(57);
					hotkey();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(62);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(63);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NamespaceContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(HotkeyParser.STRING, 0); }
		public MapContext map() {
			return getRuleContext(MapContext.class,0);
		}
		public NamespaceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_namespace; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HotkeyListener ) ((HotkeyListener)listener).enterNamespace(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HotkeyListener ) ((HotkeyListener)listener).exitNamespace(this);
		}
	}

	public final NamespaceContext namespace() throws RecognitionException {
		NamespaceContext _localctx = new NamespaceContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_namespace);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(65);
			match(T__6);
			setState(66);
			match(STRING);
			setState(67);
			map();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class HotkeyContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(HotkeyParser.STRING, 0); }
		public Sequence_conditionContext sequence_condition() {
			return getRuleContext(Sequence_conditionContext.class,0);
		}
		public Simultaneous_conditionContext simultaneous_condition() {
			return getRuleContext(Simultaneous_conditionContext.class,0);
		}
		public HotkeyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_hotkey; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HotkeyListener ) ((HotkeyListener)listener).enterHotkey(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HotkeyListener ) ((HotkeyListener)listener).exitHotkey(this);
		}
	}

	public final HotkeyContext hotkey() throws RecognitionException {
		HotkeyContext _localctx = new HotkeyContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_hotkey);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(69);
			match(T__7);
			setState(70);
			match(STRING);
			setState(73);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				{
				setState(71);
				sequence_condition();
				}
				break;
			case 2:
				{
				setState(72);
				simultaneous_condition();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Sequence_conditionContext extends ParserRuleContext {
		public List<TerminalNode> STRING() { return getTokens(HotkeyParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(HotkeyParser.STRING, i);
		}
		public Sequence_conditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sequence_condition; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HotkeyListener ) ((HotkeyListener)listener).enterSequence_condition(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HotkeyListener ) ((HotkeyListener)listener).exitSequence_condition(this);
		}
	}

	public final Sequence_conditionContext sequence_condition() throws RecognitionException {
		Sequence_conditionContext _localctx = new Sequence_conditionContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_sequence_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			match(T__8);
			setState(76);
			match(T__9);
			setState(77);
			match(STRING);
			setState(78);
			match(T__10);
			setState(79);
			match(STRING);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Simultaneous_conditionContext extends ParserRuleContext {
		public List<TerminalNode> STRING() { return getTokens(HotkeyParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(HotkeyParser.STRING, i);
		}
		public Simultaneous_conditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_simultaneous_condition; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HotkeyListener ) ((HotkeyListener)listener).enterSimultaneous_condition(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HotkeyListener ) ((HotkeyListener)listener).exitSimultaneous_condition(this);
		}
	}

	public final Simultaneous_conditionContext simultaneous_condition() throws RecognitionException {
		Simultaneous_conditionContext _localctx = new Simultaneous_conditionContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_simultaneous_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(81);
			match(T__8);
			setState(82);
			match(T__9);
			setState(83);
			match(STRING);
			setState(84);
			match(T__11);
			setState(85);
			match(STRING);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\23Z\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3"+
		"\2\3\2\7\2\31\n\2\f\2\16\2\34\13\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\7\4%\n"+
		"\4\f\4\16\4(\13\4\3\4\3\4\3\4\5\4-\n\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6"+
		"\3\6\5\68\n\6\3\7\3\7\3\7\7\7=\n\7\f\7\16\7@\13\7\3\7\3\7\3\b\3\b\3\b"+
		"\3\b\3\t\3\t\3\t\3\t\5\tL\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3"+
		"\13\3\13\3\13\3\13\2\2\f\2\4\6\b\n\f\16\20\22\24\2\2Y\2\26\3\2\2\2\4\35"+
		"\3\2\2\2\6,\3\2\2\2\b.\3\2\2\2\n\67\3\2\2\2\f9\3\2\2\2\16C\3\2\2\2\20"+
		"G\3\2\2\2\22M\3\2\2\2\24S\3\2\2\2\26\32\5\4\3\2\27\31\5\f\7\2\30\27\3"+
		"\2\2\2\31\34\3\2\2\2\32\30\3\2\2\2\32\33\3\2\2\2\33\3\3\2\2\2\34\32\3"+
		"\2\2\2\35\36\7\3\2\2\36\37\7\21\2\2\37 \5\6\4\2 \5\3\2\2\2!&\5\b\5\2\""+
		"#\7\4\2\2#%\5\b\5\2$\"\3\2\2\2%(\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\')\3\2\2"+
		"\2(&\3\2\2\2)*\7\5\2\2*-\3\2\2\2+-\7\5\2\2,!\3\2\2\2,+\3\2\2\2-\7\3\2"+
		"\2\2./\7\21\2\2/\60\7\17\2\2\60\61\5\n\6\2\61\t\3\2\2\2\628\7\21\2\2\63"+
		"8\7\22\2\2\648\7\6\2\2\658\7\7\2\2\668\7\b\2\2\67\62\3\2\2\2\67\63\3\2"+
		"\2\2\67\64\3\2\2\2\67\65\3\2\2\2\67\66\3\2\2\28\13\3\2\2\29>\7\20\2\2"+
		":=\5\16\b\2;=\5\20\t\2<:\3\2\2\2<;\3\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2\2"+
		"\2?A\3\2\2\2@>\3\2\2\2AB\7\5\2\2B\r\3\2\2\2CD\7\t\2\2DE\7\21\2\2EF\5\6"+
		"\4\2F\17\3\2\2\2GH\7\n\2\2HK\7\21\2\2IL\5\22\n\2JL\5\24\13\2KI\3\2\2\2"+
		"KJ\3\2\2\2L\21\3\2\2\2MN\7\13\2\2NO\7\f\2\2OP\7\21\2\2PQ\7\r\2\2QR\7\21"+
		"\2\2R\23\3\2\2\2ST\7\13\2\2TU\7\f\2\2UV\7\21\2\2VW\7\16\2\2WX\7\21\2\2"+
		"X\25\3\2\2\2\t\32&,\67<>K";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}