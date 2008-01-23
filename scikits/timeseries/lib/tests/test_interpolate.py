"""
:author: Pierre Gerard-Marchant & Matt Knox
:contact: pierregm_at_uga_dot_edu & mattknox_ca_at_hotmail_dot_com
:version: $Id: test_interpolate.py 3836 2008-01-15 13:09:03Z matthew.brett@gmail.com $
"""
__author__ = "Pierre GF Gerard-Marchant & Matt Knox ($Author: matthew.brett@gmail.com $)"
__version__ = '1.0'
__revision__ = "$Revision: 3836 $"
__date__     = '$Date: 2008-01-15 08:09:03 -0500 (Tue, 15 Jan 2008) $'

import numpy as N
import numpy.core.numeric as numeric

from scipy.testing import *

from numpy.ma.testutils import *
from numpy.ma import MaskedArray, masked

from scikits.timeseries.lib.interpolate import \
     backward_fill, forward_fill, interp_masked1d

class TestFuncs(TestCase):

    def __init__(self, *args, **kwds):
        TestCase.__init__(self, *args, **kwds)
        self.mask = [1,0,1,0,0,1,1,0,0,0]
        self.data = numeric.arange(10)
        self.test_array = masked_array(self.data, mask=self.mask)

    def test_backward_fill (self):
        result = masked_array(self.data, mask=self.mask)
        result[0] = 1
        result[2] = 3

        assert_equal(backward_fill(self.test_array, maxgap=1), result)

        result[5] = 7
        result[6] = 7

        assert_equal(backward_fill(self.test_array), result)

    def test_forward_fill (self):
        result = masked_array(self.data, mask=self.mask)
        result[2] = 1

        assert_equal(forward_fill(self.test_array, maxgap=1), result)

        result[5] = 4
        result[6] = 4

        assert_equal(forward_fill(self.test_array), result)

    def test_interp_fill(self):
        result_lin = masked_array(self.data).astype(float_)
        result_lin[0] = masked

        approx(interp_masked1d(self.test_array.astype(float_), kind='linear'), result_lin)

###############################################################################
#------------------------------------------------------------------------------
if __name__ == "__main__":
    nose.run(argv=['', __file__])
