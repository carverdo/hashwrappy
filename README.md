# hashwrappy
This package is a python wrapper for hashcat, allowing our user the 
ability to interact with the hashcat cmd line via python.

Hashcat lives here: https://hashcat.net/oclhashcat/

And that url (especially the wiki) is by far the best place to learn 
more about how it operates. Briefly however, hashcat helps crack 
hashed passwords (but you wouldn't be here unless you knew that).

## CREDITS (WHERE CREDITS DUE)
This code is a reworking of the code found here:
https://github.com/Rich5/pyHashcat

Some years ago Rich5 wrote `pyHashcat` to serve much the same purpose
as hashwrappy. That underlying code was re-built in order to make 
hashwrappy more functionally-oriented.

## ABOUT THE CODE / STRUCTURE
There are two main flavours of hashcat, where it operates via CPU or 
by GPU (hereafter labelled _hc or _ocl respectively in python files).

### config
`config.py` contains base variables mapping directly to hashcat; 
this file is modified by the `config_hc.py` and `config_ocl.py`.

`resets.py` sets a block of base hashcat variables, and is similarly 
modified by `resets_hc.py` and `resets_ocl.py`.

`msgs.py` is just a list of tailorable msgs.

### hashwrappy
`wrapper.py` has two main classes, `Vars`, and `Backbone` (which inherits 
Vars). Vars captures our earlier referenced config vars, and is
packaged into Backbone which holds a series of helper functions for our
two main classes -

`wrapper_hc.py` contains `HCWrapper` the main class to operate hashcat 
in its CPU format.

`wrapper_ocl.py` contains `OCLWrapper` the main class to operate 
hashcat in its GPU format.

## SETUP



## CONTACT
Please send bug reports, patches, and other feedback via github.
