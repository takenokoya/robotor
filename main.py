import csv

import termcolor

while True:
    s = '''\
    #################################################
    こんにちは!私はRobokoです。あなたの名前は何ですか?
    #################################################
    '''
    print(termcolor.colored(s, 'green'))
    name = input(str)
    if name != '':
        s = '''\
        #################################################
        {}さん。どこのレストランが好きですか?
        #################################################
        '''
        print(termcolor.colored(s.format(name), 'green'))
        answer = input(str).title()
        if answer != '':
            s = '''\
            #################################################
            {}さん。ありがとうございました。良い一日を!さようなら。
            #################################################
            '''
            print(termcolor.colored(s.format(name), 'green'))
            break
