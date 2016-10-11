# -*- coding: utf-8 -*-

from base import ObjectBase

class HostDetailSource(ObjectBase):
    _member1 = ()
    _member2 = ('type', 'name', 'description')

    def __init__(self, param={}, debug=False):
        super(HostDetailSource, self).__init__(param, debug)
        if debug: self.check_keyword(param)

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self._name)


if __name__ == '__main__':
    x = HostDetailSource( {'type':'1','name':'2','other':'o'} )
    print( str(x) )
    print( repr(x) )
    print( x.type )
    print( x.name )
    print( x.description )

