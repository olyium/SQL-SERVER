import core.classes as classes
import pathlib
import sqlite3
import json
import os

DATABASE_FOLDER_NAME_GLOBAL = None

def EDP(SQL_COMMAND: str, DB_NAME: str, MAIN_DIR: str) -> dict:

    try:
        global DATABASE_FOLDER_NAME_GLOBAL
        DB_NAME = pathlib.Path(DB_NAME).stem
        CONN = sqlite3.connect(rf"{MAIN_DIR}\{DATABASE_FOLDER_NAME_GLOBAL}\{DB_NAME}.db")
        CURSOR = CONN.cursor()

        CURSOR.execute(SQL_COMMAND)
        CONN.commit()

        return {'STATUS': 'SUCCESS'}

    except sqlite3.OperationalError as e:

        return {'ERROR': f'There was a syntax ERROR: {e}'}

    except Exception as e:
        print(e)
        return {'ERROR': 'Error occured in EDP function in [functions.py], unknown why?'}

def SETUP(ROOT: str) -> dict:

    try:

        with open(f"{ROOT}\misc\settings.json", "rb") as SETTINGS:

            SETTINGS_DATA = json.loads(SETTINGS.read().decode())
            DATABASE_FOLDER_NAME = SETTINGS_DATA.get('DATABASE_FOLDER_NAME')

            if SETTINGS_DATA == None or set(sorted(SETTINGS_DATA)) == " ":
                raise classes.SettingsFileCorrupted

            if DATABASE_FOLDER_NAME == None or DATABASE_FOLDER_NAME == " ":
                raise classes.SettingsFileDatabaseNameInvalid
            
            FOLDER_PATH_REAL: str = f"{ROOT}/{DATABASE_FOLDER_NAME}"

            if not os.path.exists(FOLDER_PATH_REAL):
                FOLDER_PATH: pathlib.Path = pathlib.Path(FOLDER_PATH_REAL)
                FOLDER_PATH.mkdir(parents=True, exist_ok=True)

            global DATABASE_FOLDER_NAME_GLOBAL
            DATABASE_FOLDER_NAME_GLOBAL = DATABASE_FOLDER_NAME
            return {'STATUS': 'SUCCESS'}
                
    except classes.SettingsFileCorrupted:
        
        return {'ERROR': classes.SettingsFileCorrupted.base_error_message}
    
    except classes.SettingsFileDatabaseNameInvalid:

        return {'ERROR': classes.SettingsFileDatabaseNameInvalid.base_error_message}