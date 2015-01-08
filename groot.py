import logging
import random

from kitnirc.client import Channel
from kitnirc.modular import Module


_log = logging.getLogger(__name__)


class GrootModule(Module):
    """Be Groot."""

    last_reply = {}

    @Module.handle("PRIVMSG")
    def respond(self, client, actor, recipient, message):
        if isinstance(recipient, Channel):
            if not ("groot" in message.lower() or message.lower().startswith("bot rave")):
                return
        reply = self.choose_reply(recipient)
        _log.info("{}: <{}> {}".format(recipient, actor.split("!")[0], message))
        _log.info("{}: <{}> {}".format(recipient, client.user.nick, reply))
        client.reply(recipient, actor, reply)
        return True

    def choose_reply(self, recipient):
        last = self.last_reply.get(recipient)
        _log.info("Last reply in {} was '{}'.".format(recipient, last))
        reply = self.generate_reply()
        while reply == last:
            _log.info("Matched, regenerating.")
            reply = self.generate_reply()
        self.last_reply[recipient] = reply
        return reply

    def generate_reply(self):
        reply = ""
        if not random.randrange(15):
            reply += "... "
        reply += "I "
        if not random.randrange(5):
            reply += "... "
        reply += "am "
        if not random.randrange(10):
            reply += "... "
        reply += "Groot"
        endpunct = random.randrange(100)
        if endpunct < 3:
            reply += "?"
        elif endpunct < 10:
            reply += " ..."
        elif endpunct < 50:
            reply += "!"
        else:
            reply += "."
        return reply


module = GrootModule

# vim: set ts=4 sts=4 sw=4 et:
