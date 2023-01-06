"""BambuLab Error Exceptions"""


class BambuLabError(Exception):
    """Generic BambuLab Exception"""


class BambuLabUnsupportedFeature(Exception):
    """Unsupported feature exception"""


class BambuLabConnectionError(BambuLabError):
    """BambuLab connection exception"""


class BambuLabConnectionTimeoutError(BambuLabConnectionError):
    """BambuLab connection Timeout exception"""


class BambuLabConnectionClosed(BambuLabConnectionError):
    """BambuLab Websocket connection has been closed"""
