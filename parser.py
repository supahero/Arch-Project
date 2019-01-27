import requests, re

names = ['CXBW.TXT', 'VEBD.TXT', 'KJKL.TXT', 'KPXE.TXT', 'CYKO.TXT', 'KGWB.TXT', 'ENHK.TXT', 'CWVQ.TXT', 'KSAZ.TXT',
         'EGGD.TXT', 'FOOG.TXT',
         'KQDM.TXT', 'KHNR.TXT', 'LKVO.TXT', 'LJPZ.TXT', 'KBPI.TXT', 'SBPC.TXT', 'SBSG.TXT', 'SBCC.TXT', 'KPRB.TXT',
         'KSAW.TXT',
         'URMT.TXT', 'KRWF.TXT', 'K7BM.TXT', 'KEKO.TXT', 'SBBI.TXT', 'KVQQ.TXT', 'KMFD.TXT', 'KMTN.TXT', 'K79J.TXT']

# get info from resourse
parsed_array = []
for x in names:
    r = requests.get('http://tgftp.nws.noaa.gov/data/observations/metar/decoded/%s' % names[names.index(x)])
    parsed_array.append(r.text)

taggedlist = []
for x in parsed_array:
    block = re.sub(r"\n", r"\nDate: ", parsed_array[parsed_array.index(x)],
                   count=1)  # find newline and add the str below once
    block = "Name: " + block
    taggedlist.append(block)

namedlist = []
for x in taggedlist:
    block = "\n--------"
    block = taggedlist[taggedlist.index(x)] + block
    namedlist.append(block)

readylist = []
for x in range(len(namedlist)):
    list = namedlist[x].split('\n')
    readylist.append(list)

readydict = dict(zip(names, readylist))

#return names, list, readydict
