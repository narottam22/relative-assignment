#!/usr/bin/env python

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine, checkfirst=True)

app = FastAPI()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/store_data')
async def store_contract_data(lot_id: int, req_lotcreated: int, req_lotjoined: int, \
                              req_lotresolved: int, db_instance: Session = Depends(get_db)):
    '''This API route stores the contract information in the database table'''

    db_contract = models.goerli(id=lot_id, lotcreated=req_lotcreated, lotjoined=req_lotjoined, \
                         lotresolved=req_lotresolved)

    db_instance.add(db_contract)
    db_instance.commit()

    return "Contract information stored"


@app.get('/lot_details/{id}')
async def get_lot_details(lot_id: int, db_instance: Session = Depends(get_db)):
    '''This API route fetches the contract information from the database'''

    lot_details = db_instance.query(models.goerli).filter\
        (models.goerli.id == lot_id).first()
    
    return lot_details

