from PySide6.QtWidgets import QApplication
from archivos_py.windows.inicio_login import Inicio
import sys
from archivos_py.windows.inicio_minimarket import MainWindow


# inicio del login
#if __name__ == "__main__":
#    app = QApplication(sys.argv)
#    app.setStyle("Fusion")
#    window = Inicio()
#    window.show()
#    sys.exit(app.exec())


# inicio del minimarket solo para pruebas
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    print("se inicia el minimarket")
    main_window = MainWindow(usuario="mariano", account="Administrador")
    main_window.resize(1690, 900)
    main_window.show()
    sys.exit(app.exec())

