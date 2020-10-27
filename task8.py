a = input('sadas')
if len(a) == 2:
    print(a[0:2])
elif len(a) < 2:
    print(Error)
else:
    print(a[0:2] + a[-2:])