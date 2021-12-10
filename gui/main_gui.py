# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.gui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QRect, Qt, QDate)

from PyQt5.QtWidgets import (QCheckBox, QDateEdit, QFormLayout,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QListWidget, QMenuBar, QProgressBar, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1037, 1129)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_10 = QGridLayout(self.groupBox)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_10.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_10.setContentsMargins(9, -1, -1, -1)
        self.groupBox_setting = QGroupBox(self.groupBox)
        self.groupBox_setting.setObjectName("groupBox_3")
        self.groupBox_setting.setFlat(True)
        self.groupBox_setting.setCheckable(True)
        self.groupBox_setting.setChecked(False)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_setting)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_standard = QRadioButton(self.groupBox_setting)
        self.radioButton_standard.setObjectName("radioButton_5")
        self.radioButton_standard.setChecked(True)
        self.horizontalLayout_2.addWidget(self.radioButton_standard)
        self.radioButton_json = QRadioButton(self.groupBox_setting)
        self.radioButton_json.setObjectName("radioButton_6")
        self.horizontalLayout_2.addWidget(self.radioButton_json)
        self.radioButton_xml = QRadioButton(self.groupBox_setting)
        self.radioButton_xml.setObjectName("radioButton_7")
        self.horizontalLayout_2.addWidget(self.radioButton_xml)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.gridLayout_10.addWidget(self.groupBox_setting, 2, 0, 1, 1)
        self.progressBar = QProgressBar(self.groupBox)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)
        self.gridLayout_10.addWidget(self.progressBar, 1, 0, 1, 1)
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.gridLayout_9.addItem(self.verticalSpacer_2, 1, 0, 1, 2)
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setPlaceholderText("Укажите строку поиск")
        font = self.lineEdit.font()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.gridLayout_9.addWidget(self.lineEdit, 0, 0, 1, 2)
        self.pushButton_directory = QPushButton(self.groupBox)
        self.pushButton_directory.setObjectName("pushButton_2")
        self.gridLayout_9.addWidget(self.pushButton_directory, 2, 0, 1, 1)
        self.pushButton_search = QPushButton(self.groupBox)
        self.pushButton_search.setObjectName("pushButton_3")
        self.gridLayout_9.addWidget(self.pushButton_search, 2, 1, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.stackedWidget = QStackedWidget(self.groupBox)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QWidget()
        self.page.setObjectName("page")
        self.verticalLayout = QVBoxLayout(self.page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QScrollArea(self.page)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 958, 631))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.formLayout_23 = QFormLayout()
        self.formLayout_23.setObjectName("formLayout_23")
        self.formLayout_23.setVerticalSpacing(3)
        self.checkBox_standard_date_modification = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_standard_date_modification.setObjectName("checkBox_47")
        self.formLayout_23.setWidget(0, QFormLayout.LabelRole, self.checkBox_standard_date_modification)
        self.current_date = QDate()
        self.dateEdit_7 = QDateEdit(self.scrollAreaWidgetContents)
        self.dateEdit_7.setDate(self.current_date.currentDate())
        self.dateEdit_7.setObjectName("dateEdit_7")
        self.formLayout_23.setWidget(0, QFormLayout.FieldRole, self.dateEdit_7)
        self.checkBox_standard_file_name = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_standard_file_name.setObjectName("checkBox_48")
        self.formLayout_23.setWidget(1, QFormLayout.LabelRole, self.checkBox_standard_file_name)
        self.lineEdit_13 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_13.setPlaceholderText('Пример: "test, file". Результат: ["test.txt", "my_test.json", "file1.xml"]')
        self.formLayout_23.setWidget(1, QFormLayout.FieldRole, self.lineEdit_13)
        self.verticalLayout_34.addLayout(self.formLayout_23)
        self.groupBox_standard_file_format = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_standard_file_format.setObjectName("groupBox_24")
        self.groupBox_standard_file_format.setFlat(True)
        self.groupBox_standard_file_format.setCheckable(True)
        self.groupBox_standard_file_format.setChecked(False)
        self.formLayout_24 = QFormLayout(self.groupBox_standard_file_format)
        self.formLayout_24.setObjectName("formLayout_24")
        self.formLayout_25 = QFormLayout()
        self.formLayout_25.setObjectName("formLayout_25")
        self.checkBox_txt = QCheckBox(self.groupBox_standard_file_format)
        self.checkBox_txt.setObjectName("checkBox_49")
        self.checkBox_txt.setChecked(True)
        self.formLayout_25.setWidget(0, QFormLayout.LabelRole, self.checkBox_txt)
        self.checkBox_log = QCheckBox(self.groupBox_standard_file_format)
        self.checkBox_log.setObjectName("checkBox_50")
        self.checkBox_log.setChecked(True)
        self.formLayout_25.setWidget(0, QFormLayout.FieldRole, self.checkBox_log)
        self.checkBox_xml = QCheckBox(self.groupBox_standard_file_format)
        self.checkBox_xml.setObjectName("checkBox_51")
        self.checkBox_xml.setChecked(True)
        self.formLayout_25.setWidget(1, QFormLayout.LabelRole, self.checkBox_xml)
        self.checkBox_json = QCheckBox(self.groupBox_standard_file_format)
        self.checkBox_json.setObjectName("checkBox_52")
        self.checkBox_json.setChecked(True)
        self.formLayout_25.setWidget(1, QFormLayout.FieldRole, self.checkBox_json)
        self.label_6 = QLabel(self.groupBox_standard_file_format)
        self.label_6.setObjectName("label_6")
        self.formLayout_25.setWidget(2, QFormLayout.LabelRole, self.label_6)
        self.lineEdit_14 = QLineEdit(self.groupBox_standard_file_format)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_14.setPlaceholderText('Пример: doc, docx, md')
        self.formLayout_25.setWidget(2, QFormLayout.FieldRole, self.lineEdit_14)
        self.formLayout_24.setLayout(0, QFormLayout.SpanningRole, self.formLayout_25)
        self.verticalLayout_34.addWidget(self.groupBox_standard_file_format)
        self.verticalLayout_8.addLayout(self.verticalLayout_34)
        self.groupBox_17 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_17.setObjectName("groupBox_17")
        self.groupBox_17.setFlat(True)
        self.groupBox_17.setCheckable(True)
        self.groupBox_17.setChecked(False)
        self.verticalLayout_35 = QVBoxLayout(self.groupBox_17)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        # self.groupBox_28 = QGroupBox(self.groupBox_17)
        # self.groupBox_28.setObjectName("groupBox_28")
        # self.horizontalLayout_9 = QHBoxLayout(self.groupBox_28)
        # self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        # self.formLayout_2 = QFormLayout()
        # self.formLayout_2.setObjectName("formLayout_2")
        # self.radioButton_standard_sinc = QRadioButton(self.groupBox_28)
        # self.radioButton_standard_sinc.setObjectName("radioButton_3")
        # self.radioButton_standard_sinc.setChecked(True)
        # self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.radioButton_standard_sinc)
        # self.radioButton_standard_asinc = QRadioButton(self.groupBox_28)
        # self.radioButton_standard_asinc.setObjectName("radioButton_4")
        # self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.radioButton_standard_asinc)
        # self.horizontalLayout_9.addLayout(self.formLayout_2)
        # self.verticalLayout_35.addWidget(self.groupBox_28)
        self.groupBox_25 = QGroupBox(self.groupBox_17)
        self.groupBox_25.setObjectName("groupBox_25")
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_25)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.formLayout_26 = QFormLayout()
        self.formLayout_26.setObjectName("formLayout_26")
        self.radioButton_standard_str = QRadioButton(self.groupBox_25)
        self.radioButton_standard_str.setObjectName("radioButton_29")
        self.radioButton_standard_str.setChecked(True)
        self.formLayout_26.setWidget(0, QFormLayout.LabelRole, self.radioButton_standard_str)
        self.radioButton_standard_no_str = QRadioButton(self.groupBox_25)
        self.radioButton_standard_no_str.setObjectName("radioButton_30")
        self.formLayout_26.setWidget(0, QFormLayout.FieldRole, self.radioButton_standard_no_str)
        self.horizontalLayout_8.addLayout(self.formLayout_26)
        self.verticalLayout_35.addWidget(self.groupBox_25)
        self.groupBox_26 = QGroupBox(self.groupBox_17)
        self.groupBox_26.setObjectName("groupBox_26")
        self.groupBox_26.setCheckable(False)
        self.groupBox_26.setChecked(False)
        self.verticalLayout_36 = QVBoxLayout(self.groupBox_26)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.radioButton_standard_no_reg = QRadioButton(self.groupBox_26)
        self.radioButton_standard_no_reg.setObjectName("radioButton_31")
        self.radioButton_standard_no_reg.setChecked(True)
        self.verticalLayout_37.addWidget(self.radioButton_standard_no_reg)
        self.radioButton_standard_reg = QRadioButton(self.groupBox_26)
        self.radioButton_standard_reg.setObjectName("radioButton_32")
        self.verticalLayout_37.addWidget(self.radioButton_standard_reg)
        self.radioButton_standard_st = QRadioButton(self.groupBox_26)
        self.radioButton_standard_st.setObjectName("radioButton_33")
        self.verticalLayout_37.addWidget(self.radioButton_standard_st)
        self.radioButton_standard_en = QRadioButton(self.groupBox_26)
        self.radioButton_standard_en.setObjectName("radioButton_34")
        self.verticalLayout_37.addWidget(self.radioButton_standard_en)
        self.radioButton_standard_re = QRadioButton(self.groupBox_26)
        self.radioButton_standard_re.setObjectName("radioButton_35")
        self.verticalLayout_37.addWidget(self.radioButton_standard_re)
        self.verticalLayout_36.addLayout(self.verticalLayout_37)
        self.verticalLayout_35.addWidget(self.groupBox_26)
        self.groupBox_27 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_27.setObjectName("groupBox_27")
        self.groupBox_27.setFlat(True)
        self.groupBox_27.setCheckable(True)
        self.groupBox_27.setChecked(False)
        self.verticalLayout_38 = QVBoxLayout(self.groupBox_27)
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.checkBox_standard_path = QCheckBox(self.groupBox_27)
        self.checkBox_standard_path.setObjectName("checkBox_53")
        self.checkBox_standard_path.setChecked(True)
        self.verticalLayout_39.addWidget(self.checkBox_standard_path)
        self.checkBox_standard_count = QCheckBox(self.groupBox_27)
        self.checkBox_standard_count.setObjectName("checkBox_54")
        self.checkBox_standard_count.setChecked(True)
        self.verticalLayout_39.addWidget(self.checkBox_standard_count)
        self.checkBox_standard_search_str = QCheckBox(self.groupBox_27)
        self.checkBox_standard_search_str.setObjectName("checkBox_55")
        self.checkBox_standard_display_modification_date = QCheckBox(self.groupBox_27)
        self.verticalLayout_39.addWidget(self.checkBox_standard_search_str)
        self.verticalLayout_39.addWidget(self.checkBox_standard_display_modification_date)
        self.verticalLayout_38.addLayout(self.verticalLayout_39)
        self.verticalLayout_8.addWidget(self.groupBox_17)
        self.verticalLayout_7.addLayout(self.verticalLayout_8)
        self.verticalLayout_7.addWidget(self.groupBox_27)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_2 = QVBoxLayout(self.page_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea_2 = QScrollArea(self.page_3)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 351, 347))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.formLayout_27 = QFormLayout()
        self.formLayout_27.setObjectName("formLayout_27")
        self.formLayout_27.setVerticalSpacing(3)
        self.checkBox_date_modification = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_date_modification.setObjectName("checkBox_56")
        self.formLayout_27.setWidget(0, QFormLayout.LabelRole, self.checkBox_date_modification)
        self.dateEdit_8 = QDateEdit(self.scrollAreaWidgetContents_2)
        self.dateEdit_8.setDate(self.current_date.currentDate())
        self.dateEdit_8.setObjectName("dateEdit_8")
        self.formLayout_27.setWidget(0, QFormLayout.FieldRole, self.dateEdit_8)
        self.checkBox_file_name = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_file_name.setObjectName("checkBox_57")
        self.formLayout_27.setWidget(1, QFormLayout.LabelRole, self.checkBox_file_name)
        self.lineEdit_15 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_15.setPlaceholderText('Пример: "test, file". Результат: ["test.txt", "my_test.json", "file1.xml"]')
        self.formLayout_27.setWidget(1, QFormLayout.FieldRole, self.lineEdit_15)
        self.verticalLayout_40.addLayout(self.formLayout_27)
        self.verticalLayout_10.addLayout(self.verticalLayout_40)
        self.groupBox_18 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_18.setObjectName("groupBox_18")
        self.groupBox_18.setFlat(True)
        self.groupBox_18.setCheckable(True)
        self.groupBox_18.setChecked(False)
        self.verticalLayout_41 = QVBoxLayout(self.groupBox_18)
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        #self.groupBox_30 = QGroupBox(self.groupBox_18)
        #self.groupBox_30.setObjectName("groupBox_30")
        #self.horizontalLayout_10 = QHBoxLayout(self.groupBox_30)
        #self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        #self.formLayout_3 = QFormLayout()
        #self.formLayout_3.setObjectName("formLayout_3")
        #self.radioButton_sinc = QRadioButton(self.groupBox_30)
        #self.radioButton_sinc.setObjectName("radioButton_8")
        #self.radioButton_sinc.setChecked(True)
        #self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.radioButton_sinc)
        #self.radioButton_asinc = QRadioButton(self.groupBox_30)
        #self.radioButton_asinc.setObjectName("radioButton_9")
        #self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.radioButton_asinc)
        #self.horizontalLayout_10.addLayout(self.formLayout_3)
        #self.verticalLayout_41.addWidget(self.groupBox_30)
        self.groupBox_29 = QGroupBox(self.groupBox_18)
        self.groupBox_29.setObjectName("groupBox_29")
        self.groupBox_29.setCheckable(False)
        self.groupBox_29.setChecked(False)
        self.verticalLayout_42 = QVBoxLayout(self.groupBox_29)
        self.verticalLayout_42.setObjectName("verticalLayout_42")
        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.radioButton_tag_key = QRadioButton(self.groupBox_29)
        self.radioButton_tag_key.setObjectName("radioButton_36")
        self.radioButton_tag_key.setChecked(True)
        self.verticalLayout_43.addWidget(self.radioButton_tag_key)
        self.radioButton_value = QRadioButton(self.groupBox_29)
        self.radioButton_value.setObjectName("radioButton_37")
        self.verticalLayout_43.addWidget(self.radioButton_value)
        self.verticalLayout_42.addLayout(self.verticalLayout_43)
        self.verticalLayout_41.addWidget(self.groupBox_29)
        self.groupBox_33 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_33.setObjectName("groupBox_33")
        self.groupBox_33.setFlat(True)
        self.groupBox_33.setCheckable(True)
        self.groupBox_33.setChecked(False)
        self.verticalLayout_44 = QVBoxLayout(self.groupBox_33)
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        self.verticalLayout_45 = QVBoxLayout()
        self.verticalLayout_45.setObjectName("verticalLayout_45")
        self.checkBox_path = QCheckBox(self.groupBox_33)
        self.checkBox_path.setObjectName("checkBox_62")
        self.checkBox_path.setChecked(True)
        self.verticalLayout_45.addWidget(self.checkBox_path)
        self.checkBox_count = QCheckBox(self.groupBox_33)
        self.checkBox_count.setObjectName("checkBox_63")
        self.checkBox_count.setChecked(True)
        self.checkBox_display_modification_date = QCheckBox(self.groupBox_33)
        self.verticalLayout_45.addWidget(self.checkBox_count)
        self.verticalLayout_45.addWidget(self.checkBox_display_modification_date)
        self.verticalLayout_44.addLayout(self.verticalLayout_45)
        self.verticalLayout_10.addWidget(self.groupBox_18)
        self.verticalLayout_9.addLayout(self.verticalLayout_10)
        self.verticalLayout_9.addWidget(self.groupBox_33)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea_2)
        self.stackedWidget.addWidget(self.page_3)
        self.gridLayout_10.addWidget(self.stackedWidget, 3, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_4)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_12 = QGridLayout(self.groupBox_2)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.listWidget_2 = QListWidget(self.groupBox_2)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout_11.addWidget(self.listWidget_2, 0, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_11, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_5)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.version = QLabel("version")
        self.version.setAlignment(Qt.AlignCenter)
        self.verticalLayout_3.addWidget(self.version)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1037, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "File search Wizard 3.0", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", "Поиск файла", None))
        self.groupBox_setting.setTitle(QCoreApplication.translate("MainWindow", "Настройки", None))
        self.radioButton_standard.setText(QCoreApplication.translate("MainWindow", "Стандартный поиск", None))
        self.radioButton_json.setText(QCoreApplication.translate("MainWindow", "Поиск в JSON", None))
        self.radioButton_xml.setText(QCoreApplication.translate("MainWindow", "Поиск в XML", None))
        self.pushButton_directory.setText(QCoreApplication.translate("MainWindow", "Выбор дериктории", None))
        self.pushButton_search.setText(QCoreApplication.translate("MainWindow", "Поиск", None))
        self.checkBox_standard_date_modification.setText(QCoreApplication.translate("MainWindow", "Поиск по дате модификации файла", None))
        self.checkBox_standard_file_name.setText(QCoreApplication.translate("MainWindow", "Поиск с учетом имени файла", None))
        self.groupBox_standard_file_format.setTitle(QCoreApplication.translate("MainWindow", "Настройка форматов файла", None))
        self.checkBox_txt.setText(QCoreApplication.translate("MainWindow", ".txt", None))
        self.checkBox_log.setText(QCoreApplication.translate("MainWindow", ".log", None))
        self.checkBox_xml.setText(QCoreApplication.translate("MainWindow", ".xml", None))
        self.checkBox_json.setText(QCoreApplication.translate("MainWindow", ".json", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", "Свои варианты", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", "Настройки поиска", None))
        #self.groupBox_28.setTitle(QCoreApplication.translate("MainWindow", "Режим работы", None))
        #self.radioButton_standard_sinc.setText(QCoreApplication.translate("MainWindow", "Синхронный режим", None))
        #self.radioButton_standard_asinc.setText(QCoreApplication.translate("MainWindow", "Асинхронноый режим", None))
        self.groupBox_25.setTitle(QCoreApplication.translate("MainWindow", "Варианты чтения файла", None))
        self.radioButton_standard_str.setText(QCoreApplication.translate("MainWindow", "Построчное чтение файла", None))
        self.radioButton_standard_no_str.setText(QCoreApplication.translate("MainWindow", "Чтение файла целиком", None))
        self.groupBox_26.setTitle(QCoreApplication.translate("MainWindow", "Варианты поиска в файле", None))
        self.radioButton_standard_no_reg.setText(QCoreApplication.translate("MainWindow", "Поиск без учета регистра", None))
        self.radioButton_standard_reg.setText(QCoreApplication.translate("MainWindow", "Поиск с учетом регистра", None))
        self.radioButton_standard_st.setText(QCoreApplication.translate("MainWindow", "Поиск в начале строки", None))
        self.radioButton_standard_en.setText(QCoreApplication.translate("MainWindow", "Поиск в конце строки", None))
        self.radioButton_standard_re.setText(QCoreApplication.translate("MainWindow", "Поиск RegEx", None))
        self.groupBox_27.setTitle(QCoreApplication.translate("MainWindow", "Настройки отображения результатов поиска", None))
        self.checkBox_standard_path.setText(QCoreApplication.translate("MainWindow", "Показывать путь к файлу", None))
        self.checkBox_standard_count.setText(QCoreApplication.translate("MainWindow", "Показывать кол-во повторений текста", None))
        self.checkBox_standard_search_str.setText(QCoreApplication.translate("MainWindow", "Показывать строку с искомым текстом", None))
        self.checkBox_standard_display_modification_date.setText(QCoreApplication.translate("MainWindow", "Показывать дату модификации файла", None))
        self.checkBox_date_modification.setText(QCoreApplication.translate("MainWindow", "Поиск по дате модификации файла", None))
        self.checkBox_file_name.setText(QCoreApplication.translate("MainWindow", "Поиск с учетом имени файла", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("MainWindow", "Настройки поиска", None))
        #self.groupBox_30.setTitle(QCoreApplication.translate("MainWindow", "Режим работы", None))
        #self.radioButton_sinc.setText(QCoreApplication.translate("MainWindow", "Синхронный режим", None))
        #self.radioButton_asinc.setText(QCoreApplication.translate("MainWindow", "Асинхронноый режим", None))
        self.groupBox_29.setTitle(QCoreApplication.translate("MainWindow", "Варианты поиска в файле", None))
        self.radioButton_tag_key.setText(QCoreApplication.translate("MainWindow", "По ключу/тегу", None))
        self.radioButton_value.setText(QCoreApplication.translate("MainWindow", "По занчению", None))
        self.groupBox_33.setTitle(QCoreApplication.translate("MainWindow", "Настройки отображения результатов поиска", None))
        self.checkBox_path.setText(QCoreApplication.translate("MainWindow", "Показывать путь к файлу", None))
        self.checkBox_count.setText(QCoreApplication.translate("MainWindow", "Показывать кол-во повторений текста", None))
        self.checkBox_display_modification_date.setText(QCoreApplication.translate("MainWindow", "Показывать дату модификации файла", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", "Найденые файлы", None))
    # retranslateUi
