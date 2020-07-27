import app
import json
import urllib.request

urlData = "http://jsonplaceholder.typicode.com/todos/1"
webURL = urllib.request.urlopen(urlData)
data_ = webURL.read()
encoding = webURL.info().get_content_charset('utf-8')
r2 = json.loads(data_.decode(encoding))

app.getAllData(r2)