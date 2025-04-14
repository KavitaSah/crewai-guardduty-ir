from crewai import Crew, Task
from agents.triage_agent import triage_agent

crew = Crew(
  agents=[triage_agent],
  tasks=[Task("Classify GuardDuty alert")]
)
crew.run()