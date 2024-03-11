import uuid
import datetime

class BaseModel():
    id = uuid.uuid4()
    id = str(id)
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()
    def __str__(self):
            return self.id
    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict

