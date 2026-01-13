import logging
import knime.extension as knext
import sys

from threading import Event
import multiprocessing

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

LOGGER = logging.getLogger(__name__)

class QtGUIWidget:
    def __init__(self) -> None:
        self.app: QApplication
        self.window: QWidget
        self.label: QLabel
        self.button: QPushButton
        self._execute_finished = Event()
        self._button_clicked = False

    def run(self) -> None:
        # PyQt6 and PySide6 - both equal:
        self.app = QApplication(sys.argv)
        self.window = QWidget()
        self.window.setWindowTitle("Qt GUI Widget")

        layout = QVBoxLayout()

        self.label = QLabel("Initial text")
        layout.addWidget(self.label)

        self.button = QPushButton("Click me!")
        self.button.clicked.connect(self.on_button_clicked)
        layout.addWidget(self.button)

        self.window.setLayout(layout)

        # this freezes Knime AP:
        self.window.show()
        # We don't even get here:
        self.app.exec()

        self._execute_finished.set()

    def on_button_clicked(self) -> None:
        if not self._button_clicked:
            # First click: change label and button text
            self.label.setText("Button clicked!")
            self.button.setText("Close me")
            self._button_clicked = True
        else:
            # Second click: close the window
            self.window.close()

    def result(self) -> list[str]:
        return ["a", "b"]


def run_gui_process():
    """Function to be run in a separate process."""
    widget = QtGUIWidget()
    widget.run()

@knext.node(
    name="QT Test Node",
    node_type=knext.NodeType.OTHER,
    icon_path="../../icons/my_icon.png",
    category="/",
)
class MyGUITestNode:
    """
    Short one-line description of the node.

    Long description of the node which is in fact short.
    """

    def configure(
        self,
        configure_context: knext.ConfigurationContext,  # noqa: ARG002
    ) -> None:
        return

    def execute(
        self,
        exec_context: knext.ExecutionContext,
    ) -> None:

        # Start a second process to run the Qt App
        p = multiprocessing.Process(target=run_gui_process)
        p.start()

        # We can wait for it or continue
        p.join()
