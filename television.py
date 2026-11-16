class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self, status=False, muted=False, volume=MIN_VOLUME, channel=MIN_CHANNEL):
        self.__status = status
        self.__muted = muted
        self.__volume = volume
        self.__channel = channel

    def power(self):
        if self.__status:
            self.__status = False
        else: self.__status = True

    def mute(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
            else: self.__muted = True

    def channel_up(self):
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel = self.__channel + 1
            elif self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel = self.__channel - 1
            elif self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume = self.__volume + 1

    def volume_down(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume = self.__volume - 1

    def __str__(self) -> str:
        if self.__muted:
            volume = 0
        else:
            volume = self.__volume

        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}'
