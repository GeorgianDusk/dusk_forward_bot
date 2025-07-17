import os
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN        = os.getenv("7880440582:AAFA5aqrvkoIOP756Yam9jDGicLGukaKXa8")
SOURCE_ID    = -1001156481225        # source group
DEST_ID      = -1002562832157        # destination channel

async def forward(update, context: ContextTypes.DEFAULT_TYPE):
    # Forward every incoming message to DEST_ID
    await update.message.forward(chat_id=DEST_ID)

def main():
    app = (ApplicationBuilder()
           .token(TOKEN)
           .build())

    # Only accept messages that originate from the source group
    app.add_handler(MessageHandler(filters.Chat(SOURCE_ID) & filters.ALL, forward))

    # --- webhook settings for Render ---
    WEBHOOK_PATH = "/webhook"
    WEBHOOK_URL  = f"https://{os.getenv('RENDER_EXTERNAL_HOSTNAME')}{WEBHOOK_PATH}"

    app.run_webhook(
        listen="0.0.0.0",
        port=int(os.getenv("PORT", 8080)),
        webhook_path=WEBHOOK_PATH,
        webhook_url=WEBHOOK_URL,
    )

if __name__ == "__main__":
    main()
