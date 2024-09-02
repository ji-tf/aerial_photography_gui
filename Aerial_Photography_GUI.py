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
from qgis.gui import QgsFileWidget
from qgis.PyQt.QtWidgets import QFileDialog
from qgis.utils import iface
# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .Aerial_Photography_GUI_dialog import AerialPhotographyGUIDialog
from datetime import datetime
import jinja2
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

        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'AerialPhotographyGUI')
        self.toolbar.setObjectName(u'AerialPhotographyGUI')

        print("** INITIALIZING AerialPhotographyGUI")

        self.pluginIsActive = False
        self.dockwidget = None
        self.summary = {}
        self.plugin_path = os.path.dirname(__file__)

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
            self.dockwidget.radioButton_5.clicked.connect(self.camera_model_5_redo)
            self.dockwidget.radioButton_6.clicked.connect(self.camera_model_6_redo)
            self.dockwidget.button_analysis_txt.clicked.connect(self.analysis_txt)
            self.dockwidget.save.clicked.connect(self.save)
        

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Aerial Photography GUI'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar
        #iface.unregisterOptionsWidgetFactory(self.options_factory)


    def run(self):
        """Run method that performs all the real work"""

        if not self.pluginIsActive:
            self.pluginIsActive = True

            print("** STARTING AerialPhotographyGUI")

            # dockwidget may not exist if:
            #    first run of plugin
            #    removed on close (see self.onClosePlugin method)
            if self.dockwidget == None:
                # Create the dockwidget (after translation) and keep reference
                self.dockwidget = AerialPhotographyGUIDialog()

            # connect to provide cleanup on closing of dockwidget
            #self.dockwidget.closingPlugin.connect(self.onClosePlugin)

            # show the dockwidget
            # TODO: fix to allow choice of dock location
            #self.iface.addDockWidget(Qt.RightDockWidgetArea, self.dockwidget)
            self.dockwidget.show()

    
    def camera_model_5_redo(self):

        self.dockwidget.camera_model.setText('Sony RX1RM2')
        self.dockwidget.focal_len.setText('35')
        self.dockwidget.frame_size_x.setText('7952')
        self.dockwidget.frame_size_y.setText('5304')
        self.dockwidget.spectral_characteristics_photo.setText('RGB')
        self.dockwidget.image_format.setText('JPEG')

    def camera_model_6_redo(self):

        self.dockwidget.camera_model.setText('Sony A6000')
        self.dockwidget.focal_len.setText('20')
        self.dockwidget.frame_size_x.setText('6000')
        self.dockwidget.frame_size_y.setText('4000')
        self.dockwidget.spectral_characteristics_photo.setText('NIR')
        self.dockwidget.image_format.setText('ARW')


    def analysis_txt(self):
        file_path = self.dockwidget.button_choise_txt.filePath()
        file_widget = QgsFileWidget()
        file_widget.setFilePath(file_path)
        #filename, filter = QFileDialog.getOpenFileName(self.dockwidget, 'Выбрать текстовый файл', '', filter='Текстовые файлы (*.txt)')
        #file_widget.setFilePath(filename)

        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            # Выясняем сколько всего строк
            num_lines = len(lines)

        # Создание необходимых списко
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


    def save(self):

        # Список полей
        name_object = self.dockwidget.name_object.text() # Название или шифр объекта съёмки
        filming_location = self.dockwidget.filming_location.text() # Съёмочный участок
        executor = self.dockwidget.executor.currentText() # Исполнитель
        customer = self.dockwidget.customer.text() # Заказчик
        date_start = self.dockwidget.date_start.text() # Дата начала АФС
        date_end = self.dockwidget.date_end.text() # Дата окончания АФС
        nature_area = self.dockwidget.nature_area.currentText() # (Не)Застроенная
        type_shoot = self.dockwidget.type_shoot.text() # Вид съёмки
        area_afs = self.dockwidget.area_afs.text() # Фактическая площадь АФС, для АФС объекта площадного характера
        length_afs = self.dockwidget.length_afs.text() # Фактическая протяжность АФС, км, для АФС линейного объекта
        orientation_route = self.dockwidget.orientation_route.currentText() # Ориентация маршрутов (широтная, меридиональная, заданная)
        overlap_longitudinal = self.dockwidget.overlap_longitudinal.text() # Продольное перекрытие
        overlap_transverse = self.dockwidget.overlap_transverse.text() # Поперечное перекрытие
        height = self.dockwidget.height.text() # Высота фотографирования
        resolution = self.dockwidget.resolution.text() # Номинальное пространственное разрешение, м
        camera_model = self.dockwidget.camera_model.text() # Модель аэрофотокамеры
        camera_sn = self.dockwidget.camera_sn.text() # Серийный номер аэрофотокамеры
        long_shift = self.dockwidget.long_shift.text() # Наличие и тип компенсации продольного сдвига изображения
        focal_len = self.dockwidget.focal_len.text() # Фокусное расстояние аэрофотокамеры, мм
        type_lens = self.dockwidget.type_lens.text() # Тип и серийный номер объектива (если объектив заменяемый)
        frame_size_x = self.dockwidget.frame_size_x.text() # Размер кадра N(x) пикс
        frame_size_y = self.dockwidget.frame_size_y.text() # Размер кадра N(y) пикс
        pixel_size = self.dockwidget.pixel_size.text() # Физический размер пикселя, мм
        coordinate_orientation = self.dockwidget.coordinate_orientation.text() # Ориентация системы координат снимка
        api_type = self.dockwidget.api_type.text() # Тип аэрофотоустановки (гироплатформы)
        api_sn = self.dockwidget.api_sn.text() # Серийный номер аэрофотоустановки (гироплатформы)
        spectral_characteristics_photo = self.dockwidget.spectral_characteristics_photo.text() # Спектральная характеристика аэрофотоснимков
        image_format = self.dockwidget.image_format.text() # Формат представления цифрового изображения
        lidar_type = self.dockwidget.lidar_type.text() # Лидар (тип)
        lidar_sn = self.dockwidget.lidar_sn.text() # Лидар, серийный номер
        definition_block = self.dockwidget.definition_block.text() # Блок определения положения и ориентации, тип, модель, состав
        receiver = self.dockwidget.receiver.text() # ГНСС-приёмник, тип, модель
        other_equipment = self.dockwidget.other_equipment.text() # Прочая аппаратура
        aircraft = self.dockwidget.aircraft.text() # Воздушное судно"))
        add_information = self.dockwidget.add_information.text() # Дополнительные сведения по требованию ТЗ

        #list = [name_object, filming_location, executor, customer, date_start, date_end, nature_area, type_shoot, area_afs, length_afs, orientation_route, overlap_longitudinal,
        #    overlap_transverse, height, resolution, camera_model, camera_sn, long_shift, focal_len, type_lens, frame_size_x, frame_size_y, pixel_size, coordinate_orientation, api_type,
        #    api_sn, spectral_characteristics_photo, image_format, lidar_type, lidar_sn, definition_block, receiver, other_equipment, aircraft]

        fields = [
            {"name_object": name_object,  "filming_location": filming_location, "executor": executor,
            "customer": customer, "date_start": date_start, "date_end": date_end,
            "nature_area": nature_area, "type_shoot": type_shoot, "area_afs": area_afs, "length_afs": length_afs,
            "orientation_route": orientation_route, "overlap_longitudinal": overlap_longitudinal,
            "overlap_transverse": overlap_transverse, "height": height, "resolution": resolution,
            "camera_model": camera_model, "camera_sn": camera_sn, "long_shift": long_shift,
            "focal_len": focal_len, "type_lens": type_lens, "frame_size_x": frame_size_x,
            "frame_size_y": frame_size_y, "pixel_size": pixel_size, "coordinate_orientation": coordinate_orientation,
            "api_type": api_type, "api_sn": api_sn, "spectral_characteristics_photo": spectral_characteristics_photo,
            "image_format": image_format, "lidar_type": lidar_type, "lidar_sn": lidar_sn,
            "definition_block": definition_block, "receiver": receiver, "other_equipment": other_equipment,
            "aircraft": aircraft, "add_information": add_information}
        ]
        
        # Загрузка шаблона из файла
        loader = jinja2.FileSystemLoader('templates')
        environment = jinja2.Environment(loader=loader)
        template = environment.get_template('E:\project\aerial_photography_gui\templates\template_table.html')

        # Рендеринг шаблона для каждого набора данных
        for field in fields:
            filename = f"tableAP111.html"
            content = template.render(field=field)

            # Сохранение отрендеренного шаблона в файл
            with open(filename, mode="w", encoding="utf-8") as message:
                message.write(content)
                print(f"... wrote {filename}")

"""
        # Загрузка шаблона из файла
        template_path = "templates/"
        loader = jinja2.FileSystemLoader(searchpath="templates/")
        environment = jinja2.Environment(loader=loader)
        template = environment.get_template(template_path)

        # Рендеринг шаблона для каждого набора данных
        for field in fields:
            filename = f"1234567.html"
            content = template.render(field=field)

            # Сохранение отрендеренного шаблона в файл
            with open(filename, mode="w", encoding="utf-8") as message:
                message.write(content)
                print(f"... wrote {filename}")
"""