# Nasi Goreng
# https://lifestyle.kompas.com/read/2015/03/19/071000823/Menilik.Kandungan.Kalori.Menu.Sarapan.Orang.Indonesia?page=all#:~:text=Kandungan%20gizi%20%3A%20Tiap%201%20porsi%20(149%20gr)%20nasi%20goreng,dan%209%2C39%20g%20protein.
# Telur Dadar
# https://www.google.com/search?safe=strict&source=hp&ei=7B2fX5WEENre9QOj3biQBQ&q=kandungan+gizi+pada+telur+dadar&oq=nutrisi+pada+telur+dad&gs_lcp=CgZwc3ktYWIQAxgAMgkIABDJAxAWEB46CAgAELEDEMkDOggIABCxAxCDAToICC4QsQMQgwE6AggAOgUIABCxAzoICC4QxwEQrwE6AgguOhEILhCxAxDHARCjAhDJAxCTAjoLCC4QsQMQxwEQowI6BQgAEMkDOgYIABAWEB46CAgAEBYQChAeUOwFWOczYLVBaABwAHgAgAFfiAHhDZIBAjIymAEAoAEBqgEHZ3dzLXdpeg&sclient=psy-ab
# Timun
# https://www.sehatq.com/artikel/aneka-manfaat-timun-untuk-kesehatan

def Kalori(jenis, sisa):
    sisa = int(sisa)
    if jenis == 'Nasi Goreng':
        kalori = 1.6779
    elif jenis == 'Timun':
        kalori = 0.15
    elif jenis == 'Telur Dadar':
        kalori = 1.53
    else:
        kalori = 0
    return sisa*kalori

def Karbohidrat(jenis, sisa):
    sisa = int(sisa)
    if jenis == 'Nasi Goreng':
        karbo = 0.2106
    elif jenis == 'Timun':
        karbo = 0.0367
    elif jenis == 'Telur Dadar':
        karbo = 0.006
    else:
        karbo = 0
    return sisa*karbo

def Protein(jenis, sisa):
    sisa = int(sisa)
    if jenis == 'Nasi Goreng':
        prot = 0.063
    elif jenis == 'Timun':
        prot = 0.0067
    elif jenis == 'Telur Dadar':
        prot = 0.11
    else:
        prot = 0
    return sisa*prot

def Lemak(jenis, sisa):
    sisa = int(sisa)
    if jenis == 'Nasi Goreng':
        lemak = 0.0623
    elif jenis == 'Telur Dadar':
        lemak = 0.12
    else:
        lemak = 0
    return sisa*lemak