// Grammar for guide's hotkey configuration files.
grammar Hotkey;

project
    : project_info (os_config)*
    ;


project_info
    :   'project' STRING map
    ;

map
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
    :   'namespace' STRING map
    ;
    
hotkey
    : 'hotkey' STRING (sequence_condition | simultaneous_condition)
    ;
    
sequence_condition
    : 'condition' 'is' STRING '->' STRING
    ;
    
simultaneous_condition
    : 'condition' 'is' STRING '&' STRING
    ;


EQUAL : ('is' | '=');
    
OPERATING_SYSTEM : ('windows:' | 'linux:' | 'osx');

STRING :  '"' (ESC | ~["\\])* '"' ;
fragment ESC :   '\\' (["\\/bfnrt] | UNICODE) ;
fragment UNICODE : 'u' HEX HEX HEX HEX ;
fragment HEX : [0-9a-fA-F] ;

NUMBER
    :   '-'? INT '.' INT EXP?   // 1.35, 1.35E-9, 0.3, -4.5
    |   '-'? INT EXP            // 1e10 -3e4
    |   '-'? INT                // -3, 45
    ;
fragment INT :   '0' | '1'..'9' '0'..'9'* ; // no leading zeros
fragment EXP :   [Ee] [+\-]? INT ; // \- since - means "range" inside [...]

WS  :   [ \t\n\r]+ -> skip ;