import app

with open('data_file.json', 'r') as read_file:
	data = json.load(read_file)

app.getAllData(data)