class SentinelError(Exception): pass
class JobTimeoutError(SentinelError): pass
class HeartbeatMissedError(SentinelError): pass
