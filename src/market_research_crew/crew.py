import atexit
import logging

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from dotenv import load_dotenv
from ants_platform import AntsPlatform
from ants_platform.crewai import EventListener

load_dotenv()

_logger = logging.getLogger("ants_crew_init")

_pk = "pk-ap-ee83027c-f011-448e-aa65-7bf5fe857ee7"
_sk = "sk-ap-2c13e4d7-33b4-4157-8051-0b2424929910"
_host = "https://app.agenticants.ai"


# _pk = "pk-ap-12a80feb-7740-43e1-a252-7384f299396b"
# _sk = "sk-ap-092bbf57-17a1-455a-a3c2-61b83ae12bba"
# _host = "http://localhost:3000"

_logger.warning("ANTS_INIT PK=%s SK=%s HOST=%s", bool(_pk), bool(_sk), _host)

_ants_client = AntsPlatform(public_key=_pk, secret_key=_sk, host=_host, timeout=30)
_ants_listener = EventListener(
    public_key=_pk,
    agent_name="market_research_crew",
    agent_display_name="Market Research Crew v1.0",
)
atexit.register(_ants_client.flush)

_logger.warning("ANTS_INIT_DONE")

# create the tools for the agent
web_search_tool = SerperDevTool()
web_scraping_tool = ScrapeWebsiteTool()

toolkit = [web_search_tool, web_scraping_tool]

# define the crew class
@CrewBase
class MarketResearchCrew():
    """MarketResearchCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # provide the path for configuration files
    agents_config = "config/agents.yaml" 
    tasks_config = "config/tasks.yaml"
    
    # ================ Agents ========================
    
    @agent
    def market_research_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["market_research_specialist"],
            tools=toolkit
        )

    @agent
    def competitive_intelligence_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["competitive_intelligence_analyst"],
            tools=toolkit
        )
        
    @agent
    def customer_insights_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["customer_insights_researcher"],
            tools=toolkit
        )
        
    @agent
    def product_strategy_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config["product_strategy_advisor"],
            tools=toolkit
        )
        
    @agent
    def business_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["business_analyst"],
            tools=toolkit
        )
        
    # ================ Tasks ======================
    
    @task
    def market_research_task(self) -> Task:
        return Task(
            config=self.tasks_config["market_research_task"]
        )
        
    @task
    def competitive_intelligence_task(self) -> Task:
        return Task(
            config=self.tasks_config["competitive_intelligence_task"],
            context=[self.market_research_task()]
        )
        
    @task
    def customer_insights_task(self) -> Task:
        return Task(
            config=self.tasks_config["customer_insights_task"],
            context=[self.market_research_task(),
                     self.competitive_intelligence_task()]
        )
        
    @task
    def product_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config["product_strategy_task"],
            context=[self.market_research_task(),
                     self.competitive_intelligence_task(),
                     self.customer_insights_task()]
        )
        
    @task
    def business_analyst_task(self) -> Task:
        return Task(
            config=self.tasks_config["business_analyst_task"],
            context=[self.market_research_task(),
                     self.competitive_intelligence_task(),
                     self.customer_insights_task(),
                     self.product_strategy_task()],
            output_file="reports/report.md"
        )
        
    # ================= Crew ===========================
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential
        )