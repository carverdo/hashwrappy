#!/usr/bin/env python
# coding=utf-8
"""
Modifying class for reset as used by our HC wrapper class.
the if __name__ == below just tests inheritance has worked.
"""
from resets import ResetVars
__author__ = 'donal'
__project__ = 'hashwrappy'


class HCResetVars(ResetVars):
    def __init__(self):
        super(HCResetVars, self).__init__()
        # diff dict vals
        self.outfile_format = 0
        self.segment_size = 32
        # new attrs
        self.stdout = False
        self.salt_file = None
        self.threads = 8
        self.words_skip = 0
        self.words_limit = 0
        self.toggle_min = 1
        self.toggle_max = 16
        self.pw_min = 1
        self.pw_max = 10
        self.perm_min = 2
        self.perm_max = 10
        self.table_min = 2
        self.table_max = 10
        self.default = None


if __name__ == '__main__':
    hrv = HCResetVars()
    print(hrv.separator)
    print(hrv.perm_max)
