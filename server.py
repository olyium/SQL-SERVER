from fastapi import FastAPI, Request
import core.classes as classes
import core.functions as functions
import pathlib

ROOT: str = str(pathlib.Path(__file__).parent.resolve())
functions.SETUP(ROOT)
app = FastAPI()

@app.post('/edp')
async def EDP(request: Request) -> dict:

    try:

        REQUEST_DATA: dict = await request.json()
        
        try:

            SQL_DATA: str = REQUEST_DATA.get('SQL') or REQUEST_DATA.get('SQL'.lower())
            if SQL_DATA == None:
                raise classes.SQLDataInvalid
            DB_NAME: str = REQUEST_DATA.get('DB') or REQUEST_DATA.get('DB'.lower())
            if DB_NAME == None:
                raise classes.DBNameInvalid
            
            EDP_REQUEST = functions.EDP(SQL_DATA, DB_NAME, ROOT)

            return EDP_REQUEST

        except classes.SQLDataInvalid:
            return {'ERROR': classes.SQLDataInvalid.base_error_message}
        except classes.DBNameInvalid:
            return {'ERROR': classes.DBNameInvalid.base_error_message}
    
    except Exception as E:

        return {'ERROR': str(E)}
