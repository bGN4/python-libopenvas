# -*- coding: utf-8 -*-

from base import ObjectBase

class NVT(ObjectBase):
    _member1 = ('oid',)
    _member2 = ('name', 'cve', 'bid', 'xref', 'tags', 'family', 'cvss_base', 'risk_factor', 'cert')

    def __init__(self, param={}, debug=False):
        super(NVT, self).__init__(param, debug)
        if debug: self.check_keyword(param)

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self._oid)


if __name__ == '__main__':
    x = NVT( {'@oid':'1','name':'n','other':'o'} )
    print( str(x) )
    print( repr(x) )
    print( x.oid )
    print( x.name )
    print( x.cve )
    print( x.bid )
    print( x.xref )
    print( x.tags )
    print( x.family )
    print( x.cvss_base )
    print( x.risk_factor )
