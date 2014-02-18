from burp import IBurpExtender
from burp import IBurpExtenderCallbacks
from burp import IIntruderPayloadProcessor
from java.io import PrintWriter

class BurpExtender(IBurpExtender, IIntruderPayloadProcessor):
  def registerExtenderCallbacks(self, callbacks):
    self._callbacks = callbacks
    self._helpers = callbacks.getHelpers()

    # Register methods for error reporting
    self.stdout = PrintWriter(callbacks.getStdout(), True)
    self.stderr = PrintWriter(callbacks.getStderr(), True)

    self.stdout.println("Module loaded successfully!")
    callbacks.setExtensionName('Simple Burp Intruder Payload Processor')
    callbacks.registerIntruderPayloadProcessor(self)
    return

    def getProcessorName():
        return "Capitalize Payload Process"

    def processPayload(currentPayload, originalPayload, baseValue):
        try:
            # Data will be outputted to Burp UI by default
            self.stdout.println("currentPayload: %s" % currentPayload)
            newPayload = capitalize(currentPayload)
            self.stdout.println("newPayload: %s" % newPayload)
        except:
            print "Unexpected error:", sys.exc_info()[0]

        return newPayload

    def capitalize(data):
        # A simple function that will capitalize strings
        self.stdout.println("data: %s" % data)
        return data.upper()
