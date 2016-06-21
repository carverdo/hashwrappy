#!/usr/bin/env python
# coding=utf-8
"""
Gathering up our namespaces so that we can import config, and reference
by config. in the wrapper class.
"""
import sys
from config import HASH_TYPE_DICT, CMD_SHORT_SWITCH, \
    CMD_EQUAL_REQUIRED, IGNORE_VARS
from config_hc import HC_HASH_TYPE_DICT, HC_CMD_SHORT_SWITCH, \
    HC_CMD_EQUAL_REQUIRED, HC_IGNORE_VARS
from config_ocl import OCL_HASH_TYPE_DICT, OCL_CMD_SHORT_SWITCH, \
    OCL_CMD_EQUAL_REQUIRED, OCL_IGNORE_VARS
from resets_hc import HCResetVars
from resets_ocl import OCLResetVars

ON_POSIX = 'posix' in sys.builtin_module_names
WALK_ROOT = 'c:/'
