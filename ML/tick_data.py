import sqlalchemy, time
from sqlalchemy import create_engine, Sequence, \
Column, Integer, Float, String, DATETIME
from sqlalchemy.orm import sessionmaker
from sqlalchemy.util.langhelpers import symbol
import datetime as dt
import csv
engine = create_engine("mysql://jon:Linkssbb1!@localhost/data", echo=True)
Session = sessionmaker(bind=engine,autoflush=False)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

#Defining table scheme
class IVE_Stock(Base):
    __tablename__ = "IVE"
    symbol = Column(String(5))
    price = Column(Float)
    bid = Column(Float)
    ask = Column(Float)
    date_time = Column(DATETIME, primary_key = True)
    size = Column (Integer)

    def __repr__(self):
        return "<IVE_Stock(ID = '%s', symbol='%s', name='%s', price='%s', date_time='%s', ask='%s', bid='%s')>" \
            % (self.ID, self.symbol,  self.price, self.date_time, self.ask, self.bid)

class WDC_Stock(Base):
    __tablename__ = "WDC"
    symbol = Column(String(5))
    price = Column(Float)
    bid = Column(Float)
    ask = Column(Float)
    date_time = Column(DATETIME, primary_key = True)
    size = Column (Integer)

    def __repr__(self):
        return "<WDC_Stock(ID = '%s', symbol='%s', name='%s', price='%s', date_time='%s', ask='%s', bid='%s')>" \
            % (self.ID, self.symbol,  self.price, self.date_time, self.ask, self.bid)

Base.metadata.create_all(engine)
sess = Session()

#Reading file
with open('/home/jon/Downloads/IVE_tickbidask.txt', newline = '') as IVE_tickbidask:
    IVE_reader = csv.reader(IVE_tickbidask)
    row1 = next(IVE_reader)
    temp = dt.datetime.combine(dt.datetime.strptime(row1[0], '%m/%d/%Y'), dt.datetime.strptime(row1[1], '%H:%M:%S').time())
    sess.add(IVE_Stock(symbol = "IVE",  date_time = temp, price = row1[2], bid = row1[3], ask = row1[4], size = row1[5]))
    sess.commit()
    for row in IVE_reader:
        if(dt.datetime.combine(dt.datetime.strptime(row[0], '%m/%d/%Y'), dt.datetime.strptime(row[1], '%H:%M:%S').time()).__eq__(\
            temp)):
            #Add a line to alter previous entry to add number moved?
            continue
        else:
            temp = dt.datetime.combine(dt.datetime.strptime(row[0], '%m/%d/%Y'), dt.datetime.strptime(row[1], '%H:%M:%S').time())
            sess.add(IVE_Stock(symbol = "IVE",  date_time = temp, price = row[2], bid = row[3], ask = row[4], size = row[5]))
        sess.commit()
IVE_tickbidask.close

#with open('/home/jon/Downloads/WDC_tickbidask.txt', newline = '') as WDC_tickbidask:
#    WDC_reader = csv.reader(WDC_tickbidask)
 #   for row in WDC_reader:
   #     sess.add(WDC_Stock(symbol = "WDC",  date = row[0], time = row[1], price = row[2], bid = row[3],\
  #          ask = row[4], size = row[5]))
   # sess.commit()
#WDC_tickbidask.close