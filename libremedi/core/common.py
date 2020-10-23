class RemediError(Exception):
    pass


class NetworkError(Exception):
    pass


class BackendError(RemediError):
    pass


class ConnectionLost(NetworkError):
    pass
