import twitchio
from config import TWITCH_CALLBACK_ROUTE, TWITCH_CLIENT_ID, TWITCH_CLIENT_SECRET
from twitchio.ext import commands, eventsub

esbot = commands.Bot.from_client_credentials(
    client_id=TWITCH_CLIENT_ID, client_secret=TWITCH_CLIENT_SECRET
)
esclient = eventsub.EventSubClient(
    esbot, webhook_secret="...", callback_route=TWITCH_CALLBACK_ROUTE
)


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token="...", prefix="!", initial_channels=["channel"])

    async def __ainit__(self) -> None:
        self.loop.create_task(esclient.listen(port=4000))
        try:
            await esclient.subscribe_channel_follows(broadcaster=channel_ID)
        except twitchio.HTTPException:
            pass

    async def event_ready(self):
        print("Bot is ready!")


bot = Bot()
bot.loop.run_until_complete(bot.__ainit__())


@esbot.event()
async def event_eventsub_notification_follow(
    payload: eventsub.ChannelFollowData,
) -> None:
    print("Received event!")
    channel = bot.get_channel("channel")
    await channel.send(f"{payload.data.user.name} followed woohoo!")


bot.run()
