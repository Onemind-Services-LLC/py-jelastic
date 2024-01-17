from ..abstract import ClientAbstract
from typing import Literal

__all__ = ["Data"]
EVENT_TYPE = Literal["SEND_NOTIFICATION", "OOM_KILLER", "CUSTOM_NODE_EVENT"]


class Data(ClientAbstract):
    """
    Service provides a flexible structure to manage the database, create tables, fields, indicating the type, make notes in the tables to hold associations between data. Service is based on technology ORM (programming technique that links databases to the concepts of object-oriented programming languages, creating a "virtual object data base). Service structures has its own SQL processor (HiveQL) for the structured queries that completely eliminates the possibility of malicious injections. Service access control is also working with the structures, allowing to specify the individual rights of access as the data types, and on objects. Options for using the service:

        The development of any applications which require storage of information;
        Exchange of data between clients through the lens of service;
        Construction of API to import data from your project for other developers of applications;
        Duplication of data to reduce the risk of loss, encryption, if necessary.
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.data

        Ref: https://docs.jelastic.com/api/#!/data
    """

    _endpoint1 = "data"

    @property
    def Base(self) -> "_Base":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.data.Base

        Ref: https://docs.jelastic.com/api/private/#!/api/data.Base
        """
        return _Base(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )


class _Base(Data):
    """
    Service provides a flexible structure to manage the database, create tables, fields, indicating the type, make notes in the tables to hold associations between data. Service is based on technology ORM (programming technique that links databases to the concepts of object-oriented programming languages, creating a "virtual object data base). Service structures has its own SQL processor (HiveQL) for the structured queries that completely eliminates the possibility of malicious injections. Service access control is also working with the structures, allowing to specify the individual rights of access as the data types, and on objects. Options for using the service:

           The development of any applications which require storage of information;
           Exchange of data between clients through the lens of service;
           Construction of API to import data from your project for other developers of applications;
           Duplication of data to reduce the risk of loss, encryption, if necessary.

       Ref: https://docs.jelastic.com/api/private/#!/api/data.Base
    """

    _endpoint2 = "base"

    def AddField(
        self,
        type: str,
        field: str,
        field_type: str = None,
    ):
        """
        :param type: name type
        :param field: name added a field (id - reserved)
        :param field_type: type of added fields
        """
        return self._get(
            "AddField",
            params={
                "type": type,
                "field": field,
                "fieldType": field_type,
            },
        )

    def CreateObject(
        self,
        type: str,
        data: str = None,
    ):
        """
        :param type: name of the data type for which the object is created
        :param data: the data object in the JSON
        """
        return self._get(
            "CreateObject",
            params={
                "type": type,
                "data": data,
            },
        )

    def CreateObjects(self, type: str, data: str):
        return self._get(
            "CreateObjects",
            params={
                "type": type,
                "data": data,
            },
        )

    def DefineType(
        self,
        type: str,
        fields: str = None,
        unique: str = None,
    ):
        """
        :param type: name for the created data type, which meets the following requirements:
            is unique for the specified appid does not start with a digit contains only latin letters, digits and underscore
        :param fields: A list of fields for the created data type specified in the { fieldname : "datatype", ... }, { fieldname : "datatype", ... }, … format.
        :param unique: A unique fields data type in the { fields : [ "field_name", ... ] }, { ... } format.
        """
        return self._get(
            "DefineType",
            params={
                "type": type,
                "fields": fields,
                "unique": unique,
            },
        )

    def DefineTypeByUid(
        self,
        uid: int,
        type: str,
        fields: str = None,
        unique: str = None,
    ):
        """
        param uid: user unique identifier
        param type: type name
        param fields: fields definition
        param unique: unique fields
        """
        return self._get(
            "DefineTypeByUid",
            params={
                "uid": uid,
                "type": type,
                "fields": fields,
                "unique": unique,
            },
        )

    def DeleteObject(self, type: str, id: int):
        """
        param type: name of the type of data
        param id: object id
        """
        return self._get(
            "DeleteObject",
            params={
                "type": type,
                "id": id,
            },
        )

    def DeleteObjectsByCriteria(
        self,
        type: str,
        criteria: str = None,
    ):
        """
        param type: name of the data type for which the object is created
        param criteria: the criteria for selection
        """
        return self._get(
            "DeleteObjectsByCriteria",
            params={
                "type": type,
                "criteria": criteria,
            },
        )

    def GetNotEmptyType(
        self,
        type_like: str,
        asc: bool = None,
    ):
        return self._get(
            "GetNotEmptyType",
            params={
                "typeLike": type_like,
                "asc": asc,
            },
        )

    def GetObject(
        self,
        type: str,
        id: int,
        join: str = None,
    ):
        """
        param type: name of the type of data
        param id: object id
        """
        return self._get(
            "GetObject",
            params={
                "type": type,
                "id": id,
                "join": join,
            },
        )

    def GetObjects(
        self,
        type: str,
        froms: int = None,
        count: int = None,
        join: str = None,
    ):
        """
        param type: name of the type of data
        param froms: index which returned objects (default is 0)
        param count: number of objects (by default equal to the total number of objects for a given type)
        """
        return self._get(
            "GetObjects",
            params={
                "type": type,
                "froms": froms,
                "count": count,
                "join": join,
            },
        )

    def GetObjectsByCriteria(
        self,
        type: str,
        criteria: str = None,
        froms: int = None,
        count: int = None,
        join: str = None,
        projection: str = None,
    ):
        """
        param type: name of the type of data
        param criteria: the criteria for selection
        param froms: index which returned objects (default is 0)
        param count: number of objects (by default equal to the total number of objects for a given type)
        """
        return self._get(
            "GetObjectsByCriteria",
            params={
                "type": type,
                "criteria": criteria,
                "froms": froms,
                "count": count,
                "join": join,
                "projection": projection,
            },
        )

    def GetObjectsByRole(
        self,
        type: str,
        role: str,
        criteria: str = None,
        froms: int = None,
        count: int = None,
        join: str = None,
        projection: str = None,
    ):
        """
        param type: name of the type of data
        param criteria: the criteria for selection
        param froms: index which returned objects (default is 0)
        param count: number of objects (by default equal to the total number of objects for a given type)
        """
        return self._get(
            "GetObjectsByRole",
            params={
                "type": type,
                "role": role,
                "criteria": criteria,
                "froms": froms,
                "count": count,
                "join": join,
                "projection": projection,
            },
        )

    def GetObjectsCount(
        self,
        type: str,
        criteria: str = None,
    ):
        """
        param type: name of the data type for which the object is created
        param criteria: the criteria for selection
        """
        return self._get(
            "GetObjectsCount",
            params={
                "type": type,
                "criteria": criteria,
            },
        )

    def GetProperty(
        self,
        type: str,
        id: int,
        property: str,
        join: str = None,
    ):
        """
        param type: name of the type of data
        param id: object id
        param property: property name
        """
        return self._get(
            "GetProperty",
            params={
                "type": type,
                "id": id,
                "property": property,
                "join": join,
            },
        )

    def GetType(
        self,
        type: str,
    ):
        """
        param type: name of the type of data
        """
        return self._get(
            "GetType",
            params={
                "type": type,
            },
        )

    def GetTypes(
        self,
        froms: int = None,
        count: int = None,
    ):
        """
        param froms: index which returned objects (default is 0)
        param count: number of objects (by default equal to the total number of objects for a given type)
        """
        return self._get(
            "GetTypes",
            params={
                "froms": froms,
                "count": count,
            },
        )

    def GetTypesCount(
        self,
    ):
        return self._get("GetTypesCount", params={})

    def GetUniqueFields(
        self,
        type: str,
    ):
        """
        param type: name of the type of data
        """
        return self._get(
            "GetUniqueFields",
            params={
                "type": type,
            },
        )

    def RemoveField(
        self,
        type: str,
        field: str,
    ):
        """
        param type: name of the type of data
        param field: name deleted fields (id - reserved)
        """
        return self._get("RemoveField", params={"type": type, "field": field})

    def RenameField(
        self,
        type: str,
        old_field: str,
        new_field: str,
    ):
        """
        param type: name of the type of data
        param oldField: the current name of the field
        param newField:new field name
        """
        return self._get(
            "RenameField",
            params={"type": type, "oldField": old_field, "newField": new_field},
        )

    def RenameType(
        self,
        type: str,
        old_type: str,
        new_type: str,
    ):
        """
        param type: name of the type of data
        param old_type: old name
        param new_type: new name
        """
        return self._get(
            "RenameType",
            params={"type": type, "oldType": old_type, "newTyoe": new_type},
        )

    def SetObject(
        self,
        type: str,
        id: int,
        data: str,
    ):
        """
        param type: name of the type of data
        param id: object id
        param data: the data object in the JSON
        """
        return self._get("SetObject", params={"type": type, "id": id, "data": data})

    def SetObjects(
        self,
        type: str,
        data: str,
    ):
        """
        param type: name of the type of data
        param id: object id
        param data: the data object in the JSON
        """
        return self._get("SetObjects", params={"type": type, "data": data})

    def SetProperty(self, type: str, id: int, property: str, value: None):
        """
        param type: name of the type of data
        param id: object id
        param property: property name
        param value: property value
        """
        return self._get(
            "SetProperty",
            params={"type": type, "id": id, "property": property, "value": value},
        )

    def SetObjectsByCriteria(
        self,
        type: str,
        property: str,
        value: None = None,
        criteria: str = None,
        froms: int = None,
        count: int = None,
        join: str = None,
    ):
        return self._get(
            "SetObjectsByCriteria",
            params={
                "type": type,
                "property": property,
                "value": value,
                "criteria": criteria,
                "froms": froms,
                "count": count,
                "join": join,
            },
        )

    def SetUniqueFields(
        self,
        type: str,
        unique: str = None,
    ):
        """
        param type:name name of the type of data
        param unique: A unique fields data type in the { fields : [ "field_name", ... ] }, { ... } format.
        """
        return self._get(
            "SetUniqueFields",
            params={
                "type": type,
                "unique": unique,
            },
        )

    def UndefineType(
        self,
        type: str,
    ):
        """
        param type:name name of the type of data
        """
        return self._get(
            "UndefineType",
            params={
                "type": type,
            },
        )
