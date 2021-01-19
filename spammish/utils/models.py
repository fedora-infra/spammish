class StageUser:
    def __init__(self, ipa_stageuser):
        self._ipa_stageuser = ipa_stageuser

    def dn(self):
        return self._ipa_stageuser["dn"]

    def __getattr__(self, name):
        return self._ipa_stageuser[name][0]

    def __str__(self):
        return self.cn
