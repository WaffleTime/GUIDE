# This file is generated by objective.metadata
#
# Last update: Wed Sep 19 17:27:15 2012

import objc, sys

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
constants = '''$$'''
enums = '''$$'''
misc.update({})
functions={'DCSDictionaryGetTypeID': (b'l', '', {'comment': 'Function not present in header files'}), 'DCSGetTermRangeInString': (sel32or64(b'{_CFRange=ll}^{__DCSDictionary=}^{__CFString=}l', b'{_CFRange=qq}^{__DCSDictionary=}^{__CFString=}l'),), 'DCSCopyTextDefinition': (sel32or64(b'^{__CFString=}^{__DCSDictionary=}^{__CFString=}{_CFRange=ll}', b'^{__CFString=}^{__DCSDictionary=}^{__CFString=}{_CFRange=qq}'), '', {'retval': {'already_retained': True, 'already_cfretained': True}})}
cftypes=[('DCSDictionaryRef', b'^{__DCSDictionary=}', 'DCSDictionaryGetTypeID', None)]
expressions = {}

# END OF FILE
