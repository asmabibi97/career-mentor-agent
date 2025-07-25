import os 
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents import AsyncOpenAI
from agents.run import RunConfig
from roadmap_tool import get_career_roadmap

load_dotenv()
gemini_api_key=os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

external_client=AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
model =OpenAIChatCompletionsModel(
    model="gemini-2.0-flash" , openai_client= external_client)
config=RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)
    
career_agent=Agent(
    name="careerAgent",
    instructions="you ask about interests and suggest a career field.",
    model=model
)
skill_agent = Agent(
    name="skillAgent",
    instructions="you share the roadmap using the get_career_roadmap tool.",
    model=model,
    tools=[get_career_roadmap]
)
job_agent=Agent(
    name="jobAgent",
    instructions="you suggest job titles in the chosen career.",
    model=model
)
def main():
    print("/ncareer mentor Agent/n")
    interest=input("what are yout interest?->")

    result1=Runner.run_sync(career_agent, interest,run_config=config)
    field = result1.final_output.strip()
    print("/nsuggested career:",field)

    result2=Runner.run_sync(skill_agent, field,run_config=config)
    print("/nrequired skills:",result2.final_output)

    result3=Runner.run_sync(job_agent,field,run_config=config)
    print("/npossible jobs:",result3.final_output)


if __name__=="__main__":
    main()





