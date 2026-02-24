
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import app


engine = create_engine("sqlite:///db.library" , echo= True)
Session = sessionmaker(bind=engine) 
Base = declarative_base()


    