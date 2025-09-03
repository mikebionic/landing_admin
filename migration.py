# -*- coding: utf-8 -*-
import json, uuid, os
from main import db, create_app
from main.models import (
	User,
	Page,
	Category,
	Collection,
	Image,
	Contact,
	Media
)

from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine
from main.config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

if not database_exists(engine.url):
    create_database(engine.url)
    print(f"✅ Database {engine.url.database} created.")
else:
    print(f"ℹ️ Database {engine.url.database} already exists.")
    
    
app_migration_file = "docs/app.migration.json"
example_migration_file = "docs/example.migration.json"

if os.path.exists(app_migration_file):
    migration_file = app_migration_file
else:
    migration_file = example_migration_file
    print(f"⚠️ {app_migration_file} not found. Using {example_migration_file} instead.")

with open(migration_file, "r", encoding="utf-8") as f:
    migration_data = json.load(f)

app = create_app()
app.app_context().push()

db.drop_all()
db.create_all()

for item in migration_data["user"]:
	item['guid'] = uuid.uuid4()
	this_model = User(**item)
	db.session.add(this_model)

for item in migration_data["page"]:
	item['guid'] = uuid.uuid4()
	this_model = Page(**item)
	db.session.add(this_model)

db.session.commit()

for item in migration_data["category"]:
	item['guid'] = uuid.uuid4()
	this_model = Category(**item)
	db.session.add(this_model)

for item in migration_data["collection"]:
	item['guid'] = uuid.uuid4()
	this_model = Collection(**item)
	db.session.add(this_model)

for item in migration_data["image"]:
	item['guid'] = uuid.uuid4()
	this_model = Image(**item)
	db.session.add(this_model)


for item in migration_data["contact"]:
	item['guid'] = uuid.uuid4()
	this_model = Contact(**item)
	db.session.add(this_model)


for item in migration_data["media"]:
	item['guid'] = uuid.uuid4()
	this_model = Media(**item)
	db.session.add(this_model)

db.session.commit()