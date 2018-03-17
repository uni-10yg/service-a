import sqlite3, os, inspect
from logger import root_logger

logger = root_logger.getChild(__name__)


class Database:
    _db_path = '{}/db.sqlite'.format(os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0])))

    def __init__(self):
        if not os.path.isfile(__class__._db_path):
            logger.debug('no database found')
            query = 'CREATE TABLE hash_store (id INTEGER PRIMARY KEY, hash TEXT, salt INTEGER)'
            self._executeQuery(query)
            logger.debug('created new database')
        else:
            logger.debug("found database at '{}'".format(__class__._db_path))

    def _executeQuery(self, query):
        try:
            db_conn = sqlite3.connect(__class__._db_path)
            cursor = db_conn.cursor()
            cursor.execute(query)
            if any(statement in query for statement in ('CREATE', 'INSERT', 'DELETE', 'UPDATE')):
                db_conn.commit()
                result = True
            else:
                result = cursor.fetchall()
            db_conn.close()
            return result
        except Exception as ex:
            logger.error(ex)
            return False

    def insert(self, hash, salt):
        query = 'INSERT INTO hash_store (hash, salt) VALUES ("{}", "{}")'.format(hash, salt)
        self._executeQuery(query)

    def selectAll(self):
        query = 'SELECT * FROM hash_store'
        return self._executeQuery(query)