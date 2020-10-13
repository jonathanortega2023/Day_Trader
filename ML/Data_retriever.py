import sqlalchemy as sqla, numpy as np
from sqlalchemy import create_engine, Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy.util.langhelpers import symbol
import datetime as dt
import csv
engine = create_engine("mysql://jon:password@localhost/data", echo=True)
Session = sessionmaker(bind=engine,autoflush=False)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

#Defining table scheme
from sqlalchemy import Column, Integer, Float, String, DATETIME
class Stock(Base):
    __tablename__ = "stocks"
    ID = Column(Integer ,primary_key = True)
    symbol = Column(String(5))
    name = Column(String(50))
    price = Column(Float)
    date_time = Column(DATETIME)

    def __repr__(self):
        return "<Stock(ID = '%s', symbol='%s', name='%s', price='%s', date_time='%s')>" % (self.ID, self.symbol, self.name, self.price, self.date_time)

Base.metadata.create_all(engine)
sess = Session()

#Reading file
with open('/home/jon/Downloads/QTUM.csv', newline = '') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        sess.add(Stock(symbol = "QTUM", name = "Defiance Quantum ETF", price = row[1], date_time = row[0]))
    sess.commit()
