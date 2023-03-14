from sqlalchemy.ext.declarative import DeclarativeMeta
from datetime import datetime
import json


class JsonConverter:

    def serialize(obj):
        fields = {}
        try:
            for attr, value in obj.__dict__.items():
                if(not attr.startswith('_')):
                    if(isinstance(obj.__getattribute__(attr), datetime)):
                        data = (obj.__getattribute__(attr)).isoformat()
                    #elif(isinstance(obj.__getattribute__(attr), TherapeuticArea)):
                    #    data = (obj.__getattribute__(attr)).name_ta
                    else:
                        data = obj.__getattribute__(attr)

                    if(data is not None):
                        if(str(type(data)) == "<class 'decimal.Decimal'>"):
                            fields[attr] = str(data)
                        else:
                            fields[attr] = data

        except TypeError as ex:
            print(str(ex))
            pass

        return fields
