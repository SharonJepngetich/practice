sh=input('Enter Hours: ')
sr=input('Enter Rate: ')
try:
    fh=float(sh)
    fr=float(sr)
except:
    print('Error, please enter numeric input')
    quit()
print(fh,fr)
if fh>40:
    reg=fr*fh
    otp=(fh-40.0)*(fr*.5)
    tp=reg+otp
else:
    tp=fh*fr
print('Pay:',tp)