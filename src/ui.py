from PyQt6 import QtWidgets, QtGui, QtCore

try:
    from .text_analysis import analyze_text
    from .expert_db import find_experts
except ImportError:  # allow running as a script
    from text_analysis import analyze_text
    from expert_db import find_experts


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("سامانه پیشنهاد کارشناس")
        self.resize(800, 600)
        self._setup_ui()

    def _setup_ui(self):
        central = QtWidgets.QWidget()
        self.setCentralWidget(central)
        layout = QtWidgets.QVBoxLayout(central)

        self.order_edit = QtWidgets.QTextEdit()
        self.order_edit.setPlaceholderText("متن قرار کارشناسی را وارد کنید")
        layout.addWidget(self.order_edit)

        self.analyze_btn = QtWidgets.QPushButton("تحلیل متن")
        self.analyze_btn.clicked.connect(self.on_analyze)
        layout.addWidget(self.analyze_btn)

        self.category_list = QtWidgets.QListWidget()
        layout.addWidget(self.category_list)

        self.competency_list = QtWidgets.QListWidget()
        layout.addWidget(self.competency_list)

        human_layout = QtWidgets.QHBoxLayout()
        layout.addLayout(human_layout)
        human_layout.addWidget(QtWidgets.QLabel("انتخاب عامل انسانی:"))
        self.human_combo = QtWidgets.QComboBox()
        self.human_combo.addItems(["کارشناس", "هیات کارشناسی"])
        human_layout.addWidget(self.human_combo)

        self.expert_list = QtWidgets.QListWidget()
        layout.addWidget(self.expert_list)

        # اعمال یک استایل ساده نئومورفیسم
        self.setStyleSheet("""
            QWidget {
                background: #E0E0E0;
                font-family: Tahoma;
                font-size: 14px;
            }
            QTextEdit, QListWidget, QComboBox {
                border-radius: 10px;
                padding: 10px;
                background: #E0E0E0;
                box-shadow: inset 5px 5px 10px #bebebe,
                            inset -5px -5px 10px #ffffff;
            }
            QPushButton {
                border-radius: 10px;
                padding: 10px;
                background: #E0E0E0;
                box-shadow: 5px 5px 10px #bebebe,
                            -5px -5px 10px #ffffff;
            }
            QPushButton:pressed {
                box-shadow: inset 5px 5px 10px #bebebe,
                            inset -5px -5px 10px #ffffff;
            }
        """)

    def on_analyze(self):
        text = self.order_edit.toPlainText()
        categories, competencies = analyze_text(text)
        self.category_list.clear()
        for c in categories:
            self.category_list.addItem(c)
        self.competency_list.clear()
        for comp in competencies:
            self.competency_list.addItem(comp)
        # نمایش کارشناسان برای اولین رشته پیشنهادی
        if categories:
            experts = find_experts(categories[0])
            self.expert_list.clear()
            for ex in experts:
                self.expert_list.addItem(f"{ex.name} - {ex.category}")

