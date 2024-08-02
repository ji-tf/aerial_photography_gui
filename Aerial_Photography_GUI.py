# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AerialPhotographyGUI
                                 A QGIS plugin
 Plugin for aerial photography
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2024-07-29
        git sha              : $Format:%H$
        copyright            : (C) 2024 by Violet
        email                : madarich18@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction

# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .Aerial_Photography_GUI_dialog import AerialPhotographyGUIDialog
from datetime import datetime
import pandas as pd
import os.path

class AerialPhotographyGUI:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'AerialPhotographyGUI_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Aerial Photography GUI')

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('AerialPhotographyGUI', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/Aerial_Photography_GUI/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Aerial Photography GUI'),
            callback=self.run,
            parent=self.iface.mainWindow())
        if self.dockwidget == None:
            # Create the dockwidget (after translation) and keep reference
            self.dockwidget = AerialPhotographyGUIDialog()
            self.dockwidget.radioButton.clicked.connect(self.chang_camera)
            self.dockwidget.analysisTXTButton.clicked.connect(self.analysis_txt)
            self.dockwidget.saveButton.helpRequested.connect(self.save_file_tabl)
        
        # will be set False in run()
        self.first_start = True


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Aerial Photography GUI'),
                action)
            self.iface.removeToolBarIcon(action)


    def run(self):
        """Run method that performs all the real work"""

        # Create the dialog with elements (after translation) and keep reference
        # Only create GUI ONCE in callback, so that it will only load when the plugin is started
        if self.first_start == True:
            self.first_start = False
            self.dlg = AerialPhotographyGUIDialog()

        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            pass


    def chang_camera(self):
        """"Переключение камеры в полях"""
        
        def camera_model_3_redo():
            self.camera_model_3.setText('Sony RX1RM2')
            self.focal_len_3.setText('35')
            self.frame_size_x_3.setText('7952')
            self.frame_size_y_3.setText('5304')
            self.spectral_characteristics_photo_3.setText('RGB')
            self.image_format_3.setText('JPEG')

        def camera_model_3_redo2():
            self.camera_model_3.setText('Sony A6000')
            self.focal_len_3.setText('20')
            self.frame_size_x_3.setText('6000')
            self.frame_size_y_3.setText('4000')
            self.spectral_characteristics_photo_3.setText('NIR')
            self.image_format_3.setText('ARW')


    def analysis_txt(self):
        """"Анализ текстового файла файла"""
        # Необходимо выбирать файл из строки
        with open('E:/project/111.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            # Выясняем сколько всего строк
            num_lines = len(lines)

        # Создание необходимых списков
        list_file_number = [] # Все номера снимков
        list_yaw = [] # Все значения yaw
        list_number_m = [] # Номера маршрутов
        list_number_end = [] # Номера концевых снимков
        list_average = []  # Новый список для средних значений
        course = [] # Курс
        course_gms = [] # Курс в формате(градусы, минуты, секунды)

        for i in range(6, num_lines, 1):
            string = lines[i].split()
            file_number = string[0]
            yaw = string[6]

            # Приводим дату к привычному виду
            date_str = string[7]
            date_obj = datetime.strptime(date_str, "%Y.%m.%d")
            new_date_str = date_obj.strftime("%d.%m.%Y")

            yaw_new = float(yaw)
            list_file_number.append(file_number[-7:-4])
            list_yaw.append(yaw_new)

        # Создаём списки (номера концевых аэрофотоснимков, номера маршрутов)
        num = 0
        for i in range(1, len(list_yaw)):
            if list_yaw[i] * list_yaw[i - 1] < 0:
                num += 1
                list_number_end.append(list_file_number[i - 1])
                list_number_m.append(num)

        # Индекс первого изменения знака
        sign_change_index = -1
        for i in range(1, len(list_yaw)):
            if list_yaw[i] * list_yaw[i - 1] < 0:
                sign_change_index = i
                break

        # Вычисляем среднее значение от нулевого элемента до первого изменения знака
        if sign_change_index > 0:
            average = sum(list_yaw[:sign_change_index]) / sign_change_index
            list_average.append(average)

        # Вычисляем средние значения для оставшихся частей списка
        for i in range(sign_change_index + 1, len(list_yaw)):
            if list_yaw[i] * list_yaw[i - 1] < 0:
                # Вычисляем среднее значение от предыдущего изменения знака до текущего
                average = sum(list_yaw[sign_change_index:i]) / (i - sign_change_index)
                #print(list_yaw[sign_change_index:i])
                list_average.append(average)
                sign_change_index = i

        # Добавляем последнее среднее значение
        average = sum(list_yaw[sign_change_index:]) / (len(list_yaw) - sign_change_index)
        list_average.append(average)

        # Добавляем последние значения в списки (номера концевых аэрофотоснимков, номера маршрутов)
        list_number_end.append(list_file_number[-1])
        list_number_m.append(num + 1)

        # Курс
        for i, list_average in enumerate(list_average):
                course.append(round(list_average, 4))

        for i, course in enumerate(course):
            num_yaw = course
            int_num_yaw = round(num_yaw//1)
            minute = (num_yaw - int_num_yaw) * 60
            int_min = round(minute//1)
            second = (minute - int_min) *60
            int_sec = round(second)
            course_gms.append(f"{int_num_yaw}{"\u00B0"}{int_min}{"'"}{int_sec}{'"'}")

        #data = [[new_date_str], [list_number_m], [course_gms], [list_number_end]]
        df = pd.DataFrame({'Дата аэрофотосъёмки': new_date_str,
                        'Номер маршрута': list_number_m,
                            'Курс': course_gms,
                            'Номера концевых аэрофотоснимков': list_number_end
                            })

        print(df)
        df.to_html('E:/project/test.html', index=False)


    def save_file_tabl(self):
        pass