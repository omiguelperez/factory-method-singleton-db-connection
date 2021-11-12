from abc import ABCMeta, abstractmethod
from typing import Dict


class DBConnector:

    _connection = None

    def __init__(self):
        raise Exception("This class can't be instatiated. It's a singleton class.")

    @classmethod
    @abstractmethod
    def _create_connection(cls):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def _close_connection(cls):
        raise NotImplementedError

    @classmethod
    def connect(cls):
        if not cls._connection:
            cls._create_connection()
            print("Connection created")
        else:
            print("Reusing existing connection")
        return cls._connection

    @classmethod
    def close(cls):
        cls._close_connection()


class MysqlDBConnector(DBConnector):

    @classmethod
    def _create_connection(cls):
        # connect to mysql db
        pass

    @classmethod
    def _close_connection(cls):
        # close mysql connection
        pass


class PostgresqlDBConnector(DBConnector):

    @classmethod
    def _create_connection(cls):
        import sys
        import psycopg2
        try:
            cls._connection = psycopg2.connect(
                dbname="postgres",
                user="user",
                password="password",
                host="postgres",
                port="5432",
            )
        except psycopg2.OperationalError as e:
            print("There was an error connecting to postgres", e)
            sys.exit(-1)
        print("Connected to postgres")

    @classmethod
    def _close_connection(cls):
        # close postgres connection
        pass


class MssqlDBConnector(DBConnector):

    @classmethod
    def _create_connection(cls):
        # connect to mssql db
        pass

    @classmethod
    def _close_connection(cls):
        # close mssql connection
        pass


class OracleDBConnector(DBConnector):

    @classmethod
    def _create_connection(cls):
        # connect to oracle db
        pass

    @classmethod
    def _close_connection(cls):
        # close oracle connection
        pass


class DB:

    @staticmethod
    def get(db_type):
        db_types: Dict[str, any] = {
            "oracle": OracleDBConnector,
            "mssql": MssqlDBConnector,
            "postgres": PostgresqlDBConnector,
            "mysql": MysqlDBConnector,
        }
        if db_type not in db_types.keys():
            raise Exception(
                "Unsupported db type, only 'oracle', 'mssql', 'postgres' and 'mysql' are supported"
            )
        return db_types[db_type].connect()


if __name__ == "__main__":
    db = DB.get("postgres")
    print(db)
