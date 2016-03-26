// Generated from ../../src/parser/Hotkey.g4 by ANTLR 4.5.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link HotkeyParser}.
 */
public interface HotkeyListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link HotkeyParser#project}.
	 * @param ctx the parse tree
	 */
	void enterProject(HotkeyParser.ProjectContext ctx);
	/**
	 * Exit a parse tree produced by {@link HotkeyParser#project}.
	 * @param ctx the parse tree
	 */
	void exitProject(HotkeyParser.ProjectContext ctx);
	/**
	 * Enter a parse tree produced by {@link HotkeyParser#project_info}.
	 * @param ctx the parse tree
	 */
	void enterProject_info(HotkeyParser.Project_infoContext ctx);
	/**
	 * Exit a parse tree produced by {@link HotkeyParser#project_info}.
	 * @param ctx the parse tree
	 */
	void exitProject_info(HotkeyParser.Project_infoContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AnObject}
	 * labeled alternative in {@link HotkeyParser#map}.
	 * @param ctx the parse tree
	 */
	void enterAnObject(HotkeyParser.AnObjectContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AnObject}
	 * labeled alternative in {@link HotkeyParser#map}.
	 * @param ctx the parse tree
	 */
	void exitAnObject(HotkeyParser.AnObjectContext ctx);
	/**
	 * Enter a parse tree produced by the {@code EmptyObject}
	 * labeled alternative in {@link HotkeyParser#map}.
	 * @param ctx the parse tree
	 */
	void enterEmptyObject(HotkeyParser.EmptyObjectContext ctx);
	/**
	 * Exit a parse tree produced by the {@code EmptyObject}
	 * labeled alternative in {@link HotkeyParser#map}.
	 * @param ctx the parse tree
	 */
	void exitEmptyObject(HotkeyParser.EmptyObjectContext ctx);
	/**
	 * Enter a parse tree produced by {@link HotkeyParser#pair}.
	 * @param ctx the parse tree
	 */
	void enterPair(HotkeyParser.PairContext ctx);
	/**
	 * Exit a parse tree produced by {@link HotkeyParser#pair}.
	 * @param ctx the parse tree
	 */
	void exitPair(HotkeyParser.PairContext ctx);
	/**
	 * Enter a parse tree produced by the {@code String}
	 * labeled alternative in {@link HotkeyParser#value}.
	 * @param ctx the parse tree
	 */
	void enterString(HotkeyParser.StringContext ctx);
	/**
	 * Exit a parse tree produced by the {@code String}
	 * labeled alternative in {@link HotkeyParser#value}.
	 * @param ctx the parse tree
	 */
	void exitString(HotkeyParser.StringContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Atom}
	 * labeled alternative in {@link HotkeyParser#value}.
	 * @param ctx the parse tree
	 */
	void enterAtom(HotkeyParser.AtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Atom}
	 * labeled alternative in {@link HotkeyParser#value}.
	 * @param ctx the parse tree
	 */
	void exitAtom(HotkeyParser.AtomContext ctx);
	/**
	 * Enter a parse tree produced by {@link HotkeyParser#os_config}.
	 * @param ctx the parse tree
	 */
	void enterOs_config(HotkeyParser.Os_configContext ctx);
	/**
	 * Exit a parse tree produced by {@link HotkeyParser#os_config}.
	 * @param ctx the parse tree
	 */
	void exitOs_config(HotkeyParser.Os_configContext ctx);
	/**
	 * Enter a parse tree produced by {@link HotkeyParser#namespace}.
	 * @param ctx the parse tree
	 */
	void enterNamespace(HotkeyParser.NamespaceContext ctx);
	/**
	 * Exit a parse tree produced by {@link HotkeyParser#namespace}.
	 * @param ctx the parse tree
	 */
	void exitNamespace(HotkeyParser.NamespaceContext ctx);
	/**
	 * Enter a parse tree produced by {@link HotkeyParser#hotkey}.
	 * @param ctx the parse tree
	 */
	void enterHotkey(HotkeyParser.HotkeyContext ctx);
	/**
	 * Exit a parse tree produced by {@link HotkeyParser#hotkey}.
	 * @param ctx the parse tree
	 */
	void exitHotkey(HotkeyParser.HotkeyContext ctx);
	/**
	 * Enter a parse tree produced by {@link HotkeyParser#sequence_condition}.
	 * @param ctx the parse tree
	 */
	void enterSequence_condition(HotkeyParser.Sequence_conditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HotkeyParser#sequence_condition}.
	 * @param ctx the parse tree
	 */
	void exitSequence_condition(HotkeyParser.Sequence_conditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HotkeyParser#simultaneous_condition}.
	 * @param ctx the parse tree
	 */
	void enterSimultaneous_condition(HotkeyParser.Simultaneous_conditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HotkeyParser#simultaneous_condition}.
	 * @param ctx the parse tree
	 */
	void exitSimultaneous_condition(HotkeyParser.Simultaneous_conditionContext ctx);
}