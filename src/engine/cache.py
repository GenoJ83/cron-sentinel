class JobCache:
    _jobs = {}
    @classmethod
    def update(cls, name, ts): cls._jobs[name] = ts
    @classmethod
    def get(cls, name): return cls._jobs.get(name)
