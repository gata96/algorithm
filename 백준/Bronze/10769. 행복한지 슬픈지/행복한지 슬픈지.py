say = input()
cnt_h = say.count(':-)')
cnt_s = say.count(':-(')

if cnt_h > cnt_s:
    print('happy')
elif cnt_h < cnt_s:
    print('sad')
elif cnt_s == cnt_h == 0:
    print('none')
elif cnt_s == cnt_h:
    print('unsure')