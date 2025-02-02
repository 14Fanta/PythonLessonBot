import asyncio
import logging


from app.handlers import dp,bot,user_router

async def main():
    dp.include_router(user_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        print("Bot started")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")