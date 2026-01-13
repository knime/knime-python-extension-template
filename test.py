from queue import Full, Queue
import sys
from threading import Event, Lock

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

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


class QueuedQtGUI:
    def __init__(self) -> None:
        self.queue: Queue[QtGUIWidget | None] = Queue()
        self._main_loop_lock: Lock = Lock()
        self._main_loop_stopped: bool = False

    def enter(self) -> None:
        while True:
            # Use blocking get() instead of get_nowait() to wait for tasks
            task: QtGUIWidget | None = self.queue.get()

            if task is not None:
                task.run()
                self.queue.task_done()
            else:
                # Poison pill, exit loop.
                self.queue.task_done()
                return

    def exit(self) -> None:
        """
        Exit the main loop and stop further execution.

        This method is used to gracefully exit the main loop and stop any
        further execution. It empties the queue and puts a None value to the
        queue to signal the completion of all tasks.
        If the queue is full, it will continue to try until it can
        successfully put the `None` value into the queue.
        """
        with self._main_loop_lock:
            self._main_loop_stopped = True
            queue: Queue[QtGUIWidget | None] = self.queue
            # Aggressively try to clear queue and insert poison pill.
            while True:
                with queue.all_tasks_done:
                    queue.queue.clear()
                    queue.unfinished_tasks = 0
                try:
                    queue.put_nowait(None)  # Poison pill
                except Full:
                    continue
                else:
                    break

    def execute(self) -> list[str]:
        """
        Run the given function on the main thread, wait for its results and
        return those.
        """
        with self._main_loop_lock:
            if self._main_loop_stopped:
                msg: str = (
                    "Cannot schedule executions on the main thread after the "
                    "main loop stopped."
                )
                raise RuntimeError(msg)
            execute_task: QtGUIWidget = QtGUIWidget()
            self.queue.put(execute_task)
            return execute_task.result()


qt_queue: QueuedQtGUI = QueuedQtGUI()

qt_queue.execute()

qt_queue.enter()
