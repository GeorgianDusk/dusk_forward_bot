import os
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# ------------------------------------------------------------------
# CONFIGURATION – edit the three values below
# ------------------------------------------------------------------
SOURCE_ID = -1001156481225        # numeric ID of the group you copy FROM
DEST_ID   = -1002562832157        # numeric ID of the channel you post TO
TOKEN     = os.getenv("BOT_TOKEN")  # set this in Render’s Environment tab
# ------------------------------------------------------------------

async def forward(update, context: ContextTypes.DEFAULT_TYPE):
    """Forward every incoming message from SOURCE_ID to DEST_ID."""
    await update.message.forward(chat_id=DEST_ID)

def main() -> None:
    app = (
        ApplicationBuilder()
        .token(TOKEN)
        .build()
    )

    # Trigger only on messages that come from the specific source group
    app.add_handler(MessageHandler(filters.Chat(SOURCE_ID) & filters.ALL, forward))

    # --- Webhook settings for Render free tier ---
    WEBHOOK_PATH = "/webhook"
    host = os.getenv("RENDER_EXTERNAL_HOSTNAME", "localhost")
    WEBHOOK_URL  = f"https://{host}{WEBHOOK_PATH}"

    app.run_webhook(
        listen="0.0.0.0",
        port=int(os.getenv("PORT", 8080)),
        url_path=WEBHOOK_PATH,
        webhook_url=WEBHOOK_URL,
    )

if __name__ == "__main__":
    main()
