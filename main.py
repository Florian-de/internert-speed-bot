from Internet_speed import Check_Internet_Speed

PROMISED_DOWN = 50
PROMISED_UP = 10

internet_check = Check_Internet_Speed(down=PROMISED_DOWN, up=PROMISED_UP)

internet_check.check_internet_speed()

