from television import Television


def test_init():
    tv1 = Television()
    assert str(tv1) == "Power = False, Channel = 0, Volume = 0"

    #test initializing with power=true and a volume and channel greater than zero
    tv2 = Television(True, False, 1, 1)
    assert str(tv2) == "Power = True, Channel = 1, Volume = 1"

    #test initializing with both muted=True and a volume greater than 0
    tv3 = Television(True, True, 1, 2)
    assert str(tv3) == "Power = True, Channel = 2, Volume = 0"

def test_power():
    tv1 = Television()
    tv1.power()
    assert str(tv1) == "Power = True, Channel = 0, Volume = 0"
    tv1.power()
    assert str(tv1) == "Power = False, Channel = 0, Volume = 0"

    tv2 = Television(True)
    tv2.power()
    assert str(tv2) == "Power = False, Channel = 0, Volume = 0"


def test_mute():
    tv1 = Television(True)
    tv1.mute()
    assert str(tv1) == "Power = True, Channel = 0, Volume = 0"
    tv1.volume_up()
    assert str(tv1) == "Power = True, Channel = 0, Volume = 1"
    tv1.mute()
    assert str(tv1) == "Power = True, Channel = 0, Volume = 0"
    tv1.mute()
    assert str(tv1) == "Power = True, Channel = 0, Volume = 1"

    tv2 = Television(False, False, 2, 0)
    assert str(tv2) == "Power = False, Channel = 0, Volume = 2"
    tv2.mute()
    assert str(tv2) == "Power = False, Channel = 0, Volume = 2"
    tv2.mute()
    assert str(tv2) == "Power = False, Channel = 0, Volume = 2"


def test_channel_up():
    tv1 = Television(True)
    tv1.channel_up()
    assert str(tv1) == "Power = True, Channel = 1, Volume = 0"

    tv2 = Television(True)
    for n in range(Television.MAX_CHANNEL + 1):
        tv2.channel_up()
    assert str(tv2) == f"Power = True, Channel = {Television.MIN_CHANNEL}, Volume = 0"

    tv3 = Television()
    tv3.channel_up()
    assert str(tv3) == "Power = False, Channel = 0, Volume = 0"

def test_channel_down():
    tv1 = Television(True)
    tv1.channel_down()
    assert str(tv1) == f"Power = True, Channel = {Television.MAX_CHANNEL}, Volume = 0"

    tv2 = Television(True, False, 0, 1)
    tv2.channel_down()
    assert str(tv2) == "Power = True, Channel = 0, Volume = 0"

    tv3 = Television()
    tv3.channel_down()
    assert str(tv3) == "Power = False, Channel = 0, Volume = 0"

def test_volume_up():
    tv1 = Television(True)
    tv1.volume_up()
    assert str(tv1) == "Power = True, Channel = 0, Volume = 1"

    #test that the volume will not go above the set maximum
    tv2 = Television(True)
    for n in range(Television.MAX_VOLUME+1):
        tv2.volume_up()
    assert str(tv2) == f"Power = True, Channel = 0, Volume = {Television.MAX_VOLUME}"

    tv3 = Television()
    tv3.volume_up()
    assert str(tv3) == "Power = False, Channel = 0, Volume = 0"

    tv4 = Television(True, True, 1, 0)
    tv4.volume_up()
    assert str(tv4) == "Power = True, Channel = 0, Volume = 2"

def test_volume_down():
    tv1 = Television(True)
    #test that the volume will not go below the minimum (which is the default when initializing)
    tv1.volume_down()
    assert str(tv1) == f"Power = True, Channel = 0, Volume = {Television.MIN_VOLUME}"

    tv2 = Television(True, False, 1, 0)
    tv2.volume_down()
    assert str(tv2) == "Power = True, Channel = 0, Volume = 0"

    tv3 = Television()
    tv3.volume_down()
    assert str(tv3) == "Power = False, Channel = 0, Volume = 0"

    tv4 = Television(True, True, 2, 0)
    tv4.volume_down()
    assert str(tv4) == "Power = True, Channel = 0, Volume = 1"
