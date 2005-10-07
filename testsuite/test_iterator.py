# -*- Mode: Python -*-
# vi:si:et:sw=4:sts=4:ts=4
#
# Copyright (C) 2005 Johan Dahlin
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307  USA

import unittest
from common import gst, TestCase

class IteratorTest(TestCase):
    # XXX: This is busted. Testsuite or iterator bindings?
    def gcverify(self):
        pass
    
    # XXX: Elements
    
    def testIteratePadsFakeSrc(self):
        fakesrc = gst.element_factory_make('fakesrc')
        pads = list(fakesrc.pads())
        srcpad = fakesrc.get_pad('src')
        self.assertEqual(len(pads), 1)
        self.assertEqual(pads[0], srcpad)
        srcpads = list(fakesrc.src_pads())
        self.assertEqual(len(srcpads), 1)
        self.assertEqual(srcpads[0], srcpad)
        sinkpads = list(fakesrc.sink_pads())
        self.assertEqual(sinkpads, [])

        self.assertEqual(len(list(fakesrc)), 1)
        for pad in fakesrc:
            self.assertEqual(pad, srcpad)
            break
        else:
            raise AssertionError
        
    def testIteratePadsFakeSink(self):
        fakesink = gst.element_factory_make('fakesink')
        pads = list(fakesink.pads())
        sinkpad = fakesink.get_pad('sink')
        self.assertEqual(len(pads), 1)
        self.assertEqual(pads[0], sinkpad)
        srcpads = list(fakesink.src_pads())
        self.assertEqual(srcpads, [])
        sinkpads = list(fakesink.sink_pads())
        self.assertEqual(len(sinkpads), 1)
        self.assertEqual(sinkpads[0], sinkpad)

        self.assertEqual(len(list(fakesink)), 1)
        for pad in fakesink:
            self.assertEqual(pad, sinkpad)
            break
        else:
            raise AssertionError
    