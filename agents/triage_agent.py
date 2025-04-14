from crewai import Agent
from langchain.llms import OpenAI

triage_agent = Agent(
  role='Cloud Triage Analyst',
  goal='Classify GuardDuty alerts by severity, category, and likelihood of compromise.',
  llm=OpenAI(temperature=0.3),
  backstory='You specialize in analyzing AWS GuardDuty logs to prioritize alerts based on threat impact.'
)
