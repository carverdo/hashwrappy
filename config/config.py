#!/usr/bin/env python
# coding=utf-8
"""
Base dictionaries/lists to be used, and modified, in our wrapper classes.
"""
__author__ = 'donal'
__project__ = 'hashwrappy'

HASH_TYPE_DICT = {
    'MD5': '0',
    'md5($pass.$salt)': '10',
    'md5($salt.$pass)': '20',
    'md5(unicode($pass).$salt)': '30',
    'md5($salt.unicode($pass))': '40',
    'HMAC-MD5 (key = $pass)': '50',
    'HMAC-MD5 (key = $salt)': '60',
    'SHA1': '100',
    'sha1($pass.$salt)': '110',
    'sha1($salt.$pass)': '120',
    'sha1(unicode($pass).$salt)': '130',
    'sha1($salt.unicode($pass))': '140',
    'HMAC-SHA1 (key = $pass)': '150',
    'HMAC-SHA1 (key = $salt)': '160',
    'sha1(LinkedIn)': '190',
    'phpass': '400',
    'MD5(Wordpress)': '400',
    'MD5(phpBB3)': '400',
    'md5crypt': '500',
    'Cisco-IOS MD5': '500',
    'MD5(Unix)': '500',
    'FreeBSD MD5': '500',
    'MD4': '900',
    'NTLM': '1000',
    'mscash': '1100',
    'Domain Cached Credentials:': '1100',
    'SHA256': '1400',
    'sha256($pass.$salt)': '1410',
    'sha256($salt.$pass)': '1420',
    'sha256(unicode($pass).$salt)': '1430',
    'sha256($salt.unicode($pass))': '1440',
    'md5apr1': '1600',
    'SHA512': '1700',
    'sha512($pass.$salt)': '1710',
    'sha512($salt.$pass)': '1720',
    'sha512($salt.unicode($pass))': '1740',
    'sha512(unicode($pass).$salt)': '1730',
    'sha512crypt, SHA512(Unix)': '1800',
    'Cisco-PIX MD5': '2400',
    'WPA/WPA2': '2500',
    'Double MD5': '2600',
    'bcrypt': '3200',
    'Blowfish(OpenBSD)': '3200',
    'md5($salt.md5($pass))': '3710',
    'md5(sha1($pass))': '4400',
    'Double SHA1': '4500',
    'sha1(md5($pass))': '4700',
    'MD5(Chap)': '4800',
    'SHA-3(Keccak)': '5000',
    'Half MD5': '5100',
    'Password Safe SHA-256': '5200',
    'IKE-PSK MD5': '5300',
    'IKE-PSK SHA1': '5400',
    'NetNTLMv1+ESS': '5500',
    'NetNTLMv1-VANILLA': '5500',
    'NetNTLMv2': '5600',
    'Cisco-IOS SHA256': '5700',
    'Samsung Android Password/PIN': '5800',
    'AIX {smd5}': '6300',
    'AIX {ssha256}': '6400',
    'AIX {ssha512}': '6500',
    'AIX {ssha1}': '6700',
    'Lastpass': '6800',
    'GOST R 34.11-94': '6900',
    'OSX v10.8 / v10.9': '7100',
    'GRUB 2': '7200',
    'IPMI2 RAKP HMAC-SHA1': '7300',
    'SHA256(Unix)': '7400',
    'sha256crypt': '7400',
    'Redmine Project Management Web App': '7600',
    'HMAC-SHA256 (key = $pass)': '1450',
    'HMAC-SHA256 (key = $salt)': '1460',
    'MD5(APR)': '1600',
    'Apache MD5': '1600',
    'HMAC-SHA512 (key = $pass)': '1750',
    'HMAC-SHA512 (key = $salt)': '1760',
    'Joomla': '11',
    'osCommerce, xt:Commerce': '21',
    'nsldap, SHA-1(Base64), Netscape LDAP SHA': '101',
    'nsldaps, SSHA-1(Base64), Netscape LDAP SSHA': '111',
    'Oracle 11g': '112',
    'SMF > v1.1': '121',
    'OSX v10.4, v10.5, v10.6': '122',
    'MSSQL(2000)': '131',
    'MSSQL(2005)': '132',
    'EPiServer 6.x < v4': '141',
    'EPiServer 6.x > v4': '1441',
    'SSHA-512(Base64), LDAP {SSHA512}': '1711',
    'OSX v10.7': '1722',
    'MSSQL(2012)': '1731',
    'vBulletin < v3.8.5': '2611',
    'vBulletin > v3.8.5': '2711',
    'IPB2+, MyBB1.2+': '2811'
}
CMD_SHORT_SWITCH = {
    'attack-mode': 'a',
    'custom-charset1': '1',
    'custom-charset2': '2',
    'custom-charset3': '3',
    'custom-charset4': '4',
    'generate-rules': 'g',
    'hash-type': 'm',
    'help': 'h',
    'outfile': 'o',
    'segment-size': 'c',
    'separator': 'p',
    'version': 'V'
}
CMD_EQUAL_REQUIRED = [
    'debug-file',
    'debug-mode',
    'generate-rules-func-max',
    'generate-rules-func-min',
    'generate-rules-seed',
    'outfile-check-dir',
    'outfile-format'
]
IGNORE_VARS = [
    'argv',
    'bits',
    'charset_file',
    'cmd_equal_required',
    'defaults',
    'hash_file',
    'hash_type',
    'mask',
    'masks_file',
    'rules_files',
    'safe_dict',
    'words_files'
]
