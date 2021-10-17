from repository.databaseRepository import DatabaseRepository
from controller.controller import Controller
# from userinterface.consoleUserInterface import ConsoleUI
from userinterface.graphicalUserInterface import GraphicalUI

repository = DatabaseRepository()
controller = Controller(repository)

# consoleUI = ConsoleUI(controller)
# consoleUI.start()
# consoleUI.close_connection()

graphicalUI = GraphicalUI(controller)
graphicalUI.start_sing_in_window()
