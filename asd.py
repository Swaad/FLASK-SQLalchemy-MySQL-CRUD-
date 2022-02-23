# from sqlalchemy import Column, Integer, Date, String, create_engine, DATETIME, TEXT
# from sqlalchemy.orm import declarative_base, sessionmaker
#
#
# from sqlalchemy import Column, Integer, String
# from sqlalchemy import create_engine
#
#
# # engine = create_engine('mysql+mysqlconnector://root:root#1234@localhost/test_scoring', echo=False)
# # from sqlalchemy.ext.declarative import declarative_base
#
# # Base = declarative_base()
#
#
#
#
#
#
# from sqlalchemy.orm import sessionmaker
#
# Session = sessionmaker(bind=engine)
# session = Session()
#
#
#
#
#
# if __name__ == '__main__':
#     import os
#     from urllib.parse import quote
#
#     # engine = create_engine('sqlite:///:database:', echo=False)
#     engine = create_engine('mysql+mysqlconnector://root:root#1234@localhost/test_scoring', echo=False)
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     Base.metadata.create_all(engine)