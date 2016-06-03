#!/usr/bin/python3

class Module:
    """This is the base class for an exploitation module.

    An exploitation module will provide detection and compromise functionality.

    - Detection is defined as a check to see if a vulnerability exists. The
      detect() function returns a non-None value to indicate exploitability and
      None in the case no exploitation is required or the vulnerability is not
      present.

    - Compromise is defined as the step of actual exploitation and the
      delivering of the payload. In the event of a non-remote-shell exploit such
      as a DOS, the step of delivering the payload can be skipped. In this case,
      the detect function should check for the uptime of the service.

    - The payload variable when implementing this class should be a Payload
      object.
    """

    payload = None

    def detect(self, target):
        """Perform the detection step.

        Identify if the target is exploitable and determine the parameters for
        doing so. Pass the values in the return value.
        """
        pass

    def compromise(self, target, detect_val):
        """Perform the compromise step.

        Trigger the vulnerability and deliver the payload.
        """
        pass
