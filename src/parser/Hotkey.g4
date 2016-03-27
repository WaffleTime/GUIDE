// Grammar for guide's hotkey configuration files.
grammar Hotkey;

project
    : project_info (os_config)*
    ;

project_info
    :   'project' NAME dictionary
    ;

dictionary
    :   pair (',' pair)* ';'        # AnObject
    |   ';'                         # EmptyObject
    ;   

pair:   STRING EQUAL value ;

value
    :   STRING      # String
    |   NUMBER      # Atom
    |   'true'      # Atom
    |   'false'     # Atom
    |   'null'      # Atom
    ;

os_config
    :   OPERATING_SYSTEM ((namespace) | (hotkey))* ';'
    ;
    
namespace
    :   'namespace' NAME dictionary
    ;
    
hotkey
    : 'hotkey' NAME (sequence_condition | simultaneous_condition) ';'
    ;
    
sequence_condition
    : 'condition' 'is' NAME '->' NAME
    ;
    
simultaneous_condition
    : 'condition' 'is' NAME '&' NAME
    ;


EQUAL : ('is' | '=');
    
OPERATING_SYSTEM : ('global' | 'windows:' | 'linux:' | 'osx');

NAME : ~('\r' | '\n' | '"' | ' ')+ ;

STRING :  '"' ~('\r' | '\n' | '"')* '"' ;

NUMBER
    :   '-'? INT '.' INT EXP?   // 1.35, 1.35E-9, 0.3, -4.5
    |   '-'? INT EXP            // 1e10 -3e4
    |   '-'? INT                // -3, 45
    ;
fragment INT :   '0' | '1'..'9' '0'..'9'* ; // no leading zeros
fragment EXP :   [Ee] [+\-]? INT ; // \- since - means "range" inside [...]

WS : SPACE+ -> skip;

fragment SPACE : '\t' | ' ' | '\r' | '\n'| '\u000C';