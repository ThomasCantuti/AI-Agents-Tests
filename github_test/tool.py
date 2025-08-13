import os
from dotenv import load_dotenv

from google.adk.tools.openapi_tool.auth.auth_helpers import token_to_scheme_credential
from google.adk.tools.mcp_tool import MCPToolset, StreamableHTTPConnectionParams


load_dotenv()
GITHUB_PERSONAL_ACCESS_TOKEN = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")

github_auth_scheme, github_auth_credential = token_to_scheme_credential(
  token_type='apikey',
  location='header',
  name="GitHub-Token",
  credential_value=GITHUB_PERSONAL_ACCESS_TOKEN
)

mcp_github_tools = MCPToolset(
    connection_params=StreamableHTTPConnectionParams(
        url="https://api.githubcopilot.com/mcp/",
        headers={
            "Authorization": "Bearer " + GITHUB_PERSONAL_ACCESS_TOKEN,
        },
    ),
    auth_credential=github_auth_credential,
    auth_scheme=github_auth_scheme,
    tool_filter=["get_me"]
)