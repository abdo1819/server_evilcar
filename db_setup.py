from pymongo import MongoClient

# predefined enum like class to avoid string typos
def _create_database(URI,db_name):
    """
        Warning: This function is intended only to be used inside the scope of this file
        you should use it outside
        Usage: _create_database(URI,db_name) return a database object
        Example: db = _create_database(URI,db_name)
    """
    clinet = MongoClient(URI)
    return clinet[db_name]

class data_manager():
    """
        This class was a made as wrapper for PyMongo libraries to add some constrain on collection names and to hide mango layer to be replaceable 
        Usage:
        Example:
    """
    def __init__(self,URI="mongodb://localhost:27017/",
                 db_name="evil_car"):
        self.db = _create_database(URI,db_name)

    def _get_collection(self,collection_name):
        return self.db[collection_name]

    def add_data(self,collection_name,data):
        """
        """
        # TODO: add data checkers here
        return self._get_collection(collection_name).insert(data) 
    
    def get_data(self,collection_name,collection_filter=None):
        """
        """
        col = self._get_collection(collection_name)
        if collection_filter is not None:
            return col.find(collection_filter,{"_id":0}) 
        return col.find({},{"_id":0})

# simple test unit
if __name__ == "__main__" :
   import names 
   d = data_manager(db_name=names.test_database_name)
   d.add_data(names.testingCollection,[{"name1":4,"name2":"value3"}])
   d.add_data(names.testingCollection,[{"sddssddd":4,"name2":"value3"}])
   for i in d.get_data(names.testingCollection):
       print(i)
