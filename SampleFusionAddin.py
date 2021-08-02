import adsk.core, adsk.fusion, adsk.cam, traceback

from .fusion_addin_framework import fusion_addin_framework as faf

import logging

addin = None


def say_hi(event_args: adsk.core.CommandEventArgs):
    adsk.core.Application.get().userInterface.messageBox("hi")


def run(context):
    logger = logging.getLogger(faf.__name__)
    logger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler()
    logger.addHandler(stream_handler)
    palette_handler = faf.utils.TextPaletteLoggingHandler()
    logger.addHandler(palette_handler)

    # alternativly you can use this utiltiy function
    # faf.utils.create_logger(
    #     faf.__name__,
    #     [logging.StreamHandler(), faf.utils.TextPaletteLoggingHandler()],
    # )

    global addin
    addin = faf.FusionAddin()
    ws = faf.Workspace(parent=addin, id="FusionSolidEnvironment")
    tab = faf.Tab(parent=ws, id="SolidTab")
    panel = faf.Panel(parent=tab, id="SolidCreatePanel")
    control = faf.Control(parent=panel, isPromoted=True)
    cmd = faf.AddinCommand(parent=control, onExecute=say_hi, name="my command")


def stop(context):
    addin.stop()
