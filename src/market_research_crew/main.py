import warnings
from market_research_crew.crew import MarketResearchCrew, _ants_client
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = {
        "product_idea": "A mobile app that helps users track their daily water intake and provides personalized hydration recommendations based on their activity level, weather conditions, and health goals."
    }

    try:
        MarketResearchCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
    finally:
        _ants_client.flush()
