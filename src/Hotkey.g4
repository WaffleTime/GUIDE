// Grammar for guide's hotkey configuration files.
grammar Hotkey;

project
    : project_info (config)*
    ;

project_info
    :   'project' NAME dictionary
    ;

dictionary
    :   pair (',' pair)*  ';'       # AnObject
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

config
    :   OPERATING_SYSTEM
            ((namespace | external_tool_hotkey | custom_script_hotkey))*
            ';'
    ;

namespace
    :   'namespace' NAME dictionary
    ;

external_tool_hotkey
    : 'external_hotkey' NAME
          simultaneous_condition
          (environment_vars)?
          (working_dir)?
          'executable' EQUAL STRING
          ';'
    ;

environment_vars
    : 'environment_variables' dictionary
    ;

working_dir
    : 'working_directory' EQUAL STRING
    ;

custom_script_hotkey
    : 'internal_hotkey' NAME
          simultaneous_condition
          'executable' EQUAL STRING
          ';'
    ;

simultaneous_condition
    : 'condition' NAME (',' NAME)*
    ;


EQUAL : ('is' | '=');

OPERATING_SYSTEM : ('global:' | 'windows:' | 'linux:' | 'osx:');

NAME : [a-zA-Z0-9_-]+ ;

STRING :  '"' ~('\r' | '\n' | '"')* '"' ;

NUMBER
    :   '-'? INT '.' INT EXP?   // 1.35, 1.35E-9, 0.3, -4.5
    |   '-'? INT EXP            // 1e10 -3e4
    |   '-'? INT                // -3, 45
    ;

fragment INT :   '0' | '1'..'9' '0'..'9'* ; // no leading zeros
fragment EXP :   [Ee] [+\-]? INT ; // \- since - means "range" inside [...]

WS  :   [ \t\n\r]+ -> skip ;