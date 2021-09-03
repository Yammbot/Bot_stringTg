print("an online StringSession generator")

print("p ==> Pyrogram (docs.pyrogram.org)")
print("PyroGramUserBot ==> https://GitHub.com/SpEcHiDe/PyroGramUserBot")

print("t ==> Telethon (docs.telethon.dev)")
print("Telethon UserBot ==> https://GitHub.com/SpEcHiDe/UniBorg")

print("Select your required option: ")
s_l = input("enter p / t ? ?? ")

if s_l == "p":
  print("you selected Pyrogram")
  APP_ID = int(input("Enter APP ID here: "))
  API_HASH = input("Enter API HASH here: ")
  import pyrogram
  with pyrogram.Client(
    ":memory:",
    api_id=APP_ID,
    api_hash=API_HASH
  ) as app:
    session_str = app.export_session_string()
    s_m = app.send_message("me", session_str)
    s_m.reply_text("⬆️ This StringSession is generated ", quote=True)
    print("please check your Telegram Saved Messages for the StringSession ")

elif s_l == "t":
  print("you selected Telethon")
  from telethon.sync import TelegramClient
  from telethon.sessions import StringSession
  APP_ID = int(input("Enter APP ID here: "))
  API_HASH = input("Enter API HASH here: ")
  with TelegramClient(
    StringSession(), 
    APP_ID, 
    API_HASH
  ) as client:
    session_str = client.session.save()
    s_m = client.send_message("me", session_str)
    s_m.reply("⬆️ This StringSession is generated")
    print("please check your Telegram Saved Messages for the StringSession ")

else:
  print("?? please select only p / t, ")
