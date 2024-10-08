from crewai import Agent
from tools import yt_tool

from dotenv import load_dotenv
import os

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_APIKEY')
os.environ['OPENAI_MODEL_NAME'] = os.getenv('OPENAI_MODELNAME')

blog_researcher=Agent(
    role="Blog researcher from Youtube Video",
    goal="get the relevant video content for the topic {topic} from youtube channel",
    verboe=True,
    memory=True,
    backStory=(
        "Expert in understanding videos in AI Data Science, Machine Learning, Gen AI and provide suggestion"
    ),
    tools = [yt_tool],
    allow_delegation=True
)


blog_writer=Agent(
    role="Blog writer",
    goal="Narrate compelling tech stories about the topic {topic} from youtube channel",
    verboe=True,
    memory=True,
    backStory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner"
    ),
    tools = [yt_tool],
    allow_delegation=True
)