import sys
import platform

def is_windows_dark_mode():
    if platform.system() != "Windows":
        return False
    try:
        import winreg
        registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        key = winreg.OpenKey(registry, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
        value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
        return value == 0  # 0 = dark, 1 = light
    except Exception:
        return False

def apply_dark_palette(app):
    from PySide6.QtGui import QPalette, QColor
    palette = QPalette()
    # Fondo principal más oscuro para distinguir de los botones
    palette.setColor(QPalette.Window, QColor(30, 30, 30))
    palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
    palette.setColor(QPalette.Base, QColor(35, 35, 35))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
    palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
    palette.setColor(QPalette.Text, QColor(255, 255, 255))
    # Botones gris oscuro, pero más claro que el fondo principal
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
    palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
    app.setPalette(palette)
    # QSS global para forzar fondo oscuro en QStackedWidget, QTabWidget y sus páginas
    app.setStyleSheet('''
        QStackedWidget, QTabWidget::pane, QTabWidget > QWidget, QTabBar, QWidget {
            background-color: #1e1e1e;
        }
        QTabBar::tab {
            background: #353535;
            color: #fff;
            border: 1px solid #222;
            padding: 6px 12px;
            border-top-left-radius: 4px;
            border-top-right-radius: 4px;
        }
        QTabBar::tab:selected {
            background: #2a82da;
            color: #fff;
        }
        QTabBar::tab:!selected {
            background: #353535;
            color: #bbb;
        }
    ''')

# edicion de colores de botones y letras apartes

    # Añadir estilos personalizados solo para los botones indicados
    extra_qss = '''
    #pushButton,
    #pushButton_5,
    #pushButton_11,
    #pushButton_12,
    #pushButton_50,
    #pushButton_51,
    #pushButton_16,
    #pushButton_17 {
        color: black;
        font-weight: bold;
        font-size: 15px;

    }

    #pushButton_19 {
        color: black;
    }
    #pushButton_21 {
        color: black;
    }
    #pushButton_23 {
        color: black;
    }
    #pushButton_26 {
        color: black;
    }
    #pushButton_37 {
        color: black;
    }
    #pushButton_34 {
        color: black;
    }
    #pushButton_27 {
        color: black;
    }
    #pushButton_36 {
        color: black;
    }
    #pushButton_31 {
        color: black;
    }
    #pushButton_33 {
        color: black;
    }
    #pushButton_40 {
        color: black;
    }

    
    #comboBox_8 {
        color: black;
    }

    #comboBox_9 {
        color: black;
    }

    #comboBox_10 {
        color: black;
    }

    '''
    # Combina el QSS global con el extra
    app.setStyleSheet(app.styleSheet() + extra_qss)