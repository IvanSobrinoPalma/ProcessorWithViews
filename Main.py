from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
from views.MainWindows import MainWindows
import sys
import json

if __name__ == "__main__":
    
    # Importar el fichero de opciones
    json_file = open("configuration\inputs.json", "r")
    json_file = json_file.read()
    json_content = json.loads(json_file)

    # Inicializar la applicación
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    main = MainWindows(json_content, widget)
    widget.addWidget(main)
    widget.setFixedHeight(260)
    widget.setFixedWidth(430)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Saliendo")


