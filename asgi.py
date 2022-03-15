"""Application entry point."""
import uvicorn

if __name__ == "__main__":
    uvicorn.run("twitch_bot:init_script", host="0.0.0.0", port=4000, workers=4)
