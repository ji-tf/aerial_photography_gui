# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Aerial_Photography_GUI_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AerialPhotographyGUIDialogBase(object):
    def setupUi(self, AerialPhotographyGUIDialogBase):
        AerialPhotographyGUIDialogBase.setObjectName("AerialPhotographyGUIDialogBase")
        AerialPhotographyGUIDialogBase.resize(1038, 600)
        self.centralwidget = QtWidgets.QWidget(AerialPhotographyGUIDialogBase)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setObjectName("clear")
        self.gridLayout_12.addWidget(self.clear, 2, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(1020, 530))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -153, 1001, 841))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.object = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.object.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.object.setFrameShadow(QtWidgets.QFrame.Raised)
        self.object.setObjectName("object")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.object)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.date_start_4 = QtWidgets.QDateEdit(self.object)
        self.date_start_4.setEnabled(True)
        self.date_start_4.setObjectName("date_start_4")
        self.gridLayout_9.addWidget(self.date_start_4, 2, 1, 1, 1)
        self.label_name_object_4 = QtWidgets.QLabel(self.object)
        self.label_name_object_4.setObjectName("label_name_object_4")
        self.gridLayout_9.addWidget(self.label_name_object_4, 0, 0, 1, 1)
        self.name_object_4 = QtWidgets.QLineEdit(self.object)
        self.name_object_4.setText("")
        self.name_object_4.setObjectName("name_object_4")
        self.gridLayout_9.addWidget(self.name_object_4, 0, 1, 1, 1)
        self.nature_area_4 = QtWidgets.QComboBox(self.object)
        self.nature_area_4.setObjectName("nature_area_4")
        self.nature_area_4.addItem("")
        self.nature_area_4.addItem("")
        self.gridLayout_9.addWidget(self.nature_area_4, 3, 1, 1, 1)
        self.label_date_start_4 = QtWidgets.QLabel(self.object)
        self.label_date_start_4.setObjectName("label_date_start_4")
        self.gridLayout_9.addWidget(self.label_date_start_4, 2, 0, 1, 1)
        self.label_orientation_route_4 = QtWidgets.QLabel(self.object)
        self.label_orientation_route_4.setObjectName("label_orientation_route_4")
        self.gridLayout_9.addWidget(self.label_orientation_route_4, 6, 0, 1, 4)
        self.label_filming_location_4 = QtWidgets.QLabel(self.object)
        self.label_filming_location_4.setObjectName("label_filming_location_4")
        self.gridLayout_9.addWidget(self.label_filming_location_4, 0, 3, 1, 1)
        self.label_overlap_transverse_4 = QtWidgets.QLabel(self.object)
        self.label_overlap_transverse_4.setObjectName("label_overlap_transverse_4")
        self.gridLayout_9.addWidget(self.label_overlap_transverse_4, 7, 3, 1, 1)
        self.date_end_4 = QtWidgets.QDateEdit(self.object)
        self.date_end_4.setObjectName("date_end_4")
        self.gridLayout_9.addWidget(self.date_end_4, 2, 4, 1, 1)
        self.executor_4 = QtWidgets.QComboBox(self.object)
        self.executor_4.setObjectName("executor_4")
        self.executor_4.addItem("")
        self.executor_4.setItemText(0, "")
        self.executor_4.addItem("")
        self.executor_4.addItem("")
        self.gridLayout_9.addWidget(self.executor_4, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem, 0, 2, 1, 1)
        self.overlap_longitudinal_4 = QtWidgets.QLineEdit(self.object)
        self.overlap_longitudinal_4.setObjectName("overlap_longitudinal_4")
        self.gridLayout_9.addWidget(self.overlap_longitudinal_4, 7, 1, 1, 1)
        self.orientation_route_4 = QtWidgets.QComboBox(self.object)
        self.orientation_route_4.setObjectName("orientation_route_4")
        self.orientation_route_4.addItem("")
        self.orientation_route_4.setItemText(0, "")
        self.orientation_route_4.addItem("")
        self.orientation_route_4.addItem("")
        self.orientation_route_4.addItem("")
        self.gridLayout_9.addWidget(self.orientation_route_4, 6, 4, 1, 1)
        self.label_customer_4 = QtWidgets.QLabel(self.object)
        self.label_customer_4.setObjectName("label_customer_4")
        self.gridLayout_9.addWidget(self.label_customer_4, 1, 3, 1, 1)
        self.filming_location_4 = QtWidgets.QLineEdit(self.object)
        self.filming_location_4.setText("")
        self.filming_location_4.setObjectName("filming_location_4")
        self.gridLayout_9.addWidget(self.filming_location_4, 0, 4, 1, 1)
        self.label_area_afs_4 = QtWidgets.QLabel(self.object)
        self.label_area_afs_4.setObjectName("label_area_afs_4")
        self.gridLayout_9.addWidget(self.label_area_afs_4, 4, 0, 1, 4)
        self.type_shoot_4 = QtWidgets.QLineEdit(self.object)
        self.type_shoot_4.setObjectName("type_shoot_4")
        self.gridLayout_9.addWidget(self.type_shoot_4, 3, 4, 1, 1)
        self.label_date_end_4 = QtWidgets.QLabel(self.object)
        self.label_date_end_4.setObjectName("label_date_end_4")
        self.gridLayout_9.addWidget(self.label_date_end_4, 2, 3, 1, 1)
        self.area_afs_4 = QtWidgets.QLineEdit(self.object)
        self.area_afs_4.setObjectName("area_afs_4")
        self.gridLayout_9.addWidget(self.area_afs_4, 4, 4, 1, 1)
        self.label_overlap_longitudinal_4 = QtWidgets.QLabel(self.object)
        self.label_overlap_longitudinal_4.setObjectName("label_overlap_longitudinal_4")
        self.gridLayout_9.addWidget(self.label_overlap_longitudinal_4, 7, 0, 1, 1)
        self.label_nature_area_4 = QtWidgets.QLabel(self.object)
        self.label_nature_area_4.setObjectName("label_nature_area_4")
        self.gridLayout_9.addWidget(self.label_nature_area_4, 3, 0, 1, 1)
        self.customer_4 = QtWidgets.QLineEdit(self.object)
        self.customer_4.setText("")
        self.customer_4.setObjectName("customer_4")
        self.gridLayout_9.addWidget(self.customer_4, 1, 4, 1, 1)
        self.label_type_shoot_4 = QtWidgets.QLabel(self.object)
        self.label_type_shoot_4.setObjectName("label_type_shoot_4")
        self.gridLayout_9.addWidget(self.label_type_shoot_4, 3, 3, 1, 1)
        self.label_length_afs_4 = QtWidgets.QLabel(self.object)
        self.label_length_afs_4.setObjectName("label_length_afs_4")
        self.gridLayout_9.addWidget(self.label_length_afs_4, 5, 0, 1, 4)
        self.length_afs_4 = QtWidgets.QLineEdit(self.object)
        self.length_afs_4.setObjectName("length_afs_4")
        self.gridLayout_9.addWidget(self.length_afs_4, 5, 4, 1, 1)
        self.label_executor_4 = QtWidgets.QLabel(self.object)
        self.label_executor_4.setObjectName("label_executor_4")
        self.gridLayout_9.addWidget(self.label_executor_4, 1, 0, 1, 1)
        self.overlap_transverse_4 = QtWidgets.QLineEdit(self.object)
        self.overlap_transverse_4.setObjectName("overlap_transverse_4")
        self.gridLayout_9.addWidget(self.overlap_transverse_4, 7, 4, 1, 1)
        self.verticalLayout_2.addWidget(self.object)
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_5.setObjectName("radioButton_5")
        self.horizontalLayout_3.addWidget(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_6.setObjectName("radioButton_6")
        self.horizontalLayout_3.addWidget(self.radioButton_6)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.camera_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.camera_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.camera_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.camera_3.setObjectName("camera_3")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.camera_3)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_api_sn_5 = QtWidgets.QLabel(self.camera_3)
        self.label_api_sn_5.setObjectName("label_api_sn_5")
        self.gridLayout_10.addWidget(self.label_api_sn_5, 6, 4, 1, 1)
        self.label_camera_sn_5 = QtWidgets.QLabel(self.camera_3)
        self.label_camera_sn_5.setObjectName("label_camera_sn_5")
        self.gridLayout_10.addWidget(self.label_camera_sn_5, 1, 4, 1, 1)
        self.label_focal_len_5 = QtWidgets.QLabel(self.camera_3)
        self.label_focal_len_5.setObjectName("label_focal_len_5")
        self.gridLayout_10.addWidget(self.label_focal_len_5, 3, 0, 1, 2)
        self.label_long_shift_5 = QtWidgets.QLabel(self.camera_3)
        self.label_long_shift_5.setObjectName("label_long_shift_5")
        self.gridLayout_10.addWidget(self.label_long_shift_5, 2, 0, 1, 3)
        self.label_type_lens_5 = QtWidgets.QLabel(self.camera_3)
        self.label_type_lens_5.setObjectName("label_type_lens_5")
        self.gridLayout_10.addWidget(self.label_type_lens_5, 3, 4, 1, 1)
        self.focal_len_5 = QtWidgets.QLineEdit(self.camera_3)
        self.focal_len_5.setObjectName("focal_len_5")
        self.gridLayout_10.addWidget(self.focal_len_5, 3, 2, 1, 1)
        self.image_format_5 = QtWidgets.QLineEdit(self.camera_3)
        self.image_format_5.setObjectName("image_format_5")
        self.gridLayout_10.addWidget(self.image_format_5, 8, 5, 1, 1)
        self.pixel_size_5 = QtWidgets.QLineEdit(self.camera_3)
        self.pixel_size_5.setObjectName("pixel_size_5")
        self.gridLayout_10.addWidget(self.pixel_size_5, 5, 2, 1, 1)
        self.resolution_5 = QtWidgets.QLineEdit(self.camera_3)
        self.resolution_5.setObjectName("resolution_5")
        self.gridLayout_10.addWidget(self.resolution_5, 0, 5, 1, 1)
        self.height_5 = QtWidgets.QLineEdit(self.camera_3)
        self.height_5.setObjectName("height_5")
        self.gridLayout_10.addWidget(self.height_5, 0, 2, 1, 1)
        self.label_spectral_characteristics_photo_5 = QtWidgets.QLabel(self.camera_3)
        self.label_spectral_characteristics_photo_5.setObjectName("label_spectral_characteristics_photo_5")
        self.gridLayout_10.addWidget(self.label_spectral_characteristics_photo_5, 7, 4, 1, 1)
        self.type_lens_5 = QtWidgets.QLineEdit(self.camera_3)
        self.type_lens_5.setObjectName("type_lens_5")
        self.gridLayout_10.addWidget(self.type_lens_5, 3, 5, 1, 1)
        self.frame_size_x_5 = QtWidgets.QLineEdit(self.camera_3)
        self.frame_size_x_5.setObjectName("frame_size_x_5")
        self.gridLayout_10.addWidget(self.frame_size_x_5, 4, 2, 1, 1)
        self.label_camera_model_5 = QtWidgets.QLabel(self.camera_3)
        self.label_camera_model_5.setObjectName("label_camera_model_5")
        self.gridLayout_10.addWidget(self.label_camera_model_5, 1, 0, 1, 1)
        self.frame_size_y_5 = QtWidgets.QLineEdit(self.camera_3)
        self.frame_size_y_5.setObjectName("frame_size_y_5")
        self.gridLayout_10.addWidget(self.frame_size_y_5, 4, 5, 1, 1)
        self.long_shift_5 = QtWidgets.QLineEdit(self.camera_3)
        self.long_shift_5.setObjectName("long_shift_5")
        self.gridLayout_10.addWidget(self.long_shift_5, 2, 4, 1, 2)
        self.label_api_type_5 = QtWidgets.QLabel(self.camera_3)
        self.label_api_type_5.setObjectName("label_api_type_5")
        self.gridLayout_10.addWidget(self.label_api_type_5, 6, 0, 1, 1)
        self.coordinate_orientation_5 = QtWidgets.QLineEdit(self.camera_3)
        self.coordinate_orientation_5.setObjectName("coordinate_orientation_5")
        self.gridLayout_10.addWidget(self.coordinate_orientation_5, 5, 5, 1, 1)
        self.label_resolution_5 = QtWidgets.QLabel(self.camera_3)
        self.label_resolution_5.setObjectName("label_resolution_5")
        self.gridLayout_10.addWidget(self.label_resolution_5, 0, 4, 1, 1)
        self.label_frame_size_y_5 = QtWidgets.QLabel(self.camera_3)
        self.label_frame_size_y_5.setObjectName("label_frame_size_y_5")
        self.gridLayout_10.addWidget(self.label_frame_size_y_5, 4, 4, 1, 1)
        self.camera_model_5 = QtWidgets.QLineEdit(self.camera_3)
        self.camera_model_5.setObjectName("camera_model_5")
        self.gridLayout_10.addWidget(self.camera_model_5, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem1, 0, 3, 1, 1)
        self.api_type_5 = QtWidgets.QLineEdit(self.camera_3)
        self.api_type_5.setObjectName("api_type_5")
        self.gridLayout_10.addWidget(self.api_type_5, 6, 2, 1, 1)
        self.label_coordinate_orientation_5 = QtWidgets.QLabel(self.camera_3)
        self.label_coordinate_orientation_5.setObjectName("label_coordinate_orientation_5")
        self.gridLayout_10.addWidget(self.label_coordinate_orientation_5, 5, 4, 1, 1)
        self.label_frame_size_x_5 = QtWidgets.QLabel(self.camera_3)
        self.label_frame_size_x_5.setObjectName("label_frame_size_x_5")
        self.gridLayout_10.addWidget(self.label_frame_size_x_5, 4, 0, 1, 1)
        self.label_pixel_size_5 = QtWidgets.QLabel(self.camera_3)
        self.label_pixel_size_5.setObjectName("label_pixel_size_5")
        self.gridLayout_10.addWidget(self.label_pixel_size_5, 5, 0, 1, 1)
        self.spectral_characteristics_photo_5 = QtWidgets.QLineEdit(self.camera_3)
        self.spectral_characteristics_photo_5.setObjectName("spectral_characteristics_photo_5")
        self.gridLayout_10.addWidget(self.spectral_characteristics_photo_5, 7, 5, 1, 1)
        self.label_image_format_5 = QtWidgets.QLabel(self.camera_3)
        self.label_image_format_5.setObjectName("label_image_format_5")
        self.gridLayout_10.addWidget(self.label_image_format_5, 8, 4, 1, 1)
        self.api_sn_5 = QtWidgets.QLineEdit(self.camera_3)
        self.api_sn_5.setObjectName("api_sn_5")
        self.gridLayout_10.addWidget(self.api_sn_5, 6, 5, 1, 1)
        self.camera_sn_5 = QtWidgets.QLineEdit(self.camera_3)
        self.camera_sn_5.setObjectName("camera_sn_5")
        self.gridLayout_10.addWidget(self.camera_sn_5, 1, 5, 1, 1)
        self.label_height_5 = QtWidgets.QLabel(self.camera_3)
        self.label_height_5.setObjectName("label_height_5")
        self.gridLayout_10.addWidget(self.label_height_5, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.camera_3)
        self.equipment = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.equipment.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.equipment.setFrameShadow(QtWidgets.QFrame.Raised)
        self.equipment.setObjectName("equipment")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.equipment)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_other_equipment_3 = QtWidgets.QLabel(self.equipment)
        self.label_other_equipment_3.setObjectName("label_other_equipment_3")
        self.gridLayout_11.addWidget(self.label_other_equipment_3, 3, 0, 1, 2)
        self.lidar_type_3 = QtWidgets.QLineEdit(self.equipment)
        self.lidar_type_3.setObjectName("lidar_type_3")
        self.gridLayout_11.addWidget(self.lidar_type_3, 0, 1, 1, 1)
        self.label_lidar_sn_3 = QtWidgets.QLabel(self.equipment)
        self.label_lidar_sn_3.setObjectName("label_lidar_sn_3")
        self.gridLayout_11.addWidget(self.label_lidar_sn_3, 0, 3, 1, 1)
        self.add_information = QtWidgets.QLineEdit(self.equipment)
        self.add_information.setText("")
        self.add_information.setObjectName("add_information")
        self.gridLayout_11.addWidget(self.add_information, 5, 2, 1, 3)
        self.label_definition_block_3 = QtWidgets.QLabel(self.equipment)
        self.label_definition_block_3.setObjectName("label_definition_block_3")
        self.gridLayout_11.addWidget(self.label_definition_block_3, 1, 0, 1, 2)
        self.label_receiver_3 = QtWidgets.QLabel(self.equipment)
        self.label_receiver_3.setObjectName("label_receiver_3")
        self.gridLayout_11.addWidget(self.label_receiver_3, 2, 0, 1, 2)
        self.receiver_3 = QtWidgets.QLineEdit(self.equipment)
        self.receiver_3.setObjectName("receiver_3")
        self.gridLayout_11.addWidget(self.receiver_3, 2, 2, 1, 3)
        self.label_add_information_4 = QtWidgets.QLabel(self.equipment)
        self.label_add_information_4.setObjectName("label_add_information_4")
        self.gridLayout_11.addWidget(self.label_add_information_4, 5, 0, 1, 1)
        self.lidar_sn_3 = QtWidgets.QLineEdit(self.equipment)
        self.lidar_sn_3.setObjectName("lidar_sn_3")
        self.gridLayout_11.addWidget(self.lidar_sn_3, 0, 4, 1, 1)
        self.aircraft_5 = QtWidgets.QLineEdit(self.equipment)
        self.aircraft_5.setObjectName("aircraft_5")
        self.gridLayout_11.addWidget(self.aircraft_5, 4, 2, 1, 3)
        self.label_lidar_type_3 = QtWidgets.QLabel(self.equipment)
        self.label_lidar_type_3.setObjectName("label_lidar_type_3")
        self.gridLayout_11.addWidget(self.label_lidar_type_3, 0, 0, 1, 1)
        self.other_equipment_3 = QtWidgets.QLineEdit(self.equipment)
        self.other_equipment_3.setObjectName("other_equipment_3")
        self.gridLayout_11.addWidget(self.other_equipment_3, 3, 2, 1, 3)
        self.definition_block_3 = QtWidgets.QLineEdit(self.equipment)
        self.definition_block_3.setObjectName("definition_block_3")
        self.gridLayout_11.addWidget(self.definition_block_3, 1, 2, 1, 3)
        self.label_aircraft_3 = QtWidgets.QLabel(self.equipment)
        self.label_aircraft_3.setObjectName("label_aircraft_3")
        self.gridLayout_11.addWidget(self.label_aircraft_3, 4, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem2, 0, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.equipment)
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_afs_kml = QtWidgets.QLabel(self.frame)
        self.label_afs_kml.setObjectName("label_afs_kml")
        self.gridLayout_2.addWidget(self.label_afs_kml, 9, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 3, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 10, 1, 1, 1)
        self.button_analysis_kml = QtWidgets.QPushButton(self.frame)
        self.button_analysis_kml.setObjectName("button_analysis_kml")
        self.gridLayout_2.addWidget(self.button_analysis_kml, 10, 2, 1, 2)
        self.label_afs_txt = QtWidgets.QLabel(self.frame)
        self.label_afs_txt.setObjectName("label_afs_txt")
        self.gridLayout_2.addWidget(self.label_afs_txt, 2, 0, 1, 1)
        self.button_analysis_txt = QtWidgets.QPushButton(self.frame)
        self.button_analysis_txt.setObjectName("button_analysis_txt")
        self.gridLayout_2.addWidget(self.button_analysis_txt, 3, 2, 1, 2)
        self.button_choise_txt = QgsFileWidget(self.frame)
        self.button_choise_txt.setObjectName("button_choise_txt")
        self.gridLayout_2.addWidget(self.button_choise_txt, 2, 1, 1, 3)
        self.button_choise_kml = QgsFileWidget(self.frame)
        self.button_choise_kml.setObjectName("button_choise_kml")
        self.gridLayout_2.addWidget(self.button_choise_kml, 9, 1, 1, 3)
        self.verticalLayout_2.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_12.addWidget(self.scrollArea, 1, 0, 1, 3)
        self.save = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save.sizePolicy().hasHeightForWidth())
        self.save.setSizePolicy(sizePolicy)
        self.save.setObjectName("save")
        self.gridLayout_12.addWidget(self.save, 2, 2, 1, 1)
        self.label_passport_afs = QtWidgets.QLabel(self.centralwidget)
        self.label_passport_afs.setObjectName("label_passport_afs")
        self.gridLayout_12.addWidget(self.label_passport_afs, 0, 0, 1, 1)
        AerialPhotographyGUIDialogBase.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AerialPhotographyGUIDialogBase)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1038, 21))
        self.menubar.setObjectName("menubar")
        AerialPhotographyGUIDialogBase.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AerialPhotographyGUIDialogBase)
        self.statusbar.setObjectName("statusbar")
        AerialPhotographyGUIDialogBase.setStatusBar(self.statusbar)

        self.retranslateUi(AerialPhotographyGUIDialogBase)
        self.clear.clicked.connect(self.name_object_4.clear) # type: ignore
        self.clear.clicked.connect(self.overlap_longitudinal_4.clear) # type: ignore
        self.clear.clicked.connect(self.height_5.clear) # type: ignore
        self.clear.clicked.connect(self.pixel_size_5.clear) # type: ignore
        self.clear.clicked.connect(self.filming_location_4.clear) # type: ignore
        self.clear.clicked.connect(self.customer_4.clear) # type: ignore
        self.clear.clicked.connect(self.type_shoot_4.clear) # type: ignore
        self.clear.clicked.connect(self.area_afs_4.clear) # type: ignore
        self.clear.clicked.connect(self.length_afs_4.clear) # type: ignore
        self.clear.clicked.connect(self.overlap_transverse_4.clear) # type: ignore
        self.clear.clicked.connect(self.resolution_5.clear) # type: ignore
        self.clear.clicked.connect(self.coordinate_orientation_5.clear) # type: ignore
        self.clear.clicked.connect(self.definition_block_3.clear) # type: ignore
        self.clear.clicked.connect(self.add_information.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(AerialPhotographyGUIDialogBase)

    def retranslateUi(self, AerialPhotographyGUIDialogBase):
        _translate = QtCore.QCoreApplication.translate
        AerialPhotographyGUIDialogBase.setWindowTitle(_translate("AerialPhotographyGUIDialogBase", "Aerial Photography GUI"))
        self.clear.setText(_translate("AerialPhotographyGUIDialogBase", "Очистить поля"))
        self.label_name_object_4.setText(_translate("AerialPhotographyGUIDialogBase", "Название или шифр объекта съёмки"))
        self.nature_area_4.setItemText(0, _translate("AerialPhotographyGUIDialogBase", "Застроенная"))
        self.nature_area_4.setItemText(1, _translate("AerialPhotographyGUIDialogBase", "Не застроенная"))
        self.label_date_start_4.setText(_translate("AerialPhotographyGUIDialogBase", "Дата начала АФС"))
        self.label_orientation_route_4.setText(_translate("AerialPhotographyGUIDialogBase", "Ориентация маршрутов (широтная, меридиональная, заданная)"))
        self.label_filming_location_4.setText(_translate("AerialPhotographyGUIDialogBase", "Съёмочный участок"))
        self.label_overlap_transverse_4.setText(_translate("AerialPhotographyGUIDialogBase", "Поперечное перекрытие, %"))
        self.executor_4.setItemText(1, _translate("AerialPhotographyGUIDialogBase", "Котелевский К. А."))
        self.executor_4.setItemText(2, _translate("AerialPhotographyGUIDialogBase", "Ли В. Ю."))
        self.orientation_route_4.setItemText(1, _translate("AerialPhotographyGUIDialogBase", "Широтная"))
        self.orientation_route_4.setItemText(2, _translate("AerialPhotographyGUIDialogBase", "Меридиональная"))
        self.orientation_route_4.setItemText(3, _translate("AerialPhotographyGUIDialogBase", "Заданная"))
        self.label_customer_4.setText(_translate("AerialPhotographyGUIDialogBase", "Заказчик"))
        self.label_area_afs_4.setText(_translate("AerialPhotographyGUIDialogBase", "<html><head/><body><p>Фактическая площадь АФС, км<span style=\" vertical-align:super;\">2</span>, для АФС объекта площадного характера</p></body></html>"))
        self.label_date_end_4.setText(_translate("AerialPhotographyGUIDialogBase", "Дата окончания АФС"))
        self.label_overlap_longitudinal_4.setText(_translate("AerialPhotographyGUIDialogBase", "Продольное перекрытие, %"))
        self.label_nature_area_4.setText(_translate("AerialPhotographyGUIDialogBase", "Характер местности"))
        self.label_type_shoot_4.setText(_translate("AerialPhotographyGUIDialogBase", "Вид съёмки"))
        self.label_length_afs_4.setText(_translate("AerialPhotographyGUIDialogBase", "Фактическая протяжность АФС, км, для АФС линейного объекта"))
        self.label_executor_4.setText(_translate("AerialPhotographyGUIDialogBase", "Исполнитель АФС"))
        self.label_4.setText(_translate("AerialPhotographyGUIDialogBase", "Выбор камеры"))
        self.radioButton_5.setText(_translate("AerialPhotographyGUIDialogBase", "Sony RX1RM2"))
        self.radioButton_6.setText(_translate("AerialPhotographyGUIDialogBase", "Sony A6000"))
        self.label_api_sn_5.setText(_translate("AerialPhotographyGUIDialogBase", "Серийный номер аэрофотоустановки (гироплатформы)"))
        self.label_camera_sn_5.setText(_translate("AerialPhotographyGUIDialogBase", "Серийный номер аэрофотокамеры"))
        self.label_focal_len_5.setText(_translate("AerialPhotographyGUIDialogBase", "Фокусное расстояние аэрофотокамеры, мм"))
        self.label_long_shift_5.setText(_translate("AerialPhotographyGUIDialogBase", "Наличие и тип компенсации продольного сдвига изображения"))
        self.label_type_lens_5.setText(_translate("AerialPhotographyGUIDialogBase", "Тип и серийный номер объектива (если объектив заменяемый)"))
        self.focal_len_5.setText(_translate("AerialPhotographyGUIDialogBase", "20"))
        self.image_format_5.setText(_translate("AerialPhotographyGUIDialogBase", "ARW"))
        self.label_spectral_characteristics_photo_5.setText(_translate("AerialPhotographyGUIDialogBase", "Спектральная характеристика аэрофотоснимков"))
        self.type_lens_5.setText(_translate("AerialPhotographyGUIDialogBase", "Нет"))
        self.frame_size_x_5.setText(_translate("AerialPhotographyGUIDialogBase", "6000"))
        self.label_camera_model_5.setText(_translate("AerialPhotographyGUIDialogBase", "Модель аэрофотокамеры"))
        self.frame_size_y_5.setText(_translate("AerialPhotographyGUIDialogBase", "4000"))
        self.long_shift_5.setText(_translate("AerialPhotographyGUIDialogBase", "Нет"))
        self.label_api_type_5.setText(_translate("AerialPhotographyGUIDialogBase", "Тип аэрофотоустановки (гироплатформы)"))
        self.label_resolution_5.setText(_translate("AerialPhotographyGUIDialogBase", "Номинальное пространственное разрешение, м"))
        self.label_frame_size_y_5.setText(_translate("AerialPhotographyGUIDialogBase", "Размер кадра N(y) пикс"))
        self.camera_model_5.setText(_translate("AerialPhotographyGUIDialogBase", "Sony A6000"))
        self.api_type_5.setText(_translate("AerialPhotographyGUIDialogBase", "Нет"))
        self.label_coordinate_orientation_5.setText(_translate("AerialPhotographyGUIDialogBase", "Ориентация системы координат снимка"))
        self.label_frame_size_x_5.setText(_translate("AerialPhotographyGUIDialogBase", "Размер кадра N(x) пикс"))
        self.label_pixel_size_5.setText(_translate("AerialPhotographyGUIDialogBase", "Физический размер пикселя, мм"))
        self.spectral_characteristics_photo_5.setText(_translate("AerialPhotographyGUIDialogBase", "NIR"))
        self.label_image_format_5.setText(_translate("AerialPhotographyGUIDialogBase", "Формат представления цифрового изображения"))
        self.api_sn_5.setText(_translate("AerialPhotographyGUIDialogBase", "Нет"))
        self.camera_sn_5.setText(_translate("AerialPhotographyGUIDialogBase", "Нет"))
        self.label_height_5.setText(_translate("AerialPhotographyGUIDialogBase", "Высота фотографирования, м"))
        self.label_other_equipment_3.setText(_translate("AerialPhotographyGUIDialogBase", "Прочая аппаратура"))
        self.lidar_type_3.setText(_translate("AerialPhotographyGUIDialogBase", "Нет"))
        self.label_lidar_sn_3.setText(_translate("AerialPhotographyGUIDialogBase", "Лидар, серийный номер"))
        self.label_definition_block_3.setText(_translate("AerialPhotographyGUIDialogBase", "Блок определения положения и ориентации, тип, модель, состав"))
        self.label_receiver_3.setText(_translate("AerialPhotographyGUIDialogBase", "ГНСС-приёмник, тип, модель"))
        self.receiver_3.setText(_translate("AerialPhotographyGUIDialogBase", "Topcon OEM"))
        self.label_add_information_4.setText(_translate("AerialPhotographyGUIDialogBase", "Дополнительные сведения по требованию ТЗ"))
        self.lidar_sn_3.setText(_translate("AerialPhotographyGUIDialogBase", "Нет"))
        self.aircraft_5.setText(_translate("AerialPhotographyGUIDialogBase", "Геоскан 201 Агрогеодезия"))
        self.label_lidar_type_3.setText(_translate("AerialPhotographyGUIDialogBase", "Лидар (тип)"))
        self.other_equipment_3.setText(_translate("AerialPhotographyGUIDialogBase", "Нет"))
        self.label_aircraft_3.setText(_translate("AerialPhotographyGUIDialogBase", "Воздушное судно"))
        self.label_afs_kml.setText(_translate("AerialPhotographyGUIDialogBase", "Файл KML"))
        self.button_analysis_kml.setText(_translate("AerialPhotographyGUIDialogBase", "Анализировать файл.kml"))
        self.label_afs_txt.setText(_translate("AerialPhotographyGUIDialogBase", "Список номеров концевых списков маршрутов (файл формата .txt послеполётной обработки АФС)"))
        self.button_analysis_txt.setText(_translate("AerialPhotographyGUIDialogBase", "Анализировать файл.txt"))
        self.save.setText(_translate("AerialPhotographyGUIDialogBase", "Выгрузить форму"))
        self.label_passport_afs.setText(_translate("AerialPhotographyGUIDialogBase", "<html><head/><body><p><span style=\" font-weight:600;\">Паспорт аэрофотосъёмки</span></p></body></html>"))
from qgsfilewidget import QgsFileWidget
