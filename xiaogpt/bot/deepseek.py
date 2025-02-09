import httpx
import openai

from xiaogpt.bot.chatgptapi_bot import ChatGPTBot


class DeepSeekBot(ChatGPTBot):
    name = "DeepSeek"
    default_options = {"model": "deepseek-chat"}

    def __init__(
        self, deepseek_api_key: str, api_base="https://api.deepseek.com/v1"
    ) -> None:
        self.deepseek_api_key = deepseek_api_key
        self.api_base = api_base
        self.history: list[tuple[str, str]] = []

    def _make_openai_client(self, sess: httpx.AsyncClient) -> openai.AsyncOpenAI:
        return openai.AsyncOpenAI(
            api_key=self.deepseek_api_key, http_client=sess, base_url=self.api_base
        )

    @classmethod
    def from_config(cls, config):
        return cls(
            deepseek_api_key=config.deepseek_api_key,
            api_base="https://api.deepseek.com/v1",
        )
