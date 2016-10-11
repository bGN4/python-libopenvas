# -*- coding: utf-8 -*-

import re
from base import ObjectBase
from nvt import NVT

def parse_vas_port(port_s):
    port_l = port_s.split()
    res1   = re.match('\(?(\d+)/([\w-]+)\)?', port_s)
    res2   = re.match('(\S+)\s\(?(\d+)/([\w-]+)\)?', port_s)
    if   len(port_l)==1 and port_s.count('/')==1 and res1 is not None:
        (port,service,protocol) = (res1.group(1), '', res1.group(2))
    elif len(port_l)==2 and port_s.count('/')==1 and res2 is not None:
        (port,service,protocol) = (res2.group(2), res2.group(1), res2.group(3))
    else:
        (port,service,protocol) = (-1, port_s, port_s)
    return (port, service, protocol)

class Result(ObjectBase):
    _member1 = ('id',)
    _member2 = ('name', 'comment', 'host', 'port', 'risk_factor', 'threat', 'original_threat', 'severity', 'original_severity', 'description', 'creation_time', 'modification_time', 'scan_nvt_version', 'notes', 'overrides')

    def __init__(self, param={}, debug=False):
        super(Result, self).__init__(param, debug)
        try:
            self._nvt = NVT(param['nvt'], debug)
        except KeyError:
            self._nvt = None
        if debug: self.check_keyword(param, ('nvt',)+('owner','qod','user_tags','detection'))
        self._split_port()

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self._id)

    def _split_port(self, port_s=None):
        (self._port,self._service,self._protocol) = parse_vas_port(port_s or self._port)

    @property
    def service(self):
        return self._service

    @property
    def protocol(self):
        return self._protocol

    @property
    def nvt(self):
        return self._nvt

    @property
    def risk_factor(self):
        return self._risk_factor if self._risk_factor is not None else self._original_threat


if __name__ == '__main__':
    x = Result( {'@id':'r1','name':'n','port':'23/tcp','other':'o','original_threat':'t','nvt':{'oid':'n1'}} )
    print( str(x) )
    print( repr(x) )
    print( x.id )
    print( x.name )
    print( x.host )
    print( x.port )
    print( x.service )
    print( x.protocol )
    print( x.nvt )
    print( x.risk_factor )
    print( x.description )
    print( x.creation_time )
    print( x.original_threat )
