try:
    import pyotp
    import os
except:
    import os
    os.system('pip install pyotp')
    import pyotp
os.system('cls')
totp = pyotp.TOTP('111111')
print("\n  > Current code: " + totp.now(11111))
