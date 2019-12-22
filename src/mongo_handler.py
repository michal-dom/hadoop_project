import pymongo


class MongoConnection:
    __instance = None

    @staticmethod
    def get_instance():
        if MongoConnection.__instance is None:
            MongoConnection()
        return MongoConnection.__instance

    def __init__(self):
        if MongoConnection.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
            self.mongo_db = mongo_client["bigdata"]
            MongoConnection.__instance = self


def get_scraped_links():
    mongo_con = MongoConnection.get_instance()
    mongo_collection = mongo_con.mongo_db['corporas']

    queried_links = mongo_collection.find({}, {'_id': 0, 'file_name': 1})
    links_scraped = [x['file_name'] for x in queried_links]
    return links_scraped


def get_links_to_scrap():
    mongo_con = MongoConnection.get_instance()
    mongo_collection = mongo_con.mongo_db['links_to_scrap']
    queried_links = mongo_collection.find()

    links_to_scrap = [x['link'] for x in queried_links]
    return links_to_scrap


# print(get_links_to_scrap())
# for x in mc.mongo_collection.find({}, {'_id': 0, 'file_name': 1}):
#     print(x['file_name'])


