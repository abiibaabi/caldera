from app.utility.base_world import BaseWorld


class Obfuscation(BaseWorld):

    def __init__(self, agent):
        self.agent = agent

    def run(self, link):
        return self.decode_bytes(link.command)