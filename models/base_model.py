import uuid
import datetime

class BaseModel():
    id = uuid.uuid4()
    id = str(id)
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()
    def __str__(self):
            return self.id