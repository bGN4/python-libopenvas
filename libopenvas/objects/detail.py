# -*- coding: utf-8 -*-

from base import ObjectBase
from source import HostDetailSource

class HostDetail(ObjectBase):
    _member1 = ()
    _member2 = ('name', 'value', 'extra')

    def __init__(self, param={}, debug=False):
        super(HostDetail, self).__init__(param, debug)
        try:
            self._source = HostDetailSource(param['source'], debug)
        except KeyError:
            self._source = None
        if debug: self.check_keyword(param, ('source',))

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self._name)

    @property
    def source(self):
        return self._source


if __name__ == '__main__':
    x = HostDetail( {'name':'n','value':'0','other':'o','source':{'name':'s'}} )
    print( str(x) )
    print( repr(x) )
    print( x.name )
    print( x.value )
    print( x.source )

