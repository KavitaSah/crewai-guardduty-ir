from crewai import Agent
from langchain.llms import OpenAI

triage_agent = Agent(
  role='Cloud Triage Analyst',
  goal='Prioritize and classify GuardDuty findings by severity and context.',
  llm=OpenAI(temperature=0.3),
  backstory='You analyze and classify security findings using your domain expertise.'
)