import httpx
import openai

from xiaogpt.bot.chatgptapi_bot import ChatGPTBot


class QianFanBot(ChatGPTBot):
    name = "千帆"
    default_options = {"model": "deepseek-v3"}

    def __init__(
        self, qianfan_api_key: str, api_base="https://qianfan.baidubce.com/v2"
    ) -> None:
        self.qianfan_api_key = qianfan_api_key
        self.api_base = api_base
        self.history: list[tuple[str, str]] = []

    def _make_openai_client(self, sess: httpx.AsyncClient) -> openai.AsyncOpenAI:
        return openai.AsyncOpenAI(
            api_key=self.qianfan_api_key, http_client=sess, base_url=self.api_base
        )

    @classmethod
    def from_config(cls, config):
        return cls(
            qianfan_api_key=config.qianfan_api_key,
            api_base="https://qianfan.baidubce.com/v2",
        )
