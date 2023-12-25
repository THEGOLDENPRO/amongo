from datetime import datetime
from typing import Any, TypedDict, List


class Hello(TypedDict):
    isWritablePrimary: bool
    topologyVersion: Any
    maxBsonObjectSize: int
    maxMessageSizeBytes: int
    maxWriteBatchSize: int
    localTime: datetime
    logicalSessionTimeoutMinutes: int
    connectionId: int
    minWireVersion: int
    maxWireVersion: int
    readOnly: bool
    compression: List[str]
    saslSupportedMechs: List[str]