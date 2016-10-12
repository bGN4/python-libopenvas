# -*- coding: utf-8 -*-

from base import ObjectBase
from result import Result
from host import HostTime, Host
from task import Task

class Report(ObjectBase):
    loadtime = None
    _member1 = ('id',)
    _member2 = ('results', 'scan_start', 'scan_end', 'timezone', 'timezone_abbrev', 'timestamp', 'scan_start', 'scan_run_status')

    def __init__(self, param={}, debug=False):
        super(Report, self).__init__(param, debug)
        host_status = {}
        try:
            self._results = []
            for result in [param['results']['result'],] if isinstance(param['results']['result'], dict) else param['results']['result']:
                item = Result(result, debug)
                self._results.append( item )
                if item.name=='Ping Host'    and item.host_status: host_status.setdefault(item.host, dict(status='up',route=[],ports=''))['status'] = item.host_status
                if item.name=='Traceroute'   and item.trace_route: host_status.setdefault(item.host, dict(status='up',route=[],ports=''))['route']  = item.trace_route
                if item.name=='Host Summary' and item.open_port  : host_status.setdefault(item.host, dict(status='up',route=[],ports=''))['ports']  = item.open_port
        except KeyError:
            pass
        for action in ('start', 'end'):
            try:
                keyword = 'host_%s'%action
                setattr(self, 'host_%s_list'%action, [])
                setattr(self, 'host_%s_dict'%action, {})
                for host_action in [param[keyword],] if isinstance(param[keyword], dict) and param[keyword].has_key('host') else param[keyword]:
                    host_action['action'] = action
                    host_time = HostTime(host_action, debug)
                    getattr(self, 'host_%s_list'%action).append( host_time )
                    getattr(self, 'host_%s_dict'%action)[host_time.host] = host_time.time
            except KeyError:
                pass
        try:
            self.host_list = []
            self.host_dict = {}
            for host in [param['host'],] if isinstance(param['host'], dict) and param['host'].has_key('ip') else param['host']:
                ip = host.get('ip')
                if not ip: continue
                host_status.setdefault(ip, {}).update( dict(host_start=self.host_start_dict.get(ip), host_end=self.host_end_dict.get(ip)) )
                host.update( host_status[ip] )
                self.host_list.append( Host(host, debug) )
        except KeyError:
            pass
        try:
            self._task = Task(param['task'], debug)
        except KeyError:
            self.result_list = None
        try:
            self.omp_version = param['omp']['version']
        except KeyError:
            self.omp_version = None
        if debug: self.check_keyword(param, ('host','task','host_start','host_end')+('hosts','ports','filters','os','sort','errors','severity','severity_class','user_tags','result_count','ssl_certs','closed_cves','vulns','apps','scan','report_format','omp'))

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self._id)

    @property
    def results(self):
        return self._results

    @property
    def task(self):
        return self._task


if __name__ == '__main__':
    x = Report( {'@id':'1','other':'o','task':{'@id':'1','name':'n','other':'o','target':{'@id':'000'}},'results':{'result':[{'@id':'r1','name':'n','port':'23/tcp','other':'o','original_threat':'t','nvt':{'oid':'n1'}}]},'host':[{'ip':'1','end':'e','other':'o','detail':[{'name':'n'},]}]} )
    print( str(x) )
    print( repr(x) )
    print( x.id )
    print( x.scan_start )
    print( x.task )
    for s in x.results:
        print(s, s.nvt)
    for h in x.host_list:
        print(h, h.detail_list)
    

