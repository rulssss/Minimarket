from PySide6.QtWidgets import QApplication
from archivos_py.windows.inicio_login import Inicio
import sys
from archivos_py.windows.inicio_minimarket import MainWindow
from archivos_py.windows.inicio_login_web import InicioWeb

#inicio del login web
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = InicioWeb()
    window.show()
    sys.exit(app.exec())

##
# inicio del login pruebas del login rls
#if __name__ == "__main__":
#    app = QApplication(sys.argv)
#    app.setStyle("Fusion")
#    window = Inicio()
#    window.show()
#    sys.exit(app.exec())


# inicio del minimarket SOLO para pruebas ya que se abre el minimarket sin loguin
#if __name__ == "__main__":
#    app = QApplication(sys.argv)
#    app.setStyle("Fusion")
#    print("se inicia el minimarket")
#    main_window = MainWindow(usuario="mariano", account="Administrador")
#    main_window.resize(1690, 900)
#    main_window.show()
#    sys.exit(app.exec())    



