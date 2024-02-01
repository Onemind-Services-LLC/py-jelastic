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
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.data

        Ref: https://docs.jelastic.com/api/#!/data
    """

    _endpoint1 = "data"

    @property
    def Base(self) -> "_Base":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.data.Base

        Ref: https://docs.jelastic.com/api/private/#!/api/data.Base
        """
        return _Base(
            session=self._session,
            token=self._token,
            debug=self._debug,
            ruk=self._ruk,
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
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def CreateObject(
        self,
        type: str,
        data: str = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def CreateObjects(
        self,
        type: str,
        data: str,
        ruk: str = None,
    ):
        return self._get(
            "CreateObjects",
            params={
                "type": type,
                "data": data,
                "ruk": ruk,
            },
        )

    def DefineType(
        self,
        type: str,
        fields: str = None,
        unique: str = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def DefineTypeByUid(
        self,
        uid: int,
        type: str,
        fields: str = None,
        unique: str = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def DeleteObject(
        self,
        type: str,
        id: int,
        ruk: str = None,
    ):
        """
        param type: name of the type of data
        param id: object id
        """
        return self._get(
            "DeleteObject",
            params={
                "type": type,
                "id": id,
                "ruk": ruk,
            },
        )

    def DeleteObjectsByCriteria(
        self,
        type: str,
        criteria: str = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def GetNotEmptyType(
        self,
        type_like: str,
        asc: bool = None,
        ruk: str = None,
    ):
        return self._get(
            "GetNotEmptyType",
            params={
                "typeLike": type_like,
                "asc": asc,
                "ruk": ruk,
            },
        )

    def GetObject(
        self,
        type: str,
        id: int,
        join: str = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def GetObjects(
        self,
        type: str,
        froms: int = None,
        count: int = None,
        join: str = None,
        ruk: str = None,
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
                "ruk": ruk,
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
        ruk: str = None,
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
                "ruk": ruk,
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
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def GetObjectsCount(
        self,
        type: str,
        criteria: str = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def GetProperty(
        self,
        type: str,
        id: int,
        property: str,
        join: str = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def GetType(
        self,
        type: str,
        ruk: str = None,
    ):
        """
        param type: name of the type of data
        """
        return self._get(
            "GetType",
            params={
                "type": type,
                "ruk": ruk,
            },
        )

    def GetTypes(
        self,
        froms: int = None,
        count: int = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def GetTypesCount(
        self,
        ruk: str = None,
    ):
        return self._get(
            "GetTypesCount",
            params={
                "ruk": ruk,
            },
        )

    def GetUniqueFields(
        self,
        type: str,
        ruk: str = None,
    ):
        """
        param type: name of the type of data
        """
        return self._get(
            "GetUniqueFields",
            params={
                "type": type,
                "ruk": ruk,
            },
        )

    def RemoveField(
        self,
        type: str,
        field: str,
        ruk: str = None,
    ):
        """
        param type: name of the type of data
        param field: name deleted fields (id - reserved)
        """
        return self._get(
            "RemoveField",
            params={
                "type": type,
                "field": field,
                "ruk": ruk,
            },
        )

    def RenameField(
        self,
        type: str,
        old_field: str,
        new_field: str,
        ruk: str = None,
    ):
        """
        param type: name of the type of data
        param oldField: the current name of the field
        param newField:new field name
        """
        return self._get(
            "RenameField",
            params={
                "type": type,
                "oldField": old_field,
                "newField": new_field,
                "ruk": ruk,
            },
        )

    def RenameType(
        self,
        type: str,
        old_type: str,
        new_type: str,
        ruk: str = None,
    ):
        """
        param type: name of the type of data
        param old_type: old name
        param new_type: new name
        """
        return self._get(
            "RenameType",
            params={
                "type": type,
                "oldType": old_type,
                "newTyoe": new_type,
                "ruk": ruk,
            },
        )

    def SetObject(
        self,
        type: str,
        id: int,
        data: str,
        ruk: str = None,
    ):
        """
        param type: name of the type of data
        param id: object id
        param data: the data object in the JSON
        """
        return self._get(
            "SetObject",
            params={
                "type": type,
                "id": id,
                "data": data,
                "ruk": ruk,
            },
        )

    def SetObjects(
        self,
        type: str,
        data: str,
        ruk: str = None,
    ):
        """
        param type: name of the type of data
        param id: object id
        param data: the data object in the JSON
        """
        return self._get(
            "SetObjects",
            params={
                "type": type,
                "data": data,
                "ruk": ruk,
            },
        )

    def SetProperty(
        self,
        type: str,
        id: int,
        property: str,
        value: None,
        ruk: str = None,
    ):
        """
        param type: name of the type of data
        param id: object id
        param property: property name
        param value: property value
        """
        return self._get(
            "SetProperty",
            params={
                "type": type,
                "id": id,
                "property": property,
                "value": value,
                "ruk": ruk,
            },
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
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def SetUniqueFields(
        self,
        type: str,
        unique: str = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def UndefineType(
        self,
        type: str,
        ruk: str = None,
    ):
        """
        param type:name name of the type of data
        """
        return self._get(
            "UndefineType",
            params={
                "type": type,
                "ruk": ruk,
            },
        )
