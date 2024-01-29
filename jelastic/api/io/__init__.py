from ..abstract import ClientAbstract

__all__ = ["IO"]


class IO(ClientAbstract):
    _endpoint1 = "io"

    @property
    def File(self) -> "_File":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.io.File

        Ref: https://docs.jelastic.com/api/private/#!/api/io.File
        """
        return _File(
            session=self._session,
            token=self._token,
            debug=self._debug,
            ruk=self._ruk,
        )


class _File(IO):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/io.File
    """

    _endpoint2 = "file"

    def Copy(self, src: str, dest: str):
        return self._get(
            "Copy",
            params={"src": src, "dest": dest},
        )

    def Create(self, path: str, is_dir: bool = None):
        return self._get("Create", params={"path": path, "isdir": is_dir})

    def Delete(self, path: str, ext: str = None):
        return self._get("Delete", params={"path": path, "ext": ext})

    def GetList(self, path: str = None, ext: str = None):
        return self._get("GetList", params={"path": path, "ext": ext})

    def Read(self, path: str):
        return self._get(
            "Read",
            params={
                "path": path,
            },
        )

    def Rename(self, old_path: str, new_path: str):
        return self._get(
            "Rename",
            params={
                "oldPath": old_path,
                "newPath": new_path,
            },
        )

    def Upload(self, source_path: str, dest_path: str, over_write: bool = None):
        return self._get(
            "Upload",
            params={
                "sourcePath": source_path,
                "destPath": dest_path,
                "overWrite": over_write,
            },
        )

    def Write(self, path: str, body: str, append: bool = None):
        return self._get("Write", params={"path": path, "body": body, "append": append})
