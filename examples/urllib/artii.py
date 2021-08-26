import urllib.request

url = 'http://artii.herokuapp.com/make?text=ASCII+Art'
with urllib.request.urlopen(url) as res:
    s = res.read()
print(s.decode('utf-8'))

