// Generated from ../../src/parser/Hotkey.g4 by ANTLR 4.5.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class HotkeyLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.5.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, EQUAL=13, OPERATING_SYSTEM=14, STRING=15, 
		NUMBER=16, WS=17;
	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
		"T__9", "T__10", "T__11", "EQUAL", "OPERATING_SYSTEM", "STRING", "ESC", 
		"UNICODE", "HEX", "NUMBER", "INT", "EXP", "WS"
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


	public HotkeyLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Hotkey.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\23\u00c9\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6"+
		"\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3"+
		"\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13"+
		"\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\16\5\16r\n\16\3\17\3\17\3\17"+
		"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17"+
		"\5\17\u0085\n\17\3\20\3\20\3\20\7\20\u008a\n\20\f\20\16\20\u008d\13\20"+
		"\3\20\3\20\3\21\3\21\3\21\5\21\u0094\n\21\3\22\3\22\3\22\3\22\3\22\3\22"+
		"\3\23\3\23\3\24\5\24\u009f\n\24\3\24\3\24\3\24\3\24\5\24\u00a5\n\24\3"+
		"\24\5\24\u00a8\n\24\3\24\3\24\3\24\3\24\5\24\u00ae\n\24\3\24\5\24\u00b1"+
		"\n\24\3\25\3\25\3\25\7\25\u00b6\n\25\f\25\16\25\u00b9\13\25\5\25\u00bb"+
		"\n\25\3\26\3\26\5\26\u00bf\n\26\3\26\3\26\3\27\6\27\u00c4\n\27\r\27\16"+
		"\27\u00c5\3\27\3\27\2\2\30\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25"+
		"\f\27\r\31\16\33\17\35\20\37\21!\2#\2%\2\'\22)\2+\2-\23\3\2\b\4\2$$^^"+
		"\n\2$$\61\61^^ddhhppttvv\5\2\62;CHch\4\2GGgg\4\2--//\5\2\13\f\17\17\""+
		"\"\u00d3\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2"+
		"\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27"+
		"\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2\'\3\2\2"+
		"\2\2-\3\2\2\2\3/\3\2\2\2\5\67\3\2\2\2\79\3\2\2\2\t;\3\2\2\2\13@\3\2\2"+
		"\2\rF\3\2\2\2\17K\3\2\2\2\21U\3\2\2\2\23\\\3\2\2\2\25f\3\2\2\2\27i\3\2"+
		"\2\2\31l\3\2\2\2\33q\3\2\2\2\35\u0084\3\2\2\2\37\u0086\3\2\2\2!\u0090"+
		"\3\2\2\2#\u0095\3\2\2\2%\u009b\3\2\2\2\'\u00b0\3\2\2\2)\u00ba\3\2\2\2"+
		"+\u00bc\3\2\2\2-\u00c3\3\2\2\2/\60\7r\2\2\60\61\7t\2\2\61\62\7q\2\2\62"+
		"\63\7l\2\2\63\64\7g\2\2\64\65\7e\2\2\65\66\7v\2\2\66\4\3\2\2\2\678\7."+
		"\2\28\6\3\2\2\29:\7=\2\2:\b\3\2\2\2;<\7v\2\2<=\7t\2\2=>\7w\2\2>?\7g\2"+
		"\2?\n\3\2\2\2@A\7h\2\2AB\7c\2\2BC\7n\2\2CD\7u\2\2DE\7g\2\2E\f\3\2\2\2"+
		"FG\7p\2\2GH\7w\2\2HI\7n\2\2IJ\7n\2\2J\16\3\2\2\2KL\7p\2\2LM\7c\2\2MN\7"+
		"o\2\2NO\7g\2\2OP\7u\2\2PQ\7r\2\2QR\7c\2\2RS\7e\2\2ST\7g\2\2T\20\3\2\2"+
		"\2UV\7j\2\2VW\7q\2\2WX\7v\2\2XY\7m\2\2YZ\7g\2\2Z[\7{\2\2[\22\3\2\2\2\\"+
		"]\7e\2\2]^\7q\2\2^_\7p\2\2_`\7f\2\2`a\7k\2\2ab\7v\2\2bc\7k\2\2cd\7q\2"+
		"\2de\7p\2\2e\24\3\2\2\2fg\7k\2\2gh\7u\2\2h\26\3\2\2\2ij\7/\2\2jk\7@\2"+
		"\2k\30\3\2\2\2lm\7(\2\2m\32\3\2\2\2no\7k\2\2or\7u\2\2pr\7?\2\2qn\3\2\2"+
		"\2qp\3\2\2\2r\34\3\2\2\2st\7y\2\2tu\7k\2\2uv\7p\2\2vw\7f\2\2wx\7q\2\2"+
		"xy\7y\2\2yz\7u\2\2z\u0085\7<\2\2{|\7n\2\2|}\7k\2\2}~\7p\2\2~\177\7w\2"+
		"\2\177\u0080\7z\2\2\u0080\u0085\7<\2\2\u0081\u0082\7q\2\2\u0082\u0083"+
		"\7u\2\2\u0083\u0085\7z\2\2\u0084s\3\2\2\2\u0084{\3\2\2\2\u0084\u0081\3"+
		"\2\2\2\u0085\36\3\2\2\2\u0086\u008b\7$\2\2\u0087\u008a\5!\21\2\u0088\u008a"+
		"\n\2\2\2\u0089\u0087\3\2\2\2\u0089\u0088\3\2\2\2\u008a\u008d\3\2\2\2\u008b"+
		"\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008e\3\2\2\2\u008d\u008b\3\2"+
		"\2\2\u008e\u008f\7$\2\2\u008f \3\2\2\2\u0090\u0093\7^\2\2\u0091\u0094"+
		"\t\3\2\2\u0092\u0094\5#\22\2\u0093\u0091\3\2\2\2\u0093\u0092\3\2\2\2\u0094"+
		"\"\3\2\2\2\u0095\u0096\7w\2\2\u0096\u0097\5%\23\2\u0097\u0098\5%\23\2"+
		"\u0098\u0099\5%\23\2\u0099\u009a\5%\23\2\u009a$\3\2\2\2\u009b\u009c\t"+
		"\4\2\2\u009c&\3\2\2\2\u009d\u009f\7/\2\2\u009e\u009d\3\2\2\2\u009e\u009f"+
		"\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\5)\25\2\u00a1\u00a2\7\60\2\2"+
		"\u00a2\u00a4\5)\25\2\u00a3\u00a5\5+\26\2\u00a4\u00a3\3\2\2\2\u00a4\u00a5"+
		"\3\2\2\2\u00a5\u00b1\3\2\2\2\u00a6\u00a8\7/\2\2\u00a7\u00a6\3\2\2\2\u00a7"+
		"\u00a8\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00aa\5)\25\2\u00aa\u00ab\5+"+
		"\26\2\u00ab\u00b1\3\2\2\2\u00ac\u00ae\7/\2\2\u00ad\u00ac\3\2\2\2\u00ad"+
		"\u00ae\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b1\5)\25\2\u00b0\u009e\3\2"+
		"\2\2\u00b0\u00a7\3\2\2\2\u00b0\u00ad\3\2\2\2\u00b1(\3\2\2\2\u00b2\u00bb"+
		"\7\62\2\2\u00b3\u00b7\4\63;\2\u00b4\u00b6\4\62;\2\u00b5\u00b4\3\2\2\2"+
		"\u00b6\u00b9\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00bb"+
		"\3\2\2\2\u00b9\u00b7\3\2\2\2\u00ba\u00b2\3\2\2\2\u00ba\u00b3\3\2\2\2\u00bb"+
		"*\3\2\2\2\u00bc\u00be\t\5\2\2\u00bd\u00bf\t\6\2\2\u00be\u00bd\3\2\2\2"+
		"\u00be\u00bf\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c1\5)\25\2\u00c1,\3"+
		"\2\2\2\u00c2\u00c4\t\7\2\2\u00c3\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5"+
		"\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c8\b\27"+
		"\2\2\u00c8.\3\2\2\2\21\2q\u0084\u0089\u008b\u0093\u009e\u00a4\u00a7\u00ad"+
		"\u00b0\u00b7\u00ba\u00be\u00c5\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}