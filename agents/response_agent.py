<<<<<<< HEAD
from crewai import Agent
from langchain.llms import OpenAI

response_agent = Agent(
  role='IR Recommendation Bot',
  goal='Suggest appropriate response actions and notify security team via Slack.',
  llm=OpenAI(temperature=0.3),
  backstory='You’re a digital incident responder who advises on next steps to isolate, alert, or investigate threats.'
)
=======
# Placeholder for response agent
>>>>>>> 8355246dab3d8d504f5458bc34fee55d9972eac1
