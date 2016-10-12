# -*- coding: utf-8 -*-

import os
import time
import logging
import traceback
import xmltodict
from objects.report import Report

class OpenVASParser(object):

    @classmethod
    def parse_fromdict(cls, root):
        try:
            root_node = root['report']
        except KeyError:
            root_node = root['get_reports_response']['report']
        report_node = root_node['report']
        return Report(report_node, False)

    @classmethod
    def parse(cls, data=None, ext='xml'):
        obj = None
        if ext == 'dict':
            obj = cls.parse_fromdict( data )
        elif ext == 'xml':
            stime = time.time()
            obj = cls.parse_fromdict( xmltodict.parse( data ) )
            etime = time.time()
            obj.loadtime = int(1000*(etime-stime))
        else:
            raise TypeError("Unknown data type provided.")
        return obj

    @classmethod
    def parse_fromfile(cls, path, ext='xml'):
        try:
            with open(path, 'r') as fp:
                ret = cls.parse(fp.read(), ext)
        except IOError:
            raise
        return ret


if __name__ == '__main__':
    obj = OpenVASParser.parse_fromfile('../test.xml')
    print( getattr(obj, 'loadtime', None) )
    for h in obj.host_list:
        try:
            print( '{}: ({}ms, {}, {})'.format(h, h.cost, h.status, len(h.detail_list)) )
            print( 'route: {}'.format(h.route) )
            print( 'ports: {}'.format(h.ports) )
        except Exception as e:
            raise

