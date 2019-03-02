# coding=utf-8

import glob
import os
import sys
import subprocess
from urllib.request import urlretrieve
from urllib.parse import quote

# file download config
URL_BASE = 'https://aineistot.metsaan.fi/avoinmetsatieto/Metsavarakuviot/Maakunta/'
URL_FILES = [
    'MV_Etelä-Karjala.zip',
    'MV_Etelä-Pohjanmaa.zip',
    'MV_Etelä-Savo.zip',
    'MV_Kainuu.zip',
    'MV_Kanta-Häme.zip',
    'MV_Keski-Pohjanmaa.zip',
    'MV_Keski-Suomi.zip',
    'MV_Kymenlaakso.zip',
    'MV_Lappi_E.zip',
    'MV_Lappi_P.zip',
    'MV_Pirkanmaa.zip',
    'MV_Pohjanmaa.zip',
    'MV_Pohjois-Karjala.zip',
    'MV_Pohjois-Pohjanmaa.zip',
    'MV_Pohjois-Savo.zip',
    'MV_Päijät-Häme.zip',
    'MV_Satakunta.zip',
    'MV_Uusimaa.zip',
    'MV_Varsinais-Suomi.zip'
]

# progress hook for each download
def hook_progress(block_num, block_size, total_size):
    current_size = block_num * block_size
    status_str = 'unknown'
    if total_size > 0:
        percent = current_size / total_size
        status_str = 'progress: %.2f, current_size: %d MB, total_size: %d MB' % (percent, current_size / 1e6, total_size / 1e6)
    else:
        status_str = 'current_size: %d' % (current_size)
    print(status_str)

# download the files one by one
for x in URL_FILES:
    print('Starting to download ' + x)
    urlretrieve(URL_BASE + quote(x), './' + x, hook_progress)

# unzip all downloaded files
def func_unzip():
    print('Unzipping all downloaded .zip files...')
    with open('./7z.log', 'ab') as output:
        sp = subprocess.Popen(['7z', 'x', '*.zip', '-o./input/'], stderr=output, stdout=output)
        return sp.communicate()

func_unzip()

# merge all gpkg's to one
def func_merge(cmds):
    with open('./ogr2ogr.log', 'ab') as output:
        sp = subprocess.Popen(cmds, stderr=output, stdout=output)
        return sp.communicate()

for idx, val in enumerate(glob.iglob(os.path.join('./input', r'*.gpkg'))):
    print('Merging unzipped ' + val)
    if idx <= 0:
        func_merge(['ogr2ogr', '-f', 'GPKG', '-gt', '65536', './avoinkuviodata.gpkg', val])
    else:
        func_merge(['ogr2ogr', '-f', 'GPKG', '-gt', '65536', '-append', '-update', './avoinkuviodata.gpkg', val])

print('All done!')
