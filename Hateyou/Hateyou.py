from iconservice import *

TAG = 'Hateyou'

class Hateyou(IconScoreBase):

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self.Hateyou = DictDB('Hateyou', db, str)

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()

    @external
    def enroll(self, Hateyou: str):
        self.Hateyou[self.msg.sender] = Hateyou

    @external(readonly=True)
    def Hateyou(self) -> str:
        return self.Hateyou[self.msg.sender]
