import src.config


class SomeContext:
    def initialize_context(self):
        if src.config.settings.dev_mode is True:
            ...
        else:
            raise ValueError("This is unreachable for local dev")


some_context = SomeContext()
