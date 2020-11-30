# -*- coding: utf-8 -*-
# Copyright (C) 2019-2020 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
import pytest


class TestDemosWindows:
    @pytest.mark.parametrize('is_distribution', ['dev', 'proprietary'], indirect=True)
    @pytest.mark.parametrize('is_image_os', ['winserver2019'], indirect=True)
    def test_security_cpu(self, is_distribution, is_image_os):
        kwargs = {'user': 'ContainerAdministrator'}
        self.tester.test_docker_image(
            self.image,
            ['cmd /S /C cd C:\\\\intel\\\\openvino\\\\deployment_tools\\\\demo\\\\ && '
             'demo_security_barrier_camera.bat -d CPU -sample-options -no_show'],
            self.test_security_cpu.__name__, **kwargs,
        )

    @pytest.mark.parametrize('is_distribution', ['dev', 'proprietary'], indirect=True)
    @pytest.mark.parametrize('is_image_os', ['winserver2019'], indirect=True)
    @pytest.mark.xfail(reason='39822 issue')
    def test_squeezenet_cpu(self, is_distribution, is_image_os):
        kwargs = {'user': 'ContainerAdministrator'}
        self.tester.test_docker_image(
            self.image,
            ['cmd /S /C cd C:\\\\intel\\\\openvino\\\\deployment_tools\\\\demo\\\\ && '
             'demo_squeezenet_download_convert_run.bat -d CPU'],
            self.test_squeezenet_cpu.__name__, **kwargs,
        )

    @pytest.mark.parametrize('is_distribution', ['dev', 'proprietary'], indirect=True)
    @pytest.mark.parametrize('is_image_os', ['winserver2019'], indirect=True)
    def test_crossroad_cpp_cpu(self, is_distribution, is_image_os):
        kwargs = {'user': 'ContainerAdministrator', 'mem_limit': '3g'}
        self.tester.test_docker_image(
            self.image,
            ['cmd /S /C C:\\\\intel\\\\openvino\\\\bin\\\\setupvars.bat && '
             'C:\\\\intel\\\\openvino\\\\deployment_tools\\\\open_model_zoo\\\\demos\\\\build_demos_msvc.bat',
             'cmd /S /C C:\\\\intel\\\\openvino\\\\bin\\\\setupvars.bat && '
             'python C:\\\\intel\\\\openvino\\\\deployment_tools\\\\open_model_zoo\\\\tools\\\\'
             'downloader\\\\downloader.py '
             '--name person-vehicle-bike-detection-crossroad-0078 --precisions FP16 '
             '-o C:\\\\Users\\\\ContainerAdministrator\\\\Documents\\\\Intel\\\\OpenVINO\\\\'
             'omz_demos_build\\\\intel64\\\\Release\\\\',
             'cmd /S /C C:\\\\intel\\\\openvino\\\\bin\\\\setupvars.bat && '
             'C:\\\\Users\\\\ContainerAdministrator\\\\Documents\\\\Intel\\\\OpenVINO\\\\'
             'omz_demos_build\\\\intel64\\\\Release\\\\crossroad_camera_demo '
             '-m C:\\\\Users\\\\ContainerAdministrator\\\\Documents\\\\Intel\\\\OpenVINO\\\\'
             'omz_demos_build\\\\intel64\\\\Release\\\\intel\\\\'
             'person-vehicle-bike-detection-crossroad-0078\\\\FP16\\\\person-vehicle-bike-detection-crossroad-0078.xml '
             '-i C:\\\\intel\\\\openvino\\\\deployment_tools\\\\demo\\\\car_1.bmp -d CPU -no_show',
             ],
            self.test_crossroad_cpp_cpu.__name__, **kwargs,
        )

    @pytest.mark.parametrize('is_distribution', ['dev', 'proprietary'], indirect=True)
    @pytest.mark.parametrize('is_image_os', ['winserver2019'], indirect=True)
    def test_text_cpp_cpu(self, is_distribution, is_image_os):
        kwargs = {'user': 'ContainerAdministrator', 'mem_limit': '3g'}
        self.tester.test_docker_image(
            self.image,
            ['cmd /S /C C:\\\\intel\\\\openvino\\\\bin\\\\setupvars.bat && '
             'C:\\\\intel\\\\openvino\\\\deployment_tools\\\\open_model_zoo\\\\demos\\\\build_demos_msvc.bat',
             'cmd /S /C C:\\\\intel\\\\openvino\\\\bin\\\\setupvars.bat && '
             'python C:\\\\intel\\\\openvino\\\\deployment_tools\\\\open_model_zoo\\\\tools\\\\'
             'downloader\\\\downloader.py '
             '--name text-detection-0004 --precision FP16 -o C:\\\\Users\\\\ContainerAdministrator\\\\'
             'Documents\\\\Intel\\\\OpenVINO\\\\omz_demos_build\\\\intel64\\\\Release\\\\',
             'cmd /S /C C:\\\\intel\\\\openvino\\\\bin\\\\setupvars.bat && '
             'C:\\\\Users\\\\ContainerAdministrator\\\\Documents\\\\Intel\\\\OpenVINO\\\\'
             'omz_demos_build\\\\intel64\\\\Release\\\\text_detection_demo '
             '-m_td C:\\\\Users\\\\ContainerAdministrator\\\\Documents\\\\Intel\\\\OpenVINO\\\\'
             'omz_demos_build\\\\intel64\\\\Release\\\\intel\\\\'
             'text-detection-0004\\\\FP16\\\\text-detection-0004.xml '
             '-i C:\\\\intel\\\\openvino\\\\deployment_tools\\\\demo\\\\car_1.bmp -d_td CPU -no_show',
             ],
            self.test_text_cpp_cpu.__name__, **kwargs,
        )

    @pytest.mark.parametrize('is_distribution', ['dev', 'proprietary'], indirect=True)
    @pytest.mark.parametrize('is_image_os', ['winserver2019'], indirect=True)
    @pytest.mark.xfail(reason='38545 issue')
    def test_detection_ssd_python_cpu(self, is_distribution, is_image_os):
        kwargs = {'user': 'ContainerAdministrator'}
        self.tester.test_docker_image(
            self.image,
            ['cmd /S /C C:\\\\intel\\\\openvino\\\\bin\\\\setupvars.bat && '
             'python C:\\\\intel\\\\openvino\\\\deployment_tools\\\\open_model_zoo\\\\tools\\\\'
             'downloader\\\\downloader.py '
             '--name vehicle-detection-adas-0002 --precision FP16',
             'cmd /S /C C:\\\\intel\\\\openvino\\\\bin\\\\setupvars.bat && '
             'python C:\\\\intel\\\\openvino\\\\deployment_tools\\\\open_model_zoo\\\\demos\\\\'
             'python_demos\\\\object_detection_demo_ssd_async\\\\object_detection_demo_ssd_async.py '
             '-m C:\\\\intel\\\\openvino\\\\intel\\\\vehicle-detection-adas-0002\\\\FP16\\\\'
             'vehicle-detection-adas-0002.xml '
             '-i C:\\\\intel\\\\openvino\\\\deployment_tools\\\\demo\\\\car_1.bmp -d CPU --no_show',
             ],
            self.test_detection_ssd_python_cpu.__name__, **kwargs,
        )

    @pytest.mark.parametrize('is_distribution', ['dev', 'proprietary'], indirect=True)
    @pytest.mark.parametrize('is_image_os', ['winserver2019'], indirect=True)
    def test_segmentation_cpp_cpu(self, is_distribution, is_image_os):
        kwargs = {'user': 'ContainerAdministrator', 'mem_limit': '3g'}
        self.tester.test_docker_image(
            self.image,
            ['cmd /S /C C:\\\\intel\\\\openvino\\\\bin\\\\setupvars.bat && '
             'C:\\\\intel\\\\openvino\\\\deployment_tools\\\\open_model_zoo\\\\demos\\\\build_demos_msvc.bat',
             'cmd /S /C C:\\\\intel\\\\openvino\\\\bin\\\\setupvars.bat && '
             'python C:\\\\intel\\\\openvino\\\\deployment_tools\\\\open_model_zoo\\\\tools\\\\'
             'downloader\\\\downloader.py '
             '--name semantic-segmentation-adas-0001 --precision FP16 -o C:\\\\Users\\\\'
             'ContainerAdministrator\\\\Documents\\\\Intel\\\\OpenVINO\\\\'
             'omz_demos_build\\\\intel64\\\\Release\\\\',
             'cmd /S /C C:\\\\intel\\\\openvino\\\\bin\\\\setupvars.bat && '
             'C:\\\\Users\\\\ContainerAdministrator\\\\Documents\\\\Intel\\\\OpenVINO\\\\'
             'omz_demos_build\\\\intel64\\\\Release\\\\segmentation_demo '
             '-m C:\\\\Users\\\\ContainerAdministrator\\\\Documents\\\\Intel\\\\OpenVINO\\\\'
             'omz_demos_build\\\\intel64\\\\Release\\\\intel\\\\semantic-segmentation-adas-0001\\\\'
             'FP16\\\\semantic-segmentation-adas-0001.xml '
             '-i C:\\\\intel\\\\openvino\\\\deployment_tools\\\\demo\\\\car_1.bmp -d CPU -no_show',
             ],
            self.test_segmentation_cpp_cpu.__name__, **kwargs,
        )

    @pytest.mark.parametrize('is_distribution', ['dev', 'proprietary'], indirect=True)
    @pytest.mark.parametrize('is_image_os', ['winserver2019'], indirect=True)
    def test_segmentation_python_cpu(self, is_distribution, is_image_os):
        kwargs = {'user': 'ContainerAdministrator'}
        self.tester.test_docker_image(
            self.image,
            ['cmd /S /C C:\\\\intel\\\\openvino\\\\bin\\\\setupvars.bat && '
             'python C:\\\\intel\\\\openvino\\\\deployment_tools\\\\open_model_zoo\\\\tools\\\\'
             'downloader\\\\downloader.py '
             '--name semantic-segmentation-adas-0001 --precision FP16',
             'cmd /S /C C:\\\\intel\\\\openvino\\\\bin\\\\setupvars.bat && '
             'python C:\\\\intel\\\\openvino\\\\deployment_tools\\\\open_model_zoo\\\\demos\\\\'
             'python_demos\\\\segmentation_demo\\\\segmentation_demo.py '
             '-m C:\\\\intel\\\\openvino\\\\intel\\\\semantic-segmentation-adas-0001\\\\FP16\\\\'
             'semantic-segmentation-adas-0001.xml '
             '-i C:\\\\intel\\\\openvino\\\\deployment_tools\\\\demo\\\\car_1.bmp -d CPU',
             ],
            self.test_segmentation_python_cpu.__name__, **kwargs,
        )

    @pytest.mark.parametrize('is_distribution', ['dev', 'proprietary'], indirect=True)
    @pytest.mark.parametrize('is_image_os', ['winserver2019'], indirect=True)
    def test_object_detection_centernet_python_cpu(self, is_distribution, is_image_os):
        kwargs = {'user': 'ContainerAdministrator'}
        self.tester.test_docker_image(
            self.image,
            ['cmd /S /C C:\\\\intel\\\\openvino\\\\bin\\\\setupvars.bat && '
             'python C:\\\\intel\\\\openvino\\\\deployment_tools\\\\open_model_zoo\\\\tools\\\\'
             'downloader\\\\downloader.py '
             '--name ctdet_coco_dlav0_384 --precision FP16',
             'cmd /S /C C:\\\\intel\\\\openvino\\\\bin\\\\setupvars.bat && '
             'python C:\\\\intel\\\\openvino\\\\deployment_tools\\\\open_model_zoo\\\\tools\\\\'
             'downloader\\\\converter.py '
             '--name ctdet_coco_dlav0_384 --precision FP16',
             'cmd /S /C C:\\\\intel\\\\openvino\\\\bin\\\\setupvars.bat && '
             'python C:\\\\intel\\\\openvino\\\\deployment_tools\\\\open_model_zoo\\\\demos\\\\'
             'python_demos\\\\object_detection_demo_centernet\\\\object_detection_demo_centernet.py '
             '-m C:\\\\intel\\\\openvino\\\\public\\\\ctdet_coco_dlav0_384\\\\FP16\\\\ctdet_coco_dlav0_384.xml '
             '-i C:\\\\intel\\\\openvino\\\\deployment_tools\\\\demo\\\\car_1.bmp -d CPU --no_show',
             ],
            self.test_object_detection_centernet_python_cpu.__name__, **kwargs,
        )
