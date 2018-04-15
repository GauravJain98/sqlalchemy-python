from sqlalchemy import create_engine,Column,String

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os
db_url = "sqlite:///crud.sqlite"
engine = create_engine(db_url)

Base = declarative_base()

Session = sessionmaker()
Session.configure(bind=engine)
class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    quantity = Column(Integer)
    price = Column(Integer)


Base.metadata.create_all(bind=engine)
def add(number):
    session = Session()
    for i in range(1,number):
        product = Product()
        product.id = i
        product.name= 'name' + str(i)
        product.quantity= 3*(i%5 + 1)
        product.price= 30*(i%5 + 1)
        session.add(product)
        session.commit()
def view():
    session = Session()
    products = session.query(Product).all()
    for p in products:
       print(str(p.id) +". " + p.name + " at " + str(p.price) +"\n")

def generate(cart):
    os.system('cls')
    amount = 0
    print(" Name   Quantity  at   Amount")
    for q in cart:
        product,quantity = q
        quantity = int(quantity)
        print(product.name+ "   "+ str(quantity) +"      "+ str(product.price) + "      " + str(product.price*quantity))
        amount = amount + (product.price*quantity)
    print("Total Amount:"+str(amount))

def main():
    cart = []
    session = Session()
    want = True
    while(want):
        view()
        pid = input("Choose item to buy")
        os.system('cls')
        product = session.query(Product).filter(Product.id == pid).first()
        quantity = input("How many "+ product.name+" ?")
        cart.append((product,quantity))        
        os.system('cls')
        want = input('want more items?(y/n)')
        want = want.lower() == 'y'
    generate(cart)
main()