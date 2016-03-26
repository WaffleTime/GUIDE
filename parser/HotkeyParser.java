// Generated from ../../parser/Hotkey.g4 by ANTLR 4.5.2
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
		T__9=10, T__10=11, T__11=12, T__12=13, EQUAL=14, OPERATING_SYSTEM=15, 
		STRING=16, NUMBER=17, WS=18;
	public static final int
		RULE_project_info = 0, RULE_map = 1, RULE_pair = 2, RULE_value = 3, RULE_os_config = 4, 
		RULE_namespace = 5, RULE_hotkey = 6, RULE_sequence_condition = 7, RULE_simultaneous_condition = 8;
	public static final String[] ruleNames = {
		"project_info", "map", "pair", "value", "os_config", "namespace", "hotkey", 
		"sequence_condition", "simultaneous_condition"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'project'", "','", "';'", "'true'", "'false'", "'null'", "'windows:'", 
		"'namespace'", "'hotkey'", "'condition'", "'is'", "'->'", "'&'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, "EQUAL", "OPERATING_SYSTEM", "STRING", "NUMBER", "WS"
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
		enterRule(_localctx, 0, RULE_project_info);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(18);
			match(T__0);
			setState(19);
			match(STRING);
			setState(20);
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
		enterRule(_localctx, 2, RULE_map);
		int _la;
		try {
			setState(33);
			switch (_input.LA(1)) {
			case STRING:
				_localctx = new AnObjectContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(22);
				pair();
				setState(27);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__1) {
					{
					{
					setState(23);
					match(T__1);
					setState(24);
					pair();
					}
					}
					setState(29);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(30);
				match(T__2);
				}
				break;
			case T__2:
				_localctx = new EmptyObjectContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(32);
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
		enterRule(_localctx, 4, RULE_pair);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(35);
			match(STRING);
			setState(36);
			match(EQUAL);
			setState(37);
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
		enterRule(_localctx, 6, RULE_value);
		try {
			setState(44);
			switch (_input.LA(1)) {
			case STRING:
				_localctx = new StringContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(39);
				match(STRING);
				}
				break;
			case NUMBER:
				_localctx = new AtomContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(40);
				match(NUMBER);
				}
				break;
			case T__3:
				_localctx = new AtomContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(41);
				match(T__3);
				}
				break;
			case T__4:
				_localctx = new AtomContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(42);
				match(T__4);
				}
				break;
			case T__5:
				_localctx = new AtomContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(43);
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
		enterRule(_localctx, 8, RULE_os_config);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(46);
			match(T__6);
			setState(51);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__7 || _la==T__8) {
				{
				setState(49);
				switch (_input.LA(1)) {
				case T__7:
					{
					{
					setState(47);
					namespace();
					}
					}
					break;
				case T__8:
					{
					{
					setState(48);
					hotkey();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(53);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(54);
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
		enterRule(_localctx, 10, RULE_namespace);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(56);
			match(T__7);
			setState(57);
			match(STRING);
			setState(58);
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
		enterRule(_localctx, 12, RULE_hotkey);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(60);
			match(T__8);
			setState(61);
			match(STRING);
			setState(64);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				{
				setState(62);
				sequence_condition();
				}
				break;
			case 2:
				{
				setState(63);
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
		enterRule(_localctx, 14, RULE_sequence_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(66);
			match(T__9);
			setState(67);
			match(T__10);
			setState(68);
			match(STRING);
			setState(69);
			match(T__11);
			setState(70);
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
		enterRule(_localctx, 16, RULE_simultaneous_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(72);
			match(T__9);
			setState(73);
			match(T__10);
			setState(74);
			match(STRING);
			setState(75);
			match(T__12);
			setState(76);
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
		"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\24Q\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2"+
		"\3\2\3\3\3\3\3\3\7\3\34\n\3\f\3\16\3\37\13\3\3\3\3\3\3\3\5\3$\n\3\3\4"+
		"\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\5\5/\n\5\3\6\3\6\3\6\7\6\64\n\6\f\6\16"+
		"\6\67\13\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\5\bC\n\b\3\t\3\t\3"+
		"\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\2\2\13\2\4\6\b\n\f\16\20\22"+
		"\2\2P\2\24\3\2\2\2\4#\3\2\2\2\6%\3\2\2\2\b.\3\2\2\2\n\60\3\2\2\2\f:\3"+
		"\2\2\2\16>\3\2\2\2\20D\3\2\2\2\22J\3\2\2\2\24\25\7\3\2\2\25\26\7\22\2"+
		"\2\26\27\5\4\3\2\27\3\3\2\2\2\30\35\5\6\4\2\31\32\7\4\2\2\32\34\5\6\4"+
		"\2\33\31\3\2\2\2\34\37\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36 \3\2\2\2"+
		"\37\35\3\2\2\2 !\7\5\2\2!$\3\2\2\2\"$\7\5\2\2#\30\3\2\2\2#\"\3\2\2\2$"+
		"\5\3\2\2\2%&\7\22\2\2&\'\7\20\2\2\'(\5\b\5\2(\7\3\2\2\2)/\7\22\2\2*/\7"+
		"\23\2\2+/\7\6\2\2,/\7\7\2\2-/\7\b\2\2.)\3\2\2\2.*\3\2\2\2.+\3\2\2\2.,"+
		"\3\2\2\2.-\3\2\2\2/\t\3\2\2\2\60\65\7\t\2\2\61\64\5\f\7\2\62\64\5\16\b"+
		"\2\63\61\3\2\2\2\63\62\3\2\2\2\64\67\3\2\2\2\65\63\3\2\2\2\65\66\3\2\2"+
		"\2\668\3\2\2\2\67\65\3\2\2\289\7\5\2\29\13\3\2\2\2:;\7\n\2\2;<\7\22\2"+
		"\2<=\5\4\3\2=\r\3\2\2\2>?\7\13\2\2?B\7\22\2\2@C\5\20\t\2AC\5\22\n\2B@"+
		"\3\2\2\2BA\3\2\2\2C\17\3\2\2\2DE\7\f\2\2EF\7\r\2\2FG\7\22\2\2GH\7\16\2"+
		"\2HI\7\22\2\2I\21\3\2\2\2JK\7\f\2\2KL\7\r\2\2LM\7\22\2\2MN\7\17\2\2NO"+
		"\7\22\2\2O\23\3\2\2\2\b\35#.\63\65B";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}