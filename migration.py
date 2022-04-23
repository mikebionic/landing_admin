from main import db, create_app
import json

f = open('docs/app.migration.json')
data = json.load(f)

#print(data)

app = create_app()
app.app_context().push()


db.drop_all()
db.create_all()