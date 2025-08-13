from .prompt import githu_prompt
from .tool import mcp_github_tools
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

MODEL = "ollama/hf.co/unsloth/Qwen3-8B-GGUF:UD-Q4_K_XL"

github_agent = Agent(
    model=LiteLlm(model=MODEL),
    name="github_agent",
    instruction=githu_prompt,
    tools=[mcp_github_tools]
)

root_agent = github_agent