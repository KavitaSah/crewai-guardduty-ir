# CrewAI GuardDuty IR Agent

<<<<<<< HEAD
This is a multi-agent AI system using [CrewAI](https://github.com/joaomdmoura/crewai) to automate classification, enrichment, and incident response for AWS GuardDuty alerts.

## 🧠 What It Does

- Classifies GuardDuty alerts using an LLM agent
- Enriches findings with threat intelligence (simulated)
- Sends a summary to Slack
- Modular agents for future IR workflows

## 🔧 Architecture

```bash
GuardDuty ➜ Triage Agent ➜ Enrichment Agent ➜ Response Agent ➜ Slack
```

Each agent uses a LangChain LLM under the hood, coordinated by CrewAI.

## 🧪 Setup

```bash
git clone https://github.com/kavitasah/crewai-guardduty-ir.git
cd crewai-guardduty-ir
cp .env.example .env
pip install -r requirements.txt
python workflows/alert_response_crew.py
```

## ⚙️ Environment Variables

Create `.env` based on the following:
```env
OPENAI_API_KEY=your-key-here
SLACK_WEBHOOK=https://hooks.slack.com/services/xxx/yyy/zzz
```

## 🐳 Docker Support

```bash
docker build -t crewai-ir .
docker run --env-file .env crewai-ir
```

## ☁️ EC2/GCP

1. SSH into your cloud instance  
2. Pull the repo + install Python  
3. Run using `python workflows/alert_response_crew.py`

## 📜 License

Apache 2.0 - use it, improve it, and give credit ❤️
=======
A CrewAI-based agent system for classifying and responding to GuardDuty alerts with Slack integration.
>>>>>>> 8355246dab3d8d504f5458bc34fee55d9972eac1
