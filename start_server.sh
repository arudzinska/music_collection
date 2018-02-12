#!/bin/bash
# Creates a database and runs the local server

touch /tmp/mydatabase.db;
python -c 'from app import db; db.create_all()';
python run.py
