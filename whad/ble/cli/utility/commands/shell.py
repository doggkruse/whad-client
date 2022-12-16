"""BLE Interactive shell
"""

from prompt_toolkit import print_formatted_text, HTML
from whad.cli.app import command
from whad.ble import Scanner
from whad.ble.cli.utility.shell import BleUtilityShell

@command('interactive')
def interactive_handler(app, command_args):
    """interactive BLE shell

    <ansicyan><b>interactive</b></ansicyan>

    Starts an interactive shell and let you interact with a BLE WHAD device:
    - scan devices
    - connect to a device
    - list services and characteristics
    - read/write characteristics
    """
    # We need to have an interface specified
    if app.interface is not None:
        # Launch an interactive shell
        myshell = BleUtilityShell(app.interface)
        myshell.run()
    else:
        app.error('You need to specify an interface with option --interface.')