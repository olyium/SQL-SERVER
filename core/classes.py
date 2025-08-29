class SQLDataInvalid(Exception):
    base_error_message = 'SQL_DATA INVALID. EXAMPLE: {"SQL": "<YOUR SQL DATA HERE>"}'

class DBNameInvalid(Exception):
    base_error_message = 'DB_NAME INVALID. EXAMPLE: {"DB": "<YOUR DATABASE NAME HERE>"}'

class SettingsFileCorrupted(Exception):
    base_error_message = 'The settings file is corrupted. It should be named: "settings.json," and contain settings content.'

class SettingsFileDatabaseNameInvalid(Exception):
    base_error_message = 'The settings file setting: [DATABASE_FOLDER_NAME] is INVALID. Please ensure its a string, and has a name.'