import datetime
import os
import tempfile

data = []

with open('usage') as f:
    for line in f:
        line = line.split()
        date = datetime.datetime.strptime(line[0], '%Y-%m-%d').date()
        d1 = float(line[1])
        d2 = float(line[2])
        data.append((date, d1, d2))

with tempfile.NamedTemporaryFile(mode='w', dir=os.path.dirname(__file__), delete=False) as f:
    for start, end in zip(data,data[1:]):
        days = (end[0] - start[0]).days
        for n in range(days):
            date = start[0] + datetime.timedelta(days=n)
            delta1 = (end[1] - start[1]) / days
            delta2 = (end[2] - start[2]) / days
            print(date, delta1, delta2, file=f)
    f.close()
    os.replace(f.name, 'data')
