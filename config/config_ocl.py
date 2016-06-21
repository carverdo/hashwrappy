#!/usr/bin/env python
# coding=utf-8
"""
Modifying dictionaries/lists for our OCL wrapper class.
"""
__author__ = 'donal'
__project__ = 'hashwrappy'

OCL_HASH_TYPE_DICT = {
    'MySQL323': '200',
    'MySQL4.1': '300',
    'MySQL5': '300',
    'descrypt': '1500',
    'DES(Unix)': '1500',
    'Traditional DES': '1500',
    'Cisco-ASA MD5': '2410',
    'Domain Cached Credentials2': '2100',
    'mscash2': '2100',
    'LM': '3000',
    'Oracle 7-10g': '3100',
    'DES(Oracle)': '3100',
    'iSCSI CHAP authentication': '4800',
    'RipeMD160': '6000',
    'Whirlpool': '6100',
    'TrueCrypt 5.0+ PBKDF2-HMAC-RipeMD160 (XTS AES)': '6211',
    'TrueCrypt 5.0+ PBKDF2-HMAC-SHA512 (XTS AES)': '6221',
    'TrueCrypt 5.0+ PBKDF2-HMAC-Whirlpool (XTS AES)': '6231',
    'TrueCrypt 5.0+ PBKDF2-HMAC-RipeMD160 + boot-mode (XTS AES)': '6241',
    'TrueCrypt 5.0+ PBKDF2-HMAC-RipeMD160 + hidden-volume (XTS AES)': '6251',
    'TrueCrypt 5.0+ PBKDF2-HMAC-SHA512 + hidden-volume (XTS AES)': '6261',
    'TrueCrypt 5.0+ PBKDF2-HMAC-Whirlpool + hidden-volume (XTS AES)': '6271',
    'TrueCrypt 5.0+ PBKDF2-HMAC-RipeMD160 + hidden-volume' +
    ' + boot-mode (XTS AES)': '6281',
    '1Password, agilekeychain': '6600',
    'Kerberos 5 AS-REQ Pre-Auth etype 23': '7500',
    'SAP CODVN B (BCODE)': '7700',
    'SAP CODVN F/G (PASSCODE)': '7800',
    'Drupal7': '7900',
    'Sybase ASE': '8000',
    'Citrix Netscaler': '8100',
    '1Password, cloudkeychain': '8200',
    'DNSSEC (NSEC3)': '8300',
    'WBB3, Woltlab Burning Board 3': '8400',
    'RACF': '8500',
    'Lotus Notes/Domino 5': '8600',
    'Lotus Notes/Domino 6': '8700',
    'Android FDE': '8800',
    'scrypt': '8900',
    'Password Safe v2': '9000',
    'Lotus Notes/Domino 8': '9100',
    'Juniper Netscreen/SSG (ScreenOS)': '22',
    'Skype': '23',
    'PeopleSoft': '133',
    'hMailServer': '1421',
    'MSSQL(2014)': '1731',
    'PHPS': '2612',
    'Mediawiki B type': '3711'
}
OCL_CMD_SHORT_SWITCH = {
    'benchmark': 'b',
    'gpu-accel': 'n',
    'gpu-devices': 'd',
    'gpu-loops': 'u',
    'increment': 'i',
    'limit': 'l',
    'markov-threshold': 't',
    'rule-left': 'j',
    'rule-right': 'k',
    'rules-file': 'r',
    'skip': 's',
    'workload-profile': 'w'
}
OCL_CMD_EQUAL_REQUIRED = [
    'benchmark-mode',
    'cpu-affinity',
    'gpu-temp-abort',
    'gpu-temp-retain',
    'increment-max',
    'increment-min',
    'induction-dir',
    'markov-hcstat',
    'markov-threshold',
    'remove-time',
    'restore-timer',
    'runtime',
    'session',
    'status-timer'
]
OCL_IGNORE_VARS = ['bits']
