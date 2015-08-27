#-*-coding: utf-8 -*-
height = 1.75
weight = 80.5
if weight/(height*height)<18.5:
    print('过轻')
elif weight/(height*height)<25:
    print('正常')
elif weight/(height*height)<28:
    print('过重')
elif weight/(height*height)<32:
    print('肥胖')
else weight/(height*height)>32:
    print('严重肥胖')
 