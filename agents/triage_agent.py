from crewai import Agent
from langchain.llms import OpenAI

triage_agent = Agent(
  role='Cloud Triage Analyst',
<<<<<<< HEAD
  goal='Classify GuardDuty alerts by severity, category, and likelihood of compromise.',
  llm=OpenAI(temperature=0.3),
  backstory='You specialize in analyzing AWS GuardDuty logs to prioritize alerts based on threat impact.'
)
=======
  goal='Prioritize and classify GuardDuty findings by severity and context.',
  llm=OpenAI(temperature=0.3),
  backstory='You analyze and classify security findings using your domain expertise.'
)
>>>>>>> 8355246dab3d8d504f5458bc34fee55d9972eac1
