from dotenv import load_dotenv
load_dotenv()
import os

from EvoAgent.DeepResearchAgent import DeepResearchAgent

llm_config = {
    "config_list": 
    [
        {
            #"api_type": "openai", 
            "model": "gpt-4o",
            "base_url": os.environ["OPENAI_BASE_URL"],
            "api_key": os.environ["OPENAI_API_KEY"]
        }
    ]
}

agent = DeepResearchAgent(
    name="DeepResearchAgent",
    llm_config=llm_config,
)

message = "四川大学杨雨豪在ACM-ICPC程序设计竞赛的成就"

result = agent.run(
    message=message,
    tools=agent.tools,
    max_turns=2,
    user_input=False,
    summary_method="reflection_with_llm",
)

print(result.summary)