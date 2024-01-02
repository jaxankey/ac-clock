import zipfile, os

path = os.path.join('assettocorsa','apps','python','ac-clock','ac-clock.py')

version = input('Version? ').strip()

zip_file = zipfile.ZipFile('ac-clock v'+version+'.zip', 'w')