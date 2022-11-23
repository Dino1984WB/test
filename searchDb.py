#search for a name
import initConn as iC
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=iC.engine)
session = Session()

#do some sql to search the table for the name type in

