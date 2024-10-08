from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer


research_task = Task(
    description=(
        'Identify the video {topic}',
        'Get detailed information about the video from the channel.'
    ),
    expected_output='A comprehensive 3 paragraphs long report based on the {topic} of video content.',
    tools=[yt_tool],
    agent=blog_researcher
)

writer_task = Task(
    # output_file='new-blog-post.md'
    description=(
        'get the info from the youtube channel on the topic {topic}.'
    ),
    expected_output='Summarize the info from the youtube channel video on the topic {topic} and create the content for my blog',
    tools=[yt_tool],
    agent=blog_writer
    # async_execution=False
)