"""
This module deals with the specification for how keys are mapped to the stuff
passed to the hooking modules

The allowed key combinations so far are:
    ! " # $ % & ' ( ) *
    + , - . / 0 1 2 3 4
    5 6 7 8 9 : ; < = >
    ? @ [ \ ] ^ _ ` a b
    c d e f g h i j k l
    m n o p q r s t u v
    w x y z A B C D E F
    G H I J K L M N O P
    Q R S T U V W X Y Z
    { | } ~ LCtrl RCtrl
    LShift RShift LAlt
    RAlt Tab Return Caps
    Windows Up Down Left
    Right Space WKey 

Some of these will be converted to their shift values instead, i.e.
    B --> LShift b
"""

supported_keys = [
 '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
 '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>',
 '?', '@', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'LCtrl', 'RCtrl', 'LShift', 'RShift',
 'LAlt', 'RAlt', 'Tab', 'Return', 'Up', 'Down', 'Left', 'Right', "Esc",
 'Space', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11',
 'F12', 'PrtSc']

# These keys should be supported in the future but are not currently since we
# don't know their codes
to_support = [
    'Cap', 'PgUp', 'PgDn', 'Pause', 'Delete', 'Ins', 'Home', 'End', 'NumLock'
]


shift_table = {
    'A' : 'A', 'B' : 'B', 'C' : 'C', 'D' : 'D', 'E' : 'E', 'F' : 'F', 'G' : 'G',
    'H' : 'H', 'I' : 'I', 'J' : 'J', 'K' : 'K', 'L' : 'L', 'M' : 'M', 'N' : 'N',
    'O' : 'O', 'P' : 'P', 'Q' : 'Q', 'R' : 'R', 'S' : 'S', 'T' : 'T', 'U' : 'U',
    'V' : 'V', 'W' : 'W', 'X' : 'X', 'Y' : 'Y', 'Z' : 'Z', '~' : '`', '!' : '1',
    '@' : '2', '#' : '3', '$' : '4', '%' : '5', '^' : '6', '&' : '7', '*' : '8',
    '(' : '9', ')' : '0', '_' : '-', '+' : '=', '{' : '[', '}' : ']', '|' : '\\',
    ':' : ';', '"' : '\'', '<' : ',', '>' : '.', '?' : '/'}


class KeyConverter(object):
    """
    Class for converting keys correctly
    """
    def __init__(self):
        self.supported_keys = supported_keys
        self.shift_table = shift_table
        self.special_key_table = {}


    def convert_keys(self, keys_list):
        """
        Changes the keys in keys_list to the right format for the hook

        :param keys_list: the list of keys to change to the right format
        :return: the list converted to the correct format
        """
        new_keys_list = []
        for i in range(len(keys_list)):
            key = keys_list[i]
            if key in self.shift_table:
                new_keys_list.extend(
                    [self.special_key_table["LShift"], self.shift_table[key]])

            elif key in self.special_key_table:
                new_keys_list.append(self.special_key_table[key])

            elif key in self.supported_keys:
                if (len(key) == 1):
                    if key.islower():
                        key = key.upper()
                        new_keys_list.append(key)
                    else:
                        if "LShift" not in new_keys_list:
                            new_keys_list.extend(["LShift", key])
                        else:
                            new_keys_list.append(key)
                else:
                    new_keys_list.append(key)

            else:
                raise ValueError("The key {0} is not supported".format(key))
        return new_keys_list


class WindowsKeyConverter(KeyConverter):
    """
    Class for converting keystrokes from Windows
    """
    def __init__(self):
        super().__init__()
        self.supported_keys.append("Windows")
        self.special_key_table = {
            "LShift" : "LShift", "RShift" : "RShift", "LCtrl" : "LCtrl",
            "RCtrl" : "RCtrl", "LAlt" : "LAlt", "RAlt" : "RAlt"
            }
