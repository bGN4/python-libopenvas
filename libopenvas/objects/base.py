# -*- coding: utf-8 -*-

__all__ = ['ObjectBase',]

def gen(name):
    def x(self): return getattr(self, '_%s'%name)
    return x

class ObjectMeta(type):
    def __new__(cls, name, bases=(object,), attrs={}):
        attributes = {}
        for mb in attrs.get('_member1',[])+attrs.get('_member2',[]):
            attributes[mb] = property( gen(mb) )
        attributes.update(attrs)
        return type.__new__(cls, name, bases, attributes)

class ObjectBase(object):

    __metaclass__ = ObjectMeta

    def __init__(self, param={}, debug=False):
        for mb in self._member1:
            setattr(self, '_%s'%mb, param.get(mb, param.get('@%s'%mb)))
        for mb in self._member2:
            setattr(self, '_%s'%mb, param.get(mb))

    def check_keyword(self, param, extra=()):
        other = [(k,param[k]) for k in set(param.iterkeys()) - set(map(lambda mb:'@%s'%mb, self._member1)) - set(self._member1+self._member2+extra)]
        if len(other)>0:
            print( other )


class ObjectTest(ObjectBase):
    _member1 = ('id',)
    _member2 = ('name', 'x')

    def __init__(self, param={}, debug=False):
        super(ObjectTest, self).__init__(param, debug)
        if debug: self.check_keyword(param)

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self._id)

    @property
    def x(self):
        return 'override'

if __name__ == '__main__':
    test = ObjectTest( {'@id':'1','name':'n','other':'o'} )
    print( str(test) )
    print( repr(test) )
    print( test.id )
    print( test.name )
    print( test.x )

