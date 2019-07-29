import json
import datetime
from collections import OrderedDict

# print a formated time difference. yes, it has to be this long.
def print_date(date, temp=False):
    t_sum = datetime.timedelta(0)
    idx = range(len(data[date]))[::-1] # calculating indexes (e.g. 3, 2, 1, 0)
    for a, b in zip(idx[::2], idx[1::2]): # building pairs
        t_sum += (datetime.datetime.strptime(data[date][a], "%H:%M") - datetime.datetime.strptime(data[date][b], "%H:%M"))
    hh = str(t_sum).split(':')[0]
    mm = int(round(int(str(t_sum).split(':')[1])/60.0*100.0))
    hh_ = int(hh)
    mm_ = round(mm*4, -2)/4.0
    if mm_ == 100:
        mm_ = 0
        hh_ += 1
    hh_ = str(hh_)
    t = '*' if temp else ''
    print "\t"+t, d, " ", hh + "." + str(mm).rjust(2, '0') + " h \t => " + hh_ + "." + str(mm_).split('.')[0].rjust(2, '0')

# read ordered data
data = json.load(open('stamp.json'), object_pairs_hook=OrderedDict)
a = raw_input("\nWillkommen bei der Zeiterfassung!\n\n\tx stempeln\n\t  Zeit anzeigen\n")

# prepare timestamp
today = datetime.datetime.now().strftime("%Y-%m-%d")#.strftime("%d.%m.%Y")
t = datetime.datetime.now().strftime("%H:%M")

if a == 'x': # stamp
    if today in data.keys(): data[today].append(t)
    else: data[today] = [t]
    with open('stamp.json', 'w') as data_file:
        json.dump(data, data_file, sort_keys=True, indent=4)

print "Anwesenheitszeit:\n"
for date in data:
    d = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%d.%m.%Y")
    if str(date).split('-')[0] != datetime.datetime.now().strftime("%Y"): continue
    elif int(str(date).split('-')[1]) < int(datetime.datetime.now().strftime("%m"))-1: continue
    elif len(data[date]) % 2 == 1:
        if date == today:  # Adding temp. time stamp
            t = datetime.datetime.now().strftime("%H:%M")
            data[today].append(t)
            print_date(date, temp=True)
        else:
            print "\t", d, " ", len(data[date]), "Stempel"
    else:
        print_date(date)
print
