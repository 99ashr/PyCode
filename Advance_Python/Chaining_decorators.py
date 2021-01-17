#!/usr/bin/env python3

#* ---------------------------- Chaining Decorators --------------------------- #
def star(func):
    def inner(*args, **kwargs):
        print('*'*80)
        func(*args, **kwargs)
        print('*'*80)
    return inner


def percentage(func):
    def inner(*args, **kwargs):
        print('%'*80)
        func(*args, **kwargs)
        print('%'*80)
    return inner

# ---------------------------------------------------------------------------- #


@star
@percentage
def msg(msg):
    m = 80
    msg_len = len(msg)
    if msg_len % 2 == 0:
        tc = m-(msg_len+2)
        c = int(tc/2)
        print("-"*c, msg, "-"*c)
    else:
        tc = m-(msg_len+3)
        c = int(tc/2)
        print("-"*c, msg, "-"+"-"*c)


#@ -------------------- Calling decorated chained function -------------------- #
msg("Ashish")
msg("Shrankhla")
#* ------------------------------------ EOF ----------------------------------- #
