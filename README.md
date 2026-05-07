# 🤖 Motorming Daily Stock Bot — Setup Guide

This bot automatically posts your stock photos + caption to your Telegram group **every day at 8:00 AM** (Malaysia time). 100% **FREE**, no credit card needed.

---

## 📋 What You'll Do (One-Time Setup ~20 mins)

1. Create a Telegram bot
2. Get your group's chat ID
3. Create a free GitHub account
4. Upload these files
5. Add bot token + chat ID as secrets
6. Done — bot runs every day automatically!

---

## STEP 1️⃣ — Create Your Telegram Bot

1. Open Telegram, search for **@BotFather**
2. Send `/newbot`
3. Give it a name → e.g. `Motorming Stock Bot`
4. Give it a username → must end in `bot`, e.g. `motorming_stock_bot`
5. BotFather will give you a **TOKEN** that looks like:
   ```
   8123456789:AAH...long random string...
   ```
6. **COPY this token** and save it somewhere safe (Notes app)

---

## STEP 2️⃣ — Add Bot to Your Telegram Group

1. Open your Telegram group
2. Tap group name → **Add Members**
3. Search for your bot username (e.g. `motorming_stock_bot`)
4. Add it to the group

---

## STEP 3️⃣ — Get Your Group's Chat ID

The bot needs to know **which group** to post to.

1. In Telegram, search for **@RawDataBot** (or `@username_to_id_bot`)
2. Add @RawDataBot to your group
3. It will show a message with your group info — look for `"id": -100xxxxxxxx`
4. **COPY that ID** (with the `-` minus sign at the front!)
5. Remove @RawDataBot from your group after

> Example chat ID: `-1001234567890`

---

## STEP 4️⃣ — Create a Free GitHub Account

1. Go to **https://github.com/signup**
2. Sign up with email (FREE forever)
3. Verify email

---

## STEP 5️⃣ — Create a New Repository

1. Click the **+** icon (top right) → **New repository**
2. Name it: `motorming-bot`
3. Set it to **Private** (so your stock info stays yours)
4. ✅ Tick "Add a README file"
5. Click **Create repository**

---

## STEP 6️⃣ — Upload the Bot Files

You should have received these files:
```
motorming-bot/
├── .github/workflows/daily.yml   ← the schedule
├── photos/                        ← put your stock photos here
│   └── README.md
├── caption.txt                    ← edit your message here
└── post_stock.py                  ← the bot script
```

**Upload via GitHub web (easy way):**

1. In your repo, click **Add file → Upload files**
2. Drag-drop ALL the files (keep the folder structure)
3. Click **Commit changes**

> **Tip:** GitHub web doesn't always preserve folders. If it gets messy, use the GitHub Desktop app, OR upload files one folder at a time.

---

## STEP 7️⃣ — Add Your Secrets (Bot Token + Chat ID)

1. In your repo, click **Settings** (top menu)
2. Left sidebar → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add the first secret:
   - Name: `BOT_TOKEN`
   - Value: paste your BotFather token
   - Click **Add secret**
5. Add the second secret:
   - Name: `CHAT_ID`
   - Value: paste your group chat ID (with the minus sign)
   - Click **Add secret**

---

## STEP 8️⃣ — Add Your Stock Photos

1. In your repo, open the `photos/` folder
2. Click **Add file → Upload files**
3. Drag-drop your stock photos (JPG/PNG)
4. Click **Commit changes**

---

## STEP 9️⃣ — Test It Manually First

Before waiting for 8 AM, test it now:

1. Go to **Actions** tab in your repo
2. Click **Daily Stock Post** on the left
3. Click **Run workflow** → **Run workflow** (green button)
4. Wait ~30 seconds → check your Telegram group
5. Photos should appear with your caption 🎉

---

## ✅ DONE — You're Live!

The bot will now post every day at **8:00 AM Malaysia time** automatically.

---

## 🔄 How to Update Stock (When New Bikes Come / Prices Change)

### To change PHOTOS:
1. Go to your repo → `photos/` folder
2. Delete old photos (click photo → trash icon)
3. Upload new photos via **Add file → Upload files**
4. Click **Commit changes**

### To change MESSAGE/CAPTION:
1. Go to your repo → click `caption.txt`
2. Click the **pencil ✏️ icon** (top right)
3. Edit the text
4. Click **Commit changes**

The bot will use the new content for the next 8 AM post automatically.

---

## ⚠️ Important Notes

- GitHub Actions cron sometimes runs **5–15 mins late** during peak hours — this is normal
- Free tier gives you **2,000 minutes/month** — daily run uses ~30 mins/month, way below limit
- If you want to **skip a day**, just remove the photos OR disable the workflow temporarily
- Max 10 photos per album → if you have 15 photos, bot auto-splits into 2 albums (10 + 5)
- Caption max 1024 characters (Telegram limit)

---

## 🆘 Troubleshooting

**Bot not posting?**
- Check **Actions** tab → click latest run → see error message
- Make sure bot is **member** of your group
- Make sure `CHAT_ID` has the minus sign: `-1001234567890`

**Wrong group?**
- Update `CHAT_ID` secret with correct ID

**Want to stop the bot?**
- Go to **Actions** tab → click `...` menu → **Disable workflow**

---

Need help? Just ask me anytime 💬
