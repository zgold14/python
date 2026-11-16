class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self, status :bool =False, muted :bool =False, volume :int =MIN_VOLUME, channel :int =MIN_CHANNEL):
        """
        This function initializes the Television class.
        :param status: True if the television is on, false otherwise.
        :param muted: True if the television is muted, false otherwise.
        :param volume: Integer representing the volume of the television.
        :param channel: Integer representing the channel of the television.
        """
        self.__status = status
        self.__muted = muted
        self.__volume = volume
        self.__channel = channel

    def power(self) -> None:
        """
        This function changes the status of the television.
        :return: None
        """
        if self.__status:
            self.__status = False
        else: self.__status = True

    def mute(self) -> None:
        """
        This function changes if the television is muted.
        :return: None
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            else: self.__muted = True

    def channel_up(self) -> None:
        """
        This function changes the current channel of the television up.
        If the channel is already at the maximum, the channel is set to the minimum channel.
        :return: None
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel = self.__channel + 1
            elif self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        This function changes the current channel of the television down.
        If the channel is already at the minimum, the channel is set to the maximum channel.
        :return: None
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel = self.__channel - 1
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        This function changes the current volume of the television up.
        If the television is muted, the muted status changes in addition.
        :return: None
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume = self.__volume + 1

    def volume_down(self) -> None:
        """
        This function changes the current volume of the television down.
        If the television is muted, the muted status changes in addition.
        :return: None
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            elif self.__volume > Television.MIN_VOLUME:
                self.__volume = self.__volume - 1

    def __str__(self) -> str:
        if self.__muted:
            volume = 0
        else:
            volume = self.__volume

        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}'
