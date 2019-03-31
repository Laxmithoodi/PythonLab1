from datetime import date

date1 = date(1901, 1, 1)
date2 = date(2000, 12, 31)

date1_ord = date1.toordinal()
date2_ord = date2.toordinal()
cnt = 0

for d_ord in range(date1_ord, date2_ord):
    d = date.fromordinal(d_ord)
    if (d.weekday() == 6) and (d.day == 1):
        cnt = cnt + 1

print("Number of Sunday 1'st days is {}".format(cnt))
