# encoding: UTF-8

from __future__ import absolute_import
from vnpy.trader import vtConstant
from .korbitGateway import korbitGateway

gatewayClass = korbitGateway
gatewayName = 'KORBIT'
gatewayDisplayName = u'KORBIT'
gatewayType = vtConstant.GATEWAYTYPE_BTC
gatewayQryEnabled = True

