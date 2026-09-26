import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

# =========================
# PC FIX BOT
# TOKEN="8958908481:AAHb6RW1iQsqf_Iz8zTts--M-nymoRuqSrc"

CHANNEL = "@PCFixHelp24"
GROUP = "@PCFixHelp247"


# =========================
# HELPERS
# =========================

async def safe_edit(query, text, keyboard=None):
    """ویرایش پیام با مدیریت خطا (برای پیام‌های قدیمی یا یکسان)"""
    try:
        if keyboard:
            await query.edit_message_text(
                text,
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
        else:
            await query.edit_message_text(text)
    except Exception as e:
        print(f"[safe_edit error] {e}")


def main_keyboard():
    return [
        [
            InlineKeyboardButton("🎮 بازی‌ها", callback_data="games"),
            InlineKeyboardButton("🛠 رفع خطا", callback_data="errors"),
        ],
        [
            InlineKeyboardButton("📥 آموزش نصب", callback_data="install"),
            InlineKeyboardButton("💻 ترفندهای PC", callback_data="tips"),
        ],
        [
            InlineKeyboardButton("📢 کانال", url="https://t.me/PCFixHelp24"),
            InlineKeyboardButton("👥 گروه", url="https://t.me/PCFixHelp247"),
        ],
    ]


# =========================
# START
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🖥️ خوش اومدی به PC FIX\n\n"
        "مرجع آموزش نصب بازی، رفع خطا و ترفندهای کامپیوتر 🎮\n\n"
        "یکی از گزینه‌های زیر رو انتخاب کن:"
    )
    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(main_keyboard())
    )


# =========================
# GAMES
# =========================

async def games_menu(query):
    keyboard = [
        [InlineKeyboardButton("Resident Evil", callback_data="re")],
        [InlineKeyboardButton("Forza Horizon", callback_data="forza")],
        [InlineKeyboardButton("Red Dead Redemption 2", callback_data="rdr2")],
        [InlineKeyboardButton("🎮 سایر بازی‌ها", callback_data="other_games")],
        [InlineKeyboardButton("🔙 برگشت", callback_data="home")],
    ]
    await safe_edit(
        query,
        "🎮 بخش بازی‌ها\n\nبازی موردنظر رو انتخاب کن:",
        keyboard
    )


async def resident_evil_menu(query):
    keyboard = [
        [InlineKeyboardButton("Resident Evil 2", callback_data="re2")],
        [InlineKeyboardButton("Resident Evil 3", callback_data="re3")],
        [InlineKeyboardButton("Resident Evil 4", callback_data="re4")],
        [InlineKeyboardButton("Resident Evil 7", callback_data="re7")],
        [InlineKeyboardButton("Resident Evil Village", callback_data="revillage")],
        [InlineKeyboardButton("Resident Evil Requiem", callback_data="requiem")],
        [InlineKeyboardButton("🔙 برگشت", callback_data="games")],
    ]
    await safe_edit(
        query,
        "🧟 Resident Evil\n\nبازی موردنظر رو انتخاب کن:",
        keyboard
    )


async def game_info(query, game):
    games = {
        "re2": "🧟 Resident Evil 2\n\n🎮 راهنمای نصب و اجرای بازی\n🛠 رفع خطاهای رایج\n⚙️ تنظیمات پیشنهادی گرافیکی",
        "re3": "🧟 Resident Evil 3\n\n🎮 راهنمای نصب و اجرا\n🛠 رفع خطاهای رایج\n⚙️ تنظیمات گرافیکی",
        "re4": "🧟 Resident Evil 4\n\n🎮 راهنمای نصب و اجرا\n🛠 رفع خطاهای رایج\n⚙️ تنظیمات گرافیکی",
        "re7": "🧟 Resident Evil 7\n\n🎮 راهنمای نصب و اجرا\n🛠 رفع خطاهای رایج\n⚙️ تنظیمات گرافیکی",
        "revillage": "🧟 Resident Evil Village\n\n🎮 راهنمای نصب و اجرا\n🛠 رفع خطاهای رایج\n⚙️ تنظیمات گرافیکی",
        "requiem": "🧟 Resident Evil Requiem\n\n🎮 راهنمای نصب و اجرا\n🛠 رفع خطاهای رایج\n⚙️ تنظیمات گرافیکی",
    }
    keyboard = [
        [InlineKeyboardButton("📥 آموزش نصب", callback_data="install")],
        [InlineKeyboardButton("🛠 رفع خطا", callback_data="errors")],
        [InlineKeyboardButton("🔙 برگشت", callback_data="re")],
    ]
    await safe_edit(query, games.get(game, "اطلاعات این بازی هنوز اضافه نشده است."), keyboard)


# =========================
# INSTALL
# =========================

async def install_menu(query):
    keyboard = [
        [InlineKeyboardButton("🎮 نصب بازی", callback_data="install_game")],
        [InlineKeyboardButton("🧩 نصب پیش‌نیازها", callback_data="prerequisites")],
        [InlineKeyboardButton("💾 نصب درایور کارت گرافیک", callback_data="drivers")],
        [InlineKeyboardButton("🔙 برگشت", callback_data="home")],
    ]
    await safe_edit(
        query,
        "📥 آموزش نصب\n\nیکی از بخش‌های زیر رو انتخاب کن:",
        keyboard
    )


# =========================
# ERRORS
# =========================

async def errors_menu(query):
    keyboard = [
        [InlineKeyboardButton("❌ بازی اجرا نمی‌شود", callback_data="game_not_run")],
        [InlineKeyboardButton("❌ DLL Error", callback_data="dll")],
        [InlineKeyboardButton("❌ DirectX Error", callback_data="directx")],
        [InlineKeyboardButton("❌ Steam Error", callback_data="steam_error")],
        [InlineKeyboardButton("❌ AMD Driver Error", callback_data="amd")],
        [InlineKeyboardButton("❌ صفحه سیاه", callback_data="black_screen")],
        [InlineKeyboardButton("🔙 برگشت", callback_data="home")],
    ]
    await safe_edit(
        query,
        "🛠 رفع خطا\n\nنوع خطایی که داری رو انتخاب کن:",
        keyboard
    )


# =========================
# PC TIPS
# =========================

async def tips_menu(query):
    keyboard = [
        [InlineKeyboardButton("🚀 افزایش FPS", callback_data="fps")],
        [InlineKeyboardButton("🎮 تنظیمات گرافیکی", callback_data="graphics")],
        [InlineKeyboardButton("💻 بهینه‌سازی ویندوز", callback_data="windows")],
        [InlineKeyboardButton("🌡️ بررسی دما", callback_data="temperature")],
        [InlineKeyboardButton("🔙 برگشت", callback_data="home")],
    ]
    await safe_edit(
        query,
        "💻 ترفندهای PC\n\nموضوع موردنظر رو انتخاب کن:",
        keyboard
    )


# =========================
# CALLBACKS
# =========================

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "home":
        await safe_edit(
            query,
            "🖥️ PC FIX\n\nیکی از گزینه‌ها رو انتخاب کن:",
            main_keyboard()
        )

    elif data == "games":
        await games_menu(query)

    elif data == "re":
        await resident_evil_menu(query)

    elif data in ["re2", "re3", "re4", "re7", "revillage", "requiem"]:
        await game_info(query, data)

    elif data == "other_games":
        await safe_edit(
            query,
            "🎮 بازی‌های بیشتر به‌زودی اضافه می‌شوند.",
            [[InlineKeyboardButton("🔙 برگشت", callback_data="games")]]
        )

    elif data == "install":
        await install_menu(query)

    elif data == "install_game":
        await safe_edit(
            query,
            "📥 آموزش نصب بازی\n\n"
            "1️⃣ فایل‌های بازی را در یک پوشه قرار بده.\n"
            "2️⃣ فایل نصب یا Setup را اجرا کن.\n"
            "3️⃣ مسیر نصب را انتخاب کن.\n"
            "4️⃣ بعد از پایان نصب، بازی را اجرا کن.\n\n"
            "اگر هنگام نصب خطا گرفتی، از بخش «رفع خطا» استفاده کن.",
            [[InlineKeyboardButton("🔙 برگشت", callback_data="install")]]
        )

    elif data == "prerequisites":
        await safe_edit(
            query,
            "🧩 پیش‌نیازهای رایج بازی‌ها\n\n"
            "• Microsoft Visual C++ Redistributable\n"
            "• DirectX\n"
            "• .NET Framework\n"
            "• درایور کارت گرافیک\n\n"
            "بسته به بازی ممکن است همه این موارد لازم نباشند.",
            [[InlineKeyboardButton("🔙 برگشت", callback_data="install")]]
        )

    elif data == "drivers":
        await safe_edit(
            query,
            "💾 درایور کارت گرافیک\n\n"
            "برای نصب درایور، نسخه سازگار با مدل کارت گرافیک و نسخه ویندوزت را انتخاب کن.\n\n"
            "اگر مدل کارت گرافیکت را بفرستی، می‌توانی راهنمای مخصوص همان کارت را بگیری.",
            [[InlineKeyboardButton("🔙 برگشت", callback_data="install")]]
        )

    elif data == "errors":
        await errors_menu(query)

    elif data == "game_not_run":
        await safe_edit(
            query,
            "❌ بازی اجرا نمی‌شود\n\n"
            "موارد زیر را بررسی کن:\n"
            "• درایور GPU\n"
            "• DirectX\n"
            "• Visual C++\n"
            "• فضای خالی دیسک\n"
            "• آنتی‌ویروس و Windows Security\n"
            "• فایل‌های بازی",
            [[InlineKeyboardButton("🔙 برگشت", callback_data="errors")]]
        )

    elif data == "dll":
        await safe_edit(
            query,
            "❌ خطای DLL\n\n"
            "معمولاً نصب نبودن یکی از پیش‌نیازهای ویندوز باعث این خطا می‌شود.\n\n"
            "اول Visual C++ Redistributable و DirectX را بررسی کن.",
            [[InlineKeyboardButton("🔙 برگشت", callback_data="errors")]]
        )

    elif data == "directx":
        await safe_edit(
            query,
            "❌ DirectX Error\n\n"
            "• درایور کارت گرافیک را بررسی کن.\n"
            "• DirectX موردنیاز بازی را نصب کن.\n"
            "• سیستم را Restart کن.",
            [[InlineKeyboardButton("🔙 برگشت", callback_data="errors")]]
        )

    elif data == "steam_error":
        await safe_edit(
            query,
            "❌ Steam Error\n\n"
            "اگر بازی به Steam نیاز دارد:\n"
            "• Steam را باز کن.\n"
            "• وارد حساب شو.\n"
            "• اتصال اینترنت را بررسی کن.\n"
            "• بازی را از داخل Steam اجرا کن.",
            [[InlineKeyboardButton("🔙 برگشت", callback_data="errors")]]
        )

    elif data == "amd":
        await safe_edit(
            query,
            "❌ AMD Driver Error\n\n"
            "مدل کارت گرافیک و نسخه ویندوز را بررسی کن.\n"
            "درایور باید دقیقاً با کارت و سیستم‌عامل سازگار باشد.",
            [[InlineKeyboardButton("🔙 برگشت", callback_data="errors")]]
        )

    elif data == "black_screen":
        await safe_edit(
            query,
            "⬛ صفحه سیاه در بازی\n\n"
            "• بازی را یک‌بار با تنظیمات گرافیکی پایین اجرا کن.\n"
            "• درایور GPU را بررسی کن.\n"
            "• Resolution و حالت Fullscreen را بررسی کن.\n"
            "• اگر مشکل ادامه داشت، متن دقیق خطا را بررسی کن.",
            [[InlineKeyboardButton("🔙 برگشت", callback_data="errors")]]
        )

    elif data == "tips":
        await tips_menu(query)

    elif data == "fps":
        await safe_edit(
            query,
            "🚀 افزایش FPS\n\n"
            "• رزولوشن مناسب انتخاب کن.\n"
            "• برنامه‌های غیرضروری پس‌زمینه را ببند.\n"
            "• درایور GPU را به‌روز نگه دار.\n"
            "• تنظیمات سنگین مثل Ray Tracing را در صورت نیاز کاهش بده.",
            [[InlineKeyboardButton("🔙 برگشت", callback_data="tips")]]
        )

    elif data == "graphics":
        await safe_edit(
            query,
            "🎮 تنظیمات گرافیکی\n\n"
            "برای تعادل بین کیفیت و FPS، اول Resolution و سپس Shadow، "
            "Reflection و Volumetric Effects را تنظیم کن.",
            [[InlineKeyboardButton("🔙 برگشت", callback_data="tips")]]
        )

    elif data == "windows":
        await safe_edit(
            query,
            "💻 بهینه‌سازی ویندوز\n\n"
            "• برنامه‌های Startup غیرضروری را مدیریت کن.\n"
            "• فضای دیسک را خالی نگه دار.\n"
            "• Windows و درایورها را بررسی کن.\n"
            "• قبل از تغییرات مهم، Restore Point بساز.",
            [[InlineKeyboardButton("🔙 برگشت", callback_data="tips")]]
        )

    elif data == "temperature":
        await safe_edit(
            query,
            "🌡️ بررسی دما\n\n"
            "برای بررسی دمای CPU و GPU می‌توانی از نرم‌افزارهای مانیتورینگ "
            "سخت‌افزار استفاده کنی و هنگام اجرای بازی دما را زیر نظر بگیری.",
            [[InlineKeyboardButton("🔙 برگشت", callback_data="tips")]]
        )


# =========================
# HELP
# =========================

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🖥️ PC FIX\n\n"
        "/start - منوی اصلی\n"
        "/help - راهنما\n\n"
        "برای استفاده از امکانات، /start را بزن."
    )


# =========================
# MAIN
# =========================

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("PC FIX BOT IS RUNNING...")
    app.run_polling()


if __name__ == "__main__":
    main()
