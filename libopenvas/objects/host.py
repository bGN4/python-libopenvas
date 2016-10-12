# -*- coding: utf-8 -*-

import datetime
from base import ObjectBase
from detail import HostDetail


def parse_time(t):
    ret = None
    try:
        ret = datetime.datetime.strptime(t, '%Y-%m-%dT%H:%M:%SZ') + datetime.timedelta(hours=8)
    except ValueError:
        try: ret = datetime.datetime.strptime(t, '%Y-%m-%dT%H:%M:%S+08:00')
        except: ret = None
    except:
        ret = None
    return ret

def calc_cost(start, end):
    stm = parse_time(start)
    etm = parse_time(end)
    try:
        during = (etm-stm)
        (h, s) = divmod(during.seconds, 3600)
        (m, s) = divmod(s, 60)
        h = during.days * 24 + h
        cost = during.seconds + during.days * 24 * 3600 # '{:04}:{:02}:{:02}'.format(h, m, s)
    except:
        cost = -1 # '9999:59:59'
    return (stm if isinstance(stm, datetime.datetime) else None, 
            etm if isinstance(etm, datetime.datetime) else None, cost)


class HostTime(ObjectBase):
    _member1 = ()
    _member2 = ('host',)

    def __init__(self, param={}, debug=False):
        super(HostTime, self).__init__(param, debug)
        self._action = param['action']
        try:
            self._time = param['#text']
        except KeyError:
            self._time = None
        if debug: self.check_keyword(param, ('#text','action'))

    def __repr__(self):
        return '<%s%s: %s>' % (self.__class__.__name__, self._action.capitalize(), self._host)

    @property
    def time(self):
        return self._time

    @property
    def action(self):
        return self._action


class Host(ObjectBase):
    _member1 = ()
    _member2 = ('ip', 'start', 'end', 'host_start', 'host_end', 'status', 'route', 'ports')

    def __init__(self, param={}, debug=False):
        super(Host, self).__init__(param, debug)
        try:
            detail_list = [param['detail'],] if isinstance(param['detail'], dict) and param['detail'].has_key('name') else param['detail']
            self.detail_list = [HostDetail(detail, debug) for detail in detail_list]
        except KeyError:
            self.detail_list = []
        if debug: self.check_keyword(param, ('detail',))
        self._calc_cost()

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self._ip)

    def _calc_cost(self):
        (st, et, self.cost) = calc_cost(self._start, self._end)
        if st is not None: self._start = st
        if et is not None: self._end = et


if __name__ == '__main__':
    x = Host( {'ip':'1','end':'e','other':'o','detail':[{'name':'n'},]} )
    print( str(x) )
    print( repr(x) )
    print( x.ip )
    print( x.start )
    print( x.end )
    print( x.host_start )
    print( x.host_end )
    print( x.detail_list )
    x = HostTime( {'host':'h','#text':'t','action':'start'}, True )
    print( str(x) )
    print( repr(x) )
    print( x.host )
    print( x.time )

