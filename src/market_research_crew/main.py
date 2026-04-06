from ants_platform import AntsPlatform
from ants_platform.crewai import EventListener
import warnings
from market_research_crew.crew import MarketResearchCrew
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")



def run():
    """
    Run the crew.
    """
    
    # Initialize Ants Platform observability
    ants_platform = AntsPlatform(timeout=30)
    listener = EventListener(
        agent_name="market_research_crew",
        agent_display_name="Market Research Crew v1.0",
    )
    
    inputs = {
        "product_idea": "A mobile app that helps users track their daily water intake and provides personalized hydration recommendations based on their activity level, weather conditions, and health goals."
    }

    try:
        MarketResearchCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
    finally:
        ants_platform.flush()
