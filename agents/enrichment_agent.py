<<<<<<< HEAD
from crewai import Agent
from langchain.llms import OpenAI

enrichment_agent = Agent(
  role='Threat Intelligence Analyst',
  goal='Enhance findings with context using simulated threat intel (e.g., IP reputation, VirusTotal).',
  llm=OpenAI(temperature=0.3),
  backstory='You are experienced in correlating cloud alerts with external threat databases and past incidents.'
)
=======
# Placeholder for enrichment agent
>>>>>>> 8355246dab3d8d504f5458bc34fee55d9972eac1
