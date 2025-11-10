from __future__ import annotations


class LlmStub:
    """
    Very simple LLM stub.

    For now it just echoes the prompt with a fixed phrase.
    Later you can replace this with a real client (OpenAI, etc.).
    """

    def generate(self, prompt: str) -> str:
        """
        Generate a fake answer for the given prompt.

        Parameters
        ----------
        prompt : str
            Input prompt.

        Returns
        -------
        str
            Stub answer.
        """
        return (
            f"Model answer to: {prompt}\n\n"
            "(This is a stub model. In a real harness, this would be replaced "
            "by a call to an actual LLM API.)"
        )
