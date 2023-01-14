import logging
import unittest

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

import rfcontrol.helpers as helpers


class TestHelpers(unittest.TestCase):
    def test_pulses2binary(self) -> None:
        binary = helpers.pulses2binary(
            "020001000100010001010000010100000100010001010001000001010001000100000100010001000100010001000100010100000100010001000100010100010003",
            [["02", ""], ["0100", "1"], ["0001", "0"], ["03", ""]],
        )
        self.assertEquals("00001010001101110000000010000011", binary)

    def test_binary2pulses(self) -> None:
        pulses = helpers.binary2pulses(
            "00001010001101110000000010000011", {"1": "0100", "0": "0001"}
        )
        self.assertEquals(
            "00010001000100010100000101000001000100010100010000010100010001000001000100010001000100010001000101000001000100010001000101000100",
            pulses,
        )
