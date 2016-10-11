# -*- coding: utf-8 -*-

from base import ObjectBase

class Task(ObjectBase):
    _member1 = ('id',)
    _member2 = ('name', 'comment', 'progress')

    def __init__(self, param={}, debug=False):
        super(Task, self).__init__(param, debug)
        try:
            self._target = param['target']['@id']
        except KeyError:
            self._target = None
        if debug: self.check_keyword(param, ('target',)+('user_tags',))

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self._id)

    @property
    def target(self):
        return self._target


if __name__ == '__main__':
    x = Task( {'@id':'1','name':'n','other':'o','target':{'@id':'000'}} )
    print( str(x) )
    print( repr(x) )
    print( x.id )
    print( x.name )
    print( x.comment )
    print( x.progress )
    print( x.target )

