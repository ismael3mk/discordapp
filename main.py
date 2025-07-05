# main.py

import os
import threading
from flask import Flask, render_template
from dotenv import load_dotenv
import discord
from discord.ext import commands

# تحميل متغيرات البيئة
load_dotenv()

# إعداد Flask
app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

# إعداد ديسكورد بوت
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as: {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

# تشغيل البوت في Thread منفصل
def run_discord_bot():
    token = os.getenv("DISCORD_TOKEN")
    if token:
        bot.run(token)
    else:
        print("❌ DISCORD_TOKEN not set!")

if __name__ == "__main__":
    # تشغيل البوت
    threading.Thread(target=run_discord_bot).start()
    # تشغيل السيرفر Flask
    app.run(host="0.0.0.0", port=5000)

