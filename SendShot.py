import  os,time
from pathlib import Path
from pynput.keyboard import Key, Listener
from discord_webhook import DiscordWebhook
from dotenv import load_dotenv

load_dotenv()


class SendShotApplication:
    def __init__(self) -> None:
        self.listener=None

    def send_discord_webhook(self,file) -> None:
        webhook=DiscordWebhook(os.getenv("WEBHOOK_URL"))    
        with open(file,'rb') as f:
            webhook.add_file(file=f.read(),filename='latest.png')
        webhook.execute()

    def send_slack(self) -> None:
        pass

    def on_press(self,key) -> None:
        if(key==Key.print_screen):
            time.sleep(1)
            self.send_discord_webhook(sorted(Path(f"/home/{os.getlogin()}/Pictures").iterdir(),key=os.path.getmtime,reverse=True)[0])

    def sendshot(self) -> None:
        with Listener(on_press=self.on_press,) as listener:
            self.listener=listener
            listener.join()

    def stop(self) -> None:
        self.listener.stop()
        self.listener=None        



if __name__=="__main__":
    SShot=SendShot()
    SShot.sendshot()